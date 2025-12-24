### [Tizen.UI.Visuals.Internal](Tizen.UI.Visuals.Internal.md 'Tizen.UI.Visuals.Internal')

## NPatchVisualMap Class

The NPatchVisualMap is a class for setting the properties of the NPatchVisual.

```csharp
public class NPatchVisualMap : Tizen.UI.Visuals.Internal.ImageVisualMap
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [VisualMap](Tizen.UI.Visuals.Internal.VisualMap.md 'Tizen.UI.Visuals.Internal.VisualMap') &#129106; [RoundedVisualMap](Tizen.UI.Visuals.Internal.RoundedVisualMap.md 'Tizen.UI.Visuals.Internal.RoundedVisualMap') &#129106; [ImageVisualMap](Tizen.UI.Visuals.Internal.ImageVisualMap.md 'Tizen.UI.Visuals.Internal.ImageVisualMap') &#129106; NPatchVisualMap
### Constructors

<a name='Tizen.UI.Visuals.Internal.NPatchVisualMap.NPatchVisualMap()'></a>

## NPatchVisualMap() Constructor

Constructor to instantiate the NPatchVisualMap class.

```csharp
public NPatchVisualMap();
```
### Properties

<a name='Tizen.UI.Visuals.Internal.NPatchVisualMap.AuxiliaryImageAlpha'></a>

## NPatchVisualMap.AuxiliaryImageAlpha Property

The alpha value of the auxiliary image.

```csharp
public float AuxiliaryImageAlpha { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Visuals.Internal.NPatchVisualMap.AuxiliaryImageUrl'></a>

## NPatchVisualMap.AuxiliaryImageUrl Property

The auxiliary image URL of the NPatchVisual.

```csharp
public string AuxiliaryImageUrl { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

### Remarks
Overlays the auxiliary image on top of an NPatch image.  
The resulting visual image will be at least as large as the smallest possible n-patch or the auxiliary image, whichever is larger.

<a name='Tizen.UI.Visuals.Internal.NPatchVisualMap.Border'></a>

## NPatchVisualMap.Border Property

The border property of the NPatch image visual.

```csharp
public Tizen.UI.Thickness Border { get; set; }
```

#### Property Value
[Tizen.UI.Thickness](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Thickness 'Tizen.UI.Thickness')

<a name='Tizen.UI.Visuals.Internal.NPatchVisualMap.BorderOnly'></a>

## NPatchVisualMap.BorderOnly Property

The border only property of the NPatchVisual.

```csharp
public bool BorderOnly { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

























