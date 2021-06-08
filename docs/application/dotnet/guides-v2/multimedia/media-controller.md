# Media Controller


You can establish communication between a media control server and a media control client. You can send commands from the client to the server, and the client can request updated metadata and playback information from the server.

The main media controller features include:

- Updating and retrieving playlist

    You can [create a playlist](#creating-and-retrieving-playlist) on the server side, and then retrieve that information on the client side.

-   Updating and retrieving information

    You can [update the playback information](#updating-and-retrieving-information) on the server side, and then retrieve that information on the client side.

    The media control server provides current information about the registered application that you can send to the client.

    When the client requests the information, the media control server updates the state information of an active application before transferring the data. If the application is not running when the client request arrives, the media control server transfers the latest information.

- Sending and processing commands

    You can [send a command](#sending-and-processing-commands) on the client side, and then process the command on the server side.

- Setting and getting playback capability

    You can [set the playback capability](#setting-and-getting-playback-capability) on the server side, and then get that capability on the client side.

 - Media control metadata properties

     You can [set the metadata](#setting-and-getting-media-control-metadata) on the server side, and then get that metadata on the client side.

## Prerequisites

To enable your application to use the media controller functionality:

- The application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

   - To use the [Tizen.Multimedia.Remoting.MediaController](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaController.html) class:
       ```XML
       <privileges>
          <privilege>http://tizen.org/privilege/mediacontroller.client</privilege>
       </privileges>
       ```

   - To use the [Tizen.Multimedia.Remoting.MediaControlServer](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaControlServer.html) class:
       ```XML
       <privileges>
          <privilege>http://tizen.org/privilege/mediacontroller.server</privilege>
       </privileges>
       ```

- To use the methods and properties of the [Tizen.Multimedia.Remoting.MediaController](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaController.html), [Tizen.Multimedia.Remoting.MediaControllerManager](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaControllerManager.html), and [Tizen.Multimedia.Remoting.MediaControlServer](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaControlServer.html) classes, include the [Tizen.Multimedia.Remoting](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.html) namespace in your application:

    ```csharp
    using Tizen.Multimedia.Remoting;
    ```

-  Start the media control server using the `Start()` methods of the [Tizen.Multimedia.Remoting.MediaControlServer](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaControlServer.html) class:

    ```csharp
    MediaControlServer.Start();
    ```

- Create a new instance of the [Tizen.Multimedia.Remoting.MediaControllerManager](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaControllerManager.html) class and retrieve the currently-active controllers and select one:

    ```csharp
    var mediaControllerManager = new MediaControllerManager();
    var mediaController = mediaControllerManager.GetActiveControllers().First();
    ```

- When server is no longer needed, stop the media control server using the `Stop()` method of the [Tizen.Multimedia.Remoting.MediaControlServer](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaControlServer.html) class:

    ```csharp
    MediaControlServer.Stop();
    ```

## Creating and Retrieving Playlist

To create a playlist from the server side and retrieve it on the client side, follow these steps:

1. To create a playlist from the server side, create a new instance of the [Tizen.Multimedia.Remoting.MediaControlPlaylist](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaControlPlaylist.html) class:

    ```csharp
    var playlist = new MediaControlPlaylist("MyFavorite");
    ```

    You can also create playlist with Metadata using the following code:

    ```csharp
    var playlist = new MediaControlPlaylist("MyFavoriate",
        new Dictionary<string, MediaControlMetadata>()
        {
            {"Song1", new MediaControlMetadata() {Author = "Someone"} },
            {"Song2", new MediaControlMetadata()}
        }
    );
    ```

2. To retrieve the playlist and [metadata](#setting-and-getting-media-control-metadata) information on the client side, use the following code:

    ```csharp
    mediaController.PlaylistUpdated += (s, e) =>
    {
        Log.Info("MC", $"Updated mode : {e.Mode}, Name : {e.Name}, Title : {e.Playlist.GetMetadata("IDX1").Title}");
    };
    ```

## Updating and Retrieving Information

To update the playback information on the server side and to retrieve it on the client side, follow these steps:

1. To update the playback information on the server side, use `SetPlaybackState()`, `SetInfoOfCurrentPlayingMedia()` methods of the [Tizen.Multimedia.Remoting.MediaControlServer](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaControlServer.html) class:

    ```csharp
    MediaControlServer.SetPlaybackState(MediaControlPlaybackState.Playing, currentPosition);
    MediaControlServer.SetInfoOfCurrentPlayingMedia("MyFavorite", "IDX1");
    ```

2. To retrieve the playback information on the client side, use `GetPlaybackState()`, or `GetPlaybackPosition()` methods of the [Tizen.Multimedia.Remoting.MediaController](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaController.html) class:

    ```csharp
    Log.info("MC", $"Playback state is {mediaController.GetPlaybackState()}, index is {mediacontroller.GetIndexOfCurrentPlayingMedia()}");
    ```

## Sending and Processing Commands

To send a command from the client and to process it on the server side, follow these steps:

1.  To send a command on the client side, use the `RequestAsync()` method of the [Tizen.Multimedia.Remoting.MediaController](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaController.html) class:

    ```csharp
    mediaController.RequestAsync(new PlaybackCommand(MediaControlPlaybackCommand.Play));
    ```

2. To process the received command on the server side, add an event handler to the `PlaybackActionCommandReceived` event of the [Tizen.Multimedia.Remoting.MediaControlServer](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaControlServer.html) class:

    ```csharp
    MediaControlServer.PlaybackActionCommandReceived += (s, e) =>
    {
        Log.Info("MC", $"e.Command.Action : {e.Command.Action}");

        MediaControlServer.Response(e.Command, (int)ErrorCode.None);
    }
    ```

To send a search command from the client and to process it on the server side, follow these steps:
1.  To send a search command on the client side, use the `RequestAsync()` method of the [Tizen.Multimedia.Remoting.MediaController](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaController.html) class:

    ```csharp
    var searchCondition = new MediaControlSearchCondition(MediaControlContentType.Image,
        MediaControlSearchCategory.Artist, "GD", null);

    mediaController.RequestAsync(new SearchCommand(searchCondition));
    ```

2. To process the received search command on the server side, add an event handler to the `SearchCommandReceived` event of the [Tizen.Multimedia.Remoting.MediaControlServer](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaControlServer.html) class:

    ```csharp
    MediaControlServer.SearchCommandReceived += (s, e) =>
    {
        foreach (var condition in e.Command.Conditions)
        {
            Log.Info("MC", $"{condition.Category}, {condition.ContentType}, {condition.Keyword}");
        }

        MediaControlServer.Response(e.Command, (int)ErrorCode.None);
    };
    ```

To send a custom command from the server and to process it on the client side, follow these steps:
1.  To send a search command on the server side, use the `RequestAsync()` method of the [Tizen.Multimedia.Remoting.MediaControlServer](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaControlServer.html) class:

    ```csharp
    MediaControlServer.RequestAsync(new CustomCommand("CustomAction"));
    ```

2. To process the received custom command on the client side, add an event handler to the `CustomCommandReceived` event of the [Tizen.Multimedia.Remoting.MediaController](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaController.html) class:

    ```csharp
    mediaController.CustomCommandReceived += (s, e) =>
    {
        Log.Info("MC", $"{ e.Command.Action}");

        mediaController.Response(e.Command, (int)ErrorCode.None);
    };
    ```

## Setting and Getting Playback Capability

To get playback capability from the client and to set it on the server side, follow these steps:

1. To set playback capability on the server side, use the `SetPlaybackCapability()` method of the  [Tizen.Multimedia.Remoting.MediaControlServer](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaControlServer.html) class:

    ```csharp
    MediaControlServer.SetPlaybackCapability(MediaControlPlaybackCommand.FastForward, MediaControlCapabilitySupport.NotSupported);
    ```

2. To get playback capability on the client side, use the `GetPlaybackCapability()` method of the [Tizen.Multimedia.Remoting.MediaController](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaController.html) class:

    ```csharp
    var playCommandCapability = mediaController.GetPlaybackCapability(MediaControlPlaybackCommand.Play);
    ```

## Setting and Getting Media Control Metadata

To get metadata from the client and to set it on the server side, follow these steps:

1. To set metadata on the server side, use the `SetMetadata()` method of the  [Tizen.Multimedia.Remoting.MediaControlServer](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaControlServer.html) class:

    ```csharp
    MediaControlServer.SetMetadata(new MediaControlMetadata
    {
        Title = "Song1",
        Artist = "Someone"
    });
    ```

2. To get metadata on the client side, use the `GetMetadata()` method of the [Tizen.Multimedia.Remoting.MediaController](/application/dotnet/api/TizenFX/latest/api/Tizen.Multimedia.Remoting.MediaController.html) class:

    ```csharp
    var metadata = mediaController.GetMetadata();
    ```

The following table lists all the media control metadata properties the client can request from the server:

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
| `Season` | Season information of the latest content in the media control server |
| `Episode` | Episode information of the latest content in the media control server |
| `Resolution` | Resolution of the latest content in the media control server |


## Related Information
- Dependencies
  -   Tizen 4.0 and Higher
