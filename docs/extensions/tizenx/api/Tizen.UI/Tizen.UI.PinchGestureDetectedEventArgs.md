### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## PinchGestureDetectedEventArgs Class

Event arguments for [PinchGesture](Tizen.UI.PinchGesture.md 'Tizen.UI.PinchGesture') event.

```csharp
public class PinchGestureDetectedEventArgs : Tizen.UI.GestureDetectedEventArgs
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs') &#129106; [GestureDetectedEventArgs](Tizen.UI.GestureDetectedEventArgs.md 'Tizen.UI.GestureDetectedEventArgs') &#129106; PinchGestureDetectedEventArgs
### Constructors

<a name='Tizen.UI.PinchGestureDetectedEventArgs.PinchGestureDetectedEventArgs(Tizen.UI.View,Tizen.UI.PinchGesture)'></a>

## PinchGestureDetectedEventArgs(View, PinchGesture) Constructor

Initializes a new instance of the [PinchGestureDetectedEventArgs](Tizen.UI.PinchGestureDetectedEventArgs.md 'Tizen.UI.PinchGestureDetectedEventArgs') class.

```csharp
public PinchGestureDetectedEventArgs(Tizen.UI.View view, Tizen.UI.PinchGesture gesture);
```
#### Parameters

<a name='Tizen.UI.PinchGestureDetectedEventArgs.PinchGestureDetectedEventArgs(Tizen.UI.View,Tizen.UI.PinchGesture).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The [View](Tizen.UI.View.md 'Tizen.UI.View') that detected the [PinchGesture](Tizen.UI.PinchGesture.md 'Tizen.UI.PinchGesture').

<a name='Tizen.UI.PinchGestureDetectedEventArgs.PinchGestureDetectedEventArgs(Tizen.UI.View,Tizen.UI.PinchGesture).gesture'></a>

`gesture` [PinchGesture](Tizen.UI.PinchGesture.md 'Tizen.UI.PinchGesture')

The [PinchGesture](Tizen.UI.PinchGesture.md 'Tizen.UI.PinchGesture') object that contains information about the detected gesture.
### Properties

<a name='Tizen.UI.PinchGestureDetectedEventArgs.Gesture'></a>

## PinchGestureDetectedEventArgs.Gesture Property

Gets the [PinchGesture](Tizen.UI.PinchGesture.md 'Tizen.UI.PinchGesture') object that contains information about the detected gesture.

```csharp
public Tizen.UI.PinchGesture Gesture { get; }
```

#### Property Value
[PinchGesture](Tizen.UI.PinchGesture.md 'Tizen.UI.PinchGesture')






