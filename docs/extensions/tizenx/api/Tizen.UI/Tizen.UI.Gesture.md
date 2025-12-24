### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## Gesture Class

The Gesture class is an abstract class that represents a gesture detected by the system.

```csharp
public abstract class Gesture : Tizen.UI.NObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; Gesture

Derived  
&#8627; [LongPressGesture](Tizen.UI.LongPressGesture.md 'Tizen.UI.LongPressGesture')  
&#8627; [PanGesture](Tizen.UI.PanGesture.md 'Tizen.UI.PanGesture')  
&#8627; [PinchGesture](Tizen.UI.PinchGesture.md 'Tizen.UI.PinchGesture')  
&#8627; [RotationGesture](Tizen.UI.RotationGesture.md 'Tizen.UI.RotationGesture')  
&#8627; [TapGesture](Tizen.UI.TapGesture.md 'Tizen.UI.TapGesture')
### Properties

<a name='Tizen.UI.Gesture.Source'></a>

## Gesture.Source Property

Gets the source of the gesture.

```csharp
public Tizen.UI.GestureSource Source { get; }
```

#### Property Value
[GestureSource](Tizen.UI.GestureSource.md 'Tizen.UI.GestureSource')

<a name='Tizen.UI.Gesture.SourceData'></a>

## Gesture.SourceData Property

Gets the source data of the gesture.

```csharp
public Tizen.UI.GestureSourceData SourceData { get; }
```

#### Property Value
[GestureSourceData](Tizen.UI.GestureSourceData.md 'Tizen.UI.GestureSourceData')

<a name='Tizen.UI.Gesture.State'></a>

## Gesture.State Property

Gets the state of the gesture.

```csharp
public Tizen.UI.GestureState State { get; }
```

#### Property Value
[GestureState](Tizen.UI.GestureState.md 'Tizen.UI.GestureState')

<a name='Tizen.UI.Gesture.Time'></a>

## Gesture.Time Property

Gets the time when the gesture was detected.

```csharp
public uint Time { get; }
```

#### Property Value
[System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')






