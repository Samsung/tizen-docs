# Styling Components
Tizen 6.5 introduce two new methods for styling components derived from `View` object:
  * `ViewStyle`: designed for simple themes
  * XAML file : designed for advanced themes, changed in runtime, shared between applicaitons

# Basic themes
Basic styling of NUI components is based on the `ViewStyle` class and its derivatives. `ViewStyle` defines an attributes and stores 
its values. Below is a list of most common attributes:  
* name
* state 
* sub state
* position
* scale
* orientation
* padding 

You can find all attributes and details in: [ViewStyle attributes](https://github.com/Samsung/TizenFX/blob/master/src/Tizen.NUI/src/public/BaseComponents/Style/ViewStyle.cs)

In addition, components may be in the following states, for which styles can also be defined:
* Normal
* Focused
* Disabled 
* Selected 
* Pressed 
* DisabledFocused
* SelectedFocused 
* DisabledSelected

The NUI also defines the ViewStyle derived classes for components:  `ImageView`, `TextLabel` and `TextField`

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

# XAML themes

In more advanced applications it is better to use XAML Theme files to define UI style for NUI widgets. With XAML files it is easier to share styles between different applications. From the point of view of the application architecture, XAML allows for better separation of view definitions from application logic.

## XAML Example

Basic text style defined in previous section could be implemented using XAML in the following way:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Theme
  xmlns="http://tizen.org/Tizen.NUI/2018/XAML"
  xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml">

  <TextLabelStyle x:Key="redTextStyle" TextColor="Red" PointSize="20" />
</Theme>
```

## XAML states

Some properties in ViewStyle are Selector types that can have multiple values by control's state.

```csharp
Selector selector = new Selector<Color>()
{
  Normal = Color.Black,
  Pressed = Color.Blue,
  Disabled = Color.Red
};
```

The same xaml code is,

```xml
<Selector x:TypeArguments="Color" Normal="Black" Pressed="Blue" Disabled="Red"/>
```

Selectors works when the control state is enabled in a View. Control state are enabled for all controls in Tizen.NUI.Components by default, but not for those in Tizen.NUI.BaseComponents, such as View and TextLabel. If you want to enable control state for them, please set EnableControlState property to true.

```xml
<ViewStyle x:Key="viewColoredByTouch" EnableControlState="true">
  <ViewStyle.BackgroundColor>
      <Selector x:TypeArguments="Color" Normal="Black" Pressed="Blue" Disabled="Red"/>
  </ViewStyle.BackgroundColor>
</ViewStyle>
```
}

## Load theme in NUI application

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

## Handle theme changes in runtime

Two methods can be used to handle theme changes:
* `ThemeManager.ThemeChanged`
* `View.OnThemeChanged`

ThemeManager provides an event raised after theme changed.

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

`View.OnThemeChanged` should be used when creating a class derived from View, then we can overload `OnThemeChanged` so that all functionalities related to the look of the widget are implemented in one class.

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

## Additional informations:
  * [XAML syntax](https://github.com/dalihub/nui-demo/blob/master/ThemeExample/docs/NUIXamlStyleSyntax.md)
  * [XAML basic example](https://github.com/dalihub/nui-demo/tree/master/ThemeExample/Basic1)
  * [XAML basic example](https://github.com/dalihub/nui-demo/tree/master/ThemeExample/Basic2)
  * [XAML Todo List](https://github.com/dalihub/nui-demo/tree/master/ThemeExample/TodoList)

## Dependencies
  -   Tizen 6.5 and Higher
