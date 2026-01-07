### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## RecoilEffect Class

Recoil visaul feedback that makes view dimmed and scaled.

```csharp
public class RecoilEffect : Tizen.UI.Components.UIAttachable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [UIAttachable](Tizen.UI.Components.UIAttachable.md 'Tizen.UI.Components.UIAttachable') &#129106; RecoilEffect

### Remarks
It will make overlay dim to target view or to [GetTouchEffectTarget()](Tizen.UI.Components.ITouchEffectTarget.md#Tizen.UI.Components.ITouchEffectTarget.GetTouchEffectTarget() 'Tizen.UI.Components.ITouchEffectTarget.GetTouchEffectTarget()') if the target implemented it.  
You can change scaling target by implementing [GetTouchEffectSecondaryTarget()](Tizen.UI.Components.ITouchEffectTarget.md#Tizen.UI.Components.ITouchEffectTarget.GetTouchEffectSecondaryTarget() 'Tizen.UI.Components.ITouchEffectTarget.GetTouchEffectSecondaryTarget()') to target view.
### Constructors

<a name='Tizen.UI.Components.RecoilEffect.RecoilEffect()'></a>

## RecoilEffect() Constructor

Default constructor. Sets default values for the feedback.

```csharp
public RecoilEffect();
```
### Fields

<a name='Tizen.UI.Components.RecoilEffect.Basic'></a>

## RecoilEffect.Basic Field

Basic recoil feedback with default values. Use this if you don't need to customize the feedback.  
This follows the target view's corner shape.

```csharp
public static readonly RecoilEffect Basic;
```

#### Field Value
[RecoilEffect](Tizen.UI.Components.RecoilEffect.md 'Tizen.UI.Components.RecoilEffect')

<a name='Tizen.UI.Components.RecoilEffect.Circle'></a>

## RecoilEffect.Circle Field

Circular shape of recoil feedback with default values.

```csharp
public static readonly RecoilEffect Circle;
```

#### Field Value
[RecoilEffect](Tizen.UI.Components.RecoilEffect.md 'Tizen.UI.Components.RecoilEffect')

<a name='Tizen.UI.Components.RecoilEffect.List'></a>

## RecoilEffect.List Field

Recoil feedback for list items.

```csharp
public static readonly RecoilEffect List;
```

#### Field Value
[RecoilEffect](Tizen.UI.Components.RecoilEffect.md 'Tizen.UI.Components.RecoilEffect')
### Properties

<a name='Tizen.UI.Components.RecoilEffect.CornerRadius'></a>

## RecoilEffect.CornerRadius Property

The corner radius value for the overlay used when [InheritCornerRadius](Tizen.UI.Components.RecoilEffect.md#Tizen.UI.Components.RecoilEffect.InheritCornerRadius 'Tizen.UI.Components.RecoilEffect.InheritCornerRadius') is false.

```csharp
public Tizen.UI.CornerRadius CornerRadius { get; set; }
```

#### Property Value
Tizen.UI.CornerRadius

<a name='Tizen.UI.Components.RecoilEffect.InheritCornerRadius'></a>

## RecoilEffect.InheritCornerRadius Property

Determines whether the recoil overlay's corner radius should inherit the value from its target.  
The default is true.

```csharp
public bool InheritCornerRadius { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.RecoilEffect.OffsetFactorX'></a>

## RecoilEffect.OffsetFactorX Property

The offset length from the original length of the target box in x direction.  
The destination scale value will be calculated by adding this value to the original size of the target box.  
scale = (targetWidth + OffsetFactorX) / targetWidth * ScaleFactorX.

```csharp
public float OffsetFactorX { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.RecoilEffect.OverlayColor'></a>

## RecoilEffect.OverlayColor Property

```csharp
public Tizen.UI.Color OverlayColor { get; set; }
```

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Components.RecoilEffect.OverlayPadding'></a>

## RecoilEffect.OverlayPadding Property

The scale factor in vertical used when scaling overlay view.

```csharp
public Tizen.UI.Thickness OverlayPadding { get; set; }
```

#### Property Value
Tizen.UI.Thickness

<a name='Tizen.UI.Components.RecoilEffect.OverlayScaleFactorX'></a>

## RecoilEffect.OverlayScaleFactorX Property

The scale factor in horizontal used when scaling overlay view.

```csharp
public float OverlayScaleFactorX { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.RecoilEffect.OverlayScaleFactorY'></a>

## RecoilEffect.OverlayScaleFactorY Property

The scale factor in vertical used when scaling overlay view.

```csharp
public float OverlayScaleFactorY { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.RecoilEffect.ScaleFactorX'></a>

## RecoilEffect.ScaleFactorX Property

The scale factor used when calculating the destination scale value in x direction.  
scale = (targetWidth + Offset) / targetWidth * ScaleFactorX.

```csharp
public float ScaleFactorX { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.Components.RecoilEffect.OnAttached(Tizen.UI.View)'></a>

## RecoilEffect.OnAttached(View) Method

Called when this object is attached to the view.

```csharp
public override void OnAttached(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.Components.RecoilEffect.OnAttached(Tizen.UI.View).view'></a>

`view` Tizen.UI.View

<a name='Tizen.UI.Components.RecoilEffect.OnDetached(Tizen.UI.View)'></a>

## RecoilEffect.OnDetached(View) Method

Called when this object is detached from the view.

```csharp
public override void OnDetached(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.Components.RecoilEffect.OnDetached(Tizen.UI.View).view'></a>

`view` Tizen.UI.View



























































