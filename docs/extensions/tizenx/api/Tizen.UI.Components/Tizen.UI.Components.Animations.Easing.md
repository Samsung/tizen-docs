### [Tizen.UI.Components.Animations](Tizen.UI.Components.Animations.md 'Tizen.UI.Components.Animations')

## Easing Class

Represents an easing function used for animations.

```csharp
public class Easing
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Easing

Derived  
&#8627; [Bezier](Tizen.UI.Components.Animations.Bezier.md 'Tizen.UI.Components.Animations.Bezier')
### Constructors

<a name='Tizen.UI.Components.Animations.Easing.Easing(System.Func_float,float_)'></a>

## Easing(Func&lt;float,float>) Constructor

Initializes a new instance of the Easing class with the specified easing function.

```csharp
public Easing(System.Func&lt;float,float> easingFunc);
```
#### Parameters

<a name='Tizen.UI.Components.Animations.Easing.Easing(System.Func_float,float_).easingFunc'></a>

`easingFunc` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

The easing function to use.
### Fields

<a name='Tizen.UI.Components.Animations.Easing.Bounce'></a>

## Easing.Bounce Field

Represents an easing function that creates a bouncing effect.

```csharp
public static readonly Easing Bounce;
```

#### Field Value
[Easing](Tizen.UI.Components.Animations.Easing.md 'Tizen.UI.Components.Animations.Easing')

<a name='Tizen.UI.Components.Animations.Easing.EaseIn'></a>

## Easing.EaseIn Field

Represents an easing function that eases in using a cubic curve.

```csharp
public static readonly Easing EaseIn;
```

#### Field Value
[Easing](Tizen.UI.Components.Animations.Easing.md 'Tizen.UI.Components.Animations.Easing')

<a name='Tizen.UI.Components.Animations.Easing.EaseInOut'></a>

## Easing.EaseInOut Field

Represents an easing function that eases in and out using a cubic curve.

```csharp
public static readonly Easing EaseInOut;
```

#### Field Value
[Easing](Tizen.UI.Components.Animations.Easing.md 'Tizen.UI.Components.Animations.Easing')

<a name='Tizen.UI.Components.Animations.Easing.EaseInOutSine'></a>

## Easing.EaseInOutSine Field

Represents an easing function that eases in and out using a sine curve.

```csharp
public static readonly Easing EaseInOutSine;
```

#### Field Value
[Easing](Tizen.UI.Components.Animations.Easing.md 'Tizen.UI.Components.Animations.Easing')

<a name='Tizen.UI.Components.Animations.Easing.EaseInSine'></a>

## Easing.EaseInSine Field

Represents an easing function that eases in using a sine curve.

```csharp
public static readonly Easing EaseInSine;
```

#### Field Value
[Easing](Tizen.UI.Components.Animations.Easing.md 'Tizen.UI.Components.Animations.Easing')

<a name='Tizen.UI.Components.Animations.Easing.EaseInSquare'></a>

## Easing.EaseInSquare Field

Represents an easing function that eases in using a square curve.

```csharp
public static readonly Easing EaseInSquare;
```

#### Field Value
[Easing](Tizen.UI.Components.Animations.Easing.md 'Tizen.UI.Components.Animations.Easing')

<a name='Tizen.UI.Components.Animations.Easing.EaseOut'></a>

## Easing.EaseOut Field

Represents an easing function that eases out using a cubic curve.

```csharp
public static readonly Easing EaseOut;
```

#### Field Value
[Easing](Tizen.UI.Components.Animations.Easing.md 'Tizen.UI.Components.Animations.Easing')

<a name='Tizen.UI.Components.Animations.Easing.EaseOutBack'></a>

## Easing.EaseOutBack Field

Represents an easing function that eases out using a back curve.

```csharp
public static readonly Easing EaseOutBack;
```

#### Field Value
[Easing](Tizen.UI.Components.Animations.Easing.md 'Tizen.UI.Components.Animations.Easing')

<a name='Tizen.UI.Components.Animations.Easing.EaseOutSine'></a>

## Easing.EaseOutSine Field

Represents an easing function that eases out using a sine curve.

```csharp
public static readonly Easing EaseOutSine;
```

#### Field Value
[Easing](Tizen.UI.Components.Animations.Easing.md 'Tizen.UI.Components.Animations.Easing')

<a name='Tizen.UI.Components.Animations.Easing.EaseOutSquare'></a>

## Easing.EaseOutSquare Field

Represents an easing function that eases out using a square curve.

```csharp
public static readonly Easing EaseOutSquare;
```

#### Field Value
[Easing](Tizen.UI.Components.Animations.Easing.md 'Tizen.UI.Components.Animations.Easing')

<a name='Tizen.UI.Components.Animations.Easing.Linear'></a>

## Easing.Linear Field

Represents a linear easing function.

```csharp
public static readonly Easing Linear;
```

#### Field Value
[Easing](Tizen.UI.Components.Animations.Easing.md 'Tizen.UI.Components.Animations.Easing')

<a name='Tizen.UI.Components.Animations.Easing.LinearReverse'></a>

## Easing.LinearReverse Field

Represents a linear easing function that reverses the progress.

```csharp
public static readonly Easing LinearReverse;
```

#### Field Value
[Easing](Tizen.UI.Components.Animations.Easing.md 'Tizen.UI.Components.Animations.Easing')

<a name='Tizen.UI.Components.Animations.Easing.Sin'></a>

## Easing.Sin Field

Represents an easing function that creates a sinusoidal motion.

```csharp
public static readonly Easing Sin;
```

#### Field Value
[Easing](Tizen.UI.Components.Animations.Easing.md 'Tizen.UI.Components.Animations.Easing')
### Methods

<a name='Tizen.UI.Components.Animations.Easing.Ease(float)'></a>

## Easing.Ease(float) Method

Applies the easing function to the specified value.

```csharp
public float Ease(float v);
```
#### Parameters

<a name='Tizen.UI.Components.Animations.Easing.Ease(float).v'></a>

`v` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The value to apply the easing function to.

#### Returns
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')  
The result of applying the easing function to the specified value.
### Operators

<a name='Tizen.UI.Components.Animations.Easing.op_ImplicitTizen.UI.Components.Animations.Easing(System.Func_float,float_)'></a>

## Easing.implicit operator Easing(Func&lt;float,float>) Operator

Implicitly converts a Func{float, float} to an Easing object.

```csharp
public static Tizen.UI.Components.Animations.Easing implicit operator Easing(System.Func&lt;float,float> func);
```
#### Parameters

<a name='Tizen.UI.Components.Animations.Easing.op_ImplicitTizen.UI.Components.Animations.Easing(System.Func_float,float_).func'></a>

`func` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

The Func{float, float} to convert.

#### Returns
[Easing](Tizen.UI.Components.Animations.Easing.md 'Tizen.UI.Components.Animations.Easing')  
The resulting Easing object.


























































