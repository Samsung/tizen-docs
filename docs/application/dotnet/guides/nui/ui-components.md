# UI Components

UI components are interactive components for layout and user interface. NUI provides UI components, such as buttons, table view, text controls, image view, flex container, slider, and video view.

**Figure: UI components**

![UI components](./media/button.png) ![UI components](./media/popup.png)


The following table lists the available UI components:

**Table: UI components**

| Control                              | Description                              | Related classes                          |
| ------------------------------------ | ---------------------------------------- | ---------------------------------------- |
| [Button](./nui-components/Button.md) | A button that can set action when user select it. | `Button`                |
| [CheckBox](./nui-components/CheckBox.md) | A CheckBox that can set selected or unselected status when user selects it. | `CheckBox`                |
| [ImageView](./imageview.md)          | An image view is a class for displaying an image resource.   | `ImageView`                   |
| [Loading](./nui-components/Loading.md) | A loading is used to give information about the ongoing operations. | `Loading`                |
| [Notification](./nui-components/Notification.md) | A notification is used to pop-up a notification window with a content view. | `Notification`                |
| [Pagination](./nui-components/Pagination.md) | A Pagination is used to show the number of pages available and the currently active page. | `Pagination`                |
| [Progress](./nui-components/Progress.md) | A progress is used to show the ongoing status using a long narrow bar. | `Progress`                |
| [RadioButton](./nui-components/RadioButton.md) | A RadioButton that can set selected or unselected status when user selects it. | `RadioButton`                |
| [Slider](./nui-components/Slider.md) | A slider that indicates a modifiable value within a specific range. | `Slider`                   |
| [Switch](./nui-components/Switch.md) | A switch that can be used as a selector. | `Switch`                |
| [TableView](./tableview.md)          | A table view that can align child actors in a grid like layout. | `TableView`             |
| [TextEditor](./texteditor.md)        | A text editor that provides a multi line editable text. | `TextEditor`                |
| [TextField](./textfield.md)          | A text field that provides a single line editable text. | `TextField`                 |
| [TextLabel](./textlabel.md)          | A text label that renders a short text string. | `TextLabel`                |
| [VideoView](./videoview.md)          | A video view that controls and displays video playback. | `VideoView`                 |

The base class for the components is `View`. This class can also be used to create your own custom UI components. For more information on the view class, see [View](./view.md). In this UI Components guide, both the terms **control** and **component** are used to refer to a UI component.

You can [customize the look of the UI components with stylesheets](./styling-controls-with-JSON.md). For a reusable rendering logic that can be used by all UI components, take advantage of [visuals](./visuals.md).


## Related Information
- Dependencies
  -   Tizen 4.0 and Higher