# Event Handling

You can use events provided by Cordova in Web applications by registering custom listeners with no parameters. The Events API has no objects or properties.

The Events API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The Events API provides the following events:

- `deviceready`  
    The `deviceready` event is a prerequisite for all Cordova operations. You can use the `deviceready` event to receive a signal when Cordova's device APIs have loaded and are ready to access. You can also use this event to [register event listeners](#adding-event-listeners) for other events you are interested in.    

- `pause`  
    You can [use the `pause` event](#handling-pause-and-resume-events) to receive a signal when the application is put to the background. This happens typically when the screen is being locked or when the user switches to a different application.    

- `resume`  
    You can [use the `resume` event](#handling-pause-and-resume-events) to receive a signal when the application is retrieved from the background.    

- Button press events  
  You can [add event listeners for specific button press events](#handling-button-press-events).

## Prerequisites

To perform any Cordova-related operations, you must wait until Cordova is fully set up (the `deviceready` event occurs):

```
document.addEventListener('deviceready', onDeviceReady, false);

function onDeviceReady() {
    console.log('Cordova features now available');
}
```

Alternatively, you can add the event listener in the `<body>` element onload handler:

```
window.onload = function() {
    document.addEventListener('deviceready', onDeviceReady);
};
```

## Adding Event Listeners

The applications typically use the `document.addEventListener()` method to attach an event listener once the `deviceready` event fires. This means that event listeners for other events (such as `pause`, `resume`, and `backbutton`) are added during or after the `deviceready` event handler:

```
document.addEventListener('deviceready', onDeviceReady, false);

function onDeviceReady() {
    document.addEventListener('pause', onPause);
    document.addEventListener('volumeupbutton', onVolumeUp);
}

function onPause() {
    console.log('Application has been put into the background');
}

function onVolumeUp() {
    console.log('Volume up button pressed');
}
```

## Handling Pause and Resume Events

The pause event signals that the application is put into the background. This happens typically when the screen is being locked or when the user switches to a different application. The resume event signals that the application returns from the background to the foreground.

To handle the `pause` and `resume` events:

1. Define the event handlers for the `pause` and `resume` events:

   ```
   function onPause() {
       console.log('Application paused');
   }

   function onResume() {
       console.log('Application resumed');
   }
   ```

2. In the `deviceready` event handler, [add the listeners](#adding-event-listeners):

   ```
   document.addEventListener('pause', onPause);
   document.addEventListener('resume', onResume);
   ```

## Handling Button Press Events

You can add event listeners for specific button press events, as defined in the following table.

**Table: Button press events**

| Event              | Button name        |
| ------------------ | ------------------ |
| `backbutton`       | Back button        |
| `menubutton`       | Menu button        |
| `searchbutton`     | Search button      |
| `startcallbutton`  | Start call button  |
| `endcallbutton`    | End call button    |
| `volumedownbutton` | Volume down button |
| `volumeupbutton`   | Volume up button   |

Events are triggered when the corresponding button is pressed.

To add event listeners for the menu, volume up, and volume down buttons:

1. Define the event handlers for the `menubutton`, `volumeupbutton`, and `volumeupbutton` events:

   ```
   function onVolumeChanged() {
       console.log('Volume changed');
   }

   function onMenuButton() {
       console.log('Menu button pressed');
   }
   ```

2. In the `deviceready` event handler, [add the listeners](#adding-event-listeners).

   In this example, the same listener is used for both the volume up and down buttons.

   ```
   document.addEventListener('menubutton', onMenuButton);
   document.addEventListener('volumeupbutton', onVolumeChanged);
   document.addEventListener('volumedownbutton', onVolumeChanged);
   ```

When you press the buttons, the result is shown in the system console.

## Related Information
* Dependencies
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
