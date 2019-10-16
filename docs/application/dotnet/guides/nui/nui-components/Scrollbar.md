# ScrollBar
This tutorial describes how to create and use the scroll bar.

## Overview
A scroll bar allows users to recognize the direction and the range of lists/content.

- A scroll bar is shown on the screen only when all the content cannot be displayed on the same page.
- It is displayed on the right or at the bottom of the scrolling area.
- The method of displaying a scroll bar can vary depending on the display area (a list or a text area).
- When entering the screen consists of list, the vertical or horizontal scroll bar is displayed that has same direction with main stream of the screen.
- On the lists/contents, the scroll bar is shown when the focus moves to the same direction of contents extension.

## Create with properties

~~~{.cs}
scrollBar = new ScrollBar();
scrollBar.Position = new Position(50, 300);
scrollBar.Size = new Size(300, 4);
scrollBar.TrackColor = Color.Green;           
scrollBar.MaxValue = (int)scrollBar.SizeWidth / 10;
scrollBar.MinValue = 0;
scrollBar.ThumbSize = new Size(30, 4);
scrollBar.CurrentValue = 0;
scrollBar.ThumbColor = Color.Black;
root.Add(scrollBar);
~~~
![CreateWithProperties](./media/scrollbar_properties.PNG)


## ScrollBar Properties

The properties available in the *ScrollBar* class are:

| Property  | Type | Description
| ------------ | ------------ | ------------ |
| CurrentValue | int | Get/set the current value of the ScrollBar |
| MinValue | int | Get/set the min value of the ScrollBar |
| MaxValue | int | Get/set the max value of the ScrollBar |
| ThumbColor | Color | Get/set the color of the thumb image object |
| TrackColor | Color | Get/set the color of the track object |
| TrackImageURL | string | Get/set the image URL of the track image object |
| Direction | DirectionType | Get/set the direction of the ScrollBar |
| Duration | uint | Get/set the animation duration for thumbImage animate to CurrentValue|
| ThumbSize | Size | Get/set the size of the thumb object |

## Related Information
- Dependencies
  -   Tizen 5.5 and Higher