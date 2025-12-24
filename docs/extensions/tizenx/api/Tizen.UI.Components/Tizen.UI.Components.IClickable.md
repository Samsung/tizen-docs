### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## IClickable Interface

Clickable element interface.

```csharp
public interface IClickable
```

Derived  
&#8627; [Clickable](Tizen.UI.Components.Clickable.md 'Tizen.UI.Components.Clickable')
### Properties

<a name='Tizen.UI.Components.IClickable.ClickedCommand'></a>

## IClickable.ClickedCommand Property

Clicked command. see [Clicked](Tizen.UI.Components.IClickable.md#Tizen.UI.Components.IClickable.Clicked 'Tizen.UI.Components.IClickable.Clicked').

```csharp
System.Action&lt;object,Tizen.UI.Components.InputEventArgs> ClickedCommand { get; set; }
```

#### Property Value
[System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[InputEventArgs](Tizen.UI.Components.InputEventArgs.md 'Tizen.UI.Components.InputEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')
### Events

<a name='Tizen.UI.Components.IClickable.Clicked'></a>

## IClickable.Clicked Event

Clicked event is raised when the element is clicked.

```csharp
event EventHandler&lt;InputEventArgs> Clicked;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[InputEventArgs](Tizen.UI.Components.InputEventArgs.md 'Tizen.UI.Components.InputEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')


























































