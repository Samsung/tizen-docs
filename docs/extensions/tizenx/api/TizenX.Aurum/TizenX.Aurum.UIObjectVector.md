### [TizenX.Aurum](TizenX.Aurum.md 'TizenX.Aurum')

## UIObjectVector Class

Represents a collection of UIObject instances with vector-like operations.
This class provides methods for managing, searching, and manipulating collections of UI elements.

```csharp
public class UIObjectVector : IDisposable, IEnumerable<UIObject>, IEnumerable
```

### Constructors

<a name='TizenX.Aurum.UIObjectVector..ctor'></a>

## UIObjectVector()

```csharp
public UIObjectVector()
```
<a name='TizenX.Aurum.UIObjectVector..ctor.System.Collections.Generic.IEnumerable.TizenX.Aurum.UIObject..'></a>

## UIObjectVector(IEnumerable<UIObject>)

```csharp
public UIObjectVector(IEnumerable<UIObject> c)
```
#### Parameters

`c` IEnumerable<UIObject>

<a name='TizenX.Aurum.UIObjectVector..ctor.System.Collections.IEnumerable.'></a>

## UIObjectVector(IEnumerable)

```csharp
public UIObjectVector(IEnumerable c)
```
#### Parameters

`c` IEnumerable

<a name='TizenX.Aurum.UIObjectVector..ctor.System.Int32.'></a>

## UIObjectVector(int)

```csharp
public UIObjectVector(int capacity)
```
#### Parameters

`capacity` int

<a name='TizenX.Aurum.UIObjectVector..ctor.TizenX.Aurum.UIObjectVector.'></a>

## UIObjectVector(UIObjectVector)

```csharp
public UIObjectVector(UIObjectVector other)
```
#### Parameters

`other` UIObjectVector

### Properties

<a name='TizenX.Aurum.UIObjectVector.Capacity'></a>

## Capacity

```csharp
public int Capacity { get; set; }
```
#### Property Value

int

<a name='TizenX.Aurum.UIObjectVector.Count'></a>

## Count

```csharp
public int Count { get; }
```
#### Property Value

int

<a name='TizenX.Aurum.UIObjectVector.IsFixedSize'></a>

## IsFixedSize

```csharp
public bool IsFixedSize { get; }
```
#### Property Value

bool

<a name='TizenX.Aurum.UIObjectVector.IsReadOnly'></a>

## IsReadOnly

```csharp
public bool IsReadOnly { get; }
```
#### Property Value

bool

<a name='TizenX.Aurum.UIObjectVector.IsSynchronized'></a>

## IsSynchronized

```csharp
public bool IsSynchronized { get; }
```
#### Property Value

bool

<a name='TizenX.Aurum.UIObjectVector.Item.System.Int32.'></a>

## this[int]

Gets or sets the UIObject at the specified index in the vector.

```csharp
public UIObject this[int index] { get; set; }
```
#### Parameters

`index` int

The zero-based index of the element to get or set.

#### Property Value

UIObject

The UIObject at the specified index.

### Fields

<a name='TizenX.Aurum.UIObjectVector.swigCMemOwn'></a>

## swigCMemOwn

```csharp
protected bool swigCMemOwn
```
#### Field Value

bool

### Methods

<a name='TizenX.Aurum.UIObjectVector.Add.TizenX.Aurum.UIObject.'></a>

## Add(UIObject)

```csharp
public void Add(UIObject x)
```
#### Parameters

`x` UIObject

<a name='TizenX.Aurum.UIObjectVector.AddRange.TizenX.Aurum.UIObjectVector.'></a>

## AddRange(UIObjectVector)

```csharp
public void AddRange(UIObjectVector values)
```
#### Parameters

`values` UIObjectVector

<a name='TizenX.Aurum.UIObjectVector.Clear'></a>

## Clear()

```csharp
public void Clear()
```
<a name='TizenX.Aurum.UIObjectVector.CopyTo.System.Int32.TizenX.Aurum.UIObject...System.Int32.System.Int32.'></a>

## CopyTo(int, UIObject[], int, int)

```csharp
public void CopyTo(int index, UIObject[] array, int arrayIndex, int count)
```
#### Parameters

`index` int

`array` UIObject[]

`arrayIndex` int

`count` int

<a name='TizenX.Aurum.UIObjectVector.CopyTo.TizenX.Aurum.UIObject...'></a>

## CopyTo(UIObject[])

```csharp
public void CopyTo(UIObject[] array)
```
#### Parameters

`array` UIObject[]

<a name='TizenX.Aurum.UIObjectVector.CopyTo.TizenX.Aurum.UIObject...System.Int32.'></a>

## CopyTo(UIObject[], int)

```csharp
public void CopyTo(UIObject[] array, int arrayIndex)
```
#### Parameters

`array` UIObject[]

`arrayIndex` int

<a name='TizenX.Aurum.UIObjectVector.Dispose'></a>

## Dispose()

Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.

```csharp
public void Dispose()
```
<a name='TizenX.Aurum.UIObjectVector.Dispose.System.Boolean.'></a>

## Dispose(bool)

```csharp
protected virtual void Dispose(bool disposing)
```
#### Parameters

`disposing` bool

<a name='TizenX.Aurum.UIObjectVector.Finalize'></a>

## ~UIObjectVector()

```csharp
protected ~UIObjectVector()
```
<a name='TizenX.Aurum.UIObjectVector.GetEnumerator'></a>

## GetEnumerator()

```csharp
public UIObjectVector.UIObjectVectorEnumerator GetEnumerator()
```
#### Returns

UIObjectVector.UIObjectVectorEnumerator

<a name='TizenX.Aurum.UIObjectVector.GetRange.System.Int32.System.Int32.'></a>

## GetRange(int, int)

```csharp
public UIObjectVector GetRange(int index, int count)
```
#### Parameters

`index` int

`count` int

#### Returns

UIObjectVector

<a name='TizenX.Aurum.UIObjectVector.Insert.System.Int32.TizenX.Aurum.UIObject.'></a>

## Insert(int, UIObject)

```csharp
public void Insert(int index, UIObject x)
```
#### Parameters

`index` int

`x` UIObject

<a name='TizenX.Aurum.UIObjectVector.InsertRange.System.Int32.TizenX.Aurum.UIObjectVector.'></a>

## InsertRange(int, UIObjectVector)

```csharp
public void InsertRange(int index, UIObjectVector values)
```
#### Parameters

`index` int

`values` UIObjectVector

<a name='TizenX.Aurum.UIObjectVector.RemoveAt.System.Int32.'></a>

## RemoveAt(int)

```csharp
public void RemoveAt(int index)
```
#### Parameters

`index` int

<a name='TizenX.Aurum.UIObjectVector.RemoveRange.System.Int32.System.Int32.'></a>

## RemoveRange(int, int)

```csharp
public void RemoveRange(int index, int count)
```
#### Parameters

`index` int

`count` int

<a name='TizenX.Aurum.UIObjectVector.Repeat.TizenX.Aurum.UIObject.System.Int32.'></a>

## Repeat(UIObject, int)

```csharp
public static UIObjectVector Repeat(UIObject value, int count)
```
#### Parameters

`value` UIObject

`count` int

#### Returns

UIObjectVector

<a name='TizenX.Aurum.UIObjectVector.Reverse'></a>

## Reverse()

```csharp
public void Reverse()
```
<a name='TizenX.Aurum.UIObjectVector.Reverse.System.Int32.System.Int32.'></a>

## Reverse(int, int)

```csharp
public void Reverse(int index, int count)
```
#### Parameters

`index` int

`count` int

<a name='TizenX.Aurum.UIObjectVector.SetRange.System.Int32.TizenX.Aurum.UIObjectVector.'></a>

## SetRange(int, UIObjectVector)

```csharp
public void SetRange(int index, UIObjectVector values)
```
#### Parameters

`index` int

`values` UIObjectVector

<a name='TizenX.Aurum.UIObjectVector.ToArray'></a>

## ToArray()

```csharp
public UIObject[] ToArray()
```
#### Returns

UIObject[]

