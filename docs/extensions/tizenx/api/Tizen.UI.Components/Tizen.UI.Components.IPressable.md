### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## IPressable Interface

Represents pressable element.  
All derived class of [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') that implements this interface can have [Pressed](Tizen.UI.Components.UIState.md#Tizen.UI.Components.UIState.Pressed 'Tizen.UI.Components.UIState.Pressed') state when [IsPressed](Tizen.UI.Components.IPressable.md#Tizen.UI.Components.IPressable.IsPressed 'Tizen.UI.Components.IPressable.IsPressed') is true.

```csharp
public interface IPressable
```

Derived  
&#8627; [Pressable](Tizen.UI.Components.Pressable.md 'Tizen.UI.Components.Pressable')
### Properties

<a name='Tizen.UI.Components.IPressable.IsPressed'></a>

## IPressable.IsPressed Property

Indicates whether it is pressed or not.

```csharp
bool IsPressed { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')
### Events

<a name='Tizen.UI.Components.IPressable.PressedChanged'></a>

## IPressable.PressedChanged Event

The event that is called when the value of [IsPressed](Tizen.UI.Components.IPressable.md#Tizen.UI.Components.IPressable.IsPressed 'Tizen.UI.Components.IPressable.IsPressed') changes.

```csharp
event EventHandler&lt;InputEventArgs> PressedChanged;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[InputEventArgs](Tizen.UI.Components.InputEventArgs.md 'Tizen.UI.Components.InputEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')


























































