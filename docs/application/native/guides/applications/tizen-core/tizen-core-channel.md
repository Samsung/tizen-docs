# Tizen Core Channel

Tizen Core channel Provides a communication channel that allows safe sending and receiving of data between threads. This channel can be used to exchange information in a synchronized state without data conflict. This page describes how to create a channel sender and receiver pair, send and receive data, and destroy the channel sender and receiver pair.

## Preparation
To use the Tizen Core channel API, you must include the `tizen_core.h` header.
```c
#include <tizen_core.h>
```

## Managing channel sender and receiver pairs
### Creating channel sender and receiver pairs
Use `tizen_core_channel_make_pair()` to create a channel sender and receiver pair.
```c
{
  tizen_core_channel_sender_h sender = NULL;
  tizen_core_channel_receiver_h receiver = NULL;
  int ret;

  ret = tizen_core_channel_make_pair(&sender, &receiver);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to create channel pair. error=%d", ret);
  return;
  }
}
```
You must destroy the `sender` and `receiver` handles by calling `tizen_core_channel_sender_destroy()` and `tizen_core_channel_receiver_destroy()` respectively when they are no longer needed.

### Creating and transmitting a channel object
This example shows how to create and transmit a channel object:
```c
{
  tizen_core_channel_object_h object = NULL;
  char *str;
  int ret;

  ret = tizen_core_channel_object_create(&object);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to create channel object. error=%d", ret);
    return;
  }

  ret = tizen_core_channel_object_set_id(object, 99);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to set id to channel object. error=%d", ret);
    tizen_core_channel_object_destroy(object);
    return;
  }

  str = strdup("channel_test");
  ret = tizen_core_channel_object_set_data(object, str);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to set data to channel object. error=%d", ret);
    free(str);
    tizen_core_channel_object_destroy(object);
    return;
  }

  ret = tizen_core_channel_sender_send(sender, object);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to send channel object. error=%d", ret);
    free(str);
    tizen_core_channel_object_destroy(object);
    return;
  }
}
```
The `receiver` receives the `object` and destroys it after use by calling `tizen_core_channel_object_destroy()`. If the object's data was allocated memory, you need to release it appropriately. In this example, we allocate a string using `strdup()` and release it using `free()` when an error occurs.

### Creating a task for receiving objects
This example creates a task that registers `tizen_core_channel_receive_cb()` to receive channel objects:
```c
static void channel_receive_cb(tizen_core_channel_object_cb object, void *user_data)
{
  char *str = NULL;
  int id = -1;

  tizen_core_channel_object_get_id(object, &id);
  tizen_core_channel_object_get_data(object, (void **)&str);
  dlog_print(DLOG_INFO, LOG_TAG, "id=%d, str=%s", id, str);
  free(str);
}

static void create_and_run_task(const char *task_name, tizen_core_channel_receiver_h receiver)
{
  tizen_core_task_h task = NULL;
  tizen_core_h core = NULL;
  tizen_core_source_h source = NULL;
  int ret;

  ret = tizen_core_task_create(task_name, true, &task);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to create task. error=%d", ret);
    return;
  }

  tizen_core_task_get_tizen_core(task, &core);

  ret = tizen_core_add_channel(core, receiver, channel_receive_cb, NULL, &source);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to add channel to core, error=%d", ret);
    tizen_core_task_destroy(task);
    return;
  }

  tizen_core_task_run(task);
  //...
}
```
The `tizen_core_channel_receive_cb()` receives objects managed by the platform. There is no need to explicitly destroy them. The receiving side needs to release the received object's data.
You must call `tizen_core_remove_source()` to remove the source returned by `tizen_core_add_channel()` when it is no longer needed.
In this example, the task's loop runs on a thread, and `channel_receive_cb()` is delivered to the thread's loop.

You can receive channel objects using the receiver handle as shown below:
```c
{
  tizen_core_channel_object_h object = NULL;
  char *str = NULL;
  int id = -1;
  int ret;

  ret = tizen_core_channel_receiver_receive(receiver, &object);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to receive channel object. error=%d", ret);
    return;
  }

  tizen_core_channel_object_get_id(object, &id);
  tizen_core_channel_object_get_data(object, (void **)&str);
  dlog_print(DLOG_INFO, LOG_TAG, "id=%d, str=%s", id, str);
  free(str);
  tizen_core_channel_object_destroy(object);
}
```
The `tizen_core_channel_receiver_receive()` blocks indefinitely if there is no data being transmitted. It is recommended to use it in situations where the sender sends data reliably.
After receiving the object, its ownership is transferred to the receiving party, so you must release it by calling the `tizen_core_channel_object_destroy()`.

## Related Information
- Dependencies
  - Tizen 9.0
- API Reference
  - [Tizen Core Channel](../../../api/common/latest/group__CAPI__TIZEN__CORE__CHANNEL__MODULE.html)
