### [Tizen.UI.Visuals](Tizen.UI.Visuals.md 'Tizen.UI.Visuals')

## NPatchVisual Class

NPatchVisual is a class for the n-patch image visual.

```csharp
public class NPatchVisual : Tizen.UI.Visuals.ImageVisual
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; [VisualObject](Tizen.UI.Visuals.VisualObject.md 'Tizen.UI.Visuals.VisualObject') &#129106; [RoundedVisual](Tizen.UI.Visuals.RoundedVisual.md 'Tizen.UI.Visuals.RoundedVisual') &#129106; [ImageVisual](Tizen.UI.Visuals.ImageVisual.md 'Tizen.UI.Visuals.ImageVisual') &#129106; NPatchVisual
### Properties

<a name='Tizen.UI.Visuals.NPatchVisual.AuxiliaryImageAlpha'></a>

## NPatchVisual.AuxiliaryImageAlpha Property

The alpha value of the auxiliary image.

```csharp
public float AuxiliaryImageAlpha { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Visuals.NPatchVisual.AuxiliaryImageUrl'></a>

## NPatchVisual.AuxiliaryImageUrl Property

The auxiliary image URL of the NPatchVisual.

```csharp
public string AuxiliaryImageUrl { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

### Remarks
Overlays the auxiliary image on top of an NPatch image.  
The resulting visual image will be at least as large as the smallest possible n-patch or the auxiliary image, whichever is larger.

<a name='Tizen.UI.Visuals.NPatchVisual.Border'></a>

## NPatchVisual.Border Property

The border property of the NPatch image visual.

```csharp
public Tizen.UI.Thickness Border { get; set; }
```

#### Property Value
Tizen.UI.Thickness

<a name='Tizen.UI.Visuals.NPatchVisual.BorderOnly'></a>

## NPatchVisual.BorderOnly Property

The border only property of the NPatchVisual.

```csharp
public bool BorderOnly { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')


























