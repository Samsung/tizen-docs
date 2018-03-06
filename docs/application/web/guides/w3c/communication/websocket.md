# WebSocket

WebSocket in a Web environment enables connection-oriented full duplex communication, as with a TCP socket. (The server and browser can send and receive data in real-time through a continuously connected TCP line.)

The difference between the previously used communication method in the Web environment and the new  Web socket lies in the protocol. The Web socket protocol uses HTTP in establishing a connection, however, all communication after the connection is established happens using the Web socket's independent protocol.

With a Web socket, the used header is extremely small, causing very little overhead. A long-term connection is used as a basis, meaning that if there is connection, sending data from client or server is possible. The long-term connection means that data can be sent and received through 1 connection, and you do not need to establish a separate connection for each sending and receiving instance. [Ping and pong frames](http://www.w3.org/TR/2012/CR-websockets-20120920/#ping-and-pong-frames) can also be used.

The main features of the WebSocket API include:

- Connecting to a server

  To [connect to a server](#connecting-to-the-socket-server), you must create a [WebSocket](http://www.w3.org/TR/2012/CR-websockets-20120920/#the-websocket-interface) interface with the socket server URL as a mandatory parameter. The [URL format has some restrictions](http://www.w3.org/TR/2012/CR-websockets-20120920/#parsing-websocket-urls), for example, it must use the `ws` or `wss` protocol. If the URL is not valid or uses a wrong protocol, a syntax error occurs.

- Sending data

  By using the `send()` method of the`WebSocket` interface, you can [send data to the server](#sending-data-to-the-server). The data is transmitted using the established connection. If the `readyState` attribute value is `CONNECTING`, the method throws an `InvalidStateError` exception.

- Receiving data

  You can [receive data from the server](#receiving-data-from-the-server) through the `message` event.

- Closing a socket

  When the connection is no longer needed, you can [close the connection](#closing-the-socket-connection) with the `close()` method.

## Connecting to the Socket Server

To use the Web socket features in your application, you must learn to connect to a socket server:

1. Create a [WebSocket](http://www.w3.org/TR/2012/CR-websockets-20120920/#the-websocket-interface) interface instance using a valid socket server URL as a parameter:

   ```
   var webSocketUrl = 'wss://html5labs-interop.cloudapp.net:443/echo';

   var webSocket = new WebSocket(webSocketURL);
   ```

   If the socket server URL is valid, the connection is created automatically. When the instance is created, the `readyState` attribute of the `WebSocket` instance must be set to `0` (CONNECTING).

2. Use the `open` and `error` events to track the connection status:

   ```
   /* If the connection is established */
   webSocket.onopen = function(e) {
       console.log('connection open, readyState: ' + e.target.readyState);
   };

   /* If the connection fails or is closed with prejudice */
   webSocket.onerror = function(e) {
       /* Error handling */
   };
   ```

   If the connection is established, the `readyState` attribute is changed to `1` and the `open` event is triggered. If the connection fails, the attribute value is set to `3`, and the HTTP 503 error is returned.

### Source Code

For the complete source code related to this use case, see the following file:

- [web_socket.htm](http://download.tizen.org/misc/examples/w3c_html5/communication/the_websocket_api)

## Sending Data to the Server

To use the Web socket features in your application, you must learn to connect to send data to the server:

1. Create a [WebSocket](http://www.w3.org/TR/2012/CR-websockets-20120920/#the-websocket-interface) interface instance using a valid socket server URL as a parameter:

   ```
   var webSocketUrl = 'wss://html5labs-interop.cloudapp.net:443/echo';

   var webSocket = new WebSocket(webSocketURL);
   ```

2. Check the `readyState` attribute value, which is `1` (OPEN), if the socket is connected.

   If the socket is connected, use the `send()` method to send the data.

   ```
   function sendMessage(msg) {
       if (webSocket.readyState === 1) {
           webSocket.send(msg);
       }
   }
   ```

### Source Code

For the complete source code related to this use case, see the following file:

- [web_socket.htm](http://download.tizen.org/misc/examples/w3c_html5/communication/the_websocket_api)

## Receiving Data from the Server

To use the Web socket features in your application, you must learn to receive data from the server:

1. Create a [WebSocket](http://www.w3.org/TR/2012/CR-websockets-20120920/#the-websocket-interface) interface instance using a valid socket server URL as a parameter:

   ```
   var webSocketUrl = 'wss://html5labs-interop.cloudapp.net:443/echo';

   var webSocket = new WebSocket(webSocketURL);
   ```

2. Register the `message` event in the `WebSocket` instance. The event is triggered when data is received from the server.

   ```
   webSocket.onmessage = function(e) {
       console.log('server message: ' + e.data);
   };
   ```

### Source Code

For the complete source code related to this use case, see the following file:

- [web_socket.htm](http://download.tizen.org/misc/examples/w3c_html5/communication/the_websocket_api)

## Closing the Socket Connection

To use the Web socket features in your application, you must learn to close the socket connection:

1. Create a [WebSocket](http://www.w3.org/TR/2012/CR-websockets-20120920/#the-websocket-interface) interface instance using a valid socket server URL as a parameter:

   ```
   var webSocketUrl = 'wss://html5labs-interop.cloudapp.net:443/echo';

   var webSocket = new WebSocket(webSocketURL);
   ```

2. Register a `close` event in the `WebSocket` instance to be notified when the connection closes:

   ```
   webSocket.onclose = function(e) {
       console.log('connection close, readyState: ' + e.target.readyState);
   };
   ```

3. Check the `readyState` attribute value, which is `1` (OPEN), if the socket is connected.

   If the socket is connected, use the `close()` method to close the connection between the client and the server.

   ```
   function closeConnection() {
       if (webSocket.readyState === 1) {
           webSocket.close();
       }
   }
   ```

### Source Code

For the complete source code related to this use case, see the following file:

- [web_socket.htm](http://download.tizen.org/misc/examples/w3c_html5/communication/the_websocket_api)

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
