# Tizen Core Event

A feature to deliver events to specific tasks, which can be used to wait for completion of tasks or send notifications to other threads. This page covers creating events, registering event handlers with them, attaching them to the main loop, and receiving events.

## Preparation
To use the methods and properties of the [Tizen.Core.Event](/application/dotnet/api/TizenFX/latest/api/Tizen.Core.Event.html) and [Tizen.Core.Task](/application/dotnet/api/TizenFX/latest/api/Tizen.Core.Task.html) classes, include the [Tizen.Core](/application/dotnet/api/TizenFX/latest/api/Tizen.Core.html) namespace in your application:

```csharp
using Tizen.Core;
```

## Managing Tizen Core events
### Creating an event object and registering an event handler
Here's an example of creating an event and registering an event handler:
```csharp
var coreEvent = new Event();
coreEvent.EventReceived += (s, e) => {
    Log.Debug(LogTag, "Received Event. Message = " + (string)e.Data);
};
```
An event handler has been added to the created event.
When you no longer need `Tizen.Core.Event`, call `Tizen.Core.Event.Dispose()` to release it.

### Registering the event with the task
This example uses `Tizen.Core.Task.AddEvent()` to register an event with Tizen Core:
```csharp

var task = TizenCore.FindFromCurrentThread();
task.AddEvent(coreEvent);
```
When you no longer need the registered `Tizen.Core.Event`, call `Tizen.Core.Task.RemoveEvent()` to release it.

### Creating an event object and delivering it to the task
This example demonstrates creating an event object and delivering it to the task:
```csharp
var coreEvent = new Event();
coreEvent.EventReceived += (s, e) => {
    Log.Debug(LogTag, "Received Event. Message = " + (string)e.Data);
};

var task = TizenCore.FindFromCurrentThread();
if (!task.Running)
{
    task.Run();
}
task.AddEvent(coreEvent);

int id = 1;
string message = "Event Message";
using (var eventObject = new EventObject(id++, message))
{
    task.EmitEvent(eventObject);
}

```
If you want to deliver `Tizen.Core.EventObject` only to a specific `Tizen.Core.Event`, use `Tizen.Core.Event.Emit()` method instead.

## Related information
- Dependencies
  - Tizen 9.0
- API Reference
  - [Tizen.Core.Event](/application/dotnet/api/TizenFX/latest/api/Tizen.Core.Event.html) class
  - [Tizen.Core.EventObject](/application/dotnet/api/TizenFX/latest/api/Tizen.Core.EventObject.html) class
