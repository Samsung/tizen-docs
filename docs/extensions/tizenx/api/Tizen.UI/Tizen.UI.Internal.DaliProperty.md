### [Tizen.UI.Internal](Tizen.UI.Internal.md 'Tizen.UI.Internal')

## DaliProperty Class

Provides a set of extension methods for the View class.

```csharp
public static class DaliProperty
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; DaliProperty
### Methods

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,bool)'></a>

## DaliProperty.Get(this NObject, int, bool) Method

Gets the specified property value for the given view.

```csharp
public static void Get(this Tizen.UI.NObject view, int key, out bool value);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,bool).view'></a>

`view` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The view to get the property value from.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,bool).key'></a>

`key` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The property key.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,bool).value'></a>

`value` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

The property value.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,float)'></a>

## DaliProperty.Get(this NObject, int, float) Method

Gets the specified property value for the given view.

```csharp
public static void Get(this Tizen.UI.NObject view, int key, out float value);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,float).view'></a>

`view` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The view to get the property value from.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,float).key'></a>

`key` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The property key.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,float).value'></a>

`value` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The property value.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,float,float,float)'></a>

## DaliProperty.Get(this NObject, int, float, float, float) Method

Gets the float value of the specified property.

```csharp
public static void Get(this Tizen.UI.NObject view, int key, out float v1, out float v2, out float v3);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,float,float,float).view'></a>

`view` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The view object.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,float,float,float).key'></a>

`key` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The key of the property.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,float,float,float).v1'></a>

`v1` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The first float value.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,float,float,float).v2'></a>

`v2` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The second float value.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,float,float,float).v3'></a>

`v3` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The third float value.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,int)'></a>

## DaliProperty.Get(this NObject, int, int) Method

Gets the specified property value for the given view.

```csharp
public static void Get(this Tizen.UI.NObject view, int key, out int value);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,int).view'></a>

`view` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The view to get the property value from.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,int).key'></a>

`key` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The property key.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,int).value'></a>

`value` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The property value.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,int,int)'></a>

## DaliProperty.Get(this NObject, int, int, int) Method

Retrieves an integer property of a visual at the specified index on the given view.

```csharp
public static void Get(this Tizen.UI.NObject view, int visualIndex, int key, out int value);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,int,int).view'></a>

`view` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The view object on which the visual is applied.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,int,int).visualIndex'></a>

`visualIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index of the visual to retrieve the property from.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,int,int).key'></a>

`key` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The key identifying the property to retrieve.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,int,int).value'></a>

`value` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The retrieved integer value of the specified property.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,int,Tizen.UI.Color)'></a>

## DaliProperty.Get(this NObject, int, int, Color) Method

Retrieves the specified visual property of a given visual index on the view.

```csharp
public static void Get(this Tizen.UI.NObject view, int visualIndex, int key, out Tizen.UI.Color value);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,int,Tizen.UI.Color).view'></a>

`view` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The view object to retrieve the visual property from.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,int,Tizen.UI.Color).visualIndex'></a>

`visualIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index of the visual whose property is being retrieved.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,int,Tizen.UI.Color).key'></a>

`key` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The key identifying the property to be retrieved.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,int,Tizen.UI.Color).value'></a>

`value` [Color](Tizen.UI.Color.md 'Tizen.UI.Color')

The output color value of the specified visual property.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,int,Tizen.UI.CornerRadius)'></a>

## DaliProperty.Get(this NObject, int, int, CornerRadius) Method

Retrieves the CornerRadius property of a visual on the specified view.

```csharp
public static void Get(this Tizen.UI.NObject view, int visualIndex, int key, out Tizen.UI.CornerRadius value);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,int,Tizen.UI.CornerRadius).view'></a>

`view` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The view object to retrieve the property from.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,int,Tizen.UI.CornerRadius).visualIndex'></a>

`visualIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index of the visual to retrieve the property from.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,int,Tizen.UI.CornerRadius).key'></a>

`key` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The key identifying the property to retrieve.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,int,Tizen.UI.CornerRadius).value'></a>

`value` [CornerRadius](Tizen.UI.CornerRadius.md 'Tizen.UI.CornerRadius')

The output CornerRadius value retrieved from the visual property.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,string)'></a>

## DaliProperty.Get(this NObject, int, string) Method

Gets the specified property value for the given view.

```csharp
public static void Get(this Tizen.UI.NObject view, int key, out string value);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,string).view'></a>

`view` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The view to get the property value from.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,string).key'></a>

`key` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The property key.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,string).value'></a>

`value` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The property value.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,Tizen.UI.Color)'></a>

## DaliProperty.Get(this NObject, int, Color) Method

Gets the specified property value for the given view.

```csharp
public static void Get(this Tizen.UI.NObject view, int key, out Tizen.UI.Color value);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,Tizen.UI.Color).view'></a>

`view` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The view to get the property value from.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,Tizen.UI.Color).key'></a>

`key` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The property key.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,Tizen.UI.Color).value'></a>

`value` [Color](Tizen.UI.Color.md 'Tizen.UI.Color')

The property value.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,Tizen.UI.CornerRadius)'></a>

## DaliProperty.Get(this NObject, int, CornerRadius) Method

Gets the specified corner radius for the given view.

```csharp
public static void Get(this Tizen.UI.NObject view, int key, out Tizen.UI.CornerRadius value);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,Tizen.UI.CornerRadius).view'></a>

`view` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The view to get the property value from.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,Tizen.UI.CornerRadius).key'></a>

`key` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The property key.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,Tizen.UI.CornerRadius).value'></a>

`value` [CornerRadius](Tizen.UI.CornerRadius.md 'Tizen.UI.CornerRadius')

The property value.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,Tizen.UI.NativeHandle.PropertyMapHandle)'></a>

## DaliProperty.Get(this NObject, int, PropertyMapHandle) Method

Gets the specified property value for the given view.

```csharp
public static void Get(this Tizen.UI.NObject view, int key, Tizen.UI.NativeHandle.PropertyMapHandle map);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,Tizen.UI.NativeHandle.PropertyMapHandle).view'></a>

`view` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The view to get the property value from.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,Tizen.UI.NativeHandle.PropertyMapHandle).key'></a>

`key` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The property key.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,Tizen.UI.NativeHandle.PropertyMapHandle).map'></a>

`map` [PropertyMapHandle](Tizen.UI.NativeHandle.PropertyMapHandle.md 'Tizen.UI.NativeHandle.PropertyMapHandle')

The property map.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,Tizen.UI.NativeHandle.PropertyValueHandle)'></a>

## DaliProperty.Get(this NObject, int, PropertyValueHandle) Method

Gets the specified property value for the given view.

```csharp
public static void Get(this Tizen.UI.NObject view, int key, out Tizen.UI.NativeHandle.PropertyValueHandle value);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,Tizen.UI.NativeHandle.PropertyValueHandle).view'></a>

`view` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The view to get the property value from.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,Tizen.UI.NativeHandle.PropertyValueHandle).key'></a>

`key` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The property key.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,Tizen.UI.NativeHandle.PropertyValueHandle).value'></a>

`value` [PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')

The property value.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,Tizen.UI.Point)'></a>

## DaliProperty.Get(this NObject, int, Point) Method

Gets the value of the specified property.

```csharp
public static void Get(this Tizen.UI.NObject view, int key, out Tizen.UI.Point value);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,Tizen.UI.Point).view'></a>

`view` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The view object.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,Tizen.UI.Point).key'></a>

`key` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The key of the property.

<a name='Tizen.UI.Internal.DaliProperty.Get(thisTizen.UI.NObject,int,Tizen.UI.Point).value'></a>

`value` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The output value of the property.

<a name='Tizen.UI.Internal.DaliProperty.GetCurrent(thisTizen.UI.NObject,int,Tizen.UI.Point)'></a>

## DaliProperty.GetCurrent(this NObject, int, Point) Method

Gets the current value of the specified property.

```csharp
public static void GetCurrent(this Tizen.UI.NObject view, int key, out Tizen.UI.Point value);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.GetCurrent(thisTizen.UI.NObject,int,Tizen.UI.Point).view'></a>

`view` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The view object.

<a name='Tizen.UI.Internal.DaliProperty.GetCurrent(thisTizen.UI.NObject,int,Tizen.UI.Point).key'></a>

`key` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The key of the property.

<a name='Tizen.UI.Internal.DaliProperty.GetCurrent(thisTizen.UI.NObject,int,Tizen.UI.Point).value'></a>

`value` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The output value of the property.

<a name='Tizen.UI.Internal.DaliProperty.GetCurrent(thisTizen.UI.NObject,int,Tizen.UI.Size)'></a>

## DaliProperty.GetCurrent(this NObject, int, Size) Method

Gets the current value of the specified property.

```csharp
public static void GetCurrent(this Tizen.UI.NObject view, int key, out Tizen.UI.Size value);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.GetCurrent(thisTizen.UI.NObject,int,Tizen.UI.Size).view'></a>

`view` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The view object.

<a name='Tizen.UI.Internal.DaliProperty.GetCurrent(thisTizen.UI.NObject,int,Tizen.UI.Size).key'></a>

`key` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The key of the property.

<a name='Tizen.UI.Internal.DaliProperty.GetCurrent(thisTizen.UI.NObject,int,Tizen.UI.Size).value'></a>

`value` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The output value of the property.

<a name='Tizen.UI.Internal.DaliProperty.Register(thisTizen.UI.NObject,string,Tizen.UI.NativeHandle.PropertyValueHandle)'></a>

## DaliProperty.Register(this NObject, string, PropertyValueHandle) Method

Registers the specified property value for the given NObject.

```csharp
public static int Register(this Tizen.UI.NObject obj, string name, Tizen.UI.NativeHandle.PropertyValueHandle value);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.Register(thisTizen.UI.NObject,string,Tizen.UI.NativeHandle.PropertyValueHandle).obj'></a>

`obj` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The NObject to register the property value for.

<a name='Tizen.UI.Internal.DaliProperty.Register(thisTizen.UI.NObject,string,Tizen.UI.NativeHandle.PropertyValueHandle).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The property name.

<a name='Tizen.UI.Internal.DaliProperty.Register(thisTizen.UI.NObject,string,Tizen.UI.NativeHandle.PropertyValueHandle).value'></a>

`value` [PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')

The property value.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,bool)'></a>

## DaliProperty.Set(this NObject, int, bool) Method

Sets the specified property value for the given view.

```csharp
public static void Set(this Tizen.UI.NObject view, int key, bool value);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,bool).view'></a>

`view` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The view to set the property value for.

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,bool).key'></a>

`key` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The property key.

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,bool).value'></a>

`value` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

The property value.

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,float)'></a>

## DaliProperty.Set(this NObject, int, float) Method

Sets the specified property value for the given view.

```csharp
public static void Set(this Tizen.UI.NObject view, int key, float value);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,float).view'></a>

`view` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The view to set the property value for.

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,float).key'></a>

`key` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The property key.

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,float).value'></a>

`value` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The property value.

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,int)'></a>

## DaliProperty.Set(this NObject, int, int) Method

Sets the specified property value for the given view.

```csharp
public static void Set(this Tizen.UI.NObject view, int key, int value);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,int).view'></a>

`view` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The view to set the property value for.

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,int).key'></a>

`key` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The property key.

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,int).value'></a>

`value` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The property value.

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,Tizen.UI.Color)'></a>

## DaliProperty.Set(this NObject, int, Color) Method

Sets the specified property value for the given view.

```csharp
public static void Set(this Tizen.UI.NObject view, int key, Tizen.UI.Color value);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,Tizen.UI.Color).view'></a>

`view` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The view to set the property value for.

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,Tizen.UI.Color).key'></a>

`key` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The property key.

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,Tizen.UI.Color).value'></a>

`value` [Color](Tizen.UI.Color.md 'Tizen.UI.Color')

The property value.

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,Tizen.UI.NativeHandle.PropertyValueHandle)'></a>

## DaliProperty.Set(this NObject, int, PropertyValueHandle) Method

Sets the specified property value for the given view.

```csharp
public static void Set(this Tizen.UI.NObject view, int key, Tizen.UI.NativeHandle.PropertyValueHandle value);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,Tizen.UI.NativeHandle.PropertyValueHandle).view'></a>

`view` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The view to set the property value for.

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,Tizen.UI.NativeHandle.PropertyValueHandle).key'></a>

`key` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The property key.

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,Tizen.UI.NativeHandle.PropertyValueHandle).value'></a>

`value` [PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')

The property value.

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,Tizen.UI.NativeHandle.Vector4Handle)'></a>

## DaliProperty.Set(this NObject, int, Vector4Handle) Method

Sets the specified property value for the given view.

```csharp
public static void Set(this Tizen.UI.NObject view, int key, Tizen.UI.NativeHandle.Vector4Handle value);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,Tizen.UI.NativeHandle.Vector4Handle).view'></a>

`view` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The view to set the property value for.

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,Tizen.UI.NativeHandle.Vector4Handle).key'></a>

`key` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The property key.

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,int,Tizen.UI.NativeHandle.Vector4Handle).value'></a>

`value` [Vector4Handle](Tizen.UI.NativeHandle.Vector4Handle.md 'Tizen.UI.NativeHandle.Vector4Handle')

The property value.

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,string,Tizen.UI.NativeHandle.PropertyValueHandle)'></a>

## DaliProperty.Set(this NObject, string, PropertyValueHandle) Method

Sets the specified property value for the given NObject.

```csharp
public static void Set(this Tizen.UI.NObject obj, string name, Tizen.UI.NativeHandle.PropertyValueHandle value);
```
#### Parameters

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,string,Tizen.UI.NativeHandle.PropertyValueHandle).obj'></a>

`obj` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The NObject to set the property value for.

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,string,Tizen.UI.NativeHandle.PropertyValueHandle).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The property name.

<a name='Tizen.UI.Internal.DaliProperty.Set(thisTizen.UI.NObject,string,Tizen.UI.NativeHandle.PropertyValueHandle).value'></a>

`value` [PropertyValueHandle](Tizen.UI.NativeHandle.PropertyValueHandle.md 'Tizen.UI.NativeHandle.PropertyValueHandle')

The property value.




