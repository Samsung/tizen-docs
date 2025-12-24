### [Tizen.UI.Components.Animations](Tizen.UI.Components.Animations.md 'Tizen.UI.Components.Animations')

## AnimationExtensions Class

Provides extension methods for UIAnimation

```csharp
public static class AnimationExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; AnimationExtensions
### Methods

<a name='Tizen.UI.Components.Animations.AnimationExtensions.AbortAnimation(thisTizen.UI.View,string)'></a>

## AnimationExtensions.AbortAnimation(this View, string) Method

Aborts the animation with the specified handle.

```csharp
public static bool AbortAnimation(this Tizen.UI.View self, string handle);
```
#### Parameters

<a name='Tizen.UI.Components.Animations.AnimationExtensions.AbortAnimation(thisTizen.UI.View,string).self'></a>

`self` Tizen.UI.View

The view to abort the animation on.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.AbortAnimation(thisTizen.UI.View,string).handle'></a>

`handle` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The handle of the animation to abort.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the animation was aborted, false otherwise.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,System.Action_float_,float,float,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_)'></a>

## AnimationExtensions.Animate(this View, string, Action&lt;float>, float, float, uint, uint, Easing, Action&lt;float,bool>, Func&lt;bool>) Method

Animates a property of the view using the specified callback.

```csharp
public static void Animate(this Tizen.UI.View self, string name, System.Action&lt;float> callback, float start, float end, uint rate=16u, uint length=250u, Tizen.UI.Components.Animations.Easing easing=null, System.Action&lt;float,bool> finished=null, System.Func&lt;bool> repeat=null);
```
#### Parameters

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,System.Action_float_,float,float,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).self'></a>

`self` Tizen.UI.View

The view to animate.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,System.Action_float_,float,float,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the property to animate.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,System.Action_float_,float,float,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).callback'></a>

`callback` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')

The callback to invoke during the animation.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,System.Action_float_,float,float,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).start'></a>

`start` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The start value of the animation.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,System.Action_float_,float,float,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).end'></a>

`end` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The end value of the animation.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,System.Action_float_,float,float,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).rate'></a>

`rate` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The rate of the animation in milliseconds.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,System.Action_float_,float,float,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).length'></a>

`length` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The length of the animation in milliseconds.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,System.Action_float_,float,float,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).easing'></a>

`easing` [Easing](Tizen.UI.Components.Animations.Easing.md 'Tizen.UI.Components.Animations.Easing')

The easing function to use for the animation.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,System.Action_float_,float,float,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).finished'></a>

`finished` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

The callback to invoke when the animation is finished.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,System.Action_float_,float,float,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).repeat'></a>

`repeat` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')

The callback to invoke to determine if the animation should repeat.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,System.Action_float_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_)'></a>

## AnimationExtensions.Animate(this View, string, Action&lt;float>, uint, uint, Easing, Action&lt;float,bool>, Func&lt;bool>) Method

Animates a property of the view using the specified callback.

```csharp
public static void Animate(this Tizen.UI.View self, string name, System.Action&lt;float> callback, uint rate=16u, uint length=250u, Tizen.UI.Components.Animations.Easing easing=null, System.Action&lt;float,bool> finished=null, System.Func&lt;bool> repeat=null);
```
#### Parameters

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,System.Action_float_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).self'></a>

`self` Tizen.UI.View

The view to animate.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,System.Action_float_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the property to animate.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,System.Action_float_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).callback'></a>

`callback` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')

The callback to invoke during the animation.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,System.Action_float_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).rate'></a>

`rate` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The rate of the animation in milliseconds.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,System.Action_float_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).length'></a>

`length` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The length of the animation in milliseconds.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,System.Action_float_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).easing'></a>

`easing` [Easing](Tizen.UI.Components.Animations.Easing.md 'Tizen.UI.Components.Animations.Easing')

The easing function to use for the animation.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,System.Action_float_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).finished'></a>

`finished` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

The callback to invoke when the animation is finished.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,System.Action_float_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).repeat'></a>

`repeat` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')

The callback to invoke to determine if the animation should repeat.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,Tizen.UI.Components.Animations.UIAnimation,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_)'></a>

## AnimationExtensions.Animate(this View, string, UIAnimation, uint, uint, Easing, Action&lt;float,bool>, Func&lt;bool>) Method

Animates a property of the view using the specified animation.

```csharp
public static void Animate(this Tizen.UI.View self, string name, Tizen.UI.Components.Animations.UIAnimation animation, uint rate=16u, uint length=250u, Tizen.UI.Components.Animations.Easing easing=null, System.Action&lt;float,bool> finished=null, System.Func&lt;bool> repeat=null);
```
#### Parameters

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,Tizen.UI.Components.Animations.UIAnimation,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).self'></a>

`self` Tizen.UI.View

The view to animate.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,Tizen.UI.Components.Animations.UIAnimation,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the property to animate.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,Tizen.UI.Components.Animations.UIAnimation,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).animation'></a>

`animation` [UIAnimation](Tizen.UI.Components.Animations.UIAnimation.md 'Tizen.UI.Components.Animations.UIAnimation')

The animation to use.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,Tizen.UI.Components.Animations.UIAnimation,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).rate'></a>

`rate` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The rate of the animation in milliseconds.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,Tizen.UI.Components.Animations.UIAnimation,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).length'></a>

`length` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The length of the animation in milliseconds.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,Tizen.UI.Components.Animations.UIAnimation,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).easing'></a>

`easing` [Easing](Tizen.UI.Components.Animations.Easing.md 'Tizen.UI.Components.Animations.Easing')

The easing function to use for the animation.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,Tizen.UI.Components.Animations.UIAnimation,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).finished'></a>

`finished` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

The callback to invoke when the animation is finished.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate(thisTizen.UI.View,string,Tizen.UI.Components.Animations.UIAnimation,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).repeat'></a>

`repeat` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')

The callback to invoke to determine if the animation should repeat.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate_T_(thisTizen.UI.View,string,System.Func_float,T_,System.Action_T_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_T,bool_,System.Func_bool_)'></a>

## AnimationExtensions.Animate&lt;T>(this View, string, Func&lt;float,T>, Action&lt;T>, uint, uint, Easing, Action&lt;T,bool>, Func&lt;bool>) Method

Animates a property of the view using the specified transform and callback.

```csharp
public static void Animate&lt;T>(this Tizen.UI.View self, string name, System.Func&lt;float,T> transform, System.Action&lt;T> callback, uint rate=16u, uint length=250u, Tizen.UI.Components.Animations.Easing easing=null, System.Action&lt;T,bool> finished=null, System.Func&lt;bool> repeat=null);
```
#### Type parameters

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate_T_(thisTizen.UI.View,string,System.Func_float,T_,System.Action_T_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_T,bool_,System.Func_bool_).T'></a>

`T`

The type of the property to animate.
#### Parameters

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate_T_(thisTizen.UI.View,string,System.Func_float,T_,System.Action_T_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_T,bool_,System.Func_bool_).self'></a>

`self` Tizen.UI.View

The view to animate.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate_T_(thisTizen.UI.View,string,System.Func_float,T_,System.Action_T_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_T,bool_,System.Func_bool_).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the property to animate.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate_T_(thisTizen.UI.View,string,System.Func_float,T_,System.Action_T_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_T,bool_,System.Func_bool_).transform'></a>

`transform` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[T](Tizen.UI.Components.Animations.AnimationExtensions.md#Tizen.UI.Components.Animations.AnimationExtensions.Animate_T_(thisTizen.UI.View,string,System.Func_float,T_,System.Action_T_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_T,bool_,System.Func_bool_).T 'Tizen.UI.Components.Animations.AnimationExtensions.Animate&lt;T>(this Tizen.UI.View, string, System.Func&lt;float,T>, System.Action&lt;T>, uint, uint, Tizen.UI.Components.Animations.Easing, System.Action&lt;T,bool>, System.Func&lt;bool>).T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

The transform function to apply during the animation.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate_T_(thisTizen.UI.View,string,System.Func_float,T_,System.Action_T_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_T,bool_,System.Func_bool_).callback'></a>

`callback` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')[T](Tizen.UI.Components.Animations.AnimationExtensions.md#Tizen.UI.Components.Animations.AnimationExtensions.Animate_T_(thisTizen.UI.View,string,System.Func_float,T_,System.Action_T_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_T,bool_,System.Func_bool_).T 'Tizen.UI.Components.Animations.AnimationExtensions.Animate&lt;T>(this Tizen.UI.View, string, System.Func&lt;float,T>, System.Action&lt;T>, uint, uint, Tizen.UI.Components.Animations.Easing, System.Action&lt;T,bool>, System.Func&lt;bool>).T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')

The callback to invoke during the animation.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate_T_(thisTizen.UI.View,string,System.Func_float,T_,System.Action_T_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_T,bool_,System.Func_bool_).rate'></a>

`rate` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The rate of the animation in milliseconds.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate_T_(thisTizen.UI.View,string,System.Func_float,T_,System.Action_T_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_T,bool_,System.Func_bool_).length'></a>

`length` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The length of the animation in milliseconds.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate_T_(thisTizen.UI.View,string,System.Func_float,T_,System.Action_T_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_T,bool_,System.Func_bool_).easing'></a>

`easing` [Easing](Tizen.UI.Components.Animations.Easing.md 'Tizen.UI.Components.Animations.Easing')

The easing function to use for the animation.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate_T_(thisTizen.UI.View,string,System.Func_float,T_,System.Action_T_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_T,bool_,System.Func_bool_).finished'></a>

`finished` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[T](Tizen.UI.Components.Animations.AnimationExtensions.md#Tizen.UI.Components.Animations.AnimationExtensions.Animate_T_(thisTizen.UI.View,string,System.Func_float,T_,System.Action_T_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_T,bool_,System.Func_bool_).T 'Tizen.UI.Components.Animations.AnimationExtensions.Animate&lt;T>(this Tizen.UI.View, string, System.Func&lt;float,T>, System.Action&lt;T>, uint, uint, Tizen.UI.Components.Animations.Easing, System.Action&lt;T,bool>, System.Func&lt;bool>).T')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

The callback to invoke when the animation is finished.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Animate_T_(thisTizen.UI.View,string,System.Func_float,T_,System.Action_T_,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_T,bool_,System.Func_bool_).repeat'></a>

`repeat` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')

The callback to invoke to determine if the animation should repeat.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.AnimateKinetic(thisTizen.UI.View,string,System.Func_float,float,bool_,float,float,System.Action)'></a>

## AnimationExtensions.AnimateKinetic(this View, string, Func&lt;float,float,bool>, float, float, Action) Method

Animates a property of the view using a kinetic motion.

```csharp
public static void AnimateKinetic(this Tizen.UI.View self, string name, System.Func&lt;float,float,bool> callback, float velocity, float drag, System.Action finished=null);
```
#### Parameters

<a name='Tizen.UI.Components.Animations.AnimationExtensions.AnimateKinetic(thisTizen.UI.View,string,System.Func_float,float,bool_,float,float,System.Action).self'></a>

`self` Tizen.UI.View

The view to animate.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.AnimateKinetic(thisTizen.UI.View,string,System.Func_float,float,bool_,float,float,System.Action).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the property to animate.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.AnimateKinetic(thisTizen.UI.View,string,System.Func_float,float,bool_,float,float,System.Action).callback'></a>

`callback` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')

The callback to invoke during the kinetic motion.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.AnimateKinetic(thisTizen.UI.View,string,System.Func_float,float,bool_,float,float,System.Action).velocity'></a>

`velocity` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The initial velocity of the kinetic motion.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.AnimateKinetic(thisTizen.UI.View,string,System.Func_float,float,bool_,float,float,System.Action).drag'></a>

`drag` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The drag coefficient of the kinetic motion.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.AnimateKinetic(thisTizen.UI.View,string,System.Func_float,float,bool_,float,float,System.Action).finished'></a>

`finished` [System.Action](https://docs.microsoft.com/en-us/dotnet/api/System.Action 'System.Action')

The callback to invoke when the kinetic motion is finished.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.AnimationIsRunning(thisTizen.UI.View,string)'></a>

## AnimationExtensions.AnimationIsRunning(this View, string) Method

Determines if an animation with the specified handle is running.

```csharp
public static bool AnimationIsRunning(this Tizen.UI.View self, string handle);
```
#### Parameters

<a name='Tizen.UI.Components.Animations.AnimationExtensions.AnimationIsRunning(thisTizen.UI.View,string).self'></a>

`self` Tizen.UI.View

The view to check for running animations on.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.AnimationIsRunning(thisTizen.UI.View,string).handle'></a>

`handle` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The handle of the animation to check.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the animation is running, false otherwise.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Interpolate(float,float,float,bool)'></a>

## AnimationExtensions.Interpolate(float, float, float, bool) Method

Interpolates between two values.

```csharp
public static System.Func&lt;float,float> Interpolate(float start, float end=1f, float reverseVal=0f, bool reverse=false);
```
#### Parameters

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Interpolate(float,float,float,bool).start'></a>

`start` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The start value of the interpolation.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Interpolate(float,float,float,bool).end'></a>

`end` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The end value of the interpolation. Defaults to 1.0f.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Interpolate(float,float,float,bool).reverseVal'></a>

`reverseVal` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The value to use when reversing the interpolation.

<a name='Tizen.UI.Components.Animations.AnimationExtensions.Interpolate(float,float,float,bool).reverse'></a>

`reverse` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

If true, the interpolation will go from the end value to the start value.

#### Returns
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')  
A function that interpolates between two values based on a given progress value.


























































