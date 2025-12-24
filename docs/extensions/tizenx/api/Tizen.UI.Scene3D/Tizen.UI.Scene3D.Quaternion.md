### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## Quaternion Struct

Represents a vector that is used to encode three-dimensional physical rotations.

```csharp
public struct Quaternion
```
### Constructors

<a name='Tizen.UI.Scene3D.Quaternion.Quaternion(float,float,float,float)'></a>

## Quaternion(float, float, float, float) Constructor

Initializes a new instance of the [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion') struct with the specified [X](Tizen.UI.Scene3D.Quaternion.md#Tizen.UI.Scene3D.Quaternion.X 'Tizen.UI.Scene3D.Quaternion.X'), [Y](Tizen.UI.Scene3D.Quaternion.md#Tizen.UI.Scene3D.Quaternion.Y 'Tizen.UI.Scene3D.Quaternion.Y'), [Z](Tizen.UI.Scene3D.Quaternion.md#Tizen.UI.Scene3D.Quaternion.Z 'Tizen.UI.Scene3D.Quaternion.Z') and [W](Tizen.UI.Scene3D.Quaternion.md#Tizen.UI.Scene3D.Quaternion.W 'Tizen.UI.Scene3D.Quaternion.W') components.

```csharp
public Quaternion(float x, float y, float z, float w);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Quaternion.Quaternion(float,float,float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the vector represented by the [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion').

<a name='Tizen.UI.Scene3D.Quaternion.Quaternion(float,float,float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the vector represented by the [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion').

<a name='Tizen.UI.Scene3D.Quaternion.Quaternion(float,float,float,float).z'></a>

`z` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The z-coordinate of the vector represented by the [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion').

<a name='Tizen.UI.Scene3D.Quaternion.Quaternion(float,float,float,float).w'></a>

`w` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The scalar component of the [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion') that combines with the vector components to form the quaternion.

<a name='Tizen.UI.Scene3D.Quaternion.Quaternion(Tizen.UI.Scene3D.Vector3D,float)'></a>

## Quaternion(Vector3D, float) Constructor

Initializes a new instance of the [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion') class.

```csharp
public Quaternion(Tizen.UI.Scene3D.Vector3D axis, float angleInDegree);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Quaternion.Quaternion(Tizen.UI.Scene3D.Vector3D,float).axis'></a>

`axis` [Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D')

The axis around which to rotate.

<a name='Tizen.UI.Scene3D.Quaternion.Quaternion(Tizen.UI.Scene3D.Vector3D,float).angleInDegree'></a>

`angleInDegree` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The angle of rotation, in degrees.
### Fields

<a name='Tizen.UI.Scene3D.Quaternion.W'></a>

## Quaternion.W Field

The W value of the vector component of the quaternion.

```csharp
public float W;
```

#### Field Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.Quaternion.X'></a>

## Quaternion.X Field

The X value of the vector component of the quaternion.

```csharp
public float X;
```

#### Field Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.Quaternion.Y'></a>

## Quaternion.Y Field

The Y value of the vector component of the quaternion.

```csharp
public float Y;
```

#### Field Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.Quaternion.Z'></a>

## Quaternion.Z Field

The Z value of the vector component of the quaternion.

```csharp
public float Z;
```

#### Field Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Properties

<a name='Tizen.UI.Scene3D.Quaternion.Angle'></a>

## Quaternion.Angle Property

Gets the angle of rotation represented by the vector in degrees.

```csharp
public float Angle { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.Quaternion.Axis'></a>

## Quaternion.Axis Property

Gets the axis of rotation represented by the vector.

```csharp
public Tizen.UI.Scene3D.Vector3D Axis { get; }
```

#### Property Value
[Vector3D](Tizen.UI.Scene3D.Vector3D.md 'Tizen.UI.Scene3D.Vector3D')

<a name='Tizen.UI.Scene3D.Quaternion.Identity'></a>

## Quaternion.Identity Property

Gets a quaternion that represents no rotation.

```csharp
public static Tizen.UI.Scene3D.Quaternion Identity { get; }
```

#### Property Value
[Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')

<a name='Tizen.UI.Scene3D.Quaternion.IsIdentity'></a>

## Quaternion.IsIdentity Property

Gets a value that indicates whether the current instance is the identity quaternion.

```csharp
public bool IsIdentity { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Scene3D.Quaternion.Length'></a>

## Quaternion.Length Property

Gets the length of the vector component of the quaternion.

```csharp
public float Length { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.Quaternion.LengthSquared'></a>

## Quaternion.LengthSquared Property

Gets the squared length of the vector component of the quaternion.

```csharp
public float LengthSquared { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.Scene3D.Quaternion.Concatenate(Tizen.UI.Scene3D.Quaternion,Tizen.UI.Scene3D.Quaternion)'></a>

## Quaternion.Concatenate(Quaternion, Quaternion) Method

Concatenates two quaternions.

```csharp
public static Tizen.UI.Scene3D.Quaternion Concatenate(Tizen.UI.Scene3D.Quaternion value1, Tizen.UI.Scene3D.Quaternion value2);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Quaternion.Concatenate(Tizen.UI.Scene3D.Quaternion,Tizen.UI.Scene3D.Quaternion).value1'></a>

`value1` [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')

The first [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion') to concatenate.

<a name='Tizen.UI.Scene3D.Quaternion.Concatenate(Tizen.UI.Scene3D.Quaternion,Tizen.UI.Scene3D.Quaternion).value2'></a>

`value2` [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')

The second [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion') to concatenate.

#### Returns
[Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')  
A new [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion') that represents the concatenated rotation.

<a name='Tizen.UI.Scene3D.Quaternion.Conjugate(Tizen.UI.Scene3D.Quaternion)'></a>

## Quaternion.Conjugate(Quaternion) Method

Returns the conjugate of a specified quaternion.

```csharp
public static Tizen.UI.Scene3D.Quaternion Conjugate(Tizen.UI.Scene3D.Quaternion value);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Quaternion.Conjugate(Tizen.UI.Scene3D.Quaternion).value'></a>

`value` [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')

The [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion') value to conjugate.

#### Returns
[Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')  
The conjugated [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion') value.

<a name='Tizen.UI.Scene3D.Quaternion.CreateFromAxisAngle(System.Numerics.Vector3,float)'></a>

## Quaternion.CreateFromAxisAngle(Vector3, float) Method

Creates a quaternion from a unit vector and an angle to rotate around the vector.

```csharp
public static Tizen.UI.Scene3D.Quaternion CreateFromAxisAngle(System.Numerics.Vector3 axis, float angle);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Quaternion.CreateFromAxisAngle(System.Numerics.Vector3,float).axis'></a>

`axis` [System.Numerics.Vector3](https://docs.microsoft.com/en-us/dotnet/api/System.Numerics.Vector3 'System.Numerics.Vector3')

The axis around which to rotate.

<a name='Tizen.UI.Scene3D.Quaternion.CreateFromAxisAngle(System.Numerics.Vector3,float).angle'></a>

`angle` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The angle, in radians, by which to rotate around the axis.

#### Returns
[Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')  
A new instance of the [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion') class that represents the rotation around the specified axis and angle.

<a name='Tizen.UI.Scene3D.Quaternion.CreateFromRotationMatrix(System.Numerics.Matrix4x4)'></a>

## Quaternion.CreateFromRotationMatrix(Matrix4x4) Method

Creates a quaternion from the specified rotation matrix.

```csharp
public static Tizen.UI.Scene3D.Quaternion CreateFromRotationMatrix(System.Numerics.Matrix4x4 matrix);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Quaternion.CreateFromRotationMatrix(System.Numerics.Matrix4x4).matrix'></a>

`matrix` [System.Numerics.Matrix4x4](https://docs.microsoft.com/en-us/dotnet/api/System.Numerics.Matrix4x4 'System.Numerics.Matrix4x4')

The rotation matrix to create the instance from.

#### Returns
[Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')  
A new instance of the [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion') class representing the specified rotation matrix.

<a name='Tizen.UI.Scene3D.Quaternion.CreateFromYawPitchRoll(float,float,float)'></a>

## Quaternion.CreateFromYawPitchRoll(float, float, float) Method

Creates a new quaternion from the given yaw, pitch, and roll.

```csharp
public static Tizen.UI.Scene3D.Quaternion CreateFromYawPitchRoll(float yaw, float pitch, float roll);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Quaternion.CreateFromYawPitchRoll(float,float,float).yaw'></a>

`yaw` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The yaw angle, in radians.

<a name='Tizen.UI.Scene3D.Quaternion.CreateFromYawPitchRoll(float,float,float).pitch'></a>

`pitch` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The pitch angle, in radians.

<a name='Tizen.UI.Scene3D.Quaternion.CreateFromYawPitchRoll(float,float,float).roll'></a>

`roll` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The roll angle, in radians.

#### Returns
[Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')  
A new instance of the [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion') class.

<a name='Tizen.UI.Scene3D.Quaternion.Dot(Tizen.UI.Scene3D.Quaternion,Tizen.UI.Scene3D.Quaternion)'></a>

## Quaternion.Dot(Quaternion, Quaternion) Method

Calculates the dot product of two quaternions.

```csharp
public static float Dot(Tizen.UI.Scene3D.Quaternion quaternion1, Tizen.UI.Scene3D.Quaternion quaternion2);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Quaternion.Dot(Tizen.UI.Scene3D.Quaternion,Tizen.UI.Scene3D.Quaternion).quaternion1'></a>

`quaternion1` [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')

The first input quaternion.

<a name='Tizen.UI.Scene3D.Quaternion.Dot(Tizen.UI.Scene3D.Quaternion,Tizen.UI.Scene3D.Quaternion).quaternion2'></a>

`quaternion2` [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')

The second input quaternion.

#### Returns
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')  
The dot product of the two quaternions.

<a name='Tizen.UI.Scene3D.Quaternion.Equals(object)'></a>

## Quaternion.Equals(object) Method

Indicates whether this instance and a specified object are equal.

```csharp
public override bool Equals(object obj);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Quaternion.Equals(object).obj'></a>

`obj` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The object to compare with the current instance.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
[true](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool') if [obj](Tizen.UI.Scene3D.Quaternion.md#Tizen.UI.Scene3D.Quaternion.Equals(object).obj 'Tizen.UI.Scene3D.Quaternion.Equals(object).obj') and this instance are the same type and represent the same value; otherwise, [false](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool').

<a name='Tizen.UI.Scene3D.Quaternion.Equals(Tizen.UI.Scene3D.Quaternion)'></a>

## Quaternion.Equals(Quaternion) Method

Returns a value that indicates whether this instance and a specified Quaternion instance or a specified object are equal.

```csharp
public bool Equals(Tizen.UI.Scene3D.Quaternion other);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Quaternion.Equals(Tizen.UI.Scene3D.Quaternion).other'></a>

`other` [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')

The other quaternion.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the specified object is equal to the current instance; otherwise, false.

<a name='Tizen.UI.Scene3D.Quaternion.GetHashCode()'></a>

## Quaternion.GetHashCode() Method

Returns the hash code for this instance.

```csharp
public override int GetHashCode();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
A 32-bit signed integer that is the hash code for this instance.

<a name='Tizen.UI.Scene3D.Quaternion.Inverse(Tizen.UI.Scene3D.Quaternion)'></a>

## Quaternion.Inverse(Quaternion) Method

Returns the inverse of a quaternion.

```csharp
public static Tizen.UI.Scene3D.Quaternion Inverse(Tizen.UI.Scene3D.Quaternion value);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Quaternion.Inverse(Tizen.UI.Scene3D.Quaternion).value'></a>

`value` [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')

The [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion') to invert.

#### Returns
[Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')  
The inverted  [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion').

<a name='Tizen.UI.Scene3D.Quaternion.Lerp(Tizen.UI.Scene3D.Quaternion,Tizen.UI.Scene3D.Quaternion,float)'></a>

## Quaternion.Lerp(Quaternion, Quaternion, float) Method

Performs a linear interpolation between two quaternions based on a value that specifies the weighting of the second quaternion.

```csharp
public static Tizen.UI.Scene3D.Quaternion Lerp(Tizen.UI.Scene3D.Quaternion quaternion1, Tizen.UI.Scene3D.Quaternion quaternion2, float amount);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Quaternion.Lerp(Tizen.UI.Scene3D.Quaternion,Tizen.UI.Scene3D.Quaternion,float).quaternion1'></a>

`quaternion1` [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')

The first input quaternion.

<a name='Tizen.UI.Scene3D.Quaternion.Lerp(Tizen.UI.Scene3D.Quaternion,Tizen.UI.Scene3D.Quaternion,float).quaternion2'></a>

`quaternion2` [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')

The second input quaternion.

<a name='Tizen.UI.Scene3D.Quaternion.Lerp(Tizen.UI.Scene3D.Quaternion,Tizen.UI.Scene3D.Quaternion,float).amount'></a>

`amount` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The amount of interpolation between the two quaternions.

#### Returns
[Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')  
The interpolated result.

<a name='Tizen.UI.Scene3D.Quaternion.Normalize(Tizen.UI.Scene3D.Quaternion)'></a>

## Quaternion.Normalize(Quaternion) Method

Divides each component of a specified Quaternion by its length.

```csharp
public static Tizen.UI.Scene3D.Quaternion Normalize(Tizen.UI.Scene3D.Quaternion value);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Quaternion.Normalize(Tizen.UI.Scene3D.Quaternion).value'></a>

`value` [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')

The input [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion') instance to normalize.

#### Returns
[Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')  
A new instance of the [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion') class with its values set to the normalized values of the given instance.

<a name='Tizen.UI.Scene3D.Quaternion.Slerp(Tizen.UI.Scene3D.Quaternion,Tizen.UI.Scene3D.Quaternion,float)'></a>

## Quaternion.Slerp(Quaternion, Quaternion, float) Method

Interpolates between two quaternions, using spherical linear interpolation.

```csharp
public static Tizen.UI.Scene3D.Quaternion Slerp(Tizen.UI.Scene3D.Quaternion quaternion1, Tizen.UI.Scene3D.Quaternion quaternion2, float amount);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Quaternion.Slerp(Tizen.UI.Scene3D.Quaternion,Tizen.UI.Scene3D.Quaternion,float).quaternion1'></a>

`quaternion1` [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')

The first quaternion.

<a name='Tizen.UI.Scene3D.Quaternion.Slerp(Tizen.UI.Scene3D.Quaternion,Tizen.UI.Scene3D.Quaternion,float).quaternion2'></a>

`quaternion2` [Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')

The second quaternion.

<a name='Tizen.UI.Scene3D.Quaternion.Slerp(Tizen.UI.Scene3D.Quaternion,Tizen.UI.Scene3D.Quaternion,float).amount'></a>

`amount` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The amount of interpolation.

#### Returns
[Quaternion](Tizen.UI.Scene3D.Quaternion.md 'Tizen.UI.Scene3D.Quaternion')  
The interpolated quaternion.

<a name='Tizen.UI.Scene3D.Quaternion.ToString()'></a>

## Quaternion.ToString() Method

Returns the fully qualified type name of this instance.

```csharp
public override string ToString();
```

#### Returns
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
The fully qualified type name.





































