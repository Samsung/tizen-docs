### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## IFocusAlgorithm Interface

The IFocusAlgorithm interface defines the methods required for a focus algorithm to be used by the FocusManager.

```csharp
public interface IFocusAlgorithm
```
### Methods

<a name='Tizen.UI.IFocusAlgorithm.GetNextFocusableView(Tizen.UI.View,Tizen.UI.View,Tizen.UI.FocusDirection,string)'></a>

## IFocusAlgorithm.GetNextFocusableView(View, View, FocusDirection, string) Method

Gets the next focusable view based on the current view and the focus direction.

```csharp
Tizen.UI.View GetNextFocusableView(Tizen.UI.View current, Tizen.UI.View proposed, Tizen.UI.FocusDirection direction, string deviceName);
```
#### Parameters

<a name='Tizen.UI.IFocusAlgorithm.GetNextFocusableView(Tizen.UI.View,Tizen.UI.View,Tizen.UI.FocusDirection,string).current'></a>

`current` [View](Tizen.UI.View.md 'Tizen.UI.View')

The current view.

<a name='Tizen.UI.IFocusAlgorithm.GetNextFocusableView(Tizen.UI.View,Tizen.UI.View,Tizen.UI.FocusDirection,string).proposed'></a>

`proposed` [View](Tizen.UI.View.md 'Tizen.UI.View')

The proposed view.

<a name='Tizen.UI.IFocusAlgorithm.GetNextFocusableView(Tizen.UI.View,Tizen.UI.View,Tizen.UI.FocusDirection,string).direction'></a>

`direction` [FocusDirection](Tizen.UI.FocusDirection.md 'Tizen.UI.FocusDirection')

The focus direction.

<a name='Tizen.UI.IFocusAlgorithm.GetNextFocusableView(Tizen.UI.View,Tizen.UI.View,Tizen.UI.FocusDirection,string).deviceName'></a>

`deviceName` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the device that is requesting the focus.

#### Returns
[View](Tizen.UI.View.md 'Tizen.UI.View')  
The next focusable view.






