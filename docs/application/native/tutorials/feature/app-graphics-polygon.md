# Polygons on the Canvas

You can draw various polygons, such as triangles and pentagons, on a
canvas.

The following example uses the same **Basic UI** template as the square
drawing example. For more information on how to create the project with
the template, see [Squares on the Canvas](app-graphics-square.md).

To implement polygons in an application:

1.  Create a new project and specify the project name as
    **DrawPolygon**.
2. After the project is created, open the `.c` source file in the `src`
    folder and add the new code to the `create_base_gui()` function to
    create a canvas and a triangle.

    The following functions are used to create the triangle:

    -   `evas_object_polygon_add()` creates a polygon object on
        a canvas.
    -   `evas_object_polygon_point_add()` adds point coordinates to a
        polygon object. A polygon must have at least 3 points. The first
        parameter indicates the polygon object, and the second and third
        parameters indicate the X and Y coordinates.
    -   `evas_object_color_set()` specifies a color for a shape. The
        parameters are Red, Green, Blue, and semi-transparency.

    The label is not used in this example, so annotate it.

    ```c++
    /*
       Conformant
       Create and initialize elm_conformant
       elm_conformant is mandatory for the base GUI to have a proper size
       when the indicator or virtual keypad is visible
    */
    ad->conform = elm_conformant_add(ad->win);
    elm_win_indicator_mode_set(ad->win, ELM_WIN_INDICATOR_SHOW);
    elm_win_indicator_opacity_set(ad->win, ELM_WIN_INDICATOR_OPAQUE);
    evas_object_size_hint_weight_set(ad->conform, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
    elm_win_resize_object_add(ad->win, ad->conform);
    evas_object_show(ad->conform);
    /*
       Label
       Create an actual view of the base GUI
       Modify this part to change the view
    */
    #if 0 /* _NOT_USED */
        ad->label = elm_label_add(ad->conform);
        elm_object_text_set(ad->label, "<align=center>Hello Tizen</align>");
        evas_object_size_hint_weight_set(ad->label, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
        elm_object_content_set(ad->conform, ad->label);
    #endif

    /* Canvas */
    Evas* canvas = evas_object_evas_get(ad->win);

    /* Polygon triangle */
    Evas_Object *polygon = evas_object_polygon_add(canvas);
    evas_object_polygon_point_add(polygon, 20, 50);
    evas_object_polygon_point_add(polygon, 170, 150);
    evas_object_polygon_point_add(polygon, 20, 250);
    evas_object_color_set(polygon, 255, 200, 0, 255);
    evas_object_show(polygon);

    /* Show the window after the base GUI is set up */
    evas_object_show(ad->win);
    ```

3. Build and run the application.

    A yellow triangle is displayed on the screen.

    ![Create the project](./media/graphics_triangle.png)

4. Adding 4 points to a polygon object creates a square, while adding 5
    points creates a pentagon.

    Create a pentagon by adding new code to the
    `create_base_gui()` function.

    ```c++
    /* Polygon triangle */
    Evas_Object *polygon = evas_object_polygon_add(canvas);
    evas_object_polygon_point_add(polygon, 20, 50);
    evas_object_polygon_point_add(polygon, 170, 150);
    evas_object_polygon_point_add(polygon, 20, 250);
    evas_object_color_set(polygon, 255, 200, 0, 255);
    evas_object_show(polygon);

    /* Polygon -Pentagon */
    polygon = evas_object_polygon_add(canvas);
    evas_object_polygon_point_add(polygon, 360, 50);
    evas_object_polygon_point_add(polygon, 460, 130);
    evas_object_polygon_point_add(polygon, 410, 230);
    evas_object_polygon_point_add(polygon, 310, 230);
    evas_object_polygon_point_add(polygon, 260, 130);
    evas_object_color_set(polygon, 255, 128, 128, 255);
    evas_object_show(polygon);
    ```

5. Build and run the application again.

    A pink pentagon is displayed next to the yellow triangle.

    ![Create the project](./media/graphics_pentagon.png)
