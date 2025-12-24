### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## ProgressTimer Class

A progress component that specific GUI that can indicate a time value.

```csharp
public class ProgressTimer : Tizen.UI.Components.TimeCounter
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; [Tizen.UI.Components.TimeCounter](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.TimeCounter 'Tizen.UI.Components.TimeCounter') &#129106; ProgressTimer
### Constructors

<a name='Tizen.UI.Components.Material.ProgressTimer.ProgressTimer()'></a>

## ProgressTimer() Constructor

Constructs a new timer progress.

```csharp
public ProgressTimer();
```

<a name='Tizen.UI.Components.Material.ProgressTimer.ProgressTimer(int)'></a>

## ProgressTimer(int) Constructor

Constructs a new timer progress.

```csharp
public ProgressTimer(int totalTimeInMilliseconds);
```
#### Parameters

<a name='Tizen.UI.Components.Material.ProgressTimer.ProgressTimer(int).totalTimeInMilliseconds'></a>

`totalTimeInMilliseconds` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.ProgressTimer.ProgressTimer(Tizen.UI.Components.Material.ProgressTimerVariables)'></a>

## ProgressTimer(ProgressTimerVariables) Constructor

Constructs a new timer progress.

```csharp
public ProgressTimer(Tizen.UI.Components.Material.ProgressTimerVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.ProgressTimer.ProgressTimer(Tizen.UI.Components.Material.ProgressTimerVariables).variables'></a>

`variables` [ProgressTimerVariables](Tizen.UI.Components.Material.ProgressTimerVariables.md 'Tizen.UI.Components.Material.ProgressTimerVariables')
### Properties

<a name='Tizen.UI.Components.Material.ProgressTimer.IsPaused'></a>

## ProgressTimer.IsPaused Property

Gets or sets whether the timer is paused state.

```csharp
public bool IsPaused { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.ProgressTimer.IsReversed'></a>

## ProgressTimer.IsReversed Property

Determines whether the trail represents elapsed time or remaining time.  
The default is false, which means the trail represents elapsed time.

```csharp
public bool IsReversed { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.ProgressTimer.TrackColor'></a>

## ProgressTimer.TrackColor Property

Gets or sets the track color.

```csharp
public Tizen.UI.Color TrackColor { get; set; }
```

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.Material.ProgressTimer.TrackThickness'></a>

## ProgressTimer.TrackThickness Property

Gets or sets the track thinkness.

```csharp
public float TrackThickness { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
If the value is less than 1 and greater than 0, it will be treat as percentage for the radius.

<a name='Tizen.UI.Components.Material.ProgressTimer.TrailColor'></a>

## ProgressTimer.TrailColor Property

Gets or sets the trail color.

```csharp
public Tizen.UI.Color TrailColor { get; set; }
```

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

### Remarks
Once this value is set, the predefined color changes for the warning and paused state will be ignored.
### Events

<a name='Tizen.UI.Components.Material.ProgressTimer.PausedChanged'></a>

## ProgressTimer.PausedChanged Event

Invoked when the warning state of the timer progress changes.

```csharp
public event EventHandler PausedChanged;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')













































