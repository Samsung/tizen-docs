### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## ProgressCircle Class

A progress component that indicates a specific value from a continuous or discrete range of values in circular shape.

```csharp
public class ProgressCircle : Tizen.UI.Components.Progress
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; [Tizen.UI.Components.Progress](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.Progress 'Tizen.UI.Components.Progress') &#129106; ProgressCircle
### Constructors

<a name='Tizen.UI.Components.Material.ProgressCircle.ProgressCircle()'></a>

## ProgressCircle() Constructor

Constructs a new progress circle.

```csharp
public ProgressCircle();
```

<a name='Tizen.UI.Components.Material.ProgressCircle.ProgressCircle(float,float)'></a>

## ProgressCircle(float, float) Constructor

Constructs a new progress circle.

```csharp
public ProgressCircle(float minimumValue, float maximumValue);
```
#### Parameters

<a name='Tizen.UI.Components.Material.ProgressCircle.ProgressCircle(float,float).minimumValue'></a>

`minimumValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.ProgressCircle.ProgressCircle(float,float).maximumValue'></a>

`maximumValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.ProgressCircle.ProgressCircle(float,float,Tizen.UI.Components.Material.ProgressCircleVariables)'></a>

## ProgressCircle(float, float, ProgressCircleVariables) Constructor

Constructs a new progress circle.

```csharp
public ProgressCircle(float minimumValue, float maximumValue, Tizen.UI.Components.Material.ProgressCircleVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.ProgressCircle.ProgressCircle(float,float,Tizen.UI.Components.Material.ProgressCircleVariables).minimumValue'></a>

`minimumValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.ProgressCircle.ProgressCircle(float,float,Tizen.UI.Components.Material.ProgressCircleVariables).maximumValue'></a>

`maximumValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.ProgressCircle.ProgressCircle(float,float,Tizen.UI.Components.Material.ProgressCircleVariables).variables'></a>

`variables` [ProgressCircleVariables](Tizen.UI.Components.Material.ProgressCircleVariables.md 'Tizen.UI.Components.Material.ProgressCircleVariables')

<a name='Tizen.UI.Components.Material.ProgressCircle.ProgressCircle(Tizen.UI.Components.Material.ProgressCircleVariables)'></a>

## ProgressCircle(ProgressCircleVariables) Constructor

Constructs a new progress circle.

```csharp
public ProgressCircle(Tizen.UI.Components.Material.ProgressCircleVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.ProgressCircle.ProgressCircle(Tizen.UI.Components.Material.ProgressCircleVariables).variables'></a>

`variables` [ProgressCircleVariables](Tizen.UI.Components.Material.ProgressCircleVariables.md 'Tizen.UI.Components.Material.ProgressCircleVariables')
### Properties

<a name='Tizen.UI.Components.Material.ProgressCircle.TrackColor'></a>

## ProgressCircle.TrackColor Property

Gets or sets the track color.

```csharp
public Tizen.UI.Color TrackColor { get; set; }
```

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.Material.ProgressCircle.TrackThickness'></a>

## ProgressCircle.TrackThickness Property

Gets or sets the track thinkness.

```csharp
public float TrackThickness { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
If the value is less than 1 and greater than 0, it will be treat as percentage for the radius.

<a name='Tizen.UI.Components.Material.ProgressCircle.TrailColor'></a>

## ProgressCircle.TrailColor Property

Gets or sets the trail color.

```csharp
public Tizen.UI.Color TrailColor { get; set; }
```

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')













































