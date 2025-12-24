### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## PanGestureDetectedEventArgs Class

Event arguments for [PanGesture](Tizen.UI.PanGesture.md 'Tizen.UI.PanGesture') event.

```csharp
public class PanGestureDetectedEventArgs : Tizen.UI.GestureDetectedEventArgs
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs') &#129106; [GestureDetectedEventArgs](Tizen.UI.GestureDetectedEventArgs.md 'Tizen.UI.GestureDetectedEventArgs') &#129106; PanGestureDetectedEventArgs
### Constructors

<a name='Tizen.UI.PanGestureDetectedEventArgs.PanGestureDetectedEventArgs(Tizen.UI.View,Tizen.UI.PanGesture)'></a>

## PanGestureDetectedEventArgs(View, PanGesture) Constructor

Initializes a new instance of the [PanGestureDetectedEventArgs](Tizen.UI.PanGestureDetectedEventArgs.md 'Tizen.UI.PanGestureDetectedEventArgs') class.

```csharp
public PanGestureDetectedEventArgs(Tizen.UI.View view, Tizen.UI.PanGesture gesture);
```
#### Parameters

<a name='Tizen.UI.PanGestureDetectedEventArgs.PanGestureDetectedEventArgs(Tizen.UI.View,Tizen.UI.PanGesture).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view that detected the [PanGesture](Tizen.UI.PanGesture.md 'Tizen.UI.PanGesture').

<a name='Tizen.UI.PanGestureDetectedEventArgs.PanGestureDetectedEventArgs(Tizen.UI.View,Tizen.UI.PanGesture).gesture'></a>

`gesture` [PanGesture](Tizen.UI.PanGesture.md 'Tizen.UI.PanGesture')

The [PanGesture](Tizen.UI.PanGesture.md 'Tizen.UI.PanGesture') object that contains information about the detected gesture.
### Properties

<a name='Tizen.UI.PanGestureDetectedEventArgs.Gesture'></a>

## PanGestureDetectedEventArgs.Gesture Property

Gets the [PanGesture](Tizen.UI.PanGesture.md 'Tizen.UI.PanGesture') object that contains information about the detected gesture.

```csharp
public Tizen.UI.PanGesture Gesture { get; }
```

#### Property Value
[PanGesture](Tizen.UI.PanGesture.md 'Tizen.UI.PanGesture')






