# TextField

The `TextField` class is a control providing a single-line editable text field.

**Figure: TextField**

![TextField](./media/textfield.png)

In this tutorial, the following subjects are covered:

[TextField events](#1)<br>
[Creating a TextField](#2)<br>
[Aligning Text](#3)<br>
[TextField Properties](#4)<br>

<a name="1"></a>
## TextField events

The following table lists the basic signals provided by the `TextField` class.

**Table: TextField input signals**

| Input signal        | Description                                 |
| ------------------- | ------------------------------------------- |
| `TextChanged`       | Emitted when the text changes.              |
| `MaxLengthReached`  | Emitted when inserted text exceeds the maximum character limit. |

<a name="2"></a>
## Creating a TextField

Before text has been entered, the `TextField` class can display a placeholder text. An alternative placeholder can be displayed when the `TextField` has keyboard focus. For example, a `TextField` used to enter a username can initially show the text `Unknown Name`, and the text `Enter Name` when the cursor is visible.

```
Window window = Window.Instance;
TextField field = new TextField();
PropertyMap propertyMap = new PropertyMap();
propertyMap.Add("placeholderText", new PropertyValue("Unnamed Name"));
propertyMap.Add("placeholderTextFocused", new PropertyValue("Enter Name."));
field.Placeholder = propertyMap;
window.Add(field);
```

When the `TextField` is tapped, it automatically gets the keyboard focus. Key events enter the text, and the placeholder text is removed. After text has been entered, it can be retrieved from the `TEXT` property.

```
Property::Value fieldText = field.GetProperty( TextField::Property::TEXT );
std::string fieldTextString = fieldText.Get< std::string >();
```

<a name="3"></a>
## Aligning Text

The `TextField` class displays a single-line of text, which scrolls if there is not enough space for the text displayed. If there is enough space, the text can be aligned horizontally to the beginning, end, or center of the available area:

```
// Begin, Center, or End
field.HorizontalAlignment = HorizontalAlignment.Begin;
```

<a name="4"></a>
## TextField Properties
### Using Decorations

For text decorations, the following `TextField` class properties are available. All properties are writable and none are animatable.

**Table: TextField properties**

| Property                           | Type        | Description                              |
| ---------------------------------- | ----------- | ---------------------------------------- |
| `Text`                             | String      | The text to display in UTF-8 format.     |
| `PlaceholderText`                  | String      | The text to display when the TextField is empty and inactive. |
| `PlaceholderTextFocused`           | String      | The text to display when the TextField is empty with key-input focus. |
| `FontFamily`                       | String      | The requested font family.               |
| `FontStyle`                        | PropertyMap | The requested font style.                |
| `PointSize`                        | Float       | The size of font in points.              |
| `MaxLength`                        | Integer     | The maximum number of characters that can be inserted. |
| `ExceedPolicy`                     | Integer     | Specifies how the text is truncated when it does not fit. |
| `HorizontalAlignment`              | HorizontalAlignment | The line horizontal alignment.   |
| `VerticalAlignment`                | VerticalAlignment   | The line vertical alignment.     |
| `TextColor`                        | Color       | The text color.                          |
| `PlaceholderTextColor`             | Vector4     | The placeholder-text color.              |
| `PrimaryCursorColor`               | Vector4     | The color to apply to the primary cursor. |
| `SecondaryCursorColor`             | Vector4     | The color to apply to the secondary cursor. |
| `EnableCursorBlink`                | Boolean     | Whether the cursor should blink or not.  |
| `CursorBlinkInterval`              | Float       | The time interval in seconds between cursor on/off states. |
| `CursorBlinkDuration`              | Float       | The cursor will stop blinking after this number of seconds. |
| `CursorWidth`                      | Integer     | The cursor width.                        |
| `GrabHandleImage`                  | String      | The image to display for the grab handle. |
| `GrabHandlePressedImage`           | String      | The image to display when the grab handle is pressed. |
| `ScrollThreshold`                  | Float       | Horizontal scrolling will occur if the cursor is this close to the control border. |
| `ScrollSpeed`                      | Float       | The scroll speed in pixels per second.   |
| `SelectionHandleImageLeft`         | PropertyMap | The image to display for the left selection handle.  |
| `SelectionHandleImageRight`        | PropertyMap | The image to display for the right selection handle. |
| `SelectionHandlePressedImageLeft`  | PropertyMap | The image to display for the left selection handle marker.  |
| `SelectionHandlePressedImageRight` | PropertyMap | The image to display for the right selection handle marker. |
| `SelectionHandleMarkerImageLeft`   | PropertyMap | The image to display for the left selection handle marker.  |
| `SelectionHandleMarkerImageRight`  | PropertyMap | The image to display for the right selection handle marker. |
| `SelectionHighlightColor`          | Vector4     | The color of the selection highlight.     |
| `DecorationBoundingBox`            | Rectangle   | The decorations (handles etc) will positioned within this area on-screen. |
| `InputMethodSettings`              | PropertyMap | The settings to relating to the System's Input Method, Key and Value. |
| `InputColor`                       | Vector4     | The color of the new input text.         |
| `EnableMarkup`                     | Boolean     | Whether the mark-up processing is enabled. |
| `InputFontFamily`                  | String      | The font's family of the new input text. |
| `InputFontStyle`                   | PropertyMap | The font's style of the new input text.  |
| `InputPointSize`                   | Float       | The font's size of the new input text in points. |
| `Underline`                        | PropertyMap | The default underline parameters.        |
| `InputUnderline`                   | String      | The underline parameters of the new input text. |
| `Shadow`                           | PropertyMap | The default shadow parameters.           |
| `InputShadow`                      | String      | The shadow parameters of the new input text. |
| `Emboss`                           | PropertyMap | The default emboss parameters.           |
| `InputEmboss`                      | String      | The emboss parameters of the new input text. |
| `Outline`                          | PropertyMap | The default outline parameters.          |
| `InputOutline`                     | String      | The outline parameters of the new input text. |
| `HiddenInputSettings`              | PropertyMap | Hides the input characters and instead shows a default character for password or pin entry. |
| `PixelSize`                        | Float       | The size of font in pixels.              |
| `EnableSelection`                  | Boolean     | Enables Text selection.                  |
| `Placeholder`                      | PropertyMap | Sets the placeholder for text, color, font family, font style, point size, and pixel size. |
| `Ellipsis`                         | Boolean     | Whether we should show the ellipsis if it is required. |
| `TranslatablePlaceholderText`      | String      | The TranslatablePlaceholderText property. The text can set the SID value. |
| `TranslatableText`                 | String      | The TranslatableText property. The text can set the SID value. |


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
