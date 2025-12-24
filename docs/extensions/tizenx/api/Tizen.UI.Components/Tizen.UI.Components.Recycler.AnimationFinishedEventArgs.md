### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## AnimationFinishedEventArgs Class

Event arguments for when an animation completes.

```csharp
public class AnimationFinishedEventArgs : System.EventArgs
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs') &#129106; AnimationFinishedEventArgs
### Constructors

<a name='Tizen.UI.Components.Recycler.AnimationFinishedEventArgs.AnimationFinishedEventArgs(Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.AnimationType)'></a>

## AnimationFinishedEventArgs(ViewHolder, AnimationType) Constructor

Constructor.

```csharp
public AnimationFinishedEventArgs(Tizen.UI.Components.Recycler.ViewHolder viewHolder, Tizen.UI.Components.Recycler.AnimationType animationType);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.AnimationFinishedEventArgs.AnimationFinishedEventArgs(Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.AnimationType).viewHolder'></a>

`viewHolder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder

<a name='Tizen.UI.Components.Recycler.AnimationFinishedEventArgs.AnimationFinishedEventArgs(Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.AnimationType).animationType'></a>

`animationType` [AnimationType](Tizen.UI.Components.Recycler.AnimationType.md 'Tizen.UI.Components.Recycler.AnimationType')

Types of animations
### Properties

<a name='Tizen.UI.Components.Recycler.AnimationFinishedEventArgs.AnimationType'></a>

## AnimationFinishedEventArgs.AnimationType Property

The type of animation that was performed.

```csharp
public Tizen.UI.Components.Recycler.AnimationType AnimationType { get; }
```

#### Property Value
[AnimationType](Tizen.UI.Components.Recycler.AnimationType.md 'Tizen.UI.Components.Recycler.AnimationType')

<a name='Tizen.UI.Components.Recycler.AnimationFinishedEventArgs.ViewHolder'></a>

## AnimationFinishedEventArgs.ViewHolder Property

The view holder that the animation was performed on.

```csharp
public Tizen.UI.Components.Recycler.ViewHolder ViewHolder { get; }
```

#### Property Value
[ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')


























































