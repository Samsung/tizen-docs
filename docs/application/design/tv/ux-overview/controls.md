# Controls

Controls provide ways to control UI components and other elements on a Tizen 4.0 TV. They allow the user to access content and items on the screen easily.

You can use 2 control methods:

-   A remote control is a basic piece of equipment, essential for controlling Tizen 4.0 TV elements. The remote control keys have 2 press styles, which create different interactions based on the context and key:
    -   Short press is a normal press that takes less than 1 second.
    -   Long press takes more than 1 second. If you press a key 5 times in a row, the action is interpreted as a long press.
-   A mouse is useful when the user runs Web browser applications.

The following table lists the basic controls controlled by the remote control keys.

<table>
<tr>
 <th rowspan="2"> Name </th>
 <th rowspan="2"> Symbol </th>
 <th rowspan="2"> Case </th>
 <th colspan="2"> Short press </th>
 <th colspan="2"> Long press </th>
</tr>
<tr>
 <th> Interaction </th>
 <th> Display </th>
 <th> Interaction </th>
 <th> Display </th>
</tr>
<tr>
 <td rowspan="2">Power key</td>
 <td rowspan="2"><img alt="Power key" height="100" src="media/ux_05_power_key.png" width="100" /></td>
 <td>When powered off</td>
 <td>Switches the screen on</td>
 <td>Last channel or source screen</td>
 <td rowspan="2" colspan="2">Same as short press</td>
</tr>
<tr>
 <td>When powered on</td>
 <td>Switches the screen off</td>
 <td>Off screen</td>
</tr>
<tr>
 <td rowspan="2">Home key</td>
 <td rowspan="2"><img alt="Home key" height="100" src="media/ux_06_home_key.png" width="100" /></td>
 <td>When the home screen is not shown</td>
 <td>Shows the home screen</td>
 <td>Home screen</td>
 <td rowspan="2" colspan="2">Same as short press</td>
</tr>
<tr>
 <td>When the home screen is already shownn</td>
 <td>Dismisses the home screen</td>
 <td>Previous screen</td>
</tr>
<tr>
 <td> Volume up key<br>
 Volume down key</td>
 <td><img alt="Volume key" height="100" src="media/ux_07_volume_key.png" width="100" /></td>
 <td>All cases</td>
 <td> Turns volume up or down</td>
 <td> Volume banner</td>
 <td> Works twice as fast as the short press interaction</td>
 <td> Same as short press</td>
</tr>
<tr>
 <td> OK key</td>
 <td><img alt="OK key" height="100" src="media/ux_08_ok_key.png" width="100" /></td>
 <td>All cases</td>
 <td> Selects the focused item</td>
 <td> Response depends on the item</td>
 <td>Provides a drop-down popup</td>
 <td>Drop-down popup</td>
</tr>
<tr>
 <td rowspan="3">Back key</td>
 <td rowspan="3"><img alt="Back key" height="100" src="media/ux_09_back_key.png" width="100" /></td>
 <td> Default</td>
 <td>Goes back to the previous screen</td>
 <td>Previous screen</td>
 <td rowspan="3">Exits the current screen without a quit popup</td>
 <td rowspan="3">Source screen</td>
</tr>
<tr>
 <td>When non-first item is focused on the content area</td>
 <td>Moves focus to the first item</td>
 <td>Focus on the first item</td>
</tr>
<tr>
 <td>In fullscreen mode</td>
 <td>Provides a quit popup</td>
 <td>Quit popup</td>
</tr>
<tr>
 <td rowspan="2">Left key<br>
 Right key<br>
 Up key<br>
 Down key
</td>
 <td rowspan="2"><img alt="Direction key" height="100" src="media/ux_10_direction_key.png" width="100" /></td>
 <td>On a selectable item</td>
 <td>Moves focus to the left/right/up/down item</td>
 <td>Focus</td>
 <td>Work faster than short press interaction</td>
 <td>Same as short press</td>
</tr>
<tr>
 <td>On a non-selectable item</td>
 <td>Action depends on the UI</td>
 <td>Response depends on the case</td>
 <td colspan="2">Same as short press</td>
</tr>
<tr>
 <td>Play key<br>
 Pause key</td>
 <td><img alt="Play Pause key" height="100" src="media/ux_11_play_pause_key.png" width="100" /></td>
 <td>All cases</td>
 <td> Action depends on the UI</td>
 <td>Response depends on the case</td>
 <td colspan="2">Same as short press</td>
</tr>
<tr>
 <td>Number key</td>
 <td><img alt="Number key" height="100" src="media/ux_12_number_key.png" width="100" /></td>
 <td>When live TV screen is shown</td>
 <td> Provides a numeric keypad</td>
 <td>Numeric keypad</td>
 <td colspan="2">Same as short press</td>
</tr>
<tr>
 <td>Voice key</td>
 <td><img alt="Voice key" height="100" src="media/ux_13_voice_key.png" width="100" /></td>
 <td>All cases</td>
 <td> Action depends on the UI</td>
 <td>Response depends on the case</td>
 <td colspan="2">Same as short press</td>
</tr>
</table>

The following table lists the controls controlled by the mouse.

<table>
 <tr>
  <th rowspan="2"> Name </th>
  <th rowspan="2"> Symbol </th>
  <th rowspan="2"> Case </th>
  <th colspan="2"> Short press </th>
 </tr>
 <tr>
  <th> Interaction </th>
  <th> Display </th>
 </tr>
 <tr>
  <td rowspan="2"> Pointer </td>
  <td rowspan="2"> <img alt="Pointer" height="100" src="media/ux_14_pointer.png" width="100" /> </td>
  <td> On a selectable item </td>
  <td> Provides focus on the item </td>
  <td> Focus </td>
 </tr>
 <tr>
  <td> On a non-selectable item </td>
  <td> No response </td>
  <td> No response </td>
 </tr>
 <tr>
  <td rowspan="2"> Left-button click </td>
  <td rowspan="2"> <img alt="Left-button click" height="100" src="media/ux_15_left_button_click.png" width="100" /> </td>
  <td>  On a selectable item </td>
  <td>  Selects the item </td>
  <td>  Response depends on the item </td>
 </tr>
 <tr>
  <td>  On a non-selectable item </td>
  <td>  No response </td>
  <td>  No response </td>
 </tr>
 <tr>
  <td rowspan="2"> Right-button click </td>
  <td rowspan="2">  <img alt="Right-button click" height="100" src="media/ux_16_right_button_click.png" width="100" /> </td>
  <td>   On a selectable item </td>
  <td>  Same as long pressing the OK key on the remote control </td>
  <td>   Drop-down popup </td>
 </tr>
 <tr>
  <td>  On a non-selectable item </td>
  <td>   Same as pressing the Home key on the remote control </td>
  <td>   Home menu </td>
 </tr>
 <tr>
  <td rowspan="2"> Wheel up <br>  Wheel down </td>
  <td rowspan="2"> <img alt="Wheel up Wheel down" height="100" src="media/ux_17_wheel_up_down.png" width="100" /></td>
  <td>  In a scrollable area </td>
  <td>   Scrolls the item list to the up or down direction </td>
  <td>   Scroll bar </td>
 </tr>
 <tr>
  <td>  In a non-scrollable area </td>
  <td>   No response </td>
  <td>   No response </td>
 </tr>
 <tr>
  <td>   Drag & drop </td>
  <td>  <img alt="Drag and drop" height="100" src="media/ux_18_drag_and_drop.png" width="100" /></td>
  <td>   With a slider </td>
  <td>  Adjust the slider value </td>
  <td>   Moving handler </td>
 </tr>
</table>
