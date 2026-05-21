### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## ResizePolicy Enum

The ResizePolicy enum represents the possible resize policies for a view.

```csharp
public enum ResizePolicy
```
### Fields

<a name='Tizen.UI.ResizePolicy.DimensionDependency'></a>

`DimensionDependency` 6

One dimension is dependent on the other.

<a name='Tizen.UI.ResizePolicy.FillToParent'></a>

`FillToParent` 2

Size is to fill up to the actor's parent's bounds. Aspect ratio is not maintained.

<a name='Tizen.UI.ResizePolicy.FitToChildren'></a>

`FitToChildren` 5

The size will adjust to wrap around all children.

<a name='Tizen.UI.ResizePolicy.Fixed'></a>

`Fixed` 0

Size is fixed as set by SetSize.

<a name='Tizen.UI.ResizePolicy.SizeFixedOffsetFromParent'></a>

`SizeFixedOffsetFromParent` 4

The actors size will be ( ParentSize + SizeRelativeToParentFactor ).

<a name='Tizen.UI.ResizePolicy.SizeRelativeToParent'></a>

`SizeRelativeToParent` 3

The actors size will be ( ParentSize * SizeRelativeToParentFactor ).

<a name='Tizen.UI.ResizePolicy.UseAssignedSize'></a>

`UseAssignedSize` 7

The size will be assigned to the actor.

<a name='Tizen.UI.ResizePolicy.UseNaturalSize'></a>

`UseNaturalSize` 1

Size is to use the actor's natural size.






