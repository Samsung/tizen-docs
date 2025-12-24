### [Tizen.UI.Primitives2D](Tizen.UI.Primitives2D.md 'Tizen.UI.Primitives2D')

## ArcTo Class

Represents a command that appends a line and arc to the current path.

```csharp
public class ArcTo :
Tizen.UI.Primitives2D.IPath
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; ArcTo

Implements [IPath](Tizen.UI.Primitives2D.IPath.md 'Tizen.UI.Primitives2D.IPath')
### Constructors

<a name='Tizen.UI.Primitives2D.ArcTo.ArcTo(float,float,float,float,float,bool)'></a>

## ArcTo(float, float, float, float, float, bool) Constructor

Appends the specified arc to the path.

```csharp
public ArcTo(float x, float y, float radius, float startAngle, float sweep, bool closed);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.ArcTo.ArcTo(float,float,float,float,float,bool).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the end point of the arc.

<a name='Tizen.UI.Primitives2D.ArcTo.ArcTo(float,float,float,float,float,bool).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the end point of the arc.

<a name='Tizen.UI.Primitives2D.ArcTo.ArcTo(float,float,float,float,float,bool).radius'></a>

`radius` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The radius of the arc.

<a name='Tizen.UI.Primitives2D.ArcTo.ArcTo(float,float,float,float,float,bool).startAngle'></a>

`startAngle` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The starting angle of the arc, in radians.

<a name='Tizen.UI.Primitives2D.ArcTo.ArcTo(float,float,float,float,float,bool).sweep'></a>

`sweep` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The angle of the arc, in radians.

<a name='Tizen.UI.Primitives2D.ArcTo.ArcTo(float,float,float,float,float,bool).closed'></a>

`closed` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

A value indicating whether the arc should be connected to the start point by a straight line.
### Properties

<a name='Tizen.UI.Primitives2D.ArcTo.Closed'></a>

## ArcTo.Closed Property

Gets a value indicating whether the arc should be connected to the start point by a straight line.

```csharp
public bool Closed { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Primitives2D.ArcTo.Radius'></a>

## ArcTo.Radius Property

Gets the radius of the arc.

```csharp
public float Radius { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Primitives2D.ArcTo.StartAngle'></a>

## ArcTo.StartAngle Property

Gets the starting angle of the arc, in radians.

```csharp
public float StartAngle { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Primitives2D.ArcTo.Sweep'></a>

## ArcTo.Sweep Property

Gets the angle of the arc, in radians.

```csharp
public float Sweep { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Primitives2D.ArcTo.X'></a>

## ArcTo.X Property

Gets the x-coordinate of the end point of the arc.

```csharp
public float X { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Primitives2D.ArcTo.Y'></a>

## ArcTo.Y Property

Gets the y-coordinate of the end point of the arc.

```csharp
public float Y { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')


















































