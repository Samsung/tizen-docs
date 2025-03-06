# Tizen Core Channel

Tizen Core channel Provides a communication channel that allows safe sending and receiving of data between threads. This channel can be used to exchange information in a synchronized state without data conflict. This page describes how to create a channel sender and receiver pair, send and receive data, and destroy the channel sender and receiver pair.

## Preparation
o use the methods and properties of the [Tizen.Core.Channel](/application/dotnet/api/TizenFX/latest/api/Tizen.Core.Channel.html) and [Tizen.Core.Task](/application/dotnet/api/TizenFX/latest/api/Tizen.Core.Task.html) classes, include the [Tizen.Core](/application/dotnet/api/TizenFX/latest/api/Tizen.Core.html) namespace in your application:

```csharp
using Tizen.Core;
```

## Managing channel sender and receiver pairs
### Creating a channel
Here's an example on how to create a `Tizen.Core.Channel` object:
```csharp
try
{
    var channel = new Channel();
}
catch (OutOfMemoryException)
{
    Log.Error(LogTag, "OutOfMemoryException occurs");
}
catch (InvalidOperationException)
{
    Log.Error(LogTag, "InvalidOperationException occurs");
}
```
You must release the `channel`instance by using `Tizen.Core.Channel.Dispose()` method respectively when it's no longer needed.

### Creating and transmitting a channel object
This example shows how to create and transmit a channel object:
```csharp
{
    int id =1;
    string message = "message";
    ChannelObject channelObject = null;
    try
    {
        channelObject = new ChannelObject(id++, message);
        channel.Sender.Send(channelObject);
    }
    catch (OutOfMemoryException)
    {
        Log.Error(LogTag, "OutOfMemoryException occurs");
    }
    catch (InvalidOperationException)
    {
        Log.Error(LogTag, "InvalidOperationException occurs");
    }
}
```
You must release the `channelObject` instance by using `Tizen.Core.ChannelObject.Dispose()` method when it's no longer needed.

### Creating a task for receiving objects
This example creates a task that adds the `Tizen.Core.ChannelSender` to receive channel objects:
```csharp
var task = TizenCore.Spawn("ChannelReceiver+");
var channel = new Channel();
var receiver = channel.Receiver;
receiver.Received += (s, e) => {
    Log.Debug(LogTag, "Received Message = " + (string)e.Data);
};

task.AddChannelReceiver(receiver);
```
You must call `Tizen.Core.Task.RemoveChannelReceiver()` method to remove the source when it is no longer needed.
In this example, the task's loop runs on a thread, and `Tizen.Core.ChannelReceiver.Received` is delivered to the thread's loop.

You can receive channel objects using the receiver instance as shown below:
```csharp
var channel = new Channel();
var task = TizenCore.Find("ChannelReceiver+");
task.Send(async () => {
    var channelObject = await channel.Receiver.Receive();
    Log.Debug(LogTag, "Received Message = " + (string)channelObject.Data);
    channelObject.Dispose();
});
```
The `await channel.Receiver.Receive()` blocks indefinitely if there is no data being transmitted. It is recommended to use it in situations where the sender sends data reliably.
After receiving the object, its ownership is transferred to the receiving party, so you must release it by calling the `Tizen.Core.ChannelObject.Dispose()`.

## Related information
- Dependencies
  - Tizen 9.0
- API Reference
  - [Tizen.Core.Channel](/application/dotnet/api/TizenFX/latest/api/Tizen.Core.Channel.html) class
  - [Tizen.Core.ChannelObject](/application/dotnet/api/TizenFX/latest/api/Tizen.Core.ChannelObject.html) class
  - [Tizen.Core.ChannelReceiver](/application/dotnet/api/TizenFX/latest/api/Tizen.Core.ChannelReceiver.html) class
  - [Tizen.Core.ChannelSender](/application/dotnet/api/TizenFX/latest/api/Tizen.Core.ChannelSender.html) class
