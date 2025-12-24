### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## UIStateManager Class

Provides methods to get a UIState from a view or to notify UIState change.  
Note that there is no direct way to set a view UIState to a view.  
The indirect way is to set connected property.  
To set [Disabled](Tizen.UI.Components.UIState.md#Tizen.UI.Components.UIState.Disabled 'Tizen.UI.Components.UIState.Disabled'), for example, you need to set [Tizen.UI.View.IsEnabled](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View.IsEnabled 'Tizen.UI.View.IsEnabled') to false.

```csharp
public static class UIStateManager
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; UIStateManager
### Methods

<a name='Tizen.UI.Components.UIStateManager.AddStateChangedEventHandler_TView_(thisTView,System.EventHandler_Tizen.UI.Components.UIStateChangedEventArgs_)'></a>

## UIStateManager.AddStateChangedEventHandler&lt;TView>(this TView, EventHandler&lt;UIStateChangedEventArgs>) Method

Add an action to be invoked when a UIState of target view changes.

```csharp
public static void AddStateChangedEventHandler&lt;TView>(this TView view, System.EventHandler&lt;Tizen.UI.Components.UIStateChangedEventArgs> handler)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.UIStateManager.AddStateChangedEventHandler_TView_(thisTView,System.EventHandler_Tizen.UI.Components.UIStateChangedEventArgs_).TView'></a>

`TView`
#### Parameters

<a name='Tizen.UI.Components.UIStateManager.AddStateChangedEventHandler_TView_(thisTView,System.EventHandler_Tizen.UI.Components.UIStateChangedEventArgs_).view'></a>

`view` [TView](Tizen.UI.Components.UIStateManager.md#Tizen.UI.Components.UIStateManager.AddStateChangedEventHandler_TView_(thisTView,System.EventHandler_Tizen.UI.Components.UIStateChangedEventArgs_).TView 'Tizen.UI.Components.UIStateManager.AddStateChangedEventHandler&lt;TView>(this TView, System.EventHandler&lt;Tizen.UI.Components.UIStateChangedEventArgs>).TView')

The target view.

<a name='Tizen.UI.Components.UIStateManager.AddStateChangedEventHandler_TView_(thisTView,System.EventHandler_Tizen.UI.Components.UIStateChangedEventArgs_).handler'></a>

`handler` [System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[UIStateChangedEventArgs](Tizen.UI.Components.UIStateChangedEventArgs.md 'Tizen.UI.Components.UIStateChangedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

The action to add.

<a name='Tizen.UI.Components.UIStateManager.ConnectUIState_TView_(thisTView,Tizen.UI.Components.UIState,Tizen.UI.Components.UIStateConnectingProperty_TView_)'></a>

## UIStateManager.ConnectUIState&lt;TView>(this TView, UIState, UIStateConnectingProperty&lt;TView>) Method

Connect a UIState to a property for a target view.  
Only one connection is allowed for each UIState.

```csharp
public static void ConnectUIState&lt;TView>(this TView view, Tizen.UI.Components.UIState viewState, Tizen.UI.Components.UIStateConnectingProperty&lt;TView> connectingProperty)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.UIStateManager.ConnectUIState_TView_(thisTView,Tizen.UI.Components.UIState,Tizen.UI.Components.UIStateConnectingProperty_TView_).TView'></a>

`TView`
#### Parameters

<a name='Tizen.UI.Components.UIStateManager.ConnectUIState_TView_(thisTView,Tizen.UI.Components.UIState,Tizen.UI.Components.UIStateConnectingProperty_TView_).view'></a>

`view` [TView](Tizen.UI.Components.UIStateManager.md#Tizen.UI.Components.UIStateManager.ConnectUIState_TView_(thisTView,Tizen.UI.Components.UIState,Tizen.UI.Components.UIStateConnectingProperty_TView_).TView 'Tizen.UI.Components.UIStateManager.ConnectUIState&lt;TView>(this TView, Tizen.UI.Components.UIState, Tizen.UI.Components.UIStateConnectingProperty&lt;TView>).TView')

The view that has the connecting property.

<a name='Tizen.UI.Components.UIStateManager.ConnectUIState_TView_(thisTView,Tizen.UI.Components.UIState,Tizen.UI.Components.UIStateConnectingProperty_TView_).viewState'></a>

`viewState` [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

The UIState to connect.

<a name='Tizen.UI.Components.UIStateManager.ConnectUIState_TView_(thisTView,Tizen.UI.Components.UIState,Tizen.UI.Components.UIStateConnectingProperty_TView_).connectingProperty'></a>

`connectingProperty` [Tizen.UI.Components.UIStateConnectingProperty&lt;](Tizen.UI.Components.UIStateConnectingProperty_TView_.md 'Tizen.UI.Components.UIStateConnectingProperty&lt;TView>')[TView](Tizen.UI.Components.UIStateManager.md#Tizen.UI.Components.UIStateManager.ConnectUIState_TView_(thisTView,Tizen.UI.Components.UIState,Tizen.UI.Components.UIStateConnectingProperty_TView_).TView 'Tizen.UI.Components.UIStateManager.ConnectUIState&lt;TView>(this TView, Tizen.UI.Components.UIState, Tizen.UI.Components.UIStateConnectingProperty&lt;TView>).TView')[&gt;](Tizen.UI.Components.UIStateConnectingProperty_TView_.md 'Tizen.UI.Components.UIStateConnectingProperty&lt;TView>')

The connecting property.

<a name='Tizen.UI.Components.UIStateManager.DisconnectUIState(thisTizen.UI.View,Tizen.UI.Components.UIState)'></a>

## UIStateManager.DisconnectUIState(this View, UIState) Method

Disconnect the UIState-property connection of a view.

```csharp
public static void DisconnectUIState(this Tizen.UI.View view, Tizen.UI.Components.UIState viewState);
```
#### Parameters

<a name='Tizen.UI.Components.UIStateManager.DisconnectUIState(thisTizen.UI.View,Tizen.UI.Components.UIState).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The target view.

<a name='Tizen.UI.Components.UIStateManager.DisconnectUIState(thisTizen.UI.View,Tizen.UI.Components.UIState).viewState'></a>

`viewState` [UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')

The UIState to clean.

<a name='Tizen.UI.Components.UIStateManager.GetState(thisTizen.UI.View)'></a>

## UIStateManager.GetState(this View) Method

Gets a UIState of a view.

```csharp
public static Tizen.UI.Components.UIState GetState(this Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.Components.UIStateManager.GetState(thisTizen.UI.View).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view with UIState to get.

#### Returns
[UIState](Tizen.UI.Components.UIState.md 'Tizen.UI.Components.UIState')  
The view's view UIState.

<a name='Tizen.UI.Components.UIStateManager.RemoveStateChangedEventHandler_TView_(thisTView,System.EventHandler_Tizen.UI.Components.UIStateChangedEventArgs_)'></a>

## UIStateManager.RemoveStateChangedEventHandler&lt;TView>(this TView, EventHandler&lt;UIStateChangedEventArgs>) Method

Remove registered UIState related action from a view.

```csharp
public static void RemoveStateChangedEventHandler&lt;TView>(this TView view, System.EventHandler&lt;Tizen.UI.Components.UIStateChangedEventArgs> handler)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.UIStateManager.RemoveStateChangedEventHandler_TView_(thisTView,System.EventHandler_Tizen.UI.Components.UIStateChangedEventArgs_).TView'></a>

`TView`
#### Parameters

<a name='Tizen.UI.Components.UIStateManager.RemoveStateChangedEventHandler_TView_(thisTView,System.EventHandler_Tizen.UI.Components.UIStateChangedEventArgs_).view'></a>

`view` [TView](Tizen.UI.Components.UIStateManager.md#Tizen.UI.Components.UIStateManager.RemoveStateChangedEventHandler_TView_(thisTView,System.EventHandler_Tizen.UI.Components.UIStateChangedEventArgs_).TView 'Tizen.UI.Components.UIStateManager.RemoveStateChangedEventHandler&lt;TView>(this TView, System.EventHandler&lt;Tizen.UI.Components.UIStateChangedEventArgs>).TView')

The view to remove event handler from.

<a name='Tizen.UI.Components.UIStateManager.RemoveStateChangedEventHandler_TView_(thisTView,System.EventHandler_Tizen.UI.Components.UIStateChangedEventArgs_).handler'></a>

`handler` [System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[UIStateChangedEventArgs](Tizen.UI.Components.UIStateChangedEventArgs.md 'Tizen.UI.Components.UIStateChangedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

The handler to remove.

### Remarks
This removes actions that are added by AddStateChangedEventHandler.


























































