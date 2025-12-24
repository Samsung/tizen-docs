### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## FlexBox Class

FlexBox is a Layout that efficiently lays out it's children in a manner similar to that of CSS Flexbox.

```csharp
public class FlexBox : Tizen.UI.Layouts.Layout,
Tizen.UI.Layouts.IFlexBox,
Tizen.UI.Layouts.ILayout
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ViewGroup](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ViewGroup 'Tizen.UI.ViewGroup') &#129106; [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') &#129106; FlexBox

Implements [IFlexBox](Tizen.UI.Layouts.IFlexBox.md 'Tizen.UI.Layouts.IFlexBox'), [ILayout](Tizen.UI.Layouts.ILayout.md 'Tizen.UI.Layouts.ILayout')
### Constructors

<a name='Tizen.UI.Layouts.FlexBox.FlexBox()'></a>

## FlexBox() Constructor

Initializes a new instance of the [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') class.

```csharp
public FlexBox();
```
### Properties

<a name='Tizen.UI.Layouts.FlexBox.AlignContent'></a>

## FlexBox.AlignContent Property

Gets or sets a value that controls how multiple rows or columns of child elements are aligned.

```csharp
public Tizen.UI.Layouts.FlexAlignContent AlignContent { get; set; }
```

#### Property Value
[FlexAlignContent](Tizen.UI.Layouts.FlexAlignContent.md 'Tizen.UI.Layouts.FlexAlignContent')

<a name='Tizen.UI.Layouts.FlexBox.AlignItems'></a>

## FlexBox.AlignItems Property

Gets or sets a value that controls how child elements are laid out within their row or column.

```csharp
public Tizen.UI.Layouts.FlexAlignItems AlignItems { get; set; }
```

#### Property Value
[FlexAlignItems](Tizen.UI.Layouts.FlexAlignItems.md 'Tizen.UI.Layouts.FlexAlignItems')

<a name='Tizen.UI.Layouts.FlexBox.Direction'></a>

## FlexBox.Direction Property

Gets or sets the flex direction for child elements within this layout.

```csharp
public Tizen.UI.Layouts.FlexDirection Direction { get; set; }
```

#### Property Value
[FlexDirection](Tizen.UI.Layouts.FlexDirection.md 'Tizen.UI.Layouts.FlexDirection')

<a name='Tizen.UI.Layouts.FlexBox.JustifyContent'></a>

## FlexBox.JustifyContent Property

Gets or sets a value that that describes how child elements are justified when there is extra space around them.

```csharp
public Tizen.UI.Layouts.FlexJustify JustifyContent { get; set; }
```

#### Property Value
[FlexJustify](Tizen.UI.Layouts.FlexJustify.md 'Tizen.UI.Layouts.FlexJustify')

<a name='Tizen.UI.Layouts.FlexBox.Position'></a>

## FlexBox.Position Property

Gets or sets a value that controls whether the coordinates of child elements are specified in absolute or relative terms.

```csharp
public Tizen.UI.Layouts.FlexPosition Position { get; set; }
```

#### Property Value
[FlexPosition](Tizen.UI.Layouts.FlexPosition.md 'Tizen.UI.Layouts.FlexPosition')

<a name='Tizen.UI.Layouts.FlexBox.Wrap'></a>

## FlexBox.Wrap Property

Gets or sets a value that controls whether and how child elements within this layout wrap.

```csharp
public Tizen.UI.Layouts.FlexWrap Wrap { get; set; }
```

#### Property Value
[FlexWrap](Tizen.UI.Layouts.FlexWrap.md 'Tizen.UI.Layouts.FlexWrap')
### Methods

<a name='Tizen.UI.Layouts.FlexBox.Measure(float,float)'></a>

## FlexBox.Measure(float, float) Method

Measures the layout with the specified available width and height.

```csharp
public override Tizen.UI.Size Measure(float availableWidth, float availableHeight);
```
#### Parameters

<a name='Tizen.UI.Layouts.FlexBox.Measure(float,float).availableWidth'></a>

`availableWidth` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available width to measure the layout with.

<a name='Tizen.UI.Layouts.FlexBox.Measure(float,float).availableHeight'></a>

`availableHeight` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available height to measure the layout with.

#### Returns
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')  
The size of the layout after measuring.






























































