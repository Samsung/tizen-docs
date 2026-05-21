### [TizenX.Aurum](TizenX.Aurum.md 'TizenX.Aurum')

## UISelectorVector Class

```csharp
public class UISelectorVector : IDisposable, IEnumerable<UISelector>, IEnumerable
```

### Constructors

<a name='TizenX.Aurum.UISelectorVector..ctor'></a>

## UISelectorVector()

```csharp
public UISelectorVector()
```
<a name='TizenX.Aurum.UISelectorVector..ctor.System.Collections.Generic.IEnumerable.TizenX.Aurum.UISelector..'></a>

## UISelectorVector(IEnumerable<UISelector>)

```csharp
public UISelectorVector(IEnumerable<UISelector> c)
```
#### Parameters

`c` IEnumerable<UISelector>

<a name='TizenX.Aurum.UISelectorVector..ctor.System.Collections.IEnumerable.'></a>

## UISelectorVector(IEnumerable)

```csharp
public UISelectorVector(IEnumerable c)
```
#### Parameters

`c` IEnumerable

<a name='TizenX.Aurum.UISelectorVector..ctor.System.Int32.'></a>

## UISelectorVector(int)

```csharp
public UISelectorVector(int capacity)
```
#### Parameters

`capacity` int

<a name='TizenX.Aurum.UISelectorVector..ctor.TizenX.Aurum.UISelectorVector.'></a>

## UISelectorVector(UISelectorVector)

```csharp
public UISelectorVector(UISelectorVector other)
```
#### Parameters

`other` UISelectorVector

### Properties

<a name='TizenX.Aurum.UISelectorVector.Capacity'></a>

## Capacity

```csharp
public int Capacity { get; set; }
```
#### Property Value

int

<a name='TizenX.Aurum.UISelectorVector.Count'></a>

## Count

```csharp
public int Count { get; }
```
#### Property Value

int

<a name='TizenX.Aurum.UISelectorVector.IsFixedSize'></a>

## IsFixedSize

```csharp
public bool IsFixedSize { get; }
```
#### Property Value

bool

<a name='TizenX.Aurum.UISelectorVector.IsReadOnly'></a>

## IsReadOnly

```csharp
public bool IsReadOnly { get; }
```
#### Property Value

bool

<a name='TizenX.Aurum.UISelectorVector.IsSynchronized'></a>

## IsSynchronized

```csharp
public bool IsSynchronized { get; }
```
#### Property Value

bool

<a name='TizenX.Aurum.UISelectorVector.Item.System.Int32.'></a>

## this[int]

```csharp
public UISelector this[int index] { get; set; }
```
#### Parameters

`index` int

#### Property Value

UISelector

### Fields

<a name='TizenX.Aurum.UISelectorVector.swigCMemOwn'></a>

## swigCMemOwn

```csharp
protected bool swigCMemOwn
```
#### Field Value

bool

### Methods

<a name='TizenX.Aurum.UISelectorVector.Add.TizenX.Aurum.UISelector.'></a>

## Add(UISelector)

```csharp
public void Add(UISelector x)
```
#### Parameters

`x` UISelector

<a name='TizenX.Aurum.UISelectorVector.AddRange.TizenX.Aurum.UISelectorVector.'></a>

## AddRange(UISelectorVector)

```csharp
public void AddRange(UISelectorVector values)
```
#### Parameters

`values` UISelectorVector

<a name='TizenX.Aurum.UISelectorVector.Clear'></a>

## Clear()

```csharp
public void Clear()
```
<a name='TizenX.Aurum.UISelectorVector.CopyTo.System.Int32.TizenX.Aurum.UISelector...System.Int32.System.Int32.'></a>

## CopyTo(int, UISelector[], int, int)

```csharp
public void CopyTo(int index, UISelector[] array, int arrayIndex, int count)
```
#### Parameters

`index` int

`array` UISelector[]

`arrayIndex` int

`count` int

<a name='TizenX.Aurum.UISelectorVector.CopyTo.TizenX.Aurum.UISelector...'></a>

## CopyTo(UISelector[])

```csharp
public void CopyTo(UISelector[] array)
```
#### Parameters

`array` UISelector[]

<a name='TizenX.Aurum.UISelectorVector.CopyTo.TizenX.Aurum.UISelector...System.Int32.'></a>

## CopyTo(UISelector[], int)

```csharp
public void CopyTo(UISelector[] array, int arrayIndex)
```
#### Parameters

`array` UISelector[]

`arrayIndex` int

<a name='TizenX.Aurum.UISelectorVector.Dispose'></a>

## Dispose()

Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.

```csharp
public void Dispose()
```
<a name='TizenX.Aurum.UISelectorVector.Dispose.System.Boolean.'></a>

## Dispose(bool)

```csharp
protected virtual void Dispose(bool disposing)
```
#### Parameters

`disposing` bool

<a name='TizenX.Aurum.UISelectorVector.Finalize'></a>

## ~UISelectorVector()

```csharp
protected ~UISelectorVector()
```
<a name='TizenX.Aurum.UISelectorVector.GetEnumerator'></a>

## GetEnumerator()

```csharp
public UISelectorVector.UISelectorVectorEnumerator GetEnumerator()
```
#### Returns

UISelectorVector.UISelectorVectorEnumerator

<a name='TizenX.Aurum.UISelectorVector.GetRange.System.Int32.System.Int32.'></a>

## GetRange(int, int)

```csharp
public UISelectorVector GetRange(int index, int count)
```
#### Parameters

`index` int

`count` int

#### Returns

UISelectorVector

<a name='TizenX.Aurum.UISelectorVector.Insert.System.Int32.TizenX.Aurum.UISelector.'></a>

## Insert(int, UISelector)

```csharp
public void Insert(int index, UISelector x)
```
#### Parameters

`index` int

`x` UISelector

<a name='TizenX.Aurum.UISelectorVector.InsertRange.System.Int32.TizenX.Aurum.UISelectorVector.'></a>

## InsertRange(int, UISelectorVector)

```csharp
public void InsertRange(int index, UISelectorVector values)
```
#### Parameters

`index` int

`values` UISelectorVector

<a name='TizenX.Aurum.UISelectorVector.RemoveAt.System.Int32.'></a>

## RemoveAt(int)

```csharp
public void RemoveAt(int index)
```
#### Parameters

`index` int

<a name='TizenX.Aurum.UISelectorVector.RemoveRange.System.Int32.System.Int32.'></a>

## RemoveRange(int, int)

```csharp
public void RemoveRange(int index, int count)
```
#### Parameters

`index` int

`count` int

<a name='TizenX.Aurum.UISelectorVector.Repeat.TizenX.Aurum.UISelector.System.Int32.'></a>

## Repeat(UISelector, int)

```csharp
public static UISelectorVector Repeat(UISelector value, int count)
```
#### Parameters

`value` UISelector

`count` int

#### Returns

UISelectorVector

<a name='TizenX.Aurum.UISelectorVector.Reverse'></a>

## Reverse()

```csharp
public void Reverse()
```
<a name='TizenX.Aurum.UISelectorVector.Reverse.System.Int32.System.Int32.'></a>

## Reverse(int, int)

```csharp
public void Reverse(int index, int count)
```
#### Parameters

`index` int

`count` int

<a name='TizenX.Aurum.UISelectorVector.SetRange.System.Int32.TizenX.Aurum.UISelectorVector.'></a>

## SetRange(int, UISelectorVector)

```csharp
public void SetRange(int index, UISelectorVector values)
```
#### Parameters

`index` int

`values` UISelectorVector

<a name='TizenX.Aurum.UISelectorVector.ToArray'></a>

## ToArray()

```csharp
public UISelector[] ToArray()
```
#### Returns

UISelector[]

