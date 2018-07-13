# getUserMedia

You can access multimedia streams, such as camera, on a local device. The feature can be used, for example, for real-time communication, recording, and surveillance.

The main features of the getUserMedia API include:

- Retrieving multimedia streams

  You can use the `navigator.webkitGetUserMedia()` method to request user access to [retrieve the multimedia streams](#accessing-a-video-stream) of local devices, such as camera. The method returns the media as a JSON object.

  > **Note**  
  > The TV applications support the `navigator.webkitGetUserMedia()` method for the microphone only, because a TV has no camera.


- Capturing media

  You can [capture media content](#capturing-a-media-frame) and transform it to various formats.

> **Note**  
> Tizen supports a WebKit-based `GetUserMedia()` method, so always add the `webkit` prefix to the method name.

## Accessing a Video Stream

Learning how to access a video stream is a basic user media management skill:

1. Create the HTML5 video element (in [mobile](../../../api/latest/w3c_api/w3c_api_m.html#video), [wearable](../../../api/latest/w3c_api/w3c_api_w.html#video), and [TV](../../../api/latest/w3c_api/w3c_api_tv.html#video) applications) and a button used to control audio stream access:

   ```
   <body>
      <video id="videoPlay" src="" autoplay controls ></video><br/>
      <input type="button" value="START" onclick="getVideoStream();" id="btnStart"/>
   </body>
   ```

2. Use the `navigator.webkitGetUserMedia()` method to derive audio streams:

   ```
   <script>
       function getVideoStream() {
           navigator.webkitGetUserMedia({video: true}, successCallBack, errorCallBack);
       }
   </script>
   ```

   The first parameter is mandatory and assigns a JSON object to determine which media element (audio or video) to use.

3. Retrieve audio stream information and create stream URL:

   ```
   <script>
       function SuccessCallback(stream) {
           var URL = window.webkitURL;
           document.getElementById('videoPlay').src = URL.createObjectURL(stream);
       }
   </script>
   ```

### Source Code

For the complete source code related to this use case, see the following file:

- [video_stream.html](http://download.tizen.org/misc/examples/w3c_html5/media/get_user_media)

## Capturing a Media Frame

Learning how to capture a frame and display it in a video element is a basic user media management skill:

1. Create a [canvas](../graphics/canvas.md) element and use the `getCapture()` method to capture a frame:

   ```
   <body>
      <video id="videoView" src="" autoplay></video><br/>
      <img id="imgView" src="">
      <canvas id="canvasView" style="display: none;" width="300" height="225"></canvas><br/>
      <input type="button" value="WebCamStart" onclick="getVideoStream();" id="btnPlay"/>
      <input type="button" value="Capture" onclick="getCapture();" id="btnCapture"/>
   </body>
   ```

2. Enable rendering of the retrieved media stream by calling the `webkitGetUserMedia()` method:

   ```
   <script>
       function getVideoStream() {
           navigator.webkitGetUserMedia({video: true}, SuccessCallBack, ErrorCallBack);
       }
       function SuccessCallBack(stream) {
           var URL = window.webkitURL;
           document.getElementById('videoView').src = URL.createObjectURL(stream);
           localStream = stream;
       }
       function ErrorCallBack(e) {
           /* Error handling */
       }
   </script>
   ```

3. Display the captured frame in a [video](./video-audio.md) element using the `drawImage()` method:

   ```
   <script>
       var localStream = '';
       function getCapture() {
           if (localStream) {
               var canvas = document.getElementById('canvasView');
               var context = canvas.getContext('2d');

               context.drawImage(document.getElementById('videoView'), 0, 0, 300, 225);
               document.getElementById('imgView').src = canvas.toDataURL('image/web');
           }
       }
   </script>
   ```

### Source Code

For the complete source code related to this use case, see the following file:

- [capturing_webcam.html](http://download.tizen.org/misc/examples/w3c_html5/media/get_user_media)

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
