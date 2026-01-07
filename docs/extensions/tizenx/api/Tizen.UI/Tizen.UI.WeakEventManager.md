### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## WeakEventManager Class

Provides a weak event manager that allows subscribing and unsubscribing from events without causing memory leaks.

```csharp
public class WeakEventManager
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; WeakEventManager
### Methods

<a name='Tizen.UI.WeakEventManager.AddEventHandler(System.Delegate,string)'></a>

## WeakEventManager.AddEventHandler(Delegate, string) Method

Adds a delegate to the specified event.

```csharp
public void AddEventHandler(System.Delegate handler, string eventName="");
```
#### Parameters

<a name='Tizen.UI.WeakEventManager.AddEventHandler(System.Delegate,string).handler'></a>

`handler` [System.Delegate](https://docs.microsoft.com/en-us/dotnet/api/System.Delegate 'System.Delegate')

The delegate to add to the event.

<a name='Tizen.UI.WeakEventManager.AddEventHandler(System.Delegate,string).eventName'></a>

`eventName` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the event to which to add the delegate.

<a name='Tizen.UI.WeakEventManager.AddEventHandler_TEventArgs_(System.EventHandler_TEventArgs_,string)'></a>

## WeakEventManager.AddEventHandler&lt;TEventArgs>(EventHandler&lt;TEventArgs>, string) Method

Adds a delegate to the specified event.

```csharp
public void AddEventHandler&lt;TEventArgs>(System.EventHandler&lt;TEventArgs> handler, string eventName="")
    where TEventArgs : System.EventArgs;
```
#### Type parameters

<a name='Tizen.UI.WeakEventManager.AddEventHandler_TEventArgs_(System.EventHandler_TEventArgs_,string).TEventArgs'></a>

`TEventArgs`

The type of event arguments.
#### Parameters

<a name='Tizen.UI.WeakEventManager.AddEventHandler_TEventArgs_(System.EventHandler_TEventArgs_,string).handler'></a>

`handler` [System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[TEventArgs](Tizen.UI.WeakEventManager.md#Tizen.UI.WeakEventManager.AddEventHandler_TEventArgs_(System.EventHandler_TEventArgs_,string).TEventArgs 'Tizen.UI.WeakEventManager.AddEventHandler&lt;TEventArgs>(System.EventHandler&lt;TEventArgs>, string).TEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

The delegate to add to the event.

<a name='Tizen.UI.WeakEventManager.AddEventHandler_TEventArgs_(System.EventHandler_TEventArgs_,string).eventName'></a>

`eventName` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the event to which to add the delegate.

<a name='Tizen.UI.WeakEventManager.HandleEvent(object,object,string)'></a>

## WeakEventManager.HandleEvent(object, object, string) Method

Raises the specified event with the given sender and event arguments.

```csharp
public void HandleEvent(object sender, object args, string eventName);
```
#### Parameters

<a name='Tizen.UI.WeakEventManager.HandleEvent(object,object,string).sender'></a>

`sender` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The object that raised the event.

<a name='Tizen.UI.WeakEventManager.HandleEvent(object,object,string).args'></a>

`args` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The event arguments.

<a name='Tizen.UI.WeakEventManager.HandleEvent(object,object,string).eventName'></a>

`eventName` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the event to raise.

<a name='Tizen.UI.WeakEventManager.RemoveEventHandler(System.Delegate,string)'></a>

## WeakEventManager.RemoveEventHandler(Delegate, string) Method

Removes a delegate from the specified event.

```csharp
public void RemoveEventHandler(System.Delegate handler, string eventName="");
```
#### Parameters

<a name='Tizen.UI.WeakEventManager.RemoveEventHandler(System.Delegate,string).handler'></a>

`handler` [System.Delegate](https://docs.microsoft.com/en-us/dotnet/api/System.Delegate 'System.Delegate')

The delegate to remove from the event.

<a name='Tizen.UI.WeakEventManager.RemoveEventHandler(System.Delegate,string).eventName'></a>

`eventName` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the event from which to remove the delegate.

<a name='Tizen.UI.WeakEventManager.RemoveEventHandler_TEventArgs_(System.EventHandler_TEventArgs_,string)'></a>

## WeakEventManager.RemoveEventHandler&lt;TEventArgs>(EventHandler&lt;TEventArgs>, string) Method

Removes a delegate from the specified event.

```csharp
public void RemoveEventHandler&lt;TEventArgs>(System.EventHandler&lt;TEventArgs> handler, string eventName="")
    where TEventArgs : System.EventArgs;
```
#### Type parameters

<a name='Tizen.UI.WeakEventManager.RemoveEventHandler_TEventArgs_(System.EventHandler_TEventArgs_,string).TEventArgs'></a>

`TEventArgs`

The type of event arguments.
#### Parameters

<a name='Tizen.UI.WeakEventManager.RemoveEventHandler_TEventArgs_(System.EventHandler_TEventArgs_,string).handler'></a>

`handler` [System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[TEventArgs](Tizen.UI.WeakEventManager.md#Tizen.UI.WeakEventManager.RemoveEventHandler_TEventArgs_(System.EventHandler_TEventArgs_,string).TEventArgs 'Tizen.UI.WeakEventManager.RemoveEventHandler&lt;TEventArgs>(System.EventHandler&lt;TEventArgs>, string).TEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

The delegate to remove from the event.

<a name='Tizen.UI.WeakEventManager.RemoveEventHandler_TEventArgs_(System.EventHandler_TEventArgs_,string).eventName'></a>

`eventName` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the event from which to remove the delegate.






