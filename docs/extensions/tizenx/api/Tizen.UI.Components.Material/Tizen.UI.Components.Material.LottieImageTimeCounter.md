### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## LottieImageTimeCounter Class

A time counter component using LottieImage.

```csharp
public class LottieImageTimeCounter : Tizen.UI.Components.TimeCounter
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; [Tizen.UI.Components.TimeCounter](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.TimeCounter 'Tizen.UI.Components.TimeCounter') &#129106; LottieImageTimeCounter
### Constructors

<a name='Tizen.UI.Components.Material.LottieImageTimeCounter.LottieImageTimeCounter(int,string)'></a>

## LottieImageTimeCounter(int, string) Constructor

Constructs a new lottie image time counter.

```csharp
public LottieImageTimeCounter(int totalTimeInMilliseconds, string resourceUrl);
```
#### Parameters

<a name='Tizen.UI.Components.Material.LottieImageTimeCounter.LottieImageTimeCounter(int,string).totalTimeInMilliseconds'></a>

`totalTimeInMilliseconds` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.LottieImageTimeCounter.LottieImageTimeCounter(int,string).resourceUrl'></a>

`resourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.LottieImageTimeCounter.LottieImageTimeCounter(string)'></a>

## LottieImageTimeCounter(string) Constructor

Constructs a new lottie image time counter.

```csharp
public LottieImageTimeCounter(string resourceUrl);
```
#### Parameters

<a name='Tizen.UI.Components.Material.LottieImageTimeCounter.LottieImageTimeCounter(string).resourceUrl'></a>

`resourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')
### Properties

<a name='Tizen.UI.Components.Material.LottieImageTimeCounter.LottieImage'></a>

## LottieImageTimeCounter.LottieImage Property

Gets the lottie image handle.

```csharp
public Tizen.UI.Components.Material.LottieImage LottieImage { get; }
```

#### Property Value
[LottieImage](Tizen.UI.Components.Material.LottieImage.md 'Tizen.UI.Components.Material.LottieImage')

<a name='Tizen.UI.Components.Material.LottieImageTimeCounter.UseReverseFrameIndex'></a>

## LottieImageTimeCounter.UseReverseFrameIndex Property

Gets or sets whether to use reverse frame index for lottie to describe remaining time. Default is false.

```csharp
public bool UseReverseFrameIndex { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')













































