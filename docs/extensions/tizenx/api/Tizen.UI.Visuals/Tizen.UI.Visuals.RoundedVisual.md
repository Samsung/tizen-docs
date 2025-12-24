### [Tizen.UI.Visuals](Tizen.UI.Visuals.md 'Tizen.UI.Visuals')

## RoundedVisual Class

RoundedVisual is a base class for visuals that can have a rounded shape.

```csharp
public abstract class RoundedVisual : Tizen.UI.Visuals.VisualObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; [VisualObject](Tizen.UI.Visuals.VisualObject.md 'Tizen.UI.Visuals.VisualObject') &#129106; RoundedVisual

Derived  
&#8627; [ColorVisual](Tizen.UI.Visuals.ColorVisual.md 'Tizen.UI.Visuals.ColorVisual')  
&#8627; [ImageVisual](Tizen.UI.Visuals.ImageVisual.md 'Tizen.UI.Visuals.ImageVisual')
### Properties

<a name='Tizen.UI.Visuals.RoundedVisual.BorderlineColor'></a>

## RoundedVisual.BorderlineColor Property

Gets or sets the borderline color of the visual object.

```csharp
public Tizen.UI.Color BorderlineColor { get; set; }
```

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Visuals.RoundedVisual.BorderlineOffset'></a>

## RoundedVisual.BorderlineOffset Property

Gets or sets the borderline offset of the visual object.

```csharp
public float BorderlineOffset { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
The borderline offset indicates how far the borderline is from the visual object's boundary.  
If the offset is 1, the borderline will be drawn outside the visual object's boundary.  
If the offset is 0, the borderline will be drawn across the visual object's boundary.  
If the offset is -1, the borderline will be drawn inside the visual object's boundary.

<a name='Tizen.UI.Visuals.RoundedVisual.BorderlineWidth'></a>

## RoundedVisual.BorderlineWidth Property

Gets or sets the borderline width of the visual object.

```csharp
public float BorderlineWidth { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Visuals.RoundedVisual.CornerRadius'></a>

## RoundedVisual.CornerRadius Property

Gets or sets the corner radius of the visual object.

```csharp
public Tizen.UI.CornerRadius CornerRadius { get; set; }
```

#### Property Value
Tizen.UI.CornerRadius


























