### [Tizen.UI.Components.Animations](Tizen.UI.Components.Animations.md 'Tizen.UI.Components.Animations')

## UIAnimation Class

Represents an animation that can be composed of multiple sub-animations.

```csharp
public class UIAnimation :
System.Collections.IEnumerable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; UIAnimation

Implements [System.Collections.IEnumerable](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable 'System.Collections.IEnumerable')
### Constructors

<a name='Tizen.UI.Components.Animations.UIAnimation.UIAnimation()'></a>

## UIAnimation() Constructor

Initializes a new instance of the UIAnimation class.

```csharp
public UIAnimation();
```

<a name='Tizen.UI.Components.Animations.UIAnimation.UIAnimation(System.Action_float_,float,float,Tizen.UI.Components.Animations.Easing,System.Action)'></a>

## UIAnimation(Action&lt;float>, float, float, Easing, Action) Constructor

Initializes a new instance of the UIAnimation class with the specified callback and range.

```csharp
public UIAnimation(System.Action&lt;float> callback, float start=0f, float end=1f, Tizen.UI.Components.Animations.Easing easing=null, System.Action finished=null);
```
#### Parameters

<a name='Tizen.UI.Components.Animations.UIAnimation.UIAnimation(System.Action_float_,float,float,Tizen.UI.Components.Animations.Easing,System.Action).callback'></a>

`callback` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')

The callback to invoke during the animation.

<a name='Tizen.UI.Components.Animations.UIAnimation.UIAnimation(System.Action_float_,float,float,Tizen.UI.Components.Animations.Easing,System.Action).start'></a>

`start` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The start value of the animation.

<a name='Tizen.UI.Components.Animations.UIAnimation.UIAnimation(System.Action_float_,float,float,Tizen.UI.Components.Animations.Easing,System.Action).end'></a>

`end` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The end value of the animation.

<a name='Tizen.UI.Components.Animations.UIAnimation.UIAnimation(System.Action_float_,float,float,Tizen.UI.Components.Animations.Easing,System.Action).easing'></a>

`easing` [Easing](Tizen.UI.Components.Animations.Easing.md 'Tizen.UI.Components.Animations.Easing')

The easing function to use for the animation.

<a name='Tizen.UI.Components.Animations.UIAnimation.UIAnimation(System.Action_float_,float,float,Tizen.UI.Components.Animations.Easing,System.Action).finished'></a>

`finished` [System.Action](https://docs.microsoft.com/en-us/dotnet/api/System.Action 'System.Action')

The callback to invoke when the animation is finished.
### Methods

<a name='Tizen.UI.Components.Animations.UIAnimation.Abort(Tizen.UI.View,string)'></a>

## UIAnimation.Abort(View, string) Method

Aborts the UIAnimation of the specified view with the specified parameters.

```csharp
public void Abort(Tizen.UI.View owner, string name);
```
#### Parameters

<a name='Tizen.UI.Components.Animations.UIAnimation.Abort(Tizen.UI.View,string).owner'></a>

`owner` Tizen.UI.View

The view to abort the animation.

<a name='Tizen.UI.Components.Animations.UIAnimation.Abort(Tizen.UI.View,string).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the animated property.

<a name='Tizen.UI.Components.Animations.UIAnimation.Add(float,float,Tizen.UI.Components.Animations.UIAnimation)'></a>

## UIAnimation.Add(float, float, UIAnimation) Method

Adds a sub-animation to the UIAnimation with the specified range.

```csharp
public void Add(float beginAt, float finishAt, Tizen.UI.Components.Animations.UIAnimation animation);
```
#### Parameters

<a name='Tizen.UI.Components.Animations.UIAnimation.Add(float,float,Tizen.UI.Components.Animations.UIAnimation).beginAt'></a>

`beginAt` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The beginning progress value of the sub-animation.

<a name='Tizen.UI.Components.Animations.UIAnimation.Add(float,float,Tizen.UI.Components.Animations.UIAnimation).finishAt'></a>

`finishAt` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The ending progress value of the sub-animation.

<a name='Tizen.UI.Components.Animations.UIAnimation.Add(float,float,Tizen.UI.Components.Animations.UIAnimation).animation'></a>

`animation` [UIAnimation](Tizen.UI.Components.Animations.UIAnimation.md 'Tizen.UI.Components.Animations.UIAnimation')

The sub-animation to add.

<a name='Tizen.UI.Components.Animations.UIAnimation.Commit(Tizen.UI.View,string,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_)'></a>

## UIAnimation.Commit(View, string, uint, uint, Easing, Action&lt;float,bool>, Func&lt;bool>) Method

Commits the UIAnimation to the specified view with the specified parameters.

```csharp
public void Commit(Tizen.UI.View owner, string name, uint rate=16u, uint length=250u, Tizen.UI.Components.Animations.Easing easing=null, System.Action&lt;float,bool> finished=null, System.Func&lt;bool> repeat=null);
```
#### Parameters

<a name='Tizen.UI.Components.Animations.UIAnimation.Commit(Tizen.UI.View,string,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).owner'></a>

`owner` Tizen.UI.View

The view to commit the animation to.

<a name='Tizen.UI.Components.Animations.UIAnimation.Commit(Tizen.UI.View,string,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the property to animate.

<a name='Tizen.UI.Components.Animations.UIAnimation.Commit(Tizen.UI.View,string,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).rate'></a>

`rate` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The rate of the animation in milliseconds.

<a name='Tizen.UI.Components.Animations.UIAnimation.Commit(Tizen.UI.View,string,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).length'></a>

`length` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The length of the animation in milliseconds.

<a name='Tizen.UI.Components.Animations.UIAnimation.Commit(Tizen.UI.View,string,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).easing'></a>

`easing` [Easing](Tizen.UI.Components.Animations.Easing.md 'Tizen.UI.Components.Animations.Easing')

The easing function to use for the animation.

<a name='Tizen.UI.Components.Animations.UIAnimation.Commit(Tizen.UI.View,string,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).finished'></a>

`finished` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

The callback to invoke when the animation is finished.

<a name='Tizen.UI.Components.Animations.UIAnimation.Commit(Tizen.UI.View,string,uint,uint,Tizen.UI.Components.Animations.Easing,System.Action_float,bool_,System.Func_bool_).repeat'></a>

`repeat` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')

The callback to invoke to determine if the animation should repeat.

<a name='Tizen.UI.Components.Animations.UIAnimation.GetCallback()'></a>

## UIAnimation.GetCallback() Method

Gets the callback for the UIAnimation.

```csharp
public System.Action&lt;float> GetCallback();
```

#### Returns
[System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')  
The callback for the UIAnimation.

<a name='Tizen.UI.Components.Animations.UIAnimation.GetEnumerator()'></a>

## UIAnimation.GetEnumerator() Method

Returns an enumerator that iterates through the sub-animations of the UIAnimation.

```csharp
public System.Collections.IEnumerator GetEnumerator();
```

Implements [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable.GetEnumerator 'System.Collections.IEnumerable.GetEnumerator')

#### Returns
[System.Collections.IEnumerator](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerator 'System.Collections.IEnumerator')  
The enumerator that iterates through the sub-animations.

<a name='Tizen.UI.Components.Animations.UIAnimation.Insert(float,float,Tizen.UI.Components.Animations.UIAnimation)'></a>

## UIAnimation.Insert(float, float, UIAnimation) Method

Inserts a sub-animation into the UIAnimation with the specified range.

```csharp
public Tizen.UI.Components.Animations.UIAnimation Insert(float beginAt, float finishAt, Tizen.UI.Components.Animations.UIAnimation animation);
```
#### Parameters

<a name='Tizen.UI.Components.Animations.UIAnimation.Insert(float,float,Tizen.UI.Components.Animations.UIAnimation).beginAt'></a>

`beginAt` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The beginning progress value of the sub-animation.

<a name='Tizen.UI.Components.Animations.UIAnimation.Insert(float,float,Tizen.UI.Components.Animations.UIAnimation).finishAt'></a>

`finishAt` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The ending progress value of the sub-animation.

<a name='Tizen.UI.Components.Animations.UIAnimation.Insert(float,float,Tizen.UI.Components.Animations.UIAnimation).animation'></a>

`animation` [UIAnimation](Tizen.UI.Components.Animations.UIAnimation.md 'Tizen.UI.Components.Animations.UIAnimation')

The sub-animation to insert.

#### Returns
[UIAnimation](Tizen.UI.Components.Animations.UIAnimation.md 'Tizen.UI.Components.Animations.UIAnimation')  
The UIAnimation object for method chaining.

<a name='Tizen.UI.Components.Animations.UIAnimation.WithConcurrent(System.Action_float_,float,float,Tizen.UI.Components.Animations.Easing,float,float)'></a>

## UIAnimation.WithConcurrent(Action&lt;float>, float, float, Easing, float, float) Method

Adds a concurrent sub-animation to the UIAnimation with the specified parameters.

```csharp
public Tizen.UI.Components.Animations.UIAnimation WithConcurrent(System.Action&lt;float> callback, float start=0f, float end=1f, Tizen.UI.Components.Animations.Easing easing=null, float beginAt=0f, float finishAt=1f);
```
#### Parameters

<a name='Tizen.UI.Components.Animations.UIAnimation.WithConcurrent(System.Action_float_,float,float,Tizen.UI.Components.Animations.Easing,float,float).callback'></a>

`callback` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')

The callback to invoke during the sub-animation.

<a name='Tizen.UI.Components.Animations.UIAnimation.WithConcurrent(System.Action_float_,float,float,Tizen.UI.Components.Animations.Easing,float,float).start'></a>

`start` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The start value of the sub-animation.

<a name='Tizen.UI.Components.Animations.UIAnimation.WithConcurrent(System.Action_float_,float,float,Tizen.UI.Components.Animations.Easing,float,float).end'></a>

`end` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The end value of the sub-animation.

<a name='Tizen.UI.Components.Animations.UIAnimation.WithConcurrent(System.Action_float_,float,float,Tizen.UI.Components.Animations.Easing,float,float).easing'></a>

`easing` [Easing](Tizen.UI.Components.Animations.Easing.md 'Tizen.UI.Components.Animations.Easing')

The easing function to use for the sub-animation.

<a name='Tizen.UI.Components.Animations.UIAnimation.WithConcurrent(System.Action_float_,float,float,Tizen.UI.Components.Animations.Easing,float,float).beginAt'></a>

`beginAt` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The beginning progress value of the sub-animation.

<a name='Tizen.UI.Components.Animations.UIAnimation.WithConcurrent(System.Action_float_,float,float,Tizen.UI.Components.Animations.Easing,float,float).finishAt'></a>

`finishAt` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The ending progress value of the sub-animation.

#### Returns
[UIAnimation](Tizen.UI.Components.Animations.UIAnimation.md 'Tizen.UI.Components.Animations.UIAnimation')  
The UIAnimation object for method chaining.

<a name='Tizen.UI.Components.Animations.UIAnimation.WithConcurrent(Tizen.UI.Components.Animations.UIAnimation,float,float)'></a>

## UIAnimation.WithConcurrent(UIAnimation, float, float) Method

Adds a concurrent sub-animation to the UIAnimation with the specified range.

```csharp
public Tizen.UI.Components.Animations.UIAnimation WithConcurrent(Tizen.UI.Components.Animations.UIAnimation animation, float beginAt=0f, float finishAt=1f);
```
#### Parameters

<a name='Tizen.UI.Components.Animations.UIAnimation.WithConcurrent(Tizen.UI.Components.Animations.UIAnimation,float,float).animation'></a>

`animation` [UIAnimation](Tizen.UI.Components.Animations.UIAnimation.md 'Tizen.UI.Components.Animations.UIAnimation')

The sub-animation to add.

<a name='Tizen.UI.Components.Animations.UIAnimation.WithConcurrent(Tizen.UI.Components.Animations.UIAnimation,float,float).beginAt'></a>

`beginAt` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The beginning progress value of the sub-animation.

<a name='Tizen.UI.Components.Animations.UIAnimation.WithConcurrent(Tizen.UI.Components.Animations.UIAnimation,float,float).finishAt'></a>

`finishAt` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The ending progress value of the sub-animation.

#### Returns
[UIAnimation](Tizen.UI.Components.Animations.UIAnimation.md 'Tizen.UI.Components.Animations.UIAnimation')  
The UIAnimation object for method chaining.


























































