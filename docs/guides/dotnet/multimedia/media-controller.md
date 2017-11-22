Media Controller
================

## Dependencies

- Tizen 4.0 and Higher

You can establish communication between a media control server and a
media control client. You can send commands from the client to the
server, and the client can request updated metadata and playback
information from the server.

The main media controller features include:

-   Updating and retrieving information

    You can [update the metadata and playback information](#get_media)
    on the server side, and then retrieve that information on the
    client side.

    The media control server provides current information about the
    registered application that you can send to the client.

    When the client requests the information, the media control server
    updates the state information of an active application before
    transferring the data. If the application is not running when the
    client request arrives, the media control server transfers the
    latest information.

- Sending and processing commands

    You can [send a command](#send_media) to the server from the client
    side, and then process the command on the server side.

    The client can request server state or [metadata](#servermetadata)
    information from the server, and receive it through an
    event handler.


Prerequisites
-------------

To enable your application to use the media controller functionality:

1.  To use the
    [Tizen.Multimedia.Remoting.MediaControlServer](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1Remoting_1_1MediaControlServer.html)
    class, the application has to request permission by adding the
    following privilege to the `tizen-manifest.xml` file:

    ``` {.prettyprint}
    <privileges>
       <privilege>http://tizen.org/privilege/mediacontroller.server</privilege>
    </privileges>
    ```

2. To use the methods and properties of the
    [Tizen.Multimedia.Remoting.MediaController](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1Remoting_1_1MediaController.html),
    [Tizen.Multimedia.Remoting.MediaControllerManager](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1Remoting_1_1MediaControllerManager.html),
    and `Tizen.Multimedia.Remoting.MediaControlServer` classes, include
    the
    [Tizen.Multimedia.Remoting](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Multimedia_1_1Remoting.html)
    namespace in your application:

    ``` {.prettyprint}
    using Tizen.Multimedia.Remoting;
    ```


Updating and Retrieving Information <a id="get_media"></a>
-----------------------------------

To update the metadata and playback information on the server side, and
to retrieve it on the client side:

-   To update the metadata and playback information on the server side:
    1.  Start the media control server using the `Start()` method of the
        [Tizen.Multimedia.Remoting.MediaControlServer](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1Remoting_1_1MediaControlServer.html)
        class:

        ``` {.prettyprint}
        MediaControlServer.Start();
        ```

    2. Update the metadata or playback information using the
        `SetMetadata()` or `SetPlaybackState()` methods:

        ``` {.prettyprint}
        MediaControlServer.SetPlaybackState(MediaControlPlaybackState.Playing, currentPosition);
        ```

    3. When no longer needed, stop the media control server using the
        `Stop()` method:

        ``` {.prettyprint}
        MediaControlServer.Stop();
        ```

- To retrieve the metadata and playback information on the client
    side:
    1.  Create a new instance of the
        [Tizen.Multimedia.Remoting.MediaControllerManager](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1Remoting_1_1MediaControllerManager.html)
        class:

        ``` {.prettyprint}
        var mediaControllerManager = new MediaControllerManager();
        ```

    2. Retrieve the currently-active controllers and select one:

        ``` {.prettyprint}
        var controller = MediaControllerManager.GetActiveControllers().First();
        ```

    3. Retrieve the metadata or playback information from the server
        using the `GetMetadata()`, `GetPlaybackState()`, or
        `GetPlaybackPosition()` methods.

        For example, to retrieve the playback state from the server:

        ``` {.prettyprint}
        Tizen.Log.info(LogTag, $"Playback state is {controller.GetPlaybackState()}");
        ```


Sending and Processing Commands <a id="send_media"></a>
-------------------------------

To send a command from the client and to process it on the server side:

1.  To send a command on the client side, use the
    `SendPlaybackCommand()` method of the
    [Tizen.Multimedia.Remoting.MediaController](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1Remoting_1_1MediaController.html)
    class:

    ``` {.prettyprint}
    controller.SendPlaybackCommand(MediaControlPlaybackCommand.Pause);
    ```

2. To process the received command on the server side, add an event
    handler to the `PlaybackCommandReceived` event of the
    [Tizen.Multimedia.Remoting.MediaControlServer](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Multimedia_1_1Remoting_1_1MediaControlServer.html)
    class:

    ``` {.prettyprint}
    MediaControlServer.PlaybackCommandReceived += OnPlaybackCommandReceived;

    void OnPlaybackCommandReceived(object sender, PlaybackCommandReceivedEventArgs e)
    {
        Tizen.Log.Info(LogTag, $"Received command is {e.Command} from {e.ClientAppId}");
    }
    ```


Media Control Metadata Properties <a id="servermetadata"></a>
---------------------------------

The following table lists all the media control metadata properties the
client can request from the server.

**Table: Media control metadata properties**

| Property       | Description                              |
| -------------- | ---------------------------------------- |
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