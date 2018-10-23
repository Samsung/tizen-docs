# HTML5 Browser state

You can [access information about the network connection state of the browser](#retrieving-the-browser-state).

This feature is supported in mobile and TV applications only.

The `navigator.onLine` attribute returns `false`, if the browser cannot establish a connection to the network when a remote page is requested. To track the changes in the connection state, you must subscribe to the applicable events: `online` and `offline`. The events can be executed in the `Window` or `WorkerGlobalScope` object.

**Table: Browser state attributes and events**

| Attribute or event | Type             | Description                              |
| ------------------ | ---------------- | ---------------------------------------- |
| `onLine`           | readonly Boolean | If the browser is connected to the network, this attribute returns `true`; otherwise `false`. |
| `online`           | Event            | When the return value of the `onLine` attribute changes from `false` to `true`, a connection is established and this event is triggered. |
| `offline`          | Event            | When the return value of the `onLine` attribute changes from `true` to `false`, a connection is lost and this event is triggered. |

> **Note**  
> The device can be connected to the network without access to the Internet.

## Retrieving the Browser State

To enhance the user interaction with the device, you must learn to retrieve the browser state:

1. The `updateIndicator()` method updates the browser connection state information on the screen to reflect the current state.  
   To retrieve the current state, use the return value of the `onLine` attribute of the `navigator` interface:

   ```
   <!DOCTYPE HTML>
   <html>
      <head>
         <title>Online status</title>
         <script>
   ```

   ```
             function updateIndicator() {
                 var status = navigator.onLine ? 'online' : 'offline';
                 document.getElementById('indicator').textContent = status;
             }
   ```

2. Subscribe to event listeners to be informed when the connection state changes:

   ```
             /* Receive event when page is loaded */
             window.onload = updateIndicator;
             /* Receive event when network connection is available */
             window.ononline = updateIndicator;
             /* Receive event when network connection is unavailable */
             window.onoffline = updateIndicator;
   ```

   ```
         </script>
      </head>
      <body>
         <p>The network is: <span id="indicator">(state unknown)</span>
      </body>
   </html>
   ```

### Source Code

For the complete source code related to this use case, see the following file:

- [browser_state.htm](http://download.tizen.org/misc/examples/w3c_html5/device/html5_browser_state)

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for TV
