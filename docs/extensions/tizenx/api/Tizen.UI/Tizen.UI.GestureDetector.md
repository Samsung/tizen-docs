### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## GestureDetector Class

The GestureDetector class is an abstract class that detects gestures on a View.

```csharp
public abstract class GestureDetector : Tizen.UI.NObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; GestureDetector

Derived  
&#8627; [LongPressGestureDetector](Tizen.UI.LongPressGestureDetector.md 'Tizen.UI.LongPressGestureDetector')  
&#8627; [PanGestureDetector](Tizen.UI.PanGestureDetector.md 'Tizen.UI.PanGestureDetector')  
&#8627; [PinchGestureDetector](Tizen.UI.PinchGestureDetector.md 'Tizen.UI.PinchGestureDetector')  
&#8627; [RotationGestureDetector](Tizen.UI.RotationGestureDetector.md 'Tizen.UI.RotationGestureDetector')  
&#8627; [TapGestureDetector](Tizen.UI.TapGestureDetector.md 'Tizen.UI.TapGestureDetector')
### Methods

<a name='Tizen.UI.GestureDetector.Attach(Tizen.UI.View)'></a>

## GestureDetector.Attach(View) Method

Attaches the gesture detector to the specified view.

```csharp
public void Attach(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.GestureDetector.Attach(Tizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to attach the gesture detector to.

<a name='Tizen.UI.GestureDetector.Detach(Tizen.UI.View)'></a>

## GestureDetector.Detach(View) Method

Detaches the gesture detector from the specified view.

```csharp
public void Detach(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.GestureDetector.Detach(Tizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to detach the gesture detector from.

<a name='Tizen.UI.GestureDetector.DetachAll()'></a>

## GestureDetector.DetachAll() Method

Detaches all attached views from the gesture detector.

```csharp
public void DetachAll();
```





