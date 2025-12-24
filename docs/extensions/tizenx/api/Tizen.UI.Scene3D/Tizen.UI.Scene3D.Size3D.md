### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## Size3D Struct

Represents a three-dimensional size.

```csharp
public struct Size3D
```
### Constructors

<a name='Tizen.UI.Scene3D.Size3D.Size3D(float,float,float)'></a>

## Size3D(float, float, float) Constructor

Initializes a new instance of the [Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D') structure with the specified width, height, and depth.

```csharp
public Size3D(float x, float y, float z);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Size3D.Size3D(float,float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width of the size.

<a name='Tizen.UI.Scene3D.Size3D.Size3D(float,float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The height of the size.

<a name='Tizen.UI.Scene3D.Size3D.Size3D(float,float,float).z'></a>

`z` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The depth of the size.
### Fields

<a name='Tizen.UI.Scene3D.Size3D.Zero'></a>

## Size3D.Zero Field

Gets a [Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D') structure that has a width, height, and depth of zero.

```csharp
public static readonly Size3D Zero;
```

#### Field Value
[Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D')
### Properties

<a name='Tizen.UI.Scene3D.Size3D.IsZero'></a>

## Size3D.IsZero Property

Gets a value indicating whether this [Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D') is equal [Zero](Tizen.UI.Scene3D.Size3D.md#Tizen.UI.Scene3D.Size3D.Zero 'Tizen.UI.Scene3D.Size3D.Zero') size.

```csharp
public bool IsZero { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Scene3D.Size3D.X'></a>

## Size3D.X Property

Gets or sets the width component of this [Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D') structure.

```csharp
public float X { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.Size3D.Y'></a>

## Size3D.Y Property

Gets or sets the height component of this [Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D') structure.

```csharp
public float Y { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Scene3D.Size3D.Z'></a>

## Size3D.Z Property

Gets or sets the depth component of this [Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D') structure.

```csharp
public float Z { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.Scene3D.Size3D.Deconstruct(float,float,float)'></a>

## Size3D.Deconstruct(float, float, float) Method

Deconstructs the Size3D object into its individual components (X, Y, and Z).

```csharp
public void Deconstruct(out float x, out float y, out float z);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Size3D.Deconstruct(float,float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The X component of the Size3D.

<a name='Tizen.UI.Scene3D.Size3D.Deconstruct(float,float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The Y component of the Size3D.

<a name='Tizen.UI.Scene3D.Size3D.Deconstruct(float,float,float).z'></a>

`z` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The Z component of the Size3D.

<a name='Tizen.UI.Scene3D.Size3D.Equals(object)'></a>

## Size3D.Equals(object) Method

Indicates whether this instance and a specified object are equal.

```csharp
public override bool Equals(object obj);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Size3D.Equals(object).obj'></a>

`obj` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The object to compare with the current instance.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
[true](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool') if [obj](Tizen.UI.Scene3D.Size3D.md#Tizen.UI.Scene3D.Size3D.Equals(object).obj 'Tizen.UI.Scene3D.Size3D.Equals(object).obj') and this instance are the same type and represent the same value; otherwise, [false](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool').

<a name='Tizen.UI.Scene3D.Size3D.Equals(Tizen.UI.Scene3D.Size3D)'></a>

## Size3D.Equals(Size3D) Method

Indicates whether this instance and a specified object are equal.

```csharp
public bool Equals(Tizen.UI.Scene3D.Size3D other);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Size3D.Equals(Tizen.UI.Scene3D.Size3D).other'></a>

`other` [Size3D](Tizen.UI.Scene3D.Size3D.md 'Tizen.UI.Scene3D.Size3D')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if obj and this instance are the same type and represent the same value, otherwise false.

<a name='Tizen.UI.Scene3D.Size3D.GetHashCode()'></a>

## Size3D.GetHashCode() Method

Returns the hash code for this instance.

```csharp
public override int GetHashCode();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
A 32-bit signed integer that is the hash code for this instance.

<a name='Tizen.UI.Scene3D.Size3D.ToString()'></a>

## Size3D.ToString() Method

Returns the fully qualified type name of this instance.

```csharp
public override string ToString();
```

#### Returns
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
The fully qualified type name.





































