### [Tizen.UI.Primitives2D](Tizen.UI.Primitives2D.md 'Tizen.UI.Primitives2D')

## LinearGradientPaint Class

Represents a linear gradient paint object.

```csharp
public class LinearGradientPaint : Tizen.UI.Primitives2D.GradientPaint
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; [GradientPaint](Tizen.UI.Primitives2D.GradientPaint.md 'Tizen.UI.Primitives2D.GradientPaint') &#129106; LinearGradientPaint
### Constructors

<a name='Tizen.UI.Primitives2D.LinearGradientPaint.LinearGradientPaint()'></a>

## LinearGradientPaint() Constructor

Initializes a new instance of the [LinearGradient](https://docs.microsoft.com/en-us/dotnet/api/LinearGradient 'LinearGradient') class.

```csharp
public LinearGradientPaint();
```

<a name='Tizen.UI.Primitives2D.LinearGradientPaint.LinearGradientPaint(float,float,float,float)'></a>

## LinearGradientPaint(float, float, float, float) Constructor

Initializes a new instance of the [LinearGradientPaint](Tizen.UI.Primitives2D.LinearGradientPaint.md 'Tizen.UI.Primitives2D.LinearGradientPaint') class with the specified start and end points.

```csharp
public LinearGradientPaint(float startPointX, float startPointY, float endPointX, float endPointY);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.LinearGradientPaint.LinearGradientPaint(float,float,float,float).startPointX'></a>

`startPointX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the start point.

<a name='Tizen.UI.Primitives2D.LinearGradientPaint.LinearGradientPaint(float,float,float,float).startPointY'></a>

`startPointY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the start point.

<a name='Tizen.UI.Primitives2D.LinearGradientPaint.LinearGradientPaint(float,float,float,float).endPointX'></a>

`endPointX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the end point.

<a name='Tizen.UI.Primitives2D.LinearGradientPaint.LinearGradientPaint(float,float,float,float).endPointY'></a>

`endPointY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the end point.
### Properties

<a name='Tizen.UI.Primitives2D.LinearGradientPaint.EndPoint'></a>

## LinearGradientPaint.EndPoint Property

Gets or sets the end point of the linear gradient.

```csharp
public Tizen.UI.Point EndPoint { get; set; }
```

#### Property Value
Tizen.UI.Point

<a name='Tizen.UI.Primitives2D.LinearGradientPaint.StartPoint'></a>

## LinearGradientPaint.StartPoint Property

Gets or sets the start point of the linear gradient.

```csharp
public Tizen.UI.Point StartPoint { get; set; }
```

#### Property Value
Tizen.UI.Point



















































