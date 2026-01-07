### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## Color Struct

Defines a color with red, green, blue, and alpha components.

```csharp
public struct Color :
Tizen.UI.IToken,
System.IEquatable&lt;Tizen.UI.Color>
```

Implements [IToken](Tizen.UI.IToken.md 'Tizen.UI.IToken'), [System.IEquatable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1 'System.IEquatable`1')[Color](Tizen.UI.Color.md 'Tizen.UI.Color')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1 'System.IEquatable`1')
### Constructors

<a name='Tizen.UI.Color.Color(float)'></a>

## Color(float) Constructor

Initializes a new instance of the [Color](Tizen.UI.Color.md 'Tizen.UI.Color') struct.

```csharp
public Color(float value);
```
#### Parameters

<a name='Tizen.UI.Color.Color(float).value'></a>

`value` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The value of the red, green, and blue components.

<a name='Tizen.UI.Color.Color(float,float,float)'></a>

## Color(float, float, float) Constructor

Initializes a new instance of the [Color](Tizen.UI.Color.md 'Tizen.UI.Color') struct.

```csharp
public Color(float r, float g, float b);
```
#### Parameters

<a name='Tizen.UI.Color.Color(float,float,float).r'></a>

`r` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The red component.

<a name='Tizen.UI.Color.Color(float,float,float).g'></a>

`g` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The green component.

<a name='Tizen.UI.Color.Color(float,float,float).b'></a>

`b` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The blue component.

<a name='Tizen.UI.Color.Color(float,float,float,float)'></a>

## Color(float, float, float, float) Constructor

Initializes a new instance of the [Color](Tizen.UI.Color.md 'Tizen.UI.Color') struct.

```csharp
public Color(float r, float g, float b, float a);
```
#### Parameters

<a name='Tizen.UI.Color.Color(float,float,float,float).r'></a>

`r` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The red component.

<a name='Tizen.UI.Color.Color(float,float,float,float).g'></a>

`g` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The green component.

<a name='Tizen.UI.Color.Color(float,float,float,float).b'></a>

`b` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The blue component.

<a name='Tizen.UI.Color.Color(float,float,float,float).a'></a>

`a` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The alpha component.

<a name='Tizen.UI.Color.Color(uint,float)'></a>

## Color(uint, float) Constructor

Initializes a new instance of the [Color](Tizen.UI.Color.md 'Tizen.UI.Color') struct.

```csharp
public Color(uint value, float alpha);
```
#### Parameters

<a name='Tizen.UI.Color.Color(uint,float).value'></a>

`value` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The value of 0xRRGGBB format.

<a name='Tizen.UI.Color.Color(uint,float).alpha'></a>

`alpha` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The alpha value between 0.0 and 1.0.
### Properties

<a name='Tizen.UI.Color.A'></a>

## Color.A Property

Gets the alpha component of the color.

```csharp
public float A { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Color.B'></a>

## Color.B Property

Gets the blue component of the color.

```csharp
public float B { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Color.Default'></a>

## Color.Default Property

The default color.

```csharp
public static Tizen.UI.Color Default { get; }
```

#### Property Value
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')

<a name='Tizen.UI.Color.G'></a>

## Color.G Property

Gets the green component of the color.

```csharp
public float G { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Color.Hue'></a>

## Color.Hue Property

Gets the hue component of the color.

```csharp
public float Hue { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Color.Id'></a>

## Color.Id Property

Gets the unique identifier of the token.

```csharp
public string Id { get; }
```

Implements [Id](Tizen.UI.IToken.md#Tizen.UI.IToken.Id 'Tizen.UI.IToken.Id')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Color.IsToken'></a>

## Color.IsToken Property

Whether this is token.

```csharp
public readonly bool IsToken { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Color.Luminosity'></a>

## Color.Luminosity Property

Gets the luminosity component of the color.

```csharp
public float Luminosity { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Color.R'></a>

## Color.R Property

Gets the red component of the color.

```csharp
public float R { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Color.Saturation'></a>

## Color.Saturation Property

Gets the saturation component of the color.

```csharp
public float Saturation { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.Color.AddLuminosity(float)'></a>

## Color.AddLuminosity(float) Method

Adds the specified delta to the luminosity component of the color.

```csharp
public Tizen.UI.Color AddLuminosity(float delta);
```
#### Parameters

<a name='Tizen.UI.Color.AddLuminosity(float).delta'></a>

`delta` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The value to add to the luminosity component.

#### Returns
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')  
The new color.

<a name='Tizen.UI.Color.Equals(object)'></a>

## Color.Equals(object) Method

Indicates whether this instance and a specified object are equal.

```csharp
public override bool Equals(object obj);
```
#### Parameters

<a name='Tizen.UI.Color.Equals(object).obj'></a>

`obj` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The object to compare with the current instance.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if obj and this instance are the same type and represent the same value; otherwise, false.

<a name='Tizen.UI.Color.Equals(Tizen.UI.Color)'></a>

## Color.Equals(Color) Method

Indicates whether the current object is equal to another object of the same type.

```csharp
public bool Equals(Tizen.UI.Color color);
```
#### Parameters

<a name='Tizen.UI.Color.Equals(Tizen.UI.Color).color'></a>

`color` [Color](Tizen.UI.Color.md 'Tizen.UI.Color')

The color to compare with the current instance.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if obj and this instance are the same type and represent the same value; otherwise, false.

<a name='Tizen.UI.Color.FromHex(string)'></a>

## Color.FromHex(string) Method

Converts a hexadecimal string to a Color object.

```csharp
public static Tizen.UI.Color FromHex(string hex);
```
#### Parameters

<a name='Tizen.UI.Color.FromHex(string).hex'></a>

`hex` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The hexadecimal string to convert. The string can be in the formats #rgb, #argb, #rrggbb, or #aarrggbb.

#### Returns
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')  
A Color object representing the hexadecimal string.

<a name='Tizen.UI.Color.FromHsla(float,float,float,float)'></a>

## Color.FromHsla(float, float, float, float) Method

Creates a new Color object from hue, saturation, lightness, and alpha values.

```csharp
public static Tizen.UI.Color FromHsla(float h, float s, float l, float a=1f);
```
#### Parameters

<a name='Tizen.UI.Color.FromHsla(float,float,float,float).h'></a>

`h` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The hue value of the color.

<a name='Tizen.UI.Color.FromHsla(float,float,float,float).s'></a>

`s` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The saturation value of the color.

<a name='Tizen.UI.Color.FromHsla(float,float,float,float).l'></a>

`l` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The lightness value of the color.

<a name='Tizen.UI.Color.FromHsla(float,float,float,float).a'></a>

`a` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The alpha value of the color.

#### Returns
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')  
A new Color object with the specified hue, saturation, lightness, and alpha values.

<a name='Tizen.UI.Color.FromHsv(float,float,float)'></a>

## Color.FromHsv(float, float, float) Method

Creates a new Color object from the specified HSV values.

```csharp
public static Tizen.UI.Color FromHsv(float h, float s, float v);
```
#### Parameters

<a name='Tizen.UI.Color.FromHsv(float,float,float).h'></a>

`h` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The hue component of the color, ranging from 0 to 1.

<a name='Tizen.UI.Color.FromHsv(float,float,float).s'></a>

`s` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The saturation component of the color, ranging from 0 to 1.

<a name='Tizen.UI.Color.FromHsv(float,float,float).v'></a>

`v` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The value component of the color, ranging from 0 to 1.

#### Returns
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')  
A new Color object with the specified HSV values.

<a name='Tizen.UI.Color.FromHsv(int,int,int)'></a>

## Color.FromHsv(int, int, int) Method

Creates a new Color object from the specified HSV values.

```csharp
public static Tizen.UI.Color FromHsv(int h, int s, int v);
```
#### Parameters

<a name='Tizen.UI.Color.FromHsv(int,int,int).h'></a>

`h` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The hue component of the color, ranging from 0 to 360.

<a name='Tizen.UI.Color.FromHsv(int,int,int).s'></a>

`s` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The saturation component of the color, ranging from 0 to 100.

<a name='Tizen.UI.Color.FromHsv(int,int,int).v'></a>

`v` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The value component of the color, ranging from 0 to 100.

#### Returns
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')  
A new Color object with the specified HSV values.

<a name='Tizen.UI.Color.FromHsva(float,float,float,float)'></a>

## Color.FromHsva(float, float, float, float) Method

Creates a new Color object from the specified HSVA values.

```csharp
public static Tizen.UI.Color FromHsva(float h, float s, float v, float a);
```
#### Parameters

<a name='Tizen.UI.Color.FromHsva(float,float,float,float).h'></a>

`h` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The hue component of the color, in the range [0, 1].

<a name='Tizen.UI.Color.FromHsva(float,float,float,float).s'></a>

`s` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The saturation component of the color, in the range [0, 1].

<a name='Tizen.UI.Color.FromHsva(float,float,float,float).v'></a>

`v` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The value component of the color, in the range [0, 1].

<a name='Tizen.UI.Color.FromHsva(float,float,float,float).a'></a>

`a` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The alpha component of the color, in the range [0, 1].

#### Returns
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')  
A new Color object with the specified HSVA values.

<a name='Tizen.UI.Color.FromHsva(int,int,int,int)'></a>

## Color.FromHsva(int, int, int, int) Method

Creates a new Color object from the specified HSVA values.

```csharp
public static Tizen.UI.Color FromHsva(int h, int s, int v, int a);
```
#### Parameters

<a name='Tizen.UI.Color.FromHsva(int,int,int,int).h'></a>

`h` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The hue component of the color, ranging from 0 to 360.

<a name='Tizen.UI.Color.FromHsva(int,int,int,int).s'></a>

`s` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The saturation component of the color, ranging from 0 to 100.

<a name='Tizen.UI.Color.FromHsva(int,int,int,int).v'></a>

`v` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The value component of the color, ranging from 0 to 100.

<a name='Tizen.UI.Color.FromHsva(int,int,int,int).a'></a>

`a` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The alpha component of the color, ranging from 0 to 100.

#### Returns
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')  
A new Color object with the specified HSVA values.

<a name='Tizen.UI.Color.FromRgb(float,float,float)'></a>

## Color.FromRgb(float, float, float) Method

Creates a new Color object from red, green, and blue values.

```csharp
public static Tizen.UI.Color FromRgb(float r, float g, float b);
```
#### Parameters

<a name='Tizen.UI.Color.FromRgb(float,float,float).r'></a>

`r` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The red value of the color.

<a name='Tizen.UI.Color.FromRgb(float,float,float).g'></a>

`g` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The green value of the color.

<a name='Tizen.UI.Color.FromRgb(float,float,float).b'></a>

`b` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The blue value of the color.

#### Returns
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')  
A new Color object with the specified red, green, and blue values.

<a name='Tizen.UI.Color.FromRgb(int,int,int)'></a>

## Color.FromRgb(int, int, int) Method

Creates a new Color object from red, green, and blue values.

```csharp
public static Tizen.UI.Color FromRgb(int r, int g, int b);
```
#### Parameters

<a name='Tizen.UI.Color.FromRgb(int,int,int).r'></a>

`r` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The red value of the color.

<a name='Tizen.UI.Color.FromRgb(int,int,int).g'></a>

`g` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The green value of the color.

<a name='Tizen.UI.Color.FromRgb(int,int,int).b'></a>

`b` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The blue value of the color.

#### Returns
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')  
A new Color object with the specified red, green, and blue values.

<a name='Tizen.UI.Color.FromRgba(float,float,float,float)'></a>

## Color.FromRgba(float, float, float, float) Method

Creates a new Color object from red, green, blue, and alpha values.

```csharp
public static Tizen.UI.Color FromRgba(float r, float g, float b, float a);
```
#### Parameters

<a name='Tizen.UI.Color.FromRgba(float,float,float,float).r'></a>

`r` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The red value of the color.

<a name='Tizen.UI.Color.FromRgba(float,float,float,float).g'></a>

`g` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The green value of the color.

<a name='Tizen.UI.Color.FromRgba(float,float,float,float).b'></a>

`b` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The blue value of the color.

<a name='Tizen.UI.Color.FromRgba(float,float,float,float).a'></a>

`a` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The alpha value of the color.

#### Returns
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')  
A new Color object with the specified red, green, blue, and alpha values.

<a name='Tizen.UI.Color.FromRgba(int,int,int,int)'></a>

## Color.FromRgba(int, int, int, int) Method

Creates a new Color object from red, green, blue, and alpha values.

```csharp
public static Tizen.UI.Color FromRgba(int r, int g, int b, int a);
```
#### Parameters

<a name='Tizen.UI.Color.FromRgba(int,int,int,int).r'></a>

`r` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The red value of the color.

<a name='Tizen.UI.Color.FromRgba(int,int,int,int).g'></a>

`g` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The green value of the color.

<a name='Tizen.UI.Color.FromRgba(int,int,int,int).b'></a>

`b` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The blue value of the color.

<a name='Tizen.UI.Color.FromRgba(int,int,int,int).a'></a>

`a` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The alpha value of the color.

#### Returns
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')  
A new Color object with the specified red, green, blue, and alpha values.

<a name='Tizen.UI.Color.GetHashCode()'></a>

## Color.GetHashCode() Method

Returns a hash code for this instance.

```csharp
public override int GetHashCode();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.

<a name='Tizen.UI.Color.MultiplyAlpha(float)'></a>

## Color.MultiplyAlpha(float) Method

Multiplies the alpha component of the color by the specified value.

```csharp
public Tizen.UI.Color MultiplyAlpha(float alpha);
```
#### Parameters

<a name='Tizen.UI.Color.MultiplyAlpha(float).alpha'></a>

`alpha` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The value to multiply the alpha component by.

#### Returns
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')  
The new color.

<a name='Tizen.UI.Color.ToHex()'></a>

## Color.ToHex() Method

Converts the color to a hexadecimal string representation.

```csharp
public string ToHex();
```

#### Returns
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
The hexadecimal string representation of the color.

<a name='Tizen.UI.Color.Token(string)'></a>

## Color.Token(string) Method

Creates a new color from the token table.

```csharp
public static Tizen.UI.Color Token(string id);
```
#### Parameters

<a name='Tizen.UI.Color.Token(string).id'></a>

`id` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The unique identifier of the token.

#### Returns
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')

<a name='Tizen.UI.Color.ToString()'></a>

## Color.ToString() Method

Returns a string that represents the current object.

```csharp
public override string ToString();
```

#### Returns
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
A string that represents the current object.

<a name='Tizen.UI.Color.WithAlpha(float)'></a>

## Color.WithAlpha(float) Method

Returns a new Color object with the specified alpha value.

```csharp
public Tizen.UI.Color WithAlpha(float alpha);
```
#### Parameters

<a name='Tizen.UI.Color.WithAlpha(float).alpha'></a>

`alpha` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The new alpha value.

#### Returns
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')  
A new Color object with the specified alpha value.

<a name='Tizen.UI.Color.WithHue(float)'></a>

## Color.WithHue(float) Method

Sets the hue component of the color.

```csharp
public Tizen.UI.Color WithHue(float hue);
```
#### Parameters

<a name='Tizen.UI.Color.WithHue(float).hue'></a>

`hue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The new hue component.

#### Returns
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')  
The new color.

<a name='Tizen.UI.Color.WithLuminosity(float)'></a>

## Color.WithLuminosity(float) Method

Sets the luminosity component of the color.

```csharp
public Tizen.UI.Color WithLuminosity(float luminosity);
```
#### Parameters

<a name='Tizen.UI.Color.WithLuminosity(float).luminosity'></a>

`luminosity` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The new luminosity component.

#### Returns
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')  
The new color.

<a name='Tizen.UI.Color.WithSaturation(float)'></a>

## Color.WithSaturation(float) Method

Sets the saturation component of the color.

```csharp
public Tizen.UI.Color WithSaturation(float saturation);
```
#### Parameters

<a name='Tizen.UI.Color.WithSaturation(float).saturation'></a>

`saturation` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The new saturation component.

#### Returns
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')  
The new color.
### Operators

<a name='Tizen.UI.Color.op_Equality(Tizen.UI.Color,Tizen.UI.Color)'></a>

## Color.operator ==(Color, Color) Operator

Compares two Color objects for equality.

```csharp
public static bool operator ==(Tizen.UI.Color color1, Tizen.UI.Color color2);
```
#### Parameters

<a name='Tizen.UI.Color.op_Equality(Tizen.UI.Color,Tizen.UI.Color).color1'></a>

`color1` [Color](Tizen.UI.Color.md 'Tizen.UI.Color')

The first Color object to compare.

<a name='Tizen.UI.Color.op_Equality(Tizen.UI.Color,Tizen.UI.Color).color2'></a>

`color2` [Color](Tizen.UI.Color.md 'Tizen.UI.Color')

The second Color object to compare.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if both objects are equal, otherwise false.

<a name='Tizen.UI.Color.op_Inequality(Tizen.UI.Color,Tizen.UI.Color)'></a>

## Color.operator !=(Color, Color) Operator

Compares two Color objects for inequality.

```csharp
public static bool operator !=(Tizen.UI.Color color1, Tizen.UI.Color color2);
```
#### Parameters

<a name='Tizen.UI.Color.op_Inequality(Tizen.UI.Color,Tizen.UI.Color).color1'></a>

`color1` [Color](Tizen.UI.Color.md 'Tizen.UI.Color')

The first Color object to compare.

<a name='Tizen.UI.Color.op_Inequality(Tizen.UI.Color,Tizen.UI.Color).color2'></a>

`color2` [Color](Tizen.UI.Color.md 'Tizen.UI.Color')

The second Color object to compare.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if both objects are not equal, otherwise false.






