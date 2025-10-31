# Tracer

You can use tracepoints in Tizen .NET applications with the T-trace tool. The tool allows you to generate traces and visualize them.

The main features of the `Tizen.Tracer` class include followings:

-   Trace creation

    You can create custom [tracepoints](#insert) in your .NET application with Tizen.Tracer.

**Figure1: T-trace architecture**

![T-trace architecture](/application/native/guides/performance/media/trace.png)

## Prerequisites

To use the methods of [Tizen.Tracer](/application/dotnet/api/TizenFX/master/api/Tizen.Tracer.html), you should include the [Tizen](/application/dotnet/api/TizenFX/master/api/Tizen.html) namespace in your application:

```csharp
using Tizen;
```

<a name="tracer"></a>
## Put traces in the common trace buffer

A trace is defined by two API calls: [Begin](/application/dotnet/api/TizenFX/master/api/Tizen.Tracer.html#Tizen_Tracer_Begin_System_String_) and [End](/application/dotnet/api/TizenFX/master/api/Tizen.Tracer.html#Tizen_Tracer_End), or [AsyncBegin](/application/dotnet/api/TizenFX/master/api/Tizen.Tracer.html#Tizen_Tracer_AsyncBegin_System_Int32_System_String_) and [AsyncEnd](/application/dotnet/api/TizenFX/master/api/Tizen.Tracer.html#Tizen_Tracer_AsyncEnd_System_Int32_System_String_).

Here are examples:
  * Use synchronous tracing.

    If the trace event starts and ends in a same context within the same process, thread, and function, use `Begin` and `End` functions to track the event. Note that every `Begin` matches up with `End` that occurs after it.
    ```csharp
    void
    function()
    {
        Begin("event");
        // Something to do
        End();
    }
    ```

  * Use asynchronous tracing.

    If the trace event starts and ends in a different context (e.g., different threads), use `AsyncBegin` and `AsyncEnd` to track the event. Note that every `AsyncBegin` matches with `AsyncEnd` by using a name and a cookie. As a cookie provides an identifier among events, it must have a unique interger value.

    ```csharp
    // Use asynchronous tracing
    int cookie = 1;

    void
    function1()
    {
        trace_async_begin(cookie, "event");
    }

    void
    function2()
    {
        trace_async_end(cookie, "event);
    }
    ```

  * Track changes of an integer counter.

   If you want to track changes of an integer counter of your program in the trace, use [TraceValue](/application/dotnet/api/TizenFX/master/api/Tizen.Tracer.html#Tizen_Tracer_TraceValue_System_Int32_System_String_).

   ```csharp
   void
   function()
   {
     int counter = 0;

     // Something to do...

     TraceValue(counter, "event");
   }
   ```

## Related information
* Dependencies
  -    Since Tizen 6.5

