# Media Controller


You can establish communication between a media control server and a media control client. You can send commands from the client to the server, and the client can request updated metadata and playback information from the server.

The main media controller features include:

-   Updating and retrieving information

    You can [update the metadata and playback information](#updating-and-retrieving-information) on the server side, and then retrieve that information on the client side.

    The media control server provides current information about the registered application that you can send to the client.

    When the client requests the information, the media control server updates the state information of an active application before transferring the data. If the application is not running when the client request arrives, the media control server transfers the latest information.

- Updating and Retrieving Playlist

    You can [create a playlist](#updating-and-retrieving-playlist) on the server side, and then retrieve that information on the client side.

- Sending and processing commands

    You can [send a command](#sending-and-processing-commands) on the client side, and then process the command on the server side.

- Setting and Getting Playback Capability

    You can [set the playback capability](#setting-and-getting-playback-capability) on the server side, and then get that capability on the client side.

 - Media Control Metadata Properties

     You can [set the metadata](#media-control-metadata-properties) on the server side, and then get that metadat on the client side.

## Prerequisites

To enable your application to use the media controller functionality:

1. The application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

   - To use the [Tizen.Multimedia.Remoting.MediaController](https://samsung.github.io/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaController.html) class
       ```
       <privileges>
          <privilege>http://tizen.org/privilege/mediacontroller.client</privilege>
       </privileges>
       ```

   - To use the [Tizen.Multimedia.Remoting.MediaControlServer](https://samsung.github.io/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaControlServer.html) class
       ```
       <privileges>
          <privilege>http://tizen.org/privilege/mediacontroller.server</privilege>
       </privileges>
       ```

2. To use the methods and properties of the [Tizen.Multimedia.Remoting.MediaController](https://samsung.github.io/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaController.html), [Tizen.Multimedia.Remoting.MediaControllerManager](https://samsung.github.io/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaControllerManager.html), and `Tizen.Multimedia.Remoting.MediaControlServer` classes, include the [Tizen.Multimedia.Remoting](https://samsung.github.io/TizenFX/latest/api/Tizen.Multimedia.Remoting.html) namespace in your application:

    ```csharp
    using Tizen.Multimedia.Remoting;
    ```

## Updating and Retrieving Information

To update the metadata and playback information on the server side, and to retrieve it on the client side:

-   To update the metadata and playback information on the server side, follow these steps:
    1.  Start the media control server using the `Start()` method of the [Tizen.Multimedia.Remoting.MediaControlServer](https://samsung.github.io/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaControlServer.html) class:

        ```csharp
        MediaControlServer.Start();
        ```

    2. Update the metadata or playback information using the `SetMetadata()` or `SetPlaybackState()` methods:

        ```csharp
        MediaControlServer.SetPlaybackState(MediaControlPlaybackState.Playing, currentPosition);
        ```

    3. When no longer needed, stop the media control server using the `Stop()` method:

        ```csharp
        MediaControlServer.Stop();
        ```

- To retrieve the metadata and playback information on the client side, follow these steps:
    1.  Create a new instance of the [Tizen.Multimedia.Remoting.MediaControllerManager](https://samsung.github.io/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaControllerManager.html) class:

        ```csharp
        var mediaControllerManager = new MediaControllerManager();
        ```

    2. Retrieve the currently-active controllers and select one:

        ```csharp
        var controller = mediaControllerManager.GetActiveControllers().First();
        ```

    3. Retrieve the metadata or playback information from the server using the `GetMetadata()`, `GetPlaybackState()`, or `GetPlaybackPosition()` methods.

        For example, to retrieve the playback state from the server:

        ```csharp
        Tizen.Log.info(LogTag, $"Playback state is {controller.GetPlaybackState()}");
        ```

## Updating and Retrieving Playlist

To create a playlist from the server side, create a new instance of the [Tizen.Multimedia.Remoting.MediaControlPlaylist](https://samsung.github.io/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaControlPlaylist.html) class:

```csharp
var playlist = new MediaControlPlaylist("MyFavorite");
```

You can also create playlist with Metadata using the following code:

```csharp
var playlist = new MediaControlPlaylist("MyFavoriate",xx
    new Dictionary<string, MediaControlMetadata>()
    {
        {"Song1", new MediaControlMetadata() {Author = "Someone"} },
        {"Song2", new MediaControlMetadata()}
    }
);
```

To retrieve the playlist and metadata information on the client side, use the following code:
```csharp
controller.PlaylistUpdated += (s, e) =>
{
    Tizen.Log.Info(LogTag, $"Updated mode : {e.Mode}, Name : {e.Name}, Title :
{e.Playlist.GetMetadata("IDX1").Title}");
};
```

## Sending and Processing Commands

To send a command from the client and to process it on the server side, follow these steps:

1.  To send a command on the client side, use the `SendPlaybackCommand()` method of the [Tizen.Multimedia.Remoting.MediaController](https://samsung.github.io/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaController.html) class:

    ```csharp
    controller.SendPlaybackCommand(MediaControlPlaybackCommand.Pause);
    ```

2. To process the received command on the server side, add an event handler to the `PlaybackCommandReceived` event of the [Tizen.Multimedia.Remoting.MediaControlServer](https://samsung.github.io/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaControlServer.html) class:

    ```csharp
    MediaControlServer.PlaybackCommandReceived += OnPlaybackCommandReceived;

    void OnPlaybackCommandReceived(object sender, PlaybackCommandReceivedEventArgs e)
    {
        Tizen.Log.Info(LogTag, $"Received command is {e.Command} from {e.ClientAppId}");
    }
    ```

## Setting and Getting Playback Capability

To get playback capability from the client and to set it on the server side, follow these steps:

1. To set playback capability on the server side, use the `SetPlaybackCapability` method of the  [Tizen.Multimedia.Remoting.MediaControlServer](https://samsung.github.io/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaControlServer.html) class:

    ```csharp
    MediaControlServer.SetPlaybackCapability(MediaControlPlaybackCommand.FastForward, MediaControlCapabilitySupport.NotSupported);
    ```

2. To get playback capability on the client side, use the `GetPlaybackCapability` method of the [Tizen.Multimedia.Remoting.MediaController](https://samsung.github.io/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaController.html) class:

    ```csharp
    var playCommandCapability = controller.GetPlaybackCapability(MediaControlPlaybackCommand.Play);
    ```

## Media Control Metadata Properties

To get metadata from the client and to set it on the server side, follow these steps:

1. To set metadata on the server side, use the `SetMetadata` method of the  [Tizen.Multimedia.Remoting.MediaControlServer](https://samsung.github.io/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaControlServer.html) class:

    ```csharp
    MediaControlServer.SetMetadata(new MediaControlMetadata
    {
        Title = "Song1",
        Artist = "Someone"
    });
    ```

2. To get metadata on the client side, use the `GetMetadata` method of the [Tizen.Multimedia.Remoting.MediaController](https://samsung.github.io/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaController.html) class:

    ```csharp
    var metadata = controller.GetMetadata();
    ```

The following table lists all the media control metadata properties the client can request from the server.

**Table: Media control metadata properties**

| Property       | Description                              |
|--------------|----------------------------------------|
| `Title`        | Title of the latest content in the media control server |
| `Artist`       | Artist of the latest content in the media control server |
| `Album`        | Album name of the latest content in the media control server |
| `Author`       | Author of the latest content in the media control server |
| `Genre`        | Genre of the latest content in the media control server |
| `Duration`     | Duration of the latest content in the media control server |
| `Date`         | Date of the latest content in the media control server |
| `Copyright`    | Copyright of the latest content in the media control server |
| `Description`  | Description of the latest content in the media control server |
| `TrackNumber`  | Track number of the latest content in the media control server |
| `AlbumArtPath` | Album art of the latest content in the media control server |


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
