# TextEditor



The `Dali::Toolkit::TextEditor` class provides a control that allows multi-line text editing. It is similar to the [TextField](textfield.md) control, where a different formatting can be applied to different parts of the text.  You can change, for example, the font color, font style, point size, and font family.

The `TextEditor` also supports markup, and text can be scrolled vertically within it.

**Figure: TextEditor**

![TextEditor](./media/dali_texteditor.png)

The following table lists the basic signals provided by the `Dali::Toolkit::TextEditor` class.

**Table: Dali::Toolkit::TextEditor input signals**

| Input signal                | Description                              |
|-----------------------------|------------------------------------------|
| `TextChangedSignal()`       | Emitted when the text changes.           |
| `InputStyleChangedSignal()` | Emitted when the input style is updated as a consequence of a change in the cursor position. |

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

## Modifying TextEditor Properties

You can modify the `TextEditor` appearance and behavior through its properties. To change a property from its default value, use the `SetProperty()` function.

The following table lists the available `TextEditor` properties.

## Related Information
* Dependencies
 - Tizen 3.0 and Higher for Mobile
 - Tizen 3.0 and Higher for Wearable
