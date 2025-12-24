### [Tizen.UI.Visuals.Internal](Tizen.UI.Visuals.Internal.md 'Tizen.UI.Visuals.Internal')

## VisualMap Class

The VisualMap class is an abstract class that provides a set of properties for visual objects.

```csharp
public abstract class VisualMap :
System.IDisposable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; VisualMap

Derived  
&#8627; [RoundedVisualMap](Tizen.UI.Visuals.Internal.RoundedVisualMap.md 'Tizen.UI.Visuals.Internal.RoundedVisualMap')  
&#8627; [TextVisualMap](Tizen.UI.Visuals.Internal.TextVisualMap.md 'Tizen.UI.Visuals.Internal.TextVisualMap')

Implements [System.IDisposable](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable 'System.IDisposable')
### Properties

<a name='Tizen.UI.Visuals.Internal.VisualMap.Color'></a>

## VisualMap.Color Property

Gets or sets the color of the visual object.

```csharp
public Tizen.UI.Color Color { get; set; }
```

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Visuals.Internal.VisualMap.Handle'></a>

## VisualMap.Handle Property

Gets the PropertyMap handle for visual

```csharp
public Tizen.UI.NativeHandle.PropertyMapHandle Handle { get; set; }
```

#### Property Value
[Tizen.UI.NativeHandle.PropertyMapHandle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NativeHandle.PropertyMapHandle 'Tizen.UI.NativeHandle.PropertyMapHandle')

<a name='Tizen.UI.Visuals.Internal.VisualMap.Height'></a>

## VisualMap.Height Property

Gets or sets the height of the visual object.

```csharp
public float Height { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Visuals.Internal.VisualMap.ModifyHeight'></a>

## VisualMap.ModifyHeight Property

Modifies the height of the visual object.

```csharp
public float ModifyHeight { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
as pixel value, adjusted by adding or subtracting from the specified height

<a name='Tizen.UI.Visuals.Internal.VisualMap.ModifyWidth'></a>

## VisualMap.ModifyWidth Property

Modifies the width of the visual object.

```csharp
public float ModifyWidth { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
as pixel value, adjusted by adding or subtracting from the specified width

<a name='Tizen.UI.Visuals.Internal.VisualMap.Opacity'></a>

## VisualMap.Opacity Property

Gets or sets the opacity of the visual object.

```csharp
public float Opacity { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Visuals.Internal.VisualMap.Origin'></a>

## VisualMap.Origin Property

Gets or sets the origin of the visual object.

```csharp
public Tizen.UI.Visuals.VisualAlign Origin { get; set; }
```

#### Property Value
[VisualAlign](Tizen.UI.Visuals.VisualAlign.md 'Tizen.UI.Visuals.VisualAlign')

### Remarks
The origin indicates the position of the visual object in the view.

<a name='Tizen.UI.Visuals.Internal.VisualMap.TransformFlags'></a>

## VisualMap.TransformFlags Property

Gets or sets the transform flags of the visual object.

```csharp
public Tizen.UI.Visuals.TransformFlags TransformFlags { get; set; }
```

#### Property Value
[TransformFlags](Tizen.UI.Visuals.TransformFlags.md 'Tizen.UI.Visuals.TransformFlags')

### Remarks
The transform flags indicate whether the position and size of the visual object are relative values or absolute pixel values.

<a name='Tizen.UI.Visuals.Internal.VisualMap.Width'></a>

## VisualMap.Width Property

Gets or sets the width of the visual object.

```csharp
public float Width { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Visuals.Internal.VisualMap.X'></a>

## VisualMap.X Property

Gets or sets the x position of the visual object.

```csharp
public float X { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Visuals.Internal.VisualMap.Y'></a>

## VisualMap.Y Property

Gets or sets the Y position of the visual object.

```csharp
public float Y { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.Visuals.Internal.VisualMap.SetDirty()'></a>

## VisualMap.SetDirty() Method

Sets the map as dirty.

```csharp
public void SetDirty();
```

<a name='Tizen.UI.Visuals.Internal.VisualMap.UpdateTransformMap()'></a>

## VisualMap.UpdateTransformMap() Method

Updates the transform map of the visual object.

```csharp
public void UpdateTransformMap();
```
### Events

<a name='Tizen.UI.Visuals.Internal.VisualMap.UpdateRequired'></a>

## VisualMap.UpdateRequired Event

Occurs when the update is required.

```csharp
public event EventHandler UpdateRequired;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

























