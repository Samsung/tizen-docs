### [Tizen.UI.Primitives2D](Tizen.UI.Primitives2D.md 'Tizen.UI.Primitives2D')

## GradientPaint Class

Abstract class representing a gradient paint.

```csharp
public abstract class GradientPaint : Tizen.UI.NObject,
Tizen.UI.Primitives2D.IPaint
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; GradientPaint

Derived  
&#8627; [LinearGradientPaint](Tizen.UI.Primitives2D.LinearGradientPaint.md 'Tizen.UI.Primitives2D.LinearGradientPaint')  
&#8627; [RadialGradientPaint](Tizen.UI.Primitives2D.RadialGradientPaint.md 'Tizen.UI.Primitives2D.RadialGradientPaint')

Implements [IPaint](Tizen.UI.Primitives2D.IPaint.md 'Tizen.UI.Primitives2D.IPaint')
### Properties

<a name='Tizen.UI.Primitives2D.GradientPaint.FillRule'></a>

## GradientPaint.FillRule Property

Gets or sets the fill rule of the gradient paint.

```csharp
public Tizen.UI.Primitives2D.FillRule FillRule { get; set; }
```

Implements [FillRule](Tizen.UI.Primitives2D.IPaint.md#Tizen.UI.Primitives2D.IPaint.FillRule 'Tizen.UI.Primitives2D.IPaint.FillRule')

#### Property Value
[FillRule](Tizen.UI.Primitives2D.FillRule.md 'Tizen.UI.Primitives2D.FillRule')

<a name='Tizen.UI.Primitives2D.GradientPaint.GradientStops'></a>

## GradientPaint.GradientStops Property

Gets or sets the gradient stops of the gradient paint.

```csharp
public Tizen.UI.GradientStop[] GradientStops { get; set; }
```

#### Property Value
Tizen.UI.GradientStop[[]](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array')

<a name='Tizen.UI.Primitives2D.GradientPaint.Spread'></a>

## GradientPaint.Spread Property

Gets or sets the spread type of the gradient paint.

```csharp
public Tizen.UI.Primitives2D.SpreadType Spread { get; set; }
```

#### Property Value
[SpreadType](Tizen.UI.Primitives2D.SpreadType.md 'Tizen.UI.Primitives2D.SpreadType')

<a name='Tizen.UI.Primitives2D.GradientPaint.StrokeCap'></a>

## GradientPaint.StrokeCap Property

Gets or sets the stroke cap of the gradient paint.

```csharp
public Tizen.UI.Primitives2D.StrokeCap StrokeCap { get; set; }
```

Implements [StrokeCap](Tizen.UI.Primitives2D.IPaint.md#Tizen.UI.Primitives2D.IPaint.StrokeCap 'Tizen.UI.Primitives2D.IPaint.StrokeCap')

#### Property Value
[StrokeCap](Tizen.UI.Primitives2D.StrokeCap.md 'Tizen.UI.Primitives2D.StrokeCap')

<a name='Tizen.UI.Primitives2D.GradientPaint.StrokeDashArray'></a>

## GradientPaint.StrokeDashArray Property

Gets or sets the stroke dash array of the gradient paint.

```csharp
public float[] StrokeDashArray { get; set; }
```

Implements [StrokeDashArray](Tizen.UI.Primitives2D.IPaint.md#Tizen.UI.Primitives2D.IPaint.StrokeDashArray 'Tizen.UI.Primitives2D.IPaint.StrokeDashArray')

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[[]](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array')

<a name='Tizen.UI.Primitives2D.GradientPaint.StrokeJoin'></a>

## GradientPaint.StrokeJoin Property

Gets or sets the stroke join of the gradient paint.

```csharp
public Tizen.UI.Primitives2D.StrokeJoin StrokeJoin { get; set; }
```

Implements [StrokeJoin](Tizen.UI.Primitives2D.IPaint.md#Tizen.UI.Primitives2D.IPaint.StrokeJoin 'Tizen.UI.Primitives2D.IPaint.StrokeJoin')

#### Property Value
[StrokeJoin](Tizen.UI.Primitives2D.StrokeJoin.md 'Tizen.UI.Primitives2D.StrokeJoin')

<a name='Tizen.UI.Primitives2D.GradientPaint.StrokeWidth'></a>

## GradientPaint.StrokeWidth Property

Gets or sets the stroke width of the gradient paint.

```csharp
public float StrokeWidth { get; set; }
```

Implements [StrokeWidth](Tizen.UI.Primitives2D.IPaint.md#Tizen.UI.Primitives2D.IPaint.StrokeWidth 'Tizen.UI.Primitives2D.IPaint.StrokeWidth')

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.Primitives2D.GradientPaint.Fill(Tizen.UI.Primitives2D.Shape)'></a>

## GradientPaint.Fill(Shape) Method

Fills the specified [Shape](Tizen.UI.Primitives2D.Shape.md 'Tizen.UI.Primitives2D.Shape') with the gradient paint.

```csharp
public void Fill(Tizen.UI.Primitives2D.Shape shape);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.GradientPaint.Fill(Tizen.UI.Primitives2D.Shape).shape'></a>

`shape` [Shape](Tizen.UI.Primitives2D.Shape.md 'Tizen.UI.Primitives2D.Shape')

The shape to fill.

Implements [Fill(Shape)](Tizen.UI.Primitives2D.IPaint.md#Tizen.UI.Primitives2D.IPaint.Fill(Tizen.UI.Primitives2D.Shape) 'Tizen.UI.Primitives2D.IPaint.Fill(Tizen.UI.Primitives2D.Shape)')

<a name='Tizen.UI.Primitives2D.GradientPaint.Stroke(Tizen.UI.Primitives2D.Shape)'></a>

## GradientPaint.Stroke(Shape) Method

Strokes the specified [Shape](Tizen.UI.Primitives2D.Shape.md 'Tizen.UI.Primitives2D.Shape') with the gradient paint.

```csharp
public void Stroke(Tizen.UI.Primitives2D.Shape shape);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.GradientPaint.Stroke(Tizen.UI.Primitives2D.Shape).shape'></a>

`shape` [Shape](Tizen.UI.Primitives2D.Shape.md 'Tizen.UI.Primitives2D.Shape')

The shape to stroke.

Implements [Stroke(Shape)](Tizen.UI.Primitives2D.IPaint.md#Tizen.UI.Primitives2D.IPaint.Stroke(Tizen.UI.Primitives2D.Shape) 'Tizen.UI.Primitives2D.IPaint.Stroke(Tizen.UI.Primitives2D.Shape)')



















































