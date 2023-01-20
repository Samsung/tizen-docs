# Image Editing


Tizen offers various image processing features.

The main features of the ImageUtil API include the following:

- Converting

  You can change the [image color space](#image_colorspace) among the [supported formats](#color_format).

- Resizing

  You can change the [image resolution](#resize_image).

- Rotating

  You can change the [image angle](#rotate_image) around the X or Y axis.

- Cropping

  You can [crop the outer parts of the image](#crop_image).

- Decoding or encoding from a file or memory and encoding to a file or memory

  You can [decode images](#decode) and [encode them](#encode) with the following formats:

  - Bitmap formats: YUV420, YUV422, RGB888, RGBA8888, BGRA8888, and ARGB8888
  - Input image formats for decoding: JPEG, PNG, GIF, BMP, WEBP, HEIF, and JPEG XL
  - Output image formats for encoding: JPEG, PNG, GIF, BMP, WEBP, and JPEG XL

  > [!NOTE]
  > You must pay attention to how the [image quality depends on the size](#quality) and compression ratio.

## Prerequisites

To enable your application to use the image util functionality, follow these steps:

1. To find out the color spaces supported on the device, use `ImageUtil.GetSupportedColorSpaces()`:

   ```csharp
   foreach (var colorSpace in ImageUtil.GetSupportedColorSpaces(ImageFormat.Jpeg))
   {
      ...
   }

   or

   var colorSpace = ImageUtil.GetSupportedColorSpaces(ImageFormat.Jpeg);
   ```

   The supported color space will be one of the `Tizen.Multimedia.ColorSpace` enumeration.

2. To transform image, create `ImageTransformer` and `MediaPacket` for image source:
   ```csharp
   var imageTransformer = new ImageTransformer();
   var packet = MediaPacket.Create(new VideoMediaFormat(MediaFormatVideoMimeType.I420, 640, 480));
   ```

<a name="image_colorspace"></a>
## Convert image color space

To convert one color space of an image to another, follow these steps:

1. Create a `ColorSpaceTransform` instance:

   ```csharp
   var colorSpaceTransform = new ColorSpaceTransform(ColorSpace.I420);
   ```

   or, the color space of target image can be set by `ColorSpace` property after `ColorSpaceTransform` is created.

   ```csharp
   colorSpaceTransform.ColorSpace = ColorSpace.NV12;
   ```

2. Execute the transformation using `TransformAsync()` of `ImageTransformer` class:

   ```csharp
   var resultMediaPacket = await imageTransformer.TransformAsync(packet, colorSpaceTransform);
   ```

   > [!NOTE]
   > `TransformAsync` using `ColorSpaceTransform` only converts the color space. These functions do not change the image width, height, or any other image property. Due to these restrictions of the image processing library, not all color space combinations are supported for conversion.

<a name="resize_image"></a>
## Resize image

To resize an image, follow these steps:

1. Create a `ResizeTransform` instance:

   ```csharp
   var resizeTransform = new ResizeTransform(new Size(320, 240));
   ```

   or, the size of target image can be set by `Size` property after `ResizeTransform` is created.

   ```csharp
   resizeTransform.Size = new Size(1280, 730);
   ```

2. Execute the transformation using `TransformAsync()` of `ImageTransformer` class:

   ```csharp
   var resultMediaPacket = await imageTransformer.TransformAsync(packet, resizeTransform);
   ```

   > [!NOTE]
   > The image format has no effect on the transformation. If the color space is YUV, then the width and height of the target image must be multiples of eight. This restriction does not apply to the RGB images.

<a name="rotate_image"></a>
## Rotate image

To rotate an image, follow these steps:

1. Create a `RotateTransform` instance:

   ```csharp
   var rotateTransform = new RotateTransform(Rotation.Rotate90);
   ```

   or, the rotation of target image can be set by `Rotation` property after `RotateTransform` is created.

   ```csharp
   rotateTransform.Rotation = Rotation.Rotate180;
   ```

2. Execute the transformation using `TransformAsync()` of `ImageTransformer` class:

   ```csharp
   var resultMediaPacket = await imageTransformer.TransformAsync(packet, rotateTransform);
   ```

   > [!NOTE]
   > The image format has no effect on the transformation. If the color space is YUV, then the width and height of the target image must be multiples of eight. This restriction does not apply to the RGB images.

<a name="crop_image"></a>
## Crop image

To crop an image, follow these steps:

1. Create a `CropTransform` instance:

   ```csharp
   var cropTransform = new CropTransform(new Rectangle(0, 0, 100, 100));
   ```

   or, the area to be cropped can be set by `Location` or `Size` property after `CropTransform` is created.

   ```csharp
   cropTransform.Location = new Point(10, 10);
   cropTransform.Size = new Size(200, 200);
   ```

2. Execute the transformation using `TransformAsync()` of `ImageTransformer` class:

   ```csharp
   var resultMediaPacket = await imageTransformer.TransformAsync(packet, cropTransform);
   ```

   > [!NOTE]
   > As there is a YUV restriction and the crop start position can be set arbitrarily, the cropped image width and height must be even.


<a name="decode"></a>
## Decode from a file or memory

To decode a JPEG, PNG, GIF, BMP, WEBP, HEIF, or JPEG XL image, follow these steps:

1. Create a decoder instance as image format:

   ```csharp
   var bmpDecoder = new BmpDecoder();
   ```
   or
   ```csharp
   var pngDecoder = new PngDecoder();
   ```
   or
   ```csharp
   var jpegDecoder = new JpegDecoder();
   ```
   or
   ```csharp
   var gifDecoder = new GifDecoder();
   ```
   or
   ```csharp
   var webPDecoder = new WebPDecoder();
   ```
   or
   ```csharp
   var heifDecoder = new HeifDecoder();
   ```
   or
   ```csharp
   var jpegXlDecoder = new JpegXlDecoder();
   ```
   ```

2. Additionally, you can set the color space and JPEG downscale using `SetColorSpace()` method and `Downscale` property:

   ```csharp
   jpegDecoder.SetColorSpace(ColorSpace.NV12);
   jpegDecoder.Downscale = JpegDownscale.OneHalf;
   ```

   > [!NOTE]
   > Due to the decoder limitations, the color space setting is only supported for decoding the JPEG, the WEBP, the HEIF, and the JPEG XL images.
   > The default color space is `ColorSpace.Rgba8888`.
   > PNG, GIF, and BMP images are decoded with `ColorSpace.Rgba8888`.

4. Execute the decoding using `DecodeAsync()`:

   ```csharp
   var result = await jpegDecoder.DecodeAsync("input_file_path");
   ```
   or
   ```csharp
   var sourceImage = new byte[100];
   // set source image to sourceImage buffer
   var result = await jpegDecoder.DecodeAsync(sourceImage);
   ```

<a name="encode"></a>
## Encode to a file or memory

To encode a raw image, follow these steps:

1. Create an encoder instance as target image format:

   ```csharp
   var bmpEncoder = new BmpEncoder();

   ```
   or
   ```csharp
   var pngEncoder = new PngEncoder();
   var pngEncoder = new PngEncoder(PngCompression.Level1);

   ```
   or
   ```csharp
   var jpegEncoder = new JpegEncoder();
   var jpegEncoder = new JpegEncoder(95);

   ```
   or
   ```csharp
   var gifEncoder = new GifEncoder();

   ```
   or
   ```csharp
   var webPEncoder = new WebPEncoder();
   var webPEncoder = new WebPEncoder(true);

   ```
   or
   ```csharp
   var jpegXlEncoder = new JpegXlEncoder();
   var jpegXlEncoder = new JpegXlEncoder(true);

   ```

2. Additionally, you can set the JPEG quality or PNG compression using `Quality` or `Compression` property:

   ```csharp
   jpegEncoder.Quality = 90;
   ```
   ```csharp
   pngEncoder.Compression = PngCompression.Level3;
   ```

   > [!NOTE]
   > The compression is only supported for the PNG images. The default JPEG quality is 75. The default PNG compression is `PngCompression.Level6`.

3. Execute the encoding using `EncodeAsync()`:

   ```csharp
   var inputImage = new byte[100];
   // set source image to encode

   using (FileStream outStream = File.Create("output_path"))
   {
      await jpegEncoder.EncodeAsync(inputImage, outStream);
   }

   ```

   > [!NOTE]
   > Due to the encoder limitations, the color space setting is only supported for encoding the JPEG, the WEBP, and the JPEG XL images.
   > The default color space is `ColorSpace.Rgba8888`.
   > PNG, GIF, and BMP images are encoded with `ColorSpace.Rgba8888`.

<a name="color_format"></a>
## Supported color space formats

The following tables define the supported color space formats.

**Table: RGB pixel formats**

| Label                                    | FOURCC in hex | Bits per pixel      | Description                              |
|------------------------------------------|---------------|---------------------|------------------------------------------|
| RGB | 0x32424752    | 1, 4, 8, 16, 24, 32 | Alias for BI_RGB.                         |
| RGBA | 0x41424752    | 16, 32              | Raw RGB with alpha. Sample precision and packing is arbitrary and determined using bit masks for each component, as for BI_BITFIELDS. |

**Table: Packed YUV formats**

| Label                                    | FOURCC in hex | Bits per pixel | Description                              |
|------------------------------------------|---------------|----------------|------------------------------------------|
| UYVY | 0x59565955    | 16             | YUV 4:2:2 (Y sample at every pixel, U and V sampled at every second pixel horizontally on each line). A macropixel contains 2 pixels in 1 u_int32. |
| YUYV | 0x56595559    | 16             | Duplicate of YUY2.                       |

**Table: Planar YUV formats**

| Label                                    | FOURCC in hex | Bits per pixel | Description                              |
|------------------------------------------|---------------|----------------|------------------------------------------|
| YV16 | 0x36315659    | 16             | 8-bit Y plane followed by 8-bit 2x1 subsampled V and U planes. |
| YV12 | 0x32315659    | 12             | 8-bit Y plane followed by 8-bit 2x2 subsampled V and U planes. |
| I420 | 0x30323449    | 12             | 8-bit Y plane followed by 8-bit 2x2 subsampled U and V planes. |
| NV12 | 0x3231564E    | 12             | 8-bit Y plane followed by an interleaved U/V plane with 2x2 subsampling. |
| NV21 | 0x3132564E    | 12             | As NV12 with U and V reversed in the interleaved plane. |

<a name="quality"></a>
## Quality and size comparison

The following table shows the effect on the image quality and file sizes when using different compression ratios.

**Table: Quality and size comparison**

| Image                                    | Quality                   | Size (bytes) | Compression ratio | Description                              |
|------------------------------------------|---------------------------|--------------|-------------------|------------------------------------------|
| ![Highest quality image](./media/quality_highest.png) | Highest quality (Q = 100) | 83,261       | 2.6:1             | Extremely minor artifacts                |
| ![High quality image](./media/quality_high.png) | High quality (Q = 50)     | 15,138       | 15:1              | Initial signs of subimage artifacts      |
| ![Medium quality image](./media/quality_medium.png) | Medium quality (Q = 25)   | 9,553        | 23:1              | Stronger artifacts; loss of high-frequency information |
| ![Low quality image](./media/quality_low.png) | Low quality (Q = 10)      | 4,787        | 46:1              | Severe high frequency loss; artifacts on subimage boundaries ("macroblocking") are obvious |
| ![Lowest quality image](./media/quality_lowest.png) | Lowest quality            | -             | -                  |  -                                        |

## Related information
- Dependencies
  -   Tizen 4.0 and Higher
