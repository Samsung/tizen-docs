### [Tizen.UI.NativeHandle](Tizen.UI.NativeHandle.md 'Tizen.UI.NativeHandle')

## PropertyValueHandleExtensions Class

Provides extension methods for converting objects to PropertyValue types.

```csharp
public static class PropertyValueHandleExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; PropertyValueHandleExtensions
### Methods

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToColor(thisTizen.UI.NativeHandle.PropertyValueHandle)'></a>

## PropertyValueHandleExtensions.ToColor(this PropertyValueHandle) Method

Extension method for converting a PropertyValueHandle to a Color.

```csharp
public static Tizen.UI.Color ToColor(this Tizen.UI.NativeHandle.PropertyValueHandle handle);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToColor(thisTizen.UI.NativeHandle.PropertyValueHandle).handle'></a>

`handle` [PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')

The PropertyValueHandle object to convert.

#### Returns
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')  
The Color representation of the PropertyValueHandle.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToCornerRadius(thisTizen.UI.NativeHandle.PropertyValueHandle)'></a>

## PropertyValueHandleExtensions.ToCornerRadius(this PropertyValueHandle) Method

Extension method for converting a PropertyValueHandle to a CornerRadius.

```csharp
public static Tizen.UI.CornerRadius ToCornerRadius(this Tizen.UI.NativeHandle.PropertyValueHandle handle);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToCornerRadius(thisTizen.UI.NativeHandle.PropertyValueHandle).handle'></a>

`handle` [PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')

The PropertyValueHandle object to convert.

#### Returns
[CornerRadius](Tizen.UI.CornerRadius.md 'Tizen.UI.CornerRadius')  
The CornerRadius representation of the PropertyValueHandle.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToFloat(thisTizen.UI.NativeHandle.PropertyValueHandle)'></a>

## PropertyValueHandleExtensions.ToFloat(this PropertyValueHandle) Method

Extension method for converting a PropertyValueHandle object to a float value.

```csharp
public static float ToFloat(this Tizen.UI.NativeHandle.PropertyValueHandle handle);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToFloat(thisTizen.UI.NativeHandle.PropertyValueHandle).handle'></a>

`handle` [PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')

The PropertyValueHandle object to convert.

#### Returns
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')  
The float value represented by the PropertyValueHandle object.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToInt(thisTizen.UI.NativeHandle.PropertyValueHandle)'></a>

## PropertyValueHandleExtensions.ToInt(this PropertyValueHandle) Method

Extension method for converting a PropertyValueHandle to an integer value.

```csharp
public static int ToInt(this Tizen.UI.NativeHandle.PropertyValueHandle handle);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToInt(thisTizen.UI.NativeHandle.PropertyValueHandle).handle'></a>

`handle` [PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')

The PropertyValueHandle object to convert.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The integer value represented by the PropertyValueHandle.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToRectangleValue(thisTizen.UI.Thickness)'></a>

## PropertyValueHandleExtensions.ToRectangleValue(this Thickness) Method

Extension method for converting a Thickness struct into a PropertyValueHandle (Rect).

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle ToRectangleValue(this Tizen.UI.Thickness value);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToRectangleValue(thisTizen.UI.Thickness).value'></a>

`value` [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

The Thickness struct to convert.

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
A new PropertyValueHandle (Rect) containing the converted Thickness struct.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToStr(thisTizen.UI.NativeHandle.PropertyValueHandle)'></a>

## PropertyValueHandleExtensions.ToStr(this PropertyValueHandle) Method

Extension method for converting a PropertyValueHandle to a string.

```csharp
public static string ToStr(this Tizen.UI.NativeHandle.PropertyValueHandle handle);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToStr(thisTizen.UI.NativeHandle.PropertyValueHandle).handle'></a>

`handle` [PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')

The PropertyValueHandle object to convert.

#### Returns
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
The string representation of the PropertyValueHandle.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisbool)'></a>

## PropertyValueHandleExtensions.ToValue(this bool) Method

Creates a new PropertyValue handle from the given boolean value.

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle ToValue(this bool value);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisbool).value'></a>

`value` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

The boolean value to convert.

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
A new PropertyValue handle representing the boolean value.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisint)'></a>

## PropertyValueHandleExtensions.ToValue(this int) Method

Extension method for converting an integer value to a PropertyValueHandle object.

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle ToValue(this int value);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisint).value'></a>

`value` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The integer value to be converted.

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
A new PropertyValueHandle object containing the integer value.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisobject,bool)'></a>

## PropertyValueHandleExtensions.ToValue(this object, bool) Method

Converts an object to a PropertyValueHandle.

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle ToValue(this object value, bool useVector3=false);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisobject,bool).value'></a>

`value` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The object to convert.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisobject,bool).useVector3'></a>

`useVector3` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
A new PropertyValueHandle containing the converted value.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.AutoFontSize)'></a>

## PropertyValueHandleExtensions.ToValue(this AutoFontSize) Method

Converts an AutoFontSize to a PropertyValue.

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle ToValue(this Tizen.UI.AutoFontSize autoSize);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.AutoFontSize).autoSize'></a>

`autoSize` [AutoFontSize](Tizen.UI.AutoFontSize.md 'Tizen.UI.AutoFontSize')

The AutoFontSize to convert.

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
A PropertyValue containing the same data as the AutoFontSize.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Background)'></a>

## PropertyValueHandleExtensions.ToValue(this Background) Method

Converts a Background to a PropertyValue.

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle ToValue(this Tizen.UI.Background background);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Background).background'></a>

`background` [Background](Tizen.UI.Background.md 'Tizen.UI.Background')

The Background to convert.

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
A PropertyValue containing the same data as the Background.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Color)'></a>

## PropertyValueHandleExtensions.ToValue(this Color) Method

Extension method for converting a Color object to a PropertyValueHandle object.

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle ToValue(this Tizen.UI.Color color);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Color).color'></a>

`color` [Color](Tizen.UI.Color.md 'Tizen.UI.Color')

The Color object to be converted.

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
A new PropertyValueHandle object representing the given Color.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Color,bool)'></a>

## PropertyValueHandleExtensions.ToValue(this Color, bool) Method

Extension method for converting a Color object to a PropertyValueHandle object.

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle ToValue(this Tizen.UI.Color color, bool useVector3);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Color,bool).color'></a>

`color` [Color](Tizen.UI.Color.md 'Tizen.UI.Color')

The Color object to be converted.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Color,bool).useVector3'></a>

`useVector3` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
A new PropertyValueHandle object representing the given Color.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.CornerRadius)'></a>

## PropertyValueHandleExtensions.ToValue(this CornerRadius) Method

Converts a [CornerRadius](Tizen.UI.CornerRadius.md 'Tizen.UI.CornerRadius') struct into a [PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle') object.

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle ToValue(this Tizen.UI.CornerRadius value);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.CornerRadius).value'></a>

`value` [CornerRadius](Tizen.UI.CornerRadius.md 'Tizen.UI.CornerRadius')

The [CornerRadius](Tizen.UI.CornerRadius.md 'Tizen.UI.CornerRadius') struct to convert.

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
A new [PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle') object representing the given [CornerRadius](Tizen.UI.CornerRadius.md 'Tizen.UI.CornerRadius') struct.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.HiddenInputSetting)'></a>

## PropertyValueHandleExtensions.ToValue(this HiddenInputSetting) Method

Converts a HiddenInputSetting to a PropertyValue.

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle ToValue(this Tizen.UI.HiddenInputSetting setting);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.HiddenInputSetting).setting'></a>

`setting` [HiddenInputSetting](Tizen.UI.HiddenInputSetting.md 'Tizen.UI.HiddenInputSetting')

The HiddenInputSetting to convert.

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
A PropertyValue containing the same data as the HiddenInputSetting.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.InputMethodSetting)'></a>

## PropertyValueHandleExtensions.ToValue(this InputMethodSetting) Method

Converts an InputMethodSetting to a PropertyValue.

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle ToValue(this Tizen.UI.InputMethodSetting setting);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.InputMethodSetting).setting'></a>

`setting` [InputMethodSetting](Tizen.UI.InputMethodSetting.md 'Tizen.UI.InputMethodSetting')

The InputMethodSetting to convert.

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
A PropertyValue containing the same data as the InputMethodSetting.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.NativeHandle.PropertyArrayHandle)'></a>

## PropertyValueHandleExtensions.ToValue(this PropertyArrayHandle) Method

Converts a PropertyArray to a PropertyValue.

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle ToValue(this Tizen.UI.NativeHandle.PropertyArrayHandle handle);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.NativeHandle.PropertyArrayHandle).handle'></a>

`handle` [PropertyArrayHandle](Tizen.UI.NativeHandle.PropertyArrayHandle.md 'Tizen.UI.NativeHandle.PropertyArrayHandle')

The PropertyArray to convert.

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
A PropertyValue containing the same data as the PropertyArray.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.NativeHandle.PropertyMapHandle)'></a>

## PropertyValueHandleExtensions.ToValue(this PropertyMapHandle) Method

Converts a PropertyMap to a PropertyValue.

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle ToValue(this Tizen.UI.NativeHandle.PropertyMapHandle handle);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.NativeHandle.PropertyMapHandle).handle'></a>

`handle` [PropertyMapHandle](Tizen.UI.NativeHandle.PropertyMapHandle.md 'Tizen.UI.NativeHandle.PropertyMapHandle')

The PropertyMap to convert.

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
A PropertyValue containing the same data as the PropertyMap.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Outline)'></a>

## PropertyValueHandleExtensions.ToValue(this Outline) Method

Converts an Outline to a PropertyValue.

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle ToValue(this Tizen.UI.Outline outline);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Outline).outline'></a>

`outline` [Outline](Tizen.UI.Outline.md 'Tizen.UI.Outline')

The Outline to convert.

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
A PropertyValue containing the same data as the Outline.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Point,bool)'></a>

## PropertyValueHandleExtensions.ToValue(this Point, bool) Method

Extension method for converting a Point object to a PropertyValueHandle object.

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle ToValue(this Tizen.UI.Point value, bool useVector3=false);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Point,bool).value'></a>

`value` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The Position object to be converted.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Point,bool).useVector3'></a>

`useVector3` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Indicates whether to use Vector3 or not.

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
A new PropertyValueHandle object representing the given Position object.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Rect)'></a>

## PropertyValueHandleExtensions.ToValue(this Rect) Method

Extension method for converting a Rect struct into a PropertyValueHandle.

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle ToValue(this Tizen.UI.Rect value);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Rect).value'></a>

`value` [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

The Rect struct to be converted.

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
A new PropertyValueHandle containing the converted data.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Shadow)'></a>

## PropertyValueHandleExtensions.ToValue(this Shadow) Method

Converts a Shadow to a PropertyValue.

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle ToValue(this Tizen.UI.Shadow shadow);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Shadow).shadow'></a>

`shadow` [Shadow](Tizen.UI.Shadow.md 'Tizen.UI.Shadow')

The Shadow to convert.

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
A PropertyValue containing the same data as the Shadow.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Size)'></a>

## PropertyValueHandleExtensions.ToValue(this Size) Method

Extension method for converting a Size struct to a PropertyValueHandle.

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle ToValue(this Tizen.UI.Size value);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Size).value'></a>

`value` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The Size struct to convert.

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
A new PropertyValueHandle containing the converted value.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.TextShadow)'></a>

## PropertyValueHandleExtensions.ToValue(this TextShadow) Method

Converts a TextShadow to a PropertyValue.

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle ToValue(this Tizen.UI.TextShadow shadow);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.TextShadow).shadow'></a>

`shadow` [TextShadow](Tizen.UI.TextShadow.md 'Tizen.UI.TextShadow')

The TextShadow to convert.

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
A PropertyValue containing the same data as the TextShadow.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Thickness)'></a>

## PropertyValueHandleExtensions.ToValue(this Thickness) Method

Extension method for converting a Thickness struct into a PropertyValueHandle (Vector4).

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle ToValue(this Tizen.UI.Thickness value);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Thickness).value'></a>

`value` [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

The Thickness struct to convert.

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
A new PropertyValueHandle (Vector4) containing the converted Thickness struct.

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Underline)'></a>

## PropertyValueHandleExtensions.ToValue(this Underline) Method

Converts an Underline to a PropertyValue.

```csharp
public static Tizen.UI.NativeHandle.PropertyValueHandle ToValue(this Tizen.UI.Underline underline);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.PropertyValueHandleExtensions.ToValue(thisTizen.UI.Underline).underline'></a>

`underline` [Underline](Tizen.UI.Underline.md 'Tizen.UI.Underline')

The Underline to convert.

#### Returns
[PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')  
A PropertyValue containing the same data as the Underline.




