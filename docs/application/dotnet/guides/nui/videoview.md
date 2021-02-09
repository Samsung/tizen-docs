---
keyword: video, VideoView, playback, play, NUI, ResourceUrl, volume,
---

# VideoView

The [VideoView](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.BaseComponents.VideoView.html) class is a control for video playback and display. It provides minimum functions for playback (play, pause, stop, forward, and backward). Some options, such as volume, can be controlled through the control properties. NUI supports many kinds of video format, such as `.avi`, `.3gp` and `mp4`.

 > [!NOTE] 
 > The `VideoView` control does not use any privileges APIs on its own. However, if you use video files in a specific device storage, the application requires privileges to access the storage.


## Create a VideoView

The following basic example shows how to create a `VideoView` object:

**Figure: Basic VideoView**

![Basic VideoView](./media/basicVideoView.png)

1.  To use the `VideoView` class, add the following namespaces:

    ```cs
    using Tizen.NUI;
    using Tizen.NUI.BaseComponents;
    ```	    
  
2.   The video file is assumed to be in the resources directory. Create an instance of the `VideoView` class and use the `ResourceUrl` property to pass the path to the video file. Set `WidthResizePolicy` to make `VideoView` instance use full width of the window and set `HeightResizePolicy` to maintain aspect ratio of video. And then you can invoke the `Play()` method to start video:

      ```cs
      VideoView player = new VideoView();
      player.ResourceUrl = DirectoryInfo.Resource + "sample.mp4";
      player.WidthResizePolicy = ResizePolicyType.FillToParent;
      player.HeightResizePolicy = ResizePolicyType.DimensionDependency;
      player.Play();

      Window.Instance.Add(player);
      ```

> [!NOTE]  
> You can set the video file to be played in `new VideoView()`, or by modifying the `Video` property.


## VideoView methods

  The following are the `VideoView` functions for playback:

  - The `Play()` method starts video:

      ```cs
      player.Play();
      ```

  - The `Pause()` method pauses video. To resume the video, use the `Play()` method:

      ```cs
      player.Pause();
      ```

  - The `Stop()` method stops video. After the `Stop()` method is called, the video is started from the beginning if `Play()` method is called:

      ```cs
      player.Stop();
      ```

  - The `Forward(x)` method fast forwards the video for `x` milliseconds:

      ```cs
      player.Forward(1000); // +1 second
      ```

  - The `Backward(x)` method rewinds the video backward for `x` milliseconds:

      ```cs
      player.Backward(1000); // -1 second
      ``` 

## VideoView event

The following code shows the `Finished` event, which is emitted when the video playback is finished:

  1. Create handler for `Finished` event:

      ```cs
      private void OnFinish(object sender, VideoView.FinishedEventArgs e)
      {
          // do something when the video is finished
      }
      ```
  
  2. Add handler to the `player` created in previous section:

      ```cs
      player.Finished += OnFinish;
      ```

## VideoView properties

You can modify the `VideoView` appearance and behavior through its properties.

The following table lists the available `VideoView` properties.

**Table: VideoView properties**

| Property      | Type         | Description                              |
| ------------- | ------------ | ---------------------------------------- |
| `Video`       | PropertyMap  | Video file URL string. This property can also provide additional features, such as a custom shader, by `PropertyMap`. |
| `Looping`     | Boolean      | Enable or disable the looping of the playback. |
| `Muted`       | Boolean      | Whether the playback is muted.            |
| `Volume`      | PropertyMap  | Playback volume. The `PropertyMap` must get left and right volume scalar as a float type. |
| `Underlay`    | Boolean      | Set the underlay either as `true` or `false`, to allow NUI to draw videos on either **Underlay** or **Overlay**. |
| `ResourceUrl` | String       | The video file URL as a string type.            |

## Related information
- Dependencies
  -   Tizen 4.0 and Higher
