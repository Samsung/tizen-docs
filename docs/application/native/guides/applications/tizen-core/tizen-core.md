# Tizen Core

Tizen Core is a new main loop that improves the existing main loop model. It supports creating and running the main loop in multiple threads.
Tizen Core provides an API that supports secure communication between threads.

The following are functions provided by Tizen Core for inter-thread communication and event delivery.
 - **[Tizen Core Channel](./tizen-core-channel.md)**: Provides a thread-safe communication method between threads.
 - **[Tizen Core Event](./tizen-core-event.md)**: Provides the ability to deliver events to specific tasks.

## Preparation
To use the Tizen Core API, you must include the `tizen_core.h` header, as shown below:
```c
#include <tizen_core.h>
```

## Initializing Tizen Core
Before using Tizen core, Call `tizen_core_init()` as shown below:
```c
#include <tizen_core.h>

int main(int argc, char **argv)
{
  tizen_core_init();
  // ...
  return 0;
}
```

## Shutting down Tizen Core
When Tizen Core is no longer needed, shut down Tizen Core with the code below:
```c
#include <tizen_core.h>

int main(int argc, char **argv)
{
  tizen_core_init();
  // ...
  tizen_core_shutdown();
  return 0;
}
```

## Managing Tizen Core tasks
This section will cover creating, executing, and terminating tizen_core_task_h objects. It will also cover obtaining `tizen_core_h` from `tizen_core_task_h` and adding idle jobs, timers, and sources to the main loop.

### Creating a Task
Here's an example on how to create a `tizen_core_task_h` object:
```c
{
  tizen_core_task_h task = NULL;
  int ret;

  ret = tizen_core_task_create("task1", true, &task);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to create task. error=%d", ret);
    return;
  }
}
```
`task` was created with the name "task1" and configured to use its own thread.
The created `task` handle should be removed using `tizen_core_task_destroy()` when it is no longer needed.


### Running a task
In this example, we'll cover the code to execute a previously created task using `tizen_core_task_run()`:
```c
{
  int ret;

  ret = tizen_core_task_run(task);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to run task. error=%d", ret);
    return;
  }
}
```
`task` creates and runs a thread named "task1". After calling `tizen_core_task_run()`, the thread is created and the loop starts running.

### Checking if a task is running
An example of checking if a task is running using `tizen_core_task_is_running()`:
```c
static void check_task_running_state(tizen_core_task_h task)
{
  bool running = false;
  int ret;

  ret = tizen_core_task_is_running(task, &running);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to check whether the task is running or not. error=%d", ret);
    return;
  }

  dlog_print(DLOG_INFO, LOG_TAG, "Task is %s", running ? "running" : "not running");
}
```
If the task is running, the log message "Task is running" is printed using dlog.

### Exiting a task
An example of exiting a running task:
```c
{
  bool running = false;
  int ret;

  tizen_core_task_is_running(task, &running);
  if (running) {
    ret = tizen_core_task_quit(task);
    if (ret != TIZEN_CORE_ERROR_NONE) {
      dlog_print(DLOG_ERROR, LOG_TAG, "Failed to exit the loop of the task. error=%d", ret);
      return;
    }
  }

  // ...
}
```
In this example, the `task` checks if it is running before exiting. When `tizen_core_task_quit()` is called, the loop ends and the created thread is cleaned up.

### Getting the core handle
An example of getting a `tizen_core_h` handle from a `tizen_core_task_h` handle:
```c
{
  tizen_core_h core = NULL;
  int ret;

  ret = tizen_core_task_get_tizen_core(task, &core);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to get tizen core. error=%d", ret);
    return;
  }
}
```

A `tizen_core_h` can also be found by name. The next example shows how to find the `tizen_core_h` of a `tizen_core_task_h` created earlier with the name "task1":
```c
{
  tizen_core_h core = NULL;
  int ret;

  ret = tizen_core_find("task1", &core);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to find tizen core from name('task1'). error=%d", ret);
    return;
  }
}
```

You can obtain the Tizen Core information of the current thread through the API by using the following code:
```c
{
  tizen_core_h core = NULL;
  int ret;
  
  ret = tizen_core_find_from_this_thread(&core);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to find tizen core from this thread. error=%d", ret);
    return;
  }
}
```
If there is no `tizen_core_h` running in the current thread, the function returns the `tizen_core_h` running in the main thread.

## Adding an idle job to Tizen Core
Let's write an example that adds an idle job to `tizen_core_h` and removes the job again when the callback is called.
```c
static bool idle_job_cb(void *user_data)
{
  dlog_print(DLOG_INFO, LOG_TAG, "idle_job_cb is called");
  return false;
}

static tizen_core_source_h add_idle_job(tizen_core_h core)
{
  tizen_core_source_h source = NULL;
  int ret;

  ret = tizen_core_add_idle_job(core, idle_job_cb, NULL, &source);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to add idle job. error=%d", ret);
    return NULL;
  }

  return source;
}
```
In this example, the `idle_job_cb()` returns 'false'. If 'true' is returned, the `idle_job_cb()` will be repeatedly called.
Since the `idle_job_cb()` returns 'false', the returned source handle does not need to be explicitly freed.
However, if the `idle_job_cb()` returns 'true', you have to call `tizen_core_remove_source()` to free the source.

## Adding a timer to Tizen Core
Here's an example of registering a timer that calls the callback every 100 ms.
```c
static bool timer_cb(void *user_data)
{
  dlog_print(DLOG_INFO, LOG_TAG, "timer_cb is called");
  return true;
}

static tizen_core_source_h add_timer(tizen_core_h core)
{
  tizen_core_source_h source = NULL;
  int ret;

  ret = tizen_core_add_timer(core, 100, timer_cb, NULL, &source);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to add timer. error=%d", ret);
    return NULL;
  }

  return source;
}
```
If the registered timer source is no longer needed, you should remove it by calling `tizen_core_remove_source()`.

## Removing a source from Tizen Core
To remove a source registered with `tizen_core_add_idle_job()` or `tizen_core_add_timer()`, use `tizen_core_remove_source()` as follows:
```c
{
  int ret;

  ret = tizen_core_remove_source(core, source);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to remove source. error=%d", ret);
    return;
  }
}
```

## Managing Tizen Core sources
### Creating a poll file descriptor
This example covers creating a `tizen_core_poll_fd_h`:
```c
static tizen_core_poll_fd_h create_poll_fd(int fd, uint16_t events)
{
  tizen_core_poll_fd_h poll_fd = NULL;
  int ret;

  ret = tizen_core_poll_fd_create(&poll_fd);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to create poll fd. error=%d", ret);
    return NULL;
  }

  ret = tizen_core_poll_fd_set_fd(poll_fd, fd);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to set fd(%d) to poll fd. error=%d", fd, ret);
    tizen_core_poll_fd_destroy(poll_fd);
    return NULL;
  }

  ret = tizen_core_poll_fd_set_events(poll_fd, events);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to set request events. error=%d", ret);
    tizen_core_poll_fd_destroy(poll_fd);
    return NULL;
  }

  return poll_fd;
}
```
The created `poll_fd` handle can be registered to a source using `tizen_core_source_add_poll()`.
When the `poll_fd` is no longer needed, you must call `tizen_core_poll_fd_destroy()`.

### Creating a source and registering a poll file descriptor
This example registers the poll fd created in the previous example to a source:
```c
static tizen_core_source_h create_fd_source(tizen_core_poll_fd_h poll_fd)
{
  tizen_core_source_h source = NULL;
  tizen_core_h core = NULL;
  int ret;

  ret = tizen_core_find("task1", &core);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to find core. error=%d", ret);
    return NULL;
  }

  ret = tizen_core_source_create(&source);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to create source. error=%d", ret);
    return NULL;
  }

  ret = tizen_core_source_add_poll(source, poll_fd);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to add poll fd. error=%d", ret);
    tizen_core_source_destroy(source);
    return NULL;
  }

  ret = tizen_core_add_source(core, source);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to add source to core. error=%d", ret);
    tizen_core_source_remove_poll(source, poll_fd);
    tizen_core_source_destroy(source);
    return NULL;
  }

  return source;
}
```
This example registers the poll fd to a source and adds the source to the "task1" core.
The source begins polling the fd. You should call `tizen_core_remove_source()` to remove the source added with `tizen_core_add_source()` when it is no longer needed.

### Registering callbacks and controlling events
In case of file descriptor sources, the `tizen_core_source_prepare_cb()` function usually returns 'false' because we have to wait until poll() gets called before knowing whether or not we should process any events. We set the returned timeout value to -1 indicating we don't care how long the poll() call block lasts. The `tizen_core_source_check_cb()` function tests the result of the poll() call to verify if the required condition is met and returns 'true' if it does.
This example demonstrates registering `tizen_core_source_prepare_cb()`, `tizen_core_source_check_cb()`, `tizen_core_source_dispatch_cb()`, `tizen_core_source_finalize_cb()` functions and reading data from the fd:
```c
static bool source_prepare_cb(tizen_core_source_h source, int *timeout, void *user_data)
{
  *timeout = -1;
  return false;
}

static bool source_check_cb(tizen_core_source_h source, void *user_data)
{
  tizen_core_poll_fd_h poll_fd = (tizen_core_poll_fd_h)user_data;
  uint16_t returned_events = 0;

  tizen_core_poll_fd_get_returned_events(poll_fd, &returned_events);
  if (returned_events & TIZEN_CORE_POLL_EVENT_IN) return true;

  return false;
}

static bool source_dispatch_cb(tizen_core_source_h source, void *user_data)
{
  tizen_core_poll_fd_h poll_fd = (tizen_core_poll_fd_h)user_data;
  int fd = -1;
  ssize_t bytes;
  int ret;

  tizen_core_poll_fd_get_fd(poll_fd, &fd);
  bytes = read(fd, &ret, sizeof(int));
  if (bytes < 0) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to read data. errno=%d", errno);
    return true;
  }

  if (bytes == 0) {
    dlog_print(DLOG_ERROR, LOG_TAG, "EOF");
    tizen_core_source_destroy(source);
    return true;
  }

  dlog_print(DLOG_INFO, LOG_TAG, "result=%d", ret);
  return true;
}

static void source_finalize_cb(tizen_core_source_h source, void *user_data)
{
  tizen_core_poll_fd_h poll_fd = (tizen_core_poll_fd_h)user_data;

  tizen_core_poll_fd_destroy(poll_fd);
}

static int set_callbacks(tizen_core_source_h source) {
  int ret;

  ret = tizen_core_source_set_prepare_cb(source, source_prepare_cb, poll_fd);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to set prepare cb. error=%d", ret);
    return -1;
  }

  ret = tizen_core_source_set_check_cb(source, source_check_cb, poll_fd);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to set check cb. error=%d", ret);
    return -1;
  }

  ret = tizen_core_source_set_dispatch_cb(source, source_dispatch_cb, poll_fd);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to set dispatch cb. error=%d", ret);
    return -1;
  }

  ret = tizen_core_source_set_finalize_cb(source, source_finalize_cb, poll_fd);
  if (ret != TIZEN_CORE_ERROR_NONE) {
    dlog_print(DLOG_ERROR, LOG_TAG, "Failed to set finalize cb. error=%d", ret);
    return -1
  }

  return 0;
}
```
This example describes how to register callbacks and read results from the fd inside `tizen_core_source_dispatch_cb()`.

## Related Information
- Dependencies
  - Tizen 9.0
- API Reference
  - [Tizen Core](../../api/common/latest/group__CAPI__TIZEN__CORE__MODULE.html)
