### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## View Class

The View class is a base class for other more specific UI components, such as buttons, text fields, and layouts.

```csharp
public class View : Tizen.UI.NObject,
Tizen.UI.Internal.IViewSignalHandler
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; View

Derived  
&#8627; [ContentView](Tizen.UI.ContentView.md 'Tizen.UI.ContentView')  
&#8627; [ImageView](Tizen.UI.ImageView.md 'Tizen.UI.ImageView')  
&#8627; [InputView](Tizen.UI.InputView.md 'Tizen.UI.InputView')  
&#8627; [TbmSurfaceView](Tizen.UI.TbmSurfaceView.md 'Tizen.UI.TbmSurfaceView')  
&#8627; [TextView](Tizen.UI.TextView.md 'Tizen.UI.TextView')  
&#8627; [VideoOverlayView](Tizen.UI.VideoOverlayView.md 'Tizen.UI.VideoOverlayView')  
&#8627; [ViewGroup](Tizen.UI.ViewGroup.md 'Tizen.UI.ViewGroup')  
&#8627; [WebView](Tizen.UI.WebView.md 'Tizen.UI.WebView')

Implements Tizen.UI.Internal.IViewSignalHandler
### Constructors

<a name='Tizen.UI.View.View()'></a>

## View() Constructor

Initializes a new instance of the View class.

```csharp
public View();
```
### Properties

<a name='Tizen.UI.View.AccessibilityDescription'></a>

## View.AccessibilityDescription Property

Gets or sets the accessibility description of the view.

```csharp
public string AccessibilityDescription { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.View.AccessibilityHidden'></a>

## View.AccessibilityHidden Property

Gets or sets whether the view is hidden for accessibility.

```csharp
public bool AccessibilityHidden { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.View.AccessibilityHighlightable'></a>

## View.AccessibilityHighlightable Property

Gets or sets whether the view can be highlighted by accessibility services.

```csharp
public bool AccessibilityHighlightable { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.View.AccessibilityName'></a>

## View.AccessibilityName Property

Gets or sets the accessibility name of the view.

```csharp
public string AccessibilityName { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.View.AccessibilityRole'></a>

## View.AccessibilityRole Property

Gets or sets the accessibility role of the view.

```csharp
public Tizen.UI.AccessibilityRole AccessibilityRole { get; set; }
```

#### Property Value
[AccessibilityRole](Tizen.UI.AccessibilityRole.md 'Tizen.UI.AccessibilityRole')

<a name='Tizen.UI.View.AccessibilityValue'></a>

## View.AccessibilityValue Property

Gets or sets the accessibility value of the view.

```csharp
public string AccessibilityValue { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.View.AutomationId'></a>

## View.AutomationId Property

Gets or sets the AutomationId property.

```csharp
public string AutomationId { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.View.BackgroundColor'></a>

## View.BackgroundColor Property

Gets or sets the background color of the view.

```csharp
public Tizen.UI.Color BackgroundColor { get; set; }
```

#### Property Value
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')

<a name='Tizen.UI.View.BorderlineColor'></a>

## View.BorderlineColor Property

Gets or sets the borderline color of the view.

```csharp
public Tizen.UI.Color BorderlineColor { get; set; }
```

#### Property Value
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')

<a name='Tizen.UI.View.BorderlineOffset'></a>

## View.BorderlineOffset Property

Gets or sets the borderline offset of the view.

```csharp
public float BorderlineOffset { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.View.BorderlineWidth'></a>

## View.BorderlineWidth Property

Gets or sets the width of the borderline.

```csharp
public float BorderlineWidth { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.View.Bounds'></a>

## View.Bounds Property

Gets the bounding rectangle of the view.

```csharp
public Tizen.UI.Rect Bounds { get; }
```

#### Property Value
[Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

<a name='Tizen.UI.View.ClippingMode'></a>

## View.ClippingMode Property

Gets or sets the clipping mode of the view.

```csharp
public Tizen.UI.ClippingMode ClippingMode { get; set; }
```

#### Property Value
[ClippingMode](Tizen.UI.ClippingMode.md 'Tizen.UI.ClippingMode')

<a name='Tizen.UI.View.CornerRadius'></a>

## View.CornerRadius Property

Gets or sets the corner radius of the view.

```csharp
public Tizen.UI.CornerRadius CornerRadius { get; set; }
```

#### Property Value
[CornerRadius](Tizen.UI.CornerRadius.md 'Tizen.UI.CornerRadius')

<a name='Tizen.UI.View.CurrentOpacity'></a>

## View.CurrentOpacity Property

Gets the opacity of view on the render thread.

```csharp
public float CurrentOpacity { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.View.CurrentPosition'></a>

## View.CurrentPosition Property

Gets the position of view on the render thread.

```csharp
public Tizen.UI.Point CurrentPosition { get; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

<a name='Tizen.UI.View.CurrentScale'></a>

## View.CurrentScale Property

Gets the scale of view on the render thread.

```csharp
public Tizen.UI.Size CurrentScale { get; }
```

#### Property Value
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')

<a name='Tizen.UI.View.CurrentScreenPosition'></a>

## View.CurrentScreenPosition Property

Gets the screen position of view on the render thread  
It is updated after the view has been rendered.

```csharp
public Tizen.UI.Point CurrentScreenPosition { get; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

<a name='Tizen.UI.View.CurrentSize'></a>

## View.CurrentSize Property

Gets the size of view on the render thread.

```csharp
public Tizen.UI.Size CurrentSize { get; }
```

#### Property Value
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')

<a name='Tizen.UI.View.DesiredHeight'></a>

## View.DesiredHeight Property

Gets or sets the desired height of the view.

```csharp
public float DesiredHeight { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.View.DesiredWidth'></a>

## View.DesiredWidth Property

Gets or sets the desired width of the view.

```csharp
public float DesiredWidth { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.View.DisallowInterceptTouchEvent'></a>

## View.DisallowInterceptTouchEvent Property

Gets or sets a value indicating whether this view should disallow intercepting touch events.  
Default value is false. The value will be reset to false when touch is completed (Up, Interrupted).

```csharp
public bool DisallowInterceptTouchEvent { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.View.DownFocusableView'></a>

## View.DownFocusableView Property

Gets or sets the view that should receive focus when the down direction key is pressed.

```csharp
public Tizen.UI.View DownFocusableView { get; set; }
```

#### Property Value
[View](Tizen.UI.View.md 'Tizen.UI.View')

<a name='Tizen.UI.View.Focusable'></a>

## View.Focusable Property

Gets or sets a value indicating whether the view can receive keyboard focus.

```csharp
public bool Focusable { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.View.FocusableChildren'></a>

## View.FocusableChildren Property

Gets or sets whether the children of the view can be focused using the keyboard.

```csharp
public bool FocusableChildren { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.View.FocusableInTouch'></a>

## View.FocusableInTouch Property

Gets or sets whether the view can receive focus through touch events.

```csharp
public bool FocusableInTouch { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.View.Height'></a>

## View.Height Property

Gets or sets the height of the view.

```csharp
public float Height { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.View.HeightResizePolicy'></a>

## View.HeightResizePolicy Property

Gets or sets the height resize policy of the view.

```csharp
public Tizen.UI.ResizePolicy HeightResizePolicy { get; set; }
```

#### Property Value
[ResizePolicy](Tizen.UI.ResizePolicy.md 'Tizen.UI.ResizePolicy')

<a name='Tizen.UI.View.ID'></a>

## View.ID Property

Gets the ID of the view.

```csharp
public uint ID { get; }
```

#### Property Value
[System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

<a name='Tizen.UI.View.InheritLayoutDirection'></a>

## View.InheritLayoutDirection Property

Gets or sets a value indicating whether the view inherits its layout direction from its parent.  
If [LayoutDirection](Tizen.UI.View.md#Tizen.UI.View.LayoutDirection 'Tizen.UI.View.LayoutDirection') is set, [InheritLayoutDirection](Tizen.UI.View.md#Tizen.UI.View.InheritLayoutDirection 'Tizen.UI.View.InheritLayoutDirection') is set to false.

```csharp
public bool InheritLayoutDirection { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.View.IsEnabled'></a>

## View.IsEnabled Property

Gets or sets a value indicating whether this view is enabled for user interaction.

```csharp
public bool IsEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.View.IsOnWindow'></a>

## View.IsOnWindow Property

Gets a value indicating whether the view is currently on the window.

```csharp
public bool IsOnWindow { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.View.IsVisible'></a>

## View.IsVisible Property

Gets or sets a value indicating whether the view is visible or not.

```csharp
public bool IsVisible { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.View.LayoutDirection'></a>

## View.LayoutDirection Property

Gets or sets the layout direction of the view.  
If [LayoutDirection](Tizen.UI.View.md#Tizen.UI.View.LayoutDirection 'Tizen.UI.View.LayoutDirection') is set, [InheritLayoutDirection](Tizen.UI.View.md#Tizen.UI.View.InheritLayoutDirection 'Tizen.UI.View.InheritLayoutDirection') is set to false.

```csharp
public Tizen.UI.LayoutDirection LayoutDirection { get; set; }
```

#### Property Value
[LayoutDirection](Tizen.UI.LayoutDirection.md 'Tizen.UI.LayoutDirection')

<a name='Tizen.UI.View.LeftFocusableView'></a>

## View.LeftFocusableView Property

Gets or sets the view that should receive focus when the left direction key is pressed while this view has focus.

```csharp
public Tizen.UI.View LeftFocusableView { get; set; }
```

#### Property Value
[View](Tizen.UI.View.md 'Tizen.UI.View')

<a name='Tizen.UI.View.MultipliedColor'></a>

## View.MultipliedColor Property

Gets or sets the color of the view, which is multiplied by the view's alpha value.

```csharp
public Tizen.UI.Color MultipliedColor { get; set; }
```

#### Property Value
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')

<a name='Tizen.UI.View.Name'></a>

## View.Name Property

Gets or sets the name of the view.

```csharp
public string Name { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.View.NaturalSize'></a>

## View.NaturalSize Property

Gets the natural size of the view.

```csharp
public Tizen.UI.Size NaturalSize { get; }
```

#### Property Value
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')

<a name='Tizen.UI.View.Opacity'></a>

## View.Opacity Property

Gets or sets the opacity of the view.

```csharp
public float Opacity { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.View.Parent'></a>

## View.Parent Property

Gets the parent of the view.

```csharp
public Tizen.UI.View Parent { get; }
```

#### Property Value
[View](Tizen.UI.View.md 'Tizen.UI.View')

<a name='Tizen.UI.View.ParentObject'></a>

## View.ParentObject Property

Gets the parent object of the view.

```csharp
public Tizen.UI.NObject ParentObject { get; }
```

#### Property Value
[NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

<a name='Tizen.UI.View.ParentOrigin'></a>

## View.ParentOrigin Property

Gets or sets the parent origin of the view.

```csharp
public Tizen.UI.Point ParentOrigin { get; set; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

<a name='Tizen.UI.View.ParentOriginX'></a>

## View.ParentOriginX Property

Gets or sets the X position of the view's parent origin.

```csharp
public float ParentOriginX { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.View.ParentOriginY'></a>

## View.ParentOriginY Property

Gets or sets the Y position of the view's parent origin.

```csharp
public float ParentOriginY { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.View.PivotPoint'></a>

## View.PivotPoint Property

Gets or sets the pivot point of the view.

```csharp
public Tizen.UI.Point PivotPoint { get; set; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

### Remarks
The pivot point is the center point around which the view rotates or scales. When a rotation or scaling operation is applied to the view,  
it is performed relative to the pivot point. By changing the pivot point, you can control the origin and behavior of the rotation or scaling.

<a name='Tizen.UI.View.PivotPointX'></a>

## View.PivotPointX Property

Gets or sets the X coordinate of the pivot point of the view.

```csharp
public float PivotPointX { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.View.PivotPointY'></a>

## View.PivotPointY Property

Gets or sets the Y coordinate of the pivot point of the view.

```csharp
public float PivotPointY { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.View.PositionUsesPivotPoint'></a>

## View.PositionUsesPivotPoint Property

Gets or sets a value indicating whether the position of the view uses the pivot point.

```csharp
public bool PositionUsesPivotPoint { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.View.RightFocusableView'></a>

## View.RightFocusableView Property

Gets or sets the view that should receive focus when the right direction key is pressed while this view has focus.

```csharp
public Tizen.UI.View RightFocusableView { get; set; }
```

#### Property Value
[View](Tizen.UI.View.md 'Tizen.UI.View')

<a name='Tizen.UI.View.Rotation'></a>

## View.Rotation Property

Gets or sets the rotation of the view.

```csharp
public float Rotation { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.View.RotationX'></a>

## View.RotationX Property

Gets or sets the rotation angle of the view around the X-axis.

```csharp
public float RotationX { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.View.RotationY'></a>

## View.RotationY Property

Gets or sets the rotation angle of the view around the Y-axis.

```csharp
public float RotationY { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.View.ScaleX'></a>

## View.ScaleX Property

Gets or sets the X-axis scale factor of the view.

```csharp
public float ScaleX { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.View.ScaleY'></a>

## View.ScaleY Property

Gets or sets the Y-axis scale factor of the view.

```csharp
public float ScaleY { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.View.ScreenPosition'></a>

## View.ScreenPosition Property

Gets the position of the view in screen coordinates.  
This position is based on the view's parent (if any) and the view's position within the parent.  
It directly calculates the value using the position of the parent view. This means that you can obtain the updated value before the view is rendered.

```csharp
public Tizen.UI.Point ScreenPosition { get; }
```

#### Property Value
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')

<a name='Tizen.UI.View.Sensitive'></a>

## View.Sensitive Property

Gets or sets the status of whether the view should emit touch or hover signals.  
If a View is made insensitive, then the View and its children are not hittable.

```csharp
public bool Sensitive { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.View.this[string]'></a>

## View.this[string] Property

Gets the descendant view with the specified name.

```csharp
public Tizen.UI.View this[string name] { get; }
```
#### Parameters

<a name='Tizen.UI.View.this[string].name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

#### Property Value
[View](Tizen.UI.View.md 'Tizen.UI.View')

<a name='Tizen.UI.View.TouchEdgeInsets'></a>

## View.TouchEdgeInsets Property

Gets or sets the inset or outset margins for the rectangle surrounding of touch area  
Use this property to extend or reduce touch area.

```csharp
public Tizen.UI.Thickness TouchEdgeInsets { get; set; }
```

#### Property Value
[Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

<a name='Tizen.UI.View.UpFocusableView'></a>

## View.UpFocusableView Property

Gets or sets the view that should receive focus when the up direction key is pressed.

```csharp
public Tizen.UI.View UpFocusableView { get; set; }
```

#### Property Value
[View](Tizen.UI.View.md 'Tizen.UI.View')

<a name='Tizen.UI.View.Width'></a>

## View.Width Property

Gets or sets the width of the view.

```csharp
public float Width { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.View.WidthResizePolicy'></a>

## View.WidthResizePolicy Property

Gets or sets the width resize policy of the view.

```csharp
public Tizen.UI.ResizePolicy WidthResizePolicy { get; set; }
```

#### Property Value
[ResizePolicy](Tizen.UI.ResizePolicy.md 'Tizen.UI.ResizePolicy')

<a name='Tizen.UI.View.WorldScale'></a>

## View.WorldScale Property

Gets the current world scale of the view.

```csharp
public Tizen.UI.Size WorldScale { get; }
```

#### Property Value
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')

<a name='Tizen.UI.View.X'></a>

## View.X Property

Gets or sets the x-coordinate of the view's position.

```csharp
public float X { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.View.Y'></a>

## View.Y Property

Gets or sets the y-coordinate of the view's position.

```csharp
public float Y { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')
### Methods

<a name='Tizen.UI.View.AddRenderNotification(Tizen.UI.RenderNotificationKey,System.Action)'></a>

## View.AddRenderNotification(RenderNotificationKey, Action) Method

Adds a render notification to the view.

```csharp
public void AddRenderNotification(Tizen.UI.RenderNotificationKey key, System.Action action);
```
#### Parameters

<a name='Tizen.UI.View.AddRenderNotification(Tizen.UI.RenderNotificationKey,System.Action).key'></a>

`key` [RenderNotificationKey](Tizen.UI.RenderNotificationKey.md 'Tizen.UI.RenderNotificationKey')

The key of the render notification.

<a name='Tizen.UI.View.AddRenderNotification(Tizen.UI.RenderNotificationKey,System.Action).action'></a>

`action` [System.Action](https://docs.microsoft.com/en-us/dotnet/api/System.Action 'System.Action')

The action to be executed when the render notification is triggered.

<a name='Tizen.UI.View.ClearAttached_T_()'></a>

## View.ClearAttached&lt;T>() Method

Clears the attached object of the specified type.

```csharp
public void ClearAttached&lt;T>();
```
#### Type parameters

<a name='Tizen.UI.View.ClearAttached_T_().T'></a>

`T`

The type of the attached object to clear.

<a name='Tizen.UI.View.ClearBackground()'></a>

## View.ClearBackground() Method

Clears the background of the view.

```csharp
public void ClearBackground();
```

<a name='Tizen.UI.View.ClearShadow()'></a>

## View.ClearShadow() Method

Clears the shadow of the view.

```csharp
public void ClearShadow();
```

<a name='Tizen.UI.View.FindViewById(uint)'></a>

## View.FindViewById(uint) Method

Finds a view with the specified ID.

```csharp
public static Tizen.UI.View FindViewById(uint id);
```
#### Parameters

<a name='Tizen.UI.View.FindViewById(uint).id'></a>

`id` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The ID of the view to find.

#### Returns
[View](Tizen.UI.View.md 'Tizen.UI.View')  
The view with the specified ID, or null if no view with the given ID is found.

<a name='Tizen.UI.View.GetAttached_T_()'></a>

## View.GetAttached&lt;T>() Method

Gets the attached object of the specified type.

```csharp
public T GetAttached&lt;T>();
```
#### Type parameters

<a name='Tizen.UI.View.GetAttached_T_().T'></a>

`T`

The type of the attached object to get.

#### Returns
[T](Tizen.UI.View.md#Tizen.UI.View.GetAttached_T_().T 'Tizen.UI.View.GetAttached&lt;T>().T')  
The attached object of the specified type, or the default value of [T](Tizen.UI.View.md#Tizen.UI.View.GetAttached_T_().T 'Tizen.UI.View.GetAttached&lt;T>().T') if it is not found.

<a name='Tizen.UI.View.GetDescendant(string)'></a>

## View.GetDescendant(string) Method

Gets the descendant view with the specified name.

```csharp
public virtual Tizen.UI.View GetDescendant(string name);
```
#### Parameters

<a name='Tizen.UI.View.GetDescendant(string).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the descendant view to find.

#### Returns
[View](Tizen.UI.View.md 'Tizen.UI.View')  
The descendant view with the specified name, or null if not found.

<a name='Tizen.UI.View.GetDescendant(uint)'></a>

## View.GetDescendant(uint) Method

Gets the descendant view with the specified ID.

```csharp
public Tizen.UI.View GetDescendant(uint id);
```
#### Parameters

<a name='Tizen.UI.View.GetDescendant(uint).id'></a>

`id` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The ID of the descendant view to find.

#### Returns
[View](Tizen.UI.View.md 'Tizen.UI.View')  
The descendant view with the specified ID, or null if no match is found.

<a name='Tizen.UI.View.GetLayer()'></a>

## View.GetLayer() Method

Gets the parent layer of this view.

```csharp
public Tizen.UI.Layer GetLayer();
```

#### Returns
[Layer](Tizen.UI.Layer.md 'Tizen.UI.Layer')  
The parent layer of view, or null if there is no parent layer.

<a name='Tizen.UI.View.HasFocus()'></a>

## View.HasFocus() Method

Checks if the view has the key input focus.

```csharp
public bool HasFocus();
```

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the view has the key input focus, false otherwise.

<a name='Tizen.UI.View.Lower()'></a>

## View.Lower() Method

Lowers the view to the view hierarchy.

```csharp
public void Lower();
```

<a name='Tizen.UI.View.LowerBelow(Tizen.UI.View)'></a>

## View.LowerBelow(View) Method

Lowers the view below the given target view.

```csharp
public void LowerBelow(Tizen.UI.View target);
```
#### Parameters

<a name='Tizen.UI.View.LowerBelow(Tizen.UI.View).target'></a>

`target` [View](Tizen.UI.View.md 'Tizen.UI.View')

<a name='Tizen.UI.View.LowerToBottom()'></a>

## View.LowerToBottom() Method

Lowers the view to the bottom of the view stack.

```csharp
public void LowerToBottom();
```

<a name='Tizen.UI.View.Measure(float,float)'></a>

## View.Measure(float, float) Method

Measures the view based on the available width and height.

```csharp
public virtual Tizen.UI.Size Measure(float availableWidth, float availableHeight);
```
#### Parameters

<a name='Tizen.UI.View.Measure(float,float).availableWidth'></a>

`availableWidth` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available width for the view.

<a name='Tizen.UI.View.Measure(float,float).availableHeight'></a>

`availableHeight` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available height for the view.

#### Returns
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')  
The measured size of the view.

<a name='Tizen.UI.View.Raise()'></a>

## View.Raise() Method

Raises the view to the view hierarchy.

```csharp
public void Raise();
```

<a name='Tizen.UI.View.RaiseAbove(Tizen.UI.View)'></a>

## View.RaiseAbove(View) Method

Raises the view above the target view.

```csharp
public void RaiseAbove(Tizen.UI.View target);
```
#### Parameters

<a name='Tizen.UI.View.RaiseAbove(Tizen.UI.View).target'></a>

`target` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to raise above.

<a name='Tizen.UI.View.RaiseToTop()'></a>

## View.RaiseToTop() Method

Raises the view to the top of the view hierarchy.

```csharp
public void RaiseToTop();
```

<a name='Tizen.UI.View.RemoveRenderNotification(Tizen.UI.RenderNotificationKey)'></a>

## View.RemoveRenderNotification(RenderNotificationKey) Method

Removes a render notification for the specified key.

```csharp
public void RemoveRenderNotification(Tizen.UI.RenderNotificationKey key);
```
#### Parameters

<a name='Tizen.UI.View.RemoveRenderNotification(Tizen.UI.RenderNotificationKey).key'></a>

`key` [RenderNotificationKey](Tizen.UI.RenderNotificationKey.md 'Tizen.UI.RenderNotificationKey')

The key associated with the render notification.

<a name='Tizen.UI.View.RemoveRenderNotification(Tizen.UI.RenderNotificationKey,System.Action)'></a>

## View.RemoveRenderNotification(RenderNotificationKey, Action) Method

Removes a render notification for the specified key and action.

```csharp
public void RemoveRenderNotification(Tizen.UI.RenderNotificationKey key, System.Action action);
```
#### Parameters

<a name='Tizen.UI.View.RemoveRenderNotification(Tizen.UI.RenderNotificationKey,System.Action).key'></a>

`key` [RenderNotificationKey](Tizen.UI.RenderNotificationKey.md 'Tizen.UI.RenderNotificationKey')

The key associated with the render notification.

<a name='Tizen.UI.View.RemoveRenderNotification(Tizen.UI.RenderNotificationKey,System.Action).action'></a>

`action` [System.Action](https://docs.microsoft.com/en-us/dotnet/api/System.Action 'System.Action')

The action to remove from the render notification.

<a name='Tizen.UI.View.SendMeasureInvalidated()'></a>

## View.SendMeasureInvalidated() Method

Sends a measure invalidated event to the view.

```csharp
public void SendMeasureInvalidated();
```

<a name='Tizen.UI.View.SetAccessibilityRelation(Tizen.UI.AccessibilityRelation,Tizen.UI.View)'></a>

## View.SetAccessibilityRelation(AccessibilityRelation, View) Method

Sets the accessibility relation between views.

```csharp
public void SetAccessibilityRelation(Tizen.UI.AccessibilityRelation relation, Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.View.SetAccessibilityRelation(Tizen.UI.AccessibilityRelation,Tizen.UI.View).relation'></a>

`relation` [AccessibilityRelation](Tizen.UI.AccessibilityRelation.md 'Tizen.UI.AccessibilityRelation')

Relation type

<a name='Tizen.UI.View.SetAccessibilityRelation(Tizen.UI.AccessibilityRelation,Tizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

View which will be in relation

<a name='Tizen.UI.View.SetAttached_T_(T)'></a>

## View.SetAttached&lt;T>(T) Method

Sets the attached object of the specified type.

```csharp
public void SetAttached&lt;T>(T value);
```
#### Type parameters

<a name='Tizen.UI.View.SetAttached_T_(T).T'></a>

`T`

The type of the attached object.
#### Parameters

<a name='Tizen.UI.View.SetAttached_T_(T).value'></a>

`value` [T](Tizen.UI.View.md#Tizen.UI.View.SetAttached_T_(T).T 'Tizen.UI.View.SetAttached&lt;T>(T).T')

The value of the attached object.

<a name='Tizen.UI.View.SetBackground(Tizen.UI.Background)'></a>

## View.SetBackground(Background) Method

Sets the background visual of the view.

```csharp
public void SetBackground(Tizen.UI.Background background);
```
#### Parameters

<a name='Tizen.UI.View.SetBackground(Tizen.UI.Background).background'></a>

`background` [Background](Tizen.UI.Background.md 'Tizen.UI.Background')

The background visual to set.

<a name='Tizen.UI.View.SetResizePolicyFactor(Tizen.UI.Size)'></a>

## View.SetResizePolicyFactor(Size) Method

Set ResizePolicy Factor  
This factor is only used when ResizePolicy is set to either: ResizePolicy.SizeRelativeToParent or ResizePolicy.SizeFixedOffsetFromParent.

```csharp
public void SetResizePolicyFactor(Tizen.UI.Size factor);
```
#### Parameters

<a name='Tizen.UI.View.SetResizePolicyFactor(Tizen.UI.Size).factor'></a>

`factor` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The factor to be set

<a name='Tizen.UI.View.SetShadow(Tizen.UI.Shadow)'></a>

## View.SetShadow(Shadow) Method

Sets the shadow of the view.

```csharp
public void SetShadow(Tizen.UI.Shadow shadow);
```
#### Parameters

<a name='Tizen.UI.View.SetShadow(Tizen.UI.Shadow).shadow'></a>

`shadow` [Shadow](Tizen.UI.Shadow.md 'Tizen.UI.Shadow')

The shadow object to set.
### Events

<a name='Tizen.UI.View.AttachedToWindow'></a>

## View.AttachedToWindow Event

Occurs when the view is attached to a window.

```csharp
public event EventHandler AttachedToWindow;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.View.DetachedFromWindow'></a>

## View.DetachedFromWindow Event

Occurs when the view is detached to a window.

```csharp
public event EventHandler DetachedFromWindow;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.View.Disposing'></a>

## View.Disposing Event

This event is emitted when the view is being disposed with disposing true.

```csharp
public event EventHandler Disposing;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.View.EnabledChanged'></a>

## View.EnabledChanged Event

Occurs when the value of [IsEnabled](Tizen.UI.View.md#Tizen.UI.View.IsEnabled 'Tizen.UI.View.IsEnabled') changes.

```csharp
public event EventHandler EnabledChanged;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.View.Focused'></a>

## View.Focused Event

Occurs when the view receives focus.

```csharp
public event EventHandler Focused;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.View.HoverEvent'></a>

## View.HoverEvent Event

Occurs when the mouse hovers over the view.

```csharp
public event EventHandler&lt;HoverEventArgs> HoverEvent;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[HoverEventArgs](Tizen.UI.HoverEventArgs.md 'Tizen.UI.HoverEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.View.InterceptTouchEvent'></a>

## View.InterceptTouchEvent Event

Event that allows the parent view to intercept touch events before passing them to child views.

```csharp
public event EventHandler&lt;TouchEventArgs> InterceptTouchEvent;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[TouchEventArgs](Tizen.UI.TouchEventArgs.md 'Tizen.UI.TouchEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.View.InterceptWheelEvent'></a>

## View.InterceptWheelEvent Event

Event that allows the parent view to intercept wheel events before passing them to child views.

```csharp
public event EventHandler&lt;WheelEventArgs> InterceptWheelEvent;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[WheelEventArgs](Tizen.UI.WheelEventArgs.md 'Tizen.UI.WheelEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.View.KeyEvent'></a>

## View.KeyEvent Event

Occurs when a key event is received by the view.

```csharp
public event EventHandler&lt;KeyEventArgs> KeyEvent;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[KeyEventArgs](Tizen.UI.KeyEventArgs.md 'Tizen.UI.KeyEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.View.LayoutDirectionChanged'></a>

## View.LayoutDirectionChanged Event

Occurs when the layout direction of the view changes.

```csharp
public event EventHandler LayoutDirectionChanged;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.View.MeasureInvalidated'></a>

## View.MeasureInvalidated Event

Occurs when the measure of the view is invalidated.

```csharp
public event EventHandler MeasureInvalidated;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.View.Relayout'></a>

## View.Relayout Event

Occurs when the view needs to be re-layouted.

```csharp
public event EventHandler Relayout;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.View.TokenPropertyChanged'></a>

## View.TokenPropertyChanged Event

Occurs when a token-related property in the View is changed.

```csharp
public static event EventHandler&lt;TokenPropertyChangedEventArgs> TokenPropertyChanged;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[TokenPropertyChangedEventArgs](Tizen.UI.TokenPropertyChangedEventArgs.md 'Tizen.UI.TokenPropertyChangedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.View.TouchEvent'></a>

## View.TouchEvent Event

Occurs when a touch event is received by the view.

```csharp
public event EventHandler&lt;TouchEventArgs> TouchEvent;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[TouchEventArgs](Tizen.UI.TouchEventArgs.md 'Tizen.UI.TouchEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.View.Unfocused'></a>

## View.Unfocused Event

Occurs when the view losts focus.

```csharp
public event EventHandler Unfocused;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.View.WheelEvent'></a>

## View.WheelEvent Event

Occurs when the wheel event is fired.

```csharp
public event EventHandler&lt;WheelEventArgs> WheelEvent;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[WheelEventArgs](Tizen.UI.WheelEventArgs.md 'Tizen.UI.WheelEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')





