# Photocam

This feature is supported in mobile applications only.

The photocam component displays high resolution photos taken from digital cameras. It provides a way to zoom the photo, load it quickly, and fit it nicely on the screen. It is optimized for the `.jpeg` image format and has a low memory footprint.

The photocam component implements the scroller interface, which means that scroller functions can be used with the photocam component.

For more information, see the [Photocam](../../../../api/mobile/latest/group__Elm__Photocam.html) API.

**Figure: Photocam hierarchy**

![Photocam hierarchy](./media/photocam_tree.png)

## Adding a Photocam Component

To create a photocam component, use the `elm_photocam_add()` function. You can set the image file with the `elm_photocam_file_set()` function.

```
Evas_Object *photocam;

photocam = elm_photocam_add(win);
elm_photocam_file_set(photocam, "/tmp/photo.jpeg");
```

## Using the Photocam Zoom

To use the photocam zoom:

- Set the zoom mode. You can select between 2 automatic and 1 manual zoom mode.

  To set the zoom mode to manual with a double zoom:

  ```
  elm_photocam_zoom_mode_set(photocam, ELM_PHOTOCAM_ZOOM_MODE_MANUAL);
  elm_photocam_zoom_set(photocam, 2.0);
  ```

  If you use the `ELM_PHOTOCAM_ZOOM_MODE_AUTO_FIT` mode, the photo fits exactly inside the scroll frame with no pixels outside the region. In the `ELM_PHOTOCAM_ZOOM_MODE_AUTO_FILL` mode, all the pixels of the photocam component are filled.

- Activate the multi-touch zoom by enabling gestures:

  ```
  elm_photocam_gesture_enabled_set(photocam, EINA_TRUE);
  ```

- Zoom in on a specific region.

  To zoom in on a region starting at the coordinates (200 x 200) with a width of 400 px and a height of 300 px:

  ```
  elm_photocam_image_region_bring_in(photocam, 200, 200, 400, 300);
  ```

## Using the Photocam Callbacks

To receive notifications about the photocam events, listen for the following signals:

- `clicked`: The photo is clicked without dragging.
- `press`: The photo is pressed.
- `longpressed`: The photo is pressed down for a long time without dragging.
- `clicked,double`: The photo is double-clicked.
- `load`: The photo load begins.
- `loaded`: The image file load is complete for the first view (a low resolution blurry version).
- `load,detail`: A photo detailed data load begins.
- `loaded,detail`: The image file load is complete for the detailed image data (a full resolution version).
- `zoom,start`: The zoom animation starts.
- `zoom,stop`: The zoom animation stops.
- `zoom,change`: The zoom is changed when using an auto zoom mode.
- `scroll`: The content is scrolled.
- `scroll,anim,start`: The scrolling animation starts.
- `scroll,anim,stop`: The scrolling animation stops.
- `scroll,drag,start`: Dragging the content starts.
- `scroll,drag,stop`: Dragging the content stops.

> **Note**  
> The signal list in the API reference can be more extensive, but only the above signals are actually supported in Tizen.

In all cases, the `event_info` callback parameter is `NULL`.

To register and define a callback for the `loaded` signal:

```
void
message_port_cb(int local_port_id, const char *remote_app_id, bundle *message)
{
    evas_object_smart_callback_add(photocam, "loaded", loaded_cb, data);
}

/* Callback for the "loaded" signal */
/* Called when the photo file has been loaded in a low resolution */
void
loaded_cb(void *data, Evas_Object *obj, void *event_info)
{
    dlog_print(DLOG_INFO, LOG_TAG, "The photo has been loaded\n");
}
```

> **Note**  
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
