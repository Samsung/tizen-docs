# TZSH-Softkey

TZSH-Softkey is a library to control the Softkey service window that shows the software buttons such as back button and home button. You can use TZSH-Softkey to control the Softkey service window's visible state, expandable state and opacity state.
Each state has the following properties:

> **Note**
>
> Each state can present itself differently depending on the implementation of the Softkey service.
> So, the example does not represent all the Softkey service window.

- **Visible State**: You can show or hide the Softkey service window. If you set the visible state to show, the Softkey service window appears. If you set it to hide, the Softkey service window disappears.

- **Expandable State**: You can control expandable state of the Softkey service window.
If you set the expand state to on, then the expandable button of the Softkey service window appears as follows:
![Expand On Transparent](./media/tzsh_softkey_expand_on_transparent.png)
If you set the expand state to off, then the expandable button disappears as follows:
![Expand Off Transparent](./media/tzsh_softkey_expand_off_transparent.png)

- **Opacity State**: You can control the opacity state of the Softkey service window.
If you set the opacity state to opaque, the background of the Softkey service window changes to 24-bit color opaque window as follows:
![Expand Off Opaque](./media/tzsh_softkey_expand_off_opaque.png)
If you set the opacity state to transparent, the background changes to 32-bit colored transparent window as follows:
![Expand Off Transparent](./media/tzsh_softkey_expand_off_transparent.png)

## Prerequisites

To use the functions and structures of the TZSH-Softkey API (in [mobile](../../../api/mobile/latest/group__TIZEN__WS__SHELL__SOFTKEY__MODULE.html) and [wearable](../../../api/wearable/latest/group__TIZEN__WS__SHELL__SOFTKEY__MODULE.html) applications), include the `<tzsh_softkey.h>` header file in your application:

```
#include <tzsh_softkey.h>
```

## Create TZSH-Softkey Handler

After you have created the main window of your application, call `tzsh_create()` and `tzsh_softkey_create()` with a native window ID to create the `tzsh_softkey_h` structure (in [mobile](../../../api/mobile/latest/group__TIZEN__WS__SHELL__SOFTKEY__MODULE.html#ga2ee6e5dec1081136fe1139d6a611e58d) and [wearable](../../../api/wearable/latest/group__TIZEN__WS__SHELL__SOFTKEY__MODULE.html#ga2ee6e5dec1081136fe1139d6a611e58d) applications):
	
```
#include <Elementary.h>

static void
init(const char *name)
{
    Evas_Object *main_win;

    /* create main window for your application */
    main_win = elm-win_util_standard_add(name, name);

    /* set up main window */
    ...
    evas_object_show(main_win);


    tzsh_h tzsh;
    tzsh_softkey_h tzsh_sk;
    tzsh_window tz_win;

    /* Get native window ID of main window */
    tz_win = elm_win_window_id_get(main_win);

    /* Create tzsh_h structure */
    tzsh = tzsh_create(tz_win);

    /* Create tzsh_softkey_h structure */
    tzsh_sk = tzsh_softkey_create(tzsh, tz_win);

    ...
    /* Do Something Creative */
```

## Show or Hide Softkey Window

To show or hide the Softkey service window when your application's window is activated, use the following code:

```
    int ret;

    if (show) {
        ret = tzsh_softkey_global_show(tzsh_sk); /* To show softkey service window */
        if (ret != TZSH_ERROR_NONE) {
            /* error */
        }
    } else {
        ret = tzsh_softkey_global_hide(tzsh_sk); /* To hide softkey service window */
        if (ret != TZSH_ERROR_NONE) {
            /* error */
        }
    }
```

## Get Visibility Status of Softkey Window

To get the current visible state of the Softkey service window, call `tzsh_softkey_global_visible_state_get()`. The Softkey service window will be visible or invisible depending on the visibility state:

```
    int ret;
    tzsh_softkey_state_visible_e state;

    ret = tzsh_softkey_global_visible_state_get(tzsh_sk, &state);
    if (ret != TZSH_ERROR_NONE) {
        /* error */
    }

    if (state == TZSH_SOFTKEY_STATE_VISIBLE_SHOW) {
        /* visible state */
    } else if (state == TZSH_SOFTKEY_STATE_VISIBLE_HIDE) {
        /* invisible state */
    } else {
        /* error */
    }
```

## Set Expandable Status of Softkey Window

To set expandable state of the Softkey service window, use the following code:

```
    int ret;

    if (expandable) {
        ret = tzsh_softkey_global_expand_state_set(tzsh_sk, TZSH_SOFTKEY_STATE_EXPAND_ON);
        if (ret) {
            /* error */
        }
    } else {
        ret = tzsh_softkey_global_expand_state_set(tzsh_sk, TZSH_SOFTKEY_STATE_EXPAND_OFF);
        if (ret) {
            /* error */
        }
    }
```

## Get Expandable Status of Softkey Window

To get the current expandable state of the Softkey service window, call `tzsh_softkey_global_expand_state_get()`. The Softkey service window will expand or collapse depending on expandable state:

```
    int ret;
    tzsh_softkey_expand_state_e state;

    ret = tzsh_softkey_global_expand_state_get(tzsh_sk, &state);
    if (ret != TZSH_ERROR_NONE) {
        /* error */
    }

    if (state == TZSH_SOFTKEY_STATE_EXPAND_ON) {
        /* expand state */
    } else if (state == TZSH_SOFTKEY_STATE_EXPAND_OFF) {
        /* inexpand state */
    } else {
        /* error */
    }
```

## Set Opacity State of Softkey Window

To make the Softkey service window opaque or transparent, use the following code:

```
    int ret;

    if (opaque) {
        ret = tzsh_softkey_global_opacity_state_set(tzsh_sk, TZSH_SOFTKEY_STATE_OPACITY_OPAQUE);
        if (ret != TZSH_ERROR_NONE) {
            /* error */
        }
    } else {
        ret = tzsh_softkey_global_opacity_state_set(tzsh_sk, TZSH_SOFTKEY_STATE_OPACITY_TRANSPARENT);
        if (ret != TZSH_ERROR_NONE) {
            /* error */
        }
    }
```

## Get Opacity State of Softkey Window

To get the current opacity state of the Softkey service window, call `tzsh_softkey_global_opacity_state_get()`. The Softkey service window will be opaque or transparent depending on the opacity state:

```
    int ret;
    tzsh_softkey_opacity_state_e state;

    ret = tzsh_softkey_global_opacity_state_get(tzsh_sk, &state);
    if (ret != TZSH_ERROR_NONE) {
        /* error */
    }

    if (state == TZSH_SOFTKEY_STATE_OPACITY_OPAQUE) {
        /* opaque state */
    } else if (state == TZSH_SOFTKEY_STATE_OPACITY_TRANSPARENT) {
        /* transparent state */
    } else {
        /* error */
    }
```

## Destroy TZSH-Softkey

When TZSH-Softkey and TZSH structures are no longer needed, destroy the structures. To destroy the structures, use the following code:

```
static void
deinit(void)
{
    tzsh_softkey_destroy(tzsh_sk);
    tzsh_destroy(tzsh);
}
```

## Related Information
 - Dependencies
   - Tizen 5.5 and Higher for Mobile
   - Tizen 5.5 and Higher for Wearable
