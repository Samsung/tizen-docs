# Tizen Core Event

A feature to deliver events to specific tasks, which can be used to wait for completion of tasks or send notifications to other threads. This page covers creating events, registering event handlers with them, attaching them to the main loop, and receiving events.

## Preparation
To use the Tizen Core event API, you must include the `tizen_core.h` header:
```c
#include <tizen_core.h>
```

## Managing Tizen Core events
### Creating an event handle and registering an event handler
Here's an example of creating an event and registering an event handler:
```c
static bool event_handler_cb(tizen_core_event_object_h object, void *user_data)
{
  return true;
}

static tizen_core_source_h add_event(void)
{
  tizen_core_event_h event = NULL;
  tizen_core_event_handler_h handler = NULL;
  int ret;
  
  ret = tizen_core_event_create(&event);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to create event. error=%d", ret);
	return NULL;
  }
  
  ret = tizen_core_event_add_handler(event, event_handler_cb, NULL, &handler);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to add event handler. error=%d", ret);
	tizen_core_event_destroy(event);
	return NULL;
  }
  
  return source;
}
```
An event handler has been added to the created event. To remove the event handler from the event, use `tizen_core_event_remove_handler()`.
When you no longer need `tizen_core_event_h`, call `tizen_core_event_destroy()` to destroy it.

### Registering the event with Tizen Core
This example uses `tizen_core_add_event()` to register an event with Tizen Core:
```c
{
  tizen_core_source_h source = NULL;
  tizen_core_h core = NULL;
  int ret;


  ret = tizen_core_find_from_this_thread(&core);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to find core from this thread. error=%d", ret);
	return;
  }
  
  
  ret = tizen_core_add_event(core, event, &source);
  if (ret != TIZEN_CORE_ERROR_NONE) {
	dlog_print(DLOG_ERROR, LOG_TAG, "Failed to add event to core. error=%d", ret);
	return;
  }

  // ...
}
```
When you pass `tizen_core_event_h` to `tizen_core_h` via `tizen_core_add_event()`, `tizen_core_source_h` is returned. Use `tizen_core_remove_source()` to remove `tizen_core_source_h`, which will also remove `tizen_core_event_h`.
Once you call `tizen_core_add_event()`, the ownership of `tizen_core_event_h` transfers to `tizen_core_h`.

### Creating an event object and delivering it to Tizen Core
This example demonstrates creating an event object and delivering it to Tizen Core:
```c
static void event_object_destroy_cb(void *event_data, void *user_data)
{
  char *data = (char *)event_data);
  
  free(data);
}

static tizen_core_event_object_h create_event_object(int id, void *data)
{
  tizen_core_event_object_h object = NULL;
  int ret;
  
  ret = tizen_core_event_object_create(&object, id, data);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to create event object. error=%d", ret);
	return NULL;
  }
  
  ret = tizen_core_event_object_set_destroy_cb(object, event_object_destroy_cb, NULL);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to set destroy cb. error=%d", ret);
	tizen_core_event_object_destroy(object);
	return NULL;
  }
  
  return object;
}

static int emit_event(int id, void *data)
{
  tizen_core_h core = NULL;
  tizen_core_event_object_h object = NULL;
  int ret;
  
  ret = tizen_core_find_from_this_thread(&core);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to find tizen core from this thread");
	free(data);
	return -1;
  }
  
  object = create_event_object(id, data);
  if (object == NULL)
    return -1;

  ret = tizen_core_emit_event(core, event);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to emit event. error=%d", ret);
	tizen_core_event_object_destroy(object);
	return -1;
  }
  
  return 0;
}
```
After calling `tizen_core_emit_event()`, the ownership of the created event object moves to Tizen Core. It is delivered to all registered event handlers and automatically released by the Tizen Core.
If you want to deliver `tizen_core_event_object_h` only to a specific `tizen_core_event_h`, use `tizen_core_event_emit()` instead.

## Related Information
- Dependencies
  - Tizen 9.0
- API Reference
  - [Tizen Core Event](../../../api/common/latest/group__CAPI__TIZEN__CORE__EVENT__MODULE.html)
