# Resources

NUI provides several ways to handle resource images.
This tutorial describes the use of Image resources in NUI.

## Overview

Resources in NUI can apply Images or 3D Models.

The common method to access these resources is through Visuals.
Controls use these visuals to display what is required.

See [ImageView tutorial](imageview.md).

## Loading images

Images are defined by an url which can be local or remote (internet).
The following formats are supported :

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
| `AlphaMaskURL`       | url to an image that will mask the main content image. |
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
| `BorderOnly`         | Specifies if ONLY borders to be shown for N-Patch images. |

### Animated GIF only properties

| Property Name | Description       |
|---------------|-------------------|
| `BatchSize`   | Number of Images to decode before animation starts, Default is 1. |
| `CacheSize`   | Number of images to keep cached, Can increase or decrease depending on memory available. |
| `FrameDelay`  | Millisecond delay between frames. |

Synchronous loading has niche uses, eg. ensuring image has loaded before continuing to execute application code,
the common use is to connect to the control's `ResourceReady` and perform operations at that point.

## Reducing Image memory footprint

An application that loads images can also display images at a lower resolution than their native resolution.

To support this, DALi can resize an image at load time so that its in-memory copy uses less space and its visual quality benefits from being prefiltered.
`DesiredWidth` and `DesiredHeight` can be set to the Image visual and then `FittingMode`.

The `FittingMode` namespace provides 4 algorithms, which can be used to fit an image to a desired rectangle, a desired width, or a desired height.

The `FittingMode` and suggested use cases are as follows:

| Fitting mode 	| Suggested use case |
| ------------- | ------------------ |
| `ShrinkToFit` |	Fit full image inside desired width & height, potentially not filling one of either the desired image width or height with pixels. |
| `ScaleToFill` |	The image is centered in the desired dimensions, exactly touching in one dimension, with image regions outside the other desired dimension cropped. |
| `FitWidth`    |	Image fills whole width. Height is scaled proportionately to maintain aspect ratio. |
| `FitHeight`   | Image fills whole height. Width is scaled proportionately to maintain aspect ratio. |

## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
