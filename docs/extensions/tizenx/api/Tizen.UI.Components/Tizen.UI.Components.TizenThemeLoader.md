### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## TizenThemeLoader Class

The default theme loader for Tizen. It is implemented using `Tizen.Applications.ThemeLoader`.

```csharp
public class TizenThemeLoader :
Tizen.UI.Components.IThemeLoader
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; TizenThemeLoader

Implements [IThemeLoader](Tizen.UI.Components.IThemeLoader.md 'Tizen.UI.Components.IThemeLoader')
### Constructors

<a name='Tizen.UI.Components.TizenThemeLoader.TizenThemeLoader()'></a>

## TizenThemeLoader() Constructor

Construct a new instance of the [TizenThemeLoader](Tizen.UI.Components.TizenThemeLoader.md 'Tizen.UI.Components.TizenThemeLoader').

```csharp
public TizenThemeLoader();
```
### Properties

<a name='Tizen.UI.Components.TizenThemeLoader.CurrentResourcePath'></a>

## TizenThemeLoader.CurrentResourcePath Property

Gets the current resource path.

```csharp
public string CurrentResourcePath { get; set; }
```

Implements [CurrentResourcePath](Tizen.UI.Components.IThemeLoader.md#Tizen.UI.Components.IThemeLoader.CurrentResourcePath 'Tizen.UI.Components.IThemeLoader.CurrentResourcePath')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.TizenThemeLoader.CurrentThemeId'></a>

## TizenThemeLoader.CurrentThemeId Property

Gets the current theme id.

```csharp
public string CurrentThemeId { get; set; }
```

Implements [CurrentThemeId](Tizen.UI.Components.IThemeLoader.md#Tizen.UI.Components.IThemeLoader.CurrentThemeId 'Tizen.UI.Components.IThemeLoader.CurrentThemeId')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')
### Methods

<a name='Tizen.UI.Components.TizenThemeLoader.LoadColorTable()'></a>

## TizenThemeLoader.LoadColorTable() Method

Load color table for current theme.

```csharp
public virtual System.Collections.Generic.IDictionary&lt;string,Tizen.UI.Color> LoadColorTable();
```

Implements [LoadColorTable()](Tizen.UI.Components.IThemeLoader.md#Tizen.UI.Components.IThemeLoader.LoadColorTable() 'Tizen.UI.Components.IThemeLoader.LoadColorTable()')

#### Returns
[System.Collections.Generic.IDictionary&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')
### Events

<a name='Tizen.UI.Components.TizenThemeLoader.ThemeChanged'></a>

## TizenThemeLoader.ThemeChanged Event

Occurs when the theme is changed.

```csharp
public event EventHandler ThemeChanged;
```

Implements [ThemeChanged](Tizen.UI.Components.IThemeLoader.md#Tizen.UI.Components.IThemeLoader.ThemeChanged 'Tizen.UI.Components.IThemeLoader.ThemeChanged')

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')


























































