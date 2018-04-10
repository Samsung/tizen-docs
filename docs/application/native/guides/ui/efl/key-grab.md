# Grabbing Hardware Key Events

The applications do not normally grab hardware key events, because each key event is delivered to the focused window by default. Some applications, however, have more advanced functionalities and behavior. For example, in most applications, a volume key press opens a volume control popup. But, in a memo application, you can use the volume key to resize the text.

To receive special hardware key events in the application, use the `eext_win_keygrab_set()` and `eext_win_keygrab_unset()` functions.

To grab hardware key events:

1. To use the functions and data types of the EFL Extension API (in [mobile](../../../api/mobile/latest/group__CAPI__EFL__EXTENSION__MODULE.html) and [wearable](../../../api/wearable/latest/group__CAPI__EFL__EXTENSION__MODULE.html) applications), include the `<efl_extension.h>` header file in your application:

   ```
   #include <efl_extension.h>
   ```

2. Create the application window and add UI components to it, as needed.

   For more information, see [Building UI Layouts](./ui-layouts.md).

   ```
   static void
   create_base_gui(appdata_s *ad)
   {
       Evas_Object *win = NULL;

       /* Create the window */
       win = elm_win_util_standard_add(NULL, "extension sample");
       evas_object_smart_callback_add(win, "delete,request", _win_del, NULL);

       /* Create UI containers and components */

       /* Show the window */
       evas_object_show(win);
   }
   ```

3. Register and define key event callbacks for the window using the [Ecore events](./event-types.md#ecore-events):

   ```
   Eina_Bool ctrl_pressed = EINA_FALSE;

   /* Define the callback */
   static Eina_Bool
   _key_down_cb(void *data __UNUSED__, int type __UNUSED__, void *ev)
   {
       /* Access the fields of the event key type ("*ev") */
       Ecore_Event_Key *event = ev;

       /* Test whether the pressed key is Ctrl */
       if (!strcmp("Control_L", event->key)) {
           /* If it is, store that information */
           ctrl_pressed = EINA_TRUE;
       }

       /* Let the event continue to other callbacks */
       return ECORE_CALLBACK_PASS_ON;
   }

   /* Register the callback */
   ecore_event_handler_add(ECORE_EVENT_KEY_DOWN, _key_down_cb, NULL);
   ```

4. Grab key events using the `eext_win_keygrab_set()` function with the application window object and the [key string](#keystring) as parameters.

   ```
   eext_win_keygrab_set(win, "XF86AudioRaiseVolume");
   ```

5. When the application no longer needs to grab key events, call the `eext_win_keygrab_unset()` function:

   ```
   eext_win_keygrab_unset(win, "XF86AudioRaiseVolume");
   ```

The following table lists the hardware keys from which you can grab events in different profiles.

<a name="keystring"></a>
**Table: Supported hardware keys**

| Key                       | Description                              | Mobile | Wearable | TV   |
|-------------------------|----------------------------------------|------|--------|----|
| `"XF86AudioRaiseVolume"`  | Key to raise the volume                  | Yes    | Yes      | Yes  |
| `"XF86AudioLowerVolume"`  | Key to lower the volume                  | Yes    | Yes      | Yes  |
| `"XF86PowerOff"`          | Power key to switch the device on and off | Yes    | Yes      | Yes  |
| `"XF86Menu"`              | Application-specific menu key            | Yes    | Yes      | Yes  |
| `"XF86Home"`              | Key to go to the home screen             | Yes    | Yes      | Yes  |
| `"XF86Back"`              | Key to go back to the previous status or page | Yes    | Yes      | Yes  |
| `"XF86Camera"`            | Half shutter key to do something before taking a picture on the camera | Yes    | -        | -    |
| `"XF86Camera_Full"`       | Key to take a picture on the camera      | Yes    | Yes      | Yes  |
| `"XF86Search"`            | Key to go to the search application      | Yes    | Yes      | Yes  |
| `"XF86AudioPlay"`         | Key to play media                        | Yes    | Yes      | Yes  |
| `"XF86AudioPause"`        | Key to pause the media being played      | Yes    | Yes      | Yes  |
| `"XF86AudioStop"`         | Key to stop the media being played       | Yes    | Yes      | Yes  |
| `"XF86AudioNext"`         | Key to go to the next media item         | Yes    | Yes      | Yes  |
| `"XF86AudioPrev"`         | Key to go to the previous media item     | Yes    | Yes      | Yes  |
| `"XF86AudioRewind"`       | Key to rewind the playing position of the media | Yes    | Yes      | Yes  |
| `"XF86AudioForward"`      | Key to forward the playing position of the media | Yes    | Yes      | Yes  |
| `"XF86AudioMedia"`        | Key to go to the media player            | Yes    | Yes      | Yes  |
| `"XF86AudioPlayPause"`    | Key to toggle between play and pause     | Yes    | Yes      | Yes  |
| `"XF86AudioMute"`         | Key to mute the media                    | Yes    | Yes      | Yes  |
| `"XF86AudioRecord"`       | Key to start recording media             | Yes    | Yes      | Yes  |
| `"Cancel"`                | Key to cancel the action triggered by the previous keys | Yes    | Yes      | Yes  |
| `"XF86SoftKBD"`           | Key to show and hide the soft keyboard   | Yes    | Yes      | Yes  |
| `"XF86QuickPanel"`        | Key to toggle the quick panel            | Yes    | -        | Yes  |
| `"XF86TaskPane"`          | Key to toggle the task switcher          | Yes    | Yes      | Yes  |
| `"XF86HomePage"`          | Key to go to the homepage of the user-defined Web browser | Yes    | -        | Yes  |
| `"XF86WWW"`               | Key to launch the user-defined Web browser | Yes    | -        | Yes  |
| `"XF86Mail"`              | Key to go to the user-defined email application | Yes    | -        | Yes  |
| `"XF86ScreenSaver"`       | Key to activate the screen lock (such as a pattern lock or a PIN lock) | Yes    | Yes      | Yes  |
| `"XF86MonBrightnessDown"` | Key to lower the screen brightness       | Yes    | Yes      | Yes  |
| `"XF86MonBrightnessUp"`   | Key to raise the screen brightness       | Yes    | Yes      | Yes  |
| `"XF86Voice"`             | Key to activate a voice-related application | Yes    | Yes      | Yes  |
| `"Hangul"`                | Key to toggle the current language       | Yes    | -        | Yes  |
| `"XF86Apps"`              | Key to call the application holder application | Yes    | Yes      | Yes  |
| `"XF86Call"`              | Key to launch the call application       | Yes    | Yes      | Yes  |
| `"XF86Game"`              | Key to go to the game application        | Yes    | -        | Yes  |
| `"XF86VoiceWakeUp_LPSD"`  | Key to wake up from voice input (LPSD)   | Yes    | Yes      | Yes  |
| `"XF86VoiceWakeUp"`       | Key to wake up from voice input          | Yes    | Yes      | Yes  |
| `"XF86TV"`                | Key to display the TV screen directly    | -      | -        | Yes  |
| `"XF86Display"`           | Key to toggle the video source           | -      | -        | Yes  |
| `"XF86RCConfig"`          | Key to set the remote control's specific configuration | -      | -        | Yes  |
| `"XF86RCMode"`            | Key to show and hide the virtual remote control on the screen | -      | -        | Yes  |
| `"1"`                     | Numeric key 1 on the remote control      | -      | -        | Yes  |
| `"2"`                     | Numeric key 2 on the remote control      | -      | -        | Yes  |
| `"3"`                     | Numeric key 3 on the remote control      | -      | -        | Yes  |
| `"4"`                     | Numeric key 4 on the remote control      | -      | -        | Yes  |
| `"5"`                     | Numeric key 5 on the remote control      | -      | -        | Yes  |
| `"6"`                     | Numeric key 6 on the remote control      | -      | -        | Yes  |
| `"7"`                     | Numeric key 7 on the remote control      | -      | -        | Yes  |
| `"8"`                     | Numeric key 8 on the remote control      | -      | -        | Yes  |
| `"9"`                     | Numeric key 9 on the remote control      | -      | -        | Yes  |
| `"0"`                     | Numeric key 0 on the remote control      | -      | -        | Yes  |
| `"-"`                     | Minus key on the remote control          | -      | -        | Yes  |
| `"XF86LowerChannel"`      | Key to lower the channel number          | -      | -        | Yes  |
| `"XF86RaiseChannel"`      | Key to raise the channel number          | -      | -        | Yes  |
| `"XF86ChannelList"`       | Key to display the channel list          | -      | -        | Yes  |
| `"XF86PreviousChannel"`   | Key to display the previous channel      | -      | -        | Yes  |
| `"XF86SysMenu"`           | Key to launch the system menu            | -      | -        | Yes  |
| `"XF86SimpleMenu"`        | Key to launch the simple menu            | -      | -        | Yes  |
| `"XF86History"`           | Key to launch the history functionality  | -      | -        | Yes  |
| `"XF86Favorites"`         | Key to launch the favorite channels functionality | -      | -        | Yes  |
| `"Up"`                    | Arrow key UP on the remote control       | -      | -        | Yes  |
| `"Down"`                  | Arrow key DOWN on the remote control     | -      | -        | Yes  |
| `"Left"`                  | Arrow key LEFT on the remote control     | -      | -        | Yes  |
| `"Right"`                 | Arrow key RIGHT on the remote control    | -      | -        | Yes  |
| `"Return"`                | OK key on the remote control to confirm or select an item | -      | -        | Yes  |
| `"XF86Close"`             | Exit key on the remote control to terminate the current menu or application | -      | -        | Yes  |
| `"XF86Info"`              | Key to display the basic and auxiliary information on the screen | -      | -        | Yes  |
| `"XF86Red"`               | Key to execute the functionality registered to the RED key | -      | -        | Yes  |
| `"XF86Green"`             | Key to execute the functionality registered to the GREEN key | -      | -        | Yes  |
| `"XF86Yellow"`            | Key to execute the functionality registered to the YELLOW key | -      | -        | Yes  |
| `"XF86Blue"`              | Key to execute the functionality registered to the BLUE key | -      | -        | Yes  |
| `"XF86ProgInfo"`          | Key to display the program information   | -      | -        | Yes  |
| `"XF86PictureMode"`       | Key to change the screen mode            | -      | -        | Yes  |
| `"XF86PictureSize"`       | Key to change the screen size and aspect ratio | -      | -        | Yes  |
| `"XF86PIP"`               | Key to set the PIP (Picture-In-Picture) mode to display one screen on the other | -      | -        | Yes  |
| `"XF86Guide"`             | Key to display the user guide            | -      | -        | Yes  |
| `"XF86AudioMode"`         | Key to set or change the audio mode      | -      | -        | Yes  |
| `"XF86Subtitle"`          | Key to display or hide the subtitles     | -      | -        | Yes  |
| `"XF863D"`                | Key to set or change the 3D mode         | -      | -        | Yes  |

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
