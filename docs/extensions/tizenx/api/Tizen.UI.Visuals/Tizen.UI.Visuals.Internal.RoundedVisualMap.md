### [Tizen.UI.Visuals.Internal](Tizen.UI.Visuals.Internal.md 'Tizen.UI.Visuals.Internal')

## RoundedVisualMap Class

RoundedVisualMap is an abstract class that represents a map for visuals that can have a rounded shape.

```csharp
public abstract class RoundedVisualMap : Tizen.UI.Visuals.Internal.VisualMap
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [VisualMap](Tizen.UI.Visuals.Internal.VisualMap.md 'Tizen.UI.Visuals.Internal.VisualMap') &#129106; RoundedVisualMap

Derived  
&#8627; [ColorVisualMap](Tizen.UI.Visuals.Internal.ColorVisualMap.md 'Tizen.UI.Visuals.Internal.ColorVisualMap')  
&#8627; [ImageVisualMap](Tizen.UI.Visuals.Internal.ImageVisualMap.md 'Tizen.UI.Visuals.Internal.ImageVisualMap')
### Properties

<a name='Tizen.UI.Visuals.Internal.RoundedVisualMap.BorderlineColor'></a>

## RoundedVisualMap.BorderlineColor Property

Gets or sets the borderline color of the visual object.

```csharp
public Tizen.UI.Color BorderlineColor { get; set; }
```

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Visuals.Internal.RoundedVisualMap.BorderlineOffset'></a>

## RoundedVisualMap.BorderlineOffset Property

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

<a name='Tizen.UI.Visuals.Internal.RoundedVisualMap.BorderlineWidth'></a>

## RoundedVisualMap.BorderlineWidth Property

Gets or sets the borderline width of the visual object.

```csharp
public float BorderlineWidth { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Visuals.Internal.RoundedVisualMap.CornerRadius'></a>

## RoundedVisualMap.CornerRadius Property

Gets or sets the corner radius of the visual object.

```csharp
public Tizen.UI.CornerRadius CornerRadius { get; set; }
```

#### Property Value
[Tizen.UI.CornerRadius](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.CornerRadius 'Tizen.UI.CornerRadius')

























