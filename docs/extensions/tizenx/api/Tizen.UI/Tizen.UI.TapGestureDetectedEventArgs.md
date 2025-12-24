### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## TapGestureDetectedEventArgs Class

Event arguments for [TapGesture](Tizen.UI.TapGesture.md 'Tizen.UI.TapGesture') event.

```csharp
public class TapGestureDetectedEventArgs : Tizen.UI.GestureDetectedEventArgs
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs') &#129106; [GestureDetectedEventArgs](Tizen.UI.GestureDetectedEventArgs.md 'Tizen.UI.GestureDetectedEventArgs') &#129106; TapGestureDetectedEventArgs
### Constructors

<a name='Tizen.UI.TapGestureDetectedEventArgs.TapGestureDetectedEventArgs(Tizen.UI.View,Tizen.UI.TapGesture)'></a>

## TapGestureDetectedEventArgs(View, TapGesture) Constructor

Initializes a new instance of the [TapGestureDetectedEventArgs](Tizen.UI.TapGestureDetectedEventArgs.md 'Tizen.UI.TapGestureDetectedEventArgs') class.

```csharp
public TapGestureDetectedEventArgs(Tizen.UI.View view, Tizen.UI.TapGesture tapGesture);
```
#### Parameters

<a name='Tizen.UI.TapGestureDetectedEventArgs.TapGestureDetectedEventArgs(Tizen.UI.View,Tizen.UI.TapGesture).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view that the tap gesture was detected on.

<a name='Tizen.UI.TapGestureDetectedEventArgs.TapGestureDetectedEventArgs(Tizen.UI.View,Tizen.UI.TapGesture).tapGesture'></a>

`tapGesture` [TapGesture](Tizen.UI.TapGesture.md 'Tizen.UI.TapGesture')

The tap gesture that was detected.
### Properties

<a name='Tizen.UI.TapGestureDetectedEventArgs.Gesture'></a>

## TapGestureDetectedEventArgs.Gesture Property

Gets the tap gesture that was detected.

```csharp
public Tizen.UI.TapGesture Gesture { get; }
```

#### Property Value
[TapGesture](Tizen.UI.TapGesture.md 'Tizen.UI.TapGesture')






