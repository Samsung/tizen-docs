### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## TabItem Class

TabItem is a component that can be selected among the Tizen.UI.Components.SelectionGroup.

```csharp
public class TabItem : Tizen.UI.Components.GroupSelectable,
Tizen.UI.Components.IFlexibleText,
Tizen.UI.IText
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ContentView &#129106; Tizen.UI.Components.Pressable &#129106; Tizen.UI.Components.Clickable &#129106; Tizen.UI.Components.Selectable &#129106; Tizen.UI.Components.GroupSelectable &#129106; TabItem

Implements Tizen.UI.Components.IFlexibleText, Tizen.UI.IText
### Constructors

<a name='Tizen.UI.Components.Material.TabItem.TabItem()'></a>

## TabItem() Constructor

Constructs an empty button.

```csharp
public TabItem();
```

<a name='Tizen.UI.Components.Material.TabItem.TabItem(string)'></a>

## TabItem(string) Constructor

Constructs a tab item with specified text.

```csharp
public TabItem(string text);
```
#### Parameters

<a name='Tizen.UI.Components.Material.TabItem.TabItem(string).text'></a>

`text` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The text to display on the tab item.

<a name='Tizen.UI.Components.Material.TabItem.TabItem(string,Tizen.UI.Components.Material.TabItemVariables)'></a>

## TabItem(string, TabItemVariables) Constructor

Constructs a tab item with specified text and variables.

```csharp
public TabItem(string text, Tizen.UI.Components.Material.TabItemVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.TabItem.TabItem(string,Tizen.UI.Components.Material.TabItemVariables).text'></a>

`text` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The text to display on the tab item.

<a name='Tizen.UI.Components.Material.TabItem.TabItem(string,Tizen.UI.Components.Material.TabItemVariables).variables'></a>

`variables` [TabItemVariables](Tizen.UI.Components.Material.TabItemVariables.md 'Tizen.UI.Components.Material.TabItemVariables')

Custom variables for the tab item.

<a name='Tizen.UI.Components.Material.TabItem.TabItem(Tizen.UI.Components.Material.TabItemVariables)'></a>

## TabItem(TabItemVariables) Constructor

Constructs an empty tab item with specified variables.

```csharp
public TabItem(Tizen.UI.Components.Material.TabItemVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.TabItem.TabItem(Tizen.UI.Components.Material.TabItemVariables).variables'></a>

`variables` [TabItemVariables](Tizen.UI.Components.Material.TabItemVariables.md 'Tizen.UI.Components.Material.TabItemVariables')

Custom variables for the tab item.
### Properties

<a name='Tizen.UI.Components.Material.TabItem.AutoFontSize'></a>

## TabItem.AutoFontSize Property

Gets or sets the auto font size.

```csharp
public Tizen.UI.AutoFontSize AutoFontSize { get; set; }
```

Implements AutoFontSize

#### Property Value
Tizen.UI.AutoFontSize

<a name='Tizen.UI.Components.Material.TabItem.FontFamily'></a>

## TabItem.FontFamily Property

Gets or sets the font family of the text.

```csharp
public string FontFamily { get; set; }
```

Implements FontFamily

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.TabItem.FontSize'></a>

## TabItem.FontSize Property

Gets or sets the font size of the text.

```csharp
public float FontSize { get; set; }
```

Implements FontSize, FontSize

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.TabItem.IconMultipliedColor'></a>

## TabItem.IconMultipliedColor Property

Gets or sets the mix color of the icon image.

```csharp
public Tizen.UI.Color IconMultipliedColor { get; set; }
```

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Components.Material.TabItem.IconResourceUrl'></a>

## TabItem.IconResourceUrl Property

Gets or sets the resource URL of the icon image.

```csharp
public string IconResourceUrl { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.TabItem.ItemSpacing'></a>

## TabItem.ItemSpacing Property

Gets or sets the spacing between icon and text.

```csharp
public float ItemSpacing { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.TabItem.SystemFontSizeScaleEnabled'></a>

## TabItem.SystemFontSizeScaleEnabled Property

Gets or sets whether the font size should be scaled based on the system settings.

```csharp
public bool SystemFontSizeScaleEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.TabItem.Text'></a>

## TabItem.Text Property

Gets or sets the text of the tab item.

```csharp
public string Text { get; set; }
```

Implements Text

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.TabItem.TextColor'></a>

## TabItem.TextColor Property

Gets or sets the text color of the label.

```csharp
public Tizen.UI.Color TextColor { get; set; }
```

Implements TextColor

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Components.Material.TabItem.TextOverflow'></a>

## TabItem.TextOverflow Property

Gets or sets the text ellipsize mode to be applied when the text overflows.

```csharp
public Tizen.UI.TextOverflow TextOverflow { get; set; }
```

Implements TextOverflow

#### Property Value
Tizen.UI.TextOverflow
### Methods

<a name='Tizen.UI.Components.Material.TabItem.GetTouchEffectSecondaryTarget()'></a>

## TabItem.GetTouchEffectSecondaryTarget() Method

Get the secondary target view to apply feedback.

```csharp
public override Tizen.UI.View GetTouchEffectSecondaryTarget();
```

Implements GetTouchEffectSecondaryTarget()

#### Returns
Tizen.UI.View














































