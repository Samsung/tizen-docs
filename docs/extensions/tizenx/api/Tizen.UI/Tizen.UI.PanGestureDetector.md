### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## PanGestureDetector Class

The PanGestureDetector class is used to detect panning gestures on a View.

```csharp
public class PanGestureDetector : Tizen.UI.GestureDetector
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; [GestureDetector](Tizen.UI.GestureDetector.md 'Tizen.UI.GestureDetector') &#129106; PanGestureDetector
### Constructors

<a name='Tizen.UI.PanGestureDetector.PanGestureDetector()'></a>

## PanGestureDetector() Constructor

Creates a new PanGestureDetector.

```csharp
public PanGestureDetector();
```
### Properties

<a name='Tizen.UI.PanGestureDetector.Direction'></a>

## PanGestureDetector.Direction Property

Gets or sets the direction of the pan gesture to detect.

```csharp
public Tizen.UI.PanGestureDirection Direction { get; set; }
```

#### Property Value
[PanGestureDirection](Tizen.UI.PanGestureDirection.md 'Tizen.UI.PanGestureDirection')

<a name='Tizen.UI.PanGestureDetector.MaximumTouchesRequired'></a>

## PanGestureDetector.MaximumTouchesRequired Property

Gets or sets the maximum number of touches required to recognize a pan gesture.

```csharp
public int MaximumTouchesRequired { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.PanGestureDetector.MinimumTouchesRequired'></a>

## PanGestureDetector.MinimumTouchesRequired Property

Gets or sets the minimum number of touches required to recognize a pan gesture.

```csharp
public int MinimumTouchesRequired { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')
### Events

<a name='Tizen.UI.PanGestureDetector.Detected'></a>

## PanGestureDetector.Detected Event

Event triggered when a pan gesture is detected on the attached View.

```csharp
public event EventHandler&lt;PanGestureDetectedEventArgs> Detected;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[PanGestureDetectedEventArgs](Tizen.UI.PanGestureDetectedEventArgs.md 'Tizen.UI.PanGestureDetectedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')






