### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## ISelectable Interface

Represents selectable element.  
All derived class of Tizen.UI.View that implements this interface can have [Selected](Tizen.UI.Components.UIState.md#Tizen.UI.Components.UIState.Selected 'Tizen.UI.Components.UIState.Selected') state when [IsSelected](Tizen.UI.Components.ISelectable.md#Tizen.UI.Components.ISelectable.IsSelected 'Tizen.UI.Components.ISelectable.IsSelected') is true.

```csharp
public interface ISelectable
```

Derived  
&#8627; [GroupSelectable](Tizen.UI.Components.GroupSelectable.md 'Tizen.UI.Components.GroupSelectable')  
&#8627; [IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable')  
&#8627; [Selectable](Tizen.UI.Components.Selectable.md 'Tizen.UI.Components.Selectable')
### Properties

<a name='Tizen.UI.Components.ISelectable.IsSelectable'></a>

## ISelectable.IsSelectable Property

Indicates whether it is selectable or not.

```csharp
bool IsSelectable { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.ISelectable.IsSelected'></a>

## ISelectable.IsSelected Property

Indicates whether it is selected or not.

```csharp
bool IsSelected { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')
### Methods

<a name='Tizen.UI.Components.ISelectable.Toggle(Tizen.UI.KeyDeviceClass)'></a>

## ISelectable.Toggle(KeyDeviceClass) Method

Toggle the selection state of the component.

```csharp
void Toggle(Tizen.UI.KeyDeviceClass device);
```
#### Parameters

<a name='Tizen.UI.Components.ISelectable.Toggle(Tizen.UI.KeyDeviceClass).device'></a>

`device` Tizen.UI.KeyDeviceClass
### Events

<a name='Tizen.UI.Components.ISelectable.SelectedChanged'></a>

## ISelectable.SelectedChanged Event

The event that is called when the value of [IsSelected](Tizen.UI.Components.ISelectable.md#Tizen.UI.Components.ISelectable.IsSelected 'Tizen.UI.Components.ISelectable.IsSelected') changes.

```csharp
event EventHandler&lt;InputEventArgs> SelectedChanged;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[InputEventArgs](Tizen.UI.Components.InputEventArgs.md 'Tizen.UI.Components.InputEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')



























































