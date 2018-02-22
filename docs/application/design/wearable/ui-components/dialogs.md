# Dialogs

A dialog pop-up provides critical and timely information, and asks for the user's decision on a task. It should deliver information relevant to the user's current situation. The title and the first line of the body text should be simple and clear so users can understand the message immediately.

## Usage

-   **Don't overuse**

    Only use dialog pop-ups when you need a user to confirm something. If an action isn't critical or can be reversed, provide a [toast](toasts.md) to inform the user that the task completed.

-   **Don't repeat the same pop-up**

    Only show pop-ups once unless they need to be repeated. Avoid asking users whether to show the same pop-up again.

## Elements

-   **Title**

    The title is optional and summarizes the body text. Don't simply repeat the title of the menu that the user has selected.

-   **Body content**

    Body content explains an action that will follow the user's confirmation. The first line should convey the most important information so users can understand what the pop-up is about by just scanning the text. An image or bullet points can make long passages of text easier to read.

## Behavior

The title, body content, and image of a dialog pop-up all move together when users scroll the screen. In contrast, buttons remain in a fixed position so users can select them from anywhere in the pop-up. A dialog pop-up will only close when the user selects an option like Confirm or Cancel. The pop-up appears as a [temporary view](../navigation/screen-views.md#temp_view) that interrupts the user's current workflow.

## Types

-   **Confirmation pop-up**

    A confirmation pop-up asks the user's intent before performing an irreversible action. It consists of the title and body content in the center, an OK button on the right, and a Cancel button on the left.

|**Confirmation pop-up** in developer's guides| |  
|--------------|-----------|  
|**Native**|  Pop-up > Buttons2|
|    **Web**|   Pop-up > side button|

![](media/ui_components_10.3.4_1-850x174.png)  
    *A confirmation pop-up asks for the user's agreement or decision.*


-   **Information pop-up**

    An information pop-up displays important or critical information that needs to be confirmed by the user. It consists of the title, body content, and a bottom button.

|**Information pop-up** in developer's guides| |
|---------|----------|
|  **Native**|    Pop-up > Buttons1|
|    **Web**|    Pop-up > Bottom button|

  ![](media/ui_components_10.3.4_2-850x174.png)  
    *An information pop-up provides information that needs to be confirmed by the user.*

## Design specs

-   **Confirmation pop-up**  
  ![](media/ui_components_10.3.5_1-850x258.png)

-   **Information pop-up**  

    ![](media/ui_components_10.3.5_2-850x272.png)
