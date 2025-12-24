### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## Layout Class

Layout is an abstract class that defines the base functionality for all layout classes. It provides a mechanism for arranging and positioning child views within its bounds.

```csharp
public abstract class Layout : Tizen.UI.ViewGroup,
Tizen.UI.Layouts.ILayout
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ViewGroup &#129106; Layout

Derived  
&#8627; [AbsoluteLayout](Tizen.UI.Layouts.AbsoluteLayout.md 'Tizen.UI.Layouts.AbsoluteLayout')  
&#8627; [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox')  
&#8627; [Grid](Tizen.UI.Layouts.Grid.md 'Tizen.UI.Layouts.Grid')  
&#8627; [ScrollLayout](Tizen.UI.Layouts.ScrollLayout.md 'Tizen.UI.Layouts.ScrollLayout')  
&#8627; [StackBase](Tizen.UI.Layouts.StackBase.md 'Tizen.UI.Layouts.StackBase')

Implements [ILayout](Tizen.UI.Layouts.ILayout.md 'Tizen.UI.Layouts.ILayout')
### Constructors

<a name='Tizen.UI.Layouts.Layout.Layout()'></a>

## Layout() Constructor

Initializes a new instance of the [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') class.

```csharp
public Layout();
```
### Properties

<a name='Tizen.UI.Layouts.Layout.IsManualLayout'></a>

## Layout.IsManualLayout Property

Gets or sets a value indicating whether  the layout is manual layout or not.

```csharp
public static bool IsManualLayout { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Layouts.Layout.IsOnPseudoLayout'></a>

## Layout.IsOnPseudoLayout Property

Gets or sets a value indicating whether the layout is on pseudo layout.

```csharp
public bool IsOnPseudoLayout { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Layouts.Layout.Padding'></a>

## Layout.Padding Property

Gets or sets the padding of the layout.

```csharp
public Tizen.UI.Thickness Padding { get; set; }
```

Implements [Padding](Tizen.UI.Layouts.ILayout.md#Tizen.UI.Layouts.ILayout.Padding 'Tizen.UI.Layouts.ILayout.Padding')

#### Property Value
Tizen.UI.Thickness
### Methods

<a name='Tizen.UI.Layouts.Layout.Measure(float,float)'></a>

## Layout.Measure(float, float) Method

Measures the layout with the specified available width and height.

```csharp
public override Tizen.UI.Size Measure(float availableWidth, float availableHeight);
```
#### Parameters

<a name='Tizen.UI.Layouts.Layout.Measure(float,float).availableWidth'></a>

`availableWidth` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available width to measure the layout with.

<a name='Tizen.UI.Layouts.Layout.Measure(float,float).availableHeight'></a>

`availableHeight` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available height to measure the layout with.

#### Returns
Tizen.UI.Size  
The size of the layout after measuring.

<a name='Tizen.UI.Layouts.Layout.UpdateLayout()'></a>

## Layout.UpdateLayout() Method

Updates the layout.

```csharp
public void UpdateLayout();
```

<a name='Tizen.UI.Layouts.Layout.UpdateLayout(Tizen.UI.Rect)'></a>

## Layout.UpdateLayout(Rect) Method

Updates the layout with the specified bounds.

```csharp
public virtual Tizen.UI.Size UpdateLayout(Tizen.UI.Rect bounds);
```
#### Parameters

<a name='Tizen.UI.Layouts.Layout.UpdateLayout(Tizen.UI.Rect).bounds'></a>

`bounds` Tizen.UI.Rect

The bounds to update the layout with.

#### Returns
Tizen.UI.Size  
The size of the layout after updating.































































