### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## ButtonVariables Class

Variables used for button.

```csharp
public class ButtonVariables : Tizen.UI.Components.Variables,
Tizen.UI.Components.IClickableVariables,
System.IEquatable&lt;Tizen.UI.Components.Material.ButtonVariables>
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.Components.Variables &#129106; ButtonVariables

Implements Tizen.UI.Components.IClickableVariables, [System.IEquatable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1 'System.IEquatable`1')[ButtonVariables](Tizen.UI.Components.Material.ButtonVariables.md 'Tizen.UI.Components.Material.ButtonVariables')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1 'System.IEquatable`1')
### Properties

<a name='Tizen.UI.Components.Material.ButtonVariables.BackgroundColor'></a>

## ButtonVariables.BackgroundColor Property

Button fill color.

```csharp
public Tizen.UI.Color BackgroundColor { get; set; }
```

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Components.Material.ButtonVariables.CornerRadius'></a>

## ButtonVariables.CornerRadius Property

Button corner radius.

```csharp
public Tizen.UI.CornerRadius CornerRadius { get; set; }
```

#### Property Value
Tizen.UI.CornerRadius

<a name='Tizen.UI.Components.Material.ButtonVariables.Default'></a>

## ButtonVariables.Default Property

Default button variables.

```csharp
public static Tizen.UI.Components.Material.ButtonVariables Default { get; }
```

#### Property Value
[ButtonVariables](Tizen.UI.Components.Material.ButtonVariables.md 'Tizen.UI.Components.Material.ButtonVariables')

<a name='Tizen.UI.Components.Material.ButtonVariables.Flat'></a>

## ButtonVariables.Flat Property

Flat button variables. (No background)

```csharp
public static Tizen.UI.Components.Material.ButtonVariables Flat { get; }
```

#### Property Value
[ButtonVariables](Tizen.UI.Components.Material.ButtonVariables.md 'Tizen.UI.Components.Material.ButtonVariables')

<a name='Tizen.UI.Components.Material.ButtonVariables.FontFamily'></a>

## ButtonVariables.FontFamily Property

Button text font family.

```csharp
public string FontFamily { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.ButtonVariables.FontSize'></a>

## ButtonVariables.FontSize Property

Button text font size.

```csharp
public float FontSize { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.ButtonVariables.Padding'></a>

## ButtonVariables.Padding Property

Button padding. (start, end, top, bottom).

```csharp
public Tizen.UI.Thickness Padding { get; set; }
```

#### Property Value
Tizen.UI.Thickness

<a name='Tizen.UI.Components.Material.ButtonVariables.ProgressIconHeight'></a>

## ButtonVariables.ProgressIconHeight Property

Button progress icon height.

```csharp
public float ProgressIconHeight { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.ButtonVariables.ProgressIconResourceUrl'></a>

## ButtonVariables.ProgressIconResourceUrl Property

Button progress icon image.

```csharp
public string ProgressIconResourceUrl { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.ButtonVariables.ProgressIconWidth'></a>

## ButtonVariables.ProgressIconWidth Property

Button progress icon width.

```csharp
public float ProgressIconWidth { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.ButtonVariables.TextColor'></a>

## ButtonVariables.TextColor Property

Button text color.

```csharp
public Tizen.UI.Color TextColor { get; set; }
```

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Components.Material.ButtonVariables.TextUnderline'></a>

## ButtonVariables.TextUnderline Property

Button text underline.

```csharp
public System.Nullable&lt;Tizen.UI.Underline> TextUnderline { get; set; }
```

#### Property Value
[System.Nullable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')Tizen.UI.Underline[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')

<a name='Tizen.UI.Components.Material.ButtonVariables.TouchEdgeInsets'></a>

## ButtonVariables.TouchEdgeInsets Property

Gets or sets the expanded touch area offset.

```csharp
public Tizen.UI.Thickness TouchEdgeInsets { get; set; }
```

#### Property Value
Tizen.UI.Thickness

### Remarks
For example, the `Thickness(-5, -20, 10, 15)` will expend touch area to left 5, top 20, right 10, bottom 15. (total 15 horizontally, 35 vertically)

<a name='Tizen.UI.Components.Material.ButtonVariables.TouchEffect'></a>

## ButtonVariables.TouchEffect Property

The visual effect on touch.

```csharp
public Tizen.UI.Components.UIAttachable TouchEffect { get; set; }
```

Implements TouchEffect

#### Property Value
Tizen.UI.Components.UIAttachable














































