# Capture


The `Dali::Capture` is a class to capture a snapshot of the scene tree. The captured result can be saved as a file, or can be used as an image source to be rendered by DALi `ImageView` or `ImageVisual`.


## How to capture your scene

The following example shows how to use `Dali::Capture`:

``` C++
Capture capture = Capture::New();

capture.Start( source, size, path, clearColor, quality);
```

Each parameter of `Capture::Start` is denoted as follows:

 * **Actor source**: source actor to be captured. Only this source actor and its children are captured.
 * **Vector2 size**: size of captured result image.
 * **std::string path**: system path to save the captured image file. If the path is empty, `Dali::Capture` does not save the captured image as a file. Instead, the captured image can be rendered by DALi `ImageView` or `ImageVisual`.
   * `Dali::Capture` supports PNG and JPEG format for the saved image.
 * **Vector4 clearcolor**: background color of the captured scene.
 * **int quality**: a value to control the quality of the saved image file. For JPEG file format, the value must be in the range [1,100]. Default value is 100.

If required, you can also connect a callback function to a finished signal:

``` C++
capture.FinishedSignal().Connect(this, &CaptureSceneExample::OnCaptureFinished);

void CaptureSceneExample::OnCaptureFinished( Capture capture, Capture::FinishState state )
{
  if ( state == Capture::FinishState::SUCCEEDED )
  {
    // Do something
  }
  else
  {
    // Do something
  }
}
```

You can also use the captured result as an image source to be rendered by DALi `ImageView` or `ImageVisual`:

``` C++
void CaptureSceneExample::OnCaptureFinished( Capture capture, Capture::FinishState state )
{
  if ( state == Capture::FinishState::SUCCEEDED )
  {
    std::string url = Toolkit::Image::GenerateUrl( capture.GetNativeImageSource() );
    Toolkit::ImageView imageView = Toolkit::ImageView::New( url );

    mRootLayer.Add( imageView );
  }
  else
  {
    // Do something
  }
}
```

## Related Information
- Dependencies
  - Tizen 6.0 and Higher for Mobile
  - Tizen 4.0 and Higher for Wearable
