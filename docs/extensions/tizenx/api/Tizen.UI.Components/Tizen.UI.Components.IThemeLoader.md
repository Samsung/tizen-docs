### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## IThemeLoader Interface

Interface for loading system theme.

```csharp
public interface IThemeLoader
```

Derived  
&#8627; [DummyThemeLoader](Tizen.UI.Components.DummyThemeLoader.md 'Tizen.UI.Components.DummyThemeLoader')  
&#8627; [TizenThemeLoader](Tizen.UI.Components.TizenThemeLoader.md 'Tizen.UI.Components.TizenThemeLoader')
### Properties

<a name='Tizen.UI.Components.IThemeLoader.CurrentResourcePath'></a>

## IThemeLoader.CurrentResourcePath Property

Gets the current resource path.

```csharp
string CurrentResourcePath { get; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.IThemeLoader.CurrentThemeId'></a>

## IThemeLoader.CurrentThemeId Property

Gets the current theme id.

```csharp
string CurrentThemeId { get; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')
### Methods

<a name='Tizen.UI.Components.IThemeLoader.LoadColorTable()'></a>

## IThemeLoader.LoadColorTable() Method

Load color table for current theme.

```csharp
System.Collections.Generic.IDictionary&lt;string,Tizen.UI.Color> LoadColorTable();
```

#### Returns
[System.Collections.Generic.IDictionary&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IDictionary-2 'System.Collections.Generic.IDictionary`2')
### Events

<a name='Tizen.UI.Components.IThemeLoader.ThemeChanged'></a>

## IThemeLoader.ThemeChanged Event

Occurs when the theme is changed.

```csharp
event EventHandler ThemeChanged;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')


























































