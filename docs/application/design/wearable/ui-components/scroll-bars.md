# Scroll Bars

A scroll bar indicates the current position on a page as users scroll through with a rotary action or a swipe.

## Usage

Use a scroll bar to handle text that doesn't fit on one screen.

## Behavior

-   **Visual interaction**

    A scroll bar appears when users first access a page and disappears shortly after. It reappears when users scroll the screen.

-   **Fast scroll**

    A screen scrolls more quickly when users flick the screen. The scrolling speed is proportional to the speed of the gesture.

## Type

-   **Vertical scroll bar**

    Use a vertical scroll bar when a page scrolls up and down. It forms an arc of 90 degrees on the right side of the screen.

    | **Vertical scroll bar** in developer's guides | |
    | -- | -- |
    | **Native** | Circle Scroller > vertical |
    | **Web** | -<br>\* Automatically applied unless otherwise defined. |

    ![](media/ui_components_10.13.3_1-850x174.png)  
    *A vertical scroll bar is provided when a page scrolls vertically.*

-   **Horizontal scroll bar**

    Use a horizontal scroll bar when a page scrolls right and left. It forms an arc of 90 degrees at the top of the screen.

    | **Horizontal scroll bar** in developer's guides | |
    | -- | -- |
    | **Native** | Circle Scroller > horizontal |
    | **Web** | -<br>\* Automatically applied unless otherwise defined. |

  ![](media/ui_components_10.13.3_2-850x174.png)  
    *A horizontal scroll bar is provided when a page scrolls horizontally.*

<a name="fast_scroll_index"></a>
    **Fast scroll index**

    A fast scroll index allows users to jump directly to the previous or next [group index](list.html#group_index) in a list.

    | **Fast scroll index**  in developer's guides | |
    | -- | -- |
    | **Native** | - |
    | **Web** |  Circular Index Scroll bar |

    -   **Fast rotary action**

        A fast scroll index allows users to move directly to the previous or next group index. Only display the first letter of the index title in the center of the screen when users move to a new group index with a rotary action.

        Fast scroll indexes only respond to a quick rotary action. When users rotate the bezel slowly or swipe the screen, the list scrolls.

    -   **Rotary action on fast scroll index**

        Once fast scroll indexes are displayed, users can jump to the previous/next group index by rotating the bezel slowly.

       ![](media/ui_components_10.13.3_3-850x174.png)  
*Fast scroll indexes appear when users rotate the bezel quickly in a list presented with indexes.*
