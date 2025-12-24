### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## Vector3D Struct

Represents a vector with three single-precision floating-point values.

```csharp
public struct Vector3D
```
### Constructors

<a name='Tizen.UI.Scene3D.Vector3D.Vector3D(float,float,float)'></a>

## Vector3D(float, float, float) Constructor

Initializes a new instance of the [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D') struct.

```csharp
public Vector3D(float x, float y, float z);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Vector3D.Vector3D(float,float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The X component of the vector.

<a name='Tizen.UI.Scene3D.Vector3D.Vector3D(float,float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The Y component of the vector.

<a name='Tizen.UI.Scene3D.Vector3D.Vector3D(float,float,float).z'></a>

`z` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The Z component of the vector.

<a name='Tizen.UI.Scene3D.Vector3D.Vector3D(Tizen.UI.Scene3D.Point3D)'></a>

## Vector3D(Point3D) Constructor

Initializes a new instance of the [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D') struct.

```csharp
public Vector3D(Tizen.UI.Scene3D.Point3D v);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Vector3D.Vector3D(Tizen.UI.Scene3D.Point3D).v'></a>

`v` [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D')

The [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D') to convert to a [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D').
### Properties

<a name='Tizen.UI.Scene3D.Vector3D.Length'></a>

## Vector3D.Length Property

Gets the length of the vector.

```csharp
public float Length { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.Vector3D.LengthSquared'></a>

## Vector3D.LengthSquared Property

Gets the squared length of the vector.

```csharp
public float LengthSquared { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.Vector3D.X'></a>

## Vector3D.X Property

Gets or sets the X component of the vector.

```csharp
public float X { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.Vector3D.Y'></a>

## Vector3D.Y Property

Gets or sets the Y component of the vector.

```csharp
public float Y { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.Vector3D.Z'></a>

## Vector3D.Z Property

Gets or sets the Z component of the vector.

```csharp
public float Z { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.Scene3D.Vector3D.AngleBetween(Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D)'></a>

## Vector3D.AngleBetween(Vector3D, Vector3D) Method

Returns the angle between two vectors in degrees.

```csharp
public static float AngleBetween(Tizen.UI.Scene3D.Vector3D v1, Tizen.UI.Scene3D.Vector3D v2);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Vector3D.AngleBetween(Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D).v1'></a>

`v1` [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D')

The first vector.

<a name='Tizen.UI.Scene3D.Vector3D.AngleBetween(Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D).v2'></a>

`v2` [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D')

The second vector.

#### Returns
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')  
The angle between the two vectors in degrees.

<a name='Tizen.UI.Scene3D.Vector3D.Cross(Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D)'></a>

## Vector3D.Cross(Vector3D, Vector3D) Method

Returns the cross product of two vectors.

```csharp
public static Tizen.UI.Scene3D.Vector3D Cross(Tizen.UI.Scene3D.Vector3D v1, Tizen.UI.Scene3D.Vector3D v2);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Vector3D.Cross(Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D).v1'></a>

`v1` [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D')

The first vector.

<a name='Tizen.UI.Scene3D.Vector3D.Cross(Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D).v2'></a>

`v2` [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D')

The second vector.

#### Returns
[Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D')  
The cross product of the two vectors.

<a name='Tizen.UI.Scene3D.Vector3D.Dot(Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D)'></a>

## Vector3D.Dot(Vector3D, Vector3D) Method

Returns the dot product of two vectors.

```csharp
public static float Dot(Tizen.UI.Scene3D.Vector3D v1, Tizen.UI.Scene3D.Vector3D v2);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Vector3D.Dot(Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D).v1'></a>

`v1` [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D')

The first vector.

<a name='Tizen.UI.Scene3D.Vector3D.Dot(Tizen.UI.Scene3D.Vector3D,Tizen.UI.Scene3D.Vector3D).v2'></a>

`v2` [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D')

The second vector.

#### Returns
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')  
The dot product of the two vectors.

<a name='Tizen.UI.Scene3D.Vector3D.Equals(object)'></a>

## Vector3D.Equals(object) Method

Indicates whether this instance and a specified object are equal.

```csharp
public override bool Equals(object o);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Vector3D.Equals(object).o'></a>

`o` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
[true](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool') if obj and this instance are the same type and represent the same value; otherwise, [false](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool').

<a name='Tizen.UI.Scene3D.Vector3D.GetHashCode()'></a>

## Vector3D.GetHashCode() Method

Returns the hash code for this instance.

```csharp
public override int GetHashCode();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
A 32-bit signed integer that is the hash code for this instance.

<a name='Tizen.UI.Scene3D.Vector3D.Normalize()'></a>

## Vector3D.Normalize() Method

Normalizes the vector.

```csharp
public void Normalize();
```

<a name='Tizen.UI.Scene3D.Vector3D.Round()'></a>

## Vector3D.Round() Method

Rounds the vector's components to the nearest integer values.

```csharp
public Tizen.UI.Scene3D.Vector3D Round();
```

#### Returns
[Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D')  
The rounded vector.

<a name='Tizen.UI.Scene3D.Vector3D.ToString()'></a>

## Vector3D.ToString() Method

Returns the fully qualified type name of this instance.

```csharp
public override string ToString();
```

#### Returns
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
The fully qualified type name.
### Operators

<a name='Tizen.UI.Scene3D.Vector3D.op_ExplicitTizen.UI.Scene3D.Point3D(Tizen.UI.Scene3D.Vector3D)'></a>

## Vector3D.explicit operator Point3D(Vector3D) Operator

Converts a [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D') to a [Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D').

```csharp
public static Tizen.UI.Scene3D.Point3D explicit operator Point3D(Tizen.UI.Scene3D.Vector3D v);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Vector3D.op_ExplicitTizen.UI.Scene3D.Point3D(Tizen.UI.Scene3D.Vector3D).v'></a>

`v` [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D')

The vector to convert.

#### Returns
[Point3D](Tizen.UI.Scene3D.Point3D.md 'Tizen.UI.Scene3D.Point3D')  
The converted point.





































