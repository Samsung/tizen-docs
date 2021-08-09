# Styling UI components
Styling of components in NUI is possible in two ways:
  - `ViewStyle`: a set of attributes to decorate a `View`.
  - `Theme`: a set of `ViewStyle` objects to decorate an application. You can load the theme from a XAML resource.

The main purpose of providing style and theme is to separate style details from the application structure. Managing styles separately makes it easier to customize the look of application by user context.

## ViewStyle

The basic styling of NUI components is based on the `ViewStyle` class and its derivatives. `ViewStyle` defines attributes and stores their values. 

The following is a list of the most common attributes:
- Position
- Size
- ParentOrigin

You can find all the attributes and their details on [ViewStyle attributes](https://github.com/Samsung/TizenFX/blob/master/src/Tizen.NUI/src/public/BaseComponents/Style/ViewStyle.cs) page.

The NUI also defines the `ViewStyle` derived classes for components such as `ImageViewStyle`, `TextLabelStyle`, and `TextFieldStyle`:

```csharp
ImageViewStyle blueBGStyle = new ImageViewStyle()
{
  BackgroundColor = Color.Blue
};

TextLabelStyle redTextStyle = new TextLabelStyle()
{
  TextColor = Color.Red,
  PointSize = 20
};

TextFieldStyle textStyle = new TextFieldStyle()
{
  EnableCursorBlink = false
};
```

You can apply the created styles to the corresponding view using `ApplyStyle`:

```csharp
imageView.ApplyStyle(blueBGStyle);

textLabel.ApplyStyle(redTextStyle);

textField.ApplyStyle(textStyle);
```

### ViewStyle with ControlState

The style can also be defined with the `ControlState`:

| State              | Description                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Normal`           | Specifies the default style.                                                                                                                         |
| `Focused`          | Specifies the state where all the keystrokes and events are received by the widget. There can only be one widget in this state at a time in the active window. |
| `Disabled`         | Specifies the state where the widget is disabled. All other events are ignored in this state.                                                          |
| `Selected`         | Specifies the state where the widget is selected.                                                                                                      |
| `Pressed`          |  Specifies the state where the widget receives touch event.                                                                                                                                                   |
| `DisabledFocused`  | Specifies the state that is similar to the `Focused` state, but there is no possibility to change the widget state.                                                                        |
| `SelectedFocused`  | Specifies the state where the widget is checked and all events are received.                                                                                            |
| `DisabledSelected` | Specifies the combination of disabled and selected states.                                                                                                       |

Some attributes are of `Selector` type, which expresses the change of values in different control states:

```csharp
ControlStyle pressableStyle = new ControlStyle()
{
  Size = new Size(100, 100),
  BackgroundColor = new Selector<Color>
  {
      Normal = Color.White,
      Pressed = Color.Yellow,
      Disabled = Color.Grey
  }
};

Control control = new Control();
control.ApplyStyle(pressableStyle);
```

The selectors work when the control state is enabled in a `View`. By default, the control state is enabled for all controls in the `Tizen.NUI.Components` namespace and not for the controls that belong to `Tizen.NUI.BaseComponents` namespace, such as `View` and `TextLabel`. If you want to enable a control state for them, set the `EnableControlState` property to `true`:

```csharp
View view = new View()
{
  EnableControlState = true,
};
```

## Theme

`Theme` is a set of `ViewStyle` objects that helps you to decorate an application. The following is an example of creating and applying a theme:

```csharp
// Define a theme
var theme = new Theme();

theme.AddStyle("BlueStyle", new ViewStyle() {
  BackgroundColor = Color.Blue,
});

theme.AddStyle("YellowTextStyle", new TextLabelStyle() {
  TextColor = Color.Yellow,
  PointSize = 10
});

// Apply the theme to the current application.
ThemeManager.ApplyTheme(theme);

// Create views with style name
var view = new View()
{
  StyleName = "BlueStyle",
};

var text = new TextLabel()
{
  StyleName = "YelloTextStyle"
};
```

Each style in a theme is identified by a style name and is matched to `View.StyleName`. If you set the style name to a full class name such as `Tizen.NUI.BaseComponents.TextLabel`, it applies to all the instances of that type in the application:

```csharp
// Define theme
var theme = new Theme();

theme.AddStyle(typeof(TextLabel).FullName, new TextLabelStyle() {
  TextColor = Color.Yellow,
  PointSize = 10
});


// Apply theme
ThemeManager.ApplyTheme(theme);

// Create view
var text = new TextLabel(); // Yellow text is displayed.
```

> [!NOTE]
> If you want views to change style whenever the theme is changed, you need to set a `ThemeChangeSensitive` property to `true`. The property is set as `false` by default unless the view has a style name.
>```csharp
>view.ThemeChangeSensitive = true;
>```

## Define theme using XAML

It is better to use XAML theme files in advanced applications to define UI style for NUI widgets. With XAML files, it is easier to share styles between different applications. From the application architecture point of view, XAML allows for better separation of view definitions from application logic.

The basic theme defined in the earlier section can be implemented using XAML as follows:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Theme
  xmlns="http://tizen.org/Tizen.NUI/2018/XAML"
  xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml">

  <ViewStyle x:Key="BlueStyle" BackgroundColor="Blue" />
  <TextLabelStyle x:Key="YellowTextStyle" TextColor="Yellow" PointSize="10" />

</Theme>
```
```csharp
var theme = new Theme("<path to the xamlfile.xaml>");
```

### Define selector using XAML

The creation of a `Selector` object defines the various states of a component. In `Selector` constructor, individual states must be specified:

```csharp
Selector selector = new Selector<Color>()
{
  Normal = Color.Black,
  Pressed = Color.Blue,
  Disabled = Color.Red
};
```

The equivalent XAML code is as follows:

```xml
<Selector x:TypeArguments="Color" Normal="Black" Pressed="Blue" Disabled="Red"/>
```

## Handle theme changes in runtime

The following methods can be used to handle theme changes in runtime:

- `ThemeManager.ThemeChanged`
- `View.OnThemeChanged`

When `ThemeManager.ApplyTheme` is called, `ThemeManager` calls the `ThemeChanged` callback. The following example shows how to handle `ThemeChanged` events:

```csharp
using Tizen.NUI;

namespace NUI_Theme
{
  class Program : NUIApplication
  {
    protected override void OnCreate()
    {
      //application init

      ThemeManager.ThemeChanged += OnThemeChanged;
    }

    private void OnThemeChanged(object sender, ThemeChangedEventArgs args) 
    {
      //Implement reaction on theme change here.
    }
  }
}
```

The `View.OnThemeChanged` is used when you create a class that is derived from `View`. You can overload `OnThemeChanged` so that all functionalities related to the looks of the widget are implemented in one class:

```csharp 
class AlwaysBlueTextLabel : TextLabel
{
  protected override void OnThemeChanged(object sender, ThemeChangedEventArgs e)
  {
    // Theme has changed but the new style is not applied to this view yet.

    // Call base method to apply new style in new theme to this view.
    base.OnThemeChanged(sender, e);

    // Set text color to blue.
    textLabel.TextColor = Color.Blue;
  }
}
```

## Related Information
- Examples
  - [XAML syntax](https://github.com/dalihub/nui-demo/blob/master/ThemeExample/docs/NUIXamlStyleSyntax.md)
  - [XAML theme manager](https://github.com/dalihub/nui-demo/tree/master/ThemeExample/Basic1)
  - [XAML Todo List](https://github.com/dalihub/nui-demo/tree/master/ThemeExample/TodoList)
- Dependencies
  -   Tizen 6.5 and Higher
