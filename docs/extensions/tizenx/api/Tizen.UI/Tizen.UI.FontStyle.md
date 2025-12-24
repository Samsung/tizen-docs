### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## FontStyle Struct

A struct to pass data of FontStyle PropertyMap. <br/>

```csharp
public struct FontStyle :
System.IEquatable&lt;Tizen.UI.FontStyle>
```

Implements [System.IEquatable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1 'System.IEquatable`1')[FontStyle](Tizen.UI.FontStyle.md 'Tizen.UI.FontStyle')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1 'System.IEquatable`1')

### Remarks
The FontStyle struct is used as an argument to SetFontStyle and GetFontStyle methods. <br/>
### Properties

<a name='Tizen.UI.FontStyle.Slant'></a>

## FontStyle.Slant Property

The Slant defines whether to use italics.

```csharp
public Tizen.UI.FontSlant Slant { get; set; }
```

#### Property Value
[FontSlant](Tizen.UI.FontSlant.md 'Tizen.UI.FontSlant')

<a name='Tizen.UI.FontStyle.Weight'></a>

## FontStyle.Weight Property

The Weight defines the thickness or darkness of the glyphs.

```csharp
public Tizen.UI.FontWeight Weight { get; set; }
```

#### Property Value
[FontWeight](Tizen.UI.FontWeight.md 'Tizen.UI.FontWeight')

<a name='Tizen.UI.FontStyle.Width'></a>

## FontStyle.Width Property

The Width defines occupied by each glyph.

```csharp
public Tizen.UI.FontWidth Width { get; set; }
```

#### Property Value
[FontWidth](Tizen.UI.FontWidth.md 'Tizen.UI.FontWidth')
### Methods

<a name='Tizen.UI.FontStyle.Equals(object)'></a>

## FontStyle.Equals(object) Method

Determines whether the specified object is equal to the current object.

```csharp
public override bool Equals(object obj);
```
#### Parameters

<a name='Tizen.UI.FontStyle.Equals(object).obj'></a>

`obj` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The object to compare with the current object.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if equal FontStyle, else false.

<a name='Tizen.UI.FontStyle.Equals(Tizen.UI.FontStyle)'></a>

## FontStyle.Equals(FontStyle) Method

Determines whether the specified object is equal to the current object.

```csharp
public bool Equals(Tizen.UI.FontStyle other);
```
#### Parameters

<a name='Tizen.UI.FontStyle.Equals(Tizen.UI.FontStyle).other'></a>

`other` [FontStyle](Tizen.UI.FontStyle.md 'Tizen.UI.FontStyle')

The FontStyle to compare with the current FontStyle.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if equal FontStyle, else false.

<a name='Tizen.UI.FontStyle.GetHashCode()'></a>

## FontStyle.GetHashCode() Method

Gets the hash code of this FontStyle.

```csharp
public override int GetHashCode();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The hash code.
### Operators

<a name='Tizen.UI.FontStyle.op_Equality(Tizen.UI.FontStyle,Tizen.UI.FontStyle)'></a>

## FontStyle.operator ==(FontStyle, FontStyle) Operator

The == operator.

```csharp
public static bool operator ==(Tizen.UI.FontStyle lhsFontStyle, Tizen.UI.FontStyle rhsFontStyle);
```
#### Parameters

<a name='Tizen.UI.FontStyle.op_Equality(Tizen.UI.FontStyle,Tizen.UI.FontStyle).lhsFontStyle'></a>

`lhsFontStyle` [FontStyle](Tizen.UI.FontStyle.md 'Tizen.UI.FontStyle')

FontStyle to compare

<a name='Tizen.UI.FontStyle.op_Equality(Tizen.UI.FontStyle,Tizen.UI.FontStyle).rhsFontStyle'></a>

`rhsFontStyle` [FontStyle](Tizen.UI.FontStyle.md 'Tizen.UI.FontStyle')

FontStyle to be compared

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if FontStyles are equal

<a name='Tizen.UI.FontStyle.op_Inequality(Tizen.UI.FontStyle,Tizen.UI.FontStyle)'></a>

## FontStyle.operator !=(FontStyle, FontStyle) Operator

The != operator.

```csharp
public static bool operator !=(Tizen.UI.FontStyle lhsFontStyle, Tizen.UI.FontStyle rhsFontStyle);
```
#### Parameters

<a name='Tizen.UI.FontStyle.op_Inequality(Tizen.UI.FontStyle,Tizen.UI.FontStyle).lhsFontStyle'></a>

`lhsFontStyle` [FontStyle](Tizen.UI.FontStyle.md 'Tizen.UI.FontStyle')

FontStyle to compare

<a name='Tizen.UI.FontStyle.op_Inequality(Tizen.UI.FontStyle,Tizen.UI.FontStyle).rhsFontStyle'></a>

`rhsFontStyle` [FontStyle](Tizen.UI.FontStyle.md 'Tizen.UI.FontStyle')

FontStyle to be compared

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if FontStyles are not equal






