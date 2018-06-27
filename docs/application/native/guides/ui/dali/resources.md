# Resources


DALi provides several ways to handle resource images.
This tutorial describes the use of Resources in Dali, currently Image resources.

## Overview

Resources in Dali can apply Images or 3D Models.

The common method to access these resources is through Visuals.
Controls then use these visuals to display what is required.

See [ImageView tutorial](imageview.md).

## Loading images

Images are defined by an url which can be local or remote (internet).
The following formats are supported :

| Supported image formats | extentsion |
|-------------------------|------------|
| Bitmap                  | `.bmp`     |
| Gif                     | `.gif`     |
| Jpeg                    | `.jpeg`    |
| Khronos Texture         | `.ktx`     |
| PNG                     | `.png`     |
| Mircosoft Icons         | `.ico`     |
| WAP Bitmap              | `.wbmp`    |

Controls should process the provided url and internally create the matching Image visual.
Visual creation will automatically determine if the Image is an N_PATCH, SVG, GIF not regular image from the image data.

### Image Properties

| Property Name         | Description       |
|-----------------------|-------------------|
| `ALPHA_MASK_URL`      | url to an image that will mask the main content image |
| `CROP_TO_MASK`        | Flag to determine if main content image should crop to match mask size |
| `FITTING_MODE`        | By default the image will shrink to fit the desiredHeight and desiredWidth, other modes available |
| `SAMPLING_MODE`       | The type of sampling to be used. Default is Box. |
| `DESIRED_WIDTH`       | The width you would like the Image to be.  Affected by FITTING_MODE        |
| `DESIRED_HEIGHT`      | The height you would like the Image to be. Affected by FITTING_MOD         |
| `SYNCHRONOUS_LOADING` | If loading should block the execution thread, disabled by Default.         |
| `PIXEL_AREA`          | Can be set to display only a portion of the Image           |
| `WRAP_MODE_U`         | Define how sampling should behave for u coordinate |
| `WRAP_MODE_V`         | Define how sampling should behave for v coordinate |
| `ATLASING`            | Whether to use the texture atlas to speed up loading times, enabled by default |

### N-Patch only properties

| Property Name         | Description       |
|-----------------------|-------------------|
| `BORDER`              | Specifies border values for N-Patch images |
| `BORDER_ONLY`         | Specifies if ONLY borders to be shown for N-Patch images |

### Animated GIF only properties

| Property Name | Description       |
|---------------|-------------------|
| `BATCH_SIZE`  | Number of Images to decode before animation starts, Default is 1. |
| `CACHE_SIZE`  | Number of images to keep cached, Can increase or decrease depending on memory available. |
| `FRAME_DELAY` | Millisecond delay between frames |

Synchronous loading has niche uses, eg. ensuring image has loaded before continuing to execute application code,
the common use is to connect to the control's `ResourceReadySignal` and perform operations at that point.

## Caching

Images are automatically cached, if the `ATLASING` is not disable then may be in an Atlas too.

If an Image (ImageVisual) is added then removed then added to the stage loading times can be reduced by keeping the visual registered with the control.
This is useful for Control writers and explained further in "Creating Controls with Visuals" tutorial.

## Reducing Image memory footprint

An application loading images may want to display them at lower resolution than their native resolution.

To support this, DALi can resize an image at load time so that its in-memory copy uses less space and its visual quality benefits from being prefiltered.
`DESIRED_WIDTH` and `DESIRED_HEIGHT` can be set to the Image visual and then `FITTING_MODE`.

The `Dali::FittingMode` namespace provides 4 algorithms, which can be used to fit an image to a desired rectangle, a desired width, or a desired height.

The fitting modes and suggested use cases are as follows:

| Fitting mode 	| Suggested use case |
|---------------|--------------------|
| `FittingMode::SHRINK_TO_FIT` |	Fit full image inside desired width & height, potentially not filling one of either the desired image width or height with pixels. |
| `FittingMode::SCALE_TO_FILL` |	The image is centered in the desired dimensions, exactly touching in one dimension, with image regions outside the other desired dimension cropped. |
| `FittingMode::FIT_WIDTH`     |	Image fills whole width. Height is scaled proportionately to maintain aspect ratio. |
| `FittingMode::FIT_HEIGHT`    | Image fills whole height. Width is scaled proportionately to maintain aspect ratio. |

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
