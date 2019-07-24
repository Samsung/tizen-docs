# Window of OpenTK

This guide explains how to use `Window` property of `TizenGameApplication` class. Window is internally created in `OnCreate()` method of the base class.

`Window` defines many events including [input event](#input-event), [window related event](#window-related-event), and [render related event](#render-related-event). You can add the event handlers of these events, if needed.

## Input Event

It supposed your application wants to execute some operations while a user is inputting text with a keyboard or selecting some menus with a mouse. You can implement such a use case by adding input event handlers for **key** or **mouse** event using `Window` of OpenTK. For example, if your device supports remote controller, you can use **key** event. If your device supports mouse, you can use **mouse** event.

The following code snippet shows how to add **mouse** and **key** event handlers:

```csharp
private IGameWindow mainWindow;

protected override void OnCreate()
{
    mainWindow = Window;

    mainWindow.MouseMove += MouseMoveEventHandler;    // add event handler on mouse move event
    mainWindow.KeyDown += KeyDownEventHandler;        // add event handler on key down event
}

private void MouseMoveEventHandler(object sender, MouseMoveEventArgs e)
{
    if (e.Mouse[MouseButton.Left])      // get mouse move event which happening with click left button of mouse
    {
        float x = (float)(e.XDelta);    // the move distance in x-axis
        float y = (float)(e.YDelta);    // the move distance in y-axis
        // do your action
    }

    if (e.Mouse[MouseButton.Right])     // get mouse move event which happening with click right button of mouse
    {
        float x = (float)(e.XDelta);    // the move distance in x-axis
        float y = (float)(e.YDelta);    // the move distance in y-axis
        // do your action
    }
}

private void KeyDownEventHandler(object sender, KeyboardKeyEventArgs e)
{
    switch(e.Key)
    {
        case Key.Right:                 // press right key
            // do your action
            break;
        case Key.Left:                  // press left key
            // do your action
            break;
        case Key.Up:                    // press up key
            // do your action
            break;
        case Key.Down:                  // press down key
            // do your action
            break;
        case Key.Number0:               // press number 0 key
            // do your action
            break;
        default:
            break;
    }
}

```

## Window Related Event

`Window` supports some window state related events, such as **Closed**, **Closing**, **FocusedChanged**, **Resize**, **VisibleChanged**, **WindowStateChanged**, and so on.

When the state of `Window` is changed, you can activate some actions by adding your event handlers.

The following code snippet shows adding a resize event handler:

```csharp
private IGameWindow mainWindow;

protected override void OnCreate()
{
    mainWindow = Window;

    mainWindow.Resize += ResizeEventHandler;    // add event handler on window resize event
}

private void ResizeEventHandler(object sender, EventArgs e)
{
    // do your action
}
```

## Render Related Event

`Window` also supports the render related events:

- `RenderFrame`: Occurs when a frame is rendered.
- `UpdateFrame`: Occurs when a frame is updated before `RenderFrame` event occurs.

These events repeatedly occur while the main loop of OpenTK is running.

You can add these events handlers as follows:

```csharp
private IGameWindow mainWindow;

protected override void OnCreate()
{
    mainWindow = Window;

    mainWindow.UpdateFrame += OnUpdateFrame;    // add event handler on update frame event
    mainWindow.RenderFrame += OnRenderFrame;    // add event handler on render frame event
}

private void OnUpdateFrame(Object sender, FrameEventArgs e)
{
    // do actions before render frame if you need
}

private void OnRenderFrame(Object sender, FrameEventArgs e)
{
    // draw your content here

    GL.Viewport(0, 0, mainWindow.Width, mainWindow.Height);
    GL.ClearColor(Color4.White);
    GL.Clear(ClearBufferMask.ColorBufferBit | ClearBufferMask.DepthBufferBit);
    // draw your content ...
    GL.DrawArrays();
    GL.Finish();
    mainWindow.SwapBuffers();
}
```

## Related Information
- Dependencies
  -   Tizen 5.0 and Higher
