### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## InteractiveProgress Class

A interactive progress component that indicates a specific value from a continuous or discrete range of values.

```csharp
public class InteractiveProgress : Tizen.UI.Components.Pressable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ContentView &#129106; [Pressable](Tizen.UI.Components.Pressable.md 'Tizen.UI.Components.Pressable') &#129106; InteractiveProgress
### Constructors

<a name='Tizen.UI.Components.InteractiveProgress.InteractiveProgress(float,float)'></a>

## InteractiveProgress(float, float) Constructor

Constructs a new interactive progress.

```csharp
public InteractiveProgress(float minimumValue, float maximumValue);
```
#### Parameters

<a name='Tizen.UI.Components.InteractiveProgress.InteractiveProgress(float,float).minimumValue'></a>

`minimumValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.InteractiveProgress.InteractiveProgress(float,float).maximumValue'></a>

`maximumValue` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Properties

<a name='Tizen.UI.Components.InteractiveProgress.IgnoreTap'></a>

## InteractiveProgress.IgnoreTap Property

Whether to ignore tap or not. Default is false.  
If true, the tap will not change the value.

```csharp
public bool IgnoreTap { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.InteractiveProgress.IgnoreTouchDown'></a>

## InteractiveProgress.IgnoreTouchDown Property

Whether to ignore touch down or not for selecting a value. Default is true.  
If false, the touch down will change the value immediately using the touch down position.

```csharp
public bool IgnoreTouchDown { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.InteractiveProgress.Range'></a>

## InteractiveProgress.Range Property

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
The [Value](Tizen.UI.Components.InteractiveProgress.md#Tizen.UI.Components.InteractiveProgress.Value 'Tizen.UI.Components.InteractiveProgress.Value') will be coerced to the range when the range changes.

<a name='Tizen.UI.Components.InteractiveProgress.UseRelativeTouchPoint'></a>

## InteractiveProgress.UseRelativeTouchPoint Property

Whether to use relative touch point. Default is false.  
If true, the value will be calculated based on the diff value between the last touch point and the current touch point.

```csharp
public bool UseRelativeTouchPoint { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.InteractiveProgress.Value'></a>

## InteractiveProgress.Value Property

The current value.

```csharp
public float Value { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
The [Value](Tizen.UI.Components.InteractiveProgress.md#Tizen.UI.Components.InteractiveProgress.Value 'Tizen.UI.Components.InteractiveProgress.Value') will be coerced to the range.

<a name='Tizen.UI.Components.InteractiveProgress.ValueChanging'></a>

## InteractiveProgress.ValueChanging Property

Whether the vale is changing due to user interactions such as dragging.

```csharp
public bool ValueChanging { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.InteractiveProgress.ValueStepCount'></a>

## InteractiveProgress.ValueStepCount Property

The number of segments to divide the range into.

```csharp
public int ValueStepCount { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

### Remarks
If the value is less than equals to zero, the progress will be continuous. Otherwise, the progress will be discrete and the value will be snapped to the nearest step.
### Methods

<a name='Tizen.UI.Components.InteractiveProgress.GetValueInStep(int)'></a>

## InteractiveProgress.GetValueInStep(int) Method

Calculate the value with step index.

```csharp
public float GetValueInStep(int stepIndex);
```
#### Parameters

<a name='Tizen.UI.Components.InteractiveProgress.GetValueInStep(int).stepIndex'></a>

`stepIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

#### Returns
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Events

<a name='Tizen.UI.Components.InteractiveProgress.ValueChanged'></a>

## InteractiveProgress.ValueChanged Event

An event triggered when the value of the slider changes.

```csharp
public event EventHandler&lt;InputEventArgs> ValueChanged;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[InputEventArgs](Tizen.UI.Components.InputEventArgs.md 'Tizen.UI.Components.InputEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.InteractiveProgress.ValueChangeFinished'></a>

## InteractiveProgress.ValueChangeFinished Event

An event triggered when the value of the slider stops changing by interactions such as dragging.

```csharp
public event EventHandler&lt;InputEventArgs> ValueChangeFinished;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[InputEventArgs](Tizen.UI.Components.InputEventArgs.md 'Tizen.UI.Components.InputEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.InteractiveProgress.ValueChangeStarted'></a>

## InteractiveProgress.ValueChangeStarted Event

An event triggered when the value of the slider starts to change due to user interactions such as dragging.

```csharp
public event EventHandler&lt;InputEventArgs> ValueChangeStarted;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[InputEventArgs](Tizen.UI.Components.InputEventArgs.md 'Tizen.UI.Components.InputEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')



























































