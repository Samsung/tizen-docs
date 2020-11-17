# Resources

NUI provides several ways to handle resource images.
This tutorial describes the use of Image resources in NUI.

## Image handling methods

The two basic methods of handling image resources in NUI are as follows:
 
* `Visuals`: For more details, see [Visuals tutorial](visuals.md) page.

```
//Define unique visual index.
const int IMAGE_VISUAL_INDEX = 100001;

//Create property map
PropertyMap imagePropertyMap = new PropertyMap();
imageVisual.Add(Visual.Property.Type, new PropertyValue((int)Visual.Type.Image))
           .Add(ImageVisualProperty.URL, new PropertyValue(_imageURL));

// Setup size of image visual
PropertyMap imageVisualTransform = new PropertyMap();
imageVisualTransform.Add((int)VisualTransformPropertyType.Offset, new PropertyValue(new Vector2(10, 10)))
                    .Add((int)VisualTransformPropertyType.OffsetPolicy, new PropertyValue(new Vector2((int)VisualTransformPolicyType.Absolute, (int)VisualTransformPolicyType.Absolute)))
                    .Add((int)VisualTransformPropertyType.SizePolicy, new PropertyValue(new Vector2((int)VisualTransformPolicyType.Absolute, (int)VisualTransformPolicyType.Absolute)))
                    .Add((int)VisualTransformPropertyType.Size, new PropertyValue(new Vector2(200, 200)))
                    .Add((int)VisualTransformPropertyType.Origin, new PropertyValue((int)Visual.AlignType.CenterBegin))
                    .Add((int)VisualTransformPropertyType.AnchorPoint, new PropertyValue((int)Visual.AlignType.CenterBegin));
                    
imageVisual.SetTransformAndSize(imageVisualTransform, new Vector2(this.SizeWidth, this.SizeHeight));

//Create and register image visual.
VisualBase imageVisual = VisualFactory.Instance.CreateVisual(map);
RegisterVisual(IMAGE_VISUAL_INDEX, imageVisual);

/// Set the image visual depth index
imageVisual.DepthIndex = IMAGE_VISUAL_INDEX;
```
* Load image resource in Image `Component`: For more information, see  [ImageView tutorial](imageview.md) page.

```
Window window = Window.Instance;

ImageView background = new ImageView(DirectoryInfo.Resource + "/images/bg.png");
background.Size2D = new Size2D(window.Size.Width, window.Size.Height);
window.Add(background);
```

## Loading images

Images are defined by an URL which can be local or remote (internet).
The following formats are supported:

| Supported image formats | extentsion |
|------------------------ | ---------- |
| Bitmap                  | `.bmp`     |
| Gif                     | `.gif`     |
| Jpeg                    | `.jpeg`    |
| Khronos Texture         | `.ktx`     |
| PNG                     | `.png`     |
| Mircosoft Icons         | `.ico`     |
| WAP Bitmap              | `.wbmp`    |

Controls should process the provided URL and internally create the matching Image Visual.
Visual creation automatically determines whether the image is N_PATCH, SVG, or GIF, which is not a regular image from the image data.

### Image Properties

| Property Name        | Description       |
|----------------------|-------------------|
| `AlphaMaskURL`       | URL to an image that will mask the main content image. |
| `CropToMask`         | Flag to determine if main content image should crop to match mask size. |
| `FittingMode`        | By default the image will shrink to fit the DesiredHeight and DesiredWidth, other modes available. |
| `SamplingMode`       | The type of sampling to be used. Default is Box. |
| `DesiredWidth`       | The width you would like the Image to be.  Affected by FittingMode.       |
| `DesiredHeight`      | The height you would like the Image to be. Affected by FittingMode.       |
| `SynchronousLoading` | If loading should block the execution thread, disabled by Default.        |
| `PixelArea`          | Can be set to display only a portion of the Image.           |
| `WrapModeU`          | Define how sampling should behave for u coordinate. |
| `WrapModeV`          | Define how sampling should behave for v coordinate. |


### N-Patch only properties

| Property Name        | Description       |
|----------------------|-------------------|
| `Border`             | Specifies border values for N-Patch images. |
| `BorderOnly`         | Specifies if only borders to be shown for N-Patch images. |

### Animated GIF only properties

| Property Name | Description       |
|---------------|-------------------|
| `BatchSize`   | Number of Images to decode before animation starts, Default is one. |
| `CacheSize`   | Number of images to keep cached, can increase or decrease depending on memory available. |
| `FrameDelay`  | Millisecond delay between frames. |

Synchronous loading has niche uses, for example, ensure image has loaded before continuing to execute application code,
the common use is to connect to the control's `ResourceReady` and perform operations at that point.

## Reducing image memory footprint

An application that loads images can also display images at a lower resolution than their native resolution.

To support this, DALi can resize an image at load time so that its in-memory copy uses less space and its visual quality benefits from being prefiltered.

The `FittingMode` namespace provides four algorithms, which can be used to fit an image to a desired rectangle, a desired width, or a desired height.

The fitting modes and suggested use cases are as follows:

| Fitting mode 	| Suggested use case |
| ------------- | ------------------ |
| `ShrinkToFit` | Full screen image display: limit the loaded image resolution to the device resolution, but show all of the image. |
| `ScaleToFill` | Thumbnail gallery grid: limit the loaded image resolution to the screen tile, filling the whole tile but losing a few pixels to match the tile shape. |
| `FitWidth`    | Image columns: limit the loaded image resolution to the column width. |
| `FitHeight`   | Image rows: limit the loaded image resolution to the row height. |

## Related Information
- Dependencies
  -   Tizen 4.0 and Higher
