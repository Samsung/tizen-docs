### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## LottieAnimationView Class

LottieAnimationView is a control for displaying Lottie animations.

```csharp
public class LottieAnimationView : Tizen.UI.ImageView
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; [View](Tizen.UI.View.md 'Tizen.UI.View') &#129106; [ImageView](Tizen.UI.ImageView.md 'Tizen.UI.ImageView') &#129106; LottieAnimationView
### Constructors

<a name='Tizen.UI.LottieAnimationView.LottieAnimationView()'></a>

## LottieAnimationView() Constructor

Creates a LottieAnimationView.

```csharp
public LottieAnimationView();
```
### Properties

<a name='Tizen.UI.LottieAnimationView.CurrentFrame'></a>

## LottieAnimationView.CurrentFrame Property

Gets or sets the current frame of the animation.

```csharp
public int CurrentFrame { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.LottieAnimationView.Loop'></a>

## LottieAnimationView.Loop Property

Gets or sets whether the animation should loop.

```csharp
public bool Loop { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.LottieAnimationView.PlayState'></a>

## LottieAnimationView.PlayState Property

Gets the current play state of the animation.

```csharp
public Tizen.UI.AnimationState PlayState { get; }
```

#### Property Value
[AnimationState](Tizen.UI.AnimationState.md 'Tizen.UI.AnimationState')

<a name='Tizen.UI.LottieAnimationView.RepeatCount'></a>

## LottieAnimationView.RepeatCount Property

Gets or sets the number of times the animation should repeat.

```csharp
public int RepeatCount { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.LottieAnimationView.RepeatMode'></a>

## LottieAnimationView.RepeatMode Property

Gets or sets the mode of animation repetition.

```csharp
public Tizen.UI.AnimationRepeatMode RepeatMode { get; set; }
```

#### Property Value
Tizen.UI.AnimationRepeatMode

<a name='Tizen.UI.LottieAnimationView.StopBehavior'></a>

## LottieAnimationView.StopBehavior Property

Gets or sets the behavior of the animation when it stops.

```csharp
public Tizen.UI.AnimationStopBehavior StopBehavior { get; set; }
```

#### Property Value
Tizen.UI.AnimationStopBehavior

<a name='Tizen.UI.LottieAnimationView.TotalFrame'></a>

## LottieAnimationView.TotalFrame Property

Gets the total number of frames in the animation.

```csharp
public int TotalFrame { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')
### Methods

<a name='Tizen.UI.LottieAnimationView.GetContentInfo()'></a>

## LottieAnimationView.GetContentInfo() Method

Gets the content information of the animation.

```csharp
public System.Collections.Generic.IList&lt;(string,int,int)> GetContentInfo();
```

#### Returns
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[,](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[,](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')  
of tuples containing the marker name, start frame, and end frame.

<a name='Tizen.UI.LottieAnimationView.Pause()'></a>

## LottieAnimationView.Pause() Method

Pauses the animation.

```csharp
public override void Pause();
```

<a name='Tizen.UI.LottieAnimationView.Play()'></a>

## LottieAnimationView.Play() Method

Plays the animation.

```csharp
public override void Play();
```

<a name='Tizen.UI.LottieAnimationView.Play(int,int)'></a>

## LottieAnimationView.Play(int, int) Method

Plays the animation with range.

```csharp
public void Play(int startFrame, int endFrame=int.MaxValue);
```
#### Parameters

<a name='Tizen.UI.LottieAnimationView.Play(int,int).startFrame'></a>

`startFrame` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The starting frame.

<a name='Tizen.UI.LottieAnimationView.Play(int,int).endFrame'></a>

`endFrame` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The ending frame.

<a name='Tizen.UI.LottieAnimationView.Stop()'></a>

## LottieAnimationView.Stop() Method

Stops the animation.

```csharp
public override void Stop();
```
### Events

<a name='Tizen.UI.LottieAnimationView.Finished'></a>

## LottieAnimationView.Finished Event

Event triggered when the animation finishes.

```csharp
public event EventHandler Finished;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')







