### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## Animation Class

Animation class is used to animate the properties of a view.

```csharp
public class Animation : Tizen.UI.NObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; Animation
### Constructors

<a name='Tizen.UI.Animation.Animation()'></a>

## Animation() Constructor

Constructor to create an animation object.

```csharp
public Animation();
```

<a name='Tizen.UI.Animation.Animation(System.IntPtr,bool)'></a>

## Animation(IntPtr, bool) Constructor

Constructor to create an animation object.

```csharp
public Animation(System.IntPtr handle, bool ownsHandle);
```
#### Parameters

<a name='Tizen.UI.Animation.Animation(System.IntPtr,bool).handle'></a>

`handle` [System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')

A native handle.

<a name='Tizen.UI.Animation.Animation(System.IntPtr,bool).ownsHandle'></a>

`ownsHandle` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

>The flag determines who is responsible for deleting the underlying native object.
### Properties

<a name='Tizen.UI.Animation.CurrentProgress'></a>

## Animation.CurrentProgress Property

Gets the current progress of the animation.

```csharp
public float CurrentProgress { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Animation.Duration'></a>

## Animation.Duration Property

Gets or sets the duration of the animation in milliseconds.

```csharp
public int Duration { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Animation.EndAction'></a>

## Animation.EndAction Property

Gets or sets the end action of the animation that specifies the state of the animated Property when the animation ends.

```csharp
public Tizen.UI.AnimationEndAction EndAction { get; set; }
```

#### Property Value
[AnimationEndAction](Tizen.UI.AnimationEndAction.md 'Tizen.UI.AnimationEndAction')

<a name='Tizen.UI.Animation.IsLoop'></a>

## Animation.IsLoop Property

Gets or sets whether the animation should loop or not.

```csharp
public bool IsLoop { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Animation.ProgressReachedTarget'></a>

## Animation.ProgressReachedTarget Property

Gets or sets the progress notification point of the animation.

```csharp
public float ProgressReachedTarget { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Animation.State'></a>

## Animation.State Property

Gets the current state of the animation.

```csharp
public Tizen.UI.AnimationState State { get; }
```

#### Property Value
[AnimationState](Tizen.UI.AnimationState.md 'Tizen.UI.AnimationState')
### Methods

<a name='Tizen.UI.Animation.AnimateBy(Tizen.UI.View,Tizen.UI.AnimatablePropertyValue,int,int,Tizen.UI.AlphaFunction)'></a>

## Animation.AnimateBy(View, AnimatablePropertyValue, int, int, AlphaFunction) Method

Animates the given property by the specified value with a specified delay and duration.

```csharp
public void AnimateBy(Tizen.UI.View target, Tizen.UI.AnimatablePropertyValue props, int delayMs, int durationMs, Tizen.UI.AlphaFunction alpha=null);
```
#### Parameters

<a name='Tizen.UI.Animation.AnimateBy(Tizen.UI.View,Tizen.UI.AnimatablePropertyValue,int,int,Tizen.UI.AlphaFunction).target'></a>

`target` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view whose property is to be animated.

<a name='Tizen.UI.Animation.AnimateBy(Tizen.UI.View,Tizen.UI.AnimatablePropertyValue,int,int,Tizen.UI.AlphaFunction).props'></a>

`props` [AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue')

The property to be animated.

<a name='Tizen.UI.Animation.AnimateBy(Tizen.UI.View,Tizen.UI.AnimatablePropertyValue,int,int,Tizen.UI.AlphaFunction).delayMs'></a>

`delayMs` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The delay before the animation starts in milliseconds.

<a name='Tizen.UI.Animation.AnimateBy(Tizen.UI.View,Tizen.UI.AnimatablePropertyValue,int,int,Tizen.UI.AlphaFunction).durationMs'></a>

`durationMs` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The duration of the animation in milliseconds.

<a name='Tizen.UI.Animation.AnimateBy(Tizen.UI.View,Tizen.UI.AnimatablePropertyValue,int,int,Tizen.UI.AlphaFunction).alpha'></a>

`alpha` [AlphaFunction](Tizen.UI.AlphaFunction.md 'Tizen.UI.AlphaFunction')

The alpha function to apply to the animation.

<a name='Tizen.UI.Animation.AnimateTo(Tizen.UI.View,Tizen.UI.AnimatablePropertyValue,int,int,Tizen.UI.AlphaFunction)'></a>

## Animation.AnimateTo(View, AnimatablePropertyValue, int, int, AlphaFunction) Method

Animates the given property to the specified value with a specified delay and duration.

```csharp
public void AnimateTo(Tizen.UI.View target, Tizen.UI.AnimatablePropertyValue props, int delayMs, int durationMs, Tizen.UI.AlphaFunction alpha=null);
```
#### Parameters

<a name='Tizen.UI.Animation.AnimateTo(Tizen.UI.View,Tizen.UI.AnimatablePropertyValue,int,int,Tizen.UI.AlphaFunction).target'></a>

`target` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view whose property is to be animated.

<a name='Tizen.UI.Animation.AnimateTo(Tizen.UI.View,Tizen.UI.AnimatablePropertyValue,int,int,Tizen.UI.AlphaFunction).props'></a>

`props` [AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue')

The property to be animated.

<a name='Tizen.UI.Animation.AnimateTo(Tizen.UI.View,Tizen.UI.AnimatablePropertyValue,int,int,Tizen.UI.AlphaFunction).delayMs'></a>

`delayMs` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The delay before the animation starts in milliseconds.

<a name='Tizen.UI.Animation.AnimateTo(Tizen.UI.View,Tizen.UI.AnimatablePropertyValue,int,int,Tizen.UI.AlphaFunction).durationMs'></a>

`durationMs` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The duration of the animation in milliseconds.

<a name='Tizen.UI.Animation.AnimateTo(Tizen.UI.View,Tizen.UI.AnimatablePropertyValue,int,int,Tizen.UI.AlphaFunction).alpha'></a>

`alpha` [AlphaFunction](Tizen.UI.AlphaFunction.md 'Tizen.UI.AlphaFunction')

The alpha function to apply to the animation.

<a name='Tizen.UI.Animation.Clear()'></a>

## Animation.Clear() Method

Clears all animations from the animation object.

```csharp
public void Clear();
```

<a name='Tizen.UI.Animation.Pause()'></a>

## Animation.Pause() Method

Pauses the animation.

```csharp
public void Pause();
```

<a name='Tizen.UI.Animation.Play()'></a>

## Animation.Play() Method

Plays the animation.

```csharp
public void Play();
```

<a name='Tizen.UI.Animation.Play(float)'></a>

## Animation.Play(float) Method

Plays the animation from a specified progress.

```csharp
public void Play(float progress);
```
#### Parameters

<a name='Tizen.UI.Animation.Play(float).progress'></a>

`progress` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The progress from which the animation should start.

<a name='Tizen.UI.Animation.Play(int)'></a>

## Animation.Play(int) Method

Plays the animation after a specified delay.

```csharp
public void Play(int delayTime);
```
#### Parameters

<a name='Tizen.UI.Animation.Play(int).delayTime'></a>

`delayTime` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The delay before the animation starts in milliseconds.

<a name='Tizen.UI.Animation.PlayAsync()'></a>

## Animation.PlayAsync() Method

Plays the animation asynchronously.

```csharp
public System.Threading.Tasks.Task PlayAsync();
```

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')  
A Task that completes when the animation finishes.

<a name='Tizen.UI.Animation.Stop()'></a>

## Animation.Stop() Method

Stops the animation.

```csharp
public void Stop();
```
### Events

<a name='Tizen.UI.Animation.Finished'></a>

## Animation.Finished Event

Event triggered when the animation finishes.

```csharp
public event EventHandler Finished;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Animation.ProgressReached'></a>

## Animation.ProgressReached Event

Event triggered when the animation reaches the progress notification point.

```csharp
public event EventHandler ProgressReached;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')






