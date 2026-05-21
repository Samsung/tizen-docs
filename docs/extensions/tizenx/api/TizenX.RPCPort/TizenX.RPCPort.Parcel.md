### [TizenX.RPCPort](TizenX.RPCPort.md 'TizenX.RPCPort')

## Parcel Class

Represents a parcel that can serialize and deserialize data for RPC communication.

```csharp
public class Parcel
```

### Properties

<a name='TizenX.RPCPort.Parcel.RawData'></a>

## RawData

```csharp
public Span<byte> RawData { get; }
```
#### Property Value

Span<byte>

### Methods

<a name='TizenX.RPCPort.Parcel.GetHandle.System.Object.'></a>

## GetHandle(object)

Gets the handle from an RPC port object.

```csharp
public static nint GetHandle(object port)
```
#### Parameters

`port` object

The RPC port object to get the handle from.

#### Returns

nint

The IntPtr handle of the RPC port.

<a name='TizenX.RPCPort.Parcel.ListParcelSize.System.Collections.Generic.List.System.Int32..'></a>

## ListParcelSize(List<int>)

Calculates the size of a list of integers when serialized to a parcel.

```csharp
public static int ListParcelSize(List<int> data)
```
#### Parameters

`data` List<int>

The list of integers to calculate the size for.

#### Returns

int

The size in bytes of the serialized list.

<a name='TizenX.RPCPort.Parcel.ListParcelSize.System.Collections.Generic.List.System.String..'></a>

## ListParcelSize(List<string>)

Calculates the size of a list of strings when serialized to a parcel.

```csharp
public static int ListParcelSize(List<string> data)
```
#### Parameters

`data` List<string>

The list of strings to calculate the size for.

#### Returns

int

The size in bytes of the serialized list.

<a name='TizenX.RPCPort.Parcel.LoadFromPort.System.IntPtr.'></a>

## LoadFromPort(nint)

Loads data from an RPC port handle.

```csharp
public int LoadFromPort(nint handle)
```
#### Parameters

`handle` nint

The IntPtr handle to the RPC port.

#### Returns

int

The size of the loaded data in bytes.

<a name='TizenX.RPCPort.Parcel.LoadFromRaw.System.Span.System.Byte..'></a>

## LoadFromRaw(Span<byte>)

Loads data from a byte span into the parcel.

```csharp
public int LoadFromRaw(Span<byte> bytes)
```
#### Parameters

`bytes` Span<byte>

The span of bytes to load data from.

#### Returns

int

The size of the loaded data in bytes.

<a name='TizenX.RPCPort.Parcel.Read.System.Boolean..'></a>

## Read(out bool)

Reads a boolean value from the parcel.

```csharp
public int Read(out bool value)
```
#### Parameters

`value` bool

The boolean value read from the parcel.

#### Returns

int

The new read offset position.

<a name='TizenX.RPCPort.Parcel.Read.System.Int32..'></a>

## Read(out int)

Reads an integer value from the parcel.

```csharp
public int Read(out int value)
```
#### Parameters

`value` int

The integer value read from the parcel.

#### Returns

int

The new read offset position.

<a name='TizenX.RPCPort.Parcel.Read.System.Span.System.Byte..System.Boolean..'></a>

## Read(Span<byte>, out bool)

Reads a boolean value from the specified buffer.

```csharp
public static int Read(Span<byte> buffer, out bool value)
```
#### Parameters

`buffer` Span<byte>

The buffer to read from.

`value` bool

The boolean value read from the buffer.

#### Returns

int

The number of bytes read.

<a name='TizenX.RPCPort.Parcel.Read.System.Span.System.Byte..System.Byte..'></a>

## Read(Span<byte>, out byte)

Reads a byte value from the specified buffer.

```csharp
public static int Read(Span<byte> buffer, out byte value)
```
#### Parameters

`buffer` Span<byte>

The buffer to read from.

`value` byte

The byte value read from the buffer.

#### Returns

int

The number of bytes read.

<a name='TizenX.RPCPort.Parcel.Read.System.Span.System.Byte..System.Collections.Generic.List.System.Int32...'></a>

## Read(Span<byte>, out List<int>)

Reads a list of integers from the specified buffer.

```csharp
public static int Read(Span<byte> buffer, out List<int> data)
```
#### Parameters

`buffer` Span<byte>

The buffer to read from.

`data` List<int>

The list of integers read from the buffer.

#### Returns

int

The number of bytes read.

<a name='TizenX.RPCPort.Parcel.Read.System.Span.System.Byte..System.Collections.Generic.List.System.String...'></a>

## Read(Span<byte>, out List<string>)

Reads a list of strings from the specified buffer.

```csharp
public static int Read(Span<byte> buffer, out List<string> data)
```
#### Parameters

`buffer` Span<byte>

The buffer to read from.

`data` List<string>

The list of strings read from the buffer.

#### Returns

int

The number of bytes read.

<a name='TizenX.RPCPort.Parcel.Read.System.Span.System.Byte..System.Double..'></a>

## Read(Span<byte>, out double)

Reads a double value from the specified buffer.

```csharp
public static int Read(Span<byte> buffer, out double value)
```
#### Parameters

`buffer` Span<byte>

The buffer to read from.

`value` double

The double value read from the buffer.

#### Returns

int

The number of bytes read.

<a name='TizenX.RPCPort.Parcel.Read.System.Span.System.Byte..System.Int16..'></a>

## Read(Span<byte>, out short)

Reads a short value from the specified buffer.

```csharp
public static int Read(Span<byte> buffer, out short value)
```
#### Parameters

`buffer` Span<byte>

The buffer to read from.

`value` short

The short value read from the buffer.

#### Returns

int

The number of bytes read.

<a name='TizenX.RPCPort.Parcel.Read.System.Span.System.Byte..System.Int32..'></a>

## Read(Span<byte>, out int)

Reads an integer value from the specified buffer.

```csharp
public static int Read(Span<byte> buffer, out int value)
```
#### Parameters

`buffer` Span<byte>

The buffer to read from.

`value` int

The integer value read from the buffer.

#### Returns

int

The number of bytes read.

<a name='TizenX.RPCPort.Parcel.Read.System.Span.System.Byte..System.Int64..'></a>

## Read(Span<byte>, out long)

Reads a long value from the specified buffer.

```csharp
public static int Read(Span<byte> buffer, out long value)
```
#### Parameters

`buffer` Span<byte>

The buffer to read from.

`value` long

The long value read from the buffer.

#### Returns

int

The number of bytes read.

<a name='TizenX.RPCPort.Parcel.Read.System.Span.System.Byte..System.Single..'></a>

## Read(Span<byte>, out float)

Reads a float value from the specified buffer.

```csharp
public static int Read(Span<byte> buffer, out float value)
```
#### Parameters

`buffer` Span<byte>

The buffer to read from.

`value` float

The float value read from the buffer.

#### Returns

int

The number of bytes read.

<a name='TizenX.RPCPort.Parcel.Read.System.Span.System.Byte..System.Span.System.Byte...'></a>

## Read(Span<byte>, out Span<byte>)

Reads a byte span from the specified buffer.

```csharp
public static int Read(Span<byte> buffer, out Span<byte> data)
```
#### Parameters

`buffer` Span<byte>

The buffer to read from.

`data` Span<byte>

The byte span read from the buffer.

#### Returns

int

The number of bytes read.

<a name='TizenX.RPCPort.Parcel.Read.System.Span.System.Byte..System.String..'></a>

## Read(Span<byte>, out string)

Reads a string value from the specified buffer.

```csharp
public static int Read(Span<byte> buffer, out string value)
```
#### Parameters

`buffer` Span<byte>

The buffer to read from.

`value` string

The string value read from the buffer.

#### Returns

int

The number of bytes read.

<a name='TizenX.RPCPort.Parcel.Read.System.Span.System.Byte..System.UInt32..'></a>

## Read(Span<byte>, out uint)

Reads a uint value from the specified buffer.

```csharp
public static int Read(Span<byte> buffer, out uint value)
```
#### Parameters

`buffer` Span<byte>

The buffer to read from.

`value` uint

The uint value read from the buffer.

#### Returns

int

The number of bytes read.

<a name='TizenX.RPCPort.Parcel.Read.System.Span.System.Byte...'></a>

## Read(out Span<byte>)

Reads a byte span from the parcel.

```csharp
public int Read(out Span<byte> data)
```
#### Parameters

`data` Span<byte>

The byte span read from the parcel.

#### Returns

int

The new read offset position.

<a name='TizenX.RPCPort.Parcel.Read.System.String..'></a>

## Read(out string)

Reads a string from the parcel.

```csharp
public int Read(out string data)
```
#### Parameters

`data` string

The string read from the parcel.

#### Returns

int

The new read offset position.

<a name='TizenX.RPCPort.Parcel.Read.TizenX.RPCPort.IParcelable.'></a>

## Read(IParcelable)

Reads a parcelable object from the parcel.

```csharp
public int Read(IParcelable parcel)
```
#### Parameters

`parcel` IParcelable

The IParcelable object to read into.

#### Returns

int

The new read offset position.

<a name='TizenX.RPCPort.Parcel.Read.TizenX.RPCPort.ParcelHeader.'></a>

## Read(ParcelHeader)

Reads a header from the parcel.

```csharp
public int Read(ParcelHeader header)
```
#### Parameters

`header` ParcelHeader

The ParcelHeader to read into.

#### Returns

int

The number of bytes read.

<a name='TizenX.RPCPort.Parcel.Read.TizenX.RPCPort.ParcelHeader.TizenX.RPCPort.IParcelable.System.Int32.'></a>

## Read(ParcelHeader, IParcelable, int)

Reads a header and a parcelable object from the parcel.

```csharp
public int Read(ParcelHeader header, IParcelable body, int offset = 0)
```
#### Parameters

`header` ParcelHeader

The ParcelHeader to read into.

`body` IParcelable

The IParcelable object to read into.

`offset` int

The offset to start reading from (default is 0).

#### Returns

int

The number of bytes read.

<a name='TizenX.RPCPort.Parcel.StringParcelSize.System.String.'></a>

## StringParcelSize(string)

Calculates the size of a string when serialized to a parcel.

```csharp
public static int StringParcelSize(string str)
```
#### Parameters

`str` string

The string to calculate the size for.

#### Returns

int

The size in bytes of the serialized string.

<a name='TizenX.RPCPort.Parcel.Write.System.Span.System.Byte..System.Boolean.'></a>

## Write(Span<byte>, bool)

Writes a boolean value to the specified buffer.

```csharp
public static int Write(Span<byte> buffer, bool value)
```
#### Parameters

`buffer` Span<byte>

The buffer to write to.

`value` bool

The boolean value to write.

#### Returns

int

The number of bytes written.

<a name='TizenX.RPCPort.Parcel.Write.System.Span.System.Byte..System.Byte.'></a>

## Write(Span<byte>, byte)

Writes a byte value to the specified buffer.

```csharp
public static int Write(Span<byte> buffer, byte value)
```
#### Parameters

`buffer` Span<byte>

The buffer to write to.

`value` byte

The byte value to write.

#### Returns

int

The number of bytes written.

<a name='TizenX.RPCPort.Parcel.Write.System.Span.System.Byte..System.Collections.Generic.List.System.Int32..'></a>

## Write(Span<byte>, List<int>)

Writes a list of integers to the specified buffer.

```csharp
public static int Write(Span<byte> buffer, List<int> data)
```
#### Parameters

`buffer` Span<byte>

The buffer to write to.

`data` List<int>

The list of integers to write.

#### Returns

int

The number of bytes written.

<a name='TizenX.RPCPort.Parcel.Write.System.Span.System.Byte..System.Collections.Generic.List.System.String..'></a>

## Write(Span<byte>, List<string>)

Writes a list of strings to the specified buffer.

```csharp
public static int Write(Span<byte> buffer, List<string> data)
```
#### Parameters

`buffer` Span<byte>

The buffer to write to.

`data` List<string>

The list of strings to write.

#### Returns

int

The number of bytes written.

<a name='TizenX.RPCPort.Parcel.Write.System.Span.System.Byte..System.Double.'></a>

## Write(Span<byte>, double)

Writes a double value to the specified buffer.

```csharp
public static int Write(Span<byte> buffer, double value)
```
#### Parameters

`buffer` Span<byte>

The buffer to write to.

`value` double

The double value to write.

#### Returns

int

The number of bytes written.

<a name='TizenX.RPCPort.Parcel.Write.System.Span.System.Byte..System.Int16.'></a>

## Write(Span<byte>, short)

Writes a short value to the specified buffer.

```csharp
public static int Write(Span<byte> buffer, short value)
```
#### Parameters

`buffer` Span<byte>

The buffer to write to.

`value` short

The short value to write.

#### Returns

int

The number of bytes written.

<a name='TizenX.RPCPort.Parcel.Write.System.Span.System.Byte..System.Int32.'></a>

## Write(Span<byte>, int)

Writes an integer value to the specified buffer.

```csharp
public static int Write(Span<byte> buffer, int value)
```
#### Parameters

`buffer` Span<byte>

The buffer to write to.

`value` int

The integer value to write.

#### Returns

int

The number of bytes written.

<a name='TizenX.RPCPort.Parcel.Write.System.Span.System.Byte..System.Int64.'></a>

## Write(Span<byte>, long)

Writes a long value to the specified buffer.

```csharp
public static int Write(Span<byte> buffer, long value)
```
#### Parameters

`buffer` Span<byte>

The buffer to write to.

`value` long

The long value to write.

#### Returns

int

The number of bytes written.

<a name='TizenX.RPCPort.Parcel.Write.System.Span.System.Byte..System.Single.'></a>

## Write(Span<byte>, float)

Writes a float value to the specified buffer.

```csharp
public static int Write(Span<byte> buffer, float value)
```
#### Parameters

`buffer` Span<byte>

The buffer to write to.

`value` float

The float value to write.

#### Returns

int

The number of bytes written.

<a name='TizenX.RPCPort.Parcel.Write.System.Span.System.Byte..System.Span.System.Byte..'></a>

## Write(Span<byte>, Span<byte>)

Writes a byte span to the specified buffer.

```csharp
public static int Write(Span<byte> buffer, Span<byte> data)
```
#### Parameters

`buffer` Span<byte>

The buffer to write to.

`data` Span<byte>

The byte span to write.

#### Returns

int

The number of bytes written.

<a name='TizenX.RPCPort.Parcel.Write.System.Span.System.Byte..System.String.'></a>

## Write(Span<byte>, string)

Writes a string value to the specified buffer.

```csharp
public static int Write(Span<byte> buffer, string value)
```
#### Parameters

`buffer` Span<byte>

The buffer to write to.

`value` string

The string value to write.

#### Returns

int

The number of bytes written.

<a name='TizenX.RPCPort.Parcel.Write.System.Span.System.Byte..System.UInt32.'></a>

## Write(Span<byte>, uint)

Writes a uint value to the specified buffer.

```csharp
public static int Write(Span<byte> buffer, uint value)
```
#### Parameters

`buffer` Span<byte>

The buffer to write to.

`value` uint

The uint value to write.

#### Returns

int

The number of bytes written.

<a name='TizenX.RPCPort.Parcel.Write.TizenX.RPCPort.ParcelHeader.System.Collections.Generic.IEnumerable.TizenX.RPCPort.IParcelable..'></a>

## Write(ParcelHeader, IEnumerable<IParcelable>)

Writes a header and multiple parcelable objects to the parcel.

```csharp
public int Write(ParcelHeader header, IEnumerable<IParcelable> parcels)
```
#### Parameters

`header` ParcelHeader

The ParcelHeader to write.

`parcels` IEnumerable<IParcelable>

The collection of IParcelable objects to write.

#### Returns

int

The total size of the written data in bytes.

<a name='TizenX.RPCPort.Parcel.Write.TizenX.RPCPort.ParcelHeader.TizenX.RPCPort.IParcelable.'></a>

## Write(ParcelHeader, IParcelable)

Writes a header and a single parcelable object to the parcel.

```csharp
public int Write(ParcelHeader header, IParcelable body)
```
#### Parameters

`header` ParcelHeader

The ParcelHeader to write.

`body` IParcelable

The IParcelable object to write.

#### Returns

int

The total size of the written data in bytes.

<a name='TizenX.RPCPort.Parcel.WriteToPort.System.IntPtr.'></a>

## WriteToPort(nint)

Writes the parcel data to an RPC port handle.

```csharp
public void WriteToPort(nint handle)
```
#### Parameters

`handle` nint

The IntPtr handle to the RPC port.

<a name='TizenX.RPCPort.Parcel.Write..1.System.Span.System.Byte....0.'></a>

## Write<T>(Span<byte>, T)

Writes a generic struct value to the specified buffer.

```csharp
public static int Write<T>(Span<byte> buffer, T value) where T : struct
```
#### Parameters

`buffer` Span<byte>

The buffer to write to.

`value` T

The struct value to write.

#### Returns

int

The number of bytes written.

