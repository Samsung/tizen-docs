# Icon

This feature is supported in wearable applications only.

The icon component is used to display standard icon images, such as "delete", "home", and "apps", in an icon context.

The icon component inherits from the image component, which means that image functions can be used on the icon component.

For more information, see the [Icon](../../../../api/wearable/latest/group__Elm__Icon.html) API.

**Figure: Icon hierarchy**

![Icon hierarchy](./media/icon_tree.png)

## Adding an Icon Component

To create an icon component, use the `elm_icon_add()` function.

To set the icon as the [freedesktop.org](http://freedesktop.org) standard `Home` icon, use the `elm_icon_standard_set()` function.

```
Evas_Object *icon;
Evas_Object *parent;

icon = elm_icon_add(parent);
elm_icon_standard_set(icon, "Home");
```

## Changing the Image File

To change the image file:

- You can use an image in the filesystem (for example, `/tmp/Home.png`):

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

## Using the Icon Callbacks

To receive notifications about the icon events, listen for the following signals:

- `thumb,done`: The `elm_icon_thumb_set()` function is completed with success.
- `thumb,error`: The `elm_icon_thumb_set()` function fails.

> **Note**  
> The signal list in the API reference can be more extensive, but only the above signals are actually supported in Tizen.

In both cases, the `event_info` callback parameter is `NULL`.

> **Note**  
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.3.1 and Higher for Wearable
