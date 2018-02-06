# XMLHttpRequest

You can send HTTP (or HTTPS) [requests](http://www.w3.org/TR/2014/WD-XMLHttpRequest-20140130/#request) to and receive [responses](http://www.w3.org/TR/2014/WD-XMLHttpRequest-20140130/#response) from a Web server using JavaScript. The API is based on the [HTML5](http://www.w3.org/TR/2014/CR-html5-20140429/) specification and the Ajax mechanism widely used in the Web environment, and it has been enhanced from the older [XMLHttpRequest](http://www.w3.org/TR/2012/WD-XMLHttpRequest-20121206/) API.

The main features of the XMLHttpRequest API include:

- Supporting cross-origin request sharing (CORS)

  In the older XMLHttpRequest API, only same-origin resource sharing was possible. However, the latest XMLHttpRequest API supports [CORS](../security/cors.md).

  To [send a cross-origin request](#sending-a-cross-origin-request), you must create an [XMLHttpRequest](http://www.w3.org/TR/2014/WD-XMLHttpRequest-20140130/#dom-xmlhttprequest) interface instance and use its `open()` method. Set the request URL method parameter as the cross-origin URL.

> **Note**  
> For the cross-origin request to work, [the authority for the external domain access must be set](../security/cors.md#using-simple-requests) in the server belonging to the cross-origin URL.

- Supporting various response types

  The older XMLHttpRequest API only supported the `text/html` format for sending requests. The latest XMLHttpRequest API supports various response types, such as `arraybuffer`, `blob`, `document`, `json`, and `text`.

- Supporting form data

  The newly supported [FormData](http://www.w3.org/TR/2014/WD-XMLHttpRequest-20140130/#interface-formdata) interface makes it possible to upload data from an entire form. For more information, see [Uploading Files with Ajax](#uploading-files-with-ajax).

- Receiving a more fragmented response state on the request progress status

  The XMLHttpRequst API provides more [event handlers](http://www.w3.org/TR/2014/WD-XMLHttpRequest-20140130/#event-handlers) for [tracking the request status and response](#handling-request-events). In addition, the `onprogress` event handler allows you to [check the send status of a large capacity file download](#tracking-download-progress-state).

## Sending a Cross-origin Request

To use the XML HTTP request features in your application, you must learn to send a cross-origin request:

1. Create an [XMLHttpRequest](http://www.w3.org/TR/2014/WD-XMLHttpRequest-20140130/#dom-xmlhttprequest) interface instance:

   ```
   <script>
       var client = new XMLHttpRequest();
   ```

2. Open the connection with the `open()` method using the cross-domain URL as a parameter. Send the request with the `send()` method.

   ```
       client.open('GET', 'video_sample.mp4');
       client.send();
   </script>
   ```

	> **Note**  
	> Cross-domain access only works if [the server allows the domain access of the client](../security/cors.md#using-simple-requests).

### Source Code

For the complete source code related to this use case, see the following files:

- [xhr3.html](http://download.tizen.org/misc/examples/w3c_html5/communication/xmlhttprequest_level_2)
- [video_sample.mp4](http://download.tizen.org/misc/examples/w3c_html5/communication/xmlhttprequest_level_2)

## Uploading Files with Ajax

To use the XML HTTP request features in your application, you must learn to upload files in the background with Ajax:

1. Define the input elements for the file upload. Use the `upload()` method for the button click event to upload the file when the button is clicked.

   ```
   <input type="file" id="uploadfile" name="uploadfile"/>
   <input type="button" value="upload" onclick="upload()"/>
   ```

2. In the `upload()` method, create a [FormData](http://www.w3.org/TR/2014/WD-XMLHttpRequest-20140130/#interface-formdata) interface instance, and add the [file](http://www.w3.org/wiki/HTML/Elements/input/file) element with the attached file into it. Use the `send()` method to send the `FormData` to the server.

   ```
   <script>
       var client = new XMLHttpRequest();

       function upload() {
           var file = document.getElementById('uploadfile');

           /* Create a FormData instance */
           var formData = new FormData();
           /* Add the file */
           formData.append('upload', file.files[0]);

           client.open('post', '/upload', true);
           client.setRequestHeader('Content-Type', 'multipart/form-data');
           client.send(formData); /* Send to server */
       }

       /* Check the response status */
       client.onreadystatechange = function() {
           if (client.readyState == 4 && client.status == 200) {
               alert(client.statusText);
           }
       };
   </script>
   ```

### Source Code

For the complete source code related to this use case, see the following file:

- [xhr1.html](http://download.tizen.org/misc/examples/w3c_html5/communication/xmlhttprequest_level_2)

## Handling Request Events

To use the XML HTTP request features in your application, you must learn to track requests through events:

1. Define a text element in which to display the request event results:

   ```
   <div id="divText"></div>
   ```

2. Create an [XMLHttpRequest](http://www.w3.org/TR/2014/WD-XMLHttpRequest-20140130/#dom-xmlhttprequest) interface instance and define event handlers for it:

   ```
   <script>
       var html = '';

       var client = new XMLHttpRequest();

       /* Event handlers */
       client.onloadstart = onloadstarthandler;
       client.onprogress = onprogresshandler;
       client.onabort = onaborthandler;
       client.onerror = onerrorhandler;
       client.onload = onloadhandler;
       client.ontimeout = ontimeouthandler;
       client.onloadend = onloadendhandler;
       client.onreadystatechange = onreadystatechangehandler;

       /* Assign request type and server path */
       client.open('GET', 'video_sample.mp4');
       client.send();
   ```

3. Define the actions of each [event handler](http://www.w3.org/TR/2014/WD-XMLHttpRequest-20140130/#event-handlers):

   ```
       /* When the request begins */
       function onloadstarthandler(e) {
           html += 'onloadstart<br/>';
           document.getElementById('divText').innerHTML = html;
       }

       /* When the request is in progress */
       function onprogresshandler(e) {
           html += 'onprogress<br/>';
           document.getElementById('divText').innerHTML = html;
       }

       /* When the client cancels the request */
       function onaborthandler(e) {
           html += 'onabort<br/>';
           document.getElementById('divText').innerHTML = html;
       }

       /* When server exception occurs */
       function onerrorhandler(e) {
           html += 'onerror<br/>';
           document.getElementById('divText').innerHTML = html;
       }

       /* When the request is successfully terminated */
       function onloadhandler(e) {
           html += 'onload<br/>';
           document.getElementById('divText').innerHTML = html;
       }

       /* When a timeout occurs */
       function ontimeouthandler(e) {
           html += 'ontimeout<br/>';
           document.getElementById('divText').innerHTML = html;
       }

       /* When request is terminated regardless of success or failure */
       function onloadendhandler(e) {
           html += 'onloadend<br/>';
           document.getElementById('divText').innerHTML = html;
       }

       /* Checks current progress based on a random repetition period */
       function onreadystatechangehandler(e) {
           html += 'onreadystate<br/>';
           document.getElementById('divText').innerHTML = html;
       }
   </script>
   ```

### Source Code

For the complete source code related to this use case, see the following files:

- [xhr2.html](http://download.tizen.org/misc/examples/w3c_html5/communication/xmlhttprequest_level_2)
- [video_sample.mp4](http://download.tizen.org/misc/examples/w3c_html5/communication/xmlhttprequest_level_2)

## Tracking Download Progress State

To use the XML HTTP request features in your application, you must learn to track download progress:

1. Define the input elements for managing a download. Use the `sendRequest()` and `abortRequest()` methods for the button click events to start and cancel a download.

   ```
   <input type="button" value="Send XMLHttpRequest" onclick="sendRequest()"/>
   <input type="button" value="Abort Sending" onclick="abortRequest()"/>
   <div id="divText"></div>
   ```

2. Create an [XMLHttpRequest](http://www.w3.org/TR/2014/WD-XMLHttpRequest-20140130/#dom-xmlhttprequest) interface instance and define the handlers for the `onprogress` and `onabort` events to track the download progress and cancellation events:

   ```
   <script>
       var client = new XMLHttpRequest();

       client.onprogress = onprogresshandler;
       client.onabort = onaborthandler;
   </script>
   ```

3. Use the `send()` method to request for a file to be read when the **Start download** button is clicked. When the **Cancel download** button is clicked, use the `abort()` method to cancel the download.

   ```
   <script>
       /* When Start download button is clicked */
       function sendRequest() {
           client.send();
       }

       /* When Cancel download button is clicked */
       function abortRequest() {
           client.abort();
       }
   ```

4. During the download, use the `onprogresshandler` event handler to track the current and total download size, and calculate the download status. With the `onaborthandler` event handler, you can display the cancellation notification on the screen.

   ```
       function onprogresshandler(e) {
           document.getElementById('divText').innerHTML = 'DownLoading... (' + parseInt(e.loaded / e.total * 100) + '%)';
       }

       function onaborthandler(e) {
           document.getElementById('divText').innerHTML = 'Download has been cancelled by user.';
       }
   </script>
   ```

### Source Code

For the complete source code related to this use case, see the following file:

- [xhr3.html](http://download.tizen.org/misc/examples/w3c_html5/communication/xmlhttprequest_level_2)

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
