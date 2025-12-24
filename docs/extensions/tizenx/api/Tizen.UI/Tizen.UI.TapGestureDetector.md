### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## TapGestureDetector Class

The TapGestureDetector class is used to detect when the user performs a tap gesture on a view.

```csharp
public class TapGestureDetector : Tizen.UI.GestureDetector
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; [GestureDetector](Tizen.UI.GestureDetector.md 'Tizen.UI.GestureDetector') &#129106; TapGestureDetector
### Constructors

<a name='Tizen.UI.TapGestureDetector.TapGestureDetector()'></a>

## TapGestureDetector() Constructor

Creates a new TapGestureDetector.

```csharp
public TapGestureDetector();
```

<a name='Tizen.UI.TapGestureDetector.TapGestureDetector(int)'></a>

## TapGestureDetector(int) Constructor

Creates a new TapGestureDetector with the specified number of taps required.

```csharp
public TapGestureDetector(int tapsRequired);
```
#### Parameters

<a name='Tizen.UI.TapGestureDetector.TapGestureDetector(int).tapsRequired'></a>

`tapsRequired` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The number of taps required for the gesture to be recognized.
### Properties

<a name='Tizen.UI.TapGestureDetector.MaximumTapsRequired'></a>

## TapGestureDetector.MaximumTapsRequired Property

Gets or sets the maximum number of taps required for the gesture to be recognized.

```csharp
public int MaximumTapsRequired { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.TapGestureDetector.MinimumTapsRequired'></a>

## TapGestureDetector.MinimumTapsRequired Property

Gets or sets the minimum number of taps required for the gesture to be recognized.

```csharp
public int MinimumTapsRequired { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')
### Events

<a name='Tizen.UI.TapGestureDetector.Detected'></a>

## TapGestureDetector.Detected Event

Occurs when the user performs a tap gesture on the view.

```csharp
public event EventHandler&lt;TapGestureDetectedEventArgs> Detected;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[TapGestureDetectedEventArgs](Tizen.UI.TapGestureDetectedEventArgs.md 'Tizen.UI.TapGestureDetectedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')






