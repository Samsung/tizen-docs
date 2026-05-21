### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## GestureDetectedEventArgs Class

A base event arguments for gesture events.

```csharp
public abstract class GestureDetectedEventArgs : System.EventArgs
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs') &#129106; GestureDetectedEventArgs

Derived  
&#8627; [LongPressGestureDetectedEventArgs](Tizen.UI.LongPressGestureDetectedEventArgs.md 'Tizen.UI.LongPressGestureDetectedEventArgs')  
&#8627; [PanGestureDetectedEventArgs](Tizen.UI.PanGestureDetectedEventArgs.md 'Tizen.UI.PanGestureDetectedEventArgs')  
&#8627; [PinchGestureDetectedEventArgs](Tizen.UI.PinchGestureDetectedEventArgs.md 'Tizen.UI.PinchGestureDetectedEventArgs')  
&#8627; [RotationGestureDetectedEventArgs](Tizen.UI.RotationGestureDetectedEventArgs.md 'Tizen.UI.RotationGestureDetectedEventArgs')  
&#8627; [TapGestureDetectedEventArgs](Tizen.UI.TapGestureDetectedEventArgs.md 'Tizen.UI.TapGestureDetectedEventArgs')
### Properties

<a name='Tizen.UI.GestureDetectedEventArgs.Handled'></a>

## GestureDetectedEventArgs.Handled Property

Gets or sets a value indicating whether the gesture has been handled by the view.

```csharp
public bool Handled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the gesture has been handled, false otherwise.

<a name='Tizen.UI.GestureDetectedEventArgs.View'></a>

## GestureDetectedEventArgs.View Property

Gets the [View](Tizen.UI.GestureDetectedEventArgs.md#Tizen.UI.GestureDetectedEventArgs.View 'Tizen.UI.GestureDetectedEventArgs.View') that detected the gesture.

```csharp
public Tizen.UI.View View { get; }
```

#### Property Value
[View](Tizen.UI.View.md 'Tizen.UI.View')






