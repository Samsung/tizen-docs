### [TizenX.RPCPort](TizenX.RPCPort.md 'TizenX.RPCPort')

## ParcelHeader Class

Represents a header for parcel data containing metadata about the parcel.

```csharp
public class ParcelHeader : IParcelable
```

### Properties

<a name='TizenX.RPCPort.ParcelHeader.DataSize'></a>

## DataSize

Gets the size of the header data when serialized.

```csharp
public int DataSize { get; }
```
#### Property Value

int

The total size in bytes of the serialized header data.

<a name='TizenX.RPCPort.ParcelHeader.SequenceNumber'></a>

## SequenceNumber

Gets or sets the sequence number of this header.

```csharp
public int SequenceNumber { get; set; }
```
#### Property Value

int

An integer representing the sequence number for ordering parcels.

<a name='TizenX.RPCPort.ParcelHeader.Tag'></a>

## Tag

Gets or sets the tag associated with this header.

```csharp
public string Tag { get; set; }
```
#### Property Value

string

A string tag used to identify or categorize the parcel.

<a name='TizenX.RPCPort.ParcelHeader.TimeStamp'></a>

## TimeStamp

Gets or sets the timestamp of this header.

```csharp
public DateTimeOffset TimeStamp { get; set; }
```
#### Property Value

DateTimeOffset

A DateTimeOffset representing when the parcel was created or processed.

### Methods

<a name='TizenX.RPCPort.ParcelHeader.ReadFrom.System.Span.System.Byte..'></a>

## ReadFrom(Span<byte>)

Reads header data from the specified byte span.

```csharp
public int ReadFrom(Span<byte> bytes)
```
#### Parameters

`bytes` Span<byte>

The byte span to read from.

#### Returns

int

The number of bytes read.

<a name='TizenX.RPCPort.ParcelHeader.SetTimeStamp.System.Int64.System.Int64.'></a>

## SetTimeStamp(long, long)

Sets the timestamp using Unix time seconds and nanoseconds.

```csharp
public void SetTimeStamp(long sec, long nsec)
```
#### Parameters

`sec` long

The Unix time seconds.

`nsec` long

The nanoseconds component.

<a name='TizenX.RPCPort.ParcelHeader.WriteTo.System.Span.System.Byte..'></a>

## WriteTo(Span<byte>)

Writes the header data to the specified byte span.

```csharp
public int WriteTo(Span<byte> bytes)
```
#### Parameters

`bytes` Span<byte>

The byte span to write to.

#### Returns

int

The number of bytes written.

