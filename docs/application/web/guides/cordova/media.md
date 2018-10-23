# Media Playback and Recording

You can play and record audio files using various functionalities, such as play, stop, pause, volume change, and seek to position.

The Media API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The main features of the Media API include:

- Playing audio files

  You can [start audio file playback](#playing-audio-files).

- Seeking position

  You can [change the playing position](#seeking-position).

- Changing the volume

  You can [change the volume during playback](#changing-the-volume).

- Using playback callbacks

  You can [use callbacks](#using-playback-callbacks) to handle playback success and errors, and various status events.

- Getting the duration and position

  You can [get the duration of the audio file, and retrieve the current position](#getting-the-duration-and-position).

- Recording audio

  You can [start and stop recording](#recording-audio).

## Prerequisites

To enable your application to use the media functionality:

1. To perform any Cordova-related operations, you must wait until Cordova is fully set up (the `deviceready` event occurs):

   ```
   document.addEventListener('deviceready', onDeviceReady, false);

   function onDeviceReady() {
       console.log('Cordova features now available');
   }
   ```

2. To use the Media API (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/media.html), [wearable](../../api/latest/device_api/wearable/tizen/cordova/media.html), and [TV](../../api/latest/device_api/tv/tizen/cordova/media.html) applications), the application has to request permission by adding the following privileges to the `config.xml` file:

   ```
   <!--To record audio-->
   <tizen:privilege name="http://tizen.org/privilege/mediacapture"/>
   <!--To change the volume during playback-->
   <tizen:privilege name="http://tizen.org/privilege/volume.set"/>
   ```

## Playing Audio Files

To implement simple audio file playback, where the audio is played from the beginning to the end:

1. Place the audio file in a directory on a device. In this example, it is in the owner home directory: `/home/owner/content/Music/play.mp3`.

2. Construct a new media object from the audio file. No additional parameters are required.

   ```
   var myMedia = new Media('file:///home/owner/content/Music/play.mp3');
   ```

3. Call the `play()` method:

   ```
   myMedia.play();
   ```

Release the media resources when they are no longer needed.

## Seeking Position

To change the position of the played file:

1. Construct a new media object from the audio file.

   ```
   var myMedia = new Media('file:///home/owner/content/Music/play.mp3');
   ```

2. Start playing:

   ```
   myMedia.play();
   ```

3. After 5 seconds, seek the position of 10 seconds.

   A timer is registered using the `setTimeout()` global function.

   ```
   setTimeout(function() {
       myMedia.seekTo(10000);
       console.log('Playback position has been set to 10 seconds.');
   }, 5000);
   ```

4. Stop the media and release after 10 seconds:

   ```
   setTimeout(function() {
       myMedia.release();
   }, 10000);
   ```

## Changing the Volume

To change the volume during playback:

1. Construct a new media object from the audio file:

   ```
   var myMedia = new Media('file:///home/owner/content/Music/play.mp3');
   ```

2. Start playing:

   ```
   myMedia.play();
   ```

3. Mute the volume after 2 seconds:

   ```
   setTimeout(function() {
       myMedia.setVolume(0.0);
   }, 2000);
   ```

4. Set volume to 1.0 after 5 seconds:

   ```
   setTimeout(function() {
       myMedia.setVolume(1.0);
   }, 5000);
   ```

## Using Playback Callbacks

You can monitor the playback status changes by defining a status callback for the `Media` constructor (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/media.html#Media), [wearable](../../api/latest/device_api/wearable/tizen/cordova/media.html#Media), and [TV](../../api/latest/device_api/tv/tizen/cordova/media.html#Media) applications). Each time the status changes, the defined callback is called with a status constant as a parameter. The following table lists the available status constants.

**Table: Playback status changes**

| Constant               | Description           |
| ---------------------- | --------------------- |
| `Media.MEDIA_NONE`     | File has no status.   |
| `Media.MEDIA_STARTING` | Playback is starting. |
| `Media.MEDIA_RUNNING`  | Playback is running.  |
| `Media.MEDIA_PAUSED`   | Playback is paused.   |
| `Media.MEDIA_STOPPED`  | Playback is stopped.  |

To handle playback callbacks:

1. Define a success callback, which is called when the playback finishes successfully:

   ```
   var successCallback = function() {
       console.log('Audio file has been played back.');
   };
   ```

2. Define an error callback, which is called when an error occurs. The only parameter contains the error code (for a list of error codes, see the `MediaError` API Reference in [mobile](../../api/latest/device_api/mobile/tizen/cordova/media.html#MediaError), [wearable](../../api/latest/device_api/wearable/tizen/cordova/media.html#MediaError), and [TV](../../api/latest/device_api/tv/tizen/cordova/media.html#MediaError) applications).

   ```
   var errorCallback = function(err) {
       console.log('An error occurred: ' + err.code);
   };
   ```

3. Define a status callback, which is called when a playback event (such as preparing to playback, running, paused, and stopped) occurs:

   ```
   var statusCallback = function(status) {
       switch (status) {
           case Media.MEDIA_NONE: console.log('Audio file status is none');
               break;
           case Media.MEDIA_STARTING: console.log('Audio file is starting');
               break;
           case Media.MEDIA_RUNNING: console.log('Audio file is running');
               break;
           case Media.MEDIA_PAUSED: console.log('Audio file is paused');
               break;
           case Media.MEDIA_STOPPED: console.log('Audio file is stopped');
               break;
           default: console.log('Audio file status unknown');
               break;
       }
   };
   ```

4. Construct a new media object and pass the callbacks as parameters.

   Since the callbacks are optional, you do not need to provide them all. However, to monitor status changes, you must provide the status callback defined in the previous step.

   ```
   var src = 'file:///home/owner/content/Music/play.mp3';
   var myMedia = new Media(src, successCallback, errorCallback, statusCallback);
   ```

5. Start playing:

   ```
   myMedia.play();
   ```

6. Test the callbacks by pausing and resuming playback after 3 and 5 seconds:

   ```
   setTimeout(function() {
       myMedia.pause();
   }, 3000);

   setTimeout(function() {
       myMedia.play();
   }, 5000);
   ```

## Getting the Duration and Position

To get the duration of the audio file, and retrieve the current position:

1. Construct a new media object from an audio file:

   ```
   var myMedia = new Media('file:///home/owner/content/Music/play.mp3');
   ```

2. Get the duration and print it to the system log. The -1 value means that the duration is unknown.

   ```
   console.log('Audio duration in seconds is ' + myMedia.getDuration());
   ```

3. Start playing:

   ```
   myMedia.play();
   ```

4. The method for getting the current position is asynchronous, so a callback is used. Define the callback:

   ```
   var positionCallback = function(position) {
       console.log('Current position in seconds is ' + position);
   };
   ```

5. Define the optional callback for errors in retrieving the position. For the specific error codes, see the `MediaError` API Reference (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/media.html#MediaError), [wearable](../../api/latest/device_api/wearable/tizen/cordova/media.html#MediaError), and [TV](../../api/latest/device_api/tv/tizen/cordova/media.html#MediaError) applications).

   ```
   var errorCallback = function(err) {
       console.log('An error occurred: ' + err.code);
   };
   ```

6. Request the position. The result is passed asynchronously to the callback function.

   ```
   myMedia.getCurrentPosition(positionCallback, errorCallback);
   ```

7. You can set a timer to get the position 5 seconds later:

   ```
   setTimeout(function() {
       myMedia.getCurrentPosition(positionCallback, errorCallback);
   }, 5000);
   ```

   Something similar to the following example is shown in the system log:

   ```
   Current position in seconds is 0
   Current position in seconds is 4.919
   ```

## Recording Audio

To start and stop recording:

1. Define the optional success and error callbacks:

   ```
   var successCallback = function() {
       console.log('Started recording audio file.');
   };

   var errorCallback = function(err) {
       console.log('Error occurred ' + err.code);
   };
   ```

2. Construct a media object and pass the name for the new audio file:

   ```
   var myMedia = new Media('recording.mp3', successCallback, errorCallback);
   ```

3. Start recording:

   ```
   myMedia.startRecord();
   ```

4. Stop recording after 10 seconds and release the media object:

   ```
   setTimeout(function() {
       myMedia.stopRecord();
       console.log('Stopped recording an audio file.');
       myMedia.release();
   }, 10000);
   ```

   Always release the media object when no longer needed.


## Related Information
* Dependencies   
   - Tizen 3.0 and Higher for Mobile
   - Tizen 3.0 and Higher for Wearable
   - Tizen 3.0 and Higher for TV
