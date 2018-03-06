# Text Fields

Text fields are used to input text.

 

|**Text field** in developer's guides|          |
|----------|----------|
|**Native**|Entry     |
|**Web**   |-         |

## Usage

-   **Limit text input to one line**

    Direct users to their phone when they need to enter more than one line of text.

-   **Only use text fields when other options are not available**

    We recommend using voice input or displaying a list of pre-defined options for users to choose from.

## Behavior

-   **Input**

    Tapping on a text field pulls up the keyboard from the bottom of the screen. Users finish text input by tapping the Done button or by pressing the Back key.

-   **Keyboard**

    You can define the input type of a text field to ensure the appropriate keyboard is launched. Keyboards have default, numeric, e-mail, or URL formats. You can also assign different functions to the Return key such as Done, Search, and Send.

## Elements

-   **Field**

    The field receives the user's text input. When tapped, it displays a cursor and pulls up the keyboard.

-   **Hint text (optional)**

    Hint text explains or shows an example of what users should type in the text input field. You can provide hint text about an empty field before users start typing or after they've cleared all text. The hint text automatically disappears when users begin typing.


-   **Clear text button (optional)**

    A clear text button erases all the text in the field. It should be placed at the right of the input field.

     ![](media/ui_components_10.7.3_1-850x174.png)  
    *A clear text button deletes all the text in the field.*

-   **Remove field button (optional)**

    A remove field button deletes an entire input field. It should be placed at the right of the input field. When you provide a remove field button, give users a way to add it back.

    ![](media/ui_components_10.7.3_2-850x174.png)  
    *A remove field button is placed at the right end of the input field.*
