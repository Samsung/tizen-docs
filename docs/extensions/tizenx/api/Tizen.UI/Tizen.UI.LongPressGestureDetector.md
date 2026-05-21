### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## LongPressGestureDetector Class

The LongPressGestureDetector class is used to detect long press gestures on a View.

```csharp
public class LongPressGestureDetector : Tizen.UI.GestureDetector
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; [GestureDetector](Tizen.UI.GestureDetector.md 'Tizen.UI.GestureDetector') &#129106; LongPressGestureDetector
### Constructors

<a name='Tizen.UI.LongPressGestureDetector.LongPressGestureDetector()'></a>

## LongPressGestureDetector() Constructor

Creates a new LongPressGestureDetector.

```csharp
public LongPressGestureDetector();
```
### Methods

<a name='Tizen.UI.LongPressGestureDetector.SetTouchesRequired(int)'></a>

## LongPressGestureDetector.SetTouchesRequired(int) Method

Sets the number of touches required for the gesture to be recognized.

```csharp
public void SetTouchesRequired(int touches);
```
#### Parameters

<a name='Tizen.UI.LongPressGestureDetector.SetTouchesRequired(int).touches'></a>

`touches` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The number of touches required.

<a name='Tizen.UI.LongPressGestureDetector.SetTouchesRequired(int,int)'></a>

## LongPressGestureDetector.SetTouchesRequired(int, int) Method

Sets the minimum and maximum number of touches required for the gesture to be recognized.

```csharp
public void SetTouchesRequired(int min, int max);
```
#### Parameters

<a name='Tizen.UI.LongPressGestureDetector.SetTouchesRequired(int,int).min'></a>

`min` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The minimum number of touches required.

<a name='Tizen.UI.LongPressGestureDetector.SetTouchesRequired(int,int).max'></a>

`max` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The maximum number of touches required.
### Events

<a name='Tizen.UI.LongPressGestureDetector.Detected'></a>

## LongPressGestureDetector.Detected Event

Event triggered when a long press gesture is detected on the attached View.

```csharp
public event EventHandler&lt;LongPressGestureDetectedEventArgs> Detected;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[LongPressGestureDetectedEventArgs](Tizen.UI.LongPressGestureDetectedEventArgs.md 'Tizen.UI.LongPressGestureDetectedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')






