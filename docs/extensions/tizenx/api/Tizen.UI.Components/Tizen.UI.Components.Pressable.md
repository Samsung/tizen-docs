### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## Pressable Class

Pressable is a base class for components that can be pressed.  
It provides [PressedChanged](Tizen.UI.Components.Pressable.md#Tizen.UI.Components.Pressable.PressedChanged 'Tizen.UI.Components.Pressable.PressedChanged') event.

```csharp
public class Pressable : Tizen.UI.ContentView,
Tizen.UI.Components.IPressable,
Tizen.UI.Components.ITouchEffectTarget
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; Pressable

Derived  
&#8627; [Clickable](Tizen.UI.Components.Clickable.md 'Tizen.UI.Components.Clickable')  
&#8627; [InteractiveProgress](Tizen.UI.Components.InteractiveProgress.md 'Tizen.UI.Components.InteractiveProgress')  
&#8627; [PressableBox](Tizen.UI.Components.PressableBox.md 'Tizen.UI.Components.PressableBox')

Implements [IPressable](Tizen.UI.Components.IPressable.md 'Tizen.UI.Components.IPressable'), [ITouchEffectTarget](Tizen.UI.Components.ITouchEffectTarget.md 'Tizen.UI.Components.ITouchEffectTarget')
### Constructors

<a name='Tizen.UI.Components.Pressable.Pressable()'></a>

## Pressable() Constructor

Create an instance of Component.

```csharp
public Pressable();
```
### Properties

<a name='Tizen.UI.Components.Pressable.IsPressed'></a>

## Pressable.IsPressed Property

The boolean flag for pressed state.

```csharp
public bool IsPressed { get; set; }
```

Implements [IsPressed](Tizen.UI.Components.IPressable.md#Tizen.UI.Components.IPressable.IsPressed 'Tizen.UI.Components.IPressable.IsPressed')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Pressable.PressedChangedCommand'></a>

## Pressable.PressedChangedCommand Property

PressedChanged command. see [PressedChanged](Tizen.UI.Components.Pressable.md#Tizen.UI.Components.Pressable.PressedChanged 'Tizen.UI.Components.Pressable.PressedChanged').

```csharp
public System.Action&lt;object,Tizen.UI.Components.InputEventArgs> PressedChangedCommand { get; set; }
```

#### Property Value
[System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[InputEventArgs](Tizen.UI.Components.InputEventArgs.md 'Tizen.UI.Components.InputEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')
### Methods

<a name='Tizen.UI.Components.Pressable.GetTouchEffectSecondaryTarget()'></a>

## Pressable.GetTouchEffectSecondaryTarget() Method

Get the secondary target view to apply feedback.

```csharp
public virtual Tizen.UI.View GetTouchEffectSecondaryTarget();
```

Implements [GetTouchEffectSecondaryTarget()](Tizen.UI.Components.ITouchEffectTarget.md#Tizen.UI.Components.ITouchEffectTarget.GetTouchEffectSecondaryTarget() 'Tizen.UI.Components.ITouchEffectTarget.GetTouchEffectSecondaryTarget()')

#### Returns
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

<a name='Tizen.UI.Components.Pressable.GetTouchEffectTarget()'></a>

## Pressable.GetTouchEffectTarget() Method

Get the target view to apply feedback.

```csharp
public virtual Tizen.UI.View GetTouchEffectTarget();
```

Implements [GetTouchEffectTarget()](Tizen.UI.Components.ITouchEffectTarget.md#Tizen.UI.Components.ITouchEffectTarget.GetTouchEffectTarget() 'Tizen.UI.Components.ITouchEffectTarget.GetTouchEffectTarget()')

#### Returns
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')
### Events

<a name='Tizen.UI.Components.Pressable.PressedChanged'></a>

## Pressable.PressedChanged Event

The event that is called when the value of [IsPressed](Tizen.UI.Components.IPressable.md#Tizen.UI.Components.IPressable.IsPressed 'Tizen.UI.Components.IPressable.IsPressed') changes.

```csharp
public event EventHandler&lt;InputEventArgs> PressedChanged;
```

Implements [PressedChanged](Tizen.UI.Components.IPressable.md#Tizen.UI.Components.IPressable.PressedChanged 'Tizen.UI.Components.IPressable.PressedChanged')

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[InputEventArgs](Tizen.UI.Components.InputEventArgs.md 'Tizen.UI.Components.InputEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')


























































