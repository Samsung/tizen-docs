# Plug

This feature is supported in wearable applications only.

The plug component shows an `Evas_Object` created by another process. It can be used anywhere in the same way as any other Elementary UI component.

For more information, see the [Plug](../../../../api/wearable/latest/group__Plug.html) API.

**Figure: Plug hierarchy**

![Plug hierarchy](./media/plug_tree.png)

## Adding a Plug Component

To create a plug component, use the `elm_plug_add()` function:

```
Evas_Object *plug;
Evas_Object *parent;

plug = elm_plug_add(parent);
```

## Using the Plug

To use the plug:

1. The socket image provides the service to which the plug component is connected. Use the `elm_plug_connect()` function, and define as parameters the service name and number set by the socket you want to connect to.

   To connect to a service named `plug_test` on the number 0:

   ```
   elm_plug_connect(plug, "plug_test", 0, EINA_FALSE);
   ```

2. Retrieve the `Evas_Object` corresponding to the remote image with the `elm_plug_image_object_get()` function:

   ```
   Evas_Object *plug_img = elm_plug_image_object_get(plug);
   ```

   > **Note**
   >
   > The socket to connect to must be started with the `elm_win_socket_listen()` function in the other process on the remote window object (`remote_win`):
   > ```
   > /* Create a remote window in the other process */
   > Elm_Win *remote_win = elm_win_add(NULL, "Window Socket",
   >                                   ELM_WIN_SOCKET_IMAGE);
   > /* Create a socket named "plug_test" and listen to it */
   > elm_win_socket_listen(remote_win, "plug_test", 0, EINA_FALSE);
   > ```

## Using the Plug Callbacks

To receive notifications about the plug events, listen for the following signals:

- `clicked`: The image is clicked (press/release).

  The `event_info` callback parameter is `NULL`.

- `image,deleted`: The server side is deleted.

  The `event_info` callback parameter is `NULL`.

- `image,resized`: The server side is resized.

  The `event_info` callback parameter is `Evas_Coord_Size` (2 integers).

> **Note**
>
> The signal list in the API reference can be more extensive, but only the above signals are actually supported in Tizen.

To register and define a callback for the `clicked` signal:

```
{
    evas_object_smart_callback_add(plug, "clicked", clicked_cb, data);
}

/* Callback for the "clicked" signal */
/* Called when the plug is clicked */
void
clicked_cb(void *data, Evas_Object *obj, void *event_info)
{
    dlog_print(DLOG_INFO, LOG_TAG, "Plug is clicked\n");
}
```

> **Note**
>
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.3.1 and Higher for Wearable
