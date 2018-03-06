# Pickers

Pickers are used to set a single, specific value from a given set.

## Usage

Use pickers to set a number, a date, or time.

## Behavior

-   **Changing value**

    A number picker changes values as the bezel is rotated..

    ![](media/ui_components_10.8.2_1-850x174.png)  
    *Users set a value on a picker by rotating the bezel.*

-   **Selecting pickers**

    You can have multiple pickers on one page at the same time. Pickers on the same page should present values of the same category. A picker is highlighted when users tap it, and changes values as users rotate the bezel.

    ![](media/ui_components_10.8.2_2-850x174.png)  
    *Users can tap to switch between multiple pickers on a page.*

-   **Confirmation**

    A confirmation button at the bottom confirms a set value.

-   **Multiple pages**

    istribute pickers across multiple pages if you need to present different kinds of values together. For example, if users need to set both the time and date, have a time picker on one page, and a date picker on the next. The pages are navigated only by swiping. We recommend providing linear page indicators to show which page is currently being viewed.

## Types

-   **Number picker**

    A number picker is the most basic type of this component.

|**Number picker** in developer's guides|          |
|-----------------|------------|
|  **Native**    |   Spinner   |
|  **Web**      |    -       |

  ![](media/ui_components_10.8.3_1-850x174.png)  
    *A number picker is the most basic picker type. One or more pickers can be placed on one page.*

-   **Date picker**

    Date pickers set the day, month, and year. Spinning dials present values for each catergory: 12 months, 28/29/30/31 days, and 50 years. One full spin of the year dial is 50 years. Refer to [Date & time](../writing-style.md#date_time) for style guides on displaying the date.

|**Date picker** in developer's guides|         |
|------------|-------------|
|  **Native**|    Datetime |
|   **Web**  |   -         |

  ![](media/ui_components_10.8.3_2-850x174.png)  
    *A date picker sets the date.*

-   **Time picker**

    Time pickers can set hours and minutes, and toggle between AM/PM. The AM/PM button is displayed when the picker uses the 12-hour format, and hidden for the 24-hour format. Refer to [Date & time](../writing-style.md#date_time) for style guides on displaying time.

|**Time picker** in developer's guides|           |
|--------------|------------|
|  **Native**   |   Datetime|
|    **Web**    |   -       |

  ![](media/ui_components_10.8.3_3-850x174.png)  
    *A time picker sets the time.*


-   **Color picker**

    A color picker allows users to choose a color. This picker is displayed as a [rotary selector](rotary-selectors.md) with the focused color in the center of the screen. When users pick a color, it returns them to the previous screen. You can customize the colors on a picker.

|**Color picker** in developer's guides|             |
|----------------|--------------|
|   **Native**   |    -         |
|    **Web**     |    -         |

  ![](media/ui_components_10.8.3_4-850x174.png)  
    *A color picker is provided as a rotary selector and picks a color.*
