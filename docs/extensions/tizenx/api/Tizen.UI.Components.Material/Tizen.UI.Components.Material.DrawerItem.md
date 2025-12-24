### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## DrawerItem Class

DrawerItem is a component that can be selected among the [Tizen.UI.Components.SelectionGroup](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.SelectionGroup 'Tizen.UI.Components.SelectionGroup').

```csharp
public class DrawerItem : Tizen.UI.Components.GroupSelectable,
Tizen.UI.IText,
Tizen.UI.Components.IFlexibleText
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; [Tizen.UI.Components.Pressable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.Pressable 'Tizen.UI.Components.Pressable') &#129106; [Tizen.UI.Components.Clickable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.Clickable 'Tizen.UI.Components.Clickable') &#129106; [Tizen.UI.Components.Selectable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.Selectable 'Tizen.UI.Components.Selectable') &#129106; [Tizen.UI.Components.GroupSelectable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.GroupSelectable 'Tizen.UI.Components.GroupSelectable') &#129106; DrawerItem

Implements [Tizen.UI.IText](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText 'Tizen.UI.IText'), [Tizen.UI.Components.IFlexibleText](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IFlexibleText 'Tizen.UI.Components.IFlexibleText')
### Constructors

<a name='Tizen.UI.Components.Material.DrawerItem.DrawerItem()'></a>

## DrawerItem() Constructor

Constructs a default Drawer item.

```csharp
public DrawerItem();
```

<a name='Tizen.UI.Components.Material.DrawerItem.DrawerItem(string)'></a>

## DrawerItem(string) Constructor

Constructs a Drawer item with specified text.

```csharp
public DrawerItem(string text);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DrawerItem.DrawerItem(string).text'></a>

`text` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The text to display on the Drawer item.

<a name='Tizen.UI.Components.Material.DrawerItem.DrawerItem(string,Tizen.UI.Components.Material.DrawerItemVariables)'></a>

## DrawerItem(string, DrawerItemVariables) Constructor

Constructs a Drawer item with specified text and variables.

```csharp
public DrawerItem(string text, Tizen.UI.Components.Material.DrawerItemVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DrawerItem.DrawerItem(string,Tizen.UI.Components.Material.DrawerItemVariables).text'></a>

`text` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The text to display on the Drawer item.

<a name='Tizen.UI.Components.Material.DrawerItem.DrawerItem(string,Tizen.UI.Components.Material.DrawerItemVariables).variables'></a>

`variables` [DrawerItemVariables](Tizen.UI.Components.Material.DrawerItemVariables.md 'Tizen.UI.Components.Material.DrawerItemVariables')

Custom variables for the Drawer item.

<a name='Tizen.UI.Components.Material.DrawerItem.DrawerItem(Tizen.UI.Components.Material.DrawerItemVariables)'></a>

## DrawerItem(DrawerItemVariables) Constructor

Constructs an empty Drawer item with specified variables.

```csharp
public DrawerItem(Tizen.UI.Components.Material.DrawerItemVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DrawerItem.DrawerItem(Tizen.UI.Components.Material.DrawerItemVariables).variables'></a>

`variables` [DrawerItemVariables](Tizen.UI.Components.Material.DrawerItemVariables.md 'Tizen.UI.Components.Material.DrawerItemVariables')

Custom variables for the Drawer item.
### Properties

<a name='Tizen.UI.Components.Material.DrawerItem.AutoFontSize'></a>

## DrawerItem.AutoFontSize Property

Gets or sets the auto font size.

```csharp
public Tizen.UI.AutoFontSize AutoFontSize { get; set; }
```

Implements [AutoFontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IFlexibleText.AutoFontSize 'Tizen.UI.Components.IFlexibleText.AutoFontSize')

#### Property Value
[Tizen.UI.AutoFontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AutoFontSize 'Tizen.UI.AutoFontSize')

<a name='Tizen.UI.Components.Material.DrawerItem.FontFamily'></a>

## DrawerItem.FontFamily Property

Gets or sets the font family of the text.

```csharp
public string FontFamily { get; set; }
```

Implements [FontFamily](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.FontFamily 'Tizen.UI.IText.FontFamily')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.DrawerItem.FontSize'></a>

## DrawerItem.FontSize Property

Gets or sets the font size of the text.

```csharp
public float FontSize { get; set; }
```

Implements [FontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IFlexibleText.FontSize 'Tizen.UI.Components.IFlexibleText.FontSize'), [FontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.FontSize 'Tizen.UI.IText.FontSize')

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.DrawerItem.Text'></a>

## DrawerItem.Text Property

Gets or sets the text of the Drawer item.

```csharp
public string Text { get; set; }
```

Implements [Text](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.Text 'Tizen.UI.IText.Text')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.DrawerItem.TextColor'></a>

## DrawerItem.TextColor Property

Gets or sets the color of the text.

```csharp
public Tizen.UI.Color TextColor { get; set; }
```

Implements [TextColor](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.TextColor 'Tizen.UI.IText.TextColor')

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.Material.DrawerItem.TextOverflow'></a>

## DrawerItem.TextOverflow Property

Gets or sets the text ellipsize mode to be applied when the text overflows.

```csharp
public Tizen.UI.TextOverflow TextOverflow { get; set; }
```

Implements [TextOverflow](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IFlexibleText.TextOverflow 'Tizen.UI.Components.IFlexibleText.TextOverflow')

#### Property Value
[Tizen.UI.TextOverflow](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.TextOverflow 'Tizen.UI.TextOverflow')
### Methods

<a name='Tizen.UI.Components.Material.DrawerItem.GetTouchEffectSecondaryTarget()'></a>

## DrawerItem.GetTouchEffectSecondaryTarget() Method

Get the secondary target view to apply feedback.

```csharp
public override Tizen.UI.View GetTouchEffectSecondaryTarget();
```

Implements [GetTouchEffectSecondaryTarget()](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.ITouchEffectTarget.GetTouchEffectSecondaryTarget 'Tizen.UI.Components.ITouchEffectTarget.GetTouchEffectSecondaryTarget')

#### Returns
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')













































