# Page Indicators

Page indicators show the number of pages in a series and indicate which page is currently being displayed.

## Usage

Page indicators are dots at the top of the screen. There are 2 types of page indicator to choose from, depending on whether the pages can be navigated with a rotary action or not.

## Behavior

-   **Focus**

    Page indicators are shown as dots. Each dot represents one page in a series. When users rotate the bezel or swipe the screen, the focus shifts to the next or previous dot.

-   **Linking multiple pages to the middle dot**

    Page indicators can use up to 20 dots, representing 20 pages. If you have more than 20 pages in a series, multiple pages will be represented by the 11th dot in the middle, which will stay in focus until all linked pages are scrolled through.

## Types

-   **Circular page indicators**

    Circular page indicators curve around the top edge of the screen when the pages can be navigated by rotary action and swiping. They form an center-aligned arc of up to 120 degrees.

| **Circular page indicators** in developer's guides | |
| --- | --- |
| **Native** | Index > circle |
| **Web** |  - |

  ![](media/ui_components_10.12.3_1-850x174.png)  
    *Circular page indicators are provided when both the rotary action and swiping are available for page navigation.*


-   **Linear page indicators**

    Linear page indicators form a horizontal line at the top edge of the screen. Use them when navigation is through swiping only. Choose the linear page indicator when the rotary action controls other functions and can't be used for page navigation.

| **Linear page indicators** in developer's guides | |
| --- | --- |
| **Native** |  Index > thumbnail |
|  **Web** |  Page Indicator<br>(+Section Changer) |

  ![](media/ui_components_10.12.3_2-850x174.png)  
    *Linear page indicators are provided when swiping is the only available interaction for page navigation.*
