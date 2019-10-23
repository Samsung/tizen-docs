# ScrollBar
A scroll bar allows you to recognize the direction of the display, the range of lists, and the range of content.  
A scroll bar is shown on the screen only when the entire content cannot be displayed on the same page.  
The method of displaying a scroll bar can vary depending on the display area such as a list or a text area.

A scroll bar is displayed on the right or at the bottom of the scrolling area.  
On the lists or the contents, the scroll bar is shown when the focus moves to the same direction of contents extension.  
When entering the screen consists of list, the vertical or horizontal scroll bar is displayed that has same direction with mainstream of the screen.

![CreateWithProperties](./media/scrollbar_properties.PNG)

## Create with Property

To create a scrollbar using property, follow these steps:

1. Create scrollbar using the default constructor:

    ```cs
    scrollBar = new ScrollBar();
    ```

2. Set the scrollbar property:

    ```cs
    scrollBar.Position = new Position(50, 300);
    scrollBar.Size = new Size(300, 4);
    scrollBar.TrackColor = Color.Green;
    scrollBar.MaxValue = (int)scrollBar.SizeWidth / 10;
    scrollBar.MinValue = 0;
    scrollBar.ThumbSize = new Size(30, 4);
    scrollBar.CurrentValue = 0;
    scrollBar.ThumbColor = Color.Black;
    root.Add(scrollBar);
    ```

Following output is generated when the progress is created using property:

![CreateWithProperties](./media/scrollbar_properties.PNG)

## ScrollBar Properties

The properties available in the ScrollBar class are:

| Property  | Type | Description
| ------------ | ------------ | ------------ |
| CurrentValue | int | Get or set the current value of the ScrollBar |
| MinValue | int | Get or set the minimum value of the ScrollBar |
| MaxValue | int | Ge or set the maximum value of the ScrollBar |
| ThumbColor | Color | Get or set the color of the thumb image object |
| TrackColor | Color | Get or set the color of the track object |
| TrackImageURL | string | Get or set the image URL of the track image object |
| Direction | DirectionType | Get or set the direction of the ScrollBar |
| Duration | uint | Get or set the animation duration for thumbImage animate to CurrentValue|
| ThumbSize | Size | Get or set the size of the thumb object |

## Related Information
- Dependencies
  -   Tizen 5.5 and Higher