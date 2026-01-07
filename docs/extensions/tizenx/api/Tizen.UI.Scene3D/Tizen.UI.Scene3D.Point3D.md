### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## Point3D Struct

Represents a point in 3D space.

```csharp
public struct Point3D
```
### Constructors

<a name='Tizen.UI.Scene3D.Point3D.Point3D(float,float,float)'></a>

## Point3D(float, float, float) Constructor

Initializes a new instance of the [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D') struct.

```csharp
public Point3D(float x, float y, float z);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Point3D.Point3D(float,float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the point.

<a name='Tizen.UI.Scene3D.Point3D.Point3D(float,float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the point.

<a name='Tizen.UI.Scene3D.Point3D.Point3D(float,float,float).z'></a>

`z` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The z-coordinate of the point.

<a name='Tizen.UI.Scene3D.Point3D.Point3D(Tizen.UI.Scene3D.Size3D)'></a>

## Point3D(Size3D) Constructor

Initializes a new instance of the [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D') struct.

```csharp
public Point3D(Tizen.UI.Scene3D.Size3D sz);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Point3D.Point3D(Tizen.UI.Scene3D.Size3D).sz'></a>

`sz` [Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D')

A [Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D') representing the size of the point.

<a name='Tizen.UI.Scene3D.Point3D.Point3D(Tizen.UI.Scene3D.Vector3D)'></a>

## Point3D(Vector3D) Constructor

Initializes a new instance of the [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D') struct.

```csharp
public Point3D(Tizen.UI.Scene3D.Vector3D v);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Point3D.Point3D(Tizen.UI.Scene3D.Vector3D).v'></a>

`v` [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D')

A [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D') representing the vector of the point.
### Fields

<a name='Tizen.UI.Scene3D.Point3D.Zero'></a>

## Point3D.Zero Field

A point at the origin (0, 0, 0).

```csharp
public static Point3D Zero;
```

#### Field Value
[Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D')
### Properties

<a name='Tizen.UI.Scene3D.Point3D.IsEmpty'></a>

## Point3D.IsEmpty Property

Gets a value indicating whether the point is empty.

```csharp
public bool IsEmpty { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Scene3D.Point3D.X'></a>

## Point3D.X Property

The x-coordinate of the point.

```csharp
public float X { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.Point3D.Y'></a>

## Point3D.Y Property

The y-coordinate of the point.

```csharp
public float Y { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.Point3D.Z'></a>

## Point3D.Z Property

The z-coordinate of the point.

```csharp
public float Z { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.Scene3D.Point3D.Deconstruct(float,float,float)'></a>

## Point3D.Deconstruct(float, float, float) Method

Deconstructs the Point3D into its individual components (x, y, and z).

```csharp
public void Deconstruct(out float x, out float y, out float z);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Point3D.Deconstruct(float,float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the point.

<a name='Tizen.UI.Scene3D.Point3D.Deconstruct(float,float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the point.

<a name='Tizen.UI.Scene3D.Point3D.Deconstruct(float,float,float).z'></a>

`z` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The z-coordinate point.

<a name='Tizen.UI.Scene3D.Point3D.Distance(Tizen.UI.Scene3D.Point3D)'></a>

## Point3D.Distance(Point3D) Method

Calculates the distance between two points in 3D space.

```csharp
public double Distance(Tizen.UI.Scene3D.Point3D other);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Point3D.Distance(Tizen.UI.Scene3D.Point3D).other'></a>

`other` [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D')

The other point to calculate the distance to.

#### Returns
[System.Double](https://docs.microsoft.com/en-us/dotnet/api/System.Double 'System.Double')  
The distance between the two points.

<a name='Tizen.UI.Scene3D.Point3D.Equals(object)'></a>

## Point3D.Equals(object) Method

Indicates whether this instance and a specified object are equal.

```csharp
public override bool Equals(object o);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Point3D.Equals(object).o'></a>

`o` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
[true](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool') if obj and this instance are the same type and represent the same value; otherwise, [false](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool').

<a name='Tizen.UI.Scene3D.Point3D.GetHashCode()'></a>

## Point3D.GetHashCode() Method

Returns the hash code for this instance.

```csharp
public override int GetHashCode();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
A 32-bit signed integer that is the hash code for this instance.

<a name='Tizen.UI.Scene3D.Point3D.Offset(float,float,float)'></a>

## Point3D.Offset(float, float, float) Method

Returns a new [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D') that is offset by the specified distances.

```csharp
public Tizen.UI.Scene3D.Point3D Offset(float dx, float dy, float dz);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Point3D.Offset(float,float,float).dx'></a>

`dx` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The distance to offset the x-coordinate.

<a name='Tizen.UI.Scene3D.Point3D.Offset(float,float,float).dy'></a>

`dy` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The distance to offset the y-coordinate.

<a name='Tizen.UI.Scene3D.Point3D.Offset(float,float,float).dz'></a>

`dz` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The distance to offset the z-coordinate.

#### Returns
[Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D')  
A new [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D') offset by the specified distances.

<a name='Tizen.UI.Scene3D.Point3D.Round()'></a>

## Point3D.Round() Method

Returns a new [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D') with the coordinates rounded to the nearest integer values.

```csharp
public Tizen.UI.Scene3D.Point3D Round();
```

#### Returns
[Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D')  
A new [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D') with the coordinates rounded to the nearest integer values.

<a name='Tizen.UI.Scene3D.Point3D.ToString()'></a>

## Point3D.ToString() Method

Returns the fully qualified type name of this instance.

```csharp
public override string ToString();
```

#### Returns
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
The fully qualified type name.
### Operators

<a name='Tizen.UI.Scene3D.Point3D.op_ExplicitTizen.UI.Scene3D.Size3D(Tizen.UI.Scene3D.Point3D)'></a>

## Point3D.explicit operator Size3D(Point3D) Operator

Explicitly converts a [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D') to a [Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D').

```csharp
public static Tizen.UI.Scene3D.Size3D explicit operator Size3D(Tizen.UI.Scene3D.Point3D pt);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Point3D.op_ExplicitTizen.UI.Scene3D.Size3D(Tizen.UI.Scene3D.Point3D).pt'></a>

`pt` [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D')

The [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D') to convert.

#### Returns
[Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D')  
A new [Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D') with the same coordinates as the [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D').

<a name='Tizen.UI.Scene3D.Point3D.op_ExplicitTizen.UI.Scene3D.Vector3D(Tizen.UI.Scene3D.Point3D)'></a>

## Point3D.explicit operator Vector3D(Point3D) Operator

Explicitly converts a [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D') to a [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D').

```csharp
public static Tizen.UI.Scene3D.Vector3D explicit operator Vector3D(Tizen.UI.Scene3D.Point3D pt);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Point3D.op_ExplicitTizen.UI.Scene3D.Vector3D(Tizen.UI.Scene3D.Point3D).pt'></a>

`pt` [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D')

The [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D') to convert.

#### Returns
[Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D')  
A new [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D') with the same coordinates as the [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D').





































