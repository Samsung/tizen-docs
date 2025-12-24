### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## Timer Class

The Timer class provides a convenient way to run a function at specified time intervals.

```csharp
public class Timer : Tizen.UI.NObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; Timer
### Constructors

<a name='Tizen.UI.Timer.Timer(uint)'></a>

## Timer(uint) Constructor

Initializes a new instance of the Timer class with the specified interval in milliseconds.

```csharp
public Timer(uint millisec);
```
#### Parameters

<a name='Tizen.UI.Timer.Timer(uint).millisec'></a>

`millisec` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The interval in milliseconds.
### Properties

<a name='Tizen.UI.Timer.Interval'></a>

## Timer.Interval Property

Gets or sets the interval of the timer in milliseconds.

```csharp
public uint Interval { get; set; }
```

#### Property Value
[System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

<a name='Tizen.UI.Timer.IsRunning'></a>

## Timer.IsRunning Property

Gets a value indicating whether the timer is running or not.

```csharp
public bool IsRunning { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Timer.TickHandler'></a>

## Timer.TickHandler Property

Gets or sets the handler function to be called when the timer is ticked.

```csharp
public System.Func&lt;bool> TickHandler { get; set; }
```

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')
### Methods

<a name='Tizen.UI.Timer.Repeat(uint,System.Func_bool_)'></a>

## Timer.Repeat(uint, Func&lt;bool>) Method

Creates a new [Timer](Tizen.UI.Timer.md 'Tizen.UI.Timer') instance that repeatedly executes the specified function at a specified interval in milliseconds.

```csharp
public static Tizen.UI.Timer Repeat(uint interval, System.Func&lt;bool> handler);
```
#### Parameters

<a name='Tizen.UI.Timer.Repeat(uint,System.Func_bool_).interval'></a>

`interval` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The interval in milliseconds between timer ticks.

<a name='Tizen.UI.Timer.Repeat(uint,System.Func_bool_).handler'></a>

`handler` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')

The function to be invoked when the timer elapses. The function should return a value indicating whether to continue  
            running the timer. Return true to keep the timer running, false to stop it.

#### Returns
[Timer](Tizen.UI.Timer.md 'Tizen.UI.Timer')  
A new [Timer](Tizen.UI.Timer.md 'Tizen.UI.Timer') instance that will repeatedly execute the specified function at the specified interval.

<a name='Tizen.UI.Timer.Reset()'></a>

## Timer.Reset() Method

Resets the timer. If the timer is running, it is first stopped, and then restarted.

```csharp
public void Reset();
```

<a name='Tizen.UI.Timer.Start()'></a>

## Timer.Start() Method

Starts the timer.

```csharp
public void Start();
```

<a name='Tizen.UI.Timer.Stop()'></a>

## Timer.Stop() Method

Stops the timer.

```csharp
public void Stop();
```

<a name='Tizen.UI.Timer.Timeout(uint,System.Action)'></a>

## Timer.Timeout(uint, Action) Method

Creates a new [Timer](Tizen.UI.Timer.md 'Tizen.UI.Timer') instance that executes a single action after the specified timeout in milliseconds.

```csharp
public static Tizen.UI.Timer Timeout(uint timeout, System.Action action);
```
#### Parameters

<a name='Tizen.UI.Timer.Timeout(uint,System.Action).timeout'></a>

`timeout` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The timeout in milliseconds before executing the action.

<a name='Tizen.UI.Timer.Timeout(uint,System.Action).action'></a>

`action` [System.Action](https://docs.microsoft.com/en-us/dotnet/api/System.Action 'System.Action')

The action to be executed after the timeout elapses.

#### Returns
[Timer](Tizen.UI.Timer.md 'Tizen.UI.Timer')  
A new [Timer](Tizen.UI.Timer.md 'Tizen.UI.Timer') instance that will execute the specified action after the timeout.




