### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## AnimatedLayout Class

Provides animated layout functionalities

```csharp
public static class AnimatedLayout
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; AnimatedLayout
### Methods

<a name='Tizen.UI.Components.AnimatedLayout.ApplyAnimation_T_(thisT,int,Tizen.UI.AlphaFunction)'></a>

## AnimatedLayout.ApplyAnimation&lt;T>(this T, int, AlphaFunction) Method

Applies an animation to child position and size changes when the layout is updated.

```csharp
public static T ApplyAnimation&lt;T>(this T layout, int duration=150, Tizen.UI.AlphaFunction alphaFunction=null)
    where T : Tizen.UI.Layouts.Layout;
```
#### Type parameters

<a name='Tizen.UI.Components.AnimatedLayout.ApplyAnimation_T_(thisT,int,Tizen.UI.AlphaFunction).T'></a>

`T`

The type of the layout.
#### Parameters

<a name='Tizen.UI.Components.AnimatedLayout.ApplyAnimation_T_(thisT,int,Tizen.UI.AlphaFunction).layout'></a>

`layout` [T](Tizen.UI.Components.AnimatedLayout.md#Tizen.UI.Components.AnimatedLayout.ApplyAnimation_T_(thisT,int,Tizen.UI.AlphaFunction).T 'Tizen.UI.Components.AnimatedLayout.ApplyAnimation&lt;T>(this T, int, Tizen.UI.AlphaFunction).T')

The layout to animate.

<a name='Tizen.UI.Components.AnimatedLayout.ApplyAnimation_T_(thisT,int,Tizen.UI.AlphaFunction).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The duration of the animation in milliseconds.

<a name='Tizen.UI.Components.AnimatedLayout.ApplyAnimation_T_(thisT,int,Tizen.UI.AlphaFunction).alphaFunction'></a>

`alphaFunction` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function applied to the animation. Can be null.

#### Returns
[T](Tizen.UI.Components.AnimatedLayout.md#Tizen.UI.Components.AnimatedLayout.ApplyAnimation_T_(thisT,int,Tizen.UI.AlphaFunction).T 'Tizen.UI.Components.AnimatedLayout.ApplyAnimation&lt;T>(this T, int, Tizen.UI.AlphaFunction).T')  
The layout with animation applied.


























































