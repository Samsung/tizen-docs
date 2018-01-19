# Custom View Controls

NUI provides the ability to create custom views.

The following general guidelines apply to creating a custom view:

-   Derive your view from the `CustomView` class.
- Use **properties** as much as possible, as views must be data-driven.

    These views are used through JavaScript and JSON files.

- The view can be updated when the properties (such as styles) change

    Ensure the view deals with these property changes gracefully, on both first and subsequent times they are set.

- Use visuals rather than creating several child views.

    This makes the rendering pipeline more efficient.

- Accessibility actions must be considered when designing the view.
- Use events if the application needs to react to changes in the view state.
- Use of gestures is preferred over analyzing raw touch events.

<a name="existingcustomview"></a>
## CustomView Class

The NUI `CustomView` class provides common functionality required by all views. The `CustomView` class is derived from the `ViewWrapper` class:

```
public class CustomView : ViewWrapper
```

The `ViewWrapper` class in turn is derived from `View` class:

```
public class ViewWrapper : View
```

There are several controls derived from `CustomView` objects already existing in NUI, including:

-   **Spin** control, which is used for continuously changing values when the user can easily predict a set of values.
- **ContactView**, which consists of 4 visuals (`Image`, `Primitive`, `Text`, and `Color`), to display contact information.

    All of these visuals can be configured through properties: `ImageURL` (`Image`), `Shape` (`Primitive`), `Name` (`Text`), and `Color`.

    The tap gesture is enabled on the `ContactView`, changing the color visual to a random color when the `ContactView` is tapped.

    **Figure: ContactView**

    ![ContactView](media/ContactView.png)

    The contact view screenshot shows 5 contacts, each with the 4 visuals.

- **VisualView** control, which enables you to add any visual. For more information, see [Visual View Class](visuals.md#visualview).
- **StarRating** custom control, which is used for star rating of images (draggable to change the rating).

### CustomView Methods

The following table lists the `CustomView` class methods.

| Name                       | Description                              |
|--------------------------|----------------------------------------|
| `OnInitialize()`           | Called after the view has been initialized. |
| `SetBackground()`          | Sets the background with a property map. |
| `EnableGestureDetection()` | Allows deriving classes to enable any of the gesture detectors that are available. |
| `RegisterVisual()`         | Registers a visual by a property index, linking a view to a visual when required. |
| `CreateTransition()`       | Creates a transition effect on the view for animations. |
| `RelayoutRequest()`        | Requests a re-layout, which means performing a size negotiation on this view, its parent, and children (and potentially whole scene). |
| `OnStageConnection()`      | Called after the view has been connected to the stage default window. |

<a name="creation"></a>  
## Creating a Custom View
A view is created with the `new` operator:

```
contactView = new ContactView();
```

Each custom C\# View must have its static constructor called before any JSON file is loaded. Static constructors for a class are only run once (they are run per view, not per instance). The View must register its type inside the static constructor. The `CustomViewRegistry.Instance.Register()` method registers the views and any scriptable properties they have with the Type Registry:

```
static ContactView()
{
    CustomViewRegistry.Instance.Register(CreateInstance, typeof(ContactView));
}
```

In addition, the custom view must provide a `CreateInstance()` method, which gets passed to the `CustomViewRegistry.Instance.Register()` method. The `CreateInstance()` method is called if the view is in a JSON file:

```
static CustomView CreateInstance()
{
    return new ContactView();
}
```

Override the`OnInitialize()` method if necessary:

```
public override void OnInitialize()
{
    // Create a container for the star images
    _container = new FlexContainer();

    _container.FlexDirection = FlexContainer.FlexDirectionType.Row;
    _container.WidthResizePolicy = ResizePolicyType.FillToParent;
    _container.HeightResizePolicy = ResizePolicyType.FillToParent;

    this.Add(_container);
}
```

<a name="rendering"></a>
## Rendering Content

To render content, the required views can be created and added to the control itself as its children. However, this solution is not fully optimized and means extra views are added, requiring additional processing.

It is recommended to use or reuse visuals to create the required content. For more information, see [Visuals](visuals.md).

The following example shows the creation and registration of an image visual in `ContactView.cs`:

```
private VisualBase _imageVisual;

[ScriptableProperty()]
public string ImageURL
{
    get
    {
        return _imageURL;
    }
    set
    {
        _imageURL = value;

        // Create and register an image visual
        PropertyMap imageVisual = new PropertyMap();
        imageVisual.Add( Visual.Property.Type, new PropertyValue( (int)Visual.Type.Image ))
                   .Add( ImageVisualProperty.URL, new PropertyValue( _imageURL ) )
                   .Add( ImageVisualProperty.AlphaMaskURL, new PropertyValue( _maskURL ));
       _imageVisual =  VisualFactory.Get().CreateVisual( imageVisual );

        RegisterVisual( GetPropertyIndex("ImageURL"), _imageVisual );

        // Set the depth index for the image visual
       _imageVisual.DepthIndex = ImageVisualPropertyIndex;
    }
}
```

> **Note**   
> The `ImageURL` property is a [ScriptableProperty](#enableproperties), which automatically generates indices.

`RegisterVisual()` registers a visual by a property index, linking a view to a visual when required.

`GetPropertyIndex()` gets the generated index corresponding to the property name.

A range of property indices are provided for `ImageVisualPropertyIndex`, 0 by default.

For more information on the property maps that can be used for each visual type, see [Visuals](visuals.md).

<a name="stylable"></a>
## Styling Custom Views

The NUI property system allows custom views to be easily styled. The JSON syntax is used in the stylesheets:

### Current JSON Styling Format

This is an example of the current (as of July 2017) JSON stylesheet format. This example includes a visual.

```
"styles":
{
  "TextField":
  {
    "pointSize":18,
    "primaryCursorColor":[0.0,0.72,0.9,1.0],
    "secondaryCursorColor":[0.0,0.72,0.9,1.0],
    "cursorWidth":3,
    "selectionHighlightColor":[0.75,0.96,1.0,1.0],
    "grabHandleImage" : "{DALI_STYLE_IMAGE_DIR}cursor_handler_drop_center.png",
    "selectionHandleImageLeft" : {"filename":"{DALI_STYLE_IMAGE_DIR}selection_handle_drop_left.png" },
    "selectionHandleImageRight": {"filename":"{DALI_STYLE_IMAGE_DIR}selection_handle_drop_right.png" },
    "enableSelection":true
  },

  "TextFieldFontSize0":
  {
    "pointSize":10
  },

  "TextSelectionPopup":
  {
    "popupMaxSize":[656,72],
    "optionDividerSize":[2,0],
    "popupDividerColor":[0.23,0.72,0.8,0.11],
    "popupIconColor":[1.0,1.0,1.0,1.0],
    "popupPressedColor":[0.24,0.72,0.8,0.11],
    "background":
    {
      "visualType": "IMAGE",
      "url": "{DALI_IMAGE_DIR}selection-popup-background.9.png"
    },
    "backgroundBorder":
    {
      "visualType": "IMAGE",
      "url": "{DALI_IMAGE_DIR}selection-popup-border.9.png",
      "mixColor":[0.24,0.72,0.8,1.0]
    },
    "popupFadeInDuration":0.25,
    "popupFadeOutDuration":0.25
  }
}
```

### New JSON Styling Format

This is an example of the new stylesheet format, currently under development. This example also includes a visual.

```
"states":
{
  "NORMAL":
  {
    "states":
    {
      "UNSELECTED":
      {
        "visuals":
        {
          "backgroundVisual":
           {
            "visualType":"IMAGE",
            "url":"backgroundUnSelected.png"
           }
        }
      },
      "SELECTED":
      {
        "visuals":
        {
          "backgroundVisual":
           {
            "visualType":"IMAGE",
            "url":"backgroundSelected.png"
           }
        }
      }
    }
  }
}
```

Styling gives the UI designer the ability to change the look and feel of the View without any code changes.

| Normal Style                             | Customized Style                         |
|----------------------------------------|----------------------------------------|
| ![Popup window, normal style](media/popup-normal.png) | ![Popup window, custom style](media/popup-styled.png) |

For more information on building up visuals for the button states using JSON stylesheets and transitioning between the various button states, see [Styling Controls with JSON](styling-controls-with-JSON.md).

<a name="typeregistration"></a>
## Type Registration

The Type Registry is used to register your custom view. Type registration allows the creation of the view through a JSON file, as well as registering properties, signals, actions, transitions, and animation effects.

Type registration is performed by the `CustomViewRegistry.Instance.Register()` method. For more information, see [Creating a Custom View](#creation).

<a name="properties"></a>
## Properties in Custom Views

Properties can be animatable or non-animatable. Examples of animatable `View` class properties are `Position`, `Orientation`, `Scale`, and `Color`.

For more information on the NUI animation framework, see [Animation](animation.md).

Properties can be accessed through a unique index. The index can be set manually in code (hard-coded), or calculated automatically. `ContactView.cs` contains examples of both indexing methods; fixed for depth index, and automatic for registering visuals. The NUI code base is currently been modified (as of July 2017) to utilize property registration based solely on automatic generation of indices.

<a name="enableproperties"></a>
## Property Registration

The `ScriptableProperty` class enables a property to be registered with the type registry. Add `ScriptableProperty` to any view-related property that you want to script from JSON.

```
internal class ScriptableProperty : System.Attribute
```

Property indices are generated automatically in the `ScriptableProperty` class. A unique index for each property can be obtained by the `GetPropertyIndex()` method, with the name of the property as a parameter.

[Rendering](#rendering) has an example of the use of a scriptable property, with `GetPropertyIndex`.

<a name="creatingtransitions"></a>
## Creating Transitions

Controls, such as buttons, change between states from user interaction. All controls can move between the `NORMAL`, `FOCUSED`, and `DISABLED` states. Whilst in those states, a button has the `SELECTED` and `UNSELECTED` substates.

To move between states and substates, transition animations can be defined. Each state and substate can have an entry and exit transition.

To make defining common transitions easier, an effect can be used with a "from state" and a "to state". One such effect is `CROSSFADE`, which animates the opacity of visuals fading in and out to give a nice transition.

Transition effects can be read from stylesheets, or created directly with the `CreateTransition` API.

### CreateTransition API

Its possible to animate scriptable properties by using the `CreateTransition` API from `CustomView`-derived classes.

The `CreateTransition()` method creates a transition effect on the view. The `transitionData` parameter describes the effect to create, and the return value is a handle to an animation defined with the given effect, or an empty handle if no properties match.

```
protected Animation CreateTransition(TransitionData transitionData)
```

The following example code is taken from the `AnimateVisual()` method in `VisualView`, which is a `CustomView`-derived class.

```
_alphaFunction = "EASE_IN_OUT_SINE";

PropertyMap _animator = new PropertyMap();
if ( _alphaFunction != null)
{
    _animator.Add("alphaFunction", new PropertyValue(_alphaFunction));
}

PropertyMap _timePeriod = new PropertyMap();
_timePeriod.Add("duration", new PropertyValue((endTime - startTime) / 1000.0f));
_timePeriod.Add("delay", new PropertyValue(startTime / 1000.0f));
_animator.Add("timePeriod", new PropertyValue(_timePeriod));

string _str1 = property.Substring(0, 1);
string _str2 = property.Substring(1);
string _str = _str1.ToLower() + _str2;
if (_str == "position") {_str = "offset";}

PropertyValue destVal = PropertyValue.CreateFromObject(destinationValue);

PropertyMap _transition = new PropertyMap();
_transition.Add("target", new PropertyValue(target.Name));
_transition.Add("property", new PropertyValue(_str));
if (initialValue != null)
{
    PropertyValue initVal = PropertyValue.CreateFromObject(initialValue);
    _transition.Add("initialValue", new PropertyValue(initVal));
}

_transition.Add("targetValue", destVal);
_transition.Add("animator", new PropertyValue(_animator));

TransitionData _transitionData = new TransitionData(_transition);
return this.CreateTransition(_transitionData);
```

### Transition Values in a Stylesheet

The following example uses the `CROSSFADE` effect:

```
"transitions":
[
  {
    "from":"UNSELECTED",
    "to":"SELECTED",
    "visualName":"*",
    "effect":"CROSSFADE",
    "animator":
    {
      "alphaFunction":"EASE_OUT",
      "duration":0.2,
      "delay":0
    }
  }
]
```

<a name="viewbehaviour"></a>
## Setting View Behavior

The `CustomViewBehaviour` enumeration specifies the following behavior:



| Behavior                            | Description                              |
|-----------------------------------|----------------------------------------|
| `ViewBehaviourDefault`              | Default behavior (size negotiation is on, style changes are monitored, event callbacks are not called) |
| `DisableSizeNegotiation`            | View does not need size negotiation and is skipped by the size negotiation algorithm |
| `DisableStyleChangeSignals`         | View does not need to monitor style change signals, such as theme or font changes |
| `RequiresKeyboardNavigationSupport` | View needs to support keyboard navigation |
| `LastViewBehaviour`                 | -                                        |

`CustomViewBehaviour` is used during object construction. For example:

```
public VisualView() : base(typeof(VisualView).Name, CustomViewBehaviour.ViewBehaviourDefault)
{
}

public ContactView() : base(typeof(ContactView).Name, CustomViewBehaviour.RequiresKeyboardNavigationSupport)
{
}
```

<a name="events"></a>
## View Events

The `View` class contains the following events:

-   `TouchEvent` is triggered when any touch occurs within the bounds of the custom view.
-   `HoverEvent` is triggered when a pointer moves within the bounds of a custom view (for example, mouse pointer or hover pointer).
-   `WheelEvent` is triggered when the mouse wheel (or similar) is moved while hovering over a view (through a mouse pointer or hover pointer).

## Gestures

NUI has a gesture system which analyses a stream of touch events and attempts to determine the intention of the user. The following gesture detectors are provided:

-   **Pan:** When the user starts panning (or dragging) 1 or more fingers.

    The panning must start from within the bounds of the view.

- **Pinch:** Detects when 2 touch points move towards or away from each other.

    The center point of the pinch must be within the bounds of the view.

- **Tap:** When the user taps within the bounds of the view.
- **LongPress:** When the user presses and holds on a certain point within the bounds of a view.

Gesture detectors can be specified in the `OnInitialize()` method.

The following example is taken from the `ContactView` custom view:

```
public override void OnInitialize()
{
   // Enable the Tap gesture on ContactView
   EnableGestureDetection(Gesture.GestureType.Tap);
}
```

The `EnableGestureDetection()` method allows deriving classes to enable any of the gesture detectors that are available. The above code snippet only enables the default gesture detection for each type. If customization of the gesture detection is required, the gesture detector can be retrieved and set up accordingly in the same method:

```
PanGestureDetector panGestureDetector = GetPanGestureDetector();
panGestureDetector.AddDirection(PanGestureDetector.DIRECTION_VERTICAL);
```

Finally, the appropriate method must be overridden:

```
OnPan(PanGesture& pan) // Handle the pan gesture
OnPinch(PinchGesture& pinch ) // Handle the pinch gesture
OnTap(TapGesture& tap) // Handle the tap gesture
OnLongPress(LongPressGesture& longPress) // Handle the long-press gesture
```

The following example shows the `OnTap()` method from the `ContactView` class:

```
public override void OnTap(TapGesture tap)
{
    // Change the color visual of ContactView with a random color
    Random random = new Random();
    float nextRed   = (random.Next(0, 256) / 255.0f);
    float nextGreen = (random.Next(0, 256) / 255.0f);
    float nextBlue  = (random.Next(0, 256) / 255.0f);
    Animation anim = AnimateBackgroundColor( new Color( nextRed, nextGreen, nextBlue, 1.0f), 0, 2000 );
    anim.Play();
}
```


## Accessibility


Accessibility is functionality that has been designed to aid usage by the visually impaired. Accessibility behavior can be customized in the view by overriding certain virtual methods, for example, `OnAccessibilityTouch()`. Touch events are delivered differently in the accessibility mode. The `OnAccessibilityTouch()` method needs to be overridden if a special behavior is required when these touch events are received.

<a name="defaultwindowconnection"></a>
## Window Connection

If a notification is required when a custom view is connected to or disconnected from a window, override the `OnStageConnection()` and `OnStageDisconnection()` methods in the `CustomView` class.

<a name="sizenegotiation"></a>
## Size Negotiation

Size negotiation controls the view sizes in a container. It is implemented with the values of the `ResizePolicyType` enumeration.

The following table contains the values of the `ResizePolicyType` enumeration.

**Table: Resize policy types**

| Name                        | Description                              |
|---------------------------|----------------------------------------|
| `Fixed`                     | Size is fixed, set by `SetSize()` (default) |
| `UseNaturalSize`            | Use the views's natural size, meaning the dimensions of the image, or the size of the text |
| `FillToParent`              | Fill up to the bounds of the view's parent. Aspect ratio is not maintained. |
| `SizeRelativeToParent`      | Fill up to the bounds of the parent with a relative scale. Use `SetSizeModeFactor()` to specify the ratio. |
| `SizeFixedOffsetFromParent` | Fill up to the bounds of the view's parent, and add a fixed offset using `SetSizeModeFactor()`. |
| `FitToChildren`             | Size adjusts to wrap around all the children of the view. For example, a popup's height can be adjusted to fit around its contents. |
| `DimensionDependency`       | One dimension is dependent on the other  |

> **Note**   
> `UseAssignedSize`, which makes the view use a size assigned to it, is not a resize policy, but more of an implementation detail.

-   `UseNaturalSize`: Use this option for objects, such as images or text, to get their natural size, meaning the dimensions of an image or the size of the text without wrapping. Also use this on a `TableView` when the size of the table depends on its children.
-   `FillToParent`: Size fills up to the size of its parent, taking a size factor into account to allow for proportionate filling.
-   `FitToChildren`: Size scales around the size of the view's children. For example, a popup's height can be adjusted to fit around its content.
-   `DimensionDependency`: This covers rules, such as width-for-height and height-for-width. You specify that 1 dimension depends on another.

An example of setting a resize policy for a custom view:

```
contactView = new ContactView();
contactView.WidthResizePolicy  = ResizePolicyType.FillToParent;
contactView.HeightResizePolicy = ResizePolicyType.FillToParent;
```

Relayout requests are put in automatically when a property is changed on a view, or a change to the stage hierarchy is made and manual requests are usually not necessary. The `RelayoutRequest()` method is available for deriving views to call when they would like themselves to be relaid out.

The following overridable methods provide customization points for the size negotiation algorithm:

-   `GetNaturalSize()` returns the natural size of the view.
-   `GetHeightForWidth()` returns the height for a given width. Invoked by the size negotiation algorithm if using a fixed width.
-   `GetWidthForHeight()` returns the width for a given height. Invoked by the size negotiation algorithm if using a fixed height.
-   Override the `OnRelayout()` method to position and resize. The method is called during the relayout process at the end of the frame immediately after the new size has been set on the view, meaning after size negotiation is complete.
-   `OnSetResizePolicy()` is called when the resize policy is set on a view, and it allows deriving views to respond to changes in resize policy. The method can be overridden to receive notice that the resize policy has changed on the view and action can be taken.

Size negotiation is enabled on views by default. To disable size negotiation, simply pass the `DisableSizeNegotiation` behavior flag into the view constructor. For more information, see [Setting View Behavior](#viewbehaviour).

## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
