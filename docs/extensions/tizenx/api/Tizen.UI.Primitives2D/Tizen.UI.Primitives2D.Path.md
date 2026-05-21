### [Tizen.UI.Primitives2D](Tizen.UI.Primitives2D.md 'Tizen.UI.Primitives2D')

## Path Class

Provides a set of static methods for creating [IPath](Tizen.UI.Primitives2D.IPath.md 'Tizen.UI.Primitives2D.IPath') objects.

```csharp
public static class Path
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Path
### Methods

<a name='Tizen.UI.Primitives2D.Path.ArcTo(float,float,float,float,float,bool)'></a>

## Path.ArcTo(float, float, float, float, float, bool) Method

Appends the specified arc to the path.

```csharp
public static Tizen.UI.Primitives2D.IPath ArcTo(float x, float y, float radius, float startAngle, float sweep, bool closed);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.Path.ArcTo(float,float,float,float,float,bool).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the end point of the arc.

<a name='Tizen.UI.Primitives2D.Path.ArcTo(float,float,float,float,float,bool).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the end point of the arc.

<a name='Tizen.UI.Primitives2D.Path.ArcTo(float,float,float,float,float,bool).radius'></a>

`radius` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The radius of the arc.

<a name='Tizen.UI.Primitives2D.Path.ArcTo(float,float,float,float,float,bool).startAngle'></a>

`startAngle` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The starting angle of the arc, in radians.

<a name='Tizen.UI.Primitives2D.Path.ArcTo(float,float,float,float,float,bool).sweep'></a>

`sweep` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The angle of the arc, in radians.

<a name='Tizen.UI.Primitives2D.Path.ArcTo(float,float,float,float,float,bool).closed'></a>

`closed` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

A value indicating whether the arc should be connected to the start point by a straight line.

#### Returns
[IPath](Tizen.UI.Primitives2D.IPath.md 'Tizen.UI.Primitives2D.IPath')  
An [MovArcToeTo](https://docs.microsoft.com/en-us/dotnet/api/MovArcToeTo 'MovArcToeTo') object.

<a name='Tizen.UI.Primitives2D.Path.BezierTo(float,float,float,float,float,float)'></a>

## Path.BezierTo(float, float, float, float, float, float) Method

Draws a Bezier curve to the specified point.

```csharp
public static Tizen.UI.Primitives2D.IPath BezierTo(float endPointX, float endPointY, float controlPoint1X, float controlPoint1Y, float controlPoint2X, float controlPoint2Y);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.Path.BezierTo(float,float,float,float,float,float).endPointX'></a>

`endPointX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the end point.

<a name='Tizen.UI.Primitives2D.Path.BezierTo(float,float,float,float,float,float).endPointY'></a>

`endPointY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the end point.

<a name='Tizen.UI.Primitives2D.Path.BezierTo(float,float,float,float,float,float).controlPoint1X'></a>

`controlPoint1X` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the first control point.

<a name='Tizen.UI.Primitives2D.Path.BezierTo(float,float,float,float,float,float).controlPoint1Y'></a>

`controlPoint1Y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the first control point.

<a name='Tizen.UI.Primitives2D.Path.BezierTo(float,float,float,float,float,float).controlPoint2X'></a>

`controlPoint2X` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the second control point.

<a name='Tizen.UI.Primitives2D.Path.BezierTo(float,float,float,float,float,float).controlPoint2Y'></a>

`controlPoint2Y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the second control point.

#### Returns
[IPath](Tizen.UI.Primitives2D.IPath.md 'Tizen.UI.Primitives2D.IPath')  
A [BezierTo(float, float, float, float, float, float)](Tizen.UI.Primitives2D.Path.md#Tizen.UI.Primitives2D.Path.BezierTo(float,float,float,float,float,float) 'Tizen.UI.Primitives2D.Path.BezierTo(float, float, float, float, float, float)') object.

<a name='Tizen.UI.Primitives2D.Path.Close()'></a>

## Path.Close() Method

Closes this context and flushes its content so that it can be rendered.

```csharp
public static Tizen.UI.Primitives2D.IPath Close();
```

#### Returns
[IPath](Tizen.UI.Primitives2D.IPath.md 'Tizen.UI.Primitives2D.IPath')  
A [Close()](Tizen.UI.Primitives2D.Path.md#Tizen.UI.Primitives2D.Path.Close() 'Tizen.UI.Primitives2D.Path.Close()') object.

<a name='Tizen.UI.Primitives2D.Path.DrawCircle(float,float,float)'></a>

## Path.DrawCircle(float, float, float) Method

Draws a circle on the canvas.

```csharp
public static Tizen.UI.Primitives2D.IPath DrawCircle(float centerX, float centerY, float radius);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.Path.DrawCircle(float,float,float).centerX'></a>

`centerX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Primitives2D.Path.DrawCircle(float,float,float).centerY'></a>

`centerY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Primitives2D.Path.DrawCircle(float,float,float).radius'></a>

`radius` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

#### Returns
[IPath](Tizen.UI.Primitives2D.IPath.md 'Tizen.UI.Primitives2D.IPath')  
A [DrawCircle(float, float, float)](Tizen.UI.Primitives2D.Path.md#Tizen.UI.Primitives2D.Path.DrawCircle(float,float,float) 'Tizen.UI.Primitives2D.Path.DrawCircle(float, float, float)') object.

<a name='Tizen.UI.Primitives2D.Path.DrawOval(float,float,float,float)'></a>

## Path.DrawOval(float, float, float, float) Method

Draws an oval on the canvas.

```csharp
public static Tizen.UI.Primitives2D.IPath DrawOval(float centerX, float centerY, float radiusX, float radiusY);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.Path.DrawOval(float,float,float,float).centerX'></a>

`centerX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the center of the oval.

<a name='Tizen.UI.Primitives2D.Path.DrawOval(float,float,float,float).centerY'></a>

`centerY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the center of the oval.

<a name='Tizen.UI.Primitives2D.Path.DrawOval(float,float,float,float).radiusX'></a>

`radiusX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-radius of the oval.

<a name='Tizen.UI.Primitives2D.Path.DrawOval(float,float,float,float).radiusY'></a>

`radiusY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-radius of the oval.

#### Returns
[IPath](Tizen.UI.Primitives2D.IPath.md 'Tizen.UI.Primitives2D.IPath')  
A [DrawOval(float, float, float, float)](Tizen.UI.Primitives2D.Path.md#Tizen.UI.Primitives2D.Path.DrawOval(float,float,float,float) 'Tizen.UI.Primitives2D.Path.DrawOval(float, float, float, float)') object.

<a name='Tizen.UI.Primitives2D.Path.DrawRoundRect(float,float,float,float,float,float)'></a>

## Path.DrawRoundRect(float, float, float, float, float, float) Method

Draws a rounded rectangle.

```csharp
public static Tizen.UI.Primitives2D.IPath DrawRoundRect(float x, float y, float width, float height, float radiusX, float radiusY);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.Path.DrawRoundRect(float,float,float,float,float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the upper-left corner of the rectangle.

<a name='Tizen.UI.Primitives2D.Path.DrawRoundRect(float,float,float,float,float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the upper-left corner of the rectangle.

<a name='Tizen.UI.Primitives2D.Path.DrawRoundRect(float,float,float,float,float,float).width'></a>

`width` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width of the rectangle.

<a name='Tizen.UI.Primitives2D.Path.DrawRoundRect(float,float,float,float,float,float).height'></a>

`height` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The height of the rectangle.

<a name='Tizen.UI.Primitives2D.Path.DrawRoundRect(float,float,float,float,float,float).radiusX'></a>

`radiusX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-radius of the rounded corners.

<a name='Tizen.UI.Primitives2D.Path.DrawRoundRect(float,float,float,float,float,float).radiusY'></a>

`radiusY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-radius of the rounded corners.

#### Returns
[IPath](Tizen.UI.Primitives2D.IPath.md 'Tizen.UI.Primitives2D.IPath')  
A [DrawRoundRect(float, float, float, float, float, float)](Tizen.UI.Primitives2D.Path.md#Tizen.UI.Primitives2D.Path.DrawRoundRect(float,float,float,float,float,float) 'Tizen.UI.Primitives2D.Path.DrawRoundRect(float, float, float, float, float, float)') object.

<a name='Tizen.UI.Primitives2D.Path.LineTo(float,float)'></a>

## Path.LineTo(float, float) Method

Add a line from the last point to the specified point.

```csharp
public static Tizen.UI.Primitives2D.IPath LineTo(float x, float y);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.Path.LineTo(float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the end of a line.

<a name='Tizen.UI.Primitives2D.Path.LineTo(float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the end of a line.

#### Returns
[IPath](Tizen.UI.Primitives2D.IPath.md 'Tizen.UI.Primitives2D.IPath')  
A [LineTo(float, float)](Tizen.UI.Primitives2D.Path.md#Tizen.UI.Primitives2D.Path.LineTo(float,float) 'Tizen.UI.Primitives2D.Path.LineTo(float, float)') object.

<a name='Tizen.UI.Primitives2D.Path.MoveTo(float,float)'></a>

## Path.MoveTo(float, float) Method

Set the beginning of the next contour to the point.

```csharp
public static Tizen.UI.Primitives2D.IPath MoveTo(float x, float y);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.Path.MoveTo(float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the start of a new contour.

<a name='Tizen.UI.Primitives2D.Path.MoveTo(float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the start of a new contour.

#### Returns
[IPath](Tizen.UI.Primitives2D.IPath.md 'Tizen.UI.Primitives2D.IPath')  
A [MoveTo(float, float)](Tizen.UI.Primitives2D.Path.md#Tizen.UI.Primitives2D.Path.MoveTo(float,float) 'Tizen.UI.Primitives2D.Path.MoveTo(float, float)') object.


















































