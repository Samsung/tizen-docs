### [TizenX.RPCPort](TizenX.RPCPort.md 'TizenX.RPCPort')

## IParcelable Interface

Defines the interface for objects that can be serialized and deserialized for RPC communication.

```csharp
public interface IParcelable
```

### Properties

<a name='TizenX.RPCPort.IParcelable.DataSize'></a>

## DataSize

Gets the size of the data when serialized.

```csharp
int DataSize { get; }
```
#### Property Value

int

The size in bytes of the serialized data.

### Methods

<a name='TizenX.RPCPort.IParcelable.ReadFrom.System.Span.System.Byte..'></a>

## ReadFrom(Span<byte>)

Reads the object data from the specified byte span.

```csharp
int ReadFrom(Span<byte> bytes)
```
#### Parameters

`bytes` Span<byte>

The span of bytes to read the data from.

#### Returns

int

The number of bytes read.

<a name='TizenX.RPCPort.IParcelable.WriteTo.System.Span.System.Byte..'></a>

## WriteTo(Span<byte>)

Writes the object data to the specified byte span.

```csharp
int WriteTo(Span<byte> bytes)
```
#### Parameters

`bytes` Span<byte>

The span of bytes to write the data to.

#### Returns

int

The number of bytes written.

