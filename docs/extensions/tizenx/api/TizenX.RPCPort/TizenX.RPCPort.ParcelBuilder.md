### [TizenX.RPCPort](TizenX.RPCPort.md 'TizenX.RPCPort')

## ParcelBuilder Class

Provides a fluent API for building Parcel objects by adding various types of data.

```csharp
public sealed class ParcelBuilder
```

### Methods

<a name='TizenX.RPCPort.ParcelBuilder.Add.System.String.'></a>

## Add(string)

Adds a string value to the builder by wrapping it in a StringParcelable.

```csharp
public ParcelBuilder Add(string value)
```
#### Parameters

`value` string

The string value to add.

#### Returns

ParcelBuilder

The current ParcelBuilder instance for method chaining.

<a name='TizenX.RPCPort.ParcelBuilder.Add.TizenX.RPCPort.IParcelable.'></a>

## Add(IParcelable)

Adds an IParcelable object to the builder.

```csharp
public ParcelBuilder Add(IParcelable parcelable)
```
#### Parameters

`parcelable` IParcelable

The IParcelable object to add.

#### Returns

ParcelBuilder

The current ParcelBuilder instance for method chaining.

<a name='TizenX.RPCPort.ParcelBuilder.Add..1...0.'></a>

## Add<T>(T)

Adds a value type to the builder by wrapping it in a ValueParcelable.

```csharp
public ParcelBuilder Add<T>(T v) where T : struct
```
#### Parameters

`v` T

The value to add.

#### Returns

ParcelBuilder

The current ParcelBuilder instance for method chaining.

<a name='TizenX.RPCPort.ParcelBuilder.Build.TizenX.RPCPort.ParcelHeader.TizenX.RPCPort.Parcel.'></a>

## Build(ParcelHeader, Parcel)

Builds the Parcel with the added data and the specified header.

```csharp
public int Build(ParcelHeader header, Parcel parcel)
```
#### Parameters

`header` ParcelHeader

The ParcelHeader to use for the parcel.

`parcel` Parcel

The Parcel to write the data to.

#### Returns

int

The number of bytes written to the parcel.

