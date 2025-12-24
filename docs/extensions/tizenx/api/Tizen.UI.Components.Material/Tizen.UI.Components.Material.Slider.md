### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## Slider Class

A slider component that indicates a specific value from a continuous or discrete range of values in bar shape.  
It can be used to select a value by moving the trail along the track.

```csharp
public class Slider : Tizen.UI.Components.InteractiveProgress
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ContentView &#129106; Tizen.UI.Components.Pressable &#129106; Tizen.UI.Components.InteractiveProgress &#129106; Slider
### Constructors

<a name='Tizen.UI.Components.Material.Slider.Slider(float,float)'></a>

## Slider(float, float) Constructor

Constructs a new progress bar.

```csharp
public Slider(float minimumValue, float maximumValue);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Slider.Slider(float,float).minimumValue'></a>

`minimumValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.Slider.Slider(float,float).maximumValue'></a>

`maximumValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.Slider.Slider(float,float,Tizen.UI.Components.Material.SliderVariables)'></a>

## Slider(float, float, SliderVariables) Constructor

Constructs a new progress bar.

```csharp
public Slider(float minimumValue, float maximumValue, Tizen.UI.Components.Material.SliderVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Slider.Slider(float,float,Tizen.UI.Components.Material.SliderVariables).minimumValue'></a>

`minimumValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.Slider.Slider(float,float,Tizen.UI.Components.Material.SliderVariables).maximumValue'></a>

`maximumValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.Slider.Slider(float,float,Tizen.UI.Components.Material.SliderVariables).variables'></a>

`variables` [SliderVariables](Tizen.UI.Components.Material.SliderVariables.md 'Tizen.UI.Components.Material.SliderVariables')
### Properties

<a name='Tizen.UI.Components.Material.Slider.AccessibilityValueTextGenerator'></a>

## Slider.AccessibilityValueTextGenerator Property

Generate accessibility value text with given.

```csharp
public System.Func&lt;Tizen.UI.Components.Material.Slider,string> AccessibilityValueTextGenerator { get; set; }
```

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[Slider](Tizen.UI.Components.Material.Slider.md 'Tizen.UI.Components.Material.Slider')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

<a name='Tizen.UI.Components.Material.Slider.KeyStep'></a>

## Slider.KeyStep Property

The step size for keyboard navigation.

```csharp
public float KeyStep { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.Slider.Padding'></a>

## Slider.Padding Property

Gets or sets the padding of button.

```csharp
public Tizen.UI.Thickness Padding { get; set; }
```

#### Property Value
Tizen.UI.Thickness

<a name='Tizen.UI.Components.Material.Slider.TrackColor'></a>

## Slider.TrackColor Property

The color of the track.

```csharp
public Tizen.UI.Color TrackColor { get; set; }
```

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Components.Material.Slider.TrackThickness'></a>

## Slider.TrackThickness Property

The thickness of the track.

```csharp
public float TrackThickness { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.Slider.TrailColor'></a>

## Slider.TrailColor Property

The color of the trail.

```csharp
public Tizen.UI.Color TrailColor { get; set; }
```

#### Property Value
Tizen.UI.Color














































