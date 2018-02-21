# Feedback

The Gear offers visual, auditory, and haptic feedback. Whichever the type of feedback being used, it should clearly communicate the result of a user's input. You can combine more than one type of feedback when you need to emphasize user input.

<table>
     <tr>
       <th> Interaction </th>
       <th>   </th>
       <th> Example </th>
     </tr>
     <tr>
       <td> Haptic response </td>
       <td> <img src="media/interaction_7.5.0_1-100x91.png"> </td>
       <td rowspan="3"> Respond to user input </td>
     </tr>
     <tr>
       <td> Visual response </td>
       <td> <img src="media/interaction_7.5.0_2-100x127.png"> </td>
     </tr>
     <tr>
       <td> Sound response </td>
       <td> <img src="media/interaction_7.5.0_3-100x90.png"> </td>
     </tr>
    </table>





## Haptic responses

Haptic responses deliver feedback to users using vibration so that they don't have to look at the screen. You can vary the duration and number of vibrations to communicate different meanings.

-   **Designing vibration**

    You can design haptic patterns by using a mix of silence and vibrations of varying durations. Because users might have difficulty differentiating between complicated patterns, try to keep them as simple as possible.

-   **Sample vibration Patterns**

| Examples | | Meaning |
|---|---|---|
| Single short<br>*(e.g. 100 ms)* | ![](media/interaction_7.5.1_1_1-77x45.png) | Provides simple information |
| Single long<br>*(e.g. 500 ms)* | ![](media/interaction_7.5.1_1_2-126x45.png) | Signals a clear status<br>*(e.g. completion of a task)* |
|  2-3 times fast | ![](media/interaction_7.5.1_1_3-211x45.png) | Provides a warning or an alert |
| 2-3 times middle speed | ![](media/interaction_7.5.1_1_4-263x45.png) | Provides a general notification |
| 2-3 times slow<br>*(e.g. 60 times / min=60 BPM)* |  ![](media/interaction_7.5.1_1_5-407x45.png) | Provides an alert about an incoming/ongoing event |


-   **Duration of vibrations**

    Users often find extended vibrations annoying. In addition, long vibrations drain battery power.

-   **Appropriate feedback**

    Haptic vibration can be created with different intensities. Since the Gear is worn on the wrist, several factors can affect range of vibration that's detectable, including whether users are moving, whether they are wearing the Gear, or how much they are focusing on the device. Haptic feedback should only be provided selectively to avoid tiring out users with unnecessarily frequent feedback.

-   **Feedback on text input**

    Since users generally type to perform a task, they need quick feedback on whether they are typing correctly. Consider ways to minimize latency to ensure instantaneous feedback on typing. Haptic feedback should be as brief as possible, within the range that users can notice the vibration. (e.g. below 30 ms)

## Visual responses

Visual responses inform users of a current state. Provide visual feedback to inform users that they have reached the end of a scrollable page or that a button or icon has been pressed. Refer to [Visual design](../visual-design/animation.md#clear_feedback) for more details.

-   **Overscroll**

    [Overscrolling](../patterns/overscroll.md) effects indicate that the user has reached the end of a scrollable list or page. It appears as a straight line, at the edge of both a linear and circular page.

-   **Button press**

    Button press effects indicate that a button or icon has been pressed by adjusting the color opacity or size of the button.

-   **Adjusting the color opacity**

    You can adjust the color opacity of a button by 40% to indicate that the button has been pressed.

| Normal | Pressed |
|:---:|:---:|
|![](media/interaction_7.5.1_2-850x174_1.png)| ![](media/interaction_7.5.1_2-850x174_2.png)  |
| Opacity 100% | Opacity 40% |  

  *The opacity of the entire container is adjusted to 40% when users press a colored icon.*  

| Normal | Pressed |
|:---:|:---:|
|   ![](media/interaction_7.5.1_3-850x174_1.png)  |   ![](media/interaction_7.5.1_3-850x174_2.png)  |
| Opacity 100% | Opacity 40% |  

  *The color opacity of the whole container drops to 40% when users press a text button.*

-   **Adjusting the size**

    You can adjust the size of a button to indicate that the button has been pressed.

| Normal | Pressed |
|:---:|:---:|
|     ![](media/2-800x166_1.png)  |     ![](media/2-800x166_2.png)  |
|  Scale 100% |  Scale 110%  |  

  *When users press a 2D icon without a container, a circle appears around the button and is scaled up to 110% of its original size*

  | Normal | Pressed |
  |:---:|:---:|
  |     ![](media/interaction_7.5.1_5-850x174_1.png)    |         ![](media/interaction_7.5.1_5-850x174_2.png)    |
  |  Scale 100% |  Scale 110%  |  

       
  *When users touch the screen itself, the screen is scaled down to 90% and then returns to 100%.*


## Auditory responses

Auditory responses deliver feedback for the user's touches or gestures. Using different stream types, durations, and melodies creates sounds that help users perform the correct next steps.

 

-   **Stream type**

    Consider which stream type is suitable for each auditory response. It could be a ringtone, a notification (message), or a snippet of media.

-   **Properties: notes, tones, melodies**

    Consider the meaning of each property when you're designing your auditory feedback. For instance, touch interaction performs many different actions, so the related sounds typically have a neutral and simple tone. You can use a higher note when values go up, and a lower note one values go down. Likewise, you can use an ascending melody when turning on a function and a descending one when turning it off. Create standards that remain consistent throughout your app.

 

The table below shows some examples of the Gear's auditory responses for each type of interaction.

| | | |
|--------------------------|--------------------------|--------------------------|
|Touch/mode change        |<img src="media/interaction_7.5.3_icon_play1.png" width="70" height="70" /> |<img src="media/interaction_7.5.3_icon_01.png" width="220" height="40" /> |
| Nokey (reach limit)      |<img src="media/interaction_7.5.3_icon_play1.png" width="70" height="70" /> |<img src="media/interaction_7.5.3_icon_02.png" width="220" height="40" /> |
| Up/down                  |<img src="media/interaction_7.5.3_icon_play2.png" width="160" height="70" /> |<img src="media/interaction_7.5.3_icon_03_02.png" width="220" height="40" /> |
| On/off, Enable/disable   |<img src="media/interaction_7.5.3_icon_play2.png" width="160" height="70" /> |<img src="media/interaction_7.5.3_icon_04.png" width="220" height="40" /> |
| Confirm/start/success    |<img src="media/interaction_7.5.3_icon_play1.png" width="70" height="70" /> |<img src="media/interaction_7.5.3_icon_05.png" width="220" height="40" /> |
| Error/alert              |<img src="media/interaction_7.5.3_icon_play1.png" width="70" height="70" /> |<img src="media/interaction_7.5.3_icon_06.png" width="220" height="40" /> |



> **Tip**  
> Media and system sounds will be automatically muted when users set their sound profile to Mute or Vibration mode.

 

-   **Format**

    We recommend using the open source .ogg format. The file compression ratio should be at least 128 kbps (mono/stereo).

-   **Duration**

    Create a sound file of at least 100 msec. If the sound lasts for less than 100 msec, the system might not be able to play it.

-   **Pitch and Volume**

    Design your sounds considering the range of volume levels. Did you make sure that your sound is not too low or high to avoid straying from the peak range? Is the volume of your sound appropriate at the Gear's default volume level? Does your sound play at all volume levels from 1 to 15?

    Refer to the table below for the default volume of each stream type.  

| Ringtone   | Notification   | Media       | System      |
|:--:|:--:|:--:|:--:|
| 11      | 11        | 7       | 9          |

-   **Sound and vibration**

    Sync sounds and vibrations when you combine them. It might confuse users if sounds and vibrations occur separately for the same feedback.
