# TZSH-Quickpanel

TZSH-Quickpanel is a library to control the Quickpanel service window that shows notifications and system setup widgets. You can use TZSH-Quickpanel to get various information from the Quickpanel service window.
For example, media player application needs to close the Quickpanel service window during playback of video. In this case, you can use the TZSH-Quickpanel library.

## Prerequisites

To use the functions and structures of the TZSH-Quickpanel API (in [mobile](../../../api/mobile/latest/group__TIZEN__WS__SHELL__QUICKPANEL__MODULE.html) and [wearable](../../../api/wearable/latest/group__TIZEN__WS__SHELL__QUICKPANEL__MODULE.html) applications), include the `<tzsh_quickpanel.h>` header file in your application:

```
#include <tzsh_quickpanel.h>
```

## Create TZSH-Quickpanel Handler
After you have created the main window of your application, call `tzsh_quickpanel_create_with_type()` with a native window ID to create the `tzsh_quickpanel_h` structure (in [mobile](../../../api/mobile/latest/group__TIZEN__WS__SHELL__QUICKPANEL__MODULE.html#gaaa00e8e25b43c9538ca188bc43bdb3ac) and [wearable](../../../api/wearable/latest/group__TIZEN__WS__SHELL__QUICKPANEL__MODULE.html#gaaa00e8e25b43c9538ca188bc43bdb3ac) applications):

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

To show or hide the Quickpanel service window when your application's window is activated, use the following code:

```
    if (show)
        tzsh_quickpanel_show(tzsh_qp); /* To show quickpanel window */
    else
        tzsh_quickpanel_hide(tzsh_qp); /* To hide quickpanel window */
```

## Get Visibility Status of Quickpanel Window
To get the current visibility status of the Quickpanel service window, call `tzsh_quickpanel_visible_get()`. The Quickpanel service window will be visible or invisible depending on the visible state:

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
To get notified about the state changes, implement the appropriate event callback function and call `tzsh_quickpanel_event_handler_add()` with that event callback function. If you want to change your application's behavior to match the visibility of the Quickpanel service window, you need to handle the state change event. To handle the state change event, use the following code:

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

## Destroy TZSH-Quickpanel
When TZSH-Quickpanel is no longer needed, destroy the structures. To destroy the structures, use the following code:

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
