# VideoView

## Dependencies

- Tizen 2.4 and Higher for Mobile
- Tizen 3.0 and Higher for Wearable

The `Dali::Toolkit::VideoView` is a control for video playback and display. It provides minimum functions for playback (play, pause, stop, forward, and backward). Some options, such as volume, can be controlled through the control properties. For the VideoView to work, a video plugin is needed. The Tizen 3.0 platform includes the required Dali video plugin.

**Figure: VideoView**

![VideoView](./media/dali_videoview.png)

 **Note** 

The VideoView control does not use any privileges APIs on its own. However, if you use video files in a specific device storage, the application can require privileges to access the storage. For more information, see the Player API Reference (in [mobile](http://org.tizen.native.mobile.apireference/group__CAPI__MEDIA__PLAYER__MODULE.html) and [wearable](http://org.tizen.native.wearable.apireference/group__CAPI__MEDIA__PLAYER__MODULE.html) applications).    

The `VideoView` class provides the `FinishedSignal()`, which is emitted when the video playback is finished. The related callback can support some basic actions.

```
void Create( Application& application )
{
  mView.FinishedSignal().Connect( this, &VideoViewController::OnFinished );
}

void OnFinished( VideoView& view )
{
  mFinished = true;
}
```

## Creating a VideoView

The following basic example shows how to create a `Dali::Toolkit::VideoView` object:

```
class VideoViewController: public ConnectionTracker
{
  public:
    VideoViewController( Application& application )
      : mApplication( application )
    {
      mApplication.InitSignal().Connect( this, &VideoViewController::Create );
    }

    void Create( Application& application )
    {
      // Set the handle
      mView = Toolkit::VideoView::New( "videofile.mp4" );
      Stage::GetCurrent().Add( mView );
      mView.SetParentOrigin( ParentOrigin::CENTER );
      mView.SetAnchorPoint( AnchorPoint::CENTER );
      mView.SetResizePolicy( ResizePolicy::USE_NATURAL_SIZE, Dimension::ALL_DIMENSIONS );
      mView.SetSize( WIDTH, HEIGHT );
      mView.Play();
    }

  private:
    Application& mApplication;
    VideoView mView;
}
```

​        **Note**        You can set the video file to be played in the `VideoView::New()` function, or by modifying `VIDEO` property with `SetProperty( VideoView::Property::VIDEO, "videofile2.mp4" )`.    

## Modifying VideoView Properties

You can modify the `VideoView` appearance and behavior through its properties.

To change a property from its default value, use the `SetProperty()` function:

```
Property::Map oldMap;
Property::Value value = mView.GetProperty( VideoView::Property::VOLUME );
Value.Get( oldMap );

Property::Map newMap;
newMap.Insert( "volumeLeft", 1.0f );
newMap.Insert( "volumeRight", 0.5f );
mView.SetProperty( VideoView::Property::VOLUME, newMap );
```

The following table lists the available `VideoView` properties.

**Table: VideoView properties**

| Property  | Type                        | Description                              |
| --------- | --------------------------- | ---------------------------------------- |
| `VIDEO`   | `String` or `Property::Map` | Video file URL string. This property can also provide additional features, such as a custom shader, by `Property::Map`. |
| `LOOPING` | `Bool`                      | Whether the playback loops               |
| `MUTED`   | `Bool`                      | Whether the playback is muted            |
| `VOLUME`  | `Property::Map`             | Playback volume. The `Property::Map` must get left and right volume scalar as a float type. |