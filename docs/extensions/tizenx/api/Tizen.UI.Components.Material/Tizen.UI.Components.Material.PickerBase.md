### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## PickerBase Class

The base abstract class for all picker implementations.  
Contains common properties and logic for picker components.

```csharp
public abstract class PickerBase : Tizen.UI.ContentView
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ContentView &#129106; PickerBase

Derived  
&#8627; [InputPicker](Tizen.UI.Components.Material.InputPicker.md 'Tizen.UI.Components.Material.InputPicker')  
&#8627; [Picker](Tizen.UI.Components.Material.Picker.md 'Tizen.UI.Components.Material.Picker')
### Properties

<a name='Tizen.UI.Components.Material.PickerBase.DisplayedValues'></a>

## PickerBase.DisplayedValues Property

Gets or sets the displayed values of the picker.

```csharp
public System.Collections.ObjectModel.ReadOnlyCollection&lt;string> DisplayedValues { get; set; }
```

#### Property Value
[System.Collections.ObjectModel.ReadOnlyCollection&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ObjectModel.ReadOnlyCollection-1 'System.Collections.ObjectModel.ReadOnlyCollection`1')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ObjectModel.ReadOnlyCollection-1 'System.Collections.ObjectModel.ReadOnlyCollection`1')

<a name='Tizen.UI.Components.Material.PickerBase.Range'></a>

## PickerBase.Range Property

Gets or sets the range of the picker.

```csharp
public Tizen.UI.Components.ClosedRange&lt;int> Range { get; set; }
```

#### Property Value
Tizen.UI.Components.ClosedRange&lt;[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')&gt;

<a name='Tizen.UI.Components.Material.PickerBase.Value'></a>

## PickerBase.Value Property

Gets or sets the current value of the picker.

```csharp
public int Value { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')
### Events

<a name='Tizen.UI.Components.Material.PickerBase.EditModeChanged'></a>

## PickerBase.EditModeChanged Event

Occurs when the picker edit mode changed.

```csharp
public event EventHandler EditModeChanged;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.Material.PickerBase.InputPanelVisibilityChanged'></a>

## PickerBase.InputPanelVisibilityChanged Event

Occurs when the input panel visibility state changed.

```csharp
public event EventHandler&lt;bool> InputPanelVisibilityChanged;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Material.PickerBase.ValueChanged'></a>

## PickerBase.ValueChanged Event

Occurs when the picker value changed.

```csharp
public event EventHandler ValueChanged;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')














































