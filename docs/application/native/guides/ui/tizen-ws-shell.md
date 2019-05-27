# Tizen Window System Shell


The TZSH is an interface for manipulating windows of the system GUI services such as the quickpanel and the softkey. It provides C libraries that allow you to control windows of system GUI services and get notifications about the state changes of each window within an application.

Since, the system GUI service runs different process, all of operations of the TZSH are performed using the inter-process communication (IPC). It is needed to enable communication between system GUI service processes and separated user application process using the display server. The following figure illustrates a simple software architecture of the TZSH:

**Figure: Layer diagram for the Tizen window system shell**

![Layer diagram for the Tizen window system shell](./media/tzsh_arch.png)

To support each system GUI service in Tizen, the TZSH provides the following libraries:

- **tzsh-quickpanel**: For the quickpanel window which shows notifications and system setup widgets.

- **tzsh-softkey**: For the softkey window which shows the device back and home buttons.

Not all applications require to use the TZSH's functionalities. However, in some cases, certain applications may require to perform manipulation of system GUI service's window. For example, media player application needs to close the quickpanel window during playback of video. In this case, you can use the tzsh-quickpanel library.


## Prerequisites

To use the functions and structures of the TZSH quickpanel API (in [mobile](../../api/mobile/latest/group__TIZEN__WS__SHELL__QUICKPANEL__MODULE.html) and [wearable](../../api/wearable/latest/group__TIZEN__WS__SHELL__QUICKPANEL__MODULE.html) applications), include the `<tzsh_quickpanel.h>` header file in your application:

```
#include <tzsh_quickpanel.h>
```


## Create TZSH Quickpanel Handler
Once you have created the main window for your application, call the `tzsh_quickpanel_create_with_type` function with a native window ID to create `tzsh_quickpanel_h` structure (in [mobile](../../api/mobile/latest/group__TIZEN__WS__SHELL__QUICKPANEL__MODULE.html#gaaa00e8e25b43c9538ca188bc43bdb3ac) and [wearable](../../api/wearable/latest/group__TIZEN__WS__SHELL__QUICKPANEL__MODULE.html#gaaa00e8e25b43c9538ca188bc43bdb3ac) applications).

```
#include <Elementary.h>

static void
init(const char *name)
{
   Evas_Object *main_win;

   /* create main window for the application */
   main_win = elm_win_util_standard_add(name, name);

   /* set up main window */
   ...
   evas_object_show(main_win);


   tzsh_h tzsh;
   tzsh_quickpanel_h tzsh_qp;
   tzsh_window tz_win;

   /* Get native window ID of main window */
   tz_win = elm_win_window_id_get(main_win);

   /* Create tzsh_h structure */
   tzsh = tzsh_create(TZSH_TOOLKIT_TYPE_EFL);

   /* Create tzsh_quickpanel_h structure */
   tzsh_qp = tzsh_quickpanel_create_with_type(tzsh, tz_win, TZSH_QUICKPANEL_TYPE_SYSTEM_DEFAULT);
```


## Show or Hide Quickpanel Window

To show or hide quickpanel window when your application's window is activated, call the following functions:

```
   if (show)
     tzsh_quickpanel_show(tzsh_qp); /* To show quickpanel window */
   else
     tzsh_quickpanel_hide(tzsh_qp); /* To hide quickpanel window */
```

## Get Visibility Status of Quickpanel Window
To know the state of current visibility of quickpanel service's window, call the `tzsh_quickpanel_visible_get` function. The quickpanel service's window may be visible or invisible on the screen.

```
   tzsh_quickpanel_state_visible_e state;

   tzsh_quickpanel_visible_get(tzsh_qp, &state);
   if (state == TZSH_QUICKPANEL_STATE_VISIBLE_SHOWN) {
     /* visible state */
   } else if (state == TZSH_QUICKPANEL_STATE_VISIBLE_HIDDEN) {
     /* invisible state */
   } else {
     /* error */
   }

```


## Register a Changed Event for Quickpanel Window
To be notified about the state changes, implement the appropriate event callback function and call the `tzsh_quickpanel_event_handler_add` function with that. If you want to change your application's behavior to match visibility of the quicknapel service's window, you need to handle state change event as follows:

```
static tzsh_quickpanel_event_handler_h handler;

static void
ev_callback(int type, tzsh_quickpanel_event_info_h ev_info, void *data)
{
   tzsh_quickpanel_state_visible_e state;

   if (type != TZSH_QUICKPANEL_EVENT_VISIBLE)
     return;

   tzsh_quickpanel_event_visible_get(ev_info, &state);
   if (state == TZSH_QUICKPANEL_STATE_VISIBLE_SHOWN) {
     /* visible state */
   } else if (state == TZSH_QUICKPANEL_STATE_VISIBLE_HIDDEN) {
     /* invisible state */
   } else {
     /* error */
   }
}

static void
init(Evas_Object *main_win)
{
   ...

   /* register event callback */
   handler = tzsh_quickpanel_event_handler_add(tzsh_qp, TZSH_QUICKPANEL_EVENT_VISIBLE, ev_callback, NULL);
}
```


## Destroy TZSH Quickpanel and TZSH Structures
When TZSH quickpanel and TZSH structures are no longer needed, free the structures as follows:

```
static void
deinit(void)
{
   tzsh_quickpanel_event_handler_del(tzsh_qp, handler);
   tzsh_quickpanel_destroy(tzsh_qp);
   tzsh_destroy(tzsh);
}
```


## Related Information
- Dependencies
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
