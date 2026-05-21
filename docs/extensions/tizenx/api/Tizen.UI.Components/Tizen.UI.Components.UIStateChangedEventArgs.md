### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## UIStateChangedEventArgs Class

The event arguments for the UIState changed event.

```csharp
public class UIStateChangedEventArgs : System.EventArgs
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs') &#129106; UIStateChangedEventArgs
### Properties

<a name='Tizen.UI.Components.UIStateChangedEventArgs.Current'></a>

## UIStateChangedEventArgs.Current Property

Gets or sets the current UIState.

```csharp
public Tizen.UI.Components.UIState Current { get; set; }
```

#### Property Value
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

<a name='Tizen.UI.Components.UIStateChangedEventArgs.Previous'></a>

## UIStateChangedEventArgs.Previous Property

Gets or sets the previous UIState.

```csharp
public Tizen.UI.Components.UIState Previous { get; set; }
```

#### Property Value
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')
### Methods

<a name='Tizen.UI.Components.UIStateChangedEventArgs.Test(Tizen.UI.Components.UIStateConstraint)'></a>

## UIStateChangedEventArgs.Test(UIStateConstraint) Method

Tests if the specified constraint is matched with this change.

```csharp
public bool Test(Tizen.UI.Components.UIStateConstraint constraint);
```
#### Parameters

<a name='Tizen.UI.Components.UIStateChangedEventArgs.Test(Tizen.UI.Components.UIStateConstraint).constraint'></a>

`constraint` [UIStateConstraint](Tizen.UI.Components.UIStateConstraint.md 'Tizen.UI.Components.UIStateConstraint')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')


























































