### [Tizen.UI.Internal](Tizen.UI.Internal.md 'Tizen.UI.Internal')

## ObjectPool&lt;T> Class

Provides a pool of objects that can be reused to improve performance and reduce memory usage.

```csharp
public class ObjectPool&lt;T> :
System.IDisposable
```
#### Type parameters

<a name='Tizen.UI.Internal.ObjectPool_T_.T'></a>

`T`

The type of object to pool.

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; ObjectPool&lt;T>

Implements [System.IDisposable](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable 'System.IDisposable')
### Constructors

<a name='Tizen.UI.Internal.ObjectPool_T_.ObjectPool(T)'></a>

## ObjectPool(T) Constructor

Initializes a new instance of the [ObjectPool&lt;T&gt;](Tizen.UI.Internal.ObjectPool_T_.md 'Tizen.UI.Internal.ObjectPool&lt;T>') class.

```csharp
public ObjectPool(T value);
```
#### Parameters

<a name='Tizen.UI.Internal.ObjectPool_T_.ObjectPool(T).value'></a>

`value` [T](Tizen.UI.Internal.ObjectPool_T_.md#Tizen.UI.Internal.ObjectPool_T_.T 'Tizen.UI.Internal.ObjectPool&lt;T>.T')

The initial value of the object.
### Properties

<a name='Tizen.UI.Internal.ObjectPool_T_.Count'></a>

## ObjectPool&lt;T>.Count Property

Gets the number of objects currently in the pool.

```csharp
public static int Count { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Internal.ObjectPool_T_.Value'></a>

## ObjectPool&lt;T>.Value Property

Gets the current value of the object.

```csharp
public T Value { get; }
```

#### Property Value
[T](Tizen.UI.Internal.ObjectPool_T_.md#Tizen.UI.Internal.ObjectPool_T_.T 'Tizen.UI.Internal.ObjectPool&lt;T>.T')
### Methods

<a name='Tizen.UI.Internal.ObjectPool_T_.Dispose()'></a>

## ObjectPool&lt;T>.Dispose() Method

Releases the object back into the pool.

```csharp
public void Dispose();
```

Implements [Dispose()](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable.Dispose 'System.IDisposable.Dispose')

<a name='Tizen.UI.Internal.ObjectPool_T_.New()'></a>

## ObjectPool&lt;T>.New() Method

Creates a new object from the pool or creates a new instance if the pool is empty.

```csharp
public static Tizen.UI.Internal.ObjectPool&lt;T> New();
```

#### Returns
[Tizen.UI.Internal.ObjectPool&lt;](Tizen.UI.Internal.ObjectPool_T_.md 'Tizen.UI.Internal.ObjectPool&lt;T>')[T](Tizen.UI.Internal.ObjectPool_T_.md#Tizen.UI.Internal.ObjectPool_T_.T 'Tizen.UI.Internal.ObjectPool&lt;T>.T')[&gt;](Tizen.UI.Internal.ObjectPool_T_.md 'Tizen.UI.Internal.ObjectPool&lt;T>')  
A new object from the pool or a new instance if the pool is empty.
### Operators

<a name='Tizen.UI.Internal.ObjectPool_T_.op_ImplicitT(Tizen.UI.Internal.ObjectPool_T_)'></a>

## ObjectPool&lt;T>.implicit operator T(ObjectPool&lt;T>) Operator

Implicitly converts the object pool to its underlying value.

```csharp
public static T implicit operator T(Tizen.UI.Internal.ObjectPool&lt;T> obj);
```
#### Parameters

<a name='Tizen.UI.Internal.ObjectPool_T_.op_ImplicitT(Tizen.UI.Internal.ObjectPool_T_).obj'></a>

`obj` [Tizen.UI.Internal.ObjectPool&lt;](Tizen.UI.Internal.ObjectPool_T_.md 'Tizen.UI.Internal.ObjectPool&lt;T>')[T](Tizen.UI.Internal.ObjectPool_T_.md#Tizen.UI.Internal.ObjectPool_T_.T 'Tizen.UI.Internal.ObjectPool&lt;T>.T')[&gt;](Tizen.UI.Internal.ObjectPool_T_.md 'Tizen.UI.Internal.ObjectPool&lt;T>')

The object pool to convert.

#### Returns
[T](Tizen.UI.Internal.ObjectPool_T_.md#Tizen.UI.Internal.ObjectPool_T_.T 'Tizen.UI.Internal.ObjectPool&lt;T>.T')




