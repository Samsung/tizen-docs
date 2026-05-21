### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## Window Class

Represents a window on the screen.

```csharp
public class Window : Tizen.UI.NObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; Window
### Constructors

<a name='Tizen.UI.Window.Window()'></a>

## Window() Constructor

Initializes a new instance of the [Window](Tizen.UI.Window.md 'Tizen.UI.Window') class.

```csharp
public Window();
```

<a name='Tizen.UI.Window.Window(string)'></a>

## Window(string) Constructor

Initializes a new instance of the [Window](Tizen.UI.Window.md 'Tizen.UI.Window') class.

```csharp
public Window(string name);
```
#### Parameters

<a name='Tizen.UI.Window.Window(string).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the window.

<a name='Tizen.UI.Window.Window(string,bool)'></a>

## Window(string, bool) Constructor

Initializes a new instance of the [Window](Tizen.UI.Window.md 'Tizen.UI.Window') class.

```csharp
public Window(string name, bool isTranslucent);
```
#### Parameters

<a name='Tizen.UI.Window.Window(string,bool).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the window.

<a name='Tizen.UI.Window.Window(string,bool).isTranslucent'></a>

`isTranslucent` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

A value indicating whether the window is translucent.
### Properties

<a name='Tizen.UI.Window.BorderArea'></a>

## Window.BorderArea Property

Gets or sets the border area of the window.

```csharp
public Tizen.UI.Thickness BorderArea { get; set; }
```

#### Property Value
[Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

<a name='Tizen.UI.Window.Default'></a>

## Window.Default Property

Gets the default window.

```csharp
public static Tizen.UI.Window Default { get; set; }
```

#### Property Value
[Window](Tizen.UI.Window.md 'Tizen.UI.Window')

<a name='Tizen.UI.Window.DefaultLayer'></a>

## Window.DefaultLayer Property

Gets the default layer of the window.

```csharp
public Tizen.UI.Layer DefaultLayer { get; }
```

#### Property Value
[Layer](Tizen.UI.Layer.md 'Tizen.UI.Layer')

<a name='Tizen.UI.Window.DPI'></a>

## Window.DPI Property

Gets the DPI of the window.

```csharp
public int DPI { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Window.IsMaximized'></a>

## Window.IsMaximized Property

Gets whether the window is maximized or not.

```csharp
public bool IsMaximized { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Window.IsMinimized'></a>

## Window.IsMinimized Property

Gets whether the window is minimized or not.

```csharp
public bool IsMinimized { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Window.IsVisible'></a>

## Window.IsVisible Property

Gets a value indicating whether the window is visible.

```csharp
public bool IsVisible { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Window.Layers'></a>

## Window.Layers Property

Gets the list of child layers

```csharp
public System.Collections.Generic.IReadOnlyList&lt;Tizen.UI.Layer> Layers { get; }
```

#### Property Value
[System.Collections.Generic.IReadOnlyList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyList-1 'System.Collections.Generic.IReadOnlyList`1')[Layer](Tizen.UI.Layer.md 'Tizen.UI.Layer')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyList-1 'System.Collections.Generic.IReadOnlyList`1')

<a name='Tizen.UI.Window.Title'></a>

## Window.Title Property

Gets or sets a title of window.

```csharp
public string Title { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Window.WindowType'></a>

## Window.WindowType Property

Gets or sets a window type.  
Most of window type can be set to use WindowType, except for IME type.  
IME type can be set to use one of NUIApplication's constrcutors.

```csharp
public Tizen.UI.WindowType WindowType { get; set; }
```

#### Property Value
[WindowType](Tizen.UI.WindowType.md 'Tizen.UI.WindowType')
### Methods

<a name='Tizen.UI.Window.Activate()'></a>

## Window.Activate() Method

Activates the window.

```csharp
public void Activate();
```

<a name='Tizen.UI.Window.Add(Tizen.UI.Layer)'></a>

## Window.Add(Layer) Method

Adds a layer to the window.

```csharp
public void Add(Tizen.UI.Layer layer);
```
#### Parameters

<a name='Tizen.UI.Window.Add(Tizen.UI.Layer).layer'></a>

`layer` [Layer](Tizen.UI.Layer.md 'Tizen.UI.Layer')

The layer to add.

<a name='Tizen.UI.Window.AddAuxiliaryHint(string,string)'></a>

## Window.AddAuxiliaryHint(string, string) Method

Adds an auxiliary hint to the window.

```csharp
public uint AddAuxiliaryHint(string hint, string value);
```
#### Parameters

<a name='Tizen.UI.Window.AddAuxiliaryHint(string,string).hint'></a>

`hint` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The auxiliary hint string.

<a name='Tizen.UI.Window.AddAuxiliaryHint(string,string).value'></a>

`value` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The value string for the auxiliary hint.

#### Returns
[System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')  
The ID of the new auxiliary hint on success, 0 on failure.

<a name='Tizen.UI.Window.AddAvailableOrientation(Tizen.UI.WindowOrientation)'></a>

## Window.AddAvailableOrientation(WindowOrientation) Method

Adds an available orientation to the window.

```csharp
public void AddAvailableOrientation(Tizen.UI.WindowOrientation orientation);
```
#### Parameters

<a name='Tizen.UI.Window.AddAvailableOrientation(Tizen.UI.WindowOrientation).orientation'></a>

`orientation` [WindowOrientation](Tizen.UI.WindowOrientation.md 'Tizen.UI.WindowOrientation')

The orientation to add.

<a name='Tizen.UI.Window.AddFrameUpdateCallback(Tizen.UI.FrameUpdateCallback)'></a>

## Window.AddFrameUpdateCallback(FrameUpdateCallback) Method

Adds a frame update callback to the window.

```csharp
public void AddFrameUpdateCallback(Tizen.UI.FrameUpdateCallback frameUpdateCallback);
```
#### Parameters

<a name='Tizen.UI.Window.AddFrameUpdateCallback(Tizen.UI.FrameUpdateCallback).frameUpdateCallback'></a>

`frameUpdateCallback` [FrameUpdateCallback](Tizen.UI.FrameUpdateCallback.md 'Tizen.UI.FrameUpdateCallback')

The frame update callback to add.

<a name='Tizen.UI.Window.FeedHover(Tizen.UI.TouchPoint)'></a>

## Window.FeedHover(TouchPoint) Method

Feeds a hover event into the window.

```csharp
public void FeedHover(Tizen.UI.TouchPoint touchPoint=null);
```
#### Parameters

<a name='Tizen.UI.Window.FeedHover(Tizen.UI.TouchPoint).touchPoint'></a>

`touchPoint` [TouchPoint](Tizen.UI.TouchPoint.md 'Tizen.UI.TouchPoint')

The touch point to feed hover event. If null is entered, the feed hover event is generated with the last inputed touch point.

<a name='Tizen.UI.Window.FeedKey(Tizen.UI.KeyEvent)'></a>

## Window.FeedKey(KeyEvent) Method

Feeds a key event to the window.

```csharp
public void FeedKey(Tizen.UI.KeyEvent keyEvent);
```
#### Parameters

<a name='Tizen.UI.Window.FeedKey(Tizen.UI.KeyEvent).keyEvent'></a>

`keyEvent` [KeyEvent](Tizen.UI.KeyEvent.md 'Tizen.UI.KeyEvent')

The key event to feed.

<a name='Tizen.UI.Window.FeedTouch(Tizen.UI.TouchPoint,int)'></a>

## Window.FeedTouch(TouchPoint, int) Method

Feeds a touch point into the window.

```csharp
public void FeedTouch(Tizen.UI.TouchPoint touchPoint, int timeStamp);
```
#### Parameters

<a name='Tizen.UI.Window.FeedTouch(Tizen.UI.TouchPoint,int).touchPoint'></a>

`touchPoint` [TouchPoint](Tizen.UI.TouchPoint.md 'Tizen.UI.TouchPoint')

The touch point to feed.

<a name='Tizen.UI.Window.FeedTouch(Tizen.UI.TouchPoint,int).timeStamp'></a>

`timeStamp` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The timeStamp.

<a name='Tizen.UI.Window.GetAuxiliaryHint(string)'></a>

## Window.GetAuxiliaryHint(string) Method

Gets the value of the specified auxiliary hint string of the window.

```csharp
public string GetAuxiliaryHint(string hint);
```
#### Parameters

<a name='Tizen.UI.Window.GetAuxiliaryHint(string).hint'></a>

`hint` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The auxiliary hint string to be searched.

#### Returns
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
The value of the specified auxiliary hint string, or an empty string if the specified hint is not found.

<a name='Tizen.UI.Window.GetClientSize()'></a>

## Window.GetClientSize() Method

Gets the size of the client area of the window.

```csharp
public Tizen.UI.Size GetClientSize();
```

#### Returns
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')  
The size of the client area.

<a name='Tizen.UI.Window.GetCurrentOrientation()'></a>

## Window.GetCurrentOrientation() Method

Gets the current orientation of the window.

```csharp
public Tizen.UI.WindowOrientation GetCurrentOrientation();
```

#### Returns
[WindowOrientation](Tizen.UI.WindowOrientation.md 'Tizen.UI.WindowOrientation')  
The current orientation of the window.

<a name='Tizen.UI.Window.GetLastHoverEvent()'></a>

## Window.GetLastHoverEvent() Method

Retrieves the last hover event that occurred on the window.

```csharp
public Tizen.UI.HoverEvent GetLastHoverEvent();
```

#### Returns
[HoverEvent](Tizen.UI.HoverEvent.md 'Tizen.UI.HoverEvent')  
The last hover event that occurred on the window.

<a name='Tizen.UI.Window.GetLastKeyEvent()'></a>

## Window.GetLastKeyEvent() Method

Retrieves the last key event that was received by the window.

```csharp
public Tizen.UI.KeyEvent GetLastKeyEvent();
```

#### Returns
[KeyEvent](Tizen.UI.KeyEvent.md 'Tizen.UI.KeyEvent')  
The last key event received by the window.

<a name='Tizen.UI.Window.GetLastTouchEvent()'></a>

## Window.GetLastTouchEvent() Method

Retrieves the last touch event that occurred on the window.

```csharp
public Tizen.UI.TouchEvent GetLastTouchEvent();
```

#### Returns
[TouchEvent](Tizen.UI.TouchEvent.md 'Tizen.UI.TouchEvent')  
The last touch event that occurred on the window.

<a name='Tizen.UI.Window.GetNativeWindowHandle()'></a>

## Window.GetNativeWindowHandle() Method

Gets the native window handle of the Window object.

```csharp
public System.IntPtr GetNativeWindowHandle();
```

#### Returns
[System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')  
The native window handle.

<a name='Tizen.UI.Window.GetPosition()'></a>

## Window.GetPosition() Method

Gets the position of the window.

```csharp
public Tizen.UI.Point GetPosition();
```

#### Returns
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')  
The position of the window.

<a name='Tizen.UI.Window.GetSize()'></a>

## Window.GetSize() Method

Gets the size of the window.

```csharp
public Tizen.UI.Size GetSize();
```

#### Returns
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')  
The size of the window.

<a name='Tizen.UI.Window.GetWindow(Tizen.UI.Layer)'></a>

## Window.GetWindow(Layer) Method

Gets the window associated with the specified layer.

```csharp
public static Tizen.UI.Window GetWindow(Tizen.UI.Layer layer);
```
#### Parameters

<a name='Tizen.UI.Window.GetWindow(Tizen.UI.Layer).layer'></a>

`layer` [Layer](Tizen.UI.Layer.md 'Tizen.UI.Layer')

The layer to get the window from.

#### Returns
[Window](Tizen.UI.Window.md 'Tizen.UI.Window')  
The window associated with the specified layer.

<a name='Tizen.UI.Window.GetWindow(Tizen.UI.View)'></a>

## Window.GetWindow(View) Method

Gets the window that contains the specified view.

```csharp
public static Tizen.UI.Window GetWindow(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.Window.GetWindow(Tizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to search for its parent window.

#### Returns
[Window](Tizen.UI.Window.md 'Tizen.UI.Window')  
The window that contains the specified view, or null if the view is not currently added to any window.

<a name='Tizen.UI.Window.GrabKey(int,Tizen.UI.KeyGrabMode)'></a>

## Window.GrabKey(int, KeyGrabMode) Method

Grabs the key specified by a key for a window in a GrabMode. <br/>  
Details: This function can be used for following example scenarios: <br/>  
- TV - A user might want to change the volume or channel of the background TV contents while focusing on the foregrund app. <br/>  
- Mobile - When a user presses the Home key, the homescreen appears regardless of the current foreground app. <br/>  
- Mobile - Using the volume up or down as zoom up or down in camera apps. <br/>

```csharp
public bool GrabKey(int keyCode, Tizen.UI.KeyGrabMode mode);
```
#### Parameters

<a name='Tizen.UI.Window.GrabKey(int,Tizen.UI.KeyGrabMode).keyCode'></a>

`keyCode` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The key code to grab.

<a name='Tizen.UI.Window.GrabKey(int,Tizen.UI.KeyGrabMode).mode'></a>

`mode` [KeyGrabMode](Tizen.UI.KeyGrabMode.md 'Tizen.UI.KeyGrabMode')

The grab mode for the key.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the grab succeeds.

#### Exceptions

[System.UnauthorizedAccessException](https://docs.microsoft.com/en-us/dotnet/api/System.UnauthorizedAccessException 'System.UnauthorizedAccessException')  
This exception can be thrown due to permission denied.

<a name='Tizen.UI.Window.Hide()'></a>

## Window.Hide() Method

Hides the window.

```csharp
public void Hide();
```

<a name='Tizen.UI.Window.KeepRendering(float)'></a>

## Window.KeepRendering(float) Method

Keeps rendering the window for the specified duration in seconds.

```csharp
public void KeepRendering(float durationSeconds);
```
#### Parameters

<a name='Tizen.UI.Window.KeepRendering(float).durationSeconds'></a>

`durationSeconds` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The duration in seconds to keep rendering.

<a name='Tizen.UI.Window.Lower()'></a>

## Window.Lower() Method

Lowers the window to the bottom of the window stack.

```csharp
public void Lower();
```

<a name='Tizen.UI.Window.LowerLayerToBottom(Tizen.UI.Layer)'></a>

## Window.LowerLayerToBottom(Layer) Method

Lowers a layer to the bottom of the window.

```csharp
public void LowerLayerToBottom(Tizen.UI.Layer layer);
```
#### Parameters

<a name='Tizen.UI.Window.LowerLayerToBottom(Tizen.UI.Layer).layer'></a>

`layer` [Layer](Tizen.UI.Layer.md 'Tizen.UI.Layer')

The layer to lower.

<a name='Tizen.UI.Window.Maximize(bool)'></a>

## Window.Maximize(bool) Method

Sets whether the window is maximized or not.

```csharp
public void Maximize(bool enable);
```
#### Parameters

<a name='Tizen.UI.Window.Maximize(bool).enable'></a>

`enable` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True if the window should be maximized, false otherwise.

<a name='Tizen.UI.Window.Minimize(bool)'></a>

## Window.Minimize(bool) Method

Sets whether the window is minimized or not.

```csharp
public void Minimize(bool enable);
```
#### Parameters

<a name='Tizen.UI.Window.Minimize(bool).enable'></a>

`enable` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True if the window can be minimized, false otherwise.

<a name='Tizen.UI.Window.Raise()'></a>

## Window.Raise() Method

Raises the window to the top of the window stack.

```csharp
public void Raise();
```

<a name='Tizen.UI.Window.RaiseLayerToTop(Tizen.UI.Layer)'></a>

## Window.RaiseLayerToTop(Layer) Method

Raises a layer to the top of the window.

```csharp
public void RaiseLayerToTop(Tizen.UI.Layer layer);
```
#### Parameters

<a name='Tizen.UI.Window.RaiseLayerToTop(Tizen.UI.Layer).layer'></a>

`layer` [Layer](Tizen.UI.Layer.md 'Tizen.UI.Layer')

The layer to raise.

<a name='Tizen.UI.Window.Remove(Tizen.UI.Layer)'></a>

## Window.Remove(Layer) Method

Removes a layer from the window.

```csharp
public void Remove(Tizen.UI.Layer layer);
```
#### Parameters

<a name='Tizen.UI.Window.Remove(Tizen.UI.Layer).layer'></a>

`layer` [Layer](Tizen.UI.Layer.md 'Tizen.UI.Layer')

The layer to remove.

<a name='Tizen.UI.Window.RemoveAvailableOrientation(Tizen.UI.WindowOrientation)'></a>

## Window.RemoveAvailableOrientation(WindowOrientation) Method

Removes an available orientation from the window.

```csharp
public void RemoveAvailableOrientation(Tizen.UI.WindowOrientation orientation);
```
#### Parameters

<a name='Tizen.UI.Window.RemoveAvailableOrientation(Tizen.UI.WindowOrientation).orientation'></a>

`orientation` [WindowOrientation](Tizen.UI.WindowOrientation.md 'Tizen.UI.WindowOrientation')

The orientation to remove.

<a name='Tizen.UI.Window.RemoveFrameUpdateCallback(Tizen.UI.FrameUpdateCallback)'></a>

## Window.RemoveFrameUpdateCallback(FrameUpdateCallback) Method

Removes a frame update callback from the window.

```csharp
public void RemoveFrameUpdateCallback(Tizen.UI.FrameUpdateCallback frameUpdateCallbck);
```
#### Parameters

<a name='Tizen.UI.Window.RemoveFrameUpdateCallback(Tizen.UI.FrameUpdateCallback).frameUpdateCallbck'></a>

`frameUpdateCallbck` [FrameUpdateCallback](Tizen.UI.FrameUpdateCallback.md 'Tizen.UI.FrameUpdateCallback')

<a name='Tizen.UI.Window.SetBackgroundColor(Tizen.UI.Color)'></a>

## Window.SetBackgroundColor(Color) Method

Sets the background color of the window.

```csharp
public void SetBackgroundColor(Tizen.UI.Color color);
```
#### Parameters

<a name='Tizen.UI.Window.SetBackgroundColor(Tizen.UI.Color).color'></a>

`color` [Color](Tizen.UI.Color.md 'Tizen.UI.Color')

The background color of the window.

<a name='Tizen.UI.Window.SetFocusSkip(bool)'></a>

## Window.SetFocusSkip(bool) Method

Sets whether to skip focus on window.

```csharp
public void SetFocusSkip(bool skip);
```
#### Parameters

<a name='Tizen.UI.Window.SetFocusSkip(bool).skip'></a>

`skip` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True to skip focus on window, otherwise false.

<a name='Tizen.UI.Window.SetInputRegion(Tizen.UI.Rect)'></a>

## Window.SetInputRegion(Rect) Method

Sets the input region for the window to receive touch events.

```csharp
public void SetInputRegion(Tizen.UI.Rect region);
```
#### Parameters

<a name='Tizen.UI.Window.SetInputRegion(Tizen.UI.Rect).region'></a>

`region` [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

A rectangular area that defines where touch events will be received by this window.  
            Touches outside this region will be passed to windows located behind this window.

<a name='Tizen.UI.Window.SetMaximumSize(int,int)'></a>

## Window.SetMaximumSize(int, int) Method

Sets the maximum size of the window.

```csharp
public void SetMaximumSize(int width, int height);
```
#### Parameters

<a name='Tizen.UI.Window.SetMaximumSize(int,int).width'></a>

`width` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The maximum width of the window.

<a name='Tizen.UI.Window.SetMaximumSize(int,int).height'></a>

`height` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The maximum height of the window.

<a name='Tizen.UI.Window.SetMinimumSize(int,int)'></a>

## Window.SetMinimumSize(int, int) Method

Sets the minimum size of the window.

```csharp
public void SetMinimumSize(int width, int height);
```
#### Parameters

<a name='Tizen.UI.Window.SetMinimumSize(int,int).width'></a>

`width` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The minimum width of the window.

<a name='Tizen.UI.Window.SetMinimumSize(int,int).height'></a>

`height` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The minimum height of the window.

<a name='Tizen.UI.Window.SetPosition(Tizen.UI.Point)'></a>

## Window.SetPosition(Point) Method

Sets the position of the window.

```csharp
public void SetPosition(Tizen.UI.Point position);
```
#### Parameters

<a name='Tizen.UI.Window.SetPosition(Tizen.UI.Point).position'></a>

`position` [Point](Tizen.UI.Point.md 'Tizen.UI.Point')

The position of the window.

<a name='Tizen.UI.Window.SetPositionSize(int,int,int,int)'></a>

## Window.SetPositionSize(int, int, int, int) Method

Sets the position and size of the window.

```csharp
public void SetPositionSize(int x, int y, int width, int height);
```
#### Parameters

<a name='Tizen.UI.Window.SetPositionSize(int,int,int,int).x'></a>

`x` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The x-coordinate of the window.

<a name='Tizen.UI.Window.SetPositionSize(int,int,int,int).y'></a>

`y` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The y-coordinate of the window.

<a name='Tizen.UI.Window.SetPositionSize(int,int,int,int).width'></a>

`width` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The width of the window.

<a name='Tizen.UI.Window.SetPositionSize(int,int,int,int).height'></a>

`height` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The height of the window.

<a name='Tizen.UI.Window.SetPreferredOrientation(Tizen.UI.WindowOrientation)'></a>

## Window.SetPreferredOrientation(WindowOrientation) Method

Sets the preferred orientation of the window.

```csharp
public void SetPreferredOrientation(Tizen.UI.WindowOrientation orientation);
```
#### Parameters

<a name='Tizen.UI.Window.SetPreferredOrientation(Tizen.UI.WindowOrientation).orientation'></a>

`orientation` [WindowOrientation](Tizen.UI.WindowOrientation.md 'Tizen.UI.WindowOrientation')

The preferred orientation.

<a name='Tizen.UI.Window.SetSize(Tizen.UI.Size)'></a>

## Window.SetSize(Size) Method

Sets the size of the window.

```csharp
public void SetSize(Tizen.UI.Size size);
```
#### Parameters

<a name='Tizen.UI.Window.SetSize(Tizen.UI.Size).size'></a>

`size` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The size of the window.

<a name='Tizen.UI.Window.SetSize(ushort,ushort)'></a>

## Window.SetSize(ushort, ushort) Method

Sets the size of the window.

```csharp
public void SetSize(ushort width, ushort height);
```
#### Parameters

<a name='Tizen.UI.Window.SetSize(ushort,ushort).width'></a>

`width` [System.UInt16](https://docs.microsoft.com/en-us/dotnet/api/System.UInt16 'System.UInt16')

The width of the window.

<a name='Tizen.UI.Window.SetSize(ushort,ushort).height'></a>

`height` [System.UInt16](https://docs.microsoft.com/en-us/dotnet/api/System.UInt16 'System.UInt16')

The height of the window.

<a name='Tizen.UI.Window.SetTransparency(bool)'></a>

## Window.SetTransparency(bool) Method

Sets the transparency of the window.

```csharp
public void SetTransparency(bool transparent);
```
#### Parameters

<a name='Tizen.UI.Window.SetTransparency(bool).transparent'></a>

`transparent` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True if the window should be transparent, false otherwise.

<a name='Tizen.UI.Window.SetWindowResizePolicy(Tizen.UI.WindowResizePolicy)'></a>

## Window.SetWindowResizePolicy(WindowResizePolicy) Method

Sets the window resize policy.

```csharp
public void SetWindowResizePolicy(Tizen.UI.WindowResizePolicy policy);
```
#### Parameters

<a name='Tizen.UI.Window.SetWindowResizePolicy(Tizen.UI.WindowResizePolicy).policy'></a>

`policy` [WindowResizePolicy](Tizen.UI.WindowResizePolicy.md 'Tizen.UI.WindowResizePolicy')

The window resize policy to set.

<a name='Tizen.UI.Window.Show()'></a>

## Window.Show() Method

Shows the window.

```csharp
public void Show();
```

<a name='Tizen.UI.Window.StartMoveRequest()'></a>

## Window.StartMoveRequest() Method

Starts the move request for the window.

```csharp
public System.Threading.Tasks.Task StartMoveRequest();
```

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')  
An awaitable Task.

<a name='Tizen.UI.Window.StartResizeRequest(Tizen.UI.WindowResizeDirection)'></a>

## Window.StartResizeRequest(WindowResizeDirection) Method

Starts a window resize request with the specified direction.

```csharp
public System.Threading.Tasks.Task StartResizeRequest(Tizen.UI.WindowResizeDirection direction);
```
#### Parameters

<a name='Tizen.UI.Window.StartResizeRequest(Tizen.UI.WindowResizeDirection).direction'></a>

`direction` [WindowResizeDirection](Tizen.UI.WindowResizeDirection.md 'Tizen.UI.WindowResizeDirection')

The direction of the window resize.

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')  
An awaitable Task.

<a name='Tizen.UI.Window.UngrabKey(int)'></a>

## Window.UngrabKey(int) Method

Ungrabs the key specified by a key for a window.<br/>  
Note: If this function is called between key down and up events of a grabbed key, an application doesn't receive the key up event. <br/>

```csharp
public bool UngrabKey(int keyCode);
```
#### Parameters

<a name='Tizen.UI.Window.UngrabKey(int).keyCode'></a>

`keyCode` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The key code to ungrab.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the ungrab succeeds.

#### Exceptions

[System.UnauthorizedAccessException](https://docs.microsoft.com/en-us/dotnet/api/System.UnauthorizedAccessException 'System.UnauthorizedAccessException')  
This exception can be thrown due to permission denied.
### Events

<a name='Tizen.UI.Window.FocusChanged'></a>

## Window.FocusChanged Event

Occurs when the window receives or losts focus.

```csharp
public event EventHandler&lt;WindowFocusChangedEventArgs> FocusChanged;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[WindowFocusChangedEventArgs](Tizen.UI.WindowFocusChangedEventArgs.md 'Tizen.UI.WindowFocusChangedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Window.HoverEvent'></a>

## Window.HoverEvent Event

Occurs when the mouse hovers over the window.

```csharp
public event EventHandler&lt;HoverEventArgs> HoverEvent;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[HoverEventArgs](Tizen.UI.HoverEventArgs.md 'Tizen.UI.HoverEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Window.InterceptTouchEvent'></a>

## Window.InterceptTouchEvent Event

Event that allows the window to intercept touch events before passing them to child views.

```csharp
public event EventHandler&lt;TouchEventArgs> InterceptTouchEvent;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[TouchEventArgs](Tizen.UI.TouchEventArgs.md 'Tizen.UI.TouchEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Window.InterceptWheelEvent'></a>

## Window.InterceptWheelEvent Event

Event that allows the window to intercept wheel events before passing them to child views.

```csharp
public event EventHandler&lt;WheelEventArgs> InterceptWheelEvent;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[WheelEventArgs](Tizen.UI.WheelEventArgs.md 'Tizen.UI.WheelEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Window.KeyEvent'></a>

## Window.KeyEvent Event

Occurs when a key event is received.

```csharp
public event EventHandler&lt;KeyEventArgs> KeyEvent;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[KeyEventArgs](Tizen.UI.KeyEventArgs.md 'Tizen.UI.KeyEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Window.Moved'></a>

## Window.Moved Event

Occurs when the window is moved.

```csharp
public event EventHandler Moved;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Window.Resized'></a>

## Window.Resized Event

Occurs when the window is resized.

```csharp
public event EventHandler Resized;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Window.TouchEvent'></a>

## Window.TouchEvent Event

Occurs when a touch event is received.

```csharp
public event EventHandler&lt;TouchEventArgs> TouchEvent;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[TouchEventArgs](Tizen.UI.TouchEventArgs.md 'Tizen.UI.TouchEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Window.VisibilityChanged'></a>

## Window.VisibilityChanged Event

Occurs when the window show or hide

```csharp
public event EventHandler VisibilityChanged;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Window.WheelEvent'></a>

## Window.WheelEvent Event

Occurs when the wheel event is fired.

```csharp
public event EventHandler&lt;WheelEventArgs> WheelEvent;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[WheelEventArgs](Tizen.UI.WheelEventArgs.md 'Tizen.UI.WheelEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')




