# Window of OpenTK

In `OpenTK` application, `OpenTKGameApplication` creates a `Window` after calling `OnCreate` method. The `Window` is provided
as a property of `TizenGameApplication`. This document will describe how to use this `Window` in your `OpenTK` application.

`Window` defines many events, including: [input event](#input-event), [window related](#window-related-event), 
[render related event](#render-related-event), you can add event handlers on those event if you need.

## Input Event

In some app scenario, you want to do some actions while an app user input something. To do this, you can add event hander on the input event of `Window`. Also, you can use `key` and `mouse` event through using `Window` of `OpenTK` if a device supports both of them.

```C#
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

## Window related Event

`Window` also provides some window state related events such as `Closed`, `Closing`, `FocusedChanged`, `Resize`, `VisibleChanged`, `WindowStateChanged`, etc. In some scenario, you may want to mirror the state of `Window`, then 
you can add event handlers on these events.

```C#
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

## Render related Event

`Window` also provides the render ralated events, including: `UpdateFrame`, `RenderFrame`.
`RenderFrame` event occurs when it is time to render a frame; `UpdateFrame` event occurs when a frame is updated
before `RenderFrame` event occurs. These events will occur repeatedly while OpenTK's main loop is running.
```C#
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
    
    //GL.Viewport(0, 0, mainWindow.Width, mainWindow.Height);
    //GL.ClearColor(Color4.White);
    //GL.Clear(ClearBufferMask.ColorBufferBit | ClearBufferMask.DepthBufferBit);
    ...
    //GL.DrawArrays();
    //GL.Finish();
    //mainWindow.SwapBuffers();
}
```
