### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## WindowBlur Struct

WindowBlurInfo is a struct designed to encapsulate the information required to apply a blur effect to a window.   
It contains three properties that define how the blur effect is applied to the window,   
including the type of blur, its intensity, and the corner rounding for the background blur.

```csharp
public struct WindowBlur :
System.IEquatable&lt;Tizen.UI.WindowBlur>
```

Implements [System.IEquatable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1 'System.IEquatable`1')[WindowBlur](Tizen.UI.WindowBlur.md 'Tizen.UI.WindowBlur')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1 'System.IEquatable`1')
### Constructors

<a name='Tizen.UI.WindowBlur.WindowBlur()'></a>

## WindowBlur() Constructor

The construct of WindowBlur

```csharp
public WindowBlur();
```

<a name='Tizen.UI.WindowBlur.WindowBlur(Tizen.UI.WindowBlurType,int)'></a>

## WindowBlur(WindowBlurType, int) Constructor

The construct with blur type and radius.

```csharp
public WindowBlur(Tizen.UI.WindowBlurType blurType, int blurRadius);
```
#### Parameters

<a name='Tizen.UI.WindowBlur.WindowBlur(Tizen.UI.WindowBlurType,int).blurType'></a>

`blurType` [WindowBlurType](Tizen.UI.WindowBlurType.md 'Tizen.UI.WindowBlurType')

<a name='Tizen.UI.WindowBlur.WindowBlur(Tizen.UI.WindowBlurType,int).blurRadius'></a>

`blurRadius` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.WindowBlur.WindowBlur(Tizen.UI.WindowBlurType,int,int)'></a>

## WindowBlur(WindowBlurType, int, int) Constructor

The construct with blur type, radius and corner radius for background type.

```csharp
public WindowBlur(Tizen.UI.WindowBlurType blurType, int blurRadius, int cornerRadius);
```
#### Parameters

<a name='Tizen.UI.WindowBlur.WindowBlur(Tizen.UI.WindowBlurType,int,int).blurType'></a>

`blurType` [WindowBlurType](Tizen.UI.WindowBlurType.md 'Tizen.UI.WindowBlurType')

<a name='Tizen.UI.WindowBlur.WindowBlur(Tizen.UI.WindowBlurType,int,int).blurRadius'></a>

`blurRadius` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.WindowBlur.WindowBlur(Tizen.UI.WindowBlurType,int,int).cornerRadius'></a>

`cornerRadius` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')
### Properties

<a name='Tizen.UI.WindowBlur.BackgroundCornerRadius'></a>

## WindowBlur.BackgroundCornerRadius Property

Gets or sets the corner radius of the window.  
It is only useful when window blur type is background.  
  
When applying the background corner radius, ensure that the window's own corner radius is applied first.   
The blur effect will respect the window's pre-defined corner radius settings   
before applying the specified background corner radius.

```csharp
public int BackgroundCornerRadius { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The corner radius of the window.

<a name='Tizen.UI.WindowBlur.BlurRadius'></a>

## WindowBlur.BlurRadius Property

Gets or sets the blur radius of the window.

```csharp
public int BlurRadius { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The blur radius of the window.

<a name='Tizen.UI.WindowBlur.BlurType'></a>

## WindowBlur.BlurType Property

Gets or sets the blur type of the window.

```csharp
public Tizen.UI.WindowBlurType BlurType { get; set; }
```

#### Property Value
[WindowBlurType](Tizen.UI.WindowBlurType.md 'Tizen.UI.WindowBlurType')  
The window blur type of the window.
### Methods

<a name='Tizen.UI.WindowBlur.Equals(object)'></a>

## WindowBlur.Equals(object) Method

Indicates whether this instance and a specified object are equal.

```csharp
public override bool Equals(object obj);
```
#### Parameters

<a name='Tizen.UI.WindowBlur.Equals(object).obj'></a>

`obj` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The object to compare with the current instance.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
[true](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool') if [obj](Tizen.UI.WindowBlur.md#Tizen.UI.WindowBlur.Equals(object).obj 'Tizen.UI.WindowBlur.Equals(object).obj') and this instance are the same type and represent the same value; otherwise, [false](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool').

<a name='Tizen.UI.WindowBlur.Equals(Tizen.UI.WindowBlur)'></a>

## WindowBlur.Equals(WindowBlur) Method

Whether this is equivalent to other.

```csharp
public bool Equals(Tizen.UI.WindowBlur other);
```
#### Parameters

<a name='Tizen.UI.WindowBlur.Equals(Tizen.UI.WindowBlur).other'></a>

`other` [WindowBlur](Tizen.UI.WindowBlur.md 'Tizen.UI.WindowBlur')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.WindowBlur.GetHashCode()'></a>

## WindowBlur.GetHashCode() Method

Returns the hash code for this instance.

```csharp
public override int GetHashCode();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
A 32-bit signed integer that is the hash code for this instance.
### Operators

<a name='Tizen.UI.WindowBlur.op_Equality(Tizen.UI.WindowBlur,Tizen.UI.WindowBlur)'></a>

## WindowBlur.operator ==(WindowBlur, WindowBlur) Operator

Compares two WindowBlurInfo for equality.

```csharp
public static bool operator ==(Tizen.UI.WindowBlur operand1, Tizen.UI.WindowBlur operand2);
```
#### Parameters

<a name='Tizen.UI.WindowBlur.op_Equality(Tizen.UI.WindowBlur,Tizen.UI.WindowBlur).operand1'></a>

`operand1` [WindowBlur](Tizen.UI.WindowBlur.md 'Tizen.UI.WindowBlur')

The first operand object.

<a name='Tizen.UI.WindowBlur.op_Equality(Tizen.UI.WindowBlur,Tizen.UI.WindowBlur).operand2'></a>

`operand2` [WindowBlur](Tizen.UI.WindowBlur.md 'Tizen.UI.WindowBlur')

The second operand object.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if both are equal, otherwise false.

<a name='Tizen.UI.WindowBlur.op_Inequality(Tizen.UI.WindowBlur,Tizen.UI.WindowBlur)'></a>

## WindowBlur.operator !=(WindowBlur, WindowBlur) Operator

Compares two WindowBlurInfo for inequality.

```csharp
public static bool operator !=(Tizen.UI.WindowBlur operand1, Tizen.UI.WindowBlur operand2);
```
#### Parameters

<a name='Tizen.UI.WindowBlur.op_Inequality(Tizen.UI.WindowBlur,Tizen.UI.WindowBlur).operand1'></a>

`operand1` [WindowBlur](Tizen.UI.WindowBlur.md 'Tizen.UI.WindowBlur')

The first operand object.

<a name='Tizen.UI.WindowBlur.op_Inequality(Tizen.UI.WindowBlur,Tizen.UI.WindowBlur).operand2'></a>

`operand2` [WindowBlur](Tizen.UI.WindowBlur.md 'Tizen.UI.WindowBlur')

The second operand object.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if both are not equal, otherwise false.






