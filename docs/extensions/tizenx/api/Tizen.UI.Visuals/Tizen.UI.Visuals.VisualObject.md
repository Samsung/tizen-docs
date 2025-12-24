### [Tizen.UI.Visuals](Tizen.UI.Visuals.md 'Tizen.UI.Visuals')

## VisualObject Class

VisualObject is the base class for all visuals.

```csharp
public abstract class VisualObject : Tizen.UI.NObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; VisualObject

Derived  
&#8627; [RoundedVisual](Tizen.UI.Visuals.RoundedVisual.md 'Tizen.UI.Visuals.RoundedVisual')  
&#8627; [TextVisual](Tizen.UI.Visuals.TextVisual.md 'Tizen.UI.Visuals.TextVisual')
### Properties

<a name='Tizen.UI.Visuals.VisualObject.Color'></a>

## VisualObject.Color Property

Gets or sets the color of the visual object.

```csharp
public Tizen.UI.Color Color { get; set; }
```

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Visuals.VisualObject.Height'></a>

## VisualObject.Height Property

Gets or sets the height of the visual object.

```csharp
public float Height { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Visuals.VisualObject.ModifyHeight'></a>

## VisualObject.ModifyHeight Property

Modifies the height of the visual object.

```csharp
public float ModifyHeight { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
as pixel value, adjusted by adding or subtracting from the specified height

<a name='Tizen.UI.Visuals.VisualObject.ModifyWidth'></a>

## VisualObject.ModifyWidth Property

Modifies the width of the visual object.

```csharp
public float ModifyWidth { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
as pixel value, adjusted by adding or subtracting from the specified width

<a name='Tizen.UI.Visuals.VisualObject.Opacity'></a>

## VisualObject.Opacity Property

Gets or sets the opacity of the visual object.

```csharp
public float Opacity { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Visuals.VisualObject.Origin'></a>

## VisualObject.Origin Property

Gets or sets the origin of the visual object.

```csharp
public Tizen.UI.Visuals.VisualAlign Origin { get; set; }
```

#### Property Value
[VisualAlign](Tizen.UI.Visuals.VisualAlign.md 'Tizen.UI.Visuals.VisualAlign')

### Remarks
The origin indicates the position of the visual object in the view.

<a name='Tizen.UI.Visuals.VisualObject.SiblingOrder'></a>

## VisualObject.SiblingOrder Property

Sibling order of this VisualBase.

```csharp
public int SiblingOrder { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

### Remarks
The sibling order is used to determine the draw order of the visuals.  
The visuals with smaller sibling order are drawn bottom,  
and the visuals with larger sibling order are drawn top.  
  
It will be changed automatically when the visuals are added to the view.  
before attached the view it is 0

<a name='Tizen.UI.Visuals.VisualObject.TransformFlags'></a>

## VisualObject.TransformFlags Property

Gets or sets the transform flags of the visual object.

```csharp
public Tizen.UI.Visuals.TransformFlags TransformFlags { get; set; }
```

#### Property Value
[TransformFlags](Tizen.UI.Visuals.TransformFlags.md 'Tizen.UI.Visuals.TransformFlags')

### Remarks
The transform flags indicate whether the position and size of the visual object are relative values or absolute pixel values.

<a name='Tizen.UI.Visuals.VisualObject.Width'></a>

## VisualObject.Width Property

Gets or sets the width of the visual object.

```csharp
public float Width { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Visuals.VisualObject.X'></a>

## VisualObject.X Property

Gets or sets the x position of the visual object.

```csharp
public float X { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Visuals.VisualObject.Y'></a>

## VisualObject.Y Property

Gets or sets the Y position of the visual object.

```csharp
public float Y { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')


























