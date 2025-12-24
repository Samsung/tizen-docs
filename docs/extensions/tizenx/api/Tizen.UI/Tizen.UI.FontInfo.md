### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## FontInfo Struct

A struct to pass data of FontInfo PropertyMap.

```csharp
public struct FontInfo :
System.IEquatable&lt;Tizen.UI.FontInfo>
```

Implements [System.IEquatable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1 'System.IEquatable`1')[FontInfo](Tizen.UI.FontInfo.md 'Tizen.UI.FontInfo')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1 'System.IEquatable`1')
### Properties

<a name='Tizen.UI.FontInfo.Family'></a>

## FontInfo.Family Property

The FontFamily of the font.

```csharp
public string Family { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.FontInfo.Path'></a>

## FontInfo.Path Property

The FontPath of the font.

```csharp
public string Path { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.FontInfo.Style'></a>

## FontInfo.Style Property

The FontStyle of the font.

```csharp
public Tizen.UI.FontStyle Style { get; set; }
```

#### Property Value
[FontStyle](Tizen.UI.FontStyle.md 'Tizen.UI.FontStyle')
### Methods

<a name='Tizen.UI.FontInfo.Equals(object)'></a>

## FontInfo.Equals(object) Method

Determines whether the specified object is equal to the current object.

```csharp
public override bool Equals(object obj);
```
#### Parameters

<a name='Tizen.UI.FontInfo.Equals(object).obj'></a>

`obj` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The object to compare with the current object.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if equal FontInfo, else false.

<a name='Tizen.UI.FontInfo.Equals(Tizen.UI.FontInfo)'></a>

## FontInfo.Equals(FontInfo) Method

Determines whether the specified object is equal to the current object.

```csharp
public bool Equals(Tizen.UI.FontInfo other);
```
#### Parameters

<a name='Tizen.UI.FontInfo.Equals(Tizen.UI.FontInfo).other'></a>

`other` [FontInfo](Tizen.UI.FontInfo.md 'Tizen.UI.FontInfo')

The FontInfo to compare with the current FontInfo.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if equal FontInfo, else false.

<a name='Tizen.UI.FontInfo.GetHashCode()'></a>

## FontInfo.GetHashCode() Method

Gets the hash code of this FontInfo.

```csharp
public override int GetHashCode();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The hash code.
### Operators

<a name='Tizen.UI.FontInfo.op_Equality(Tizen.UI.FontInfo,Tizen.UI.FontInfo)'></a>

## FontInfo.operator ==(FontInfo, FontInfo) Operator

The == operator.

```csharp
public static bool operator ==(Tizen.UI.FontInfo lhsFontInfo, Tizen.UI.FontInfo rhsFontInfo);
```
#### Parameters

<a name='Tizen.UI.FontInfo.op_Equality(Tizen.UI.FontInfo,Tizen.UI.FontInfo).lhsFontInfo'></a>

`lhsFontInfo` [FontInfo](Tizen.UI.FontInfo.md 'Tizen.UI.FontInfo')

FontInfo to compare

<a name='Tizen.UI.FontInfo.op_Equality(Tizen.UI.FontInfo,Tizen.UI.FontInfo).rhsFontInfo'></a>

`rhsFontInfo` [FontInfo](Tizen.UI.FontInfo.md 'Tizen.UI.FontInfo')

FontInfo to be compared

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if FontInfos are equal

<a name='Tizen.UI.FontInfo.op_Inequality(Tizen.UI.FontInfo,Tizen.UI.FontInfo)'></a>

## FontInfo.operator !=(FontInfo, FontInfo) Operator

The != operator.

```csharp
public static bool operator !=(Tizen.UI.FontInfo lhsFontInfo, Tizen.UI.FontInfo rhsFontInfo);
```
#### Parameters

<a name='Tizen.UI.FontInfo.op_Inequality(Tizen.UI.FontInfo,Tizen.UI.FontInfo).lhsFontInfo'></a>

`lhsFontInfo` [FontInfo](Tizen.UI.FontInfo.md 'Tizen.UI.FontInfo')

FontInfo to compare

<a name='Tizen.UI.FontInfo.op_Inequality(Tizen.UI.FontInfo,Tizen.UI.FontInfo).rhsFontInfo'></a>

`rhsFontInfo` [FontInfo](Tizen.UI.FontInfo.md 'Tizen.UI.FontInfo')

FontInfo to be compared

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
true if FontInfos are not equal






