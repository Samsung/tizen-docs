---
keyword: video, VideoView, playback, play, NUI, ResourceUrl, volume,
---

# VideoView

The [VideoView](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.BaseComponents.VideoView.html) class is a control for video playback and display. It provides minimum functions for playback (play, pause, stop, forward, and backward). Some options, such as volume, can be controlled through the control properties. NUI supports many kinds of video format, such as `.avi`, `.3gp` and `mp4`.

 > **Note**  
 > The `VideoView` control does not use any privileges APIs on its own. However, if you use video files in a specific device storage, the application requires privileges to access the storage.


## Create a VideoView

The following basic example shows how to create a `VideoView` object:

**Figure: Basic VideoView**

![Basic VideoView](./media/basicVideoview.png)

1.  To use the `VideoView` class, add the following namespaces:

    ```cs
    using Tizen.NUI;
    using Tizen.NUI.BaseComponents;
    ```	    
  
2.   The video file is assumed to be in the resources directory. Create an instance of the `VideoView` class and use the `ResourceUrl` property to pass the path to the video file. Set `WidthResizePolicy` to make `VideoView` instance use full width of the window and set `HeightResizePolicy` to maintain aspect ratio of video. In the end invoke `Play()` method to start video:

      ```cs
      VideoView player = new VideoView();
      player.ResourceUrl = DirectoryInfo.Resource + "sample.mp4";
      player.WidthResizePolicy = ResizePolicyType.FillToParent;
      player.HeightResizePolicy = ResizePolicyType.DimensionDependency;
      player.Play();

      Window.Instance.Add(player);
      ```

> **Note**  
> You can set the video file to be played in the `new VideoView()` function, or by modifying `Video` property.


## VideoView Methods

  As it was mentioned before, the `VideoView` provides minimum functions for playback:

  1. The `Play()` method starts video:

      ```cs
      player.Play();
      ```

  2. The `Pause()` method pauses video. Video can be resumed by using the `Play()` method:

      ```cs
      player.Pause();
      ```

  2. The `Stop()` method stops video. After the `Play()` method is called, the video will be started from the beginning:

      ```cs
      player.Stop();
      ```

  2. The `Forward(x)` method rewind video forward for `x` miliseconds:

      ```cs
      player.Forward(1000); // +1 second
      ```

  2. The `Backward(x)` method rewind video backward for `x` miliseconds:

      ```cs
      player.Backward(1000); // +1 second
      ``` 

## VideoView Event

The following code shows the `Finished` signal, which is emitted when the video playback is finished:

  1. Create handler for `Finished` signal:

      ```cs
      private void OnFinish(object sender, VideoView.FinishedEventArgs e)
      {
          // do something when the video is finished
      }
      ```
  
  2. Add handler to `VideoView` instance:

      ```cs
      player.Finished += OnFinish;
      ```

## VideoView Properties

You can modify the `VideoView` appearance and behavior through its properties.

The following table lists the available `VideoView` properties.

**Table: VideoView properties**

| Property      | Type         | Description                              |
| ------------- | ------------ | ---------------------------------------- |
| `Video`       | PropertyMap  | Video file URL string. This property can also provide additional features, such as a custom shader, by `PropertyMap`. |
| `Looping`     | Boolean      | Enable or disable the looping of the playback. |
| `Muted`       | Boolean      | Whether the playback is muted.            |
| `Volume`      | PropertyMap  | Playback volume. The `PropertyMap` must get left and right volume scalar as a float type. |
| `Underlay`    | Boolean      | Set the underlay either as `true` or `false`, to allow NUI(DALi) to draw videos on either **Underlay** or **Overlay**. |
| `ResourceUrl` | String       | The video file URL as a string type.            |

## Related Information
- Dependencies
  -   Tizen 4.0 and Higher
