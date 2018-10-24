# VideoView

The `VideoView` class is a control for video playback and display. It provides minimum functions for playback (play, pause, stop, forward, and backward). Some options, such as volume, can be controlled through the control properties.

 > **Note**  
 > You must install a video plugin to enable `VideoView`.

**Figure: VideoView**

![VideoView](./media/dali_videoview.png)

 > **Note**  
 > The VideoView control does not use any privileges APIs on its own. However, if you use video files in a specific device storage, the application requires privileges to access the storage.

In this tutorial, the following subjects are covered:

[VideoView event](#1)<br>
[Creating a VideoView](#2)<br>
[VideoView Properties](#3)<br>

<a name="1"></a>
## VideoView event

The following table lists the basic signal provided by the `VideoView` class.

**Table: VideoView input signals**

| Input signal  | Description                                 |
| ------------- | ------------------------------------------- |
| `Finished`    | Emitted when a video playback is finished.  |

The `VideoView` class provides the `Finished`, which is emitted when the video playback is finished. The related callback can support some basic actions.

<a name="2"></a>
## Creating a VideoView

The following basic example shows how to create a `VideoView` object:

```
// Create a ScrollView instance
Window window = Window.Instance;
VideoView view = new VideoView( "videofile.mp4" );
window.Add(view);
view.ParentOrigin = ParentOrigin.Center;
view.PivotPoint = PivotPoint.Center;
view.HeightResizePolicy = ResizePolicyType.UseNaturalSize;
view.WidthResizePolicy = ResizePolicyType.UseNaturalSize;
view.Size2D = new Size2D( WIDTH, HEIGHT );
view.Play();
```

 > **Note**  
 > You can set the video file to be played in the `new VideoView()` function, or by modifying `Video` property.

<a name="3"></a>
## VideoView Properties

You can modify the `VideoView` appearance and behavior through its properties.

The following table lists the available `VideoView` properties.

**Table: VideoView properties**

| Property      | Type         | Description                              |
| ------------- | ------------ | ---------------------------------------- |
| `Video`       | PropertyMap  | Video file URL string. This property can also provide additional features, such as a custom shader, by `Property::Map`. |
| `Looping`     | Boolean      | Enable or disable the looping of the playback. |
| `Muted`       | Boolean      | Whether the playback is muted.            |
| `Volume`      | PropertyMap  | Playback volume. The `PropertyMap` must get left and right volume scalar as a float type. |
| `Underlay`    | Boolean      | Set the underlay either as `true` or `false`, to allow NUI(DALi) to draw videos on either **Underlay** or **Overlay**. |
| `ResourceUrl` | String       | The video file URL as a string type.            |



## Related Information
- Dependencies
  -   Tizen 4.0 and Higher
