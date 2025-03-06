# Tizen Core

Tizen Core is a new main loop that improves the existing main loop model. It supports creating and running the main loop in multiple threads.
Tizen Core provides an API that supports secure communication between threads.

The following are functions provided by Tizen Core for inter-thread communication and event delivery.
 - **[Tizen Core Channel](./tizen-core-channel.md)**: Provides a thread-safe communication method between threads.
 - **[Tizen Core Event](./tizen-core-event.md)**: Provides the ability to deliver events to specific tasks.

## Preparation

To use the methods and properties of the [Tizen.Core.TizenCore](/application/dotnet/api/TizenFX/latest/api/Tizen.Core.TizenCore.html) and [Tizen.Core.Task](/application/dotnet/api/TizenFX/latest/api/Tizen.Core.Task.html) classes, include the [Tizen.Core](/application/dotnet/api/TizenFX/latest/api/Tizen.Core.html) namespace in your application:

```csharp
using Tizen.Core;
```

## Initializing Tizen Core
Before using Tizen Core, Call `TizenCore.Initialize()` as shown below:

```csharp
TizenCore.Initialize();
```

## Shutting down Tizen Core
When Tizen Core is no longer needed, shut down Tizen Core with the code below:
```csharp
TizenCore.Shutdown();
```

## Managing Tizen Core tasks
This section will cover creating, executing, and terminating `Tizen.Core.Task` objects. It will also cover obtaining `Tizen.Core` from `Tizen.Core.Task` and adding idle jobs using `Tizen.Core.Task.Post()` method, timers, and sources to the main loop.

### Creating a task
Here's an example on how to create a `Tizen.Core.Task` object:
```csharp
var task = TizenCore.Spawn("worker");
```
`Tizen.Core.Task` was created with the name "task" and configured to use its own thread.
The created `task` handle should be removed using `Tizen.Core.Task.Dispose()` method when it is no longer needed.


### Running a task
In this example, we'll cover the code to execute a previously created task using `Tizen.Core.Task.Run()`:
```csharp
task.Run();
```
`Tizen.Core.Task` creates and runs a thread named "task". After calling `Tizen.Core.Task.Run()`, the thread is created and the loop starts running.

### Checking if a task is running
An example of checking if a task is running using `Tizen.Core.Task.Running`:
```csharp
if (task.Running)
{
    Log.Debug(LogTag, "Task is running");
}
else
{
    Log.Debug(LogTag, "Task is not running");
}
```
If the task is running, the log message "Task is running" is printed using dlog.

### Exiting a task
An example of exiting a running task:
```csharp
if (task.Running)
{
    task.Quit();
}
```
In this example, the `task` checks if it is running before exiting. When `Tizen.Core.Task.Quit()` method is called, the loop ends and the created thread is cleaned up.

### Getting the task instance
A `Tizen.Core.Task` can also be found by ID. The next example shows how to find the `Tizen.Core.Task` created earlier with the ID "worker":
```csharp
var task = TizenCore.Find("worker");
if (task == null)
{
    Log.Error(LogTag, "Failed to find task from ID('worker')");
}
```

You can obtain the Tizen Core information of the current thread through the API by using the following code:
```csharp
var task = TizenCore.FindFromCurrentThread();
```
If there is no `Tizen.Core.Task` running in the current thread, the function returns the `Tizen.Core.Task` running in the main thread.

## Adding an idle job to the task
Let's write an example that adds an idle job to `Tizen.Core.Task` and removes the job again when the callback is called.
```csharp
var task = TizenCore.FindFromCurrentThread();
if (task != null)
{
    task.Post(() => {
        Log.Debug(LogTag, "idler is invoked");
    });
}
```

## Adding a timer to the task
Here's an example of registering a timer that calls the callback every 100 ms.
```csharp
var task = TizenCore.FindFromCurrentThread();
var timerId = task.AddTimer(100, () => {
    Log.Debug(LogTag, "Timer is invoked");
});
```
If the registered timer source is no longer needed, you should remove it by calling `Tizen.Core.Task.RemoveTimer()` with the `timerId`.

## Related information
- Dependencies
  - Tizen 9.0
- API Reference
  - [Tizen.Core.TizenCore](/application/dotnet/api/TizenFX/latest/api/Tizen.Core.TizenCore.html) class
  - [Tizen.Core.Task](/application/dotnet/api/TizenFX/latest/api/Tizen.Core.Task.html) class

