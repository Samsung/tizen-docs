# Notification Dialogs

You can make different types of notifications to the user, so that each time a notification dialog box is closed, the result is provided in a callback function. The `navigator.notification` object allows access to the Dialogs API.

The Dialogs API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The main features of the Dialogs API include:

- Alerts        

  You can [create an alert dialog box](#creating-alerts), which shows an alert text and a dismiss button with custom text.

- Confirmations        

  You can [create a confirmation dialog box](#creating-confirmations), which shows a confirmation text with a set of buttons.

- Prompts        

  You can [create a prompt dialog box](#creating-prompts), which shows a prompt where the user can put some text, and a set of buttons.

- Beeps        

  You can [make a beep sound](#making-beep-sounds).

## Prerequisites

To perform any Cordova-related operations, you must wait until Cordova is fully set up (the `deviceready` event occurs):

```
document.addEventListener('deviceready', onDeviceReady, false);

function onDeviceReady() {
    console.log('Cordova features now available');
}
```

## Creating Alerts

To show a custom alert with 1 button:

1. Define a callback method to be invoked when the user closes the alert.

   The callback has no parameters.

   ```
   var alertDismissed = function() {
       console.log('Alert was dismissed');
   };
   ```

2. Open the alert dialog box with an alert text and callback function:

   ```
   navigator.notification.alert('Please click OK button.', alertDismissed);
   ```

   Alternatively, you can open the alert dialog box with an optional title (default is `Dialog`), and an optional button name (default is `OK`):

   ```
   navigator.notification.alert('Please click Close button.', alertDismissed,
                                'Alert title', 'Close');
   ```

When the user dismisses the dialog box, the log appears in the console.

## Creating Confirmations

To show a confirmation dialog box with a set of buttons:

1. Define a callback method to be invoked when the user clicks a button.

   The callback has 1 parameter: the index of the pressed button, or 0, if the dialog is dismissed without a button press.

   ```
   var confirmCallback = function(buttonIndex) {
       console.log('Selected button was ' + buttonIndex);
   };
   ```

2. Open the confirmation dialog box with a set of buttons as the last parameter. The default value is `['OK', 'Cancel']`.

   ```
   navigator.notification.confirm('Choose one option:', confirmCallback,
                                  'Options title', ['Option1', 'Option2']);
   ```

The callback is invoked when the user performs an action.

## Creating Prompts

To show a prompt dialog box where the user can put some text, with a set of buttons:

1. Define a callback method to be invoked when the user clicks a button.

   The callback has 1 parameter: the `PromptData` object (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/dialogs.html#PromptData), [wearable](../../api/latest/device_api/wearable/tizen/cordova/dialogs.html#PromptData), and [TV](../../api/latest/device_api/tv/tizen/cordova/dialogs.html#PromptData) applications) containing the user input and pressed button index.

   ```
   var promptCallback = function(results) {
       console.log('User entered a value ' + results.input1 + ', and selected option ' + results.buttonIndex);
   };
   ```

2. Open a prompt dialog box with a set of buttons and default text to be shown in the text input field. The default values are `['OK', 'Cancel']` and an empty string.

   ```
   navigator.notification.prompt('Please enter text:', promptCallback, 'Prompt dialog box',
                                 ['OK', 'Exit'], 'default text');
   ```

The callback provides the `PromptData` object, holding all the data provided by the user.

**Table: PromptData object properties**

| Property    | Value                                    |
| ----------- | ---------------------------------------- |
| buttonIndex | Index of a button pressed by the user. The index uses one-based indexing, so the values can be 1, 2, 3, and so on. |
| input1      | Text entered by the user.                |

## Making Beep Sounds

To make a beep sound once or more:

- Make a beep only once:

  ```
  navigator.notification.beep(1);
  ```

- Make a beep 3 times:

  ```
  navigator.notification.beep(3);
  ```

## Related Information
* Dependencies  
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
