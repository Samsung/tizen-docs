# Scroller

The scroller container holds and clips a single object and allows you to scroll across it. This means that the user can use a scroll bar or a finger to drag the viewable region across the object, moving through a much larger area than is contained in the viewport. A scroller always has a default minimum size that is not limited by its content. For more information, see the Scroller API (in [mobile](../../../api/mobile/latest/group__Elm__Scroller.html) and [wearable](../../../api/wearable/latest/group__Elm__Scroller.html) applications).

## Basic Usage

To build a layout with a scroller:

1. Add a scroller with the `elm_scroller_add()` function:

   ```
   Evas_Object *scroller;

   scroller = elm_scroller_add(parent);
   ```

2. Set a [style](#styles) to the scroller with the `elm_object_style_set()` function. If you use the default style, you can skip this step.

   ```
   elm_object_style_set(scroller, "handler");
   ```

3. Add an object and set it to the scroller with the `elm_object_content_set()` function:

   ```
   Evas_Object *image;

   elm_object_content_set(scroller, image);
   ```

   The content object must have a minimum size bigger than the scroller size to be scrollable.

4. Register the [callback](#callbacks) functions.  

 The following example shows how to define and register a callback for the `scroll,drag,start` signal:

   ```
   evas_object_smart_callback_add(scroller, "scroll,drag,start", _scroll_start_cb, NULL);

   void
   _scroll_start_cb(void *data, Evas_Object *obj, void *event_info)
   {
       printf("Scroll starts\n");
   }
   ```

The following example shows a simple use case of the scroller component, where an image objects is set into a scroller. The minimum size of the image (1600 x 1600 pixels) is larger than the scroller (smaller than 720 * 1280 pixels), so you can scroll across the image.

**Example: Scroller use case**

 ![Scroller](./media/scroller1.png) ![Scroller](./media/scroller2.png) ![Scroller](./media/scroller3.png)

```
Evas_Object *win;
Evas_Object *conf;
Evas_Object *nf;
Evas_Object *scroller;
Evas_Object *img;

/* Starting right after the basic EFL UI layout code */
/* (win - conformant - naviframe) */

/* Add a scroller and push it into the naviframe */
scroller = elm_scroller_add(nf);
evas_object_show(scroller);
elm_naviframe_item_push(nf, "Scroller", NULL, NULL, scroller, NULL);

/* Add an image and set it into the scroller */
img = elm_image_add(scroller);
elm_image_file_set(img, ICON_DIR"/tizen.png", NULL);
evas_object_size_hint_min_set(img, 1600, 1600);
evas_object_show(img);
elm_object_content_set(scroller, img);
```

## Styles

The following table lists the available component styles.

**Table: Scroller styles**

| Style     | Sample                                   |
|---------|----------------------------------------|
| `default` | ![elm/scroller/base/default](./media/scroller_default.png) |
| `handler` | ![elm/scroller/base/handler](./media/scroller_handler.png) |

## Callbacks

You can register callback functions connected to the following signals for a scroller object.

**Table: Scroller callback signals**

| Signal                | Description                              | `event_info` |
|---------------------|----------------------------------------|------------|
| `edge,left`           | The left edge of the content is reached. | `NULL`       |
| `edge,right`          | The right edge of the content is reached. | `NULL`       |
| `edge,top`            | The top edge of the content is reached.  | `NULL`       |
| `edge,bottom`         | The bottom edge of the content is reached. | `NULL`       |
| `scroll`              | The content is scrolled (moved).         | `NULL`       |
| `scroll,anim,start`   | The scrolling animation has started.     | `NULL`       |
| `scroll,anim,stop`    | The scrolling animation has stopped.     | `NULL`       |
| `scroll,drag,start`   | Dragging the content has started.        | `NULL`       |
| `scroll,drag,stop`    | Dragging the content has stopped.        | `NULL`       |
| `vbar,drag`           | The vertical scroll bar is dragged.      | `NULL`       |
| `vbar,press`          | The vertical scroll bar is pressed.      | `NULL`       |
| `vbar,unpress`        | The vertical scroll bar is unpressed.    | `NULL`       |
| `hbar,drag`           | The horizontal scroll bar is dragged.    | `NULL`       |
| `hbar,press`          | The horizontal scroll bar is pressed.    | `NULL`       |
| `hbar,unpress`        | The horizontal scroll bar is unpressed.  | `NULL`       |
| `scroll,page,changed` | The visible page has changed.            | `NULL`       |

> **Note**  
> The signal list in the API reference can be more extensive, but only the above signals are actually supported in Tizen.

## Example

A good example of scroller use is a picture slideshow: add images to the scroller and limit the scrolling to pages, meaning that one picture is shown at a time.

A scroller can limit scrolling to "pages". In this case, the scrolling occurs in page-sized chunks of content rather than in a purely continuous fashion, with the scroller displaying a single page at a time. This feature sets the size of the page relative to the viewport of the scroller. A size of 1.0 equals 1 viewport (horizontally or vertically). A size of 0.0 disables paging for that axis. These settings are mutually exclusive with page size (see the `elm_scroller_page_size_set()` function). A size of 0.5 equals half a viewport. Usable size values are normally between 0.0 and 1.0, including 1.0. If you only want a single axis to scroll in pages, use 0.0 for the other axis.

To create a picture slideshow:

1. Disable the scroll bars for both axes, limit the scrolling to pages using the `elm_scroller_page_scroll_limit_set()` function, and lock the scrolling on the Y axis using the `elm_object_scroll_lock_y_set()` function:

   ```
   elm_scroller_policy_set(scroller, ELM_SCROLLER_POLICY_OFF, ELM_SCROLLER_POLICY_OFF);
   elm_scroller_page_scroll_limit_set(scroller, 1, 0);
   elm_object_scroll_lock_y_set(scroller, EINA_TRUE);
   ```

2. Create a horizontal box, which contains all the images, and which itself is contained by the scroller:

   ```
   box = elm_box_add(scroller);
   elm_box_horizontal_set(box, EINA_TRUE);
   elm_object_content_set(scroller, box);
   evas_object_show(box);
   ```

3. Create all the images and add them to the horizontal box:

   ```
   img = elm_image_add(scroller);
   snprintf(buf, sizeof(buf), IMAGE_DIR"/%d.jpg", i);
   elm_image_file_set(img, buf, NULL);
   evas_object_show(img);
   pages = eina_list_append(pages, img);
   elm_box_pack_end(box, img);
   ```

   References to the images are stored in an `eina_list` for easy retrieval later.

4. Display the first page of the scroller:

   ```
   elm_scroller_page_show(scroller, 0, 0);
   ```

5. The size of the scroller depends on the size of the parent. When the parent changes, for example, when the window is resized or rotated, the scroller is also resized.

   Since you need to be informed when the scroller is resized, add a callback on the `EVAS_CALLBACK_RESIZE` event for the scroller:

   ```
   evas_object_event_callback_add(scroller, EVAS_CALLBACK_RESIZE, _scroller_resize_cb, NULL);
   ```

   The callback retrieves the new size of the scroller using the `evas_object_geometry_get()` function on the object pointer. The pointer is relative to the object that has been resized, which in this case is the scroller itself. Iterate through the images of the scroller and set the minimum size to fit the scroller size:

   ```
   EINA_LIST_FOREACH(images, l, page)
       evas_object_size_hint_min_set(page, w, h);
   ```

   Set the page size of the scroller to match the scroller size and display the first page:

   ```
   elm_scroller_page_size_set(obj, w, h);
   elm_scroller_page_show(obj, 0, 0);
   ```

> **Note**  
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
