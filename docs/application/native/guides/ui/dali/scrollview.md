# ScrollView


The `Dali::Toolkit::ScrollView` class provides a scrollable view, which contains actors and can be scrolled automatically or manually by panning.

The following figure shows example layouts using the `ScrollView`.

**Figure: ScrollView**

![ScrollView](./media/scrollview.png)

A scroll view emits a `ScrollView::SnapStartedSignal()` signal when the scroll view has started to snap or flick. The signal informs the target of the scroll position, scale, and rotation.

## Creating a ScrollView

The following example shows how to create a `Dali::Toolkit::ScrollView` object:

```
// This sample code is for the HelloWorldExample
// class in Creating a DALi Application
void HelloWorldExample::Create( Application& application )
{
  // Create a ScrollView instance
  ScrollView scrollView = ScrollView::New();
  scrollView.SetParentOrigin( ParentOrigin::CENTER );
  Stage::GetCurrent().Add( scrollView );

  // Set the size of scrollView;
  // it covers the entire stage
  Size size = Stage::GetCurrent().GetSize();
  scrollView.SetSize( size );

  // Add actors to the ScrollView
  for( int i; i < MY_ITEM_COUNT; ++i )
  {
    ImageView imageView = ImageView::New( MY_IMAGE_PATHS[i] );
    imageView.SetAnchorPoint( AnchorPoint::TOP_LEFT );
    imageView.SetPosition( i * size.x, 0.0f );
    scrollView.Add( imageView );
  }

  // ScrollView contents are now draggable

  // To enforce horizontal-only scrolling,
  // the Y axis ruler can be disabled
  RulerPtr rulerY = new DefaultRuler();
  rulerY->Disable();
  scrollView.SetRulerY( rulerY );

  // To enable snapping, a FixedRuler can be
  // applied to the X axis, with snap
  // points spaced to the width of the stage
  RulerPtr rulerX1 = new FixedRuler( size.width );
  scrollView.SetRulerX( rulerX1 );

  // Domain can be applied to rulers to prevent
  // scrolling beyond this boundary
  // In this case, to 4 times the width of the
  // stage, allowing for 4 pages to be scrolled
  RulerPtr rulerX2 = new FixedRuler( size.width );
  rulerX2->SetDomain( RulerDomain( 0.0f, size.width*4.0f ) );
  scrollView.SetRulerX( rulerX2 );
}
```

## Using Ruler, RulerDomain, and Wrap

The `Dali::Toolkit::Ruler` abstract class defines the scroll axes. The `Dali::Toolkit::RulerDomain` class specifies the minimum and maximum values of a ruler.

The `Dali::Toolkit::ScrollView` class provides a wrap mode for `ScrollView` contents. When enabled, the `ScrollView` contents are wrapped over the x/y domain.

The `ScrollView` behavior depends on a combination of the ruler, ruler domain, and wrap modes. The following table shows `ScrollView` behavior according to the combination.

**Figure: Ruler, ruler domain, and wrap modes**

![Ruler, ruler domain, and wrap modes](./media/scrollview_ruler.png)

**Table: Scrollview behavior in the ruler, ruler domain, and wrap mode**

| Ruler    | Domain   | Wrap    | Behavior                                 |
|----------|----------|---------|------------------------------------------|
| Disabled | Disabled | Wrap    | No movement in axis                      |
| Disabled | Enabled  | No wrap | No movement in axis                      |
| Disabled | Enabled  | Wrap    | No movement in axis                      |
| Enabled  | Disabled | No wrap | Free movement in axis                    |
| Enabled  | Disabled | Wrap    | Free movement in axis, wrapped according to domain minimum and maximum |
| Enabled  | Enabled  | No wrap | Movement limited to domain minimum and maximum |
| Enabled  | Enabled  | Wrap    | Movement limited to domain minimum and maximum |

> **Note**  
> Actors within a `ScrollView` are controlled by constraints. If you apply constraints to these actors externally, undefined behavior can occur. Since applying additional constraints can conflict with the `ScrollView` constraints, place the actors within container actors. The container actors are affected by the constraints.

## Related Information
* Dependencies
 - Tizen 2.4 and Higher for Mobile
 - Tizen 3.0 and Higher for Wearable
