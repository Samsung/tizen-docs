# Pages

Pages are where content is presented. A page consists of a header and body. The header consists of the title, and the body contains other elements of a page. At any given time, an app shows either a whole or part of a page.

![](media/ui_components_10.1.0-850x174.png)  
*A page consists of a header and a body.*

## Elements

-   **Header**

    The header includes the page title, which should be text-only without icons. Titles that are longer than the space provided slide in and fade out at the right edge of the screen. For a list page, you can also include action buttons in the header.

-   **Body**

    The body of a page contains content including the main content, images, buttons, or text.

    -   **Text content**

        Text content should have margins on either side. Without these, it's hard to read the text on a round display. When the text doesn't fit on one screen, the page scrolls vertically so users can see the full text. Refer to [Scroll bar](scroll-bars.md) for more details.

        ![](media/ui_components_10.1.1_1-664x200.png)  
        *Text content should have margins on either side.*

    -   **Image content**

        Display one thumbnail image at a time on a single page. Images on each page should be identical in size. Users rotate the bezel or swipe the screen to move between pages.

        ![](media/ui_components_10.1.1_2-850x174.png)  
        *Thumbnails are used to provide a series of images successively*

    -   **Thumbnail**

        Thumbnails can be presented with a title or subtext. Usually you should place the title below each image, but place the title above the image if the page has a [bottom button](buttons.md#bottom_button). Titles that don't fit slide in and fade out at the right-hand edge of the screen. Access to More options is not available.

## Behavior

-   **Scroll**

    Pages scroll when the text doeesn't fit on one screen. Generally, pages scroll vertically to display long text content, and scroll horizontally to present a set of images one-by-one.

-   **Multiple pages**

    Multiple pages at the same navigational level can be shown in a series. In this case, provide [page indicators](page-indicators.md) so users know where they are in the series.

-   **Select mode**

    Users can touch and hold an image to begin selecting multiple images for a particular action.
