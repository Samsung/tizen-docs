# TZSH-Softkey


tzsh-softkey is library for control the softkey window which shows the software buttons such as back and home buttons. You can manipulate the tzsh-softkey manipulate softkey window's visible state, expandable state and opacity state.
Each of states are taking following properties.

- **Visible State**: You can show or hide the softkey window. If show, the softkey window will appear. And hide, the softkey window will be hidden.

- **Expandable State**: You can control expandable state of the softkey window.
If you set expand on, then expandable button of the softkey window will be shown like below.
![Expand On Transparent](./media/tzsh_softkey_expand_on_transparent.png)
   Or, if you set expand off, then expandable button disppear.
![Expand Off Transparent](./media/tzsh_softkey_expand_off_transparent.png)

- **Opacity State**: You can manipulate opaque state of the softkey window.
      if you set opacity opaque, background of the softkey window turns 24bit color opaque window like below.
![Expand Off Opaque](./media/tzsh_softkey_expand_off_opaque.png)
   Or, if you set opacity transparent, background will turn to 32bit colored transparent window.
![Expand Off Transparent](./media/tzsh_softkey_expand_off_transparent.png)

## Prerequisites

To use the functions and structures of the TZSH softkey API (in mobile and wearable applications), include the `<tzsh_softkey.h>` header file in your application:

```
#include <tzsh_softkey.h>
```

## Create TZSH Softkey Handler

Once you have create the main window for your application, call the `tzsh_create and tzsh_softkey_create` function with a native window ID to create `tzsh_softkey_h` structure (in mobile and wearable applications).
	
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

To show or hide softkey window when your applications's window is activated, call the following functions:

```
   int ret;

   if (show)
   {
      ret = tzsh_softkey_global_show(tzsh_sk); /* To show softkey window */
      if (ret != TZSH_ERROR_NONE)
      {
         /* error */
      }
   }
   else
   {
      ret = tzsh_softkey_global_hide(tzsh_sk); /* To hide softkey window */
      if (ret != TZSH_ERROR_NONE)
      {
         /* error */
      }
   }
```

## Get Visibility Status of Softkey Window

To know the current visible state of softkey service's window, call the `tzsh_softkey_global_visible_get` function. The softkey service's window may be visible or invisible on the screen.

```
   int ret;
   tzsh_softkey_state_visible_e state;

   ret = tzsh_softkey_global_visible_state_get(tzsh_sk, &state);
   if (ret != TZSH_ERROR_NONE)
   {
      /* error */
   }
   if (state == TZSH_SOFTKEY_STATE_VISIBLE_SHOW)
   {
      /* visible state */
   }
   else if (state == TZSH_SOFTKEY_STATE_VISIBLE_HIDE)
   {
      /* invisible state */
   }
   else
   {
      /* error */
   }
```

## Set Expandable Status of Softkey Window

To make the softkey service's window can expandable or not, call the `tzsh_softkey_global_expand_state_set` function:

```
   int ret;

   if (expandable)
   {
      ret = tzsh_softkey_global_expand_state_set(tzsh_sk, TZSH_SOFTKEY_STATE_EXPAND_ON);
      if (ret)
      {
         /* error */
      }
   }
   else
   {
      ret = tzsh_softkey_global_expand_state_set(tzsh_sk, TZSH_SOFTKEY_STATE_EXPAND_OFF);
      if (ret)
      {
         /* error */
      }
   }
```

## Get Expandable Status of Softkey Window

To know the state of current expandable state of softkey service's window, call the `tzsh_softkey_global_expand_state_get` function. The softkey service's window may be expandable or inexpandable.

```
   int ret;
   tzsh_softkey_expand_state_e state;

   ret = tzsh_softkey_global_expand_state_get(tzsh_sk, &state);
   if (ret != TZSH_ERROR_NONE)
   {
      /* error */
   }
   if (state == TZSH_SOFTKEY_STATE_EXPAND_ON)
   {
      /* expand state */
   }
   else if (state == TZSH_SOFTKEY_STATE_EXPAND_OFF)
   {
      /* inexpand state */
   }
   else
   {
      /* error */
   }
```

## Set Opacity State of Softkey Window

To make the softkey service's window to be opaque or transparent, call the `tzsh_softkey_global_opacity_state_set` function:

```
   int ret;

   if (opaque)
   {
      ret = tzsh_softkey_global_opacity_state_set(tzsh_sk, TZSH_SOFTKEY_STATE_OPACITY_OPAQUE);
      if (ret != TZSH_ERROR_NONE)
      {
         /* error */
      }
   }
   else
   {
      ret = tzsh_softkey_global_opacity_state_set(tzsh_sk, TZSH_SOFTKEY_STATE_OPACITY_TRANSPARENT);
      if (ret != TZSH_ERROR_NONE)
      {
         /* error */
      }
   }
```

## Get Opacity State of Softkey Window

To know the current opacity state of softkey service's window, call the `tzsh_softkey_global_opacity_state_get` function. The softkey service's window may be opaque or transparent.

```
   int ret;
   tzsh_softkey_opacity_state_e state;

   ret = tzsh_softkey_global_opacity_state_get(tzsh_sk, &state);
   if (ret != TZSH_ERROR_NONE)
   {
      /* error */
   }
   if (state == TZSH_SOFTKEY_STATE_OPACITY_OPAQUE)
   {
      /* opaque state */
   }
   else if (state == TZSH_SOFTKEY_STATE_OPACITY_TRANSPARENT)
   {
      /* transparent state */
   }
   else
   {
      /* error */
   }
```

## Destroy the TZSH Softkey

When TZSH quickpanel and TZSH structures are no longer needed, free the structures as follows:

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
