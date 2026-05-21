### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## RotationGestureDetectedEventArgs Class

Event arguments for [RotationGesture](Tizen.UI.RotationGesture.md 'Tizen.UI.RotationGesture') event.

```csharp
public class RotationGestureDetectedEventArgs : Tizen.UI.GestureDetectedEventArgs
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs') &#129106; [GestureDetectedEventArgs](Tizen.UI.GestureDetectedEventArgs.md 'Tizen.UI.GestureDetectedEventArgs') &#129106; RotationGestureDetectedEventArgs
### Constructors

<a name='Tizen.UI.RotationGestureDetectedEventArgs.RotationGestureDetectedEventArgs(Tizen.UI.View,Tizen.UI.RotationGesture)'></a>

## RotationGestureDetectedEventArgs(View, RotationGesture) Constructor

Initializes a new instance of the [RotationGestureDetectedEventArgs](Tizen.UI.RotationGestureDetectedEventArgs.md 'Tizen.UI.RotationGestureDetectedEventArgs') class.

```csharp
public RotationGestureDetectedEventArgs(Tizen.UI.View view, Tizen.UI.RotationGesture gesture);
```
#### Parameters

<a name='Tizen.UI.RotationGestureDetectedEventArgs.RotationGestureDetectedEventArgs(Tizen.UI.View,Tizen.UI.RotationGesture).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view that the rotation gesture was detected on.

<a name='Tizen.UI.RotationGestureDetectedEventArgs.RotationGestureDetectedEventArgs(Tizen.UI.View,Tizen.UI.RotationGesture).gesture'></a>

`gesture` [RotationGesture](Tizen.UI.RotationGesture.md 'Tizen.UI.RotationGesture')

The rotation gesture that was detected.
### Properties

<a name='Tizen.UI.RotationGestureDetectedEventArgs.Gesture'></a>

## RotationGestureDetectedEventArgs.Gesture Property

Gets the rotation gesture that was detected.

```csharp
public Tizen.UI.RotationGesture Gesture { get; }
```

#### Property Value
[RotationGesture](Tizen.UI.RotationGesture.md 'Tizen.UI.RotationGesture')






