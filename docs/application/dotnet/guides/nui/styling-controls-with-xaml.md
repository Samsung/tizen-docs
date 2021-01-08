# Styling Components
Tizen 6.5 introduces two new methods for styling components derived from the `View` object:
  - `ViewStyle`: designed for simple themes
  -  XAML file: designed for advanced themes, styles change in runtime and can be shared between the applications

## Basic NUI themes
The basic styling of NUI components is based on the `ViewStyle` class and its derivatives. `ViewStyle` defines attributes and stores their values. 

The following is a list of the most common attributes:  
- name
- state 
- sub state
- position
- scale
- orientation
- padding 

You can find all the attributes and their details in [ViewStyle attributes](https://github.com/Samsung/TizenFX/blob/master/src/Tizen.NUI/src/public/BaseComponents/Style/ViewStyle.cs) page.

In addition, styles can also be defined for the components with following states:
- Normal
- Focused
- Disabled 
- Selected 
- Pressed 
- DisabledFocused
- SelectedFocused 
- DisabledSelected

The NUI also defines the `ViewStyle` derived classes for components such as  `ImageView`, `TextLabel` and `TextField`:

```csharp
ImageViewStyle swtichImageStyle = new ImageViewStyle
{
    ResourceURL = new StringSelector
    {
        Normal = "controller_switch_bg_off.png",
        Selected = "controller_switch_bg_on.png",
        Disabled = "controller_switch_bg_off_dim.png",
        DisabledSelected = "controller_switch_bg_on_dim.png"
    }
};

TettLabelStyle redTextStyle = new TextLabelStyle()
{
  TextColor = Color.Red,
  PointSize = 20
};

TextFieldStyle textStyle = new TextFieldStyle()
{
  EnableCursorBlink = False
};
```

## Define theme using XAML

It is better to use XAML theme files in advanced applications to define UI style for NUI widgets. With XAML files, it is easier to share styles between different applications. From the application architecture point of view, XAML allows for better separation of view definitions from application logic.

### XAML example

 The basic text styles defined in the earlier section can be implemented using XAML as follows:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Theme
  xmlns="http://tizen.org/Tizen.NUI/2018/XAML"
  xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml">

  <TextLabelStyle x:Key="redTextStyle" TextColor="Red" PointSize="20" />
</Theme>
```

### Handle component states

Defining different states of a component is based on creating an `Selector` object. In `Selector` constructor individual states should be specified. 

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

The selectors work when the control state is enabled in a `View`. By default, the control state is enabled for all controls in `Tizen.NUI.Components` and not for the controls in `Tizen.NUI.BaseComponents`, such as `View` and `TextLabel`. If you want to enable a control state for them, set the `EnableControlState` property to `true`:

```xml
<ViewStyle x:Key="viewColoredByTouch" EnableControlState="true">
  <ViewStyle.BackgroundColor>
      <Selector x:TypeArguments="Color" Normal="Black" Pressed="Blue" Disabled="Red"/>
  </ViewStyle.BackgroundColor>
</ViewStyle>
```
}

### Load theme in NUI application

To use the theme implemented in XAML, follow these steps: 

1. Create a theme object, `Theme theme = new Theme("PATH")`, where PATH is a full path to the XAML file in a project.
2. Use `ThemeManager` to apply theme as `ThemeManager.apply(theme)`
3. Use style defined in the XAML file in NUI component by setting the StyleName parameter to `component.StyleName = xaml_style_name`

The following example explains the implementation of the `TextLabel` NUI component:

```csharp
using Tizen.NUI; 

namespace NUI_Theme
{
  class Program : NUIApplication
  {
    protected override void OnCreate()
    {
      // Load theme from the xaml file
      Theme theme = new Theme("full_path_of_the_xaml_file.xaml");

      // Apply it to the current NUI Application
      ThemeManager.ApplyTheme(theme);

      // Set style name in NUI widget
      TextLabel textLabel = new TextLabel()
      textLabel.StyleName = "redTextStyle";
    }
  }
```

### Handle theme changes in runtime

The following methods can be used to handle theme changes in runtime:

- `ThemeManager.ThemeChanged`
- `View.OnThemeChanged`
* `ThemeManager.ThemeChanged`
* `View.OnThemeChanged`

When `ThemeManager.applyTheme` is called, `ThemeManager` calls the `ThemeChanged` callback. The following example shows how to handle `ThemeChanged` events. 

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

The `View.OnThemeChanged` should be used when creating a class derived from `View`. You can overload `OnThemeChanged` so that all functionalities related to the looks of the widget are implemented in one class:

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

## Additional information:
  * [XAML syntax](https://github.com/dalihub/nui-demo/blob/master/ThemeExample/docs/NUIXamlStyleSyntax.md)
  * [XAML basic example](https://github.com/dalihub/nui-demo/tree/master/ThemeExample/Basic1)
  * [XAML basic example](https://github.com/dalihub/nui-demo/tree/master/ThemeExample/Basic2)
  * [XAML Todo List](https://github.com/dalihub/nui-demo/tree/master/ThemeExample/TodoList)

## Dependencies
  -   Tizen 6.5 and Higher
