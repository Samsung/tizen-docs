### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## SnapControlExtensions Class

Provides extension methods for setting snap points type and alignment on a ScrollView.

```csharp
public static class SnapControlExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; SnapControlExtensions
### Methods

<a name='Tizen.UI.Layouts.SnapControlExtensions.SetSnap_T_(thisT,Tizen.UI.Layouts.SnapPointsType,Tizen.UI.Layouts.SnapPointsAlignment)'></a>

## SnapControlExtensions.SetSnap&lt;T>(this T, SnapPointsType, SnapPointsAlignment) Method

Sets the snap points type and alignment for the given ScrollView.

```csharp
public static T SetSnap&lt;T>(this T scrollView, Tizen.UI.Layouts.SnapPointsType snapType, Tizen.UI.Layouts.SnapPointsAlignment align)
    where T : Tizen.UI.Layouts.ScrollLayout;
```
#### Type parameters

<a name='Tizen.UI.Layouts.SnapControlExtensions.SetSnap_T_(thisT,Tizen.UI.Layouts.SnapPointsType,Tizen.UI.Layouts.SnapPointsAlignment).T'></a>

`T`

The type of the ScrollView.
#### Parameters

<a name='Tizen.UI.Layouts.SnapControlExtensions.SetSnap_T_(thisT,Tizen.UI.Layouts.SnapPointsType,Tizen.UI.Layouts.SnapPointsAlignment).scrollView'></a>

`scrollView` [T](Tizen.UI.Layouts.SnapControlExtensions.md#Tizen.UI.Layouts.SnapControlExtensions.SetSnap_T_(thisT,Tizen.UI.Layouts.SnapPointsType,Tizen.UI.Layouts.SnapPointsAlignment).T 'Tizen.UI.Layouts.SnapControlExtensions.SetSnap&lt;T>(this T, Tizen.UI.Layouts.SnapPointsType, Tizen.UI.Layouts.SnapPointsAlignment).T')

The ScrollView to apply the snap settings to.

<a name='Tizen.UI.Layouts.SnapControlExtensions.SetSnap_T_(thisT,Tizen.UI.Layouts.SnapPointsType,Tizen.UI.Layouts.SnapPointsAlignment).snapType'></a>

`snapType` [SnapPointsType](Tizen.UI.Layouts.SnapPointsType.md 'Tizen.UI.Layouts.SnapPointsType')

The type of snap points to use

<a name='Tizen.UI.Layouts.SnapControlExtensions.SetSnap_T_(thisT,Tizen.UI.Layouts.SnapPointsType,Tizen.UI.Layouts.SnapPointsAlignment).align'></a>

`align` [SnapPointsAlignment](Tizen.UI.Layouts.SnapPointsAlignment.md 'Tizen.UI.Layouts.SnapPointsAlignment')

The alignment of the snap points (e.g., Center, Start, End).

#### Returns
[T](Tizen.UI.Layouts.SnapControlExtensions.md#Tizen.UI.Layouts.SnapControlExtensions.SetSnap_T_(thisT,Tizen.UI.Layouts.SnapPointsType,Tizen.UI.Layouts.SnapPointsAlignment).T 'Tizen.UI.Layouts.SnapControlExtensions.SetSnap&lt;T>(this T, Tizen.UI.Layouts.SnapPointsType, Tizen.UI.Layouts.SnapPointsAlignment).T')  
The modified ScrollView instance.






























































