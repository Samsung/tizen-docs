### [Tizen.UI.Internal](Tizen.UI.Internal.md 'Tizen.UI.Internal')

## RenderModeType Enum

Enumeration for the controls of how this renderer uses its stencil properties and writes to the color buffer.

```csharp
public enum RenderModeType
```
### Fields

<a name='Tizen.UI.Internal.RenderModeType.Auto'></a>

`Auto` 1

Managed by the View Clipping API. This is the default.

<a name='Tizen.UI.Internal.RenderModeType.Color'></a>

`Color` 2

Ingore stencil properties.  Write to the color buffer.

<a name='Tizen.UI.Internal.RenderModeType.ColorStencil'></a>

`ColorStencil` 4

Use the stencil properties AND Write to the color buffer.

<a name='Tizen.UI.Internal.RenderModeType.None'></a>

`None` 0

Do not write to either color or stencil buffer (But will potentially render to depth buffer).

<a name='Tizen.UI.Internal.RenderModeType.Stencil'></a>

`Stencil` 3

Use the stencil properties. Do not write to the color buffer.




