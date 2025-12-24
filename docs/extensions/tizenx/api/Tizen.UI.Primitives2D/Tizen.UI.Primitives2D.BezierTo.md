### [Tizen.UI.Primitives2D](Tizen.UI.Primitives2D.md 'Tizen.UI.Primitives2D')

## BezierTo Class

Represents a command that draws a cubic Bezier curve to the current point.

```csharp
public class BezierTo :
Tizen.UI.Primitives2D.IPath
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; BezierTo

Implements [IPath](Tizen.UI.Primitives2D.IPath.md 'Tizen.UI.Primitives2D.IPath')
### Constructors

<a name='Tizen.UI.Primitives2D.BezierTo.BezierTo(float,float,float,float,float,float)'></a>

## BezierTo(float, float, float, float, float, float) Constructor

Draws a Bezier curve to the specified point.

```csharp
public BezierTo(float endPointX, float endPointY, float controlPoint1X, float controlPoint1Y, float controlPoint2X, float controlPoint2Y);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.BezierTo.BezierTo(float,float,float,float,float,float).endPointX'></a>

`endPointX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the end point.

<a name='Tizen.UI.Primitives2D.BezierTo.BezierTo(float,float,float,float,float,float).endPointY'></a>

`endPointY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the end point.

<a name='Tizen.UI.Primitives2D.BezierTo.BezierTo(float,float,float,float,float,float).controlPoint1X'></a>

`controlPoint1X` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the first control point.

<a name='Tizen.UI.Primitives2D.BezierTo.BezierTo(float,float,float,float,float,float).controlPoint1Y'></a>

`controlPoint1Y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the first control point.

<a name='Tizen.UI.Primitives2D.BezierTo.BezierTo(float,float,float,float,float,float).controlPoint2X'></a>

`controlPoint2X` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the second control point.

<a name='Tizen.UI.Primitives2D.BezierTo.BezierTo(float,float,float,float,float,float).controlPoint2Y'></a>

`controlPoint2Y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the second control point.
### Properties

<a name='Tizen.UI.Primitives2D.BezierTo.ControlPoint1X'></a>

## BezierTo.ControlPoint1X Property

Gets the x-coordinate of the first control point.

```csharp
public float ControlPoint1X { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Primitives2D.BezierTo.ControlPoint1Y'></a>

## BezierTo.ControlPoint1Y Property

Gets the y-coordinate of the first control point.

```csharp
public float ControlPoint1Y { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Primitives2D.BezierTo.ControlPoint2X'></a>

## BezierTo.ControlPoint2X Property

Gets the x-coordinate of the second control point.

```csharp
public float ControlPoint2X { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Primitives2D.BezierTo.ControlPoint2Y'></a>

## BezierTo.ControlPoint2Y Property

Gets the y-coordinate of the second control point.

```csharp
public float ControlPoint2Y { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Primitives2D.BezierTo.EndPointX'></a>

## BezierTo.EndPointX Property

Gets the x-coordinate of the end point.

```csharp
public float EndPointX { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Primitives2D.BezierTo.EndPointY'></a>

## BezierTo.EndPointY Property

Gets the y-coordinate of the end point.

```csharp
public float EndPointY { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')


















































