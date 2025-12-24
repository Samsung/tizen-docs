### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## RecycleScroller Class

RecyclerView Scroller class. It handles the scrolling behavior of the RecyclerView.

```csharp
public class RecycleScroller : Tizen.UI.ViewGroup
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ViewGroup](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ViewGroup 'Tizen.UI.ViewGroup') &#129106; RecycleScroller
### Constructors

<a name='Tizen.UI.Components.Recycler.RecycleScroller.RecycleScroller(Tizen.UI.Components.Recycler.RecyclerView)'></a>

## RecycleScroller(RecyclerView) Constructor

Constructor of RecycleScroller. It initializes the properties and adds the scroller to the RecyclerView.

```csharp
public RecycleScroller(Tizen.UI.Components.Recycler.RecyclerView recyclerView);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.RecycleScroller.RecycleScroller(Tizen.UI.Components.Recycler.RecyclerView).recyclerView'></a>

`recyclerView` [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView')
### Properties

<a name='Tizen.UI.Components.Recycler.RecycleScroller.CurrentViewPort'></a>

## RecycleScroller.CurrentViewPort Property

The current view port area of the scroller. It represents the current scroll position and size of the RecyclerView.

```csharp
public Tizen.UI.Rect CurrentViewPort { get; }
```

#### Property Value
[Tizen.UI.Rect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Rect 'Tizen.UI.Rect')

<a name='Tizen.UI.Components.Recycler.RecycleScroller.IsScrollAnimationStarted'></a>

## RecycleScroller.IsScrollAnimationStarted Property

Indicates whether the scroll animation is started or not. If it is started, the RecyclerView is scrolling.

```csharp
public bool IsScrollAnimationStarted { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.RecycleScroller.RecycleBody'></a>

## RecycleScroller.RecycleBody Property

Child bodies with recycling in the scroller.

```csharp
public System.Collections.Generic.IList&lt;Tizen.UI.View> RecycleBody { get; }
```

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

<a name='Tizen.UI.Components.Recycler.RecycleScroller.ScrollX'></a>

## RecycleScroller.ScrollX Property

Get the scroll x position of the scroller.

```csharp
public float ScrollX { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Recycler.RecycleScroller.ScrollY'></a>

## RecycleScroller.ScrollY Property

Get the scroll y position of the scroller.

```csharp
public float ScrollY { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Recycler.RecycleScroller.ViewPort'></a>

## RecycleScroller.ViewPort Property

The view port area of the scroller. It represents the scroll position and size of the RecyclerView.

```csharp
public Tizen.UI.Rect ViewPort { get; }
```

#### Property Value
[Tizen.UI.Rect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Rect 'Tizen.UI.Rect')
### Methods

<a name='Tizen.UI.Components.Recycler.RecycleScroller.AddBody(Tizen.UI.View)'></a>

## RecycleScroller.AddBody(View) Method

Add the body view to the scroller.

```csharp
public void AddBody(Tizen.UI.View child);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.RecycleScroller.AddBody(Tizen.UI.View).child'></a>

`child` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The child body view to add.

<a name='Tizen.UI.Components.Recycler.RecycleScroller.AdjustChildPosition(float,float,System.Func_Tizen.UI.View,bool_)'></a>

## RecycleScroller.AdjustChildPosition(float, float, Func&lt;View,bool>) Method

Add the child view in specific conditions.

```csharp
public void AdjustChildPosition(float dx, float dy, System.Func&lt;Tizen.UI.View,bool> condition);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.RecycleScroller.AdjustChildPosition(float,float,System.Func_Tizen.UI.View,bool_).dx'></a>

`dx` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The horizontal distance to adjust.

<a name='Tizen.UI.Components.Recycler.RecycleScroller.AdjustChildPosition(float,float,System.Func_Tizen.UI.View,bool_).dy'></a>

`dy` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The vertical distance to adjust.

<a name='Tizen.UI.Components.Recycler.RecycleScroller.AdjustChildPosition(float,float,System.Func_Tizen.UI.View,bool_).condition'></a>

`condition` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

The condition to adjust the child view.

<a name='Tizen.UI.Components.Recycler.RecycleScroller.AdjustScrollPosition(float,float)'></a>

## RecycleScroller.AdjustScrollPosition(float, float) Method

Adjust the scroll position by the specified distance. It moves the scroller and all its children by the specified distance.

```csharp
public void AdjustScrollPosition(float dx, float dy);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.RecycleScroller.AdjustScrollPosition(float,float).dx'></a>

`dx` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The horizontal distance to adjust.

<a name='Tizen.UI.Components.Recycler.RecycleScroller.AdjustScrollPosition(float,float).dy'></a>

`dy` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The vertical distance to adjust.

<a name='Tizen.UI.Components.Recycler.RecycleScroller.Initialize()'></a>

## RecycleScroller.Initialize() Method

Initialize the scroller position.

```csharp
public void Initialize();
```

<a name='Tizen.UI.Components.Recycler.RecycleScroller.MoveBy(float,float)'></a>

## RecycleScroller.MoveBy(float, float) Method

Move the scroller by the specified distance.

```csharp
public void MoveBy(float x, float y);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.RecycleScroller.MoveBy(float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The horizontal distance to move.

<a name='Tizen.UI.Components.Recycler.RecycleScroller.MoveBy(float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The vertical distance to move.

<a name='Tizen.UI.Components.Recycler.RecycleScroller.RemoveBody(Tizen.UI.View)'></a>

## RecycleScroller.RemoveBody(View) Method

Remove the body view from the scroller.

```csharp
public void RemoveBody(Tizen.UI.View child);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.RecycleScroller.RemoveBody(Tizen.UI.View).child'></a>

`child` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The child body view to remove.

<a name='Tizen.UI.Components.Recycler.RecycleScroller.ScrollBy(float,float,int,Tizen.UI.AlphaFunction)'></a>

## RecycleScroller.ScrollBy(float, float, int, AlphaFunction) Method

Scroll the scroller by the specified distance with animation.

```csharp
public System.Threading.Tasks.Task ScrollBy(float x, float y, int duration=0, Tizen.UI.AlphaFunction alpha=null);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.RecycleScroller.ScrollBy(float,float,int,Tizen.UI.AlphaFunction).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The horizontal distance to scroll.

<a name='Tizen.UI.Components.Recycler.RecycleScroller.ScrollBy(float,float,int,Tizen.UI.AlphaFunction).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The vertical distance to scroll.

<a name='Tizen.UI.Components.Recycler.RecycleScroller.ScrollBy(float,float,int,Tizen.UI.AlphaFunction).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The duration of the animation.

<a name='Tizen.UI.Components.Recycler.RecycleScroller.ScrollBy(float,float,int,Tizen.UI.AlphaFunction).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function of the animation.

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')  
A task representing the asynchronous operation.

<a name='Tizen.UI.Components.Recycler.RecycleScroller.ScrollStop()'></a>

## RecycleScroller.ScrollStop() Method

Stop the scroll animation.

```csharp
public void ScrollStop();
```
### Events

<a name='Tizen.UI.Components.Recycler.RecycleScroller.ScrollAnimationCanceled'></a>

## RecycleScroller.ScrollAnimationCanceled Event

Event for scroll animation canceled. Invoked when the scroll animation cancels.

```csharp
public event EventHandler ScrollAnimationCanceled;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.Recycler.RecycleScroller.ScrollAnimationFinished'></a>

## RecycleScroller.ScrollAnimationFinished Event

Event for scroll animation finished. Invoked when the scroll animation finishs.

```csharp
public event EventHandler ScrollAnimationFinished;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.Recycler.RecycleScroller.ScrollAnimationStarted'></a>

## RecycleScroller.ScrollAnimationStarted Event

Event for scroll animation started. Invoked when the scroll animation starts.

```csharp
public event EventHandler ScrollAnimationStarted;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.Recycler.RecycleScroller.Scrolling'></a>

## RecycleScroller.Scrolling Event

Event for scrolling. Invoked when scrolling happens.

```csharp
public event EventHandler&lt;ScrollEventArgs> Scrolling;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.ScrollEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ScrollEventArgs 'Tizen.UI.ScrollEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')


























































