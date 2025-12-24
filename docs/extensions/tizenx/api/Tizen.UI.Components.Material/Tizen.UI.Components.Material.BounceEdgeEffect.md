### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## BounceEdgeEffect Class

Bounce Edge effect.

```csharp
public class BounceEdgeEffect :
Tizen.UI.Components.IEdgeEffect
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; BounceEdgeEffect

Implements [Tizen.UI.Components.IEdgeEffect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IEdgeEffect 'Tizen.UI.Components.IEdgeEffect')
### Constructors

<a name='Tizen.UI.Components.Material.BounceEdgeEffect.BounceEdgeEffect(Tizen.UI.View)'></a>

## BounceEdgeEffect(View) Constructor

Bounce edge effect contructor.

```csharp
public BounceEdgeEffect(Tizen.UI.View parent);
```
#### Parameters

<a name='Tizen.UI.Components.Material.BounceEdgeEffect.BounceEdgeEffect(Tizen.UI.View).parent'></a>

`parent` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

the parent view of edge effect.

<a name='Tizen.UI.Components.Material.BounceEdgeEffect.BounceEdgeEffect(Tizen.UI.View,float)'></a>

## BounceEdgeEffect(View, float) Constructor

Bounce edge effect contructor.

```csharp
public BounceEdgeEffect(Tizen.UI.View parent, float maxDistance);
```
#### Parameters

<a name='Tizen.UI.Components.Material.BounceEdgeEffect.BounceEdgeEffect(Tizen.UI.View,float).parent'></a>

`parent` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The parent view of edge effect.

<a name='Tizen.UI.Components.Material.BounceEdgeEffect.BounceEdgeEffect(Tizen.UI.View,float).maxDistance'></a>

`maxDistance` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The max distance value.
### Properties

<a name='Tizen.UI.Components.Material.BounceEdgeEffect.EdgeDirection'></a>

## BounceEdgeEffect.EdgeDirection Property

The direction of edge. [EdgeDirection](Tizen.UI.Components.Material.BounceEdgeEffect.md#Tizen.UI.Components.Material.BounceEdgeEffect.EdgeDirection 'Tizen.UI.Components.Material.BounceEdgeEffect.EdgeDirection').

```csharp
public Tizen.UI.Components.EdgeDirection EdgeDirection { get; set; }
```

Implements [EdgeDirection](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IEdgeEffect.EdgeDirection 'Tizen.UI.Components.IEdgeEffect.EdgeDirection')

#### Property Value
[Tizen.UI.Components.EdgeDirection](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.EdgeDirection 'Tizen.UI.Components.EdgeDirection')

<a name='Tizen.UI.Components.Material.BounceEdgeEffect.MaxDistance'></a>

## BounceEdgeEffect.MaxDistance Property

The Maximum distance of touch pull over the parent view.

```csharp
public float MaxDistance { get; set; }
```

Implements [MaxDistance](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IEdgeEffect.MaxDistance 'Tizen.UI.Components.IEdgeEffect.MaxDistance')

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.BounceEdgeEffect.SourceView'></a>

## BounceEdgeEffect.SourceView Property

The source view who will reflect the edge effect.

```csharp
public Tizen.UI.View SourceView { get; set; }
```

Implements [SourceView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IEdgeEffect.SourceView 'Tizen.UI.Components.IEdgeEffect.SourceView')

#### Property Value
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

<a name='Tizen.UI.Components.Material.BounceEdgeEffect.State'></a>

## BounceEdgeEffect.State Property

The state of edge effect. [Tizen.UI.Components.EdgeState](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.EdgeState 'Tizen.UI.Components.EdgeState').

```csharp
public Tizen.UI.Components.EdgeState State { get; set; }
```

Implements [State](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IEdgeEffect.State 'Tizen.UI.Components.IEdgeEffect.State')

#### Property Value
[Tizen.UI.Components.EdgeState](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.EdgeState 'Tizen.UI.Components.EdgeState')
### Methods

<a name='Tizen.UI.Components.Material.BounceEdgeEffect.Finish()'></a>

## BounceEdgeEffect.Finish() Method

Finish edge effect immediately.

```csharp
public virtual void Finish();
```

Implements [Finish()](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IEdgeEffect.Finish 'Tizen.UI.Components.IEdgeEffect.Finish')

<a name='Tizen.UI.Components.Material.BounceEdgeEffect.OnAbsorb(float)'></a>

## BounceEdgeEffect.OnAbsorb(float) Method

Call when the effect absorbs an impact at the given velocity.

```csharp
public virtual void OnAbsorb(float velocity);
```
#### Parameters

<a name='Tizen.UI.Components.Material.BounceEdgeEffect.OnAbsorb(float).velocity'></a>

`velocity` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The velocity to absorb.

Implements [OnAbsorb(float)](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IEdgeEffect.OnAbsorb#Tizen_UI_Components_IEdgeEffect_OnAbsorb_System_Single_ 'Tizen.UI.Components.IEdgeEffect.OnAbsorb(System.Single)')

<a name='Tizen.UI.Components.Material.BounceEdgeEffect.OnPull(float,float)'></a>

## BounceEdgeEffect.OnPull(float, float) Method

A view should call this when content is pulled over form the edge.

```csharp
public virtual float OnPull(float deltaDistance, float displacement=0.5f);
```
#### Parameters

<a name='Tizen.UI.Components.Material.BounceEdgeEffect.OnPull(float,float).deltaDistance'></a>

`deltaDistance` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

Change in distance since the last call. Values may be 0 to 1.f or negative values.

<a name='Tizen.UI.Components.Material.BounceEdgeEffect.OnPull(float,float).displacement'></a>

`displacement` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The displacement from the side of the point initiating the pull. value may be from 0 to 1.

Implements [OnPull(float, float)](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IEdgeEffect.OnPull#Tizen_UI_Components_IEdgeEffect_OnPull_System_Single,System_Single_ 'Tizen.UI.Components.IEdgeEffect.OnPull(System.Single,System.Single)')

#### Returns
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')  
The amount of deltaDistance that was consumed.

<a name='Tizen.UI.Components.Material.BounceEdgeEffect.OnRelease()'></a>

## BounceEdgeEffect.OnRelease() Method

Call when the object is released after being pulled.

```csharp
public virtual void OnRelease();
```

Implements [OnRelease()](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IEdgeEffect.OnRelease 'Tizen.UI.Components.IEdgeEffect.OnRelease')













































