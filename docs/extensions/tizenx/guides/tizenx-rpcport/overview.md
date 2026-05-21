# TizenX.RPCPort

## Overview

X-RPC-Port is an optimized version of Tizen's existing RPC-PORT for .NET. While following the basic architecture of RPC-PORT, it has been modified to work more efficiently when used in .NET environments. This library provides an efficient data serialization and transmission mechanism for inter-process communication (IPC) on the Tizen platform.

## 📦 Installation

### Manual Reference

#### .NET CLI

```sh
> dotnet add package TizenX.RPCPort --version 1.0.0
```

#### PackageReference

```xml
<PackageReference Include="TizenX.RPCPort" Version="1.0.0" />
```

## XRPC Sample Apps

Visit [TizenX.RPCPort](https://github.sec.samsung.net/qad/TizenX.RPCPort) to take a look at the test appication and [learn how to run](https://github.sec.samsung.net/qad/TizenX.RPCPort) them.


## 🚀 XRPC Migration Guide

The new TizenX.RPCPort has different usage patterns compared to the existing Tizen RPC-Port. 
This guide explains how to modify legacy code generated from TIDL files to work with the new XRPC library. The changes primarily involve updating serialization/deserialization mechanisms and adapting to the new parcel system.

## Overview of Changes

The main differences between legacy code and XRPC-compatible code are:
1. Implementation of the `IParcelable` interface for data classes
2. Use of `Parcel` and `ParcelHeader` from `TizenX.RPCPort`
3. Adoption of `ParcelBuilder` for constructing parcels
4. Removal of static serialization/deserialization methods

## Step-by-Step Migration Process

### 1. Update Namespace and Using Statements

**Legacy Code:**
```csharp
using Tizen.Applications.RPCPort;
```

**New Code:**
```csharp
using Tizen.Applications.RPCPort;
using TizenX.RPCPort;
using XParcel = TizenX.RPCPort.Parcel;
using XParcelHeader = TizenX.RPCPort.ParcelHeader;
```

### 2. Implement IParcelable Interface for Data Classes

**Legacy Code:**
```csharp
public sealed class Message
{
    public List<int> Values { get; set; }
    public List<string> Lines { get; set; }

    public Message()
    {
    }
}
```

**New Code:**
```csharp
public sealed class Message : IParcelable
{
    public List<int> Values { get; set; }
    public List<string> Lines { get; set; }

    // Required property for IParcelable
    // Provides the size of data that will be written to Parcel
    public int DataSize => XParcel.ListParcelSize(Values) + XParcel.ListParcelSize(Lines);

    public Message()
    {
    }

    // Required method for IParcelable
    public int WriteTo(Span<byte> bytes)
    {
        int written = 0;
        var nextBytes = bytes[written..];
        written += XParcel.Write(nextBytes, Values);
        nextBytes = bytes[written..];
        written += XParcel.Write(nextBytes, Lines);
        return written;
    }

    // Required method for IParcelable
    public int ReadFrom(Span<byte> bytes)
    {
        int readn = 0;
        var nextBytes = bytes[readn..];
        readn += XParcel.Read(nextBytes, out List<int> intdata);
        Values = intdata;
        nextBytes = bytes[readn..];
        readn += XParcel.Read(nextBytes, out List<string> strData);
        Lines = strData;
        return readn;
    }
}
```

### 3. Update CallbackBase Class

**Legacy Code:**
```csharp
public abstract class CallbackBase
{
    internal int Id;
    internal int SeqId;
    internal bool Once;
    private static volatile int _seqNum = 0;

    public string Tag
    {
        get
        {
            return Id.ToString() + "::" + SeqId.ToString();
        }
    }

    public CallbackBase(int delegateId, bool once)
    {
        Id = delegateId;
        SeqId = _seqNum++;
        Once = once;
    }

    internal virtual void OnReceivedEvent(Parcel p) { }

    internal static void Serialize(Parcel h, CallbackBase param)
    {
        h.WriteInt(param.Id);
        h.WriteInt(param.SeqId);
        h.WriteBool(param.Once);
    }

    internal static void Deserialize(Parcel h, CallbackBase param)
    {
        param.Id = h.ReadInt();
        param.SeqId = h.ReadInt();
        param.Once = h.ReadBool();
    }
}
```

**New Code:**
```csharp
public abstract class CallbackBase : IParcelable
{
    internal int Id;
    internal int SeqId;
    internal bool Once;
    private static volatile int _seqNum = 0;

    public string Tag
    {
        get
        {
            return Id.ToString() + "::" + SeqId.ToString();
        }
    }

    // Required property for IParcelable
    // Provides the size of data that will be written to Parcel
    public int DataSize => sizeof(int) + sizeof(int) + sizeof(byte);

    public CallbackBase(int delegateId, bool once)
    {
        Id = delegateId;
        SeqId = _seqNum++;
        Once = once;
    }

    internal virtual void OnReceivedEvent(XParcel p) { }

    // Required method for IParcelable
    public int WriteTo(Span<byte> bytes)
    {
        int written = 0;
        var nextByte = bytes[written..];
        written += XParcel.Write(nextByte, Id);
        nextByte = bytes[written..];
        written += XParcel.Write(nextByte, SeqId);
        nextByte = bytes[written..];
        written += XParcel.Write(nextByte, Once);
        return written;
    }

    // Required method for IParcelable
    public int ReadFrom(Span<byte> bytes)
    {
        int readn = 0;
        var nextByte = bytes[readn..];
        readn += XParcel.Read(nextByte, out Id);
        nextByte = bytes[readn..];
        readn += XParcel.Read(nextByte, out SeqId);
        nextByte = bytes[readn..];
        readn += XParcel.Read(nextByte, out Once);
        return readn;
    }
}
```

### 4. Remove Static Serialization/Deserialization Methods

**Legacy Code:**
```csharp
private static void Serialize(Parcel h, Message param)
{
    Serialize(h, param.Values);
    Serialize(h, param.Lines);
}

private static void Deserialize(Parcel h, Message param)
{
    param.Values = new List<int>();
    Deserialize(h, param.Values);
    param.Lines = new List<string>();
    Deserialize(h, param.Lines);
}

private static void Serialize(Parcel h, List<int> param)
{
    h.WriteArrayCount(param.Count);
    foreach (var i in param)
    {
        h.WriteInt(i);
    }
}

private static void Deserialize(Parcel h, List<int> param)
{
    var v = h.ReadInt();
    param.Add(v);
}

private static void Serialize(Parcel h, List<string> param)
{
    h.WriteArrayCount(param.Count);
    foreach (var i in param)
    {
        h.WriteString(i);
    }
}

private static void Deserialize(Parcel h, List<string> param)
{
    var v = h.ReadString();
    param.Add(v);
}
```

**New Code:**
These methods are completely removed as the functionality is now handled by the `IParcelable` interface implementations.

### 5. Update Parcel Operations in Methods

**Legacy Code (Send method):**
```csharp
public int Send(Message msg)
{
    if (!_online)
        throw new NotConnectedSocketException();

    using (Parcel p = new Parcel())
    {
        ParcelHeader header = p.GetHeader();
        header.SetTag(_tidlVersion);
        p.WriteInt((int)MethodId.Send);
        Serialize(p, msg);

        lock (_lock)
        {
            // Send
            p.Send(Port);
        }

        Parcel parcelReceived;
        bool done = false;
        do
        {
            lock (_lock)
            {
                // Receive
                ConsumeCommand(out parcelReceived, Port);
            }

            if (parcelReceived == null)
            {
                throw new InvalidProtocolException();
            }

            ParcelHeader headerReceived = parcelReceived.GetHeader();
            if (!string.IsNullOrEmpty(headerReceived.GetTag()))
            {
                if (headerReceived.GetSequenceNumber() != header.GetSequenceNumber())
                {
                    parcelReceived.Dispose();
                    parcelReceived = null;
                }
            }

            if (parcelReceived != null)
                done = true;
        }
        while (!done);

        int ret = parcelReceived.ReadInt();
        parcelReceived.Dispose();
        return ret;
    }
}
```

**New Code (Send method):**
```csharp
public int Send(Message msg)
{
    if (!_online)
        throw new NotConnectedSocketException();

    lock (_lock)
    {
        XParcelHeader header = new()
        {
            Tag = _tidlVersion,
            SequenceNumber = ++_sequenceNumber
        };
        new ParcelBuilder()
            .Add((int)MethodId.Send)
            .Add(msg)
            .Build(header, _parcelForMethod);

        _parcelForMethod.WriteToPort(XParcel.GetHandle(Port));

        var receivedHeader = ConsumeCommand(_parcelForMethod, Port);

        if (receivedHeader.SequenceNumber != header.SequenceNumber)
        {
            throw new InvalidOperationException("Error on parcel sequence number");
        }

        _parcelForMethod.Read(out int ret);
        return ret;
    }
}
```

### 6. Update Event Handling Methods

**Legacy Code:**
```csharp
private void ProcessReceivedEvent(Parcel parcel)
{
    int id = parcel.ReadInt();
    int seqId = parcel.ReadInt();
    bool once = parcel.ReadBool();

    foreach (var i in _delegateList)
    {
        if ((int)i.Id == id && i.SeqId == seqId)
        {
            i.OnReceivedEvent(parcel);
            if (i.Once)
                _delegateList.Remove(i);
            break;
        }
    }
}

protected override void OnReceivedEvent(string endPoint, string portName)
{
    Parcel parcelReceived;

    try
    {
        parcelReceived = new Parcel(CallbackPort);
    }
    catch (InvalidIOException)
    {
        return;
    }

    using (parcelReceived)
    {
        int cmd = parcelReceived.ReadInt();
        if (cmd != (int)MethodId.__Callback)
        {
            return;
        }

        ProcessReceivedEvent(parcelReceived);
    }
}
```

**New Code:**
```csharp
private void ProcessReceivedEvent(XParcel parcel)
{
    parcel.Read(out int id);
    parcel.Read(out int seqId);
    parcel.Read(out bool once);

    foreach (var i in _delegateList)
    {
        if ((int)i.Id == id && i.SeqId == seqId)
        {
            i.OnReceivedEvent(parcel);
            if (i.Once)
                _delegateList.Remove(i);
            break;
        }
    }
}

protected override void OnReceivedEvent(string endPoint, string portName)
{
    XParcel parcel = new XParcel();

    try
    {
        parcel.LoadFromPort(XParcel.GetHandle(CallbackPort));
    }
    catch (InvalidIOException)
    {
        return;
    }

    XParcelHeader header = new XParcelHeader();
    parcel.Read(header);
    parcel.Read(out int cmd);
    if (cmd != (int)MethodId.__Callback)
    {
        return;
    }
    ProcessReceivedEvent(parcel);
}
```

### 7. Update Command Consumption

**Legacy Code:**
```csharp
private void ConsumeCommand(out Parcel parcel, Port port)
{
    do
    {
        Parcel p;

        try
        {
            p = new Parcel(port);
        }
        catch (InvalidIOException)
        {
            parcel = null;
            return;
        }

        int cmd = p.ReadInt();
        if (cmd == (int)MethodId.__Result)
        {
            parcel = p;
            return;
        }

        p.Dispose();
        parcel = null;
    } while (true);
}
```

**New Code:**
```csharp
private XParcelHeader ConsumeCommand(XParcel parcel, Port port)
{
    parcel.LoadFromPort(XParcel.GetHandle(port));

    XParcelHeader header = new XParcelHeader();
    parcel.Read(header);
    parcel.Read(out int cmd);

    if (cmd != (int)MethodId.__Result)
    {
        throw new InvalidOperationException("Error on RPC return value");
    }
    return header;
}
```

## Key Points to Remember

1. **IParcelable Interface**: All data classes must implement `IParcelable` with `DataSize`, `WriteTo`, and `ReadFrom` methods.
2. **Parcel Types**: Replace `Tizen.Applications.RPCPort.Parcel` with `TizenX.RPCPort.Parcel` and `Tizen.Applications.RPCPort.ParcelHeader` with `TizenX.RPCPort.ParcelHeader`.
3. **Serialization**: Remove static serialize/deserialize methods; use `IParcelable` implementation instead.
4. **Parcel Building**: Use `ParcelBuilder` to construct parcels instead of manual operations.
5. **Port Operations**: Use `XParcel.GetHandle()` and `WriteToPort()`/`LoadFromPort()` methods.
6. **Sequence Numbers**: Implement proper sequence number handling for request/response correlation.

## Example: Complete Class Migration

Here's a complete example showing how a simple data class should be migrated:

**Before:**
```csharp
public class Person
{
    public string Name { get; set; }
    public int Age { get; set; }
}
```

**After:**
```csharp
public class Person : IParcelable
{
    public string Name { get; set; }
    public int Age { get; set; }

    // Provides the size of data that will be written to Parcel
    public int DataSize => XParcel.StringParcelSize(Name) + sizeof(int);

    public int WriteTo(Span<byte> bytes)
    {
        int written = 0;
        var nextBytes = bytes[written..];
        written += XParcel.Write(nextBytes, Name);
        nextBytes = bytes[written..];
        written += XParcel.Write(nextBytes, Age);
        return written;
    }

    public int ReadFrom(Span<byte> bytes)
    {
        int readn = 0;
        var nextBytes = bytes[readn..];
        readn += XParcel.Read(nextBytes, out Name);
        nextBytes = bytes[readn..];
        readn += XParcel.Read(nextBytes, out Age);
        return readn;
    }
}
```