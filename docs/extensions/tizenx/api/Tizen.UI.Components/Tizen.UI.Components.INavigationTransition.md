### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## INavigationTransition Interface

The INavigationTransition interface defines methods to notice the changes of the navigation transition such as appearing or disappearing.

```csharp
public interface INavigationTransition
```

Derived  
&#8627; [Navigator](Tizen.UI.Components.Navigator.md 'Tizen.UI.Components.Navigator')
### Methods

<a name='Tizen.UI.Components.INavigationTransition.DidAppear(bool)'></a>

## INavigationTransition.DidAppear(bool) Method

Called right after appearing by navigation transition.

```csharp
void DidAppear(bool byPopNavigation);
```
#### Parameters

<a name='Tizen.UI.Components.INavigationTransition.DidAppear(bool).byPopNavigation'></a>

`byPopNavigation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

If true, it is called by pop navigation.

<a name='Tizen.UI.Components.INavigationTransition.DidDisappear(bool)'></a>

## INavigationTransition.DidDisappear(bool) Method

Called right after disappearing by navigation transition.

```csharp
void DidDisappear(bool byPopNavigation);
```
#### Parameters

<a name='Tizen.UI.Components.INavigationTransition.DidDisappear(bool).byPopNavigation'></a>

`byPopNavigation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

If true, it is called by pop navigation.

### Remarks
A view disappeared by pop navigation can be disposed if the view is not used anymore.

<a name='Tizen.UI.Components.INavigationTransition.WillAppear(bool)'></a>

## INavigationTransition.WillAppear(bool) Method

Called right before appearing by navigation transition.

```csharp
void WillAppear(bool byPopNavigation);
```
#### Parameters

<a name='Tizen.UI.Components.INavigationTransition.WillAppear(bool).byPopNavigation'></a>

`byPopNavigation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

If true, it is called by pop navigation.

<a name='Tizen.UI.Components.INavigationTransition.WillDisappear(bool)'></a>

## INavigationTransition.WillDisappear(bool) Method

Called right before disappearing by navigation transition.

```csharp
void WillDisappear(bool byPopNavigation);
```
#### Parameters

<a name='Tizen.UI.Components.INavigationTransition.WillDisappear(bool).byPopNavigation'></a>

`byPopNavigation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

If true, it is called by pop navigation.


























































