### [Tizen.UI.NativeHandle](Tizen.UI.NativeHandle.md 'Tizen.UI.NativeHandle')

## NativeHandleExtensions Class

Provides extension methods for converting between native types and their managed equivalents.

```csharp
public static class NativeHandleExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; NativeHandleExtensions
### Methods

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.CheckException()'></a>

## NativeHandleExtensions.CheckException() Method

Extension method for NativeHandle class to check for pending exceptions.

```csharp
public static void CheckException();
```

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.CheckException_T_(thisT)'></a>

## NativeHandleExtensions.CheckException&lt;T>(this T) Method

Extension method for NativeHandle class to check for pending exceptions.

```csharp
public static T CheckException&lt;T>(this T v);
```
#### Type parameters

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.CheckException_T_(thisT).T'></a>

`T`

The type of the object.
#### Parameters

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.CheckException_T_(thisT).v'></a>

`v` [T](Tizen.UI.NativeHandle.NativeHandleExtensions.md#Tizen.UI.NativeHandle.NativeHandleExtensions.CheckException_T_(thisT).T 'Tizen.UI.NativeHandle.NativeHandleExtensions.CheckException&lt;T>(this T).T')

The object to check for pending exceptions.

#### Returns
[T](Tizen.UI.NativeHandle.NativeHandleExtensions.md#Tizen.UI.NativeHandle.NativeHandleExtensions.CheckException_T_(thisT).T 'Tizen.UI.NativeHandle.NativeHandleExtensions.CheckException&lt;T>(this T).T')  
The original object.

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.DegreeToRadian(thisfloat)'></a>

## NativeHandleExtensions.DegreeToRadian(this float) Method

Converts the specified angle in degrees to radians.

```csharp
public static Tizen.UI.NativeHandle.RadianHandle DegreeToRadian(this float degree);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.DegreeToRadian(thisfloat).degree'></a>

`degree` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The angle in degrees to convert.

#### Returns
[RadianHandle](Tizen.UI.NativeHandle.RadianHandle.md 'Tizen.UI.NativeHandle.RadianHandle')  
The angle in radians.

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.RadianToDegree(thisfloat)'></a>

## NativeHandleExtensions.RadianToDegree(this float) Method

Converts the specified angle in radians to degrees.

```csharp
public static float RadianToDegree(this float radians);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.RadianToDegree(thisfloat).radians'></a>

`radians` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The angle in radians to convert.

#### Returns
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')  
The angle in degrees.

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToColor(thisTizen.UI.Internal.ObjectPool_Tizen.UI.NativeHandle.Vector4Handle_)'></a>

## NativeHandleExtensions.ToColor(this ObjectPool&lt;Vector4Handle>) Method

Converts the specified [Vector4Handle](Tizen.UI.NativeHandle.Vector4Handle.md 'Tizen.UI.NativeHandle.Vector4Handle') object to a [Color](Tizen.UI.Color.md 'Tizen.UI.Color') value.

```csharp
public static Tizen.UI.Color ToColor(this Tizen.UI.Internal.ObjectPool&lt;Tizen.UI.NativeHandle.Vector4Handle> vector);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToColor(thisTizen.UI.Internal.ObjectPool_Tizen.UI.NativeHandle.Vector4Handle_).vector'></a>

`vector` [Tizen.UI.Internal.ObjectPool&lt;](Tizen.UI.Internal.ObjectPool_T_.md 'Tizen.UI.Internal.ObjectPool&lt;T>')[Vector4Handle](Tizen.UI.NativeHandle.Vector4Handle.md 'Tizen.UI.NativeHandle.Vector4Handle')[&gt;](Tizen.UI.Internal.ObjectPool_T_.md 'Tizen.UI.Internal.ObjectPool&lt;T>')

The vector to convert.

#### Returns
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')  
A new [Color](Tizen.UI.Color.md 'Tizen.UI.Color') object containing the converted values.

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToColor(thisTizen.UI.NativeHandle.Vector4Handle)'></a>

## NativeHandleExtensions.ToColor(this Vector4Handle) Method

Converts the specified [Vector4Handle](Tizen.UI.NativeHandle.Vector4Handle.md 'Tizen.UI.NativeHandle.Vector4Handle') object to a [Color](Tizen.UI.Color.md 'Tizen.UI.Color') value.

```csharp
public static Tizen.UI.Color ToColor(this Tizen.UI.NativeHandle.Vector4Handle vector);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToColor(thisTizen.UI.NativeHandle.Vector4Handle).vector'></a>

`vector` [Vector4Handle](Tizen.UI.NativeHandle.Vector4Handle.md 'Tizen.UI.NativeHandle.Vector4Handle')

The vector to convert.

#### Returns
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')  
A new [Color](Tizen.UI.Color.md 'Tizen.UI.Color') object containing the converted values.

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToCornerRadius(thisTizen.UI.Internal.ObjectPool_Tizen.UI.NativeHandle.Vector4Handle_)'></a>

## NativeHandleExtensions.ToCornerRadius(this ObjectPool&lt;Vector4Handle>) Method

Converts a Vector4Handle object from an ObjectPool to a CornerRadius.

```csharp
public static Tizen.UI.CornerRadius ToCornerRadius(this Tizen.UI.Internal.ObjectPool&lt;Tizen.UI.NativeHandle.Vector4Handle> vector);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToCornerRadius(thisTizen.UI.Internal.ObjectPool_Tizen.UI.NativeHandle.Vector4Handle_).vector'></a>

`vector` [Tizen.UI.Internal.ObjectPool&lt;](Tizen.UI.Internal.ObjectPool_T_.md 'Tizen.UI.Internal.ObjectPool&lt;T>')[Vector4Handle](Tizen.UI.NativeHandle.Vector4Handle.md 'Tizen.UI.NativeHandle.Vector4Handle')[&gt;](Tizen.UI.Internal.ObjectPool_T_.md 'Tizen.UI.Internal.ObjectPool&lt;T>')

The Vector4Handle object from the ObjectPool.

#### Returns
[CornerRadius](Tizen.UI.CornerRadius.md 'Tizen.UI.CornerRadius')  
A CornerRadius object representing the corner radius values.

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToCornerRadius(thisTizen.UI.NativeHandle.Vector4Handle)'></a>

## NativeHandleExtensions.ToCornerRadius(this Vector4Handle) Method

Converts a Vector4Handle to a CornerRadius object.

```csharp
public static Tizen.UI.CornerRadius ToCornerRadius(this Tizen.UI.NativeHandle.Vector4Handle vector);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToCornerRadius(thisTizen.UI.NativeHandle.Vector4Handle).vector'></a>

`vector` [Vector4Handle](Tizen.UI.NativeHandle.Vector4Handle.md 'Tizen.UI.NativeHandle.Vector4Handle')

The Vector4Handle to convert.

#### Returns
[CornerRadius](Tizen.UI.CornerRadius.md 'Tizen.UI.CornerRadius')  
A CornerRadius object initialized with the values from the Vector4Handle.

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToNative(thisfloat)'></a>

## NativeHandleExtensions.ToNative(this float) Method

Creates a new [DegreeHandle](Tizen.UI.NativeHandle.DegreeHandle.md 'Tizen.UI.NativeHandle.DegreeHandle') object from the specified float value.

```csharp
public static Tizen.UI.NativeHandle.DegreeHandle ToNative(this float degree);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToNative(thisfloat).degree'></a>

`degree` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The angle in degrees to convert.

#### Returns
[DegreeHandle](Tizen.UI.NativeHandle.DegreeHandle.md 'Tizen.UI.NativeHandle.DegreeHandle')  
A new [DegreeHandle](Tizen.UI.NativeHandle.DegreeHandle.md 'Tizen.UI.NativeHandle.DegreeHandle') object containing the float values.

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToNative(thisTizen.UI.Color)'></a>

## NativeHandleExtensions.ToNative(this Color) Method

Creates a new [Vector4Handle](Tizen.UI.NativeHandle.Vector4Handle.md 'Tizen.UI.NativeHandle.Vector4Handle') object from the specified [Color](Tizen.UI.Color.md 'Tizen.UI.Color') value.

```csharp
public static Tizen.UI.Internal.ObjectPool&lt;Tizen.UI.NativeHandle.Vector4Handle> ToNative(this Tizen.UI.Color color);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToNative(thisTizen.UI.Color).color'></a>

`color` [Color](Tizen.UI.Color.md 'Tizen.UI.Color')

The color to convert.

#### Returns
[Tizen.UI.Internal.ObjectPool&lt;](Tizen.UI.Internal.ObjectPool_T_.md 'Tizen.UI.Internal.ObjectPool&lt;T>')[Vector4Handle](Tizen.UI.NativeHandle.Vector4Handle.md 'Tizen.UI.NativeHandle.Vector4Handle')[&gt;](Tizen.UI.Internal.ObjectPool_T_.md 'Tizen.UI.Internal.ObjectPool&lt;T>')  
A new [Vector4Handle](Tizen.UI.NativeHandle.Vector4Handle.md 'Tizen.UI.NativeHandle.Vector4Handle') object containing the color values.

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToNative(thisTizen.UI.Color,Tizen.UI.NativeHandle.Vector4Handle)'></a>

## NativeHandleExtensions.ToNative(this Color, Vector4Handle) Method

Sets the values of the specified [Vector4Handle](Tizen.UI.NativeHandle.Vector4Handle.md 'Tizen.UI.NativeHandle.Vector4Handle') object from the given [Color](Tizen.UI.Color.md 'Tizen.UI.Color') value.

```csharp
public static Tizen.UI.NativeHandle.Vector4Handle ToNative(this Tizen.UI.Color color, Tizen.UI.NativeHandle.Vector4Handle vector);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToNative(thisTizen.UI.Color,Tizen.UI.NativeHandle.Vector4Handle).color'></a>

`color` [Color](Tizen.UI.Color.md 'Tizen.UI.Color')

The color to convert.

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToNative(thisTizen.UI.Color,Tizen.UI.NativeHandle.Vector4Handle).vector'></a>

`vector` [Vector4Handle](Tizen.UI.NativeHandle.Vector4Handle.md 'Tizen.UI.NativeHandle.Vector4Handle')

The vector to set the values of.

#### Returns
[Vector4Handle](Tizen.UI.NativeHandle.Vector4Handle.md 'Tizen.UI.NativeHandle.Vector4Handle')  
The specified [Vector4Handle](Tizen.UI.NativeHandle.Vector4Handle.md 'Tizen.UI.NativeHandle.Vector4Handle') object with its values set.

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToNative(thisTizen.UI.CornerRadius)'></a>

## NativeHandleExtensions.ToNative(this CornerRadius) Method

Creates a new [Vector4Handle](Tizen.UI.NativeHandle.Vector4Handle.md 'Tizen.UI.NativeHandle.Vector4Handle') object from the specified [CornerRadius](Tizen.UI.CornerRadius.md 'Tizen.UI.CornerRadius') value.

```csharp
public static Tizen.UI.Internal.ObjectPool&lt;Tizen.UI.NativeHandle.Vector4Handle> ToNative(this Tizen.UI.CornerRadius value);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToNative(thisTizen.UI.CornerRadius).value'></a>

`value` [CornerRadius](Tizen.UI.CornerRadius.md 'Tizen.UI.CornerRadius')

The corner radius to convert.

#### Returns
[Tizen.UI.Internal.ObjectPool&lt;](Tizen.UI.Internal.ObjectPool_T_.md 'Tizen.UI.Internal.ObjectPool&lt;T>')[Vector4Handle](Tizen.UI.NativeHandle.Vector4Handle.md 'Tizen.UI.NativeHandle.Vector4Handle')[&gt;](Tizen.UI.Internal.ObjectPool_T_.md 'Tizen.UI.Internal.ObjectPool&lt;T>')  
A new [Vector4Handle](Tizen.UI.NativeHandle.Vector4Handle.md 'Tizen.UI.NativeHandle.Vector4Handle') object containing the corner radius values.

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToNative(thisTizen.UI.Point)'></a>

## NativeHandleExtensions.ToNative(this Point) Method

Creates a new [Vector2Handle](Tizen.UI.NativeHandle.Vector2Handle.md 'Tizen.UI.NativeHandle.Vector2Handle') object from the specified [Point](Tizen.UI.Point.md 'Tizen.UI.Point') value.

```csharp
public static Tizen.UI.Internal.ObjectPool&lt;Tizen.UI.NativeHandle.Vector2Handle> ToNative(this Tizen.UI.Point value);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToNative(thisTizen.UI.Point).value'></a>

`value` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The point to convert.

#### Returns
[Tizen.UI.Internal.ObjectPool&lt;](Tizen.UI.Internal.ObjectPool_T_.md 'Tizen.UI.Internal.ObjectPool&lt;T>')[Vector2Handle](Tizen.UI.NativeHandle.Vector2Handle.md 'Tizen.UI.NativeHandle.Vector2Handle')[&gt;](Tizen.UI.Internal.ObjectPool_T_.md 'Tizen.UI.Internal.ObjectPool&lt;T>')  
A new [Vector2Handle](Tizen.UI.NativeHandle.Vector2Handle.md 'Tizen.UI.NativeHandle.Vector2Handle') object containing the point values.

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToNative(thisTizen.UI.Size)'></a>

## NativeHandleExtensions.ToNative(this Size) Method

Creates a new [Vector2Handle](Tizen.UI.NativeHandle.Vector2Handle.md 'Tizen.UI.NativeHandle.Vector2Handle') object from the specified [Size](Tizen.UI.Size.md 'Tizen.UI.Size') value.

```csharp
public static Tizen.UI.Internal.ObjectPool&lt;Tizen.UI.NativeHandle.Vector2Handle> ToNative(this Tizen.UI.Size value);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToNative(thisTizen.UI.Size).value'></a>

`value` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The size to convert.

#### Returns
[Tizen.UI.Internal.ObjectPool&lt;](Tizen.UI.Internal.ObjectPool_T_.md 'Tizen.UI.Internal.ObjectPool&lt;T>')[Vector2Handle](Tizen.UI.NativeHandle.Vector2Handle.md 'Tizen.UI.NativeHandle.Vector2Handle')[&gt;](Tizen.UI.Internal.ObjectPool_T_.md 'Tizen.UI.Internal.ObjectPool&lt;T>')  
A new [Vector2Handle](Tizen.UI.NativeHandle.Vector2Handle.md 'Tizen.UI.NativeHandle.Vector2Handle') object containing the size values.

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToNativeRectangle(thisTizen.UI.Rect)'></a>

## NativeHandleExtensions.ToNativeRectangle(this Rect) Method

Creates a new [RectangleHandle](Tizen.UI.NativeHandle.RectangleHandle.md 'Tizen.UI.NativeHandle.RectangleHandle') object from the specified [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') value.

```csharp
public static Tizen.UI.NativeHandle.RectangleHandle ToNativeRectangle(this Tizen.UI.Rect rect);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToNativeRectangle(thisTizen.UI.Rect).rect'></a>

`rect` [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

The rect to convert.

#### Returns
[RectangleHandle](Tizen.UI.NativeHandle.RectangleHandle.md 'Tizen.UI.NativeHandle.RectangleHandle')  
A new [RectangleHandle](Tizen.UI.NativeHandle.RectangleHandle.md 'Tizen.UI.NativeHandle.RectangleHandle') object containing the rect values.

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToNativeRectangle(thisTizen.UI.Thickness)'></a>

## NativeHandleExtensions.ToNativeRectangle(this Thickness) Method

Creates a new [RectangleHandle](Tizen.UI.NativeHandle.RectangleHandle.md 'Tizen.UI.NativeHandle.RectangleHandle') object from the specified [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness') value.

```csharp
public static Tizen.UI.NativeHandle.RectangleHandle ToNativeRectangle(this Tizen.UI.Thickness rect);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToNativeRectangle(thisTizen.UI.Thickness).rect'></a>

`rect` [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

The thickness to convert.

#### Returns
[RectangleHandle](Tizen.UI.NativeHandle.RectangleHandle.md 'Tizen.UI.NativeHandle.RectangleHandle')  
A new [RectangleHandle](Tizen.UI.NativeHandle.RectangleHandle.md 'Tizen.UI.NativeHandle.RectangleHandle') object containing the thickness values.

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToPoint(thisTizen.UI.NativeHandle.Vector2Handle)'></a>

## NativeHandleExtensions.ToPoint(this Vector2Handle) Method

Converts the specified [Vector2Handle](Tizen.UI.NativeHandle.Vector2Handle.md 'Tizen.UI.NativeHandle.Vector2Handle') object to a [Point](Tizen.UI.Point.md 'Tizen.UI.Point') value.

```csharp
public static Tizen.UI.Point ToPoint(this Tizen.UI.NativeHandle.Vector2Handle value);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToPoint(thisTizen.UI.NativeHandle.Vector2Handle).value'></a>

`value` [Vector2Handle](Tizen.UI.NativeHandle.Vector2Handle.md 'Tizen.UI.NativeHandle.Vector2Handle')

convert.

#### Returns
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')  
A new [Point](Tizen.UI.Point.md 'Tizen.UI.Point') object containing the converted values.

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToPoint(thisTizen.UI.NativeHandle.Vector3Handle)'></a>

## NativeHandleExtensions.ToPoint(this Vector3Handle) Method

Converts the specified [Vector3Handle](Tizen.UI.NativeHandle.Vector3Handle.md 'Tizen.UI.NativeHandle.Vector3Handle') object to a [Point](Tizen.UI.Point.md 'Tizen.UI.Point') value.

```csharp
public static Tizen.UI.Point ToPoint(this Tizen.UI.NativeHandle.Vector3Handle value);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToPoint(thisTizen.UI.NativeHandle.Vector3Handle).value'></a>

`value` [Vector3Handle](Tizen.UI.NativeHandle.Vector3Handle.md 'Tizen.UI.NativeHandle.Vector3Handle')

convert.

#### Returns
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')  
A new [Point](Tizen.UI.Point.md 'Tizen.UI.Point') object containing the converted values.

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToRect(thisTizen.UI.NativeHandle.Vector4Handle)'></a>

## NativeHandleExtensions.ToRect(this Vector4Handle) Method

Converts the specified [Vector4Handle](Tizen.UI.NativeHandle.Vector4Handle.md 'Tizen.UI.NativeHandle.Vector4Handle') object to a [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') value.

```csharp
public static Tizen.UI.Rect ToRect(this Tizen.UI.NativeHandle.Vector4Handle vector);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToRect(thisTizen.UI.NativeHandle.Vector4Handle).vector'></a>

`vector` [Vector4Handle](Tizen.UI.NativeHandle.Vector4Handle.md 'Tizen.UI.NativeHandle.Vector4Handle')

The vector to convert.

#### Returns
[Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')  
A new [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect') object containing the converted values.

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToSize(thisTizen.UI.NativeHandle.Vector3Handle)'></a>

## NativeHandleExtensions.ToSize(this Vector3Handle) Method

Converts the specified [Vector3Handle](Tizen.UI.NativeHandle.Vector3Handle.md 'Tizen.UI.NativeHandle.Vector3Handle') object to a [Size](Tizen.UI.Size.md 'Tizen.UI.Size') value.

```csharp
public static Tizen.UI.Size ToSize(this Tizen.UI.NativeHandle.Vector3Handle vector);
```
#### Parameters

<a name='Tizen.UI.NativeHandle.NativeHandleExtensions.ToSize(thisTizen.UI.NativeHandle.Vector3Handle).vector'></a>

`vector` [Vector3Handle](Tizen.UI.NativeHandle.Vector3Handle.md 'Tizen.UI.NativeHandle.Vector3Handle')

The vector to convert.

#### Returns
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')  
A new [Size](Tizen.UI.Size.md 'Tizen.UI.Size') object containing the converted values.




