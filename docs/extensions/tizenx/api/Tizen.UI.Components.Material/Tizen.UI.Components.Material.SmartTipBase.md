### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## SmartTipBase Class

Provide base structure for SmartTips.

```csharp
public class SmartTipBase : Tizen.UI.ContentView
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ContentView &#129106; SmartTipBase

Derived  
&#8627; [SmartTip](Tizen.UI.Components.Material.SmartTip.md 'Tizen.UI.Components.Material.SmartTip')  
&#8627; [SmartTipMenu](Tizen.UI.Components.Material.SmartTipMenu.md 'Tizen.UI.Components.Material.SmartTipMenu')  
&#8627; [SmartTipView](Tizen.UI.Components.Material.SmartTipView.md 'Tizen.UI.Components.Material.SmartTipView')
### Constructors

<a name='Tizen.UI.Components.Material.SmartTipBase.SmartTipBase()'></a>

## SmartTipBase() Constructor

Constructs a smart tip.

```csharp
public SmartTipBase();
```

<a name='Tizen.UI.Components.Material.SmartTipBase.SmartTipBase(Tizen.UI.Components.Material.SmartTipViewVariables)'></a>

## SmartTipBase(SmartTipViewVariables) Constructor

Constructs a smart tip.

```csharp
public SmartTipBase(Tizen.UI.Components.Material.SmartTipViewVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.SmartTipBase.SmartTipBase(Tizen.UI.Components.Material.SmartTipViewVariables).variables'></a>

`variables` [SmartTipViewVariables](Tizen.UI.Components.Material.SmartTipViewVariables.md 'Tizen.UI.Components.Material.SmartTipViewVariables')
### Properties

<a name='Tizen.UI.Components.Material.SmartTipBase.ArrowHeight'></a>

## SmartTipBase.ArrowHeight Property

Gets or sets the arrow height.

```csharp
public float ArrowHeight { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.SmartTipBase.ArrowPosition'></a>

## SmartTipBase.ArrowPosition Property

Gets or sets the position of the arrow.

```csharp
public Tizen.UI.Components.Material.SmartTipArrowPosition ArrowPosition { get; set; }
```

#### Property Value
[SmartTipArrowPosition](Tizen.UI.Components.Material.SmartTipArrowPosition.md 'Tizen.UI.Components.Material.SmartTipArrowPosition')

<a name='Tizen.UI.Components.Material.SmartTipBase.ArrowWidth'></a>

## SmartTipBase.ArrowWidth Property

Gets or sets the arrow width.

```csharp
public float ArrowWidth { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.SmartTipBase.DismissedCommand'></a>

## SmartTipBase.DismissedCommand Property

DismissStarted event command. [Dismissed](Tizen.UI.Components.Material.SmartTipBase.md#Tizen.UI.Components.Material.SmartTipBase.Dismissed 'Tizen.UI.Components.Material.SmartTipBase.Dismissed').

```csharp
public System.Action&lt;object,System.EventArgs> DismissedCommand { get; set; }
```

#### Property Value
[System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

<a name='Tizen.UI.Components.Material.SmartTipBase.HiddenCommand'></a>

## SmartTipBase.HiddenCommand Property

Dismissed event command. [Hidden](Tizen.UI.Components.Material.SmartTipBase.md#Tizen.UI.Components.Material.SmartTipBase.Hidden 'Tizen.UI.Components.Material.SmartTipBase.Hidden').

```csharp
public System.Action&lt;object,System.EventArgs> HiddenCommand { get; set; }
```

#### Property Value
[System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

<a name='Tizen.UI.Components.Material.SmartTipBase.ShapeCornerRadius'></a>

## SmartTipBase.ShapeCornerRadius Property

Gets or sets the bubble corner radius.

```csharp
public Tizen.UI.CornerRadius ShapeCornerRadius { get; set; }
```

#### Property Value
Tizen.UI.CornerRadius

<a name='Tizen.UI.Components.Material.SmartTipBase.ShapeFillColor'></a>

## SmartTipBase.ShapeFillColor Property

Gets or sets the bubble fill color.

```csharp
public Tizen.UI.Color ShapeFillColor { get; set; }
```

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Components.Material.SmartTipBase.ShapeShadows'></a>

## SmartTipBase.ShapeShadows Property

Gets or sets the bubble shadows.

```csharp
public System.Collections.Generic.IEnumerable&lt;Tizen.UI.Shadow> ShapeShadows { get; set; }
```

#### Property Value
[System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')Tizen.UI.Shadow[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')

### Remarks
The shadows will finally sets the under shadow visuals so they can get cleared by SetUnderShadowVisuals or ClearUnderShadowVisuals.

<a name='Tizen.UI.Components.Material.SmartTipBase.ShapeStrokeColor'></a>

## SmartTipBase.ShapeStrokeColor Property

Gets or sets the bubble stroke color.

```csharp
public Tizen.UI.Color ShapeStrokeColor { get; set; }
```

#### Property Value
Tizen.UI.Color
### Methods

<a name='Tizen.UI.Components.Material.SmartTipBase.Dismiss()'></a>

## SmartTipBase.Dismiss() Method

Dismiss the modal from the window.

```csharp
public void Dismiss();
```

<a name='Tizen.UI.Components.Material.SmartTipBase.GetArrowPosition()'></a>

## SmartTipBase.GetArrowPosition() Method

Gets the arrow position.

```csharp
public Tizen.UI.Point GetArrowPosition();
```

#### Returns
Tizen.UI.Point

<a name='Tizen.UI.Components.Material.SmartTipBase.GetArrowPosition(float,float)'></a>

## SmartTipBase.GetArrowPosition(float, float) Method

Gets the arrow position with given smart tip size.

```csharp
public Tizen.UI.Point GetArrowPosition(float width, float height);
```
#### Parameters

<a name='Tizen.UI.Components.Material.SmartTipBase.GetArrowPosition(float,float).width'></a>

`width` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.SmartTipBase.GetArrowPosition(float,float).height'></a>

`height` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

#### Returns
Tizen.UI.Point

<a name='Tizen.UI.Components.Material.SmartTipBase.Post()'></a>

## SmartTipBase.Post() Method

Post as a modal content.

```csharp
public void Post();
```

<a name='Tizen.UI.Components.Material.SmartTipBase.Post(Tizen.UI.Point)'></a>

## SmartTipBase.Post(Point) Method

Post as a modal content with anchor data to the default window.

```csharp
public void Post(Tizen.UI.Point anchorPoint);
```
#### Parameters

<a name='Tizen.UI.Components.Material.SmartTipBase.Post(Tizen.UI.Point).anchorPoint'></a>

`anchorPoint` Tizen.UI.Point

The anchor point. It should be relative to the window's coordinate system.

<a name='Tizen.UI.Components.Material.SmartTipBase.Post(Tizen.UI.View)'></a>

## SmartTipBase.Post(View) Method

Post as a modal content with anchor data to the default window.

```csharp
public void Post(Tizen.UI.View anchorObject);
```
#### Parameters

<a name='Tizen.UI.Components.Material.SmartTipBase.Post(Tizen.UI.View).anchorObject'></a>

`anchorObject` Tizen.UI.View

The anchor object.

<a name='Tizen.UI.Components.Material.SmartTipBase.Post(Tizen.UI.Window)'></a>

## SmartTipBase.Post(Window) Method

Post as a modal content to the given window. If no window is specified, it uses default window.

```csharp
public void Post(Tizen.UI.Window window);
```
#### Parameters

<a name='Tizen.UI.Components.Material.SmartTipBase.Post(Tizen.UI.Window).window'></a>

`window` Tizen.UI.Window

The window to post the modal to.

<a name='Tizen.UI.Components.Material.SmartTipBase.Post(Tizen.UI.Window,Tizen.UI.Point)'></a>

## SmartTipBase.Post(Window, Point) Method

Post as a modal content to the given window. If no window is specified, it uses default window.

```csharp
public void Post(Tizen.UI.Window window, Tizen.UI.Point anchorPoint);
```
#### Parameters

<a name='Tizen.UI.Components.Material.SmartTipBase.Post(Tizen.UI.Window,Tizen.UI.Point).window'></a>

`window` Tizen.UI.Window

The window to post the modal to.

<a name='Tizen.UI.Components.Material.SmartTipBase.Post(Tizen.UI.Window,Tizen.UI.Point).anchorPoint'></a>

`anchorPoint` Tizen.UI.Point

The anchor point. It should be relative to the window's coordinate system.

<a name='Tizen.UI.Components.Material.SmartTipBase.Post(Tizen.UI.Window,Tizen.UI.View)'></a>

## SmartTipBase.Post(Window, View) Method

Post as a modal content with anchor data.

```csharp
public void Post(Tizen.UI.Window window, Tizen.UI.View anchorObject);
```
#### Parameters

<a name='Tizen.UI.Components.Material.SmartTipBase.Post(Tizen.UI.Window,Tizen.UI.View).window'></a>

`window` Tizen.UI.Window

The window to post the modal to.

<a name='Tizen.UI.Components.Material.SmartTipBase.Post(Tizen.UI.Window,Tizen.UI.View).anchorObject'></a>

`anchorObject` Tizen.UI.View

The anchor object.
### Events

<a name='Tizen.UI.Components.Material.SmartTipBase.Dismissed'></a>

## SmartTipBase.Dismissed Event

Occurred when the dismiss requested.

```csharp
public event EventHandler Dismissed;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.Material.SmartTipBase.Hidden'></a>

## SmartTipBase.Hidden Event

Occurred when the smart tip is fully dismissed (animation finished).

```csharp
public event EventHandler Hidden;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')














































