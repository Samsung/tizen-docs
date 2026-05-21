### [Tizen.UI.WindowBorder](Tizen.UI.WindowBorder.md 'Tizen.UI.WindowBorder').[BorderView](Tizen.UI.WindowBorder.BorderView.md 'Tizen.UI.WindowBorder.BorderView')

## BorderView.BorderViewModel Class

The BorderViewModel class provides the view model for the BorderView class.

```csharp
public class BorderView.BorderViewModel :
System.ComponentModel.INotifyPropertyChanged
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; BorderViewModel

Implements [System.ComponentModel.INotifyPropertyChanged](https://docs.microsoft.com/en-us/dotnet/api/System.ComponentModel.INotifyPropertyChanged 'System.ComponentModel.INotifyPropertyChanged')
### Properties

<a name='Tizen.UI.WindowBorder.BorderView.BorderViewModel.CloseAction'></a>

## BorderView.BorderViewModel.CloseAction Property

Gets or sets the action to be performed when the window is closed.

```csharp
public System.Action CloseAction { get; set; }
```

#### Property Value
[System.Action](https://docs.microsoft.com/en-us/dotnet/api/System.Action 'System.Action')

<a name='Tizen.UI.WindowBorder.BorderView.BorderViewModel.IsMaximized'></a>

## BorderView.BorderViewModel.IsMaximized Property

Gets or sets a value indicating whether the window is maximized or not.

```csharp
public bool IsMaximized { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.WindowBorder.BorderView.BorderViewModel.MaximizeAction'></a>

## BorderView.BorderViewModel.MaximizeAction Property

Gets or sets the action to be performed when the window is maximized or restored.

```csharp
public System.Action&lt;bool> MaximizeAction { get; set; }
```

#### Property Value
[System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')

<a name='Tizen.UI.WindowBorder.BorderView.BorderViewModel.MinimizeAction'></a>

## BorderView.BorderViewModel.MinimizeAction Property

Gets or sets the action to be performed when the window is minimized.

```csharp
public System.Action MinimizeAction { get; set; }
```

#### Property Value
[System.Action](https://docs.microsoft.com/en-us/dotnet/api/System.Action 'System.Action')

<a name='Tizen.UI.WindowBorder.BorderView.BorderViewModel.ResizeAction'></a>

## BorderView.BorderViewModel.ResizeAction Property

Gets or sets the action to be performed when the window is resized.

```csharp
public System.Action&lt;Tizen.UI.WindowResizeDirection> ResizeAction { get; set; }
```

#### Property Value
[System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')Tizen.UI.WindowResizeDirection[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')

<a name='Tizen.UI.WindowBorder.BorderView.BorderViewModel.TargetWindow'></a>

## BorderView.BorderViewModel.TargetWindow Property

Gets or sets the target window of the BorderView.

```csharp
public Tizen.UI.Window TargetWindow { get; set; }
```

#### Property Value
Tizen.UI.Window
### Events

<a name='Tizen.UI.WindowBorder.BorderView.BorderViewModel.PropertyChanged'></a>

## BorderView.BorderViewModel.PropertyChanged Event

Occurs when a property value changes.

```csharp
public event PropertyChangedEventHandler PropertyChanged;
```

Implements [PropertyChanged](https://docs.microsoft.com/en-us/dotnet/api/System.ComponentModel.INotifyPropertyChanged.PropertyChanged 'System.ComponentModel.INotifyPropertyChanged.PropertyChanged')

#### Event Type
[System.ComponentModel.PropertyChangedEventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.ComponentModel.PropertyChangedEventHandler 'System.ComponentModel.PropertyChangedEventHandler')















