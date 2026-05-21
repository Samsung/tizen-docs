### [TizenX.Aurum](TizenX.Aurum.md 'TizenX.Aurum')

## Rect Class

```csharp
public class Rect : IDisposable
```

### Constructors

<a name='TizenX.Aurum.Rect..ctor'></a>

## Rect()

```csharp
public Rect()
```
<a name='TizenX.Aurum.Rect..ctor.System.Int32.System.Int32.System.Int32.System.Int32.'></a>

## Rect(int, int, int, int)

```csharp
public Rect(int x1, int y1, int x2, int y2)
```
#### Parameters

`x1` int

`y1` int

`x2` int

`y2` int

<a name='TizenX.Aurum.Rect..ctor.TizenX.Aurum.Point2D.TizenX.Aurum.Point2D.'></a>

## Rect(Point2D, Point2D)

```csharp
public Rect(Point2D tl, Point2D br)
```
#### Parameters

`tl` Point2D

`br` Point2D

<a name='TizenX.Aurum.Rect..ctor.TizenX.Aurum.Rect.'></a>

## Rect(Rect)

```csharp
public Rect(Rect src)
```
#### Parameters

`src` Rect

### Fields

<a name='TizenX.Aurum.Rect.swigCMemOwn'></a>

## swigCMemOwn

```csharp
protected bool swigCMemOwn
```
#### Field Value

bool

### Methods

<a name='TizenX.Aurum.Rect.Diff.TizenX.Aurum.Rect.'></a>

## Diff(Rect)

```csharp
public bool Diff(Rect rhs)
```
#### Parameters

`rhs` Rect

#### Returns

bool

<a name='TizenX.Aurum.Rect.Dispose'></a>

## Dispose()

Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.

```csharp
public void Dispose()
```
<a name='TizenX.Aurum.Rect.Dispose.System.Boolean.'></a>

## Dispose(bool)

```csharp
protected virtual void Dispose(bool disposing)
```
#### Parameters

`disposing` bool

<a name='TizenX.Aurum.Rect.Equal.TizenX.Aurum.Rect.'></a>

## Equal(Rect)

```csharp
public bool Equal(Rect rhs)
```
#### Parameters

`rhs` Rect

#### Returns

bool

<a name='TizenX.Aurum.Rect.Finalize'></a>

## ~Rect()

```csharp
protected ~Rect()
```
<a name='TizenX.Aurum.Rect.Height'></a>

## Height()

```csharp
public int Height()
```
#### Returns

int

<a name='TizenX.Aurum.Rect.IsInRect.TizenX.Aurum.Point2D.'></a>

## IsInRect(Point2D)

```csharp
public bool IsInRect(Point2D point)
```
#### Parameters

`point` Point2D

#### Returns

bool

<a name='TizenX.Aurum.Rect.IsInRect.TizenX.Aurum.Rect.'></a>

## IsInRect(Rect)

```csharp
public bool IsInRect(Rect rect)
```
#### Parameters

`rect` Rect

#### Returns

bool

<a name='TizenX.Aurum.Rect.MidPoint'></a>

## MidPoint()

```csharp
public Point2D MidPoint()
```
#### Returns

Point2D

<a name='TizenX.Aurum.Rect.Width'></a>

## Width()

```csharp
public int Width()
```
#### Returns

int

