### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## ImageLoaderSamplingMode Enum

Enumeration for [ImageLoader](Tizen.UI.ImageLoader.md 'Tizen.UI.ImageLoader') sampling mode.

```csharp
public enum ImageLoaderSamplingMode
```
### Fields

<a name='Tizen.UI.ImageLoaderSamplingMode.Box'></a>

`Box` 0

Iteratively box filter to generate an image of 1/2, 1/4, 1/8, etc. width and height and approximately the desired size. <br/>  
This is the default.

<a name='Tizen.UI.ImageLoaderSamplingMode.BoxThenLinear'></a>

`BoxThenLinear` 4

Iteratively box filter to almost the right size, then for each output pixel, read four pixels from the last level of box filtering and write their weighted average.

<a name='Tizen.UI.ImageLoaderSamplingMode.BoxThenNearest'></a>

`BoxThenNearest` 3

Iteratively box filter to generate an image of 1/2, 1/4, 1/8, etc. width and height and approximately the desired size, <br/>  
then for each output pixel, read one pixel from the last level of box filtering.<br/>

<a name='Tizen.UI.ImageLoaderSamplingMode.DontCare'></a>

`DontCare` 6

For caching algorithms where a client strongly prefers a cache-hit to reuse a cached image.

<a name='Tizen.UI.ImageLoaderSamplingMode.Linear'></a>

`Linear` 2

For each output pixel, read a quad of four input pixels and write a weighted average of them.

<a name='Tizen.UI.ImageLoaderSamplingMode.Nearest'></a>

`Nearest` 1

For each output pixel, read one input pixel.

<a name='Tizen.UI.ImageLoaderSamplingMode.NoFilter'></a>

`NoFilter` 5

No filtering is performed. If the SCALE_TO_FILL scaling mode is enabled, the borders of the image may be trimmed to match the aspect ratio of the desired dimensions.






