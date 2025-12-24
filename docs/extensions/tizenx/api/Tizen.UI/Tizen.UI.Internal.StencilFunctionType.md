### [Tizen.UI.Internal](Tizen.UI.Internal.md 'Tizen.UI.Internal')

## StencilFunctionType Enum

Enumeration for the comparison function used on the stencil buffer.

```csharp
public enum StencilFunctionType
```
### Fields

<a name='Tizen.UI.Internal.StencilFunctionType.Always'></a>

`Always` 7

Always passes

<a name='Tizen.UI.Internal.StencilFunctionType.Equal'></a>

`Equal` 2

Passes if  ( reference & mask ) =  ( stencil & mask )

<a name='Tizen.UI.Internal.StencilFunctionType.Greater'></a>

`Greater` 4

Passes if  ( reference & mask ) >  ( stencil & mask )

<a name='Tizen.UI.Internal.StencilFunctionType.GreaterEqual'></a>

`GreaterEqual` 6

Passes if  ( reference & mask ) >= ( stencil & mask )

<a name='Tizen.UI.Internal.StencilFunctionType.Less'></a>

`Less` 1

Passes if  ( reference & mask ) &lt;  ( stencil & mask )

<a name='Tizen.UI.Internal.StencilFunctionType.LessEqual'></a>

`LessEqual` 3

Passes if  ( reference & mask ) &lt;= ( stencil & mask )

<a name='Tizen.UI.Internal.StencilFunctionType.Never'></a>

`Never` 0

Always fails

<a name='Tizen.UI.Internal.StencilFunctionType.NotEqual'></a>

`NotEqual` 5

Passes if  ( reference & mask ) != ( stencil & mask )




