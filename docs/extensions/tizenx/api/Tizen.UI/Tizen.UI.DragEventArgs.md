### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## DragEventArgs Class

The event arguments of drag.

```csharp
public class DragEventArgs : System.EventArgs
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs') &#129106; DragEventArgs
### Constructors

<a name='Tizen.UI.DragEventArgs.DragEventArgs()'></a>

## DragEventArgs() Constructor

Create drag evnet arguments.

```csharp
public DragEventArgs();
```

<a name='Tizen.UI.DragEventArgs.DragEventArgs(Tizen.UI.Point,Tizen.UI.Point)'></a>

## DragEventArgs(Point, Point) Constructor

Create drag event arguments with initial values.

```csharp
public DragEventArgs(Tizen.UI.Point touchPosition, Tizen.UI.Point displacement);
```
#### Parameters

<a name='Tizen.UI.DragEventArgs.DragEventArgs(Tizen.UI.Point,Tizen.UI.Point).touchPosition'></a>

`touchPosition` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The drag touch screen position.

<a name='Tizen.UI.DragEventArgs.DragEventArgs(Tizen.UI.Point,Tizen.UI.Point).displacement'></a>

`displacement` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The drag displacement.
### Properties

<a name='Tizen.UI.DragEventArgs.Displacement'></a>

## DragEventArgs.Displacement Property

The displacement of the drag.

```csharp
public Tizen.UI.Point Displacement { get; set; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

<a name='Tizen.UI.DragEventArgs.TouchPosition'></a>

## DragEventArgs.TouchPosition Property

The screen position of the drag touch.

```csharp
public Tizen.UI.Point TouchPosition { get; set; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')




