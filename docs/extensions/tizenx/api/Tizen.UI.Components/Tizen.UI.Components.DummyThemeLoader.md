### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## DummyThemeLoader Class

Implements a dummy font scale loader.

```csharp
public class DummyThemeLoader :
Tizen.UI.Components.IThemeLoader
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; DummyThemeLoader

Implements [IThemeLoader](Tizen.UI.Components.IThemeLoader.md 'Tizen.UI.Components.IThemeLoader')
### Constructors

<a name='Tizen.UI.Components.DummyThemeLoader.DummyThemeLoader(string[])'></a>

## DummyThemeLoader(string[]) Constructor

Creates a new instance of DummyThemeLoader with the specified theme resource directories.

```csharp
public DummyThemeLoader(params string[] themeResourceDirectories);
```
#### Parameters

<a name='Tizen.UI.Components.DummyThemeLoader.DummyThemeLoader(string[]).themeResourceDirectories'></a>

`themeResourceDirectories` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[[]](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array')
### Properties

<a name='Tizen.UI.Components.DummyThemeLoader.CurrentResourcePath'></a>

## DummyThemeLoader.CurrentResourcePath Property

Gets the current resource path.

```csharp
public string CurrentResourcePath { get; set; }
```

Implements [CurrentResourcePath](Tizen.UI.Components.IThemeLoader.md#Tizen.UI.Components.IThemeLoader.CurrentResourcePath 'Tizen.UI.Components.IThemeLoader.CurrentResourcePath')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.DummyThemeLoader.CurrentThemeId'></a>

## DummyThemeLoader.CurrentThemeId Property

Gets the current theme id.

```csharp
public string CurrentThemeId { get; }
```

Implements [CurrentThemeId](Tizen.UI.Components.IThemeLoader.md#Tizen.UI.Components.IThemeLoader.CurrentThemeId 'Tizen.UI.Components.IThemeLoader.CurrentThemeId')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.DummyThemeLoader.Instance'></a>

## DummyThemeLoader.Instance Property

Gets a singleton instance of the DummyThemeLoader.

```csharp
public static Tizen.UI.Components.DummyThemeLoader Instance { get; }
```

#### Property Value
[DummyThemeLoader](Tizen.UI.Components.DummyThemeLoader.md 'Tizen.UI.Components.DummyThemeLoader')
### Methods

<a name='Tizen.UI.Components.DummyThemeLoader.LoadColorTable()'></a>

## DummyThemeLoader.LoadColorTable() Method

Load color table for current theme.

```csharp
public System.Collections.Generic.IDictionary&lt;string,Tizen.UI.Color> LoadColorTable();
```

Implements [LoadColorTable()](Tizen.UI.Components.IThemeLoader.md#Tizen.UI.Components.IThemeLoader.LoadColorTable() 'Tizen.UI.Components.IThemeLoader.LoadColorTable()')

#### Returns
[System.Collections.Generic.IDictionary&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')Tizen.UI.Color[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')

<a name='Tizen.UI.Components.DummyThemeLoader.NextTheme()'></a>

## DummyThemeLoader.NextTheme() Method

Change theme to next one.

```csharp
public void NextTheme();
```

<a name='Tizen.UI.Components.DummyThemeLoader.ResetTheme()'></a>

## DummyThemeLoader.ResetTheme() Method

Resets to the default theme.

```csharp
public void ResetTheme();
```

<a name='Tizen.UI.Components.DummyThemeLoader.SwitchTheme(int)'></a>

## DummyThemeLoader.SwitchTheme(int) Method

Change theme with specified index.

```csharp
public void SwitchTheme(int index);
```
#### Parameters

<a name='Tizen.UI.Components.DummyThemeLoader.SwitchTheme(int).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')
### Events

<a name='Tizen.UI.Components.DummyThemeLoader.ThemeChanged'></a>

## DummyThemeLoader.ThemeChanged Event

Occurs when the theme is changed.

```csharp
public event EventHandler ThemeChanged;
```

Implements [ThemeChanged](Tizen.UI.Components.IThemeLoader.md#Tizen.UI.Components.IThemeLoader.ThemeChanged 'Tizen.UI.Components.IThemeLoader.ThemeChanged')

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')


























































