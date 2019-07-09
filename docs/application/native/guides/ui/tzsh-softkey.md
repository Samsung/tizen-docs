# TZSH-Softkey


tzsh-softkey is library for control the softkey window which shows the software buttons such as back and home buttons. You can use the tzsh-softkey manipulate softkey window's visible state, expandable state and opacity state.
Each of states are taking following properties.

- **Visible State**: You can show or hide the softkey window. If show, the softkey window will appear. And hide, the softkey window will be hidden.

- **Expandable State**: You can control expandable state of the softkey window.
If you set expand on, then expandable button of the softkey window will be shown like below.
![Expand On Transparent](./media/tzsh_softkey_expand_on_transparent.png)
   Or, if you set expand off, then expandable button disppear.
![Expand Off Transparent](./media/tzsh_softkey_expand_off_transparent.png)

- **Opacity State**: You can manipulate opaque state of the softkey window.
      if you set opacity_opaque, background of the softkey window turns 24bit color opaque window like below.
![Expand Off Opaque](./media/tzsh_softkey_expand_off_opaque.png)
   Or, if you set opacity transparent, background will turn to 32bit colored transparent window.
![Expand Off Transparent](./media/tzsh_softkey_expand_off_transparent.png)

## Prerequisites

To use the functions and structures of the TZSH softkey API (in mobile and wearable applications), include the `<tzsh_softkey.h>` header file in your application:

```
#include <tzsh_softkey.h>
```

## Create TZSH Softkey Handler

Once you have created the main window for your application, call the `tzsh_create and tzsh_softkey_create` function with a native window ID to create `tzsh_softkey_h` structure (in mobile and wearable applications).
	
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

