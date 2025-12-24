### [Tizen.UI.Components.Animations](Tizen.UI.Components.Animations.md 'Tizen.UI.Components.Animations')

## TypedAnimationExtensions Class

Provides extension methods for typed animation.

```csharp
public static class TypedAnimationExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; TypedAnimationExtensions
### Methods

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.Animate_T_(thisTizen.UI.Animation,T)'></a>

## TypedAnimationExtensions.Animate&lt;T>(this Animation, T) Method

Prepare to animate a given target view. This returns a bridge providing various animatable properties for the target view.

```csharp
public static Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> Animate&lt;T>(this Tizen.UI.Animation animation, T targetView)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.Animate_T_(thisTizen.UI.Animation,T).T'></a>

`T`

The type of the target view.
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.Animate_T_(thisTizen.UI.Animation,T).animation'></a>

`animation` [Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')

The animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.Animate_T_(thisTizen.UI.Animation,T).targetView'></a>

`targetView` [T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.Animate_T_(thisTizen.UI.Animation,T).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.Animate&lt;T>(this Tizen.UI.Animation, T).T')

The target view to be animated.

#### Returns
[Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.Animate_T_(thisTizen.UI.Animation,T).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.Animate&lt;T>(this Tizen.UI.Animation, T).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')  
The bridge providing various animatable properties for the target view.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BackgroundColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.BackgroundColorBy&lt;T>(this TypedAnimationTargetBridge&lt;T>, Color, int, AlphaFunction, int) Method

Animate background color by relative mount.

```csharp
public static Tizen.UI.Animation BackgroundColorBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, Tizen.UI.Color relativeValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BackgroundColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BackgroundColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.BackgroundColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.BackgroundColorBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, Tizen.UI.Color, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BackgroundColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).relativeValue'></a>

`relativeValue` [Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

The relative value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BackgroundColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BackgroundColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BackgroundColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BackgroundColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.BackgroundColorTo&lt;T>(this TypedAnimationTargetBridge&lt;T>, Color, int, AlphaFunction, int) Method

Animate background color to destination value.

```csharp
public static Tizen.UI.Animation BackgroundColorTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, Tizen.UI.Color destinationValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BackgroundColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BackgroundColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.BackgroundColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.BackgroundColorTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, Tizen.UI.Color, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BackgroundColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).destinationValue'></a>

`destinationValue` [Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

The destination value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BackgroundColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BackgroundColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BackgroundColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowBlurRadiusBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.BoxShadowBlurRadiusBy&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, int, AlphaFunction, int) Method

Animate box shadow's blur radius by relative mount.

```csharp
public static Tizen.UI.Animation BoxShadowBlurRadiusBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float relativeValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowBlurRadiusBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowBlurRadiusBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowBlurRadiusBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowBlurRadiusBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowBlurRadiusBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).relativeValue'></a>

`relativeValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The relative value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowBlurRadiusBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowBlurRadiusBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowBlurRadiusBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowBlurRadiusTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.BoxShadowBlurRadiusTo&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, int, AlphaFunction, int) Method

Animate box shadow's blur radius to destination value.

```csharp
public static Tizen.UI.Animation BoxShadowBlurRadiusTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float destinationValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowBlurRadiusTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowBlurRadiusTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowBlurRadiusTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowBlurRadiusTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowBlurRadiusTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).destinationValue'></a>

`destinationValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The destination value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowBlurRadiusTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowBlurRadiusTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowBlurRadiusTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOffsetBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.BoxShadowOffsetBy&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, float, int, AlphaFunction, int) Method

Animate box shadow's offset by relative mount.

```csharp
public static Tizen.UI.Animation BoxShadowOffsetBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float x, float y, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOffsetBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOffsetBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOffsetBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOffsetBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOffsetBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The relative x value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOffsetBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The relative y value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOffsetBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOffsetBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOffsetBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOffsetTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.BoxShadowOffsetTo&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, float, int, AlphaFunction, int) Method

Animate box shadow's offset to destination value.

```csharp
public static Tizen.UI.Animation BoxShadowOffsetTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float x, float y, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOffsetTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOffsetTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOffsetTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOffsetTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOffsetTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The destination x value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOffsetTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The destination y value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOffsetTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOffsetTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOffsetTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOpacityBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.BoxShadowOpacityBy&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, int, AlphaFunction, int) Method

Animate box shadow's opacity by relative mount.

```csharp
public static Tizen.UI.Animation BoxShadowOpacityBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float relativeValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOpacityBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOpacityBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOpacityBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOpacityBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOpacityBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).relativeValue'></a>

`relativeValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The relative value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOpacityBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOpacityBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOpacityBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOpacityTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.BoxShadowOpacityTo&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, int, AlphaFunction, int) Method

Animate box shadow's opacity to destination value.

```csharp
public static Tizen.UI.Animation BoxShadowOpacityTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float destinationValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOpacityTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOpacityTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOpacityTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOpacityTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOpacityTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).destinationValue'></a>

`destinationValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The destination value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOpacityTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOpacityTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.BoxShadowOpacityTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.ColorBy&lt;T>(this TypedAnimationTargetBridge&lt;T>, Color, int, AlphaFunction, int) Method

Animate color by relative mount.

```csharp
public static Tizen.UI.Animation ColorBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, Tizen.UI.Color relativeValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.ColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.ColorBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, Tizen.UI.Color, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).relativeValue'></a>

`relativeValue` [Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

The relative value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.ColorTo&lt;T>(this TypedAnimationTargetBridge&lt;T>, Color, int, AlphaFunction, int) Method

Animate color to destination value.

```csharp
public static Tizen.UI.Animation ColorTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, Tizen.UI.Color destinationValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.ColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.ColorTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, Tizen.UI.Color, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).destinationValue'></a>

`destinationValue` [Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

The destination value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerRadiusBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.CornerRadiusBy&lt;T>(this TypedAnimationTargetBridge&lt;T>, CornerRadius, int, AlphaFunction, int) Method

Animate corner radius by relative mount.

```csharp
public static Tizen.UI.Animation CornerRadiusBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, Tizen.UI.CornerRadius relativeValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerRadiusBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerRadiusBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerRadiusBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerRadiusBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, Tizen.UI.CornerRadius, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerRadiusBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).relativeValue'></a>

`relativeValue` [Tizen.UI.CornerRadius](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.CornerRadius 'Tizen.UI.CornerRadius')

The relative value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerRadiusBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerRadiusBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerRadiusBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerRadiusTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.CornerRadiusTo&lt;T>(this TypedAnimationTargetBridge&lt;T>, CornerRadius, int, AlphaFunction, int) Method

Animate corner radius to destination value.

```csharp
public static Tizen.UI.Animation CornerRadiusTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, Tizen.UI.CornerRadius destinationValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerRadiusTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerRadiusTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerRadiusTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerRadiusTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, Tizen.UI.CornerRadius, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerRadiusTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).destinationValue'></a>

`destinationValue` [Tizen.UI.CornerRadius](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.CornerRadius 'Tizen.UI.CornerRadius')

The destination value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerRadiusTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerRadiusTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerRadiusTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerSquarenessBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.CornerSquarenessBy&lt;T>(this TypedAnimationTargetBridge&lt;T>, CornerRadius, int, AlphaFunction, int) Method

Animate corner squareness by relative mount.

```csharp
public static Tizen.UI.Animation CornerSquarenessBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, Tizen.UI.CornerRadius relativeValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerSquarenessBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerSquarenessBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerSquarenessBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerSquarenessBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, Tizen.UI.CornerRadius, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerSquarenessBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).relativeValue'></a>

`relativeValue` [Tizen.UI.CornerRadius](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.CornerRadius 'Tizen.UI.CornerRadius')

The relative value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerSquarenessBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerSquarenessBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerSquarenessBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerSquarenessTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.CornerSquarenessTo&lt;T>(this TypedAnimationTargetBridge&lt;T>, CornerRadius, int, AlphaFunction, int) Method

Animate corner squareness to destination value.

```csharp
public static Tizen.UI.Animation CornerSquarenessTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, Tizen.UI.CornerRadius destinationValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerSquarenessTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerSquarenessTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerSquarenessTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerSquarenessTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, Tizen.UI.CornerRadius, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerSquarenessTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).destinationValue'></a>

`destinationValue` [Tizen.UI.CornerRadius](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.CornerRadius 'Tizen.UI.CornerRadius')

The destination value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerSquarenessTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerSquarenessTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.CornerSquarenessTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.CornerRadius,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.HeightBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.HeightBy&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, int, AlphaFunction, int) Method

Animate size-height by relative mount.

```csharp
public static Tizen.UI.Animation HeightBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float relativeValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.HeightBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.HeightBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.HeightBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.HeightBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.HeightBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).relativeValue'></a>

`relativeValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The relative value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.HeightBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.HeightBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.HeightBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.HeightTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.HeightTo&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, int, AlphaFunction, int) Method

Animate size-height to destination value.

```csharp
public static Tizen.UI.Animation HeightTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float destinationValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.HeightTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.HeightTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.HeightTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.HeightTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.HeightTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).destinationValue'></a>

`destinationValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The destination value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.HeightTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.HeightTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.HeightTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.OpacityBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.OpacityBy&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, int, AlphaFunction, int) Method

Animate opacity by relative mount.

```csharp
public static Tizen.UI.Animation OpacityBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float relativeValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.OpacityBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.OpacityBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.OpacityBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.OpacityBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.OpacityBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).relativeValue'></a>

`relativeValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The relative value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.OpacityBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.OpacityBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.OpacityBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.OpacityTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.OpacityTo&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, int, AlphaFunction, int) Method

Animate opacity to destination value.

```csharp
public static Tizen.UI.Animation OpacityTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float destinationValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.OpacityTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.OpacityTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.OpacityTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.OpacityTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.OpacityTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).destinationValue'></a>

`destinationValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The destination value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.OpacityTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.OpacityTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.OpacityTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.PositionBy&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, float, int, AlphaFunction, int) Method

Animate position-x by relative mount.

```csharp
public static Tizen.UI.Animation PositionBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float relativeX, float relativeY, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).relativeX'></a>

`relativeX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The relative X value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).relativeY'></a>

`relativeY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The relative Y value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Point,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.PositionBy&lt;T>(this TypedAnimationTargetBridge&lt;T>, Point, int, AlphaFunction, int) Method

Animate position-x by relative mount.

```csharp
public static Tizen.UI.Animation PositionBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, Tizen.UI.Point relativeValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Point,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Point,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Point,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, Tizen.UI.Point, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Point,int,Tizen.UI.AlphaFunction,int).relativeValue'></a>

`relativeValue` [Tizen.UI.Point](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Point 'Tizen.UI.Point')

The relative value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Point,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Point,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Point,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.PositionTo&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, float, int, AlphaFunction, int) Method

Animate position to destination value.

```csharp
public static Tizen.UI.Animation PositionTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float destinationX, float destinationY, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).destinationX'></a>

`destinationX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The destination X value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).destinationY'></a>

`destinationY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The destination X value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Point,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.PositionTo&lt;T>(this TypedAnimationTargetBridge&lt;T>, Point, int, AlphaFunction, int) Method

Animate position to destination value.

```csharp
public static Tizen.UI.Animation PositionTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, Tizen.UI.Point destinationValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Point,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Point,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Point,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, Tizen.UI.Point, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Point,int,Tizen.UI.AlphaFunction,int).destinationValue'></a>

`destinationValue` [Tizen.UI.Point](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Point 'Tizen.UI.Point')

The destination value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Point,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Point,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Point,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionXBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.PositionXBy&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, int, AlphaFunction, int) Method

Animate position-x by relative mount.

```csharp
public static Tizen.UI.Animation PositionXBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float relativeValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionXBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionXBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionXBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionXBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionXBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).relativeValue'></a>

`relativeValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The relative value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionXBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionXBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionXBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionXTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.PositionXTo&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, int, AlphaFunction, int) Method

Animate position-x to destination value.

```csharp
public static Tizen.UI.Animation PositionXTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float destinationValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionXTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionXTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionXTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionXTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionXTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).destinationValue'></a>

`destinationValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The destination value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionXTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionXTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionXTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionYBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.PositionYBy&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, int, AlphaFunction, int) Method

Animate position-y by relative mount.

```csharp
public static Tizen.UI.Animation PositionYBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float relativeValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionYBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionYBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionYBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionYBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionYBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).relativeValue'></a>

`relativeValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The relative value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionYBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionYBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionYBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionYTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.PositionYTo&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, int, AlphaFunction, int) Method

Animate position-y to destination value.

```csharp
public static Tizen.UI.Animation PositionYTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float destinationValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionYTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionYTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionYTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionYTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionYTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).destinationValue'></a>

`destinationValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The destination value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionYTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionYTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.PositionYTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.ScaleBy&lt;T>(this TypedAnimationTargetBridge&lt;T>, Size, int, AlphaFunction, int) Method

Animate scale by relative mount.

```csharp
public static Tizen.UI.Animation ScaleBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, Tizen.UI.Size relativeValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, Tizen.UI.Size, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).relativeValue'></a>

`relativeValue` [Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')

The relative value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.ScaleTo&lt;T>(this TypedAnimationTargetBridge&lt;T>, Size, int, AlphaFunction, int) Method

Animate scale to destination value.

```csharp
public static Tizen.UI.Animation ScaleTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, Tizen.UI.Size destinationValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, Tizen.UI.Size, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).destinationValue'></a>

`destinationValue` [Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')

The destination value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleXBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.ScaleXBy&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, int, AlphaFunction, int) Method

Animate scale-x by relative mount.

```csharp
public static Tizen.UI.Animation ScaleXBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float relativeValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleXBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleXBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleXBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleXBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleXBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).relativeValue'></a>

`relativeValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The relative value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleXBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleXBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleXBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleXTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.ScaleXTo&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, int, AlphaFunction, int) Method

Animate scale-x to destination value.

```csharp
public static Tizen.UI.Animation ScaleXTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float destinationValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleXTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleXTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleXTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleXTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleXTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).destinationValue'></a>

`destinationValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The destination value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleXTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleXTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleXTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleYBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.ScaleYBy&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, int, AlphaFunction, int) Method

Animate scale-y by relative mount.

```csharp
public static Tizen.UI.Animation ScaleYBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float relativeValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleYBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleYBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleYBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleYBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleYBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).relativeValue'></a>

`relativeValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The relative value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleYBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleYBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleYBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleYTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.ScaleYTo&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, int, AlphaFunction, int) Method

Animate scale-y to destination value.

```csharp
public static Tizen.UI.Animation ScaleYTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float destinationValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleYTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleYTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleYTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleYTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleYTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).destinationValue'></a>

`destinationValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The destination value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleYTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleYTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.ScaleYTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.SizeBy&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, float, int, AlphaFunction, int) Method

Animate size-width by relative mount.

```csharp
public static Tizen.UI.Animation SizeBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float relativeX, float relativeY, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).relativeX'></a>

`relativeX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The relative X value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).relativeY'></a>

`relativeY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The relative Y value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.SizeBy&lt;T>(this TypedAnimationTargetBridge&lt;T>, Size, int, AlphaFunction, int) Method

Animate size-width by relative mount.

```csharp
public static Tizen.UI.Animation SizeBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, Tizen.UI.Size relativeValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, Tizen.UI.Size, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).relativeValue'></a>

`relativeValue` [Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')

The relative value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.SizeTo&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, float, int, AlphaFunction, int) Method

Animate size-width to destination value.

```csharp
public static Tizen.UI.Animation SizeTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float destinationX, float destinationY, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).destinationX'></a>

`destinationX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The destination X value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).destinationY'></a>

`destinationY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The destination Y value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.SizeTo&lt;T>(this TypedAnimationTargetBridge&lt;T>, Size, int, AlphaFunction, int) Method

Animate size-width to destination value.

```csharp
public static Tizen.UI.Animation SizeTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, Tizen.UI.Size destinationValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, Tizen.UI.Size, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).destinationValue'></a>

`destinationValue` [Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')

The destination value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.SizeTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Size,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.TextColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.TextColorBy&lt;T>(this TypedAnimationTargetBridge&lt;T>, Color, int, AlphaFunction, int) Method

Animate text color by relative mount.

```csharp
public static Tizen.UI.Animation TextColorBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, Tizen.UI.Color relativeValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View, Tizen.UI.IText;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.TextColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.TextColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.TextColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.TextColorBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, Tizen.UI.Color, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.TextColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).relativeValue'></a>

`relativeValue` [Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

The relative value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.TextColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.TextColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.TextColorBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.TextColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.TextColorTo&lt;T>(this TypedAnimationTargetBridge&lt;T>, Color, int, AlphaFunction, int) Method

Animate text color to destination value.

```csharp
public static Tizen.UI.Animation TextColorTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, Tizen.UI.Color destinationValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View, Tizen.UI.IText;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.TextColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.TextColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.TextColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.TextColorTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, Tizen.UI.Color, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.TextColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).destinationValue'></a>

`destinationValue` [Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

The destination value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.TextColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.TextColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.TextColorTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,Tizen.UI.Color,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.WidthBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.WidthBy&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, int, AlphaFunction, int) Method

Animate size-width by relative mount.

```csharp
public static Tizen.UI.Animation WidthBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float relativeValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.WidthBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.WidthBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.WidthBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.WidthBy&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.WidthBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).relativeValue'></a>

`relativeValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The relative value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.WidthBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.WidthBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.WidthBy_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.WidthTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int)'></a>

## TypedAnimationExtensions.WidthTo&lt;T>(this TypedAnimationTargetBridge&lt;T>, float, int, AlphaFunction, int) Method

Animate size-width to destination value.

```csharp
public static Tizen.UI.Animation WidthTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T> target, float destinationValue, int duration, Tizen.UI.AlphaFunction alpha=null, int delay=0)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.WidthTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.WidthTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).target'></a>

`target` [Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')[T](Tizen.UI.Components.Animations.TypedAnimationExtensions.md#Tizen.UI.Components.Animations.TypedAnimationExtensions.WidthTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).T 'Tizen.UI.Components.Animations.TypedAnimationExtensions.WidthTo&lt;T>(this Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>, float, int, Tizen.UI.AlphaFunction, int).T')[&gt;](Tizen.UI.Components.Animations.TypedAnimationTargetBridge_T_.md 'Tizen.UI.Components.Animations.TypedAnimationTargetBridge&lt;T>')

The extension target.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.WidthTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).destinationValue'></a>

`destinationValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The destination value.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.WidthTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation duration in milliseconds.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.WidthTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function for the animation.

<a name='Tizen.UI.Components.Animations.TypedAnimationExtensions.WidthTo_T_(thisTizen.UI.Components.Animations.TypedAnimationTargetBridge_T_,float,int,Tizen.UI.AlphaFunction,int).delay'></a>

`delay` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The animation delay in milliseconds.

#### Returns
[Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation')  
The typed animation instance.























































