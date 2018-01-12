# Media Key Events

You can manage media key events in your application. The media keys are used to [control multimedia playback](#managing-media-key-state-changes). The user can click keys, such as **PLAY** and **FAST FORWARD**, and you can detect the key clicks in your application and change the playback accordingly.

This feature is supported in mobile and wearable applications only.

The main features of the Media Key API include:

- Registering a listener

  You can register and deregister a listener for the media key state changes.

> **Note**  
> You can register only 1 media key state change listener for your application. If you attempt to register a second listener, the first listener is unset and replaced with the new one.

- Handling state changes

  With the registered listener, you can monitor the media keys and react to their state changes when the user presses or releases a key.

## Managing Media Key State Changes

Learning how to register key event listener is a basic media key management skill:

1. Implement the listener to handle media key state changes. The listener can contain event listeners for key press (`onpressed`) and release (`onreleased`) notifications.

   ```
   var myMediaKeyChangeListener = {
       onpressed: function(key) {
           console.log('Pressed key: ' + key);
       },
       onreleased: function(key) {
           console.log('Released key: ' + key);
       }
   }
   ```

2. Register the media key state change listener:

   ```
   tizen.mediakey.setMediaKeyEventListener(myMediaKeyChangeListener);
   ```

3. Deregister the media key state change listener when it is no longer needed:

   ```
   tizen.mediakey.unsetMediaKeyEventListener();
   ```

## Related Information
* Dependencies   
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
