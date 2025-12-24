### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## GridUnitType Enum

Enumerates values that control how the [Value](Tizen.UI.Layouts.GridLength.md#Tizen.UI.Layouts.GridLength.Value 'Tizen.UI.Layouts.GridLength.Value') property is interpreted for row and column definitions.

```csharp
public enum GridUnitType
```
### Fields

<a name='Tizen.UI.Layouts.GridUnitType.Absolute'></a>

`Absolute` 0

Interpret the [Value](Tizen.UI.Layouts.GridLength.md#Tizen.UI.Layouts.GridLength.Value 'Tizen.UI.Layouts.GridLength.Value') property value as the number of device-specific units.

<a name='Tizen.UI.Layouts.GridUnitType.Auto'></a>

`Auto` 2

Interpret the [Value](Tizen.UI.Layouts.GridLength.md#Tizen.UI.Layouts.GridLength.Value 'Tizen.UI.Layouts.GridLength.Value') property value as a proportional weight, to be laid out after rows and columns with Absolute or Auto are accounted for.

<a name='Tizen.UI.Layouts.GridUnitType.Star'></a>

`Star` 1

Ignore the [Value](Tizen.UI.Layouts.GridLength.md#Tizen.UI.Layouts.GridLength.Value 'Tizen.UI.Layouts.GridLength.Value') property value and choose a size that fits the children of the row or column.






























































