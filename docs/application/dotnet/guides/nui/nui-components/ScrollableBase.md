# ScrollableBase

ScrollableBase is a common component which support scrolling. Several views can be added to ScrollableBase.
User can use mouse or finger to drag it on the touch screen.

![ScrollableBase](./media/ScrollableBase.png)

## Create with property

To create a ScrollableBase using property, follow these steps:

1. Create ScrollableBase using the default constructor:

    ```cs
    ScrollableBase scrollableBase = new ScrollableBase();
    ```

2. Set the ScrollableBase property:

    ```cs
    scrollableBase.Size = new Size(400, 300);
    scrollableBase.ScrollingDirection = ScrollableBase.Direction.Vertical;
    root.Add(scrollableBase);
    ```

3. Add child views for ScrollableBase:

    ```cs
    items = new View[5];
    for (int i = 0; i < 5; i++)
    {
        items[i] = new View
        {
            Position = new Position(0, i * 100),
            Size = new Size(400, 100),
        };
        if (i % 2 == 0)
        {
            items[i].BackgroundColor = Color.Magenta;
        }
        else
        {
            items[i].BackgroundColor = Color.Cyan;
        }
        scrollableBase.Add(items[i]);
    }
    ```

Following output is generated when the ScrollableBase is created using property:

![ScrollableBaseProperty](./media/ScrollableBase.png)

## Responding to scroll drag events

When you drag a ScrollableBase, the ScrollableBase instance receives a scroll drag started event.
And after you stop dragging, the ScrollableBase instance receives a scroll drag ended event.
You can declare the events handlers as follows:

```cs
ScrollableBase scrollableBase = new ScrollableBase();
scrollableBase.ScrollDragStarted += ScrollDragStarted;
scrollableBase.ScrollDragEnded += ScrollDragEnded;
```

```cs
private void ScrollDragStarted(object sender, ScrollEventArgs e)
{
    // Do something in response to scroll drag started
}

private void ScrollDragEnded(object sender, ScrollEventArgs e)
{
    // Do something in response to scroll drag ended
}
```

Following output is generated when the ScrollableBase is being dragged:

![ScrollableBaseDrag](./media/ScrollableBase.gif)

## Related Information

- Dependencies
  -   Tizen 6.0 and Higher
