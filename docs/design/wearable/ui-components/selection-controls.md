# Selection Controls



Selection controls help users select an item. The appropriate type will depend on how you want to present items for the user’s selection.

## Usage

Selection controls are used with list items or text content when users need to make selections or toggle between on/off.

## Behavior

-   **Touch area**

    A whole list item area should be tappable when the item is presented with a selection control. This helps users select an item easily.

    ![](media/ui_components_10.10.2_1-850x174.png)  
    *A whole area should be tappable when a list item is presented with a selection control.*

-   **Applying the value**

    It’s recommended that the value is immediately applied when users make a selection.

-   **Single control**

    A list item can only have one type of selection control. List items with a selection control cannot also have an icon.

    ![](media/ui_components_10.10.3_1-850x257.png)  
    *Selection controls components cannot be provided along with an icon.*

-   **Use in text content**

    Selection controls only appear on list items, except for checkboxes that are used on the body of text content.

## Types

  **Switches**

  Switches toggle a feature on and off and are found next to the main text of a list item. You can design a switch to turn off all sub-items related to one main parent item. Subtext is not recommended, but if necessary, use it to describe the function.

|**Switch**|          |
|----------|----------|
|**Native**|Check > on and off|
|  **Web** |   -      |

  ![](media/ui_components_10.10.2_2-850x257.png)  
    *Subtext for a switch should provide a description, not the on/off status.*

  **Checkboxes**

  Checkboxes are used to select multiple items from a list, or on pop-ups that ask users to confirm their decision or agreement.

|**Checkbox**|           |
|------------|-----------|
| **Native** |    Check  |
|   **Web**  |  Checkbox |

  ![](media/ui_components_10.10.3_2-850x174.png)  
  *Checkboxes allow for multiple selections in a list.*

  **Radio buttons**

  Radio buttons are used instead of checkboxes when users can only select a single item from a list. When users tap a list item with a radio button, that item is brought into focus in the center of the screen.

|**Radio button**|                 |
|----------------|-----------------|
|  **Native**    |     Radio       |
|    **Web**     |   Radio button  |

  ![](media/ui_components_10.10.3_3-850x174.png)  
    *Radio buttons are usedwhen users can select only a single item from a list.*

> **Tip**  
> Lists that ask users to choose a ringtone or vibration can be set to play a preview when an item is selected.
