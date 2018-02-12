# TextEditor



The `Dali::Toolkit::TextEditor` class provides a control that allows multi-line text editing. It is similar to the [TextField](textfield.md) control, where a different formatting can be applied to different parts of the text.  You can change, for example, the font color, font style, point size, and font family.

The `TextEditor` also supports markup, and text can be scrolled vertically within it.

**Figure: TextEditor**

![TextEditor](./media/dali_texteditor.png)

In this tutorial, the following subjects are covered:

[TextEditor events](#1)<br>
[Creating a TextEditor](#2)<br>
[TextEditor Properties](#3)<br>

<a name="1"></a>
## TextEditor events

The following table lists the basic signals provided by the `Dali::Toolkit::TextEditor` class.

**Table: Dali::Toolkit::TextEditor input signals**

| Input signal                 | Description                              |
|----------------------------|----------------------------------------|
| `TextChangedSignal()`        | Emitted when the text changes.           |
| `InputStyleChangedSignal()`  | Emitted when the input style is updated as a consequence of a change in the cursor position. |
| `ScrollStateChangedSignal()` | Emitted when TextEditor scrolling is started or finished. |

<a name="2"></a>
## Creating a TextEditor

The following basic example shows how to create a `Dali::Toolkit::TextEditor` object:

```
TextEditor editor = TextEditor::New();
editor.SetSize( mStageWidth, mStageHeight * 0.4f );
editor.SetAnchorPoint( AnchorPoint::TOP_CENTER );
editor.SetParentOrigin( ParentOrigin::TOP_CENTER );
editor.SetProperty( TextEditor::Property::DECORATION_BOUNDING_BOX, boundingBox );
editor.SetProperty( TextEditor::Property::TEXT_COLOR, Color::BLACK );
editor.SetProperty( TextEditor::Property::TEXT,
                    "This is a multiline text.\n"
                    "I can write several lines.\n"
                    "Line wrapping is also supported for very long sentences."
                    "The text should be scrollable as well.\n" );
Stage::GetCurrent().Add( editor );
```

<a name="3"></a>
## TextEditor Properties

You can modify the `TextEditor` appearance and behavior through its properties. To change a property from its default value, use the `SetProperty()` function.

The following table lists the available `TextEditor` properties.

**Table: TextEditor properties**

| Property                               | Type      | Description                              |
|--------------------------------------|---------|----------------------------------------|
| `RENDERING_BACKEND`                    | INTEGER   | The type or rendering e.g. bitmap-based  |
| `TEXT`                                 | STRING    | The text to display in UTF-8 format      |
| `TEXT_COLOR`                           | VECTOR4   | The text color                           |
| `FONT_FAMILY`                          | STRING    | The requested font family                |
| `FONT_STYLE`                           | STRING or MAP | The requested font style             |
| `POINT_SIZE`                           | FLOAT     | The size of font in points               |
| `MAX_LENGTH`                           | INTEGER   | The maximum number of characters that can be inserted |
| `EXCEED_POLICY`                        | INTEGER   | Specifies how the text is truncated when it does not fit |
| `HORIZONTAL_ALIGNMENT`                 | STRING    | The line horizontal alignment            |
| `SCROLL_THRESHOLD`                     | FLOAT     | Horizontal scrolling will occur if the cursor is this close to the control border |
| `SCROLL_SPEED`                         | FLOAT     | The scroll speed in pixels per second    |
| `PRIMARY_CURSOR_COLOR`                 | VECTOR4   | The color to apply to the primary cursor |
| `SECONDARY_CURSOR_COLOR`               | VECTOR4   | The color to apply to the secondary cursor |
| `ENABLE_CURSOR_BLINK`                  | BOOLEAN   | Whether the cursor should blink or not      |
| `CURSOR_BLINK_INTERVAL`                | FLOAT     | The time interval in seconds between cursor on/off states |
| `CURSOR_BLINK_DURATION`                | FLOAT     | The cursor will stop blinking after this number of seconds |
| `CURSOR_WIDTH`                         | INTEGER   | The cursor width                         |
| `GRAB_HANDLE_IMAGE`                    | STRING    | The image to display for the grab handle |
| `GRAB_HANDLE_PRESSED_IMAGE`            | STRING    | The image to display when the grab handle is pressed |
| `SELECTION_HANDLE_IMAGE_LEFT`          | MAP       | The image to display for the left selection handle |
| `SELECTION_HANDLE_IMAGE_RIGHT`         | MAP       | The image to display for the right selection handle |
| `SELECTION_HANDLE_PRESSED_IMAGE_LEFT`  | MAP       | The image to display for the left selection handle marker |
| `SELECTION_HANDLE_PRESSED_IMAGE_RIGHT` | MAP       | The image to display for the right selection handle marker |
| `SELECTION_HANDLE_MARKER_IMAGE_LEFT`   | MAP       | The image to display for the left selection handle marker |
| `SELECTION_HANDLE_MARKER_IMAGE_RIGHT`  | MAP       | The image to display for the right selection handle marker |
| `SELECTION_HIGHLIGHT_COLOR`            | VECTOR4   | The color of the selection highlight     |
| `DECORATION_BOUNDING_BOX`              | RECTANGLE | The decorations (handles etc) will positioned within this area on-screen |
| `ENABLE_MARKUP`                        | BOOLEAN   | Whether the mark-up processing is enabled |
| `INPUT_COLOR`                          | VECTOR4   | The color of the new input text          |
| `INPUT_FONT_FAMILY`                    | STRING    | The font's family of the new input text  |
| `INPUT_FONT_STYLE`                     | MAP       | The font's style of the new input text   |
| `INPUT_POINT_SIZE`                     | FLOAT     | The font's size of the new input text in points |
| `LINE_SPACING`                         | FLOAT     | The default extra space between lines in points |
| `INPUT_LINE_SPACING`                   | FLOAT     | The extra space between lines in points  |
| `UNDERLINE`                            | MAP       | The default underline parameters         |
| `INPUT_UNDERLINE`                      | MAP       | The underline parameters of the new input text |
| `SHADOW`                               | MAP       | The default shadow parameters            |
| `INPUT_SHADOW`                         | MAP       | The shadow parameters of the new input text |
| `EMBOSS`                               | MAP       | The default emboss parameters            |
| `INPUT_EMBOSS`                         | MAP       | The emboss parameters of the new input text |
| `OUTLINE`                              | MAP       | The default outline parameters           |
| `INPUT_OUTLINE`                        | MAP       | The outline parameters of the new input text |
| `SMOOTH_SCROLL`                        | BOOLEAN   | Enable or disable the smooth scroll animation |
| `SMOOTH_SCROLL_DURATION`               | FLOAT     | Sets the duration of smooth scroll animation |
| `ENABLE_SCROLL_BAR`                    | BOOLEAN   | Enable or disable the scroll bar          |
| `SCROLL_BAR_SHOW_DURATION`             | FLOAT     | Sets the duration of scroll bar to show  |
| `SCROLL_BAR_FADE_DURATION`             | FLOAT     | Sets the duration of scroll bar to fade out |
| `PIXEL_SIZE`                           | FLOAT     | The size of font in pixels               |
| `LINE_COUNT`                           | INTEGER   | The line count of text                   |
| `ENABLE_SELECTION`                     | BOOLEAN   | Enables Text selection                   |
| `PLACEHOLDER`                          | MAP       | Sets the placeholder : text, color, font family, font style, point size, and pixel size |
| `LINE_WRAP_MODE`                       | INTEGER or STRING | Line wrap mode when text lines are greater than the layout width |

## Related Information
- Dependencies
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
