### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## GradientBackground Class

GradientBackground is a base class for visuals that have a gradient effect.

```csharp
public abstract class GradientBackground : Tizen.UI.Background
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Background](Tizen.UI.Background.md 'Tizen.UI.Background') &#129106; GradientBackground

Derived  
&#8627; [LinearGradientBackground](Tizen.UI.LinearGradientBackground.md 'Tizen.UI.LinearGradientBackground')  
&#8627; [RadialGradientBackground](Tizen.UI.RadialGradientBackground.md 'Tizen.UI.RadialGradientBackground')
### Properties

<a name='Tizen.UI.GradientBackground.GradientStops'></a>

## GradientBackground.GradientStops Property

Gets the list of gradient stops.

```csharp
public System.Collections.Generic.IList&lt;Tizen.UI.GradientStop> GradientStops { get; }
```

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[GradientStop](Tizen.UI.GradientStop.md 'Tizen.UI.GradientStop')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

<a name='Tizen.UI.GradientBackground.GradientVisualSpreadMethod'></a>

## GradientBackground.GradientVisualSpreadMethod Property

Gets or sets the spread method of the gradient.

```csharp
public System.Nullable&lt;Tizen.UI.GradientVisualSpreadMethod> GradientVisualSpreadMethod { get; set; }
```

#### Property Value
[System.Nullable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')[GradientVisualSpreadMethod](Tizen.UI.GradientVisualSpreadMethod.md 'Tizen.UI.GradientVisualSpreadMethod')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')
### Methods

<a name='Tizen.UI.GradientBackground.BuildPropertyMap(Tizen.UI.NativeHandle.PropertyMapHandle)'></a>

## GradientBackground.BuildPropertyMap(PropertyMapHandle) Method

Builds the property map for the visual element.

```csharp
public override void BuildPropertyMap(Tizen.UI.NativeHandle.PropertyMapHandle map);
```
#### Parameters

<a name='Tizen.UI.GradientBackground.BuildPropertyMap(Tizen.UI.NativeHandle.PropertyMapHandle).map'></a>

`map` [PropertyMapHandle](Tizen.UI.NativeHandle.PropertyMapHandle.md 'Tizen.UI.NativeHandle.PropertyMapHandle')

The property map handle.






