### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## IDescendantFocusObserver Interface

The IDescendantFocusObserver interface defines a contract for classes that wish to receive notifications when a descendant view receives focus.

```csharp
public interface IDescendantFocusObserver
```
### Methods

<a name='Tizen.UI.IDescendantFocusObserver.OnDescendantFocused(Tizen.UI.View)'></a>

## IDescendantFocusObserver.OnDescendantFocused(View) Method

Called when a descendant view receives focus.

```csharp
void OnDescendantFocused(Tizen.UI.View descendant);
```
#### Parameters

<a name='Tizen.UI.IDescendantFocusObserver.OnDescendantFocused(Tizen.UI.View).descendant'></a>

`descendant` [View](Tizen.UI.View.md 'Tizen.UI.View')

The descendant view that received focus.






