### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## AnimatedImageVisualMap Class

AnimatedImageVisualMap is a class that represents a property map for the animated image visual.

```csharp
public class AnimatedImageVisualMap : Tizen.UI.Internal.ImageVisualMap
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.Internal.ImageVisualMap](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Internal.ImageVisualMap 'Tizen.UI.Internal.ImageVisualMap') &#129106; AnimatedImageVisualMap
### Properties

<a name='Tizen.UI.Components.AnimatedImageVisualMap.CacheSize'></a>

## AnimatedImageVisualMap.CacheSize Property

Defines the cache size for loading images in the sequential image animation.  
number of images to keep cached ahead during playback.

```csharp
public int CacheSize { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

### Remarks
cacheSize should be >= batchSize. If it isn't, then the cache will automatically be changed to batchSize.  
because of the defaults, it is expected that the application developer tune the batch and cache sizes to their particular use case.

<a name='Tizen.UI.Components.AnimatedImageVisualMap.FrameSpeedFactor'></a>

## AnimatedImageVisualMap.FrameSpeedFactor Property

Specifies a speed factor for the animated image frame.

```csharp
public float FrameSpeedFactor { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
The speed factor is a multiplier of the normal velocity of the animation. Values between [0,1] will  
slow down the animation and values above one will speed up the animation.  
The range of this value is clamped between [0.01f ~ 100.0f].

<a name='Tizen.UI.Components.AnimatedImageVisualMap.PreloadingBatchSize'></a>

## AnimatedImageVisualMap.PreloadingBatchSize Property

Defines the batch size for pre-loading images in the sequential image animation.  
number of images to pre-load before starting to play.

```csharp
public int PreloadingBatchSize { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.AnimatedImageVisualMap.RepeatCount'></a>

## AnimatedImageVisualMap.RepeatCount Property

Gets or sets whether the animation should loop.

```csharp
public int RepeatCount { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.AnimatedImageVisualMap.RepeatMode'></a>

## AnimatedImageVisualMap.RepeatMode Property

Gets or sets the mode of animation repetition.

```csharp
public Tizen.UI.AnimationRepeatMode RepeatMode { get; set; }
```

#### Property Value
[Tizen.UI.AnimationRepeatMode](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AnimationRepeatMode 'Tizen.UI.AnimationRepeatMode')

<a name='Tizen.UI.Components.AnimatedImageVisualMap.StopBehavior'></a>

## AnimatedImageVisualMap.StopBehavior Property

Gets or sets the behavior of the animation when it stops.

```csharp
public Tizen.UI.AnimationStopBehavior StopBehavior { get; set; }
```

#### Property Value
[Tizen.UI.AnimationStopBehavior](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AnimationStopBehavior 'Tizen.UI.AnimationStopBehavior')


























































