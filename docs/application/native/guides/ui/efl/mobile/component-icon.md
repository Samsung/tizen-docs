# Icon

The icon UI component is used to display standard icon images ("delete", "home", and "apps") or images coming from a custom file (such as PNG, JPG, and Edje) in icon contexts. The icon component inherits from the [image](component-image.md) component, which means that image functions can be used on icon objects. For more information, see the [Icon](../../../../api/mobile/latest/group__Elm__Icon.html) API.

This feature is supported in mobile applications only.

In the following cases, use an icon instead of an image:

- You need a thumbnail version of an original image.
- You need [freedesktop.org](http://freedesktop.org)-provided icon images.
- You need theme-provided icon images (Edje groups).

## Basic Usage

To use an icon component in your application:

1. Add an icon with the `elm_icon_add()` function:

   ```
   Evas_Object *icon;

   icon = elm_icon_add(parent);
   ```

2. Set an image to the icon.

   To set a standard icon from [freedesktop.org](http://freedesktop.org), use the `elm_icon_standard_set()` function:

   ```
   Evas_Object *icon;
   Evas_Object *parent;

   icon = elm_icon_add(parent);
   elm_icon_standard_set(icon, "Home");
   ```

3. Register the [callback](#callbacks) functions.

To change the image file:

- You can use an image in the file system (for example, `/tmp/Home.png`):

  ```
  elm_image_file_set(icon, "/tmp/Home.png", NULL);
  ```

  You can also use a group in an Edje file (for example, `/tmp/Home.edj`):

  ```
  elm_image_file_set(icon, "/tmp/Home.edj", "elm/icon/Home/default");
  ```

- You can generate and use a thumbnail:

  ```
  elm_icon_thumb_set(icon, "/tmp/Home.png", NULL);
  ```

  The `elm_icon_thumb_set()` function sets the file in the icon and enables the use of a cached thumbnail, if it already exists. Otherwise, it creates a new thumbnail and caches it for future use. The Ethumb library support is required for the thumbnail usage.

The following example shows a simple use case of the icon component.

**Example: Icon use case**

![Icon](./media/icon1.png)

```
Evas_Object *win;
Evas_Object *conf;
Evas_Object *nf;
Evas_Object *box;
Evas_Object icon;
Elm_Object_Item *nf_it;

/* Starting right after the basic EFL UI layout code */
/* win - conformant - naviframe */

/* Add a box to pack icons */
box = elm_box_add(nf);
elm_object_content_set(nf, box);
evas_object_show(box);
elm_naviframe_item_push(nf, "Icon", NULL, NULL, box, NULL);

icon = elm_icon_add(box);
elm_icon_standard_set(icon, "apps");
evas_object_size_hint_min_set(icon, ELM_SCALE_SIZE(50), ELM_SCALE_SIZE(50));
evas_object_show(icon);
elm_box_pack_end(box, icon);

icon = elm_icon_add(box);
elm_icon_standard_set(icon, "home");
evas_object_size_hint_min_set(icon, ELM_SCALE_SIZE(50), ELM_SCALE_SIZE(50));
evas_object_show(icon);
elm_box_pack_end(box, icon);

icon = elm_icon_add(box);
elm_icon_standard_set(icon, "clock");
evas_object_size_hint_min_set(icon, ELM_SCALE_SIZE(50), ELM_SCALE_SIZE(50));
evas_object_show(icon);
elm_box_pack_end(box, icon);
```

## Standard Icons

**Table: Icon styles**

| Style                  | Sample                                   |
|----------------------|----------------------------------------|
| `apps`                 | ![apps](./media/icon_apps.png)   |
| `arrow_down`           | ![arrow_down](./media/icon_arrowdown.png) |
| `arrow_left`           | ![arrow_left](./media/icon_arrowleft.png) |
| `arrow_right`          | ![arrow_right](./media/icon_arrowright.png) |
| `arrow_up`             | ![arrow_up](./media/icon_arrowup.png) |
| `chat`                 | ![chat](./media/icon_chat.png)   |
| `clock`                | ![clock](./media/icon_clock.png) |
| `close`                | ![close](./media/icon_close.png) |
| `delete`               | ![delete](./media/icon_delete.png) |
| `edit`                 | ![edit](./media/icon_edit.png)   |
| `file`                 | ![file](./media/icon_file.png)   |
| `folder`               | ![folder](./media/icon_folder.png) |
| `home`                 | ![home](./media/icon_home.png)   |
| `no_photo`             | ![no_photo](./media/icon_nophoto.png) |
| `refresh`              | ![refresh](./media/icon_refresh.png) |
| `media_player/forward` | ![media_player/forward](./media/icon_forward.png) |
| `media_player/info`    | ![media_player/info](./media/icon_info.png) |
| `media_player/next`    | ![media_player/next](./media/icon_next.png) |
| `media_player/pause`   | ![media_player/pause](./media/icon_pause.png) |
| `media_player/play`    | ![media_player/play](./media/icon_play.png) |
| `media_player/prev`    | ![media_player/prev](./media/icon_prev.png) |
| `media_player/rewind`  | ![media_player/rewind](./media/icon_rewind.png) |
| `media_player/stop`    | ![media_player/stop](./media/icon_stop.png) |
| `menu/apps`            | ![menu/apps](./media/icon_menu_apps.png) |
| `menu/arrow_down`      | ![menu/arrow_down](./media/icon_menu_arrdown.png) |
| `menu/arrow_left`      | ![menu/arrow_left](./media/icon_menu_arrleft.png) |
| `menu/arrow_right`     | ![menu/arrow_right](./media/icon_menu_arrright.png) |
| `menu/arrow_up`        | ![menu/arrow_up](./media/icon_menu_arrup.png) |
| `menu/chat`            | ![menu/chat](./media/icon_menu_chat.png) |
| `menu/clock`           | ![menu/clock](./media/icon_menu_clock.png) |
| `menu/close`           | ![menu/close](./media/icon_menu_close.png) |
| `menu/delete`          | ![menu/delete](./media/icon_menu_delete.png) |
| `menu/edit`            | ![menu/edit](./media/icon_menu_edit.png) |
| `menu/file`            | ![menu/file](./media/icon_menu_file.png) |
| `menu/folder`          | ![menu/folder](./media/icon_menu_folder.png) |
| `menu/home`            | ![menu/home](./media/icon_menu_home.png) |
| `menu/refresh`         | ![menu/refresh](./media/icon_menu_refresh.png) |
| `photo/no_photo`       | ![photo/no_photo](./media/icon_photo_nophoto.png) |
| `toolbar/apps`         | ![toolbar/apps](./media/icon_toolbar_apps.png) |
| `toolbar/arrow_down`   | ![toolbar/arrow_down](./media/icon_toolbar_arrdown.png) |
| `toolbar/arrow_left`   | ![toolbar/arrow_left](./media/icon_toolbar_arrleft.png) |
| `toolbar/arrow_right`  | ![toolbar/arrow_right](./media/icon_toolbar_arrright.png) |
| `toolbar/arrow_up`     | ![toolbar/arrow_up](./media/icon_toolbar_arrup.png) |
| `toolbar/chat`         | ![toolbar/chat](./media/icon_toolbar_chat.png) |
| `toolbar/clock`        | ![toolbar/clock](./media/icon_toolbar_clock.png) |
| `toolbar/close`        | ![toolbar/close](./media/icon_toolbar_close.png) |
| `toolbar/delete`       | ![toolbar/delete](./media/icon_toolbar_delete.png) |
| `toolbar/edit`         | ![toolbar/edit](./media/icon_toolbar_edit.png) |
| `toolbar/file`         | ![toolbar/file](./media/icon_toolbar_file.png) |
| `toolbar/folder`       | ![toolbar/folder](./media/icon_toolbar_folder.png) |
| `toolbar/home`         | ![toolbar/home](./media/icon_toolbar_home.png) |
| `toolbar/more_menu`    | ![toolbar/more_menu](./media/icon_toolbar_moremenu.png) |
| `toolbar/refresh`      | ![toolbar/refresh](./media/icon_toolbar_refresh.png) |

## Callbacks

You can register callback functions connected to the following signals for an icon object.

**Table: Icon callback signals**

| Signal        | Description                              | `event_info` |
|-------------|----------------------------------------|------------|
| `thumb,done`  | The `elm_icon_thumb_set()` function is completed with success. | `NULL`       |
| `thumb,error` | The `elm_icon_thumb_set()` function fails. | `NULL`       |

> **Note**  
> The signal list in the API reference can be more extensive, but only the above signals are actually supported in Tizen.

> **Note**  
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
