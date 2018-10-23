# Voice Control

You can enable the user to control the device through their voice. You can register general voice commands, which trigger a listener when the user speaks them. The voice control service recognizes the sound data recorded by the user and sends the result as a predefined command.

The Voice Control API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The main features of the Voice Control API include:

- Managing commands

  You can use the voice control service to register commands as foreground type. When the user speaks a registered command, the listener returns the recognition result.

- Retrieving information

  You can [get the current language](#info). A command is valid only when the command language is the same as the current language. The current language can be changed with the voice control setting application or by changing the display language on the device.

  You can get a notification of the language change in a listener. If the display language is changed to a non-supported one, the voice control language changes to English.


To use the voice control:


1. Set up the voice control and [register listeners](#callback).

   The initialization allows the voice control to distinguish your application from any other applications also using voice control. The registered listeners allow you to receive notifications about changes in the language, recognition result, and about any errors.

2. Set commands.

   You can [create a command list](#commands), and add or remove individual commands in the list. When creating an individual command, set the command text and type for each command handle. When all commands are created and added to the command list, set the command list to the voice control for recognition.

3. Get the recognition result.

   The recognition result is sent through a registered listener.

   If the registered command is duplicated or the user speaks multiple commands, the recognition result can contain multiple results. If you set duplicated commands, the voice control service can reject the command. The rejection is shown in the result event.

4. When no longer needed, release the voice control instance.

   You must disconnect the voice control service and deinitialize the voice control using the `release()` function.

## Prerequisites

   To enable your application to use the voice control functionality:

   1. Initialize a voice control client instance using the `getVoiceControlClient()` function:

      ```csharp
      var initializeVoiceControlClient()
      {
          var client = tizen.voicecontrol.getVoiceControlClient();
      }
      ```

   2. When voice control is no longer needed, deinitialize the instance:

      ```csharp
      var releaseVoiceControlClient()
      {
          var client = tizen.voicecontrol.getVoiceControlClient();

          client.release();
      }
      ```

      > **Note**  
      > Do not call the `release()` function in a listener.

<a name="callback"></a>
## Managing Listeners
To set and unset listeners to get notifications about recognition results and language changes:


* Add the current language change listener to be invoked when the system or application language changes:

   ```csharp
   /* Listener */
   var languageChangeListenerCallback = function(previous, current)
   {
       console.log("Language change callback " + previous + "->" + current);
   }

   /* Add */
   var addCurrentLanguageChanged()
   {
       var client = tizen.voicecontrol.getVoiceControlClient();
       var id = client.addLanguageChangeListener(languageChangeListenerCallback);
   }

   /* Remove */
   var removeCurrentLanguageChanged()
   {
       var client = tizen.voicecontrol.getVoiceControlClient();
       var id = client.addLanguageChangeListener(languageChangeListenerCallback);

       client.removeLanguageChangeListener(id);
   }
   ```

* Add the recognition result listener to be invoked when a voice command is recognized.

   > **Note**  
   >   If the recognition result produces a reject event, the voice control service has rejected the recognized command. Make sure that the command does not conflict with other commands and there are no duplicated commands.

   To get the command, check the `list` parameter in the recognition result listener. The parameter is an array of recognized `VoiceControlCommand` instances. The `result` parameter contains the recognized text.

   ```csharp
   /* Listener */
   var resultListenerCallback = function(event, list, result)
   {
       console.log("Result callback - event: " + event + ", result: " + result);
   }

   /* Add */
   var addResultListener()
   {
       var client = tizen.voicecontrol.getVoiceControlClient();
       var id = client.addResultListener(resultListenerCallback);
   }

   /* Remove */
   var removeResultListener()
   {
       var client = tizen.voicecontrol.getVoiceControlClient();
       var id = client.addResultListener(resultListenerCallback);

       client.removeResultListener(id);
   }
   ```

<a name="info"></a>
## Retrieving the Current Language

To get the current language, use the `getCurrentLanguage()` function. The voice control recognition works for the current (default) language. To be notified of language changes, use the language change listener.

```csharp
var getCurrentLang()
{
    var client = tizen.voicecontrol.getVoiceControlClient();
    var currentLanguage = client.getCurrentLanguage();
    console.log("Current language is: " + currentLanguage);

    /*
       Expected output:
       Current language is: en_US
    */
}
```

<a name="commands"></a>
## Managing Commands

To create a command list and commands:

1. Create a command.  

   Create a command with a command text and a command type. The command type is optional and the default command type is <code>FOREGROUND</code>.
   ```csharp
   var createCommandList()
   {
       var command1 = new tizen.VoiceControlCommand("alpha");
       var command2 = new tizen.VoiceControlCommand("bravo", "FOREGROUND");
       var command3 = new tizen.VoiceControlCommand("charlie")];
   ```

2. Create a command list.  

   The command list can include many commands, each with their own command text and type. The list can have <code>FOREGROUND</code> type commands, which are valid when the application is in a visible state.

   You can access the command list after you set it to the voice control and when you get the recognition result.
   ```csharp
       var commands = [command1, command2, command3];
   ```

3. Set and unset the command list.  

   You can set the command list with commands using the `setCommandList()` function.

   If you want to update the registered commands, set the command list again with the updated commands using the `setCommandList()` function.

   ```csharp
       client.setCommandList(commands, "FOREGROUND");
   ```

   When no longer needed, unset the command list using the `unsetCommandList()` function:  
   ```csharp
       if ("FOREGROUND" == type)
           client.unsetCommandList("FOREGROUND");
   }
   ```

## Related Information
* Dependencies
  - Tizen 4.0 and Higher for Mobile
  - Tizen 4.0 and Higher for Wearable
  - Tizen 4.0 and Higher for TV
