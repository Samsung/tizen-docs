# TextField



The `Dali::Toolkit::TextField` class is a control providing a single-line editable text field.

**Figure: TextField**

![TextField](./media/textfield.png)

## Creating a TextField

Before text has been entered, the `Dali::Toolkit::TextField` class can display a placeholder text. An alternative placeholder can be displayed when the `TextField` has keyboard focus. For example, a `TextField` used to enter a username can initially show the text `Unknown Name`, and the text `Enter Name.` when the cursor is visible.

```
TextField field = TextField::New();
field.SetProperty( TextField::Property::PLACEHOLDER_TEXT, "Unnamed Name" );
field.SetProperty( TextField::Property::PLACEHOLDER_TEXT_FOCUSED, "Enter Name." );
Stage::GetCurrent().Add( field );
```

When the `TextField` is tapped, it automatically gets the keyboard focus. Key events enter the text, and the placeholder text is removed. After text has been entered, it can be retrieved from the `TEXT` property.

```
Property::Value fieldText = field.GetProperty( TextField::Property::TEXT );
std::string fieldTextString = fieldText.Get< std::string >();
```

## Aligning Text

The `Dali::Toolkit::TextField` class displays a single-line of text, which scrolls if there is not enough space for the text displayed. If there is enough space, the text can be aligned horizontally to the beginning, end, or center of the available area:

```
// "CENTER" or "END"
field.SetProperty( TextField::Property::HORIZONTAL_ALIGNMENT, "BEGIN" );
```

## Using Decorations

For text decorations, the following `TextField` class properties are available. All properties are writable and none are animatable.

**Table: TextField properties**

| Property                               | Type      |
|----------------------------------------|-----------|
| `RENDERING_BACKEND`                    | Integer   |
| `TEXT`                                 | String    |
| `PLACEHOLDER_TEXT`                     | String    |
| `PLACEHOLDER_TEXT_FOCUSED`             | String    |
| `FONT_FAMILY`                          | String    |
| `FONT_STYLE`                           | String    |
| `POINT_SIZE`                           | Float     |
| `MAX_LENGTH`                           | Integer   |
| `EXCEED_POLICY`                        | Integer   |
| `HORIZONTAL_ALIGNMENT`                 | String    |
| `VERTICAL_ALIGNMENT`                   | String    |
| `COLOR`                                | Vector4   |
| `SHADOW_OFFSET`                        | Vector2   |
| `SHADOW_COLOR`                         | Vector4   |
| `PRIMARY_CURSOR_COLOR`                 | Vector4   |
| `SECONDARY_CURSOR_COLOR`               | Vector4   |
| `ENABLE_CURSOR_BLINK`                  | Boolean   |
| `CURSOR_BLINK_INTERVAL`                | Float     |
| `CURSOR_BLINK_DURATION`                | Float     |
| `GRAB_HANDLE_IMAGE`                    | String    |
| `GRAB_HANDLE_PRESSED_IMAGE`            | String    |
| `SCROLL_THRESHOLD`                     | Float     |
| `SCROLL_SPEED`                         | Float     |
| `SELECTION_HANDLE_IMAGE_RIGHT`         | String    |
| `SELECTION_HANDLE_PRESSED_IMAGE_LEFT`  | String    |
| `SELECTION_HANDLE_PRESSED_IMAGE_RIGHT` | String    |
| `SELECTION_HIGHLIGHT_COLOR`            | Vector4   |
| `DECORATION_BOUNDING_BOX`              | Rectangle |
| `INPUT_METHOD_SETTINGS`                | Map       |

To change the color of the text, use the `TEXT_COLOR` property. An alternative color can be used for placeholder text by setting the `PLACEHOLDER_TEXT_COLOR` property. Unlike the `Actor::COLOR` property, these properties do not affect child actors added to the `TextField`.

```
field.SetProperty( TextField::Property::TEXT_COLOR, Color::CYAN );
field.SetProperty( TextField::Property::PLACEHOLDER_TEXT_COLOR, Color::BLACK );
```

## Related Information
* Dependencies
 - Tizen 2.4 and Higher for Mobile
 - Tizen 3.0 and Higher for Wearable
