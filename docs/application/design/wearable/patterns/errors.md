# Errors

Errors occur when the Gear fails to complete an intended action. For instance, when data loading fails or user inputs can't be processed.

## Error pages

When errors occur, your app should explain the cause of the error and a solution to the user.

-   **Use visual elements**

    Visual elements help users quickly understand the cause of an error and the appropriate response. Images or icons are more effective than text descriptions when explaining the cause and solution.

    ![](media/pattern_9.5.1_1-850x174.png)  
    *Visual elements help users understand error messages.*

-   **Provide an error message and buttons.**

    An error message with buttons directs users to the appropriate follow-up action. For example, if the Gear loses the Bluetooth connection with the user's mobile phone, use a Retry pop-up. Allow users to exit the page when a task, such as data loading, fails before completion.

    ![](media/pattern_9.5.1_2-850x174.png)  
    *Buttons on error messages direct users to take follow-up actions.*

## User input errors

User input errors occur when the user enters incorrect data. For this type of error, help users quickly correct the data by providing appropriate text.

-   **Hint text**

    Hint text provides instructions on what to enter into an input field.

-   **Error text**

    Error text informs users when data is incorrect. It appears below an input field in a color that stands out.

## App errors

App errors occur within the app regardless of any user input.

-   **General error**

    When a general error occurs, use a loading indicator until the error message appears. You can also indicate the features that are unavailable by disabling them in the UI.

-   **Connectivity error**

    When there are problems with mobile or data connectivity, users should still be able to interact with other features that don't need a connection. You can also provide a Retry button so users can try to connect again.
