### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## DropdownItem Class

DropdownListItem is a component that can be selected among the [Tizen.UI.Components.SelectionGroup](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.SelectionGroup 'Tizen.UI.Components.SelectionGroup').

```csharp
public class DropdownItem : Tizen.UI.Components.GroupSelectable,
Tizen.UI.Components.IFlexibleText,
Tizen.UI.IText
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; [Tizen.UI.Components.Pressable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.Pressable 'Tizen.UI.Components.Pressable') &#129106; [Tizen.UI.Components.Clickable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.Clickable 'Tizen.UI.Components.Clickable') &#129106; [Tizen.UI.Components.Selectable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.Selectable 'Tizen.UI.Components.Selectable') &#129106; [Tizen.UI.Components.GroupSelectable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.GroupSelectable 'Tizen.UI.Components.GroupSelectable') &#129106; DropdownItem

Derived  
&#8627; [DropdownActionItem](Tizen.UI.Components.Material.DropdownActionItem.md 'Tizen.UI.Components.Material.DropdownActionItem')  
&#8627; [DropdownCheckItem](Tizen.UI.Components.Material.DropdownCheckItem.md 'Tizen.UI.Components.Material.DropdownCheckItem')

Implements [Tizen.UI.Components.IFlexibleText](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IFlexibleText 'Tizen.UI.Components.IFlexibleText'), [Tizen.UI.IText](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText 'Tizen.UI.IText')
### Constructors

<a name='Tizen.UI.Components.Material.DropdownItem.DropdownItem()'></a>

## DropdownItem() Constructor

Construct a new instance.

```csharp
public DropdownItem();
```

<a name='Tizen.UI.Components.Material.DropdownItem.DropdownItem(string)'></a>

## DropdownItem(string) Constructor

Construct a new instance.

```csharp
public DropdownItem(string text);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DropdownItem.DropdownItem(string).text'></a>

`text` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.DropdownItem.DropdownItem(string,Tizen.UI.Components.Material.DropdownItemVariables)'></a>

## DropdownItem(string, DropdownItemVariables) Constructor

Construct a new instance.

```csharp
public DropdownItem(string text, Tizen.UI.Components.Material.DropdownItemVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DropdownItem.DropdownItem(string,Tizen.UI.Components.Material.DropdownItemVariables).text'></a>

`text` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.DropdownItem.DropdownItem(string,Tizen.UI.Components.Material.DropdownItemVariables).variables'></a>

`variables` [DropdownItemVariables](Tizen.UI.Components.Material.DropdownItemVariables.md 'Tizen.UI.Components.Material.DropdownItemVariables')

<a name='Tizen.UI.Components.Material.DropdownItem.DropdownItem(Tizen.UI.Components.Material.DropdownItemVariables)'></a>

## DropdownItem(DropdownItemVariables) Constructor

Construct a new instance.

```csharp
public DropdownItem(Tizen.UI.Components.Material.DropdownItemVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DropdownItem.DropdownItem(Tizen.UI.Components.Material.DropdownItemVariables).variables'></a>

`variables` [DropdownItemVariables](Tizen.UI.Components.Material.DropdownItemVariables.md 'Tizen.UI.Components.Material.DropdownItemVariables')
### Properties

<a name='Tizen.UI.Components.Material.DropdownItem.AutoFontSize'></a>

## DropdownItem.AutoFontSize Property

Gets or sets the auto font size.

```csharp
public Tizen.UI.AutoFontSize AutoFontSize { get; set; }
```

Implements [AutoFontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IFlexibleText.AutoFontSize 'Tizen.UI.Components.IFlexibleText.AutoFontSize')

#### Property Value
[Tizen.UI.AutoFontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AutoFontSize 'Tizen.UI.AutoFontSize')

<a name='Tizen.UI.Components.Material.DropdownItem.FontFamily'></a>

## DropdownItem.FontFamily Property

Gets or sets the font family of the text.

```csharp
public string FontFamily { get; set; }
```

Implements [FontFamily](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.FontFamily 'Tizen.UI.IText.FontFamily')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.DropdownItem.FontSize'></a>

## DropdownItem.FontSize Property

Gets or sets the font size of the text.

```csharp
public float FontSize { get; set; }
```

Implements [FontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.FontSize 'Tizen.UI.IText.FontSize'), [FontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IFlexibleText.FontSize 'Tizen.UI.Components.IFlexibleText.FontSize')

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.DropdownItem.IconMultipliedColor'></a>

## DropdownItem.IconMultipliedColor Property

Gets or sets the mix color of the icon.

```csharp
public Tizen.UI.Color IconMultipliedColor { get; set; }
```

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.Material.DropdownItem.IconPlacement'></a>

## DropdownItem.IconPlacement Property

Gets or sets the placement of the icon.

```csharp
public Tizen.UI.Components.IconPlacement IconPlacement { get; set; }
```

#### Property Value
[Tizen.UI.Components.IconPlacement](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IconPlacement 'Tizen.UI.Components.IconPlacement')

<a name='Tizen.UI.Components.Material.DropdownItem.IconResourceUrl'></a>

## DropdownItem.IconResourceUrl Property

Gets or sets the resource URL of the icon image.

```csharp
public string IconResourceUrl { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.DropdownItem.ItemSpacing'></a>

## DropdownItem.ItemSpacing Property

Gets or sets the spacing between icon and text.

```csharp
public float ItemSpacing { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.DropdownItem.Padding'></a>

## DropdownItem.Padding Property

Gets or sets the padding.

```csharp
public Tizen.UI.Thickness Padding { get; set; }
```

#### Property Value
[Tizen.UI.Thickness](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Thickness 'Tizen.UI.Thickness')

<a name='Tizen.UI.Components.Material.DropdownItem.SystemFontSizeScaleEnabled'></a>

## DropdownItem.SystemFontSizeScaleEnabled Property

Gets or sets whether the font size should be scaled based on the system settings.

```csharp
public bool SystemFontSizeScaleEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.DropdownItem.Text'></a>

## DropdownItem.Text Property

Gets or sets the text of the tab item.

```csharp
public string Text { get; set; }
```

Implements [Text](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.Text 'Tizen.UI.IText.Text')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.DropdownItem.TextColor'></a>

## DropdownItem.TextColor Property

Gets or sets the text color of the label.

```csharp
public Tizen.UI.Color TextColor { get; set; }
```

Implements [TextColor](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.TextColor 'Tizen.UI.IText.TextColor')

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.Material.DropdownItem.TextOverflow'></a>

## DropdownItem.TextOverflow Property

Gets or sets the text ellipsize mode to be applied when the text overflows.

```csharp
public Tizen.UI.TextOverflow TextOverflow { get; set; }
```

Implements [TextOverflow](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IFlexibleText.TextOverflow 'Tizen.UI.Components.IFlexibleText.TextOverflow')

#### Property Value
[Tizen.UI.TextOverflow](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.TextOverflow 'Tizen.UI.TextOverflow')
### Methods

<a name='Tizen.UI.Components.Material.DropdownItem.GetTouchEffectSecondaryTarget()'></a>

## DropdownItem.GetTouchEffectSecondaryTarget() Method

Get the secondary target view to apply feedback.

```csharp
public override Tizen.UI.View GetTouchEffectSecondaryTarget();
```

Implements [GetTouchEffectSecondaryTarget()](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.ITouchEffectTarget.GetTouchEffectSecondaryTarget 'Tizen.UI.Components.ITouchEffectTarget.GetTouchEffectSecondaryTarget')

#### Returns
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')













































