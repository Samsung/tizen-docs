### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## TimeCounter Class

A time counter component that indicates a specific time value.

```csharp
public class TimeCounter : Tizen.UI.ContentView
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; TimeCounter
### Constructors

<a name='Tizen.UI.Components.TimeCounter.TimeCounter()'></a>

## TimeCounter() Constructor

Constructs a new time counter.

```csharp
public TimeCounter();
```

<a name='Tizen.UI.Components.TimeCounter.TimeCounter(int)'></a>

## TimeCounter(int) Constructor

Constructs a new time counter.

```csharp
public TimeCounter(int totalTimeInMilliseconds);
```
#### Parameters

<a name='Tizen.UI.Components.TimeCounter.TimeCounter(int).totalTimeInMilliseconds'></a>

`totalTimeInMilliseconds` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')
### Properties

<a name='Tizen.UI.Components.TimeCounter.IsWarning'></a>

## TimeCounter.IsWarning Property

Gets whether the timer is warning state.

```csharp
public bool IsWarning { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.TimeCounter.RemainingTime'></a>

## TimeCounter.RemainingTime Property

The current value.

```csharp
public int RemainingTime { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

### Remarks
The [RemainingTime](Tizen.UI.Components.TimeCounter.md#Tizen.UI.Components.TimeCounter.RemainingTime 'Tizen.UI.Components.TimeCounter.RemainingTime') will be coerced to the range.

<a name='Tizen.UI.Components.TimeCounter.TotalTime'></a>

## TimeCounter.TotalTime Property

The range of values.

```csharp
public int TotalTime { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

#### Exceptions

[System.ArgumentException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentException 'System.ArgumentException')  
Thrown when the maximum is less than or equal to the minimum.

### Remarks
The [RemainingTime](Tizen.UI.Components.TimeCounter.md#Tizen.UI.Components.TimeCounter.RemainingTime 'Tizen.UI.Components.TimeCounter.RemainingTime') will be coerced to the range when the range changes.

<a name='Tizen.UI.Components.TimeCounter.WarningTime'></a>

## TimeCounter.WarningTime Property

The warning time in milliseconds.  
The timer get into the warning state when the remaining time is less than or equal to the warning time.

```csharp
public int WarningTime { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')
### Events

<a name='Tizen.UI.Components.TimeCounter.RemainingTimeChanged'></a>

## TimeCounter.RemainingTimeChanged Event

Invoked when the warning state of the timer progress changes.

```csharp
public event EventHandler RemainingTimeChanged;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.TimeCounter.WarningChanged'></a>

## TimeCounter.WarningChanged Event

Invoked when the warning state of the timer progress changes.

```csharp
public event EventHandler WarningChanged;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')


























































