# Text Input, Gesture and Voice


The text input, gesture and voice features introduce how you can convert speech to text and back to speech, and provide recognized gestures, customized keyboards and voice control, and retrieve previous data in a text input field.

You can use the following text input, gesture and voice features in your native applications:

- [Input Method](input-method.md)

  You can create an Input Method Editor (IME) application that provides a customized keyboard for the user. You can show and hide the keyboard as needed, and offer a keyboard option menu to allow the user to manage the keyboard settings.

- [Autofill](autofill.md)

  You can retrieve the previously entered data stored in an autofill service.

- [Autofill Service](autofill-service.md)

  You can create an autofill service application that saves and provides the data previously entered by the user.

- [Autofill Manager](autofill-manager.md)

  You can create an Autofill manager application that shows installed Autofill service and switches to the selected Autofill service.

- [Gesture](capi-ui-gesture.md) **in wearable applications only**

  You can recognize hand gestures from input sensor data.

- [Speech-to-text](stt.md)

  You can recognize sound data recorded by the user and send the result as text. The result text can, for example, be displayed on the screen.

- [Text-to-speech](tts.md)

  You can synthesize text into sound data as utterances and play it. You can also control the playback by pausing, resuming, and stopping it, as needed.

- [Voice Control](voice-control.md)

  You can allow the user to control the device through voice commands. You can register voice commands, which trigger a callback when the user speaks them. Voice commands registered for EFL-supported UI components can be used to perform component-related actions, such as button clicks.

- [Voice Control Manager](voice-control-manager.md)

  You can record voice and get responses for the recognized voice commands. You can register general and system voice commands such as "power on", "power off", "music play", "music stop", and so on. In addition, you can start and stop voice recording.

- [Voice Control Engine](voice-control-engine.md)

  You can manage Voice-Control-Engine (VCE) service application and control the recorded audio. The result of audio recording is sent as a predefined command.

- [Multi-assistant](multi-assistant.md)

  You can create a voice assistant application that can be used in conjunction with other voice assistants on the same machine.

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
