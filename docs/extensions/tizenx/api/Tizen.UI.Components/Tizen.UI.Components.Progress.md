### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## Progress Class

A progress component that indicates a specific value from a continuous or discrete range of values.

```csharp
public class Progress : Tizen.UI.ContentView
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; Progress
### Constructors

<a name='Tizen.UI.Components.Progress.Progress(float,float)'></a>

## Progress(float, float) Constructor

Constructs a new progress.

```csharp
public Progress(float minimumValue, float maximumValue);
```
#### Parameters

<a name='Tizen.UI.Components.Progress.Progress(float,float).minimumValue'></a>

`minimumValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Progress.Progress(float,float).maximumValue'></a>

`maximumValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Properties

<a name='Tizen.UI.Components.Progress.IsDeterminate'></a>

## Progress.IsDeterminate Property

Indicates whether the progress bar shows determinate or indeterminate state. Default is true.

```csharp
public bool IsDeterminate { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Progress.Range'></a>

## Progress.Range Property

The range of values.

```csharp
public Tizen.UI.Components.ClosedRange&lt;float> Range { get; set; }
```

#### Property Value
[Tizen.UI.Components.ClosedRange&lt;](Tizen.UI.Components.ClosedRange_T_.md 'Tizen.UI.Components.ClosedRange&lt;T>')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[&gt;](Tizen.UI.Components.ClosedRange_T_.md 'Tizen.UI.Components.ClosedRange&lt;T>')

#### Exceptions

[System.ArgumentException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentException 'System.ArgumentException')  
Thrown when the maximum is less than or equal to the minimum.

### Remarks
The [Value](Tizen.UI.Components.Progress.md#Tizen.UI.Components.Progress.Value 'Tizen.UI.Components.Progress.Value') will be coerced to the range when the range changes.

<a name='Tizen.UI.Components.Progress.Value'></a>

## Progress.Value Property

The current value.

```csharp
public float Value { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
The [Value](Tizen.UI.Components.Progress.md#Tizen.UI.Components.Progress.Value 'Tizen.UI.Components.Progress.Value') will be coerced to the range.

<a name='Tizen.UI.Components.Progress.ValueStepCount'></a>

## Progress.ValueStepCount Property

The number of segments to divide the range into.

```csharp
public int ValueStepCount { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

### Remarks
If the value is less than equals to zero, the progress will be continuous. Otherwise, the progress will be discrete and the value will be snapped to the nearest step.
### Events

<a name='Tizen.UI.Components.Progress.ValueChanged'></a>

## Progress.ValueChanged Event

An event triggered when the value of the slider changes.

```csharp
public event EventHandler ValueChanged;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')


























































