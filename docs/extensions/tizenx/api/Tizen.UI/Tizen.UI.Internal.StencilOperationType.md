### [Tizen.UI.Internal](Tizen.UI.Internal.md 'Tizen.UI.Internal')

## StencilOperationType Enum

Enumeration for specifying the action to take when the stencil (or depth) test fails during stencil test.

```csharp
public enum StencilOperationType
```
### Fields

<a name='Tizen.UI.Internal.StencilOperationType.Decrement'></a>

`Decrement` 4

Decrements the current stencil buffer value. Clamps to 0

<a name='Tizen.UI.Internal.StencilOperationType.DecrementWrap'></a>

`DecrementWrap` 7

Decrements the current stencil buffer value.  
Wraps stencil buffer value to the maximum representable unsigned value when decrementing a stencil buffer value of zero

<a name='Tizen.UI.Internal.StencilOperationType.Increment'></a>

`Increment` 3

Increments the current stencil buffer value. Clamps to the maximum representable unsigned value

<a name='Tizen.UI.Internal.StencilOperationType.IncrementWrap'></a>

`IncrementWrap` 6

Increments the current stencil buffer value.  
Wraps stencil buffer value to zero when incrementing the maximum representable unsigned value

<a name='Tizen.UI.Internal.StencilOperationType.Invert'></a>

`Invert` 5

Bitwise inverts the current stencil buffer value

<a name='Tizen.UI.Internal.StencilOperationType.Keep'></a>

`Keep` 1

Keeps the current value

<a name='Tizen.UI.Internal.StencilOperationType.Replace'></a>

`Replace` 2

Sets the stencil buffer value to ref, as specified by glStencilFunc

<a name='Tizen.UI.Internal.StencilOperationType.Zero'></a>

`Zero` 0

Sets the stencil buffer value to 0




