# Event Handling

EFL relies on events and callbacks. In case of an event, such as a key press, mouse click, or a battery running low, the main loop calls the callback functions that are associated with that specific event. After the callbacks have finished, the main loop takes over and waits for new events, upon which to trigger new callbacks.

It is important to do light work in the callbacks and to return to the main loop relatively quickly. If there is heavy work to do, use an asynchronous mechanism, such as `Ecore_con` for network I/O, or threads for CPU-intensive tasks. Failing to return quickly to the main loop blocks the application UI and makes it appear frozen.

## EFL Event Types

There are several event types in EFL, and their use depends on the level of the event. The event types from the lowest to the highest level are:

- [Ecore events](./event-types.md#ecore-events) are the lowest-level events and come directly from the system. Except for application-wide shortcuts, it is not advisable to use them.
- [Evas events](./event-types.md#evas-events) are events on the graphical canvas as a whole. They are fairly low-level and mostly useful when drawing directly on the canvas.
- [Evas object events](./event-types.md#evas-object-events) concern the objects that are on the canvas. You can also implement [multi-point touch events](./multipoint-touch.md) for Evas objects.
- [Evas smart events](./event-types.md#evas-smart-object-events) are the most often used and take place on collections of Evas objects. They are called "smart", because they have an internal logic and can define their own events, while the other event types are fixed.

**Figure: Event types in the EFLs**

![Event types in the EFLs](./media/events_scope.png)

> **Note**	  
> There are also [Edje signals](./event-types.md#edje-events), which come from program blocks in the theme EDC files. They can be used from the high level Elementary APIs or the low level Edje APIs.

## Basic Event Flow

A realistic scenario involving various types of events is an application showing a button, which triggers the download of a file to be processed. There are progress bars for the operations.

The following steps are involved in the above basic event flow:

1. Create a window and box, set the box to be vertical, and add a button and 2 progress bars. At first, only the button is fully visible.

2. When the user clicks the button, an Evas smart object event named `clicked` is emitted.

3. The callback for the `clicked` event starts the download in `Ecore_con`, displays the first progress bar, and adds a callback to monitor the download progress. When the download progress changes, the callback updates the progress bar.

4. After the download is finished, the second progress bar is displayed and the file processing is offloaded to another thread through the `Ecore_thread`. The processing function regularly updates the progress bar, which wrapped in the `ecore_main_loop_thread_safe_call_async()` function because GUI operations are not thread-safe.

Events enable operations taking more than a few milliseconds' time to be executed outside of the main loop, therefore not blocking UI redraws.

The following figure illustrates the event flow that follows a click on the screen.

**Figure: Event flow for a user click**

![Event flow for a user click](./media/events_flow.png)

> **Note**  
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
