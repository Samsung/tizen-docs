# ScrollView

The `ScrollView` class provides a scrollable view, which can be scrolled manually by panning.

The following figure shows an example of layouts using the `ScrollView`.

**Figure: ScrollView**

![ScrollView](./media/scrollview.png)


In this tutorial, the following subjects are covered:

[ScrollView event](#1)<br>
[Creating a ScrollView](#2)<br>

<a name="1"></a>
## ScrollView event

The following table lists the basic signal provided by the `ScrollView` class.

**Table: ScrollView input signal**

| Input signal    | Description                                               |
| --------------- | --------------------------------------------------------- |
| `SnapStarted`   | Emitted when the ScrollView has started to snap or flick. |

A scroll view emits `SnapStarted` when it starts to snap or flick. The signal informs the target of the scroll position, scale, and rotation.

<a name="2"></a>
## Creating a ScrollView

The following example illustrates how to create a `ScrollView` object:

```
// Create a ScrollView instance
Window window = Window.Instance;
ScrollView _scrollView = new ScrollView();
Size windowSize = new Size(window.Size.Width, window.Size.Height, 0.0f);
_scrollView.Size2D = new Size2D((int)windowSize.Width, (int)windowSize.Height);
_scrollView.ParentOrigin = ParentOrigin.Center;
window.Add(_scrollView);

// Add actors to a scroll view with 3 pages
int pageRows = 1;
int pageColumns = 3;
for(int pageRow = 0; pageRow < pageRows; pageRow++)
{
  for(int pageColumn = 0; pageColumn < pageColumns; pageColumn++)
  {
    View pageActor = new View();
    pageActor.WidthResizePolicy = ResizePolicyType.FillToParent;
    pageActor.HeightResizePolicy = ResizePolicyType.FillToParent;
    pageActor.ParentOrigin = ParentOrigin.Center;
    pageActor.PivotPoint = PivotPoint.Center;
    pageActor.Position = new Position(pageColumn * windowSize.Width, pageRow * windowSize.Height, 0.0f);
    _scrollView.Add(pageActor);
  }
}

_scrollView.SetAxisAutoLock(true);

// ScrollView contents are now draggable
// Set scroll view to have 3 pages in X axis and allow page snapping,
// and also disable scrolling in Y axis.
PropertyMap rulerMap = new PropertyMap();
rulerMap.Add((int)ScrollModeType.XAxisScrollEnabled, new PropertyValue(true));
rulerMap.Add((int)ScrollModeType.XAxisSnapToInterval, new PropertyValue(windowSize.Width));
rulerMap.Add((int)ScrollModeType.XAxisScrollBoundary, new PropertyValue(windowSize.Width * pageColumns ) );
rulerMap.Add((int)ScrollModeType.YAxisScrollEnabled, new PropertyValue( false ) );
_scrollView.ScrollMode = rulerMap;
```

## Related Information
- Dependencies
  -   Tizen 4.0 and Higher
