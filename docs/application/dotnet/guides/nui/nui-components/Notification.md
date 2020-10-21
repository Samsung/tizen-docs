# Notification
Notification is a common component that is help to raise a notification window with a content View.

A Notification can be created using property.

![Notification](./media/notification.png)

## Create with Property

To create a notification using property, follow these steps:

1. Create notification using the default constructor:

    ```cs
    View view = new View();
    notification = new Notification(view);
    ```

2. Set the notification property:

    ```cs
    // Sets a user-defined animation to play when dismiss the notification.
    dismissAni = new Animation(3000);
    notification.SetAnimationOnDismiss(dismissAni);

    // Sets a user-defined animation to play when posting the notification.
    postAni = new Animation(3000);
    notification.SetAnimationOnPost(postAni);

    // Sets a priority level for the specified notification window, includes: None , Base , Medium , High , Top.
    // Need to add the privilege: <privilege>http://tizen.org/privilege/window.priority.set</privilege>.
    notification.SetLevel(NotificationLevel.Base);
  
    // Sets position and size of the notification window.
    positionSize = new Rectangle(0, 0, 600, 300);
    notification.SetPositionSize(positionSize);

    // Post a notification window with the content view.
    // Need to add the privilege: <privilege>http://tizen.org/privilege/window.priority.set</privilege>.
    notification.Post(3000);
    ```

3. Responding to OnWindowTouch:

    ```cs
    bool dismissOnTouch = true;
    notification.SetDismissOnTouch(dismissOnTouch);     // Dismiss notification window on touch if the value is true.
    ```

## Related Information
- Dependencies
  -   Tizen 6.0 and Higher