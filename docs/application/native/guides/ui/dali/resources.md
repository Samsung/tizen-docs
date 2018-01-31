# Resources


DALi provides several ways to handle resource images.

## Loading Image Files

You can load an image file with the `ResourceImage` class by specifying its location:

```
Dali::ResourceImage image = Dali::ResourceImage::New( "/my-path/my-image.png" );
```

The loaded image can be displayed using the [ImageView](imageview.md) component:

```
ImageView imageView = ImageView::New( image );
Stage::GetCurrent().Add( imageView );
```

### Supported Resource Types

The resource location can be a file path or a URL.

The currently supported image types are:

- `png`
- `jpeg`
- `gif`
- `bmp`
- `wbmp`
- `ico`
- `ktx`

The currently supported URL schemes are:

- `http`
- `https`

### Asynchronous Loading

Resources are loaded in separate threads, which means that when you call the `ResourceImage::New()` function, it returns immediately.

The application can connect to the `Dali::ResourceImage::LoadingFinishedSignal()` signal to get notified when the image has loaded:

```
class ResourceImageController : public ConnectionTracker
{
  public:
    ResourceImageController( Application& application ) : mApplication( application )
    {
      mApplication.InitSignal().Connect( this, &ResourceImageController::Create );
    }

    void Create( Application& application )
    {
      ResourceImage image = ResourceImage::New( "https://www.tizen.org/sites/default/files/admins/tizen-branding-lockup-on-light.png" );
      image.LoadingFinishedSignal().Connect( this, &ResourceImageController::OnLoadFinished );

      ImageView imageView = ImageView::New( image );
      imageView.SetSize( 400, 200 );
      imageView.SetParentOrigin( ParentOrigin::CENTER );
      Stage::GetCurrent().Add( imageView );
    }

    void OnLoadFinished( ResourceImage image )
    {
      LoadingState state = image.GetLoadingState();
      if( state == ResourceLoadingSucceeded )
         cout << "Loading " << image.GetUrl() << " succeeded" << endl;
      else if( state == ResourceLoadingFailed )
         cout << "Loading " << image.GetUrl() << " failed" << endl;
    }
};
```

For more information on the resource threads, see [Resource Loading with Multi-threading](multi-threaded.md#resource-loading-with-multi-threading).

### Load Time Resizing

An application loading images from an external source often wants to display those images at a lower resolution than their native ones. To support this, DALi can resize an image at load time so that its in-memory copy uses less space and its visual quality benefits from being prefiltered. The `Dali::FittingMode` namespace (in [mobile](../../../../../org.tizen.native.mobile.apireference/namespaceDali_1_1FittingMode.html) and [wearable](../../../../../org.tizen.native.wearable.apireference/namespaceDali_1_1FittingMode.html) applications) provides 4 algorithms, which can be used to fit an image to a desired rectangle, a desired width, or a desired height.

The following code snippet is an example of rescaling:

```
Dali::Image image = Dali::ResourceImage::New( filename, ImageDimensions( 240, 240 ), FittingMode::SCALE_TO_FILL );
```

This example sets the size and fitting mode appropriately for a large thumbnail during the `Dali::ResourceImage` object construction. In general, to enable scaling on load, pass a non-zero width or height and one of the 4 fitting modes to the `Dali::ResourceImage`creator function as shown above.

The fitting modes and suggested use cases are as follows:

**Table: Fitting mode use cases**

| Fitting mode                       | Suggested use case                       |
|------------------------------------|------------------------------------------|
| `Dali::FittingMode::SHRINK_TO_FIT` | Full-screen image display: limit the loaded image resolution to the device resolution, but show all of the image. |
| `Dali::FittingMode::SCALE_TO_FILL` | Thumbnail gallery grid: limit the loaded image resolution to the screen tile, filling the whole tile but losing a few pixels to match the tile shape. |
| `Dali::FittingMode::FIT_WIDTH`     | Image columns: limit the loaded image resolution to the column width. |
| `Dali::FittingMode::FIT_HEIGHT`    | Image rows: limit the loaded image resolution to the row height. |

### Image Size

If the application requires the image dimensions immediately, they can be retrieved synchronously:

```
Dali::ImageDimensions dimensions = Dali::ResourceImage::GetImageSize( "/my-path/my-image.png" );
```

This is a disk-read operation, which can be slow and block the event thread. This operation is currently not supported for remote resources, such as HTTP or HTTPS URLs.

## Using a Buffer Image

A `Dali::BufferImage` class (in [mobile](../../../../../org.tizen.native.mobile.apireference/classDali_1_1BufferImage.html) and [wearable](../../../../../org.tizen.native.wearable.apireference/classDali_1_1BufferImage.html) applications) represents an image resource in the form of pixel buffer data. The application can write to this buffer as required and the image is updated on the screen:

```
// Create a 200 by 200 pixel buffer with a color-depth of 32-bits (with alpha)
Dali::BufferImage image = Dali::BufferImage::New( 200, 200 );
```

## Related Information
* Dependencies
 - Tizen 2.4 and Higher for Mobile
 - Tizen 3.0 and Higher for Wearable
