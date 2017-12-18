# Page Indicators

Page indicators show the number of pages in a series and indicate which page is currently being displayed.

## Usage

Page indicators are presented at the top of the screen as dots that represent each page. There are 2 types of page indicator available, depending on whether the pages can be navigated with a rotary action or not.

## Behavior

-   **Focus**

    Page indicators are presented as dots. Each dot represents one page in a series. When users rotate the bezel or swipe the screen, the focus shifts to the next or previous dot.

-   **Linking multiple pages to the middle dot**

    Page indicators can use up to 20 dots. If you have more than 20 pages in a series, multiple pages will be represented by the 11th dot in the middle, which will stay in focus until all linked pages are scrolled through.

## Types

-   **Circular page indicators**

    These indicators curve around the top edge of the screen when the pages are navigated by a rotary action and a swipe. They can form an arc of up to 120 degrees and are center-aligned.

| Circular page indicators | |
| --- | --- |
| **Native** | Index > circle |
| **Web** |  - |

  ![](media/ui_components_10.12.3_1-850x174.png)  
    *Circular page indicators are provided when both the rotary action and swiping are available for page navigation.*


-   **Linear page indicators**

    These indicators form a horizontal line at the top edge of the screen when navigation is through swiping only. This type of indicator is recommended when the rotary action controls other functions and can’t be used for page navigation.

| Linear page indicators | |
| --- | --- |
| **Native** |  Index > thumbnail |
|  **Web** |  Page Indicator<br>(+Section Changer) |

  ![](media/ui_components_10.12.3_2-850x174.png)  
    *Linear page indicators are provided when swiping is the only available interaction for page navigation.*
