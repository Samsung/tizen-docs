# Animation

Effective animations help users understand the changes of on-screen elements. Animations express subtle meanings and moods in a way that static designs can't. Animation effects should have a clear purpose to avoid confusing users.

## Look and feel

The Gear can show animations where objects glide across the screen as if they were blown by a breeze. Provide animations with this look and feel by precisely adjusting the timing and ease of the gliding effect.

  ------------------------------------ ------------------------------------
![Do](media/8.4.1.lookandfeel_do_0.mp4)   ![Don't](media/8.4.1.lookandfeel_dont_0.mp4)                      
  ------------------------------------ ------------------------------------

*Animations should glide across the screen like a gentle breeze.*

## Consistent flow

When transitioning between screens, use consistent animations to indicate whether the transition is at a higher, lower, or the same navigational level. Likewise, use the same animation to express the same meaning when animating components in the screen.

-   **Clearly express visual hierarchy**

    Animated transitions between screens should visually show the hierarchy of each screen. Let animations introduce layers based on where the layers are actually coming from. Users should be able to determine the hierarchy of the transitioning screens solely from the animation. For example, it can confuse users if a screen to the left of the current screen comes in from the right-hand side.

      ------------------------------------ ------------------------------------
      ![Do](media/8.4.2.visualhierarchy_do.mp4)   ![Don't](media/8.4.2.visualhierarchy_dont.mp4)
      ------------------------------------ ------------------------------------

    *Animations should show the visual hierarchy between the transitioning screens.*

-   **Use a uniform style**

    Animations that appear simultaneously on the same screen should be consistent. Uniform animations help users understand what is happening on the screen. Only apply a different animation style when there’s a clear reason to do so.

      ------------------------------------ ------------------------------------
      ![Do](media/8.4.2.uniformstyle_do.mp4)   ![Don't](media/8.4.2.uniformstyle_dont.mp4)  
       ------------------------------------ ------------------------------------

    *A uniform animation style should be applied when multiple objects need to appear on the screen at once.*

-   **Maintain a smooth flow.**

    Animations should create a continuous flow. For example, users understand that they’re exploring the same menu if an animation smoothly brings the same element from one screen to the next.

    ![](media/8.4.2.seamlesstransition.mp4)  
    *By consistently providing the same element from one screen to the next, animations can give your app a natural flow.*

<a name="clear_feedback"></a>
## Clear feedback

Animated feedback helps users distinguish outputs from inputs. Feedback should be provided immediately after the user input. A time gap between an input and animation makes it difficult to tell which action the feedback relates to.

-   **Touch feedback**

    Use animations to indicate changes on the screen after a [touch interaction](../interaction/touch.md).

    **Dispersion effect**

    Color transitions and ripple effects should occur in a consistent direction to maximize the impact of the animation. For example, colors should either brighten or darken (not both) and ripple effects should either spread out or in.

    **Duration**

    An animation’s motion should be 300–400 ms.

    **Fade out**

    You can use a fade animation when users release a touch so users know which object they last interacted with.

  ------------------------------------ ------------------------------------
  ![Do](media/8.4.3.touchfeedback_do_6.mp4)   ![Don't](media/8.4.3.touchfeedback_dont_4.mp4)
  ------------------------------------ ------------------------------------

*The fade animation is provided when users release a touch, showing which object they last interacted with. Changing the object size is not recommended.*

-   **Bezel feedback**

    Use animation to indicate elements that respond to a [bezel interaction](../interaction/bezel-interactions.md). Since users don’t obscure the display with their hand when using the bezel, animations can show the impact of any rotary action.

    ![](media/8.4.3.bezel__0.mp4)  

    *When providing feedback on a rotary action, the animation should reflect the direction of the bezel’s rotation.*

## Intuitive interaction

Animations hint at how to interact with your app, allowing users to easily determine which elements they can select and which pages they can transition to. Through your animations, users should be able to predict the result of interactions.

![](media/8.4.4.affordance.mp4)  

*An animation can suggest a rotary action to answer/reject a call.*



File attachments: 

![3.dynamic\_motion.mp4](https://developer.tizen.org/sites/default/files/documentation/3.dynamic_motion.mp4)

![7.2.6.visual\_indicators\_do.mp4](https://developer.tizen.org/sites/default/files/documentation/7.2.6.visual_indicators_do.mp4)

![8.4.1.lookandfeel\_dont.mp4](https://developer.tizen.org/sites/default/files/documentation/8.4.1.lookandfeel_dont_0.mp4)

![8.4.2.seamlesstransition.mp4](https://developer.tizen.org/sites/default/files/documentation/8.4.2.seamlesstransition.mp4)

![8.4.2.uniformstyle\_do.mp4](https://developer.tizen.org/sites/default/files/documentation/8.4.2.uniformstyle_do.mp4)

![8.4.2.uniformstyle\_dont.mp4](https://developer.tizen.org/sites/default/files/documentation/8.4.2.uniformstyle_dont.mp4)

![8.4.2.visualhierarchy\_do.mp4](https://developer.tizen.org/sites/default/files/documentation/8.4.2.visualhierarchy_do.mp4)

![8.4.2.visualhierarchy\_dont.mp4](https://developer.tizen.org/sites/default/files/documentation/8.4.2.visualhierarchy_dont.mp4)

![8.4.3.bezel\_.mp4](https://developer.tizen.org/sites/default/files/documentation/8.4.3.bezel__0.mp4)

![8.4.4.affordance.mp4](https://developer.tizen.org/sites/default/files/documentation/8.4.4.affordance.mp4)

![9.7.overscroll.mp4](https://developer.tizen.org/sites/default/files/documentation/9.7.overscroll.mp4)

![1.2.1.directionconnection1\_health.mp4](https://developer.tizen.org/sites/default/files/documentation/1.2.1.directionconnection1_health.mp4)

![1.2.1.directionconnection2\_moreoption.mp4](https://developer.tizen.org/sites/default/files/documentation/1.2.1.directionconnection2_moreoption.mp4)

![8.4.1.easing\_do.mp4](https://developer.tizen.org/sites/default/files/documentation/8.4.1.easing_do.mp4)

![8.4.1.easing\_do\_nt.mp4](https://developer.tizen.org/sites/default/files/documentation/8.4.1.easing_do_nt.mp4)

![8.4.3.touchfeedback\_do.mp4](https://developer.tizen.org/sites/default/files/documentation/8.4.3.touchfeedback_do_10.mp4)

![8.4.3.touchfeedback\_dont.mp4](https://developer.tizen.org/sites/default/files/documentation/8.4.3.touchfeedback_dont_5.mp4)
