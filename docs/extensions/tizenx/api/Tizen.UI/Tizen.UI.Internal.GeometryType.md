### [Tizen.UI.Internal](Tizen.UI.Internal.md 'Tizen.UI.Internal')

## GeometryType Enum

Enumeration for the description of the type of geometry,  
used to determine how the coordinates will be used.

```csharp
public enum GeometryType
```
### Fields

<a name='Tizen.UI.Internal.GeometryType.LINE_LOOP'></a>

`LINE_LOOP` 2

A strip of lines (made of 1 point each) which also joins the first and last point.

<a name='Tizen.UI.Internal.GeometryType.LINE_STRIP'></a>

`LINE_STRIP` 3

A strip of lines (made of 1 point each).

<a name='Tizen.UI.Internal.GeometryType.LINES'></a>

`LINES` 1

Individual lines (made of 2 points each).

<a name='Tizen.UI.Internal.GeometryType.POINTS'></a>

`POINTS` 0

Individual points.

<a name='Tizen.UI.Internal.GeometryType.TRIANGLE_FAN'></a>

`TRIANGLE_FAN` 5

A fan of triangles around a centre point (after the first triangle, following triangles need only 1 point).

<a name='Tizen.UI.Internal.GeometryType.TRIANGLE_STRIP'></a>

`TRIANGLE_STRIP` 6

A strip of triangles (after the first triangle, following triangles need only 1 point).

<a name='Tizen.UI.Internal.GeometryType.TRIANGLES'></a>

`TRIANGLES` 4

Individual triangles (made of 3 points each).




