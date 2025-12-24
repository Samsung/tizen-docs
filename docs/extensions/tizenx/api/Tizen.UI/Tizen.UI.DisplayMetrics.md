### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## DisplayMetrics Class

Provides methods for converting between display units and pixels.

```csharp
public static class DisplayMetrics
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; DisplayMetrics
### Properties

<a name='Tizen.UI.DisplayMetrics.DPI'></a>

## DisplayMetrics.DPI Property

Gets the dots per inch (DPI) of the device screen.

```csharp
public static int DPI { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.DisplayMetrics.Scale'></a>

## DisplayMetrics.Scale Property

Gets or sets the scale factor.

```csharp
public static float Scale { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.DisplayMetrics.ScreenHeight'></a>

## DisplayMetrics.ScreenHeight Property

Gets the height of the device screen in pixels.

```csharp
public static int ScreenHeight { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.DisplayMetrics.ScreenWidth'></a>

## DisplayMetrics.ScreenWidth Property

Gets the width of the device screen in pixels.

```csharp
public static int ScreenWidth { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')
### Methods

<a name='Tizen.UI.DisplayMetrics.SetDensityBasedScaleFactor(float,int)'></a>

## DisplayMetrics.SetDensityBasedScaleFactor(float, int) Method

Sets the scale factor based on density.

```csharp
public static void SetDensityBasedScaleFactor(float userScale=1f, int baseDPI=160);
```
#### Parameters

<a name='Tizen.UI.DisplayMetrics.SetDensityBasedScaleFactor(float,int).userScale'></a>

`userScale` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The user-defined scale factor.

<a name='Tizen.UI.DisplayMetrics.SetDensityBasedScaleFactor(float,int).baseDPI'></a>

`baseDPI` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The base DPI value.

<a name='Tizen.UI.DisplayMetrics.ToPoint(thisfloat)'></a>

## DisplayMetrics.ToPoint(this float) Method

Converts the specified pixel value to point value.

```csharp
public static float ToPoint(this float pixel);
```
#### Parameters

<a name='Tizen.UI.DisplayMetrics.ToPoint(thisfloat).pixel'></a>

`pixel` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The pixel value to be converted.

#### Returns
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')  
The converted point value.
### Events

<a name='Tizen.UI.DisplayMetrics.ScaleUpdated'></a>

## DisplayMetrics.ScaleUpdated Event

Occurs when the scale factors are updated.

```csharp
public static event EventHandler ScaleUpdated;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')






