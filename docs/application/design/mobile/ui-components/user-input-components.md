# User Input Components



User input components are used to collect user input for specific tasks. The following UI components are user input components:

-   [Button](#button_)
-   [Checkbox components](#check_)
-   [Radio button](#radio_)
-   [Text input](#text_)
-   [Dropdown menu](#drop_)
-   [Slider](#slider_)
-   [Picker](#picker_)

 
<a name="button_"></a>
## Button

A button is used to allow user interactions to trigger events. On a button, you can include text, an image, or both.

The following button types are available:

-   Circle button
-   Box button
-   Bottom button

To learn how to implement a button, see [Button](../../../native/guides/ui/efl/component-button-m.md).

 

#### Circle Button

A circle button is a simple icon that the user can easily understand. You can provide text labels under the icons to further enhance user understanding.



![Circle buttons](media/circle_button-260x72.png)  
Circle buttons



 

#### Box Button

A box button is displayed as a rounded box shape. You can include text, icons, or both in them.


![Box button](media/5.3.1_b-220x166.png)  
Box buttons


<a name="bottom_"></a>
#### Bottom Button

A bottom button is used for main actions. It is fixed at the bottom section of the screen and does not scroll with the content on the screen.


![Bottom button](media/5.3.1_c-260x55.png)  
Bottom buttons

 
<a name="check_"></a>
## Checkbox Components

Checkbox components are action icons that allow the user to switch certain features on or off, or to select various options. These icons are frequently used in the screen designs of galleries, lists, timers, and calendars.

The following checkbox component types are available:

-   Toggle
-   Checkbox
-   Favorite

Use simple and flat pictographic icons when you design checkbox components. Tizen assigns system colors for checkbox and radio buttons. For other icons, colors may be selected according to the significance of the icons.

To learn how to implement a checkbox, see [Check](../../../native/guides/ui/efl/component-check-m.md).

 

#### Toggle

A toggle is used to allow the user to switch a feature on or off.


![Toggle](media/5.3.2.a-200x80.png)  
Toggles


 

#### Checkbox

A checkbox is used to allow users to select or clear items, or to confirm tasks.



![Checkbox](media/5.3.2.b-200x80.png)  
Checkboxes


 

#### Favorite

Favorites are used to allow users to tag items for future reference.


![Favorite](media/5.3.2.c-200x80.png)  
Favorites


In the Toggle and Checkbox Icon Pack, you can find the action icon examples created for various screen sizes. This package includes icons designed in Adobe® Photoshop® format, so that you can customize and use them for your own designs.

 

 
<a name="radio_"></a>
## Radio Button

A radio button is used to allow the user to select an item from a list of multiple choices.

To learn how to implement a radio button, see [Radio](../../../native/guides/ui/efl/component-radio-m.md).



![Radio button](media/5.3.2.d-200x80.png)  
Radio buttons


 

 
<a name="text_"></a>
## Text Input

The text input component provides an input field for the user to enter text information.



![Typical text input component in an app](media/text_input_rev-260x156.png)  
Typical text input component parts



The following text input component types are available:

-   Single-line text input
-   Multi-line text input
-   Text enveloper

The text enveloper provides an extended functionality to text input. It recognizes the delimiters between text input and binds the entries, such as email addresses or keywords, in meaningful or functional chunks, so that the user can individually control or modify them. The enter key input ( ↵ ), comma ( , ), and semi colon ( ; ) are generally used for text delimiters, but you can define your own delimiters to suit the type and purpose of your app.

To learn how to implement a text input component, see [Entry](../../../native/guides/ui/efl/component-entry-m.md).



![Text input and text enveloper](media/text_input_enveloper_01-260x43.png) ![Text input and text enveloper](media/text_envelope_02-260x99.png)  
Text input and text enveloper



 

 
<a name="drop_"></a>
## Dropdown Menu

A dropdown menu allows the user to select an item from a list of multiple choices. A list of items is displayed when the user taps the dropdown menu.

To learn how to implement a dropdown menu, see [Hoversel](../../../native/guides/ui/efl/component-hoversel.md).



![Dropdown menu](media/5.3.5-259x460.png)  
Dropdown menu



 

 
<a name="slider_"></a>
## Slider

A slider is used to adjust a value within a certain range. You can include a description or an icon that explains the slider's value range. The user can tap or drag the slider bar to increase or decrease the value. You can also provide numbers on the slider to indicate the value.

To learn how to implement a slider, see [Slider](../../../native/guides/ui/efl/component-slider-m.md).



![Slider](media/5.3.6-240x154.png)  
Sliders



 

 
<a name="picker_"></a>
## Picker

A picker allows the user to select a specific value or multiple interconnected values from multiple options.

The following picker types are available:

-   Number picker
-   Date and time picker
-   Color picker

 

#### Number Picker

A number picker allows the user to select a specific number.

To learn how to implement a number picker, see [Spinner](../../../native/guides/ui/efl/component-spinner.md) and [Flipselector](../../../native/guides/ui/efl/component-flipselector.md).



![Number picker](media/time_picker2-260x134.jpg)  
Number pickers



 

#### Date and Time Picker

A date and time picker allows the user to set the date and time for different user apps using a specific picker type:

-   Time picker
-   Date picker

To learn how to implement date and time pickers, see [Datetime](../../../native/guides/ui/efl/component-datetime-m.md).

 


![Time picker](media/clock_ref-260x142.png)  
Time picker


![Date picker](media/are-250x121.png) ![Date picker](media/5-250x136.png)  
Date pickers


 

#### Color Picker

A color picker allows the user to select a color from a set of colors.

To learn how to implement a color picker, see [Colorselector](../../../native/guides/ui/efl/component-colorselector.md).



![Time picker](media/5.7.3_d-250x74.png)  
Color picker
