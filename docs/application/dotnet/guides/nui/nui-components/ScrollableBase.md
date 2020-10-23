# ScrollableBase

ScrollableBase is a common component that supports scrolling. You can add several views to the ScrollableBase component.
You can use a mouse or finger on the touch screen to drag a ScrollableBase component.

![ScrollableBase](./media/ScrollableBase.png)

## Create with property

To create a ScrollableBase using various properties, follow these steps:

1. Create ScrollableBase using the default constructor:

    ```csharp
    ScrollableBase scrollableBase = new ScrollableBase();
    ```

2. Set the ScrollableBase property:

    ```csharp
    scrollableBase.Size = new Size(400, 300);
    scrollableBase.ScrollingDirection = ScrollableBase.Direction.Vertical;
    root.Add(scrollableBase);
    ```

3. Add child views for ScrollableBase:

    ```csharp
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

## Scroll drag events responses

When a ScrollableBase is dragged, the ScrollableBase instance receives a scroll drag start event.
When the ScrollBase dragging is stopped, the ScrollableBase instance receives a scroll drag ended event.
You can declare the events handlers as follows:

```csharp
ScrollableBase scrollableBase = new ScrollableBase();
scrollableBase.ScrollDragStarted += ScrollDragStarted;
scrollableBase.ScrollDragEnded += ScrollDragEnded;
```

```csharp
private void ScrollDragStarted(object sender, ScrollEventArgs e)
{
    // Do something in response to scroll drag started
}

private void ScrollDragEnded(object sender, ScrollEventArgs e)
{
    // Do something in response to scroll drag ended
}
```

The following output is generated when the ScrollableBase is dragged:

![ScrollableBaseDrag](./media/ScrollableBase.gif)

## Related information

- Dependencies
  -   Tizen 6.0 and Higher
