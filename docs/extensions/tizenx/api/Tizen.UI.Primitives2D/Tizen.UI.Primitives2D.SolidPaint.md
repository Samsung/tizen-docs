### [Tizen.UI.Primitives2D](Tizen.UI.Primitives2D.md 'Tizen.UI.Primitives2D')

## SolidPaint Class

Represents a solid paint object used for drawing shapes.

```csharp
public class SolidPaint :
Tizen.UI.Primitives2D.IPaint
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; SolidPaint

Implements [IPaint](Tizen.UI.Primitives2D.IPaint.md 'Tizen.UI.Primitives2D.IPaint')
### Constructors

<a name='Tizen.UI.Primitives2D.SolidPaint.SolidPaint()'></a>

## SolidPaint() Constructor

Initializes a new instance of the [SolidPaint](Tizen.UI.Primitives2D.SolidPaint.md 'Tizen.UI.Primitives2D.SolidPaint') class.

```csharp
public SolidPaint();
```

<a name='Tizen.UI.Primitives2D.SolidPaint.SolidPaint(Tizen.UI.Color)'></a>

## SolidPaint(Color) Constructor

Initializes a new instance of the [SolidPaint](Tizen.UI.Primitives2D.SolidPaint.md 'Tizen.UI.Primitives2D.SolidPaint') class with the specified color.

```csharp
public SolidPaint(Tizen.UI.Color color);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.SolidPaint.SolidPaint(Tizen.UI.Color).color'></a>

`color` Tizen.UI.Color

The color of the paint.
### Properties

<a name='Tizen.UI.Primitives2D.SolidPaint.Color'></a>

## SolidPaint.Color Property

Gets or sets the color of the paint.

```csharp
public Tizen.UI.Color Color { get; set; }
```

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Primitives2D.SolidPaint.FillRule'></a>

## SolidPaint.FillRule Property

Gets or sets the fill rule used to determine which points are inside or outside the shape.

```csharp
public Tizen.UI.Primitives2D.FillRule FillRule { get; set; }
```

Implements [FillRule](Tizen.UI.Primitives2D.IPaint.md#Tizen.UI.Primitives2D.IPaint.FillRule 'Tizen.UI.Primitives2D.IPaint.FillRule')

#### Property Value
[FillRule](Tizen.UI.Primitives2D.FillRule.md 'Tizen.UI.Primitives2D.FillRule')

<a name='Tizen.UI.Primitives2D.SolidPaint.StrokeCap'></a>

## SolidPaint.StrokeCap Property

Gets or sets the cap style of the stroke.

```csharp
public Tizen.UI.Primitives2D.StrokeCap StrokeCap { get; set; }
```

Implements [StrokeCap](Tizen.UI.Primitives2D.IPaint.md#Tizen.UI.Primitives2D.IPaint.StrokeCap 'Tizen.UI.Primitives2D.IPaint.StrokeCap')

#### Property Value
[StrokeCap](Tizen.UI.Primitives2D.StrokeCap.md 'Tizen.UI.Primitives2D.StrokeCap')

<a name='Tizen.UI.Primitives2D.SolidPaint.StrokeDashArray'></a>

## SolidPaint.StrokeDashArray Property

Gets or sets the dash array of the stroke.

```csharp
public float[] StrokeDashArray { get; set; }
```

Implements [StrokeDashArray](Tizen.UI.Primitives2D.IPaint.md#Tizen.UI.Primitives2D.IPaint.StrokeDashArray 'Tizen.UI.Primitives2D.IPaint.StrokeDashArray')

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[[]](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array')

<a name='Tizen.UI.Primitives2D.SolidPaint.StrokeJoin'></a>

## SolidPaint.StrokeJoin Property

Gets or sets the join style of the stroke.

```csharp
public Tizen.UI.Primitives2D.StrokeJoin StrokeJoin { get; set; }
```

Implements [StrokeJoin](Tizen.UI.Primitives2D.IPaint.md#Tizen.UI.Primitives2D.IPaint.StrokeJoin 'Tizen.UI.Primitives2D.IPaint.StrokeJoin')

#### Property Value
[StrokeJoin](Tizen.UI.Primitives2D.StrokeJoin.md 'Tizen.UI.Primitives2D.StrokeJoin')

<a name='Tizen.UI.Primitives2D.SolidPaint.StrokeWidth'></a>

## SolidPaint.StrokeWidth Property

Gets or sets the width of the stroke.

```csharp
public float StrokeWidth { get; set; }
```

Implements [StrokeWidth](Tizen.UI.Primitives2D.IPaint.md#Tizen.UI.Primitives2D.IPaint.StrokeWidth 'Tizen.UI.Primitives2D.IPaint.StrokeWidth')

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.Primitives2D.SolidPaint.Fill(Tizen.UI.Primitives2D.Shape)'></a>

## SolidPaint.Fill(Shape) Method

Fills the specified [Shape](Tizen.UI.Primitives2D.Shape.md 'Tizen.UI.Primitives2D.Shape') with the paint.

```csharp
public void Fill(Tizen.UI.Primitives2D.Shape shape);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.SolidPaint.Fill(Tizen.UI.Primitives2D.Shape).shape'></a>

`shape` [Shape](Tizen.UI.Primitives2D.Shape.md 'Tizen.UI.Primitives2D.Shape')

The shape to fill.

Implements [Fill(Shape)](Tizen.UI.Primitives2D.IPaint.md#Tizen.UI.Primitives2D.IPaint.Fill(Tizen.UI.Primitives2D.Shape) 'Tizen.UI.Primitives2D.IPaint.Fill(Tizen.UI.Primitives2D.Shape)')

<a name='Tizen.UI.Primitives2D.SolidPaint.Stroke(Tizen.UI.Primitives2D.Shape)'></a>

## SolidPaint.Stroke(Shape) Method

Strokes the specified [Shape](Tizen.UI.Primitives2D.Shape.md 'Tizen.UI.Primitives2D.Shape') with the paint.

```csharp
public void Stroke(Tizen.UI.Primitives2D.Shape shape);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.SolidPaint.Stroke(Tizen.UI.Primitives2D.Shape).shape'></a>

`shape` [Shape](Tizen.UI.Primitives2D.Shape.md 'Tizen.UI.Primitives2D.Shape')

The shape to stroke.

Implements [Stroke(Shape)](Tizen.UI.Primitives2D.IPaint.md#Tizen.UI.Primitives2D.IPaint.Stroke(Tizen.UI.Primitives2D.Shape) 'Tizen.UI.Primitives2D.IPaint.Stroke(Tizen.UI.Primitives2D.Shape)')


















































