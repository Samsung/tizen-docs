### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## AnimatedImage Class

AnimatedImage is a control for displaying an animated image resource such as gif, webp and sequential images.

```csharp
public class AnimatedImage : Tizen.UI.Components.Material.Image,
Tizen.UI.Components.IAnimatedImage
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ImageView &#129106; [Image](Tizen.UI.Components.Material.Image.md 'Tizen.UI.Components.Material.Image') &#129106; AnimatedImage

Implements Tizen.UI.Components.IAnimatedImage
### Constructors

<a name='Tizen.UI.Components.Material.AnimatedImage.AnimatedImage()'></a>

## AnimatedImage() Constructor

Creates an instance of an AnimatedImage.

```csharp
public AnimatedImage();
```

<a name='Tizen.UI.Components.Material.AnimatedImage.AnimatedImage(string)'></a>

## AnimatedImage(string) Constructor

Creates an instance of an AnimatedImage.

```csharp
public AnimatedImage(string resourceUrl);
```
#### Parameters

<a name='Tizen.UI.Components.Material.AnimatedImage.AnimatedImage(string).resourceUrl'></a>

`resourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.AnimatedImage.AnimatedImage(System.Collections.Generic.IEnumerable_string_,int,int)'></a>

## AnimatedImage(IEnumerable&lt;string>, int, int) Constructor

Creates an instance of an AnimatedImage.

```csharp
public AnimatedImage(System.Collections.Generic.IEnumerable&lt;string> sequentialResourceUrls, int preloadingBatchSize=1, int cacheSize=1);
```
#### Parameters

<a name='Tizen.UI.Components.Material.AnimatedImage.AnimatedImage(System.Collections.Generic.IEnumerable_string_,int,int).sequentialResourceUrls'></a>

`sequentialResourceUrls` [System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')

The list of resource urls to be played sequentially.

<a name='Tizen.UI.Components.Material.AnimatedImage.AnimatedImage(System.Collections.Generic.IEnumerable_string_,int,int).preloadingBatchSize'></a>

`preloadingBatchSize` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The size of the batch to preload.

<a name='Tizen.UI.Components.Material.AnimatedImage.AnimatedImage(System.Collections.Generic.IEnumerable_string_,int,int).cacheSize'></a>

`cacheSize` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The number of images to keep cached ahead during playback.
### Properties

<a name='Tizen.UI.Components.Material.AnimatedImage.CurrentFrame'></a>

## AnimatedImage.CurrentFrame Property

Gets or sets the current frame of the animation.

```csharp
public int CurrentFrame { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.AnimatedImage.FrameSpeedFactor'></a>

## AnimatedImage.FrameSpeedFactor Property

Gets or sets a speed factor for the animated image frame.

```csharp
public float FrameSpeedFactor { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
The speed factor is a multiplier of the normal velocity of the animation. Values between [0,1] will  
slow down the animation and values above one will speed up the animation.  
The range of this value is clamped between [0.01f ~ 100.0f].

<a name='Tizen.UI.Components.Material.AnimatedImage.IsLooping'></a>

## AnimatedImage.IsLooping Property

Gets or sets whether the animation should loop.

```csharp
public bool IsLooping { get; set; }
```

Implements IsLooping

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.AnimatedImage.RepeatCount'></a>

## AnimatedImage.RepeatCount Property

Gets or sets the number of times the animation should repeat.

```csharp
public int RepeatCount { get; set; }
```

Implements RepeatCount

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.AnimatedImage.RepeatMode'></a>

## AnimatedImage.RepeatMode Property

Gets or sets the mode of animation repetition.

```csharp
public Tizen.UI.AnimationRepeatMode RepeatMode { get; set; }
```

#### Property Value
Tizen.UI.AnimationRepeatMode

<a name='Tizen.UI.Components.Material.AnimatedImage.StopBehavior'></a>

## AnimatedImage.StopBehavior Property

Gets or sets the behavior of the animation when it stops.

```csharp
public Tizen.UI.AnimationStopBehavior StopBehavior { get; set; }
```

Implements StopBehavior

#### Property Value
Tizen.UI.AnimationStopBehavior

<a name='Tizen.UI.Components.Material.AnimatedImage.TotalFrame'></a>

## AnimatedImage.TotalFrame Property

Gets the total number of frames in the animation.

```csharp
public int TotalFrame { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')
### Methods

<a name='Tizen.UI.Components.Material.AnimatedImage.SetSequentialResourceUrls(System.Collections.Generic.IEnumerable_string_,int,int)'></a>

## AnimatedImage.SetSequentialResourceUrls(IEnumerable&lt;string>, int, int) Method

Sets the resource urls to be played sequentially.

```csharp
public void SetSequentialResourceUrls(System.Collections.Generic.IEnumerable&lt;string> sequentialResourceUrls, int preloadingBatchSize=1, int cacheSize=1);
```
#### Parameters

<a name='Tizen.UI.Components.Material.AnimatedImage.SetSequentialResourceUrls(System.Collections.Generic.IEnumerable_string_,int,int).sequentialResourceUrls'></a>

`sequentialResourceUrls` [System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')

The list of resource urls to be played sequentially.

<a name='Tizen.UI.Components.Material.AnimatedImage.SetSequentialResourceUrls(System.Collections.Generic.IEnumerable_string_,int,int).preloadingBatchSize'></a>

`preloadingBatchSize` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The size of the batch to preload.

<a name='Tizen.UI.Components.Material.AnimatedImage.SetSequentialResourceUrls(System.Collections.Generic.IEnumerable_string_,int,int).cacheSize'></a>

`cacheSize` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The number of images to keep cached ahead during playback.

### Remarks
This will ignore the value of [Image.ResourceUrl](https://docs.microsoft.com/en-us/dotnet/api/Image.ResourceUrl 'Image.ResourceUrl').














































