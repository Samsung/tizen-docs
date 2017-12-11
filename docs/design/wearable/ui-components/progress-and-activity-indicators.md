# Progress and Activity Indicators



Indicators visually show that a task is ongoing. Using a progress or activity indicator will depend on if you can determine the amount of time a user will be waiting.

## Usage

Use indicators to show the progress of data loading or other similar tasks.

## Behavior

-   **Filling**

    A progress indicator will gradually fill up according to the level of progress made.

-   **Spinning**

    An activity indicator will spin until an activity is completed.

## Types

-   **Progress indicators**

    A progress indicator helps users determine how long they’ll be waiting by displaying how far a task has progressed. You can show progress with a percentage scale or a fraction indicator. The indicator will disappear when the task is completed.  
    <table>
     <tr>
       <th> **Progress Indicator** </th>    
       <th>  </th>
     </tr>
     <tr>
       <td> **Native** </td>
       <td> Progress Bar </td>
     </tr>
     <tr>
       <td> **Web** </td>
       <td> Progress Bar </td>
     </tr>
    </table>

    -   **Full progress indicator**  
      You can display a full progress indicator around the edge of the screen.

      ![](media/ui_components_10.11.3_1-850x174.png)  
      *A full progress indicator shows progress around the edge of the screen.*

    -   **Small progress indicator**

        You can display a small progress indicator in the middle of the screen. A description of the progress status can be provided below the indicator.

        ![](media/ui_components_10.11.3_2-850x174.png)  
        *A small progress indicator shows progress in the middle of the screen.*

    -   **In list progress indicator**

        The progress of an action on a list item can be displayed with an in list indicator.

       ![](media/ui_components_10.11.3_3-850x174.png)  
        *The progress of a list item action is displayed with an in list progress indicator.*

-   **Activity indicators**

    Activity indicators inform users that a task is ongoing without specifying the progress rate. The indicator disappears when the task is completed.

    <table>
     <tr>
       <th> **Activity Indicator (Full)** </th>    
       <th>  </th>
     </tr>
     <tr>
       <td> **Native** </td>
       <td> Progress Bar > process </td>
     </tr>
     <tr>
       <td> **Web** </td>
       <td> Progressing </td>
     </tr>
    </table>

    -   **Full activity indicator**

        You can display a full activity indicator around the edge of the screen to indicate that an action is ongoing. The indicator keeps spinning around the edge until the action is completed.

        ![](media/ui_components_10.11.3_4-850x174.png)  
        *A full activity indicator spins around the edge of the screen to indicate that an action is ongoing.*

    -   **Small activity indicator**

        You can display a small activity inidcator in the center of the screen to indicate that an action is ongoing. A small circle keeps spinning until the action is completed. A description of the action can be shown below the indicator.

        ![](media/ui_components_10.11.3_5-850x174.png)  
        *A small activity indicator spins in the middle of the screen to show that an action is ongoing.*

    -   **In list activity indicator**

        Ongoing actions on a list item can be higlighted with an in list indicator.

        ![](media/ui_components_10.11.3_6-850x174.png)  
        *An ongoing list item action is indicated with an activity indicator to the right of the item.*
