### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## LongPressGestureDetectedEventArgs Class

Event arguments for [LongPressGesture](Tizen.UI.LongPressGesture.md 'Tizen.UI.LongPressGesture') event.

```csharp
public class LongPressGestureDetectedEventArgs : Tizen.UI.GestureDetectedEventArgs
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs') &#129106; [GestureDetectedEventArgs](Tizen.UI.GestureDetectedEventArgs.md 'Tizen.UI.GestureDetectedEventArgs') &#129106; LongPressGestureDetectedEventArgs
### Constructors

<a name='Tizen.UI.LongPressGestureDetectedEventArgs.LongPressGestureDetectedEventArgs(Tizen.UI.View,Tizen.UI.LongPressGesture)'></a>

## LongPressGestureDetectedEventArgs(View, LongPressGesture) Constructor

Initializes a new instance of the [LongPressGestureDetectedEventArgs](Tizen.UI.LongPressGestureDetectedEventArgs.md 'Tizen.UI.LongPressGestureDetectedEventArgs') class.

```csharp
public LongPressGestureDetectedEventArgs(Tizen.UI.View view, Tizen.UI.LongPressGesture gesture);
```
#### Parameters

<a name='Tizen.UI.LongPressGestureDetectedEventArgs.LongPressGestureDetectedEventArgs(Tizen.UI.View,Tizen.UI.LongPressGesture).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The [View](Tizen.UI.View.md 'Tizen.UI.View') that detected the [LongPressGesture](Tizen.UI.LongPressGesture.md 'Tizen.UI.LongPressGesture').

<a name='Tizen.UI.LongPressGestureDetectedEventArgs.LongPressGestureDetectedEventArgs(Tizen.UI.View,Tizen.UI.LongPressGesture).gesture'></a>

`gesture` [LongPressGesture](Tizen.UI.LongPressGesture.md 'Tizen.UI.LongPressGesture')

The [LongPressGesture](Tizen.UI.LongPressGesture.md 'Tizen.UI.LongPressGesture') object that contains information about the detected gesture.
### Properties

<a name='Tizen.UI.LongPressGestureDetectedEventArgs.Gesture'></a>

## LongPressGestureDetectedEventArgs.Gesture Property

Gets the [LongPressGesture](Tizen.UI.LongPressGesture.md 'Tizen.UI.LongPressGesture') object that contains information about the detected gesture.

```csharp
public Tizen.UI.LongPressGesture Gesture { get; }
```

#### Property Value
[LongPressGesture](Tizen.UI.LongPressGesture.md 'Tizen.UI.LongPressGesture')






