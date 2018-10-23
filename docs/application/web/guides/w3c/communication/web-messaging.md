# HTML5 Web Messaging

Web messaging is used to deliver messages between documents. Web messaging allows [cross-origin resource sharing (CORS)](../security/cors.md).

The main features of the HTML5 Web Messaging API include:

- Cross-document messaging

  You can [send and receive data between more than 2 Web pages](#using-cross-document-messaging). Because the [Same Origin Policy](http://www.w3.org/2001/tag/dj9/scriptorigin.html) is not applied for cross-document messaging, communication between other domains is also possible.

- Channel messaging

   You can [send and receive messages through the port](#using-channel-messaging) of the `MessageChannel` interface (in [mobile](http://www.w3.org/TR/2015/REC-webmessaging-20150519/#message-channels), [wearable](http://www.w3.org/TR/2012/CR-webmessaging-20120501/#message-channels), and [TV](http://www.w3.org/TR/2015/REC-webmessaging-20150519/#message-channels) applications).

With the Web Messaging API, messages are sent and received asynchronously using the `MessageEvent` object (in [mobile](http://www.w3.org/TR/2015/REC-webmessaging-20150519/#the-messageevent-interfaces), [wearable](http://www.w3.org/TR/2012/CR-webmessaging-20120501/#event-definitions), and [TV](http://www.w3.org/TR/2015/REC-webmessaging-20150519/#the-messageevent-interfaces) applications), within 1 domain or between different domains.

## Using Cross-document Messaging

Send the message from the sending page using the `postMessage()` method of the receiving page window object (in [mobile](http://www.w3.org/TR/2015/REC-webmessaging-20150519/#posting-messages), [wearable](http://www.w3.org/TR/2012/CR-webmessaging-20120501/#posting-messages), and [TV](http://www.w3.org/TR/2015/REC-webmessaging-20150519/#posting-messages) applications). To receive the page, the receiving page window object must be registered to receive messages.

The `postMessage()` method supports the following parameters:

- `message`: Message to be sent.
- `targetOrigin`: Domain receiving the message. If a certain domain cannot be defined, use the wildcard ('\*').
- `transfer` (optional): List of transferable objects.

Learning how to use cross-document messaging enhances the communication capabilities of your application:

1. Create document A and B.

2. Insert document B as `iframe` into document A:

   ```
   <iframe id="frame1" src="./web_messaging_cross_document_messaging_iframe.htm"></iframe>
   ```

3. In document A, use the `sendMessage()` method to send a message to document B.

   Use the `postMessage()` method of the `iframe` window, which sends the message from the method content, to deliver the message to the `iframe`.

   ```
   <script>
       function sendMessage(message) {
           var frame1 = document.getElementById('frame1');
           frame1.contentWindow.postMessage(message, '*');
       }
   </script>
   ```

4. Register the `message` event handler in document B to receive the sent message:

   ```
   <script>
       btnSendMessageHandler = function(e) {
           var messageEle = document.getElementById('message');
           sendMessage(messageEle.value);
       };
       /* Register event handler */
       btnSendMessage.onclick = btnSendMessageHandler;
   </script>
   ```

### Source Code

For the complete source code related to this use case, see the following file:

- [web_messaging_cross_document_messaging.htm](http://download.tizen.org/misc/examples/w3c_html5/communication/html5_web_messaging)

## Using Channel Messaging

The `MessageChannel` instance broadcasts message sending and receiving, and has 2 properties: `port1` and `port2`. Each port is used to send and receive messages, and a message that is sent from one port with the `postMessage()` method is received by the other through the `message` event.

Learning how to use channel messaging enhances the communication capabilities of your application:

1. To send a message from document A to document B, create in document A a `MessageChannel` interface instance (in [mobile](http://www.w3.org/TR/2015/REC-webmessaging-20150519/#message-channels), [wearable](http://www.w3.org/TR/2012/CR-webmessaging-20120501/#message-channels), and [TV](http://www.w3.org/TR/2015/REC-webmessaging-20150519/#message-channels) applications), which has 2 `message port` attributes (in [mobile](http://www.w3.org/TR/2015/REC-webmessaging-20150519/#message-ports), [wearable](http://www.w3.org/TR/2012/CR-webmessaging-20120501/#message-ports), [TV](http://www.w3.org/TR/2015/REC-webmessaging-20150519/#message-ports) applications): `port1` and `port2`.

   The `port2` attribute of the `MessageChannel` instance is delivered to document B through the `postMessage()` method of the document B window object:

   ```
   <script>
       var messageChannel = new MessageChannel();

       function setMessagePort() {
           /* iframe element ID of the port to be delivered */
           var frame1 = document.getElementById('iframe1');
           frame1.contentWindow.postMessage('', [messageChannel.port2], '*');
       }

       window.onload = function() {
           setMessagePort();
       };

       /* Message is sent to port2 through port1 */
       function sendMessage(message) {
           messageChannel.port1.postMessage(message);
       }
   </script>
   ```

   > **Note**  
   > The `postMessage()` method can have 3 parameters: `message`, `origin` (in [mobile](http://www.w3.org/TR/2015/REC-webmessaging-20150519/#security-postmsg), [wearable](http://www.w3.org/TR/2012/CR-webmessaging-20120501/#security-postmsg), and [TV](http://www.w3.org/TR/2015/REC-webmessaging-20150519/#security-postmsg) applications), and `ports`.  
   > According to the W3C specifications, the arguments are ordered as `message`, `origin`, and `ports`. However, in Tizen, the order used is actually `message`, `ports`, and `origin`. This approach is used in all browsers that currently support the `MessageChannel` interface.

2. Define a `message` event in the `window` object of document B, and register the event handler in the `port` sent from document A.

   ```
   <script>
       var port = null;

       messageHandler = function(e) {
           port = e.ports[0];
           port.onmessage = function(e) {
               var messageEle = document.getElementById('message');
               messageEle.innerHTML = e.data;
           };
       };

       window.onmessage = messageHandler;
   </script>
   ```

   A message sent through the `postMessage()` method of `port1` from document A is received through the `message` event of `port2` in document B, and the message sent through the `postMessage()` method of `port2` from document B is received through the `message` event of `port1` in document A.

### Source Code

For the complete source code related to this use case, see the following files:

- [web_messaging_channel_messaging.htm](http://download.tizen.org/misc/examples/w3c_html5/communication/html5_web_messaging)
- [web_messaging_channel_messaging_iframe.htm](http://download.tizen.org/misc/examples/w3c_html5/communication/html5_web_messaging)

## Related Informationi
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
