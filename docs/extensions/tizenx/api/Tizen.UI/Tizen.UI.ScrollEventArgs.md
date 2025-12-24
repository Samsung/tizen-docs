### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## ScrollEventArgs Class

The event arguments of scroll.

```csharp
public class ScrollEventArgs : System.EventArgs
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs') &#129106; ScrollEventArgs
### Constructors

<a name='Tizen.UI.ScrollEventArgs.ScrollEventArgs()'></a>

## ScrollEventArgs() Constructor

Create scroll evnet arguments.

```csharp
public ScrollEventArgs();
```

<a name='Tizen.UI.ScrollEventArgs.ScrollEventArgs(Tizen.UI.Point,Tizen.UI.Point)'></a>

## ScrollEventArgs(Point, Point) Constructor

Create scroll event arguments with initial values.

```csharp
public ScrollEventArgs(Tizen.UI.Point scrollPosition, Tizen.UI.Point displacement);
```
#### Parameters

<a name='Tizen.UI.ScrollEventArgs.ScrollEventArgs(Tizen.UI.Point,Tizen.UI.Point).scrollPosition'></a>

`scrollPosition` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The scroll position.

<a name='Tizen.UI.ScrollEventArgs.ScrollEventArgs(Tizen.UI.Point,Tizen.UI.Point).displacement'></a>

`displacement` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The scroll displacement.
### Properties

<a name='Tizen.UI.ScrollEventArgs.Displacement'></a>

## ScrollEventArgs.Displacement Property

The displacement of the scroll.

```csharp
public Tizen.UI.Point Displacement { get; set; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

<a name='Tizen.UI.ScrollEventArgs.ScrollPosition'></a>

## ScrollEventArgs.ScrollPosition Property

The position of the scroll.

```csharp
public Tizen.UI.Point ScrollPosition { get; set; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')




