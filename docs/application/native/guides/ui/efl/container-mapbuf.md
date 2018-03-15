# Mapbuf

A mapbuf component is a container UI component that uses an Evas map to hold a content object. This component is used to improve the moving and resizing performance of complex UI components.

The content object is treated as a single image by the Evas map. If you have a content object containing several child objects, frequently moving the mapbuf component is faster than frequently moving the content object.

The mapbuf component inherits from the container component, which means that container functions can be used on the mapbuf component. The mapbuf component emits no signals.

For more information, see the Mapbuf API (in [mobile](../../../api/mobile/latest/group__Elm__Mapbuf.html) and [wearable](../../../api/wearable/latest/group__Elm__Mapbuf.html) applications).

**Figure: Mapbuf hierarchy**

![Mapbuf hierarchy](./media/mapbuf_tree.png)

## Adding a Mapbuf Component

To create a mapbuf component, use the `elm_mapbuf_add()` function:

```
Evas_Object *mapbuf;
Evas_Object *parent;
Evas_Object *content;

/* Creating a mapbuf */
mapbuf = elm_mapbuf_add(parent);
```

## Adding Content to the Mapbuf

To add content to the mapbuf component, use the `elm_object_content_set()` function with the `default` part:

```
elm_object_content_set(mapbuf, content);
```

> **Note**  
> Calling the `elm_object_content_set(mapbuf, content)` function is equivalent to calling the `elm_object_part_content_set(mapbuf, "default", content)` function.

To activate smooth map rendering and alpha rendering for the mapbuf component:

```
elm_mapbuf_smooth_set(mapbuf, EINA_TRUE);
elm_mapbuf_alpha_set(mapbuf, EINA_TRUE);
```

## Activating the Mapbuf

To use the mapbuf component, activate it:

```
elm_mapbuf_enabled_set(mapbuf, EINA_TRUE);
```

> **Note**  
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
