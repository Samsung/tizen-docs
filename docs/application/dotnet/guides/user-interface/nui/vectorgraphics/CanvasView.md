# CanvasView

A CanvasView is NUI control that displays a vector primitives.

## Create a CanvasView

1. To create a canvas view:

    ```cs
    using Tizen.NUI;
    using Tizen.NUI.BaseComponents.VectorGraphics;
    ```

2.  Create an instance of the `CanvasView` class.

    ```cs
    CanvasView canvsView = new CanvasView();
    Window.Instance.Add(imageView);
    ```

    Create an instance of the `CanvasView` class with viewBox Size

    ```cs
    Size2d viewBox = new Size2D(100, 100);
    CanvasView canvsView = new CanvasView(viewBox);
    Window.Instance.Add(canvasView);
    ```

The `viewBox` is the drawing area inside the `CanvasView`. `Drawables` drawn inside the `CanvasView` are affected by the `size` of the `viewBox`. This is a kind of internal coordinate system.

![CanvasViewAndViewBox](./media/vectorgraphics_canvasview.png)

If the size of `CanvasView` and `viewBox` are the same, the size of the primitive drawn inside is the same as the value set by the application.<br>
However, if the `viewbox` size is larger than the `CanvasView` size, the actual primitive size becomes smaller. Conversely, if the `viewBox` size is smaller than the `CanvasView` size, the primitive is drawn larger.

## Related Information
- Dependencies
  -   Tizen 6.5 and Higher


