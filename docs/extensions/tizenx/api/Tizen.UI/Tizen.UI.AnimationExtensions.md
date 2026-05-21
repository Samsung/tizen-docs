### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## AnimationExtensions Class

Provides extension methods for the Animation class.

```csharp
public static class AnimationExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; AnimationExtensions
### Methods

<a name='Tizen.UI.AnimationExtensions.AnimateTo(thisTizen.UI.View,Tizen.UI.AnimatablePropertyValue,int)'></a>

## AnimationExtensions.AnimateTo(this View, AnimatablePropertyValue, int) Method

Animates the specified view to the given value.

```csharp
public static System.Threading.Tasks.Task AnimateTo(this Tizen.UI.View view, Tizen.UI.AnimatablePropertyValue value, int duration=250);
```
#### Parameters

<a name='Tizen.UI.AnimationExtensions.AnimateTo(thisTizen.UI.View,Tizen.UI.AnimatablePropertyValue,int).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to animate.

<a name='Tizen.UI.AnimationExtensions.AnimateTo(thisTizen.UI.View,Tizen.UI.AnimatablePropertyValue,int).value'></a>

`value` [AnimatablePropertyValue](Tizen.UI.AnimatablePropertyValue.md 'Tizen.UI.AnimatablePropertyValue')

The value to animate to.

<a name='Tizen.UI.AnimationExtensions.AnimateTo(thisTizen.UI.View,Tizen.UI.AnimatablePropertyValue,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The duration of the animation, in milliseconds.

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')  
A Task that completes when the animation finishes.

<a name='Tizen.UI.AnimationExtensions.MoveTo(thisTizen.UI.View,float,float,int)'></a>

## AnimationExtensions.MoveTo(this View, float, float, int) Method

Animates the specified view to the given position.

```csharp
public static System.Threading.Tasks.Task MoveTo(this Tizen.UI.View view, float x, float y, int duration=250);
```
#### Parameters

<a name='Tizen.UI.AnimationExtensions.MoveTo(thisTizen.UI.View,float,float,int).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to animate.

<a name='Tizen.UI.AnimationExtensions.MoveTo(thisTizen.UI.View,float,float,int).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the position to animate to.

<a name='Tizen.UI.AnimationExtensions.MoveTo(thisTizen.UI.View,float,float,int).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the position to animate to.

<a name='Tizen.UI.AnimationExtensions.MoveTo(thisTizen.UI.View,float,float,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The duration of the animation, in milliseconds.

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')  
A Task that completes when the animation finishes.

<a name='Tizen.UI.AnimationExtensions.RotateTo(thisTizen.UI.View,float,int)'></a>

## AnimationExtensions.RotateTo(this View, float, int) Method

Animates the specified view to the given rotation.

```csharp
public static System.Threading.Tasks.Task RotateTo(this Tizen.UI.View view, float rotate, int duration=250);
```
#### Parameters

<a name='Tizen.UI.AnimationExtensions.RotateTo(thisTizen.UI.View,float,int).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to animate.

<a name='Tizen.UI.AnimationExtensions.RotateTo(thisTizen.UI.View,float,int).rotate'></a>

`rotate` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The angle of rotation, in degrees.

<a name='Tizen.UI.AnimationExtensions.RotateTo(thisTizen.UI.View,float,int).duration'></a>

`duration` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The duration of the animation, in milliseconds.

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')  
A Task that completes when the animation finishes.






