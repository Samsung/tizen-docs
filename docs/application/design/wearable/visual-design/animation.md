# Animation

Effective animations help users understand changes in on-screen elements. Animations can express subtle meanings and moods in a way that static designs can't. Animation effects should have a clear purpose to avoid confusing users.

## Look and feel

The Gear can show animations where objects glide across the screen as if they were blown by a breeze. Provide animations with this look and feel by precisely adjusting the timing and ease of the gliding effect.

<table>
<tr>
<td width="346"> <video controls>
    <source src="media/8.4.1.lookandfeel_do_0.mp4" type=video/mp4>
  </video> </td>
<td> <video controls>
  <source src="media/8.4.1.lookandfeel_dont_0.mp4" type=video/mp4>
  </video> </td>
</tr>
<tr>
<td> <img src="media/do_bar.png" /> </td>
<td> <img src="media/dont_bar-296x12.png" /> </td>
</tr>
</table>

*Animations should glide across the screen like a gentle breeze.*

## Consistent flow

When transitioning between screens, use consistent animations to indicate whether the transition is at a higher, lower, or equivalent navigational level. Likewise, when animating components in the screen, use the same animation to express the same meaning.

- **Clearly express visual hierarchy**

    Animated transitions between screens should visually show the hierarchy of each screen. Let animations introduce layers based on where the layers are actually coming from. Users should be able to determine the hierarchy of the transitioning screens solely from the animation. For example, it can confuse users if a screen to the left of the current screen comes in from the right-hand side.


  <table>
    <tr>
    <td width="360"> <video controls width="360">       <source src="media/8.4.2.visualhierarchy_do.mp4" type=video/mp4>
      </video> </td>
    <td> <video controls width="360">      <source src="media/8.4.2.visualhierarchy_dont.mp4" type=video/mp4>
      </video> </td>
    </tr>
    <tr>
    <td> <img src="media/do_bar.png" /> </td>
    <td> <img src="media/dont_bar-296x12.png" /> </td>
    </tr>
  </table>

    *Animations should show the hierarchy of the transitioning screens.*

-   **Use a uniform style**

    Animations that appear simultaneously on the same screen should be consistent. Uniform animations help users understand what is happening on the screen. Only apply a different animation style when there's a clear reason to do so.

      <table>
		<tr>
        <td width="360"> <video controls width="360">       <source src="media/8.4.2.uniformstyle_do.mp4" type=video/mp4>
          </video> </td>
        <td> <video controls width="360">      <source src="media/8.4.2.uniformstyle_dont.mp4" type=video/mp4>
          </video> </td>
        </tr>
        <tr>
        <td> <img src="media/do_bar.png" /> </td>
        <td> <img src="media/dont_bar-296x12.png" /> </td>
        </tr>
      </table>

    *A uniform animation style should be applied when multiple objects need to appear on the screen at once.*

-   **Maintain a smooth flow.**

    Animated feedback helps users distinguish outputs from inputs. Feedback should be provided immediately after user input. A time gap between an input and animation makes it difficult to tell which action the feedback relates to.

    <video controls width="360">
      <source src="media/8.4.2.seamlesstransition.mp4" type=video/mp4>
    </video>

    *By consistently showing the same element from one screen to the next, animations can give your app a natural flow.*


<a name="clear_feedback"></a>
## Clear feedback

Animated feedback helps users distinguish outputs from inputs. Feedback should be provided immediately after the user input. A time gap between an input and animation makes it difficult to tell which action the feedback relates to.

-  **Touch feedback**

    Use animations to indicate changes on the screen after a [touch interaction](../interaction/touch.md).

-   **Dispersion effect**

    Color transitions and ripple effects should occur in a consistent direction to maximize the impact of the animation. For example, colors should either brighten or darken (not both) and ripple effects should either spread out or in.

-   **Duration**

    An animation's motion should be 300–400 ms.

-   **Fade out**

    You can use a fade animation when users release a touch so users know which object they last interacted with.

  <table>
    <tr>
    <td width="412"> <video controls width="412">       <source src="media/8.4.3.touchfeedback_do_6.mp4" type=video/mp4>
      </video> </td>
    <td> <video controls width="412">      <source src="media/8.4.3.touchfeedback_dont_4.mp4" type=video/mp4>
      </video> </td>
    </tr>
    <tr>
    <td> <img src="media/do_bar.png" /> </td>
    <td> <img src="media/dont_bar-296x12.png" /> </td>
    </tr>
  </table>


*The fade animation is provided when users release a touch, showing which object they last interacted with. We recommend against changing the object size.*

-   **Bezel feedback**

    Use animation to indicate elements that respond to a [bezel interaction](../interaction/bezel-interactions.md). Since users don't obscure the display with their hand when using the bezel, animations can show the impact of any rotary action.

    <video controls width="360">
      <source src="media/8.4.3.bezel__0.mp4" type=video/mp4>
    </video>

    *When providing feedback on a rotary action, the animation should reflect the direction of the bezel's rotation.*

## Intuitive interaction

Animations hint at how to interact with your app, allowing users to determine which elements they can select and which pages they can transition to. Users should be able to predict the result of interactions through your animations.

<video controls width="360">
  <source src="media/8.4.4.affordance.mp4" type=video/mp4>
</video>  

*An animation can suggest a rotary action to answer/reject a call.*
