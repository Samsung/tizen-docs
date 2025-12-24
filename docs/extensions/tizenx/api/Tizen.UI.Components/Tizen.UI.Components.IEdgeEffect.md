### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## IEdgeEffect Interface

Edge effect for over scroll in scrollable view.  
when the scrollable view reach the end edge of scroll,  
pulling over the view process the Egde effect.

```csharp
public interface IEdgeEffect
```
### Properties

<a name='Tizen.UI.Components.IEdgeEffect.EdgeDirection'></a>

## IEdgeEffect.EdgeDirection Property

The direction of edge. [EdgeDirection](Tizen.UI.Components.IEdgeEffect.md#Tizen.UI.Components.IEdgeEffect.EdgeDirection 'Tizen.UI.Components.IEdgeEffect.EdgeDirection').

```csharp
Tizen.UI.Components.EdgeDirection EdgeDirection { get; set; }
```

#### Property Value
[EdgeDirection](Tizen.UI.Components.EdgeDirection.md 'Tizen.UI.Components.EdgeDirection')

<a name='Tizen.UI.Components.IEdgeEffect.MaxDistance'></a>

## IEdgeEffect.MaxDistance Property

The Maximum distance of touch pull over the parent view.

```csharp
float MaxDistance { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.IEdgeEffect.SourceView'></a>

## IEdgeEffect.SourceView Property

The source view who will reflect the edge effect.

```csharp
Tizen.UI.View SourceView { get; set; }
```

#### Property Value
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

<a name='Tizen.UI.Components.IEdgeEffect.State'></a>

## IEdgeEffect.State Property

The state of edge effect. [EdgeState](Tizen.UI.Components.EdgeState.md 'Tizen.UI.Components.EdgeState').

```csharp
Tizen.UI.Components.EdgeState State { get; }
```

#### Property Value
[EdgeState](Tizen.UI.Components.EdgeState.md 'Tizen.UI.Components.EdgeState')
### Methods

<a name='Tizen.UI.Components.IEdgeEffect.Finish()'></a>

## IEdgeEffect.Finish() Method

Finish edge effect immediately.

```csharp
void Finish();
```

<a name='Tizen.UI.Components.IEdgeEffect.OnAbsorb(float)'></a>

## IEdgeEffect.OnAbsorb(float) Method

Call when the effect absorbs an impact at the given velocity.

```csharp
void OnAbsorb(float velocity);
```
#### Parameters

<a name='Tizen.UI.Components.IEdgeEffect.OnAbsorb(float).velocity'></a>

`velocity` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The velocity to absorb.

<a name='Tizen.UI.Components.IEdgeEffect.OnPull(float,float)'></a>

## IEdgeEffect.OnPull(float, float) Method

A view should call this when content is pulled over form the edge.

```csharp
float OnPull(float deltaDistance, float displacement=0.5f);
```
#### Parameters

<a name='Tizen.UI.Components.IEdgeEffect.OnPull(float,float).deltaDistance'></a>

`deltaDistance` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

Change in distance since the last call. Values may be 0 to 1.f or negative values.

<a name='Tizen.UI.Components.IEdgeEffect.OnPull(float,float).displacement'></a>

`displacement` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The displacement from the side of the point initiating the pull. value may be from 0 to 1.

#### Returns
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')  
The amount of deltaDistance that was consumed.

<a name='Tizen.UI.Components.IEdgeEffect.OnRelease()'></a>

## IEdgeEffect.OnRelease() Method

Call when the object is released after being pulled.

```csharp
void OnRelease();
```


























































