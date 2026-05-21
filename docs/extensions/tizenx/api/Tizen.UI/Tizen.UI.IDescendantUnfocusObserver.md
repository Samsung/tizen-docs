### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## IDescendantUnfocusObserver Interface

The IDescendantUnfocusObserver interface defines a contract for classes that wish to receive notifications when a descendant view loses focus.

```csharp
public interface IDescendantUnfocusObserver
```
### Methods

<a name='Tizen.UI.IDescendantUnfocusObserver.OnDescendantUnfocused(Tizen.UI.View)'></a>

## IDescendantUnfocusObserver.OnDescendantUnfocused(View) Method

Called when a descendant view loses focus.

```csharp
void OnDescendantUnfocused(Tizen.UI.View descendant);
```
#### Parameters

<a name='Tizen.UI.IDescendantUnfocusObserver.OnDescendantUnfocused(Tizen.UI.View).descendant'></a>

`descendant` [View](Tizen.UI.View.md 'Tizen.UI.View')

The descendant view that lost focus.






