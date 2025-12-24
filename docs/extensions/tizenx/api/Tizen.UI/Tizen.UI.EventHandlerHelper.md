### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## EventHandlerHelper Class

EventHandlerHelper class provides a helper method to set and get event handlers using actions.

```csharp
public static class EventHandlerHelper
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; EventHandlerHelper
### Methods

<a name='Tizen.UI.EventHandlerHelper.Get_TEventHandler_(System.Action)'></a>

## EventHandlerHelper.Get&lt;TEventHandler>(Action) Method

Gets the event handler associated with the given action and removes the association.

```csharp
public static TEventHandler Get&lt;TEventHandler>(System.Action action)
    where TEventHandler : System.Delegate;
```
#### Type parameters

<a name='Tizen.UI.EventHandlerHelper.Get_TEventHandler_(System.Action).TEventHandler'></a>

`TEventHandler`

The type of the event handler.
#### Parameters

<a name='Tizen.UI.EventHandlerHelper.Get_TEventHandler_(System.Action).action'></a>

`action` [System.Action](https://docs.microsoft.com/en-us/dotnet/api/System.Action 'System.Action')

The action to get the event handler for.

#### Returns
[TEventHandler](Tizen.UI.EventHandlerHelper.md#Tizen.UI.EventHandlerHelper.Get_TEventHandler_(System.Action).TEventHandler 'Tizen.UI.EventHandlerHelper.Get&lt;TEventHandler>(System.Action).TEventHandler')  
The event handler associated with the given action, or null if no association exists.

<a name='Tizen.UI.EventHandlerHelper.Set_TEventHandler_(TEventHandler,System.Action)'></a>

## EventHandlerHelper.Set&lt;TEventHandler>(TEventHandler, Action) Method

Sets the event handler for the given action.

```csharp
public static TEventHandler Set&lt;TEventHandler>(TEventHandler handler, System.Action action)
    where TEventHandler : System.Delegate;
```
#### Type parameters

<a name='Tizen.UI.EventHandlerHelper.Set_TEventHandler_(TEventHandler,System.Action).TEventHandler'></a>

`TEventHandler`

The type of the event handler.
#### Parameters

<a name='Tizen.UI.EventHandlerHelper.Set_TEventHandler_(TEventHandler,System.Action).handler'></a>

`handler` [TEventHandler](Tizen.UI.EventHandlerHelper.md#Tizen.UI.EventHandlerHelper.Set_TEventHandler_(TEventHandler,System.Action).TEventHandler 'Tizen.UI.EventHandlerHelper.Set&lt;TEventHandler>(TEventHandler, System.Action).TEventHandler')

The event handler to set.

<a name='Tizen.UI.EventHandlerHelper.Set_TEventHandler_(TEventHandler,System.Action).action'></a>

`action` [System.Action](https://docs.microsoft.com/en-us/dotnet/api/System.Action 'System.Action')

The action to associate with the event handler.

#### Returns
[TEventHandler](Tizen.UI.EventHandlerHelper.md#Tizen.UI.EventHandlerHelper.Set_TEventHandler_(TEventHandler,System.Action).TEventHandler 'Tizen.UI.EventHandlerHelper.Set&lt;TEventHandler>(TEventHandler, System.Action).TEventHandler')  
The event handler that was set.






