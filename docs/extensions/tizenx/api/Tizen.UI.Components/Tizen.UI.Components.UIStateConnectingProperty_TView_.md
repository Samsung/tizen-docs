### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## UIStateConnectingProperty&lt;TView> Class

Represents a property for a view that can be connected to a state.

```csharp
public class UIStateConnectingProperty&lt;TView>
```
#### Type parameters

<a name='Tizen.UI.Components.UIStateConnectingProperty_TView_.TView'></a>

`TView`

The type of the view.

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; UIStateConnectingProperty&lt;TView>
### Constructors

<a name='Tizen.UI.Components.UIStateConnectingProperty_TView_.UIStateConnectingProperty(System.Func_TView,bool_,System.Action_TView,System.EventHandler_,System.Action_TView,System.EventHandler_)'></a>

## UIStateConnectingProperty(Func&lt;TView,bool>, Action&lt;TView,EventHandler>, Action&lt;TView,EventHandler>) Constructor

Create a new instance of the StateConnectingProperty.

```csharp
public UIStateConnectingProperty(System.Func&lt;TView,bool> getter, System.Action&lt;TView,System.EventHandler> addObserver, System.Action&lt;TView,System.EventHandler> removeObserver);
```
#### Parameters

<a name='Tizen.UI.Components.UIStateConnectingProperty_TView_.UIStateConnectingProperty(System.Func_TView,bool_,System.Action_TView,System.EventHandler_,System.Action_TView,System.EventHandler_).getter'></a>

`getter` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[TView](Tizen.UI.Components.UIStateConnectingProperty_TView_.md#Tizen.UI.Components.UIStateConnectingProperty_TView_.TView 'Tizen.UI.Components.UIStateConnectingProperty&lt;TView>.TView')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

The boolean-type property getter function.

<a name='Tizen.UI.Components.UIStateConnectingProperty_TView_.UIStateConnectingProperty(System.Func_TView,bool_,System.Action_TView,System.EventHandler_,System.Action_TView,System.EventHandler_).addObserver'></a>

`addObserver` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[TView](Tizen.UI.Components.UIStateConnectingProperty_TView_.md#Tizen.UI.Components.UIStateConnectingProperty_TView_.TView 'Tizen.UI.Components.UIStateConnectingProperty&lt;TView>.TView')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

The action that adds an observer to the view. The observer should be [System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler') type.

<a name='Tizen.UI.Components.UIStateConnectingProperty_TView_.UIStateConnectingProperty(System.Func_TView,bool_,System.Action_TView,System.EventHandler_,System.Action_TView,System.EventHandler_).removeObserver'></a>

`removeObserver` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[TView](Tizen.UI.Components.UIStateConnectingProperty_TView_.md#Tizen.UI.Components.UIStateConnectingProperty_TView_.TView 'Tizen.UI.Components.UIStateConnectingProperty&lt;TView>.TView')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

The action that removes an observer from the view.
### Properties

<a name='Tizen.UI.Components.UIStateConnectingProperty_TView_.AddObserver'></a>

## UIStateConnectingProperty&lt;TView>.AddObserver Property

Gets the action that adds an observer to the view.

```csharp
public System.Action&lt;TView,System.EventHandler> AddObserver { get; set; }
```

#### Property Value
[System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[TView](Tizen.UI.Components.UIStateConnectingProperty_TView_.md#Tizen.UI.Components.UIStateConnectingProperty_TView_.TView 'Tizen.UI.Components.UIStateConnectingProperty&lt;TView>.TView')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

<a name='Tizen.UI.Components.UIStateConnectingProperty_TView_.Getter'></a>

## UIStateConnectingProperty&lt;TView>.Getter Property

Gets the boolean-type property getter function.

```csharp
public System.Func&lt;TView,bool> Getter { get; set; }
```

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[TView](Tizen.UI.Components.UIStateConnectingProperty_TView_.md#Tizen.UI.Components.UIStateConnectingProperty_TView_.TView 'Tizen.UI.Components.UIStateConnectingProperty&lt;TView>.TView')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

<a name='Tizen.UI.Components.UIStateConnectingProperty_TView_.RemoveObserver'></a>

## UIStateConnectingProperty&lt;TView>.RemoveObserver Property

Gets the action that removed an observer from the view.

```csharp
public System.Action&lt;TView,System.EventHandler> RemoveObserver { get; set; }
```

#### Property Value
[System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[TView](Tizen.UI.Components.UIStateConnectingProperty_TView_.md#Tizen.UI.Components.UIStateConnectingProperty_TView_.TView 'Tizen.UI.Components.UIStateConnectingProperty&lt;TView>.TView')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')


























































