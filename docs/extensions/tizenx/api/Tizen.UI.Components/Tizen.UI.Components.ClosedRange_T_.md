### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## ClosedRange&lt;T> Struct

A range that is inclusive of both ends.

```csharp
public struct ClosedRange&lt;T>
    where T : System.IComparable&lt;T>
```
#### Type parameters

<a name='Tizen.UI.Components.ClosedRange_T_.T'></a>

`T`
### Constructors

<a name='Tizen.UI.Components.ClosedRange_T_.ClosedRange(T,T)'></a>

## ClosedRange(T, T) Constructor

Construct a closed range with the given start and end values.

```csharp
public ClosedRange(T startValue, T endValue);
```
#### Parameters

<a name='Tizen.UI.Components.ClosedRange_T_.ClosedRange(T,T).startValue'></a>

`startValue` [T](Tizen.UI.Components.ClosedRange_T_.md#Tizen.UI.Components.ClosedRange_T_.T 'Tizen.UI.Components.ClosedRange&lt;T>.T')

The start value of the range.

<a name='Tizen.UI.Components.ClosedRange_T_.ClosedRange(T,T).endValue'></a>

`endValue` [T](Tizen.UI.Components.ClosedRange_T_.md#Tizen.UI.Components.ClosedRange_T_.T 'Tizen.UI.Components.ClosedRange&lt;T>.T')

The end value of the range.

#### Exceptions

[System.ArgumentException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentException 'System.ArgumentException')  
Thrown when the start value is greater than or equal to the end value.
### Properties

<a name='Tizen.UI.Components.ClosedRange_T_.EndValue'></a>

## ClosedRange&lt;T>.EndValue Property

The end value of the range.

```csharp
public readonly T EndValue { get; }
```

#### Property Value
[T](Tizen.UI.Components.ClosedRange_T_.md#Tizen.UI.Components.ClosedRange_T_.T 'Tizen.UI.Components.ClosedRange&lt;T>.T')

<a name='Tizen.UI.Components.ClosedRange_T_.StartValue'></a>

## ClosedRange&lt;T>.StartValue Property

The start value of the range.

```csharp
public readonly T StartValue { get; }
```

#### Property Value
[T](Tizen.UI.Components.ClosedRange_T_.md#Tizen.UI.Components.ClosedRange_T_.T 'Tizen.UI.Components.ClosedRange&lt;T>.T')
### Methods

<a name='Tizen.UI.Components.ClosedRange_T_.Clamp(T)'></a>

## ClosedRange&lt;T>.Clamp(T) Method

Enusres it fits in the range.

```csharp
public readonly T Clamp(T value);
```
#### Parameters

<a name='Tizen.UI.Components.ClosedRange_T_.Clamp(T).value'></a>

`value` [T](Tizen.UI.Components.ClosedRange_T_.md#Tizen.UI.Components.ClosedRange_T_.T 'Tizen.UI.Components.ClosedRange&lt;T>.T')

The value to be clamped.

#### Returns
[T](Tizen.UI.Components.ClosedRange_T_.md#Tizen.UI.Components.ClosedRange_T_.T 'Tizen.UI.Components.ClosedRange&lt;T>.T')  
The clamped value.

<a name='Tizen.UI.Components.ClosedRange_T_.Contains(T)'></a>

## ClosedRange&lt;T>.Contains(T) Method

Determine whether the given value is within this range.

```csharp
public readonly bool Contains(T value);
```
#### Parameters

<a name='Tizen.UI.Components.ClosedRange_T_.Contains(T).value'></a>

`value` [T](Tizen.UI.Components.ClosedRange_T_.md#Tizen.UI.Components.ClosedRange_T_.T 'Tizen.UI.Components.ClosedRange&lt;T>.T')

The value to check.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the value is within the range, false otherwise.

<a name='Tizen.UI.Components.ClosedRange_T_.ToString()'></a>

## ClosedRange&lt;T>.ToString() Method

Returns the fully qualified type name of this instance.

```csharp
public override string ToString();
```

#### Returns
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
The fully qualified type name.


























































