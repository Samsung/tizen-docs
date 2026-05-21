### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## FocusManager Class

The FocusManager class is used to manage the focus between views.

```csharp
public class FocusManager : Tizen.UI.NObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; FocusManager
### Properties

<a name='Tizen.UI.FocusManager.Instance'></a>

## FocusManager.Instance Property

Gets the singleton instance of the FocusManager.

```csharp
public static Tizen.UI.FocusManager Instance { get; }
```

#### Property Value
[FocusManager](Tizen.UI.FocusManager.md 'Tizen.UI.FocusManager')
### Methods

<a name='Tizen.UI.FocusManager.ClearFocus()'></a>

## FocusManager.ClearFocus() Method

Clears the focus from the currently focused view.

```csharp
public void ClearFocus();
```

<a name='Tizen.UI.FocusManager.EnableDefaultFocusAlgorithm(bool)'></a>

## FocusManager.EnableDefaultFocusAlgorithm(bool) Method

Enables or disables the default focus algorithm.

```csharp
public void EnableDefaultFocusAlgorithm(bool enable);
```
#### Parameters

<a name='Tizen.UI.FocusManager.EnableDefaultFocusAlgorithm(bool).enable'></a>

`enable` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True to enable the default algorithm, false to disable it.

<a name='Tizen.UI.FocusManager.EnableFocusIndicator(bool)'></a>

## FocusManager.EnableFocusIndicator(bool) Method

Enables or disables the focus indicator.

```csharp
public void EnableFocusIndicator(bool enable);
```
#### Parameters

<a name='Tizen.UI.FocusManager.EnableFocusIndicator(bool).enable'></a>

`enable` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True to enable the focus indicator, false to disable it.

<a name='Tizen.UI.FocusManager.GetFocused()'></a>

## FocusManager.GetFocused() Method

Gets the currently focused view.

```csharp
public Tizen.UI.View GetFocused();
```

#### Returns
[View](Tizen.UI.View.md 'Tizen.UI.View')  
The currently focused view.

<a name='Tizen.UI.FocusManager.GetNearestFocusableView(Tizen.UI.View,Tizen.UI.View,Tizen.UI.FocusDirection)'></a>

## FocusManager.GetNearestFocusableView(View, View, FocusDirection) Method

Gets the nearest focusable view within the specified view hierarchy.

```csharp
public Tizen.UI.View GetNearestFocusableView(Tizen.UI.View rootView, Tizen.UI.View currentView, Tizen.UI.FocusDirection direction);
```
#### Parameters

<a name='Tizen.UI.FocusManager.GetNearestFocusableView(Tizen.UI.View,Tizen.UI.View,Tizen.UI.FocusDirection).rootView'></a>

`rootView` [View](Tizen.UI.View.md 'Tizen.UI.View')

The root view of the view hierarchy.

<a name='Tizen.UI.FocusManager.GetNearestFocusableView(Tizen.UI.View,Tizen.UI.View,Tizen.UI.FocusDirection).currentView'></a>

`currentView` [View](Tizen.UI.View.md 'Tizen.UI.View')

The current focused view.

<a name='Tizen.UI.FocusManager.GetNearestFocusableView(Tizen.UI.View,Tizen.UI.View,Tizen.UI.FocusDirection).direction'></a>

`direction` [FocusDirection](Tizen.UI.FocusDirection.md 'Tizen.UI.FocusDirection')

The direction of focus movement.

#### Returns
[View](Tizen.UI.View.md 'Tizen.UI.View')  
The nearest focusable view in the specified direction.

<a name='Tizen.UI.FocusManager.GetNearestFocusableViewOverride(Tizen.UI.View,Tizen.UI.View,Tizen.UI.FocusDirection)'></a>

## FocusManager.GetNearestFocusableViewOverride(View, View, FocusDirection) Method

Gets the nearest focusable view within the specified view hierarchy, using the custom focus algorithm if set.

```csharp
public Tizen.UI.View GetNearestFocusableViewOverride(Tizen.UI.View rootView, Tizen.UI.View currentView, Tizen.UI.FocusDirection direction);
```
#### Parameters

<a name='Tizen.UI.FocusManager.GetNearestFocusableViewOverride(Tizen.UI.View,Tizen.UI.View,Tizen.UI.FocusDirection).rootView'></a>

`rootView` [View](Tizen.UI.View.md 'Tizen.UI.View')

The root view of the view hierarchy.

<a name='Tizen.UI.FocusManager.GetNearestFocusableViewOverride(Tizen.UI.View,Tizen.UI.View,Tizen.UI.FocusDirection).currentView'></a>

`currentView` [View](Tizen.UI.View.md 'Tizen.UI.View')

The current focused view.

<a name='Tizen.UI.FocusManager.GetNearestFocusableViewOverride(Tizen.UI.View,Tizen.UI.View,Tizen.UI.FocusDirection).direction'></a>

`direction` [FocusDirection](Tizen.UI.FocusDirection.md 'Tizen.UI.FocusDirection')

The direction of focus movement.

#### Returns
[View](Tizen.UI.View.md 'Tizen.UI.View')  
The nearest focusable view in the specified direction.

<a name='Tizen.UI.FocusManager.SetCustomFocusAlgorithm(Tizen.UI.IFocusAlgorithm)'></a>

## FocusManager.SetCustomFocusAlgorithm(IFocusAlgorithm) Method

Sets the custom focus algorithm to be used for finding the nearest focusable view.

```csharp
public void SetCustomFocusAlgorithm(Tizen.UI.IFocusAlgorithm focusAlgorithm);
```
#### Parameters

<a name='Tizen.UI.FocusManager.SetCustomFocusAlgorithm(Tizen.UI.IFocusAlgorithm).focusAlgorithm'></a>

`focusAlgorithm` [IFocusAlgorithm](Tizen.UI.IFocusAlgorithm.md 'Tizen.UI.IFocusAlgorithm')

The custom focus algorithm to set.

<a name='Tizen.UI.FocusManager.SetFocus(Tizen.UI.View)'></a>

## FocusManager.SetFocus(View) Method

Sets the focus to the specified view.

```csharp
public bool SetFocus(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.FocusManager.SetFocus(Tizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to receive focus.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the focus is set successfully, false otherwise.

<a name='Tizen.UI.FocusManager.SetFocusIndicator(Tizen.UI.View)'></a>

## FocusManager.SetFocusIndicator(View) Method

Sets the focus indicator actor to be used when moving the focus.

```csharp
public void SetFocusIndicator(Tizen.UI.View indicator);
```
#### Parameters

<a name='Tizen.UI.FocusManager.SetFocusIndicator(Tizen.UI.View).indicator'></a>

`indicator` [View](Tizen.UI.View.md 'Tizen.UI.View')

The focus indicator actor to set.
### Events

<a name='Tizen.UI.FocusManager.FocusChanged'></a>

## FocusManager.FocusChanged Event

Occurs when the focused view changes.

```csharp
public event EventHandler&lt;FocusChangedEventArgs> FocusChanged;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[FocusChangedEventArgs](Tizen.UI.FocusChangedEventArgs.md 'Tizen.UI.FocusChangedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')






