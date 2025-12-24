### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## ProgressBar Class

A progress component that indicates a specific value from a continuous or discrete range of values in bar shape.

```csharp
public class ProgressBar : Tizen.UI.Components.Progress
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; [Tizen.UI.Components.Progress](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.Progress 'Tizen.UI.Components.Progress') &#129106; ProgressBar
### Constructors

<a name='Tizen.UI.Components.Material.ProgressBar.ProgressBar()'></a>

## ProgressBar() Constructor

Constructs a new progress bar.

```csharp
public ProgressBar();
```

<a name='Tizen.UI.Components.Material.ProgressBar.ProgressBar(float,float)'></a>

## ProgressBar(float, float) Constructor

Constructs a new progress bar.

```csharp
public ProgressBar(float minimumValue, float maximumValue);
```
#### Parameters

<a name='Tizen.UI.Components.Material.ProgressBar.ProgressBar(float,float).minimumValue'></a>

`minimumValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.ProgressBar.ProgressBar(float,float).maximumValue'></a>

`maximumValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.ProgressBar.ProgressBar(float,float,Tizen.UI.Components.Material.ProgressBarVariables)'></a>

## ProgressBar(float, float, ProgressBarVariables) Constructor

Constructs a new progress bar.

```csharp
public ProgressBar(float minimumValue, float maximumValue, Tizen.UI.Components.Material.ProgressBarVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.ProgressBar.ProgressBar(float,float,Tizen.UI.Components.Material.ProgressBarVariables).minimumValue'></a>

`minimumValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.ProgressBar.ProgressBar(float,float,Tizen.UI.Components.Material.ProgressBarVariables).maximumValue'></a>

`maximumValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.ProgressBar.ProgressBar(float,float,Tizen.UI.Components.Material.ProgressBarVariables).variables'></a>

`variables` [ProgressBarVariables](Tizen.UI.Components.Material.ProgressBarVariables.md 'Tizen.UI.Components.Material.ProgressBarVariables')

<a name='Tizen.UI.Components.Material.ProgressBar.ProgressBar(Tizen.UI.Components.Material.ProgressBarVariables)'></a>

## ProgressBar(ProgressBarVariables) Constructor

Constructs a new progress bar.

```csharp
public ProgressBar(Tizen.UI.Components.Material.ProgressBarVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.ProgressBar.ProgressBar(Tizen.UI.Components.Material.ProgressBarVariables).variables'></a>

`variables` [ProgressBarVariables](Tizen.UI.Components.Material.ProgressBarVariables.md 'Tizen.UI.Components.Material.ProgressBarVariables')
### Properties

<a name='Tizen.UI.Components.Material.ProgressBar.DividerStepCount'></a>

## ProgressBar.DividerStepCount Property

The number of segments to divide the range into to show dividers between them.

```csharp
public int DividerStepCount { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

### Remarks
If the value is less than equals to one, the divider would not appears.

<a name='Tizen.UI.Components.Material.ProgressBar.IsReversed'></a>

## ProgressBar.IsReversed Property

Determines whether the trail sticks to the start or end of the progress bar.  
The default is false, which means the trail sticks to the start of the progress bar. Otherwise, it sticks to the end of the progress bar.

```csharp
public bool IsReversed { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.ProgressBar.TrackColor'></a>

## ProgressBar.TrackColor Property

The color of the track.

```csharp
public Tizen.UI.Color TrackColor { get; set; }
```

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.Material.ProgressBar.TrackThickness'></a>

## ProgressBar.TrackThickness Property

The thickness of the track.

```csharp
public float TrackThickness { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.ProgressBar.TrailColor'></a>

## ProgressBar.TrailColor Property

The color of the trail.

```csharp
public Tizen.UI.Color TrailColor { get; set; }
```

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')













































