# Media Controller

You can have your client application communicate with a media server.

This feature is supported in mobile and wearable applications only.

To manage the media using the Media Controller API, you have to develop 2 applications:

- Client that sends requests to the server in order to change, for example, the playback state and position modes.
- Server that directly manages the media on the device.

The main features of the Media Controller API include:

- Setting up the client and server pair      

  You can [set up the client and server pair](#getting-the-client-and-server) by creating a new server using the `createServer()` method. On the client side, you can get a client and find active servers using the `getClient()` and `findServers()` methods.

- Managing requests      

  You can [send a request](#managing-requests) from the client to the server to modify various playback attributes. In the server, you can set up a listener to react to the client request and perform the requested task.

- Receiving notifications from the server

  You can [receive notifications on changes made by the server](#receiving-notifications-from-the-server) by registering a listener with the `addPlaybackInfoChangeListener()` method.

- Sending custom commands

  You can [use the client to send commands](#send_custom_commands) with the `sendCommand()` method.

  To [receive and handle incoming commands](#receive_custom_commands) in the server, use the `addCommandListener()` method.

## Prerequisites

To use the Media Controller API (in [mobile](../../api/latest/device_api/mobile/tizen/mediacontroller.html) and [wearable](../../api/latest/device_api/wearable/tizen/mediacontroller.html) applications), the application has to request permission by adding the following privileges to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/mediacontroller.client"/>
<tizen:privilege name="http://tizen.org/privilege/mediacontroller.server"/>
```

## Getting the Client and Server

To manage the media controller features in your application, you must learn to set up the client and server pair:

1. Create a media controller server using the `createServer()` method:

   ```
   var mcServer = tizen.mediacontroller.createServer();
   ```

2. Get the client using the `getClient()` method:

   ```
   var mcClient = tizen.mediaController.getClient();
   ```

3. Define a success (and optionally, an error) event handler by implementing the `MediaControllerServerInfoArraySuccessCallback` interface (in [mobile](../../api/latest/device_api/mobile/tizen/mediacontroller.html#MediaControllerServerInfoArraySuccessCallback) and [wearable](../../api/latest/device_api/wearable/tizen/mediacontroller.html#MediaControllerServerInfoArraySuccessCallback) applications):

   ```
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

4. To search for all activated media controller servers, use the `findServers()` method of the `MediaControllerClient` interface (in [mobile](../../api/latest/device_api/mobile/tizen/mediacontroller.html#MediaControllerClient) and [wearable](../../api/latest/device_api/wearable/tizen/mediacontroller.html#MediaControllerClient) applications):

   ```
   mcClient.findServers(findSuccessCallback, findErrorCallback);
   ```

## Managing Requests

To manage the media controller features in your application, you must learn to handle requests from the client to the server:

1. Create a `MediaControllerChangeRequestPlaybackInfoCallback` object (in [mobile](../../api/latest/device_api/mobile/tizen/mediacontroller.html#MediaControllerChangeRequestPlaybackInfoCallback) and [wearable](../../api/latest/device_api/wearable/tizen/mediacontroller.html#MediaControllerChangeRequestPlaybackInfoCallback) applications) to define listeners for getting the requests from a client.  
  Each listener must invoke the appropriate function to perform the related update on the server and send an appropriate notification to the client. For example, the `onplaybackstaterequest` listener must use the `updatePlaybackState()` method to update the playback state.

   ```
   var requestPlaybackInfoCb = {
       onplaybackstaterequest: function(state) {
           console.log('Request to change the playback state to: ' + state);
           mcServer.updatePlaybackState(state);
       },
       onplaybackpositionrequest: function(position) {
           console.log('Request to change the playback position to: ' + position);
           mcServer.updatePlaybackPosition(position);
       },
       onshufflemoderequest: function(mode) {
           console.log('Request to change the playback shuffle mode to: ' + (mode ? 'TRUE' : 'FALSE'));
           mcServer.updateShuffleMode(mode);
       },
       onrepeatmoderequest: function(mode) {
           console.log('Request to change the playback repeat mode to: ' + (mode ? 'TRUE' : 'FALSE'));
           mcServer.updateRepeatMode(mode);
       }
   };
   ```

2. Add the listeners defined in the `MediaControllerChangeRequestPlaybackInfoCallback` object to the server:

   ```
   var watchId = mcServer.addChangeRequestPlaybackInfoListener(requestPlaybackInfoCb);
   ```

   The `watchId` variable stores the value, which can be used in the future to remove the listeners from the server using the `removeChangeRequestPlaybackInfoListener()` method.

3. At the client side, before sending a request, define optional success and error callbacks:

   ```
   function successCallback() {
       console.log('Playback has been paused.');
   }

   function errorCallback(e) {
       console.log('Error name: ' + e.name + ' Error message: ' + e.message);
   }
   ```

4. You can send a request from the client using the `sendPlaybackState()`, `sendPlaybackPosition()`, `endShuffleMode()`, or `sendRepeatMode()` method of the `MediaControllerServerInfo` interface (in [mobile](../../api/latest/device_api/mobile/tizen/mediacontroller.html#MediaControllerServerInfo) and [wearable](../../api/latest/device_api/wearable/tizen/mediacontroller.html#MediaControllerServerInfo) applications).  
   In the following example, send a request for the changing the playback state to paused using the `sendPlaybackState()` method:

   ```
   mcServerInfo.sendPlaybackState('PAUSE', successCallback, errorCallback);
   ```

## Receiving Notifications from the Server

To manage the media controller features in your application, you must learn to receive notifications from the server:

1. Define the needed variable:

   ```
   var watcherId;
   ```

2. Define the event handlers for different notifications by implementing the `MediaControllerPlaybackInfoChangeCallback` interface (in [mobile](../../api/latest/device_api/mobile/tizen/mediacontroller.html#MediaControllerPlaybackInfoChangeCallback) and [wearable](../../api/latest/device_api/wearable/tizen/mediacontroller.html#MediaControllerPlaybackInfoChangeCallback) applications):

   ```
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

   ```
   watcherId = mcServerInfo.addPlaybackInfoChangeListener(playbackListener);
   ```

4. To stop receiving notifications, use the `removePlaybackInfoChangeListener()` method:

   ```
   mcServerInfo.removePlaybackInfoChangeListener(watcherId);
   ```

## Sending and Receiving Custom Commands

To manage the media controller features in your application, you must learn to send custom commands:

<a name="send_custom_commands"></a>

1. On the client side:

   1. Define your custom command:

      ```
      var exampleCustomCommandData = {
          myFilter: 'rock'
      };
      ```

   2. Define a success (and optionally, an error) callback implementing the `MediaControllerSendCommandSuccessCallback` interface (in [mobile](../../api/latest/device_api/mobile/tizen/mediacontroller.html#MediaControllerSendCommandSuccessCallback) and [wearable](../../api/latest/device_api/wearable/tizen/mediacontroller.html#MediaControllerSendCommandSuccessCallback) applications):

      ```
      function sendCommandSuccessCallback(response) {
          console.log('Command executed with result: ' + JSON.stringify(response));
      }

      function sendCommandErrorCallback(e) {
          console.log('Error name: ' + e.name + ' Error message: ' + e.message);
      }
      ```

   3. Send the command to the server using the `sendCommand()` method:

      ```
      mcServerInfo.sendCommand('myPlaylistFilter', sendCommandSuccessCallback, sendCommandErrorCallback);
      ```

<a name="receive_custom_commands"></a>

2. On the server side:

   1. Create the `MediaControllerReceiveCommandCallback` object (in [mobile](../../api/latest/device_api/mobile/tizen/mediacontroller.html#MediaControllerReceiveCommandCallback) and [wearable](../../api/latest/device_api/wearable/tizen/mediacontroller.html#MediaControllerReceiveCommandCallback) applications) to define a listener for receiving custom commands from a client:

      ```
      var commandReceiveListener = function(client, command, data) {
          console.log('command: ' + command + ' client: ' + client + ' data: ' + JSON.stringify(data));

          return {reply: 'response from server'};
      };
      ```

      The callback within the listener returns the object with the response to the client. The client can obtain this value as an argument of the success callback of the `sendCommand()` method that it used to send the command.

   2. Add the listener defined in the `MediaControllerReceiveCommandCallback` object to the server:

      ```
      var watcherId = mcServer.addCommandListener(commandReceiveListener);
      ```

      The `watcherId` variable stores the value, which can be used in the future to remove the listener from the server using the `removeCommandListener()` method.

## Related Information
* Dependencies      
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
