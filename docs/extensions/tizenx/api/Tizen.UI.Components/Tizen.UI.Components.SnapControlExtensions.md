### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## SnapControlExtensions Class

Provides extension methods for setting snap points type and alignment on a Scrollable.

```csharp
public static class SnapControlExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; SnapControlExtensions
### Methods

<a name='Tizen.UI.Components.SnapControlExtensions.SetSnap_T_(thisT,Tizen.UI.Layouts.SnapPointsType,Tizen.UI.Layouts.SnapPointsAlignment)'></a>

## SnapControlExtensions.SetSnap&lt;T>(this T, SnapPointsType, SnapPointsAlignment) Method

Sets the snap points type and alignment for the given Scrollable.

```csharp
public static T SetSnap&lt;T>(this T Scrollable, Tizen.UI.Layouts.SnapPointsType snapType, Tizen.UI.Layouts.SnapPointsAlignment align)
    where T : Tizen.UI.Components.Scrollable;
```
#### Type parameters

<a name='Tizen.UI.Components.SnapControlExtensions.SetSnap_T_(thisT,Tizen.UI.Layouts.SnapPointsType,Tizen.UI.Layouts.SnapPointsAlignment).T'></a>

`T`

The type of the Scrollable.
#### Parameters

<a name='Tizen.UI.Components.SnapControlExtensions.SetSnap_T_(thisT,Tizen.UI.Layouts.SnapPointsType,Tizen.UI.Layouts.SnapPointsAlignment).Scrollable'></a>

`Scrollable` [T](Tizen.UI.Components.SnapControlExtensions.md#Tizen.UI.Components.SnapControlExtensions.SetSnap_T_(thisT,Tizen.UI.Layouts.SnapPointsType,Tizen.UI.Layouts.SnapPointsAlignment).T 'Tizen.UI.Components.SnapControlExtensions.SetSnap&lt;T>(this T, Tizen.UI.Layouts.SnapPointsType, Tizen.UI.Layouts.SnapPointsAlignment).T')

The Scrollable to apply the snap settings to.

<a name='Tizen.UI.Components.SnapControlExtensions.SetSnap_T_(thisT,Tizen.UI.Layouts.SnapPointsType,Tizen.UI.Layouts.SnapPointsAlignment).snapType'></a>

`snapType` [Tizen.UI.Layouts.SnapPointsType](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Layouts.SnapPointsType 'Tizen.UI.Layouts.SnapPointsType')

The type of snap points to use

<a name='Tizen.UI.Components.SnapControlExtensions.SetSnap_T_(thisT,Tizen.UI.Layouts.SnapPointsType,Tizen.UI.Layouts.SnapPointsAlignment).align'></a>

`align` [Tizen.UI.Layouts.SnapPointsAlignment](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Layouts.SnapPointsAlignment 'Tizen.UI.Layouts.SnapPointsAlignment')

The alignment of the snap points (e.g., Center, Start, End).

#### Returns
[T](Tizen.UI.Components.SnapControlExtensions.md#Tizen.UI.Components.SnapControlExtensions.SetSnap_T_(thisT,Tizen.UI.Layouts.SnapPointsType,Tizen.UI.Layouts.SnapPointsAlignment).T 'Tizen.UI.Components.SnapControlExtensions.SetSnap&lt;T>(this T, Tizen.UI.Layouts.SnapPointsType, Tizen.UI.Layouts.SnapPointsAlignment).T')  
The modified Scrollable instance.


























































