### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## DoubleTitle Class

The title component with main title and subtitle. It can be used as a app bar title content.

```csharp
public class DoubleTitle : Tizen.UI.Layouts.VStack,
Tizen.UI.Components.IDoubleTitle,
Tizen.UI.Components.ITitle,
Tizen.UI.Components.Material.IAppBarContent
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ViewGroup](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ViewGroup 'Tizen.UI.ViewGroup') &#129106; [Tizen.UI.Layouts.Layout](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Layouts.Layout 'Tizen.UI.Layouts.Layout') &#129106; [Tizen.UI.Layouts.StackBase](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Layouts.StackBase 'Tizen.UI.Layouts.StackBase') &#129106; [Tizen.UI.Layouts.VStack](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Layouts.VStack 'Tizen.UI.Layouts.VStack') &#129106; DoubleTitle

Implements [Tizen.UI.Components.IDoubleTitle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IDoubleTitle 'Tizen.UI.Components.IDoubleTitle'), [Tizen.UI.Components.ITitle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.ITitle 'Tizen.UI.Components.ITitle'), [IAppBarContent](Tizen.UI.Components.Material.IAppBarContent.md 'Tizen.UI.Components.Material.IAppBarContent')
### Constructors

<a name='Tizen.UI.Components.Material.DoubleTitle.DoubleTitle(string,string)'></a>

## DoubleTitle(string, string) Constructor

Constructs a double title.

```csharp
public DoubleTitle(string title, string subtitle);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DoubleTitle.DoubleTitle(string,string).title'></a>

`title` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.DoubleTitle.DoubleTitle(string,string).subtitle'></a>

`subtitle` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.DoubleTitle.DoubleTitle(string,string,Tizen.UI.Components.Material.DoubleTitleVariables)'></a>

## DoubleTitle(string, string, DoubleTitleVariables) Constructor

Constructs a title.

```csharp
public DoubleTitle(string title, string subtitle, Tizen.UI.Components.Material.DoubleTitleVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DoubleTitle.DoubleTitle(string,string,Tizen.UI.Components.Material.DoubleTitleVariables).title'></a>

`title` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.DoubleTitle.DoubleTitle(string,string,Tizen.UI.Components.Material.DoubleTitleVariables).subtitle'></a>

`subtitle` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.DoubleTitle.DoubleTitle(string,string,Tizen.UI.Components.Material.DoubleTitleVariables).variables'></a>

`variables` [DoubleTitleVariables](Tizen.UI.Components.Material.DoubleTitleVariables.md 'Tizen.UI.Components.Material.DoubleTitleVariables')
### Properties

<a name='Tizen.UI.Components.Material.DoubleTitle.ItemSpacing'></a>

## DoubleTitle.ItemSpacing Property

Gets or sets padding double title item spacing.

```csharp
public float ItemSpacing { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.DoubleTitle.Subtitle'></a>

## DoubleTitle.Subtitle Property

Gets or sets the sub title.

```csharp
public string Subtitle { get; set; }
```

Implements [Subtitle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IDoubleTitle.Subtitle 'Tizen.UI.Components.IDoubleTitle.Subtitle')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.DoubleTitle.SubtitleLabel'></a>

## DoubleTitle.SubtitleLabel Property

Gets a reference to the subtitle label.

```csharp
public Tizen.UI.Components.Material.Label SubtitleLabel { get; }
```

#### Property Value
[Label](Tizen.UI.Components.Material.Label.md 'Tizen.UI.Components.Material.Label')

<a name='Tizen.UI.Components.Material.DoubleTitle.Title'></a>

## DoubleTitle.Title Property

Gets or sets the main title.

```csharp
public string Title { get; set; }
```

Implements [Title](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.ITitle.Title 'Tizen.UI.Components.ITitle.Title')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.DoubleTitle.TitleLabel'></a>

## DoubleTitle.TitleLabel Property

Gets a reference to the title label.

```csharp
public Tizen.UI.Components.Material.Label TitleLabel { get; }
```

#### Property Value
[Label](Tizen.UI.Components.Material.Label.md 'Tizen.UI.Components.Material.Label')
### Methods

<a name='Tizen.UI.Components.Material.DoubleTitle.ApplyUnifiedContentColor(Tizen.UI.Color)'></a>

## DoubleTitle.ApplyUnifiedContentColor(Color) Method

Apply app bar unified content color.

```csharp
public void ApplyUnifiedContentColor(Tizen.UI.Color color);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DoubleTitle.ApplyUnifiedContentColor(Tizen.UI.Color).color'></a>

`color` [Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

Implements [ApplyUnifiedContentColor(Color)](Tizen.UI.Components.Material.IAppBarContent.md#Tizen.UI.Components.Material.IAppBarContent.ApplyUnifiedContentColor(Tizen.UI.Color) 'Tizen.UI.Components.Material.IAppBarContent.ApplyUnifiedContentColor(Tizen.UI.Color)')













































