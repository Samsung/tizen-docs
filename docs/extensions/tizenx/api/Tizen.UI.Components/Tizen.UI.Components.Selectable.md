### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## Selectable Class

SelectableComponent.  
It provides [SelectedChanged](Tizen.UI.Components.ISelectable.md#Tizen.UI.Components.ISelectable.SelectedChanged 'Tizen.UI.Components.ISelectable.SelectedChanged') event when it activated.

```csharp
public class Selectable : Tizen.UI.Components.Clickable,
Tizen.UI.Components.ISelectable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; [Pressable](Tizen.UI.Components.Pressable.md 'Tizen.UI.Components.Pressable') &#129106; [Clickable](Tizen.UI.Components.Clickable.md 'Tizen.UI.Components.Clickable') &#129106; Selectable

Derived  
&#8627; [GroupSelectable](Tizen.UI.Components.GroupSelectable.md 'Tizen.UI.Components.GroupSelectable')  
&#8627; [SelectableBox](Tizen.UI.Components.SelectableBox.md 'Tizen.UI.Components.SelectableBox')

Implements [ISelectable](Tizen.UI.Components.ISelectable.md 'Tizen.UI.Components.ISelectable')
### Constructors

<a name='Tizen.UI.Components.Selectable.Selectable()'></a>

## Selectable() Constructor

Constructs a new selectable.

```csharp
public Selectable();
```
### Properties

<a name='Tizen.UI.Components.Selectable.IsSelectable'></a>

## Selectable.IsSelectable Property

Indicates whether it is selectable or not.

```csharp
public bool IsSelectable { get; set; }
```

Implements [IsSelectable](Tizen.UI.Components.ISelectable.md#Tizen.UI.Components.ISelectable.IsSelectable 'Tizen.UI.Components.ISelectable.IsSelectable')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Selectable.IsSelected'></a>

## Selectable.IsSelected Property

Indicates whether it is selected or not.

```csharp
public bool IsSelected { get; set; }
```

Implements [IsSelected](Tizen.UI.Components.ISelectable.md#Tizen.UI.Components.ISelectable.IsSelected 'Tizen.UI.Components.ISelectable.IsSelected')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Selectable.SelectedChangedCommand'></a>

## Selectable.SelectedChangedCommand Property

Selected changed command. see [SelectedChanged](Tizen.UI.Components.ISelectable.md#Tizen.UI.Components.ISelectable.SelectedChanged 'Tizen.UI.Components.ISelectable.SelectedChanged').

```csharp
public System.Action&lt;object,Tizen.UI.Components.InputEventArgs> SelectedChangedCommand { get; set; }
```

#### Property Value
[System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[InputEventArgs](Tizen.UI.Components.InputEventArgs.md 'Tizen.UI.Components.InputEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')
### Methods

<a name='Tizen.UI.Components.Selectable.Toggle(Tizen.UI.KeyDeviceClass)'></a>

## Selectable.Toggle(KeyDeviceClass) Method

Toggle the selection state of the component.

```csharp
public virtual void Toggle(Tizen.UI.KeyDeviceClass device=Tizen.UI.KeyDeviceClass.None);
```
#### Parameters

<a name='Tizen.UI.Components.Selectable.Toggle(Tizen.UI.KeyDeviceClass).device'></a>

`device` [Tizen.UI.KeyDeviceClass](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.KeyDeviceClass 'Tizen.UI.KeyDeviceClass')

Implements [Toggle(KeyDeviceClass)](Tizen.UI.Components.ISelectable.md#Tizen.UI.Components.ISelectable.Toggle(Tizen.UI.KeyDeviceClass) 'Tizen.UI.Components.ISelectable.Toggle(Tizen.UI.KeyDeviceClass)')
### Events

<a name='Tizen.UI.Components.Selectable.SelectedChanged'></a>

## Selectable.SelectedChanged Event

The event that is called when the value of [IsSelected](Tizen.UI.Components.ISelectable.md#Tizen.UI.Components.ISelectable.IsSelected 'Tizen.UI.Components.ISelectable.IsSelected') changes.

```csharp
public event EventHandler&lt;InputEventArgs> SelectedChanged;
```

Implements [SelectedChanged](Tizen.UI.Components.ISelectable.md#Tizen.UI.Components.ISelectable.SelectedChanged 'Tizen.UI.Components.ISelectable.SelectedChanged')

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[InputEventArgs](Tizen.UI.Components.InputEventArgs.md 'Tizen.UI.Components.InputEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')


























































