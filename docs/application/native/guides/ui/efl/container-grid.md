# Grid

The grid container places its elements at specific positions along a fixed grid, where the position of each object is given as a percentage of the full width and height of the grid. For more information, see the Grid API (in [mobile](../../../api/mobile/latest/group__Elm__Grid.html) and [wearable](../../../api/wearable/latest/group__Elm__Grid.html) applications).

**Figure: Grid component structure**

![Grid component structure](./media/grid_concept.png)

## Basic Usage

To build a layout with a grid:

1. Add a grid with the `elm_grid_add()` function:

   ```
   Evas_Object *grid;

   grid = elm_grid_add(parent);
   ```

2. Set the size of the grid with the `elm_grid_size_set()` function. The size is 100 x 100 by default.

   ```
   grid = elm_grid_size_set(grid, 20, 30);
   ```

3. Add objects and pack them into the grid with the `elm_grid_pack()` function:

   ```
   Evas_Object *button;

   elm_grid_pack(grid, button, 0, 0, 10, 10);
   ```

The following example shows a simple use case of the grid component.

**Example: Grid use case**

 ![Grid](./media/grid2.png)

```
Evas_Object *win;
Evas_Object *conf;
Evas_Object *nf;
Evas_Object *grid;
Evas_Object *button;

/* Starting right after the basic EFL UI layout code */
/* (win - conformant - naviframe) */

/* Add a grid to contain buttons and push the grid into the naviframe */
grid = elm_grid_add(nf);
elm_object_content_set(nf, grid);
evas_object_show(grid);
elm_naviframe_item_push(nf, "Grid", NULL, NULL, grid, NULL);

/* Add a button to the grid */
button = elm_button_add(grid);
elm_object_text_set(button, "Button1");
elm_grid_pack(grid, button, 10, 10, 40, 20);
evas_object_show(button);

/* Add a button to the grid */
button = elm_button_add(grid);
elm_object_text_set(button, "Button2");
elm_grid_pack(grid, button, 50, 50, 40, 30);
evas_object_show(button);

/* Add a button to the grid */
button = elm_button_add(grid);
elm_object_text_set(button, "Button3");
elm_grid_pack(grid, button, 10, 80, 30, 10);
evas_object_show(button);
```

> **Note**  
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
