### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## Animation3D Class

[Animation3D](Tizen.UI.Scene3D.Animation3D.md 'Tizen.UI.Scene3D.Animation3D') class provides a way to animate [SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject')s in 3D space.

```csharp
public class Animation3D : Tizen.UI.Animation
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.Animation](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Animation 'Tizen.UI.Animation') &#129106; Animation3D
### Constructors

<a name='Tizen.UI.Scene3D.Animation3D.Animation3D()'></a>

## Animation3D() Constructor

Initializes a new instance of the Animation3D class.

```csharp
public Animation3D();
```

<a name='Tizen.UI.Scene3D.Animation3D.Animation3D(System.IntPtr,bool)'></a>

## Animation3D(IntPtr, bool) Constructor

Initializes a new instance of the Animation3D class with specified handle.

```csharp
public Animation3D(System.IntPtr handle, bool ownsHandle);
```
#### Parameters

<a name='Tizen.UI.Scene3D.Animation3D.Animation3D(System.IntPtr,bool).handle'></a>

`handle` [System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')

The handle of the native Animation3D object.

<a name='Tizen.UI.Scene3D.Animation3D.Animation3D(System.IntPtr,bool).ownsHandle'></a>

`ownsHandle` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether the new instance owns the handle.
### Methods

<a name='Tizen.UI.Scene3D.Animation3D.AnimateBy_T_(T,Tizen.UI.Scene3D.Animatable3DPropertyValue_T_,int,int,Tizen.UI.AlphaFunction)'></a>

## Animation3D.AnimateBy&lt;T>(T, Animatable3DPropertyValue&lt;T>, int, int, AlphaFunction) Method

Animates the specified property of the target [SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject') by the specified value.

```csharp
public void AnimateBy&lt;T>(T target, Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T> prop, int delayMs, int durationMs, Tizen.UI.AlphaFunction alpha=null)
    where T : Tizen.UI.Scene3D.SceneObject;
```
#### Type parameters

<a name='Tizen.UI.Scene3D.Animation3D.AnimateBy_T_(T,Tizen.UI.Scene3D.Animatable3DPropertyValue_T_,int,int,Tizen.UI.AlphaFunction).T'></a>

`T`

The type of the target [SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject').
#### Parameters

<a name='Tizen.UI.Scene3D.Animation3D.AnimateBy_T_(T,Tizen.UI.Scene3D.Animatable3DPropertyValue_T_,int,int,Tizen.UI.AlphaFunction).target'></a>

`target` [T](Tizen.UI.Scene3D.Animation3D.md#Tizen.UI.Scene3D.Animation3D.AnimateBy_T_(T,Tizen.UI.Scene3D.Animatable3DPropertyValue_T_,int,int,Tizen.UI.AlphaFunction).T 'Tizen.UI.Scene3D.Animation3D.AnimateBy&lt;T>(T, Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>, int, int, Tizen.UI.AlphaFunction).T')

The target [SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject') to animate.

<a name='Tizen.UI.Scene3D.Animation3D.AnimateBy_T_(T,Tizen.UI.Scene3D.Animatable3DPropertyValue_T_,int,int,Tizen.UI.AlphaFunction).prop'></a>

`prop` [Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')[T](Tizen.UI.Scene3D.Animation3D.md#Tizen.UI.Scene3D.Animation3D.AnimateBy_T_(T,Tizen.UI.Scene3D.Animatable3DPropertyValue_T_,int,int,Tizen.UI.AlphaFunction).T 'Tizen.UI.Scene3D.Animation3D.AnimateBy&lt;T>(T, Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>, int, int, Tizen.UI.AlphaFunction).T')[&gt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')

The property to animate.

<a name='Tizen.UI.Scene3D.Animation3D.AnimateBy_T_(T,Tizen.UI.Scene3D.Animatable3DPropertyValue_T_,int,int,Tizen.UI.AlphaFunction).delayMs'></a>

`delayMs` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The delay before the animation starts, in milliseconds.

<a name='Tizen.UI.Scene3D.Animation3D.AnimateBy_T_(T,Tizen.UI.Scene3D.Animatable3DPropertyValue_T_,int,int,Tizen.UI.AlphaFunction).durationMs'></a>

`durationMs` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The duration of the animation, in milliseconds.

<a name='Tizen.UI.Scene3D.Animation3D.AnimateBy_T_(T,Tizen.UI.Scene3D.Animatable3DPropertyValue_T_,int,int,Tizen.UI.AlphaFunction).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function to apply to the animation.

<a name='Tizen.UI.Scene3D.Animation3D.AnimateTo_T_(T,Tizen.UI.Scene3D.Animatable3DPropertyValue_T_,int,int,Tizen.UI.AlphaFunction)'></a>

## Animation3D.AnimateTo&lt;T>(T, Animatable3DPropertyValue&lt;T>, int, int, AlphaFunction) Method

Animates the specified property of the target [SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject') to the specified value.

```csharp
public void AnimateTo&lt;T>(T target, Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T> prop, int delayMs, int durationMs, Tizen.UI.AlphaFunction alpha=null)
    where T : Tizen.UI.Scene3D.SceneObject;
```
#### Type parameters

<a name='Tizen.UI.Scene3D.Animation3D.AnimateTo_T_(T,Tizen.UI.Scene3D.Animatable3DPropertyValue_T_,int,int,Tizen.UI.AlphaFunction).T'></a>

`T`

The type of the target [SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject').
#### Parameters

<a name='Tizen.UI.Scene3D.Animation3D.AnimateTo_T_(T,Tizen.UI.Scene3D.Animatable3DPropertyValue_T_,int,int,Tizen.UI.AlphaFunction).target'></a>

`target` [T](Tizen.UI.Scene3D.Animation3D.md#Tizen.UI.Scene3D.Animation3D.AnimateTo_T_(T,Tizen.UI.Scene3D.Animatable3DPropertyValue_T_,int,int,Tizen.UI.AlphaFunction).T 'Tizen.UI.Scene3D.Animation3D.AnimateTo&lt;T>(T, Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>, int, int, Tizen.UI.AlphaFunction).T')

The target [SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject') to animate.

<a name='Tizen.UI.Scene3D.Animation3D.AnimateTo_T_(T,Tizen.UI.Scene3D.Animatable3DPropertyValue_T_,int,int,Tizen.UI.AlphaFunction).prop'></a>

`prop` [Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')[T](Tizen.UI.Scene3D.Animation3D.md#Tizen.UI.Scene3D.Animation3D.AnimateTo_T_(T,Tizen.UI.Scene3D.Animatable3DPropertyValue_T_,int,int,Tizen.UI.AlphaFunction).T 'Tizen.UI.Scene3D.Animation3D.AnimateTo&lt;T>(T, Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>, int, int, Tizen.UI.AlphaFunction).T')[&gt;](Tizen.UI.Scene3D.Animatable3DPropertyValue_T_.md 'Tizen.UI.Scene3D.Animatable3DPropertyValue&lt;T>')

The property to animate.

<a name='Tizen.UI.Scene3D.Animation3D.AnimateTo_T_(T,Tizen.UI.Scene3D.Animatable3DPropertyValue_T_,int,int,Tizen.UI.AlphaFunction).delayMs'></a>

`delayMs` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The delay before the animation starts, in milliseconds.

<a name='Tizen.UI.Scene3D.Animation3D.AnimateTo_T_(T,Tizen.UI.Scene3D.Animatable3DPropertyValue_T_,int,int,Tizen.UI.AlphaFunction).durationMs'></a>

`durationMs` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The duration of the animation, in milliseconds.

<a name='Tizen.UI.Scene3D.Animation3D.AnimateTo_T_(T,Tizen.UI.Scene3D.Animatable3DPropertyValue_T_,int,int,Tizen.UI.AlphaFunction).alpha'></a>

`alpha` [Tizen.UI.AlphaFunction](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AlphaFunction 'Tizen.UI.AlphaFunction')

The alpha function to apply to the animation.





































