# Button

A button is a small object on the UI that you press in order to operate it.
The NUI button controls include various button types:

- `PushButton` changes its appearance when pressed, and returns to its original appearance when released.
- `Checkbox` can be checked or unchecked.
- `Radio` button has 2 states, selected and unselected. Usually radio buttons are grouped, and only 1 radio button in a group can be selected at a given time.
- `Toggle` button allows the user to switch a feature on or off. Toggle buttons also support tooltips.

The `Button` class is the base class for the button UI components.

<a name="creation"></a>
## Creating a Button

To create a button:

-   Create a push button.

    In the following example, the button is added to a Table View UI component:

    ```
    private TableView _contentContainer;

    _window = Window.Instance;
    _contentContainer = new TableView(6, 5);

    // Other UI components

    PushButton button = new PushButton();
    button.LabelText = "Process";
    button.ParentOrigin = ParentOrigin.BottomLeft;

    _contentContainer.AddChild(button, new TableView.CellPosition(....);
    _window.Add(_contentContainer);
    ```

- Create a checkbox:

    ```
    CheckBoxButton checkBoxbutton = new CheckBoxButton();
    checkBoxbutton.LabelText = "Yes";
    checkBoxbutton.BackgroundColor = Color.White;
    ```

- Create a group of radio buttons:

    ```
    View radioGroup = new View();
    radioGroup.SetParentOrigin.Centre;

    RadioButton button1 = new RadioButton();
    button1.LabelText = "Yes";
    button1.Selected = true;
    radioGroup.Add(button1);

    RadioButton button2 = new RadioButton();
    button2.LabelText = "No";
    radioGroup.Add(button2);
    ```

- Create a toggle button:

    ```
    ToggleButton toggleButton = new ToggleButton();
    ```

<a name="states"></a>
## Button States

Each button can be in the `selectable`, `disabled`, and `togglable` states.

The `Button` class provides the `Toggable` and `Selected` properties. The `View` class provides the `Disabled` property.

<a name="events"></a>
## Button Events

There are 4 events associated with the `Button` class:

-   `Clicked`: The button is touched, and the touch point does not leave the boundary of the button.
-   `Pressed`: The button is touched.
-   `Released`: The button is touched, and the touch point leaves the boundary of the button.
-   `StateChanged`: The button state is changed.

For example, to add an event handler to the `Clicked` event of a push button:

```
pushButton.Clicked += (obj, e) =>
{
    PushButton sender = obj as PushButton;
    sender.LabelText = "Click Me";

    return true;
};
```

Events do not trigger if the `Disabled` property of the button is set to `true`.

The `Button` class provides the following properties which modify the triggered events:

-   If the `AutoRepeating` property is set to `true`, the `Pressed`, `Released`, and `Clicked` events are fired at regular intervals while the button is touched.

    The interval times can be modified with the `InitialAutoRepeatingDelay` and `NextAutoRepeatingDelay` properties.

    A togglable button cannot be autorepeated. If the `AutoRepeating` property is set to `true`, the `Togglable` property is set to `false` but no event is fired.

- If the `Togglable` property is set to `true`, a `StateChanged` event is fired with the selected state.

For a checkbox, all 4 events are available, though usually only the `StateChanged` event is used to notify when the button changes its state to selected or unselected.

For a radio button, use the `StateChanged` event to check when the radio button is selected.

<a name="visuals"></a>
## Button Visuals

Visuals provide reusable rendering logic which can be used by all controls. Images and icons are added to buttons using visuals.

The button's appearance can be modified by setting properties for the various state visuals. A control has 3 states: `NORMAL`, `FOCUSED`, and `DISABLED`. Buttons have substates: `SELECTED` and `UNSELECTED`. Each state and substate needs to have a visual defined for it. A visual can be shared between states.

When the button pressed, the `unselected` visuals are replaced by the `selected` visuals. The text label is always placed on the top of all images.

When the button is disabled, the background, button, and selected visuals are replaced by their `disabled` counterparts.

The following example illustrates the toggle button `StateVisuals` property, which has visuals for each state:

```
ToggleButton toggleButton = new ToggleButton();

PropertyArray array = new PropertyArray();
array.Add(new PropertyValue("./media/star-highlight.png"));
array.Add(new PropertyValue("./media/star-mod.png"));
array.Add(new PropertyValue("./media/star-dim.png"));
toggleButton.StateVisuals = array;

PropertyArray tooltips = new PropertyArray();
tooltips.Add(new PropertyValue("State A"));
tooltips.Add(new PropertyValue("State B"));
tooltips.Add(new PropertyValue("State C"));
toggleButton.Tooltips = tooltips;

toggleButton.WidthResizePolicy  = ResizePolicyType.FillToParent;
toggleButton.HeightResizePolicy = ResizePolicyType.FillToParent;
```

For more information on button styling with visuals, see [Styling Controls with JSON](styling-controls-with-JSON.md).


## Tooltips


There are various methods of adding tooltips to a button:

-   Use the `TooltipText` property, which is inherited from the `View` class:

    ```
    PushButton button = new PushButton();

    // Add a simple text-only tooltip
    button.TooltipText = "Simple Tooltip";
    ```

- Use a property array, as shown in the example in [Button Visuals](#visuals).
- Property maps

    In the following example, an array of property maps is created for a tooltip with 1 icon and 1 text visual:

    ```
    PushButton button = new PushButton();

    // Create a property map for a tooltip with 1 icon and 1 text
    PropertyArray iconTooltipContent = new Property.Array();

    // Icon
    PropertyMap iconVisual = new PropertyMap();
    iconVisual.Add(Constants.Visual.Property.Type, new PropertyValue((int)Constants.Visual.Type.Image))
              .Add(Constants.ImageVisualProperty.URL, new PropertyValue("./media/star-highlight.png"));

    iconTooltipContent.Add(new PropertyValue(iconVisual));

    // Text
    PropertyMap textVisual = new PropertyMap();
    textVisual.Add(Constants.Visual.Property.Type, new PropertyValue((int)Constants.Visual.Type.Text))
              .Add(Constants.TextVisualProperty.Text, new PropertyValue("Tooltip with Icon"));

    iconTooltipContent.Add(new PropertyValue(textVisual));

    // Icon tooltip
    PropertyMap iconTooltip = new PropertyMap();
    iconTooltip.Add(Constants.Tooltip.Property.Content, new Property.Value(iconTooltipContent))
               .Add(Constants.Tooltip.Property.Tail, new PropertyValue(true));

    // Add the tooltip with icon and text to the push button
    button.Tooltip = iconTooltip;
    ```

    The `Tooltip` property is inherited from the *View* class.

<a name="properties"></a>
## Button Properties

The `Button` class has the following properties:

| Property                             | Type      | Description                              |
| ------------------------------------ | --------- | ---------------------------------------- |
| `UnselectedVisual`                   | `Map`     | Map describing a visual, changes depending on the button state |
| `SelectedVisual`                     | `Map`     | Map describing a visual, changes depending on the button state |
| `DisabledUnselectedVisual`           | `Map`     | Map describing a visual, changes depending on the button state |
| `DisabledSelectedVisual`             | `Map`     | Map describing a visual, changes depending on the button state |
| `UnselectedBackgroundVisual`         | `Map`     | Map describing a visual, changes depending on the button state |
| `SelectedBackgroundVisual`           | `Map`     | Map describing a visual, changes depending on the button state |
| `DisabledUnselectedBackgroundVisual` | `Map`     | Map describing a visual, changes depending on the button state |
| `DisabledSelectedBackgroundVisual`   | `Map`     | Map describing a visual, changes depending on the button state |
| `LabelRelativeAlignment`             | `Align`   | Position of the text label in relation to foreground/icon when both are present |
| `LabelPadding`                       | `Vector4` | Padding area around the label (if present) |
| `ForegroundVisualPadding`            | `Vector4` | Padding area around the foreground/icon visual (if present) |
| `AutoRepeating`                      | `bool`    | Toggles the autorepeating state. For more information, see [Button Events](#events). |
| `InitialAutoRepeatingDelay`          | `float`   | Initial autorepeating delay in seconds (default: 0.15 s) |
| `NextAutoRepeatingDelay`             | `float`   | Continuous autorepeating delay in seconds (default: 0.05 s) |
| `Togglable`                          | `bool`    | If the `Togglable` property is set to `true`, the `AutoRepeating` property is set to `false`. |
| `Selected`                           | `bool`    | Sets a togglable button as either selected or unselected |
| `UnselectedColor`                    | `Color`   | Gets/sets the unselected color           |
| `SelectedColor`                      | `Color`   | Gets/sets the selected color             |
| `Label`                              | `Map`     | Button text label                        |
| `LabelText`                          | `string`  | Button text label                        |

> **Note**   
> If the `AutoRepeating` property is set to `true`, the `Togglable` property is set to `false`.

The **ToggleButton** class has the following additional properties:

| Property            | Type    | Description                              |
| ------------------- | ------- | ---------------------------------------- |
| `StateVisuals`      | `Array` | Array of property-maps, or a property array of strings. The property maps expect a description of a visual, and the strings represent image URLs. |
| `Tooltips`          | `Array` | Array of toggle state tooltip strings. Each tooltip string must match a toggle state |
| `CurrentStateIndex` | `int`   | Current state                            |


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
