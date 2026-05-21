### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## DropdownItem Class

DropdownListItem is a component that can be selected among the Tizen.UI.Components.SelectionGroup.

```csharp
public class DropdownItem : Tizen.UI.Components.GroupSelectable,
Tizen.UI.Components.IFlexibleText,
Tizen.UI.IText
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ContentView &#129106; Tizen.UI.Components.Pressable &#129106; Tizen.UI.Components.Clickable &#129106; Tizen.UI.Components.Selectable &#129106; Tizen.UI.Components.GroupSelectable &#129106; DropdownItem

Derived  
&#8627; [DropdownActionItem](Tizen.UI.Components.Material.DropdownActionItem.md 'Tizen.UI.Components.Material.DropdownActionItem')  
&#8627; [DropdownCheckItem](Tizen.UI.Components.Material.DropdownCheckItem.md 'Tizen.UI.Components.Material.DropdownCheckItem')

Implements Tizen.UI.Components.IFlexibleText, Tizen.UI.IText
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

Implements AutoFontSize

#### Property Value
Tizen.UI.AutoFontSize

<a name='Tizen.UI.Components.Material.DropdownItem.FontFamily'></a>

## DropdownItem.FontFamily Property

Gets or sets the font family of the text.

```csharp
public string FontFamily { get; set; }
```

Implements FontFamily

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.DropdownItem.FontSize'></a>

## DropdownItem.FontSize Property

Gets or sets the font size of the text.

```csharp
public float FontSize { get; set; }
```

Implements FontSize, FontSize

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.DropdownItem.IconMultipliedColor'></a>

## DropdownItem.IconMultipliedColor Property

Gets or sets the mix color of the icon.

```csharp
public Tizen.UI.Color IconMultipliedColor { get; set; }
```

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Components.Material.DropdownItem.IconPlacement'></a>

## DropdownItem.IconPlacement Property

Gets or sets the placement of the icon.

```csharp
public Tizen.UI.Components.IconPlacement IconPlacement { get; set; }
```

#### Property Value
Tizen.UI.Components.IconPlacement

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
Tizen.UI.Thickness

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

Implements Text

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.DropdownItem.TextColor'></a>

## DropdownItem.TextColor Property

Gets or sets the text color of the label.

```csharp
public Tizen.UI.Color TextColor { get; set; }
```

Implements TextColor

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Components.Material.DropdownItem.TextOverflow'></a>

## DropdownItem.TextOverflow Property

Gets or sets the text ellipsize mode to be applied when the text overflows.

```csharp
public Tizen.UI.TextOverflow TextOverflow { get; set; }
```

Implements TextOverflow

#### Property Value
Tizen.UI.TextOverflow
### Methods

<a name='Tizen.UI.Components.Material.DropdownItem.GetTouchEffectSecondaryTarget()'></a>

## DropdownItem.GetTouchEffectSecondaryTarget() Method

Get the secondary target view to apply feedback.

```csharp
public override Tizen.UI.View GetTouchEffectSecondaryTarget();
```

Implements GetTouchEffectSecondaryTarget()

#### Returns
Tizen.UI.View














































