### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## UISettings Class

Provides a set of methods for managing the appearance and behavior of the user interface.

```csharp
public static class UISettings
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; UISettings
### Methods

<a name='Tizen.UI.UISettings.SetBrokenImageUrl(string)'></a>

## UISettings.SetBrokenImageUrl(string) Method

Sets the broken image URL for all broken image types.

```csharp
public static void SetBrokenImageUrl(string url);
```
#### Parameters

<a name='Tizen.UI.UISettings.SetBrokenImageUrl(string).url'></a>

`url` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The URL of the broken image.

<a name='Tizen.UI.UISettings.SetBrokenImageUrl(Tizen.UI.BrokenImageType,string)'></a>

## UISettings.SetBrokenImageUrl(BrokenImageType, string) Method

Sets the broken image URL for a specific broken image type.

```csharp
public static void SetBrokenImageUrl(Tizen.UI.BrokenImageType type, string url);
```
#### Parameters

<a name='Tizen.UI.UISettings.SetBrokenImageUrl(Tizen.UI.BrokenImageType,string).type'></a>

`type` [BrokenImageType](Tizen.UI.BrokenImageType.md 'Tizen.UI.BrokenImageType')

The type of broken image.

<a name='Tizen.UI.UISettings.SetBrokenImageUrl(Tizen.UI.BrokenImageType,string).url'></a>

`url` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The URL of the broken image.

<a name='Tizen.UI.UISettings.SetDoubleTapTimeout(int)'></a>

## UISettings.SetDoubleTapTimeout(int) Method

Sets the duration in milliseconds the duration time for recognizing multi-tap gesture.  
If there are two taps within this time, it is a double tap.

```csharp
public static void SetDoubleTapTimeout(int ms);
```
#### Parameters

<a name='Tizen.UI.UISettings.SetDoubleTapTimeout(int).ms'></a>

`ms` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The time value in milliseconds

### Remarks
This is a global configuration option. Affects all gestures.

<a name='Tizen.UI.UISettings.SetKeyRepeat(float,float)'></a>

## UISettings.SetKeyRepeat(float, float) Method

Sets the key repeat rate and delay.

```csharp
public static void SetKeyRepeat(float rate, float delay);
```
#### Parameters

<a name='Tizen.UI.UISettings.SetKeyRepeat(float,float).rate'></a>

`rate` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The rate at which the keyboard repeats keys.

<a name='Tizen.UI.UISettings.SetKeyRepeat(float,float).delay'></a>

`delay` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The delay before repeating keys.

<a name='Tizen.UI.UISettings.SetLongPressMinimumHoldingTime(int)'></a>

## UISettings.SetLongPressMinimumHoldingTime(int) Method

Sets the minimum holding time required to be recognized as a long press gesture

```csharp
public static void SetLongPressMinimumHoldingTime(int ms);
```
#### Parameters

<a name='Tizen.UI.UISettings.SetLongPressMinimumHoldingTime(int).ms'></a>

`ms` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The time value in milliseconds

### Remarks
This is a global configuration option. Affects all gestures.

<a name='Tizen.UI.UISettings.SetPinchMinimumDistance(float)'></a>

## UISettings.SetPinchMinimumDistance(float) Method

Sets the minimum distance required to start a pinch event

```csharp
public static void SetPinchMinimumDistance(float distance);
```
#### Parameters

<a name='Tizen.UI.UISettings.SetPinchMinimumDistance(float).distance'></a>

`distance` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

Distance in pixels

### Remarks
This is a global configuration option. Affects all gestures.

<a name='Tizen.UI.UISettings.SetTapRecognizerTime(int)'></a>

## UISettings.SetTapRecognizerTime(int) Method

Sets the recognizer time required to be recognized as a tap gesture,  
This time is from touch down to touch up to recognize the tap gesture.  
If the time between touch down and touch up is longer than recognizer time, it is not recognized as a tap gesture.

```csharp
public static void SetTapRecognizerTime(int ms);
```
#### Parameters

<a name='Tizen.UI.UISettings.SetTapRecognizerTime(int).ms'></a>

`ms` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The time value in milliseconds

### Remarks
This is a global configuration option. Affects all gestures.

<a name='Tizen.UI.UISettings.UsePreCompiledShader()'></a>

## UISettings.UsePreCompiledShader() Method

Compile the visual shader in advance. Afterwards, when a visual using a new shader is requested, the pre-compiled shader is used.

```csharp
public static void UsePreCompiledShader();
```

### Remarks
It is recommended that this method be called at the top of the application code.




