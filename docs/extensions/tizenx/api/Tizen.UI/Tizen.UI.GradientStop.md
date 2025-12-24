### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## GradientStop Struct

The GradientStop structure represents a color and its position along the gradient line.

```csharp
public struct GradientStop
```
### Constructors

<a name='Tizen.UI.GradientStop.GradientStop(Tizen.UI.Color,float)'></a>

## GradientStop(Color, float) Constructor

Initializes a new instance of the GradientStop class with the specified color and offset.

```csharp
public GradientStop(Tizen.UI.Color color, float offset);
```
#### Parameters

<a name='Tizen.UI.GradientStop.GradientStop(Tizen.UI.Color,float).color'></a>

`color` [Color](Tizen.UI.Color.md 'Tizen.UI.Color')

The color of the gradient stop.

<a name='Tizen.UI.GradientStop.GradientStop(Tizen.UI.Color,float).offset'></a>

`offset` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The position of the gradient stop along the gradient line, ranging from 0 to 1.
### Properties

<a name='Tizen.UI.GradientStop.Color'></a>

## GradientStop.Color Property

Gets or sets the color of the gradient stop.

```csharp
public Tizen.UI.Color Color { get; set; }
```

#### Property Value
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')

<a name='Tizen.UI.GradientStop.Offset'></a>

## GradientStop.Offset Property

Gets or sets the position of the gradient stop along the gradient line, ranging from 0 to 1.

```csharp
public float Offset { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')






