### [Tizen.UI.Primitives2D](Tizen.UI.Primitives2D.md 'Tizen.UI.Primitives2D')

## IPaint Interface

Interface for defining paint objects used to draw shapes on a canvas.

```csharp
public interface IPaint
```

Derived  
&#8627; [GradientPaint](Tizen.UI.Primitives2D.GradientPaint.md 'Tizen.UI.Primitives2D.GradientPaint')  
&#8627; [SolidPaint](Tizen.UI.Primitives2D.SolidPaint.md 'Tizen.UI.Primitives2D.SolidPaint')
### Properties

<a name='Tizen.UI.Primitives2D.IPaint.FillRule'></a>

## IPaint.FillRule Property

Gets or sets the [FillRule](Tizen.UI.Primitives2D.IPaint.md#Tizen.UI.Primitives2D.IPaint.FillRule 'Tizen.UI.Primitives2D.IPaint.FillRule') used to determine which points are inside or outside a shape.

```csharp
Tizen.UI.Primitives2D.FillRule FillRule { get; set; }
```

#### Property Value
[FillRule](Tizen.UI.Primitives2D.FillRule.md 'Tizen.UI.Primitives2D.FillRule')

<a name='Tizen.UI.Primitives2D.IPaint.StrokeCap'></a>

## IPaint.StrokeCap Property

Gets or sets the [StrokeCap](Tizen.UI.Primitives2D.IPaint.md#Tizen.UI.Primitives2D.IPaint.StrokeCap 'Tizen.UI.Primitives2D.IPaint.StrokeCap') style used when drawing lines.

```csharp
Tizen.UI.Primitives2D.StrokeCap StrokeCap { get; set; }
```

#### Property Value
[StrokeCap](Tizen.UI.Primitives2D.StrokeCap.md 'Tizen.UI.Primitives2D.StrokeCap')

<a name='Tizen.UI.Primitives2D.IPaint.StrokeDashArray'></a>

## IPaint.StrokeDashArray Property

Gets or sets the array of dash pattern lengths used to stroke paths.

```csharp
float[] StrokeDashArray { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[[]](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array')

<a name='Tizen.UI.Primitives2D.IPaint.StrokeJoin'></a>

## IPaint.StrokeJoin Property

Gets or sets the [StrokeJoin](Tizen.UI.Primitives2D.IPaint.md#Tizen.UI.Primitives2D.IPaint.StrokeJoin 'Tizen.UI.Primitives2D.IPaint.StrokeJoin') style used when joining lines.

```csharp
Tizen.UI.Primitives2D.StrokeJoin StrokeJoin { get; set; }
```

#### Property Value
[StrokeJoin](Tizen.UI.Primitives2D.StrokeJoin.md 'Tizen.UI.Primitives2D.StrokeJoin')

<a name='Tizen.UI.Primitives2D.IPaint.StrokeWidth'></a>

## IPaint.StrokeWidth Property

Gets or sets the width of the stroke used when drawing shapes.

```csharp
float StrokeWidth { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.Primitives2D.IPaint.Fill(Tizen.UI.Primitives2D.Shape)'></a>

## IPaint.Fill(Shape) Method

Fills the specified [Shape](Tizen.UI.Primitives2D.Shape.md 'Tizen.UI.Primitives2D.Shape') using the current paint settings.

```csharp
void Fill(Tizen.UI.Primitives2D.Shape shape);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.IPaint.Fill(Tizen.UI.Primitives2D.Shape).shape'></a>

`shape` [Shape](Tizen.UI.Primitives2D.Shape.md 'Tizen.UI.Primitives2D.Shape')

The shape to fill.

<a name='Tizen.UI.Primitives2D.IPaint.Stroke(Tizen.UI.Primitives2D.Shape)'></a>

## IPaint.Stroke(Shape) Method

Strokes the specified [Shape](Tizen.UI.Primitives2D.Shape.md 'Tizen.UI.Primitives2D.Shape') using the current paint settings.

```csharp
void Stroke(Tizen.UI.Primitives2D.Shape shape);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.IPaint.Stroke(Tizen.UI.Primitives2D.Shape).shape'></a>

`shape` [Shape](Tizen.UI.Primitives2D.Shape.md 'Tizen.UI.Primitives2D.Shape')

The shape to stroke.


















































