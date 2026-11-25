# TZSH-Quickpanel

TZSH-Quickpanel is a library to control the Quickpanel service window that shows notifications and system setup widgets. You can use TZSH-Quickpanel to get various information from the Quickpanel service window.
For example, media player application needs to close the Quickpanel service window during playback of video. In this case, you can use the TZSH-Quickpanel library.

> **Note**
>
> The example uses `TZSH_TOOLKIT_TYPE_TCORE_WAYLAND`, available since Tizen 11.0. It expects a connected Tizen Core Wayland display from your application.

## Prerequisites

To use the functions and structures of the [TZSH-Quickpanel API](../../../api/common/latest/group__TIZEN__WS__SHELL__QUICKPANEL__MODULE.html), include the `<tzsh_quickpanel.h>` header file in your application:

```
#include <tzsh_quickpanel.h>
```

## Create TZSH-Quickpanel Handler
Create the application window with `tizen_core_wl_create_window()`. Then create a `tzsh_h` handle with `TZSH_TOOLKIT_TYPE_TCORE_WAYLAND`, get the window's native surface ID, and pass it with the handle and Quickpanel type to `tzsh_quickpanel_create_with_type()` to create the [`tzsh_quickpanel_h` structure](../../../api/common/latest/group__TIZEN__WS__SHELL__QUICKPANEL__MODULE.html#gaaa00e8e25b43c9538ca188bc43bdb3ac):

```
#include <tizen_core_wl.h>
#include <wayland-client.h>
#include <tzsh.h>
#include <tzsh_quickpanel.h>

static void
init(tizen_core_wl_display_h display)
{
    tizen_core_wl_window_h main_window = NULL;
    tizen_core_wl_native_surface_h surface = NULL;
    tzsh_h tzsh = NULL;
    tzsh_quickpanel_h tzsh_qp = NULL;
    tzsh_window tz_win;

    if (tizen_core_wl_create_window(display, NULL, 0, 0, 640, 480, &main_window) != TIZEN_CORE_WL_ERROR_NONE)
        return;

    tizen_core_wl_window_show(main_window);

    if (tizen_core_wl_window_get_native_surface(main_window, &surface) != TIZEN_CORE_WL_ERROR_NONE || !surface)
        return;

    tz_win = (tzsh_window)wl_proxy_get_id((struct wl_proxy *)surface);
    tzsh = tzsh_create(TZSH_TOOLKIT_TYPE_TCORE_WAYLAND);
    if (!tzsh)
        return;

    tzsh_qp = tzsh_quickpanel_create_with_type(tzsh, tz_win, TZSH_QUICKPANEL_TYPE_SYSTEM_DEFAULT);
    if (!tzsh_qp) {
        tzsh_destroy(tzsh);
        return;
    }
}
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
register_qp_event_handler(tzsh_quickpanel_h tzsh_qp)
{
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
  - Since Tizen 3.0
