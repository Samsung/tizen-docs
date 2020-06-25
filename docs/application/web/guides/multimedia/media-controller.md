# Media Controller

You can have your client application communicate with a media server.

To manage the media using the Media Controller API, you have to develop two applications:

- Client that sends requests to the server in order to change, for example, the playback state and position modes.
- Server that directly manages the media on the device.

The main features of the Media Controller API include:

- Setting up the client and server pair

  You can [set up the client and server pair](#getting-client-and-server) by creating a new server using the `createServer()` method. On the client side, you can get a client and find active servers using the `getClient()` and `findServers()` methods.

- Managing requests

  You can [send a request](#managing-requests) from the client to the server to modify various playback attributes. In the server, you can set up a listener to react to the client request and perform the requested task.

- Setting and getting the server icon URI

  You can [set the server icon URI](#setting-and-getting-server-icon-uri) and read it from the client.

- Receiving notifications from the server

  You can [receive notifications on changes made by the server](#receiving-notifications-from-server) by registering a listener with the `addPlaybackInfoChangeListener()` method.

- Sending custom commands

  You can [use the client to send commands](#send_custom_commands) with the `sendCommand()` method.

  To [receive and handle incoming commands](#receive_custom_commands) in the server, use the `addCommandListener()` method.

- Sending custom events

  You can [use the server to send the custom events](#send_custom_events) with the `sendEvent()` method.

  To [receive and handle the incoming events](#receive_custom_events) in the client, use the `setCustomEventListener()` method.

- Sending and receiving search requests

  You can use the media controller client to [send the search requests](#sending-search-request) with the `sendSearchRequest()` method.

  You can use the media controller server to [receive the search requests](#receiving-search-request) using the `setSearchRequestListener()` method, and return the `RequestReply` object to the client who sent the request.

- Setting content type for the currently playing media

  You can [set content type for the currently playing media](#setting-content-type-for-currently-playing-media) using the updatePlaybackContentType() server method.

- Setting age rating for the currently playing media

  You can [set age rating for the currently playing media](#setting-content-age-rating-for-currently-playing-media) using the updatePlaybackAgeRating() server method.

- Managing playlists on server side

  You can [manage playlists](#managing-playlists-on-server-side) on server side by creating, saving, deleting, and getting information about playlists. You can also update the playback item from the playlists item list.

- Managing playlists on client side

  You can [manage playlists](#managing-playlists-on-client-side) on client side by sending request about the new playback item to the server. You can then add listeners to be invoked when the playlist is updated on the server.

- Managing abilities of the media controller server

  You can [set the abilities](#setting-media-controller-server-abilities) of the media controller server by using the `MediaControllerAbilities` interface (in [mobile](../../api/latest/device_api/mobile/tizen/mediacontroller.html#MediaControllerAbilities), [wearable](../../api/latest/device_api/wearable/tizen/mediacontroller.html#MediaControllerAbilities), and [tv](../../api/latest/device_api/tv/tizen/mediacontroller.html#MediaControllerAbilities) applications).

  You can use the `MediaControllerAbilitiesInfo` interface (in [mobile](../../api/latest/device_api/mobile/tizen/mediacontroller.html#MediaControllerAbilitiesInfo), [wearable](../../api/latest/device_api/wearable/tizen/mediacontroller.html#MediaControllerAbilitiesInfo), and [tv](../../api/latest/device_api/tv/tizen/mediacontroller.html#MediaControllerAbilitiesInfo) applications) to check which features are supported by the server. Information about current status of the media controller server abilities can be gathered by `getLatestServerInfo()` method.

- Setting features of the media controller server

  You can [set the media controller server features](#media-controller-server-features) using the server interfaces.

## Prerequisites

To use the Media Controller API (in [mobile](../../api/latest/device_api/mobile/tizen/mediacontroller.html), [wearable](../../api/latest/device_api/wearable/tizen/mediacontroller.html), and [tv](../../api/latest/device_api/tv/tizen/mediacontroller.html) applications), the application has to request permission by adding the following privileges to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/mediacontroller.client"/>
<tizen:privilege name="http://tizen.org/privilege/mediacontroller.server"/>
```

## Getting Client and Server

To manage the media controller features in your application, you must learn to set up the client and server pair:

1. Create a media controller server using the `createServer()` method:

   ```javascript
   var mcServer = tizen.mediacontroller.createServer();
   ```

2. Get the client using the `getClient()` method:

   ```javascript
   var mcClient = tizen.mediaController.getClient();
   ```

3. Define a success (and optionally, an error) event handler by implementing the `MediaControllerServerInfoArraySuccessCallback` interface (in [mobile](../../api/latest/device_api/mobile/tizen/mediacontroller.html#MediaControllerServerInfoArraySuccessCallback), [wearable](../../api/latest/device_api/wearable/tizen/mediacontroller.html#MediaControllerServerInfoArraySuccessCallback), and [tv](../../api/latest/device_api/tv/tizen/mediacontroller.html#MediaControllerServerInfoArraySuccessCallback) applications):

   ```javascript
   var mcServerInfo;

   function findSuccessCallback(servers) {
       console.log('Found ' + servers.length + ' servers');
       if (servers.length > 0) {
           mcServerInfo = servers[0];
       }
   }

   function findErrorCallback(e) {
       console.log('Error name: ' + e.name + ' Error message: ' + e.message);
   }
   ```

4. To search for all activated media controller servers, use the `findServers()` method of the `MediaControllerClient` interface (in [mobile](../../api/latest/device_api/mobile/tizen/mediacontroller.html#MediaControllerClient), [wearable](../../api/latest/device_api/wearable/tizen/mediacontroller.html#MediaControllerClient), and [tv](../../api/latest/device_api/tv/tizen/mediacontroller.html#MediaControllerClient) applications):

   ```javascript
   mcClient.findServers(findSuccessCallback, findErrorCallback);
   ```

## Managing Requests

To manage the media controller features in your application, you must learn to handle requests from the client to the server:

1. Create a `MediaControllerChangeRequestPlaybackInfoCallback` object (in [mobile](../../api/latest/device_api/mobile/tizen/mediacontroller.html#MediaControllerChangeRequestPlaybackInfoCallback), [wearable](../../api/latest/device_api/wearable/tizen/mediacontroller.html#MediaControllerChangeRequestPlaybackInfoCallback), and [tv](../../api/latest/device_api/tv/tizen/mediacontroller.html#MediaControllerChangeRequestPlaybackInfoCallback) applications) to define listeners for getting the requests from a client.
  Each listener must invoke the appropriate function to perform the related update on the server and send an appropriate notification to the client. For example, the `onplaybackstaterequest` listener must use the `updatePlaybackState()` method to update the playback state.

   ```javascript
   var requestPlaybackInfoCb = {
       onplaybackstaterequest: function(state, clientName) {
           console.log('Request to change the playback state to: ' + state);
           mcServer.updatePlaybackState(state);
       },
       onplaybackpositionrequest: function(position, clientName) {
           console.log('Request to change the playback position to: ' + position);
           mcServer.updatePlaybackPosition(position);
       },
       onshufflemoderequest: function(mode, clientName) {
           console.log('Request to change the playback shuffle mode to: ' + (mode ? 'TRUE' : 'FALSE'));
           mcServer.updateShuffleMode(mode);
       },
       onrepeatmoderequest: function(mode, clientName) {
           console.log('Request to change the playback repeat mode to: ' + (mode ? 'TRUE' : 'FALSE'));
           mcServer.updateRepeatMode(mode);
       },
       onplaybackitemrequest: function(playlistName, index, state, position, clientName) {
           console.log("Playlist: " + playlistName + " index: " + index + " state: " + state + " position " + position + " requested by " + clientName);
       }
   };
   ```

2. Add the listeners defined in the `MediaControllerChangeRequestPlaybackInfoCallback` object to the server:

   ```javascript
   var watchId = mcServer.addChangeRequestPlaybackInfoListener(requestPlaybackInfoCb);
   ```

   The `watchId` variable stores the value, which can be used in the future to remove the listeners from the server using the `removeChangeRequestPlaybackInfoListener()` method.

3. At the client side, before sending a request, define optional success and error callbacks:

   ```javascript
   function successCallback() {
       console.log('Playback has been paused.');
   }

   function errorCallback(e) {
       console.log('Error name: ' + e.name + ' Error message: ' + e.message);
   }
   ```

4. You can send a request from the client using the `sendPlaybackState()`, `sendPlaybackPosition()`, `sendShuffleMode()`, or `sendRepeatMode()` method of the `MediaControllerServerInfo` interface (in [mobile](../../api/latest/device_api/mobile/tizen/mediacontroller.html#MediaControllerServerInfo), [wearable](../../api/latest/device_api/wearable/tizen/mediacontroller.html#MediaControllerServerInfo), and [tv](../../api/latest/device_api/tv/tizen/mediacontroller.html#MediaControllerServerInfo) applications).
   In the following example, send a request for the changing the playback state to paused using the `sendPlaybackState()` method:

   ```javascript
   mcServerInfo.sendPlaybackState('PAUSE', successCallback, errorCallback);
   ```

## Setting and Getting Server Icon URI

You can update the icon URI address of a media controller server, which can then be accessed
from the client application. The default value of the server icon URI attribute is null.
To use the icon URI attribute in your media controller application, follow these steps:

1. Set the server icon on the server side:

    ```javascript
    var mcServer = tizen.mediacontroller.createServer();
    mcServer.updateIconURI("icon.png");
    ```

2. Get the server icon URI on the client side:

    ```javascript
    var mcClient = tizen.mediacontroller.getClient();
    var mcServerInfo = mcClient.getLatestServerInfo();
    console.log(mcServerInfo.iconURI);
    ```

## Receiving Notifications from Server

To manage the media controller features in your application, you must learn to receive notifications from the server:

1. Define the needed variable:

   ```javascript
   var watcherId;
   ```

2. Define the event handlers for different notifications by implementing the `MediaControllerPlaybackInfoChangeCallback` interface (in [mobile](../../api/latest/device_api/mobile/tizen/mediacontroller.html#MediaControllerPlaybackInfoChangeCallback), [wearable](../../api/latest/device_api/wearable/tizen/mediacontroller.html#MediaControllerPlaybackInfoChangeCallback), and [tv](../../api/latest/device_api/tv/tizen/mediacontroller.html#MediaControllerPlaybackInfoChangeCallback) applications):

   ```javascript
   var playbackListener = {
       onplaybackchanged: function(state, position) {
           console.log('Current playback state: ' + state);
           console.log('Current playback position: ' + position);
       },
       onshufflemodechanged: function(mode) {
           console.log('Shuffle mode changed to: ' + mode);
       },
       onrepeatmodechanged: function(mode) {
           console.log('Repeat mode changed to: ' + mode);
       },
       onmetadatachanged: function(metadata) {
           console.log('Playback metadata changed: ' + JSON.stringify(metadata));
       }
   };
   ```

3. Register the listener to start receiving notifications about playback changes:

   ```javascript
   watcherId = mcServerInfo.addPlaybackInfoChangeListener(playbackListener);
   ```

4. To stop receiving notifications, use the `removePlaybackInfoChangeListener()` method:

   ```javascript
   mcServerInfo.removePlaybackInfoChangeListener(watcherId);
   ```

## Sending and Receiving Custom Commands

To manage the media controller features in your application, you must learn to send custom commands:

<a name="send_custom_commands"></a>

1. On the client side:

   1. Define your custom command:

      ```javascript
      var exampleCustomCommandData = new tizen.Bundle({
          myFilter: 'rock'
      });
      ```

   2. Define a success (and optionally, an error) callback implementing the `MediaControllerSendCommandSuccessCallback` interface (in [mobile](../../api/latest/device_api/mobile/tizen/mediacontroller.html#MediaControllerSendCommandSuccessCallback), [wearable](../../api/latest/device_api/wearable/tizen/mediacontroller.html#MediaControllerSendCommandSuccessCallback), and [tv](../../api/latest/device_api/tv/tizen/mediacontroller.html#MediaControllerSendCommandSuccessCallback) applications):

      ```javascript
      function sendCommandSuccessCallback(data, code) {
          console.log('Server replied with return data: ' + JSON.stringify(data) + ' and code: ' + code);
      }

      function sendCommandErrorCallback(e) {
          console.log('Error name: ' + e.name + ' Error message: ' + e.message);
      }
      ```

   3. Send the command to the server using the `sendCommand()` method:

      ```javascript
      mcServerInfo.sendCommand('myPlaylistFilter', exampleCustomCommandData, sendCommandSuccessCallback, sendCommandErrorCallback);
      ```

<a name="receive_custom_commands"></a>

2. On the server side:

   1. Create the `MediaControllerReceiveCommandCallback` object (in [mobile](../../api/latest/device_api/mobile/tizen/mediacontroller.html#MediaControllerReceiveCommandCallback), [wearable](../../api/latest/device_api/wearable/tizen/mediacontroller.html#MediaControllerReceiveCommandCallback), and [tv](../../api/latest/device_api/tv/tizen/mediacontroller.html#MediaControllerReceiveCommandCallback) applications) to define a listener for receiving custom commands from a client:

      ```javascript
      var commandReceiveListener = function(client, command, data) {
          console.log('command: ' + command + ' client: ' + client + ' data: ' + JSON.stringify(data));

          return new tizen.mediacontroller.RequestReply(new tizen.Bundle({reply: 'response from server'}), 7);
      };
      ```

      The callback within the listener returns the object with the response to the client. The client can obtain this value as an argument of the success callback of the `sendCommand()` method that it used to send the command.

   2. Add the listener defined in the `MediaControllerReceiveCommandCallback` object to the server:

      ```javascript
      var watcherId = mcServer.addCommandListener(commandReceiveListener);
      ```

      The `watcherId` variable stores the value, which can be used in the future to remove the listener from the server using the `removeCommandListener()` method.

## Sending and Receiving Custom Events

Custom command enables the client application to talk to the server application.
The communication in the opposite direction is done with the help of custom events.

<a name="receive_custom_events"></a>

1. To listen to the custom events on the client-side:

   1. Define your custom event listener callback function:

      ```javascript
      function eventReceivedCallback(serverId, event, data) {
          console.log('Event ' + event + ' received from ' + serverId);
          console.log('Event data: ' + JSON.stringify(data));

          var status = 0;
          var data = {'test': 'data'};
          return tizen.mediacontroller.RequestReply(data, status);
      }
      ```

      Event handler function can return the `RequestReply` object which will be sent back to the event author.
      `RequestReply` consists of status code integer and bundle data object.

   2. Set the events listener:

      ```javascript
      mcClient.setCustomEventListener(eventReceivedCallback);
      ```

   3. Disable the events listener, when your application is no longer listening to the custom events:

      ```javascript
      mcClient.unsetCustomEventListener();
      ```

<a name="send_custom_events"></a>

2. To send the custom events on the server-side:

   1. Define the name and data of the custom event parameters:

      ```javascript
      var eventName = 'HelloWorld';
      var eventData = new tizen.Bundle({'testKey': 'testValue'});
      ```

   2. Prepare reply callback function:

      ```javascript
      function eventReplyReceived(data, code) {
          console.log('client reply code: ' + code);
          console.log('client reply data: ' + JSON.stringify(data));
      }
      ```

   3. Retrieve the recipient client info object:

      ```javascript
      var recipient = mcServer.getAllClientsInfo()[0];
      ```

      This example assumes that there is only one client application currently running on the device.
      Otherwise, iterate all the `MediaControllerClientInfo` objects returned by the `getClientInfo()`
      method to select the recipient.

   4. Send the event:

      ```javascript
      recipient.sendEvent(eventName, eventData, eventReplyReceived);
      ```

## Sending and Receiving Search Requests from Client to Server

Client application can send search requests, which consist of a collection of search conditions.
Server listens for the incoming search requests and handles them accordingly.
After handling a request, server sends a response to the client that sent the request.

### Receiving Search Request

To receive and handle search request on the server, follow these steps:

1. Get server handle:

    ```javascript
    var mcServer = tizen.mediacontroller.createServer();
    ```

2. Define search request callback:

    ```javascript
    function searchRequestCallback(client, request) {
        console.log(client);
        console.log(request);

        // You can return RequestReply object, which will be sent to the client
        // who can handle it in search request reply callback.
        return new tizen.mediacontroller.RequestReply(123, {"someData": "someValue"});
    }
    ```

3. Register search request listener:

    ```javascript
    mcServer.setSearchRequestListener(searchRequestCallback);
    ```

### Sending Search Request

To send the search request from the client application, follow these steps:

1. Get client handle:

    ```javascript
    var mcClient = tizen.mediacontroller.getClient();
    ```

2. Get server connection:

    ```javascript
    var mcServerInfo = mcClient.getLatestServerInfo();
    ```

3. Prepare search request, which is an array of SearchFilter objects:

    ```javascript
    var request = [
        new tizen.mediacontroller.SearchFilter('MUSIC', 'TITLE', 'tizen'),
        new tizen.mediacontroller.SearchFilter('MUSIC', 'ARTIST', 'samsung')
    ];
    ```

4. Define reply callback:

    ```javascript
    function searchReplyCallback(reply) {
        console.log("server reply status code: " + reply.code);
        console.log("server reply data: " + reply.data);
    }
    ```

5. Send search request:

    ```javascript
    mcServerInfo.sendSearchRequest(request, searchReplyCallback);
    ```

## Setting Content Type for Currently Playing Media

Server can set content type for current playback. Client can access this type (read-only)
and perform some actions that depend on the content-type, such as displaying different icons for
different types of media items.

1. Setting content type on the server side:

    ```javascript
    mcServer.updatePlaybackContentType("VIDEO");
    ```

2. Accessing content type on the client side:

    ```javascript
    var type = mcServerInfo.playbackInfo.contentType;
    if (type == "VIDEO") {
        console.log("playing video");
    }
    else if (type == "MUSIC") {
        console.log("playing song");
    }
    ```


## Setting Content Age Rating for Currently Playing Media

Server can set age rating for current playback. Client can access this rating (read-only) and perform some actions such as displaying a warning for underage users.

1. Setting content age rating on the server side:

    ```javascript
    mcServer.updatePlaybackAgeRating("18");
    ```

2. Accessing content age rating on the client side:

    ```javascript
    var userAge = 17; // App developer should retrieve actual user age from user profile.
    var rating = mcServerInfo.playbackInfo.ageRating;
    if (rating > userAge) {
        console.log("Warning: this content has age rating " + rating + "+.";
    }
    ```

## Managing Playlists on Server Side

To manage the media controller playlists in your server application, you must learn to create, save, and delete playlists.

1. To create a media controller playlist, use the `createPlaylist()` method:

   ```javascript
   var playlist = mcServer.createPlaylist("testPlaylistName");
   ```

2. To add item to playlist, use the `addItem()` method:

   ```javascript
   var metadata = {
       title: "testTitle",
       artist: "testArtist",
       album: "testAlbum",
       author: "testAuthor",
       genre: "testGenre",
       duration: "testDuration",
       date: "testDate",
       copyright: "testCopyright",
       description: "testDescription",
       trackNum: "testTrackNum",
       picture: "testPicture",
       seasonNumber: 1,
       seasonTitle: "testSeasonTitle",
       episodeNumber: 1,
       episodeTitle: "testEpisodeTitle",
       resolutionWidth: 1600,
       resolutionHeight: 900
   };

   playlist.addItem("index1", metadata);
   ```

3. To save playlist, use the `savePlaylist()` method:

   ```javascript
   function successCallback() {
       console.log("savePlaylist successful.");
   }

   function errorCallback(error) {
       console.log("savePlaylist failed with error: " + error);
   }
   mcServer.savePlaylist(successCallback, errorCallback);
   ```

4. To get information about playlists, use the `getAllPlaylists()` method:

   ```javascript
   function successCallback(playlists) {
       playlists.forEach(function(playlist) {
           console.log("Playlist name: " + playlist.name);
       });
   }
   function errorCallback(error) {
       console.log("getAllPlaylists failed with error: " + error);
    }
   mcServer.getAllPlaylists(successCallback, errorCallback);
   ```

5. To get information about playlist items, use the `getItems()` method:

   ```javascript
   function successCallback(items) {
       items.forEach(function(item) {
           console.log("Index: " + item.index + " Title: " + item.metadata.title);
       });
   }
   function errorCallback(error) {
       console.log("getItems failed with error: " + error);
   }
   playlist.getItems(successCallback, errorCallback);
   ```

6. To delete playlist, use the `deletePlaylist()` method:

   ```javascript
   function deleteSuccess() {
       console.log("deletePlaylist successful.");
   }
   function deleteFailure(error) {
       console.log("deletePlaylist failed with error: " + error);
   }
   mcServer.deletePlaylist(playlist.name, deleteSuccess, deleteFailure);
   ```

## Managing Playlists on Client Side

To manage the media controller playlist in your application, you must handle requests from the client to the server:

1. Send a request from the client using the `sendPlaybackItem()` method of the `MediaControllerServerInfo` interface (in [mobile](../../api/latest/device_api/mobile/tizen/mediacontroller.html#MediaControllerServerInfo), [wearable](../../api/latest/device_api/wearable/tizen/mediacontroller.html#MediaControllerServerInfo), and [tv](../../api/latest/device_api/tv/tizen/mediacontroller.html#MediaControllerServerInfo) applications).

   ```javascript
   mcServerInfo.sendPlaybackItem("testPlaylistName", "index1", "PLAY", 0);
   ```

2. Define the event handlers for different notifications by implementing the `MediaControllerPlaylistUpdatedCallback` interface (in [mobile](../../api/latest/device_api/mobile/tizen/mediacontroller.html#MediaControllerPlaylistUpdatedCallback), [wearable](../../api/latest/device_api/wearable/tizen/mediacontroller.html#MediaControllerPlaylistUpdatedCallback), and [tv](../../api/latest/device_api/tv/tizen/mediacontroller.html#MediaControllerPlaylistUpdatedCallback) applications):

   ```javascript
   var listener = {
       onplaylistupdated: function(playlist) {
           console.log("updated playlist " + playlist.name);
       },
       onplaylistdeleted: function(playlistName) {
           console.log("deleted playlist " + playlistName);
       }
   };
   ```

3. Register the listener to start receiving notifications about playlist changes:

   ```javascript
   watcherId = mcServerInfo.addPlaylistUpdatedListener(listener);
   ```

4. To stop receiving notifications, use the `removePlaylistUpdatedListener()` method:

   ```javascript
   mcServerInfo.removePlaylistUpdatedListener(watcherId);
   ```

## Media Controller Server Abilities

Various abilities can be set to give the information to the clients about the supported features. These abilities can be divided into two groups:

1. Media controller simple abilities

    Each ability is described by a single value of `MediaControllerAbilitySupport` (in [mobile](../../api/latest/device_api/mobile/tizen/mediacontroller.html#MediaControllerAbilitySupport), [wearable](../../api/latest/device_api/wearable/tizen/mediacontroller.html#MediaControllerAbilitySupport), and [tv](../../api/latest/device_api/tv/tizen/mediacontroller.html#MediaControllerAbilitySupport) applications)  and is not a part of a complex ability structure:

    - PLAYBACK_POSITION: Changing playback position.
    - SHUFFLE: Changing shuffle mode.
    - REPEAT: Changing repeat state.
    - PLAYLIST: Adding/changing/removing playlists.
    - CLIENT_CUSTOM: Receiving custom commands from media controller clients.
    - SEARCH: Receiving search requests from media controller clients.
    - SUBTITLES: Receiving requests for subtitles mode change from media controller clients.
    - MODE_360: Receiving requests for spherical (360&deg;) mode change from media controller clients.

2. Media controller complex abilities

    Each ability consists of several types:

    - playback: Server playback actions.
    - displayRotation: Setting display orientations.
    - displayMode: Setting display modes.

### Setting Media Controller Server Abilities

You can set the media server abilities as follows:

```javascript
mcServer.abilities.playback.next = "YES";
mcServer.abilities.playback.prev = "YES";
mcServer.abilities.playback.rewind = "NO";
mcServer.abilities.playback.forward = "NO";

mcServer.abilities.playback.saveAbilities();

mcServer.abilities.displayMode.fullScreen = "YES";
mcServer.abilities.displayRotation.rotation180 = "YES";
```

### Checking Media Controller Server Abilities

Using `saveAbilities()` is required to save changes of playback abilities into database, otherwise changes will have no effect on the device and clients will not be notified about an update. Other abilities are updated instantly and there is no need to manually save these abilities.

To get abilities of the server on the client side:

```javascript
var mcClient = tizen.mediacontroller.getClient();
var mcServerInfo = mcClient.getLatestServerInfo();

console.log("ability NEXT: " + mcServerInfo.abilities.playback.next);
console.log("ability PREV: " + mcServerInfo.abilities.playback.prev);
console.log("ability REWIND: " + mcServerInfo.abilities.playback.rewind);
console.log("ability FORWARD: " + mcServerInfo.abilities.playback.forward);
```

### Monitoring Media Controller Server Abilities

You can monitor changes of server abilities using the `addAbilityChangeListener` method on client side. You will also receive the notifications about every ability change on the server side:

```javascript
/* Client-side code */
var mcClient = tizen.mediacontroller.getClient();

var listener = {
    onplaybackabilitychanged: function(server, ability) {
        console.log("playback ability changed, server name: " + server.name +
            ", abilities: ");
        console.log(JSON.stringify(ability));
    },
    ondisplayrotationabilitychanged: function(server, ability) {
        console.log("display rotation ability changed, server name: " +
            server.name + ", ability: ");
        console.log(JSON.stringify(ability));
    },
    ondisplaymodeabilitychanged: function(server, ability) {
        console.log("displayMode ability changed, server name: " + server.name +
            ", abilities: ");
        console.log(JSON.stringify(ability));
    },
    onsimpleabilitychanged: function(server, type, ability) {
        console.log(type + " ability changed, server name: " + server.name +
            ", ability: " + ability);
    }
};

var watchId = mcClient.addAbilityChangeListener(listener);

/* Server-side code */
var mcServer = tizen.mediacontroller.createServer();
mcServer.abilities.playback.play = "YES";
mcServer.abilities.playback.saveAbilities();
mcServer.abilities.shuffle = "NO";
mcServer.abilities.repeat = "YES";
```


You will receive the information about the ability changes in every active media controller server. To receive the information only from selected servers, call `subscribe()`:

```javascript
var mcClient = tizen.mediacontroller.getClient();
var mcServerInfo = mcClient.getLatestServerInfo();
mcServerInfo.abilities.subscribe();
```

After the first use of `subscribe()`, you will stop receiving changes from not subscribed servers.

You can stop monitoring the specific server, using the analogical `unsubscribe()` method. In case, if no server is subscribed, notifications from all active servers will be sent.


## Media Controller Server Features

Media controller API provides the following methods to change and monitor server features:
- Subtitles
- Mode360
- DisplayMode
- DisplayRotation

From server side, you can monitor the client requests for its features by using the corresponding change request listener:

```javascript
var watcherId = 0;  /* Watcher identifier. */
var mcClient = tizen.mediacontroller.getClient();
var mcServerInfo = mcClient.getLatestServerInfo();

/* Registers to be notified when display rotation changes. */
watcherId =
    mcServerInfo.displayRotation.addDisplayRotationChangeListener(function(
        rotation) {
        console.log(mcServerInfo.name + " server display rotation changed to " +
                    rotation);
    });

/* Cancels the watch operation. */
mcServerInfo.displayRotation.removeDisplayRotationChangeListener(watcherId);
```

From the client side you can send the request for changing the specific feature of the server by using the `sendRequest()` method. Request can be sent only after [enabling specific ability](#media-controller-server-abilities) on the server side:

```javascript
var mcClient = tizen.mediacontroller.getClient();
var mcServerInfo = mcClient.getLatestServerInfo();

var rotation = "ROTATION_180";
mcServerInfo.displayRotation.sendRequest(rotation, function(data, code) {
    console.log("Server replied with return data: " + JSON.stringify(data) + " and code: " + code);
});
```

Server can reply to the client requests by the `RequestReply` object:

```javascript
var watcherId = 0; /* Watcher identifier. */
var mcServer = tizen.mediacontroller.createServer();

var changeListener = function(clientName, rotation) {
    console.log("Display rotation change requested to: " + rotation + " by " +
                clientName);
    var result = false;
    /* do some action here and return according to the result */
    if (!result) {
        return new tizen.mediacontroller.RequestReply(
            new tizen.Bundle({"message" : "Error - Not allowed"}), 13);
    }
    return new tizen.mediacontroller.RequestReply(
        new tizen.Bundle({"message" : "Success"}), 0);
};

/* Registers to receive display rotation change requests from clients. */
watcherId = mcServer.displayRotation.addChangeRequestListener(changeListener);
```



## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
  - Tizen 5.0 and Higher for TV
