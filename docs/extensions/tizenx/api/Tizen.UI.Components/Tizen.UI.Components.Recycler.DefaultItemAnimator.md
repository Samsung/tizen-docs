### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## DefaultItemAnimator Class

Default implementation of IItemAnimator.

```csharp
public class DefaultItemAnimator :
Tizen.UI.Components.Recycler.IItemAnimator
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; DefaultItemAnimator

Implements [IItemAnimator](Tizen.UI.Components.Recycler.IItemAnimator.md 'Tizen.UI.Components.Recycler.IItemAnimator')
### Properties

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.RecyclerView'></a>

## DefaultItemAnimator.RecyclerView Property

The RecyclerView instance that owns this ItemAnimator. Required for recycling views.

```csharp
public Tizen.UI.Components.Recycler.RecyclerView RecyclerView { get; set; }
```

Implements [RecyclerView](Tizen.UI.Components.Recycler.IItemAnimator.md#Tizen.UI.Components.Recycler.IItemAnimator.RecyclerView 'Tizen.UI.Components.Recycler.IItemAnimator.RecyclerView')

#### Property Value
[RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView')
### Methods

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.AnimateAdd(Tizen.UI.Components.Recycler.ViewHolder)'></a>

## DefaultItemAnimator.AnimateAdd(ViewHolder) Method

Called when a ViewHolder is about to be added.

```csharp
public bool AnimateAdd(Tizen.UI.Components.Recycler.ViewHolder holder);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.AnimateAdd(Tizen.UI.Components.Recycler.ViewHolder).holder'></a>

`holder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder for the item being added.

Implements [AnimateAdd(ViewHolder)](Tizen.UI.Components.Recycler.IItemAnimator.md#Tizen.UI.Components.Recycler.IItemAnimator.AnimateAdd(Tizen.UI.Components.Recycler.ViewHolder) 'Tizen.UI.Components.Recycler.IItemAnimator.AnimateAdd(Tizen.UI.Components.Recycler.ViewHolder)')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the animator is ready to animate this change, false otherwise.

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.AnimateChange(Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float)'></a>

## DefaultItemAnimator.AnimateChange(ViewHolder, ViewHolder, float, float, float, float) Method

Called when a ViewHolder is about to be changed (e.g., content updated, size changed).

```csharp
public bool AnimateChange(Tizen.UI.Components.Recycler.ViewHolder oldHolder, Tizen.UI.Components.Recycler.ViewHolder newHolder, float fromX, float fromY, float toX, float toY);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.AnimateChange(Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).oldHolder'></a>

`oldHolder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder before the change.

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.AnimateChange(Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).newHolder'></a>

`newHolder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder after the change (can be the same as oldHolder).

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.AnimateChange(Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).fromX'></a>

`fromX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

Start X position.

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.AnimateChange(Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).fromY'></a>

`fromY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

Start Y position.

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.AnimateChange(Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).toX'></a>

`toX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

End X position.

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.AnimateChange(Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).toY'></a>

`toY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

End Y position.

Implements [AnimateChange(ViewHolder, ViewHolder, float, float, float, float)](Tizen.UI.Components.Recycler.IItemAnimator.md#Tizen.UI.Components.Recycler.IItemAnimator.AnimateChange(Tizen.UI.Components.Recycler.ViewHolder,Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float) 'Tizen.UI.Components.Recycler.IItemAnimator.AnimateChange(Tizen.UI.Components.Recycler.ViewHolder, Tizen.UI.Components.Recycler.ViewHolder, float, float, float, float)')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the animator is ready to animate this change, false otherwise.

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.AnimateMove(Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float)'></a>

## DefaultItemAnimator.AnimateMove(ViewHolder, float, float, float, float) Method

Called when a ViewHolder is about to be moved.

```csharp
public bool AnimateMove(Tizen.UI.Components.Recycler.ViewHolder holder, float fromX, float fromY, float toX, float toY);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.AnimateMove(Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).holder'></a>

`holder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder for the item being moved.

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.AnimateMove(Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).fromX'></a>

`fromX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

Start X position.

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.AnimateMove(Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).fromY'></a>

`fromY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

Start Y position.

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.AnimateMove(Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).toX'></a>

`toX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

End X position.

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.AnimateMove(Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float).toY'></a>

`toY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

End Y position.

Implements [AnimateMove(ViewHolder, float, float, float, float)](Tizen.UI.Components.Recycler.IItemAnimator.md#Tizen.UI.Components.Recycler.IItemAnimator.AnimateMove(Tizen.UI.Components.Recycler.ViewHolder,float,float,float,float) 'Tizen.UI.Components.Recycler.IItemAnimator.AnimateMove(Tizen.UI.Components.Recycler.ViewHolder, float, float, float, float)')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the animator is ready to animate this change, false otherwise.

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.AnimateRemove(Tizen.UI.Components.Recycler.ViewHolder)'></a>

## DefaultItemAnimator.AnimateRemove(ViewHolder) Method

Called when a ViewHolder is about to be removed.

```csharp
public bool AnimateRemove(Tizen.UI.Components.Recycler.ViewHolder holder);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.AnimateRemove(Tizen.UI.Components.Recycler.ViewHolder).holder'></a>

`holder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder for the item being removed.

Implements [AnimateRemove(ViewHolder)](Tizen.UI.Components.Recycler.IItemAnimator.md#Tizen.UI.Components.Recycler.IItemAnimator.AnimateRemove(Tizen.UI.Components.Recycler.ViewHolder) 'Tizen.UI.Components.Recycler.IItemAnimator.AnimateRemove(Tizen.UI.Components.Recycler.ViewHolder)')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the animator is ready to animate this change, false otherwise.

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.EndAnimation(Tizen.UI.Components.Recycler.ViewHolder)'></a>

## DefaultItemAnimator.EndAnimation(ViewHolder) Method

Ends the animation for a specific ViewHolder.

```csharp
public void EndAnimation(Tizen.UI.Components.Recycler.ViewHolder item);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.EndAnimation(Tizen.UI.Components.Recycler.ViewHolder).item'></a>

`item` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder whose animation should be ended.

Implements [EndAnimation(ViewHolder)](Tizen.UI.Components.Recycler.IItemAnimator.md#Tizen.UI.Components.Recycler.IItemAnimator.EndAnimation(Tizen.UI.Components.Recycler.ViewHolder) 'Tizen.UI.Components.Recycler.IItemAnimator.EndAnimation(Tizen.UI.Components.Recycler.ViewHolder)')

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.EndAnimations()'></a>

## DefaultItemAnimator.EndAnimations() Method

Ends all current animations.

```csharp
public void EndAnimations();
```

Implements [EndAnimations()](Tizen.UI.Components.Recycler.IItemAnimator.md#Tizen.UI.Components.Recycler.IItemAnimator.EndAnimations() 'Tizen.UI.Components.Recycler.IItemAnimator.EndAnimations()')

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.IsRunning(Tizen.UI.Components.Recycler.ViewHolder)'></a>

## DefaultItemAnimator.IsRunning(ViewHolder) Method

Checks if any animation is running for a specific ViewHolder.

```csharp
public bool IsRunning(Tizen.UI.Components.Recycler.ViewHolder item);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.IsRunning(Tizen.UI.Components.Recycler.ViewHolder).item'></a>

`item` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder to check.

Implements [IsRunning(ViewHolder)](Tizen.UI.Components.Recycler.IItemAnimator.md#Tizen.UI.Components.Recycler.IItemAnimator.IsRunning(Tizen.UI.Components.Recycler.ViewHolder) 'Tizen.UI.Components.Recycler.IItemAnimator.IsRunning(Tizen.UI.Components.Recycler.ViewHolder)')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if an animation is active for the item, false otherwise.

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.RunPendingAnimations()'></a>

## DefaultItemAnimator.RunPendingAnimations() Method

Runs all pending animations.

```csharp
public void RunPendingAnimations();
```

Implements [RunPendingAnimations()](Tizen.UI.Components.Recycler.IItemAnimator.md#Tizen.UI.Components.Recycler.IItemAnimator.RunPendingAnimations() 'Tizen.UI.Components.Recycler.IItemAnimator.RunPendingAnimations()')
### Events

<a name='Tizen.UI.Components.Recycler.DefaultItemAnimator.AnimationFinished'></a>

## DefaultItemAnimator.AnimationFinished Event

Event raised when an animation has finished. Useful for cleaning up resources.

```csharp
public event EventHandler&lt;AnimationFinishedEventArgs> AnimationFinished;
```

Implements [AnimationFinished](Tizen.UI.Components.Recycler.IItemAnimator.md#Tizen.UI.Components.Recycler.IItemAnimator.AnimationFinished 'Tizen.UI.Components.Recycler.IItemAnimator.AnimationFinished')

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[AnimationFinishedEventArgs](Tizen.UI.Components.Recycler.AnimationFinishedEventArgs.md 'Tizen.UI.Components.Recycler.AnimationFinishedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')


























































