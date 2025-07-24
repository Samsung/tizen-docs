# Circle Surface

This feature is supported in wearable applications only.

The circle surface component manages and renders [circle objects](component-circle-object.md). Multiple circle objects can be connected to 1 circle surface as candidates of an object to be rendered. When 1 circle object is set as visible, the surface renders the circle object and hides the others.

For more information, see the [Efl Extension Circle Surface](../../../../api/wearable/latest/group__CAPI__EFL__EXTENSION__CIRCLE__SURFACE__MODULE.html) API.

## Adding a Circle Surface Component

To create a new circle surface:

- Create a circle surface in the conformant layer using the `eext_circle_surface_conformant_add()` function:

  ```
  Eext_Circle_Surface *surface;
  Evas_Object *conformant;

  conformant = elm_conformant_add(parent);
  surface = eext_circle_surface_conformant_add(conformant);
  ```

- Create a circle surface in the layout layer using the `eext_circle_surface_layout_add()` function:

  ```
  Eext_Circle_Surface *surface;
  Evas_Object *layout;

  layout = elm_layout_add(parent);
  surface = eext_circle_surface_layout_add(layout);
  ```

- Create a circle surface in the naviframe layer using the `eext_circle_surface_naviframe_add()` function:

  ```
  Eext_Circle_Surface *surface;
  Evas_Object *naviframe;

  naviframe = elm_naviframe_add(parent);
  surface = eext_circle_surface_naviframe_add(naviframe);
  ```

> **Note**  
> A circle surface is a non-graphical object. It adds no graphics to or around the objects it holds.

## Adding Circle Objects to the Circle Surface

You can add any circle objects to a circle surface.

To create a circle slider (`eext_slider`) component and add it to a circle surface in the conformant layer:

```
Eext_Circle_Surface *surface;
Evas_Object *slider;

surface = eext_circle_surface_conformant_add(conformant);
slider = eext_circle_object_slider_add(parent, surface);
```

## Deleting the Circle Surface

Deleting the Evas object (conformant, layout, or naviframe) automatically deletes the circle surface in the same layer.

You can, however, explicitly use the `eext_circle_surface_del()` function to delete a circle surface:

```
eext_circle_surface_del(surface);
```

> **Note**    
> The `eext_circle_surface_del()` function does not delete the connected circle objects.

## Related Information
- Dependencies
  - Tizen 2.3.1 and Higher for Wearable
