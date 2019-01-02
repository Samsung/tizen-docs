# Window of OpenTK

In the OpenTK app, `OpenTKGameApplication` creates a `Window` after `OnCreate` method is called. `Window` is a
property of `TizenGameApplication`. This document will describe how to use this `Window` in your OpenTK app.

`Window` defines many events including [input event](#input-event), [window related event](#window-related-event), and
[render related event](#render-related-event). You can add the event handlers of these events, if needed.

## Input Event

There are app scenarios, where you want to do some actions while the app user inputs something. In this scenario, you can add an event handler on the input event of `Window`. Also, you can use **key** or **mouse** event using `Window` of OpenTK, if your device supports them. For example, if your device supports remote controller, then you can use **key** event. If your device supports mouse, then you can use **mouse** event.

The following is the sample code:

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

`Window` also provides some window state related events, such as **Closed**, **Closing**, **FocusedChanged**, **Resize**, **VisibleChanged**, **WindowStateChanged**, and so on. 

In some scenario, if you want to mirror the state of `Window`, then you can add event handlers on these events.

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

`Window` also provides the render related events:

- `RenderFrame`: This event occurs when a frame is rendered.
- `UpdateFrame`: This event occurs when a frame is updated before `RenderFrame` event occurs.

These events repeatedly occur while the main loop of OpenTK is running.

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
