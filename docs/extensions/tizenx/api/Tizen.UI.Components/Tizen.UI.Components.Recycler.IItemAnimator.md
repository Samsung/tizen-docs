### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## IItemAnimator Interface

An interface to animate changes to the views in a RecyclerView.

```csharp
public interface IItemAnimator
```

Derived  
&#8627; [DefaultItemAnimator](Tizen.UI.Components.Recycler.DefaultItemAnimator.md 'Tizen.UI.Components.Recycler.DefaultItemAnimator')
### Properties

<a name='Tizen.UI.Components.Recycler.IItemAnimator.RecyclerView'></a>

## IItemAnimator.RecyclerView Property

Sets the RecyclerView this animator is attached to.

```csharp
Tizen.UI.Components.Recycler.RecyclerView RecyclerView { get; set; }
```

#### Property Value
[RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView')
### Methods

<a name='Tizen.UI.Components.Recycler.IItemAnimator.AnimateAdd(Tizen.UI.Components.Recycler.ViewHolder)'></a>

## IItemAnimator.AnimateAdd(ViewHolder) Method

Called when a ViewHolder is about to be added.

```csharp
bool AnimateAdd(Tizen.UI.Components.Recycler.ViewHolder holder);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.IItemAnimator.AnimateAdd(Tizen.UI.Components.Recycler.ViewHolder).holder'></a>

`holder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder for the item being added.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the animator is ready to animate this change, false otherwise.

<a name='Tizen.UI.Components.Recycler.IItemAnimator.AnimateChange(Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float)'></a>

## IItemAnimator.AnimateChange(ViewHolder, ViewHolder, float, float, float, float) Method

Called when a ViewHolder is about to be changed (e.g., content updated, size changed).

```csharp
bool AnimateChange(Tizen.UI.Components.Recycler.ViewHolder oldHolder, Tizen.UI.Components.Recycler.ViewHolder newHolder, float fromX, float fromY, float toX, float toY);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.IItemAnimator.AnimateChange(Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).oldHolder'></a>

`oldHolder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder before the change.

<a name='Tizen.UI.Components.Recycler.IItemAnimator.AnimateChange(Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).newHolder'></a>

`newHolder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder after the change (can be the same as oldHolder).

<a name='Tizen.UI.Components.Recycler.IItemAnimator.AnimateChange(Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).fromX'></a>

`fromX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

Start X position.

<a name='Tizen.UI.Components.Recycler.IItemAnimator.AnimateChange(Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).fromY'></a>

`fromY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

Start Y position.

<a name='Tizen.UI.Components.Recycler.IItemAnimator.AnimateChange(Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).toX'></a>

`toX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

End X position.

<a name='Tizen.UI.Components.Recycler.IItemAnimator.AnimateChange(Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).toY'></a>

`toY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

End Y position.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the animator is ready to animate this change, false otherwise.

<a name='Tizen.UI.Components.Recycler.IItemAnimator.AnimateMove(Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float)'></a>

## IItemAnimator.AnimateMove(ViewHolder, float, float, float, float) Method

Called when a ViewHolder is about to be moved.

```csharp
bool AnimateMove(Tizen.UI.Components.Recycler.ViewHolder holder, float fromX, float fromY, float toX, float toY);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.IItemAnimator.AnimateMove(Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).holder'></a>

`holder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder for the item being moved.

<a name='Tizen.UI.Components.Recycler.IItemAnimator.AnimateMove(Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).fromX'></a>

`fromX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

Start X position.

<a name='Tizen.UI.Components.Recycler.IItemAnimator.AnimateMove(Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).fromY'></a>

`fromY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

Start Y position.

<a name='Tizen.UI.Components.Recycler.IItemAnimator.AnimateMove(Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).toX'></a>

`toX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

End X position.

<a name='Tizen.UI.Components.Recycler.IItemAnimator.AnimateMove(Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).toY'></a>

`toY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

End Y position.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the animator is ready to animate this change, false otherwise.

<a name='Tizen.UI.Components.Recycler.IItemAnimator.AnimateRemove(Tizen.UI.Components.Recycler.ViewHolder)'></a>

## IItemAnimator.AnimateRemove(ViewHolder) Method

Called when a ViewHolder is about to be removed.

```csharp
bool AnimateRemove(Tizen.UI.Components.Recycler.ViewHolder holder);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.IItemAnimator.AnimateRemove(Tizen.UI.Components.Recycler.ViewHolder).holder'></a>

`holder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder for the item being removed.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the animator is ready to animate this change, false otherwise.

<a name='Tizen.UI.Components.Recycler.IItemAnimator.EndAnimation(Tizen.UI.Components.Recycler.ViewHolder)'></a>

## IItemAnimator.EndAnimation(ViewHolder) Method

Ends the animation for a specific ViewHolder.

```csharp
void EndAnimation(Tizen.UI.Components.Recycler.ViewHolder item);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.IItemAnimator.EndAnimation(Tizen.UI.Components.Recycler.ViewHolder).item'></a>

`item` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder whose animation should be ended.

<a name='Tizen.UI.Components.Recycler.IItemAnimator.EndAnimations()'></a>

## IItemAnimator.EndAnimations() Method

Ends all current animations.

```csharp
void EndAnimations();
```

<a name='Tizen.UI.Components.Recycler.IItemAnimator.IsRunning(Tizen.UI.Components.Recycler.ViewHolder)'></a>

## IItemAnimator.IsRunning(ViewHolder) Method

Checks if any animation is running for a specific ViewHolder.

```csharp
bool IsRunning(Tizen.UI.Components.Recycler.ViewHolder item);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.IItemAnimator.IsRunning(Tizen.UI.Components.Recycler.ViewHolder).item'></a>

`item` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder to check.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if an animation is active for the item, false otherwise.

<a name='Tizen.UI.Components.Recycler.IItemAnimator.RunPendingAnimations()'></a>

## IItemAnimator.RunPendingAnimations() Method

Runs all pending animations.

```csharp
void RunPendingAnimations();
```
### Events

<a name='Tizen.UI.Components.Recycler.IItemAnimator.AnimationFinished'></a>

## IItemAnimator.AnimationFinished Event

Listener for animation finished.

```csharp
event EventHandler&lt;AnimationFinishedEventArgs> AnimationFinished;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[AnimationFinishedEventArgs](Tizen.UI.Components.Recycler.AnimationFinishedEventArgs.md 'Tizen.UI.Components.Recycler.AnimationFinishedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')


























































