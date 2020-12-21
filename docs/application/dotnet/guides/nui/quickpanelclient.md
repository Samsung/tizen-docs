# Quickpanel client

Quickpanel is a library to control the Quickpanel service window that shows notifications and system setup widgets. You can use Quickpanel client to get various information from the Quickpanel service window and change the values on purposes. For example, media player application needs to close the Quickpanel service window during playback of video. In this case, you can use the media player as the Quickpanel client.

## Prerequisites
To use the methods of the [Quickpanel API](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.WindowSystem.Shell.QuickPanelClient.html), use `Tizen.NUI.WindowSystem.Shell` in your application:
```
using Tizen.NUI.WindowSystem.Shell;
```

## Create QuickPanel handle
After you have created the main window of your application, call `QuickPanelClient()` with a `TizenShell` and window to create the handler:
```
private void onInitialize()
{
    Window window = NUIApplication.GetDefaultWindow();
    TizenShell tzShell = new TizenShell();
    QuickPanelClient qpClient = new QuickPanelClient(tzShell, window, QuickPanelClient.Types.SystemDefault);

    // Do something with qpClient
}
```

## Show or hide Quickpanel window
To show or hide the Quickpanel service window when your application’s window is activated, use the following code:
```
public void qpShowHide()
{
    Window window = NUIApplication.GetDefaultWindow();
    TizenShell tzShell = new TizenShell();
    QuickPanelClient qpClient = new QuickPanelClient(tzShell, window, QuickPanelClient.Types.SystemDefault);

    qpClient.Hide();

    // Do something without Quickpanel

    qpClient.Show();
}
```

## Get state of Quickpanel window
The Quickpanel window supports three states: `VisibleState`, `Orientation`, and `ScrollableState`. To get the current status for each of the Quickpanel service window state, use the following codes:
```
// After qpClient is created

VisibleState visible = qpClient.Visible;
Window.WindowOrientation orientation = qpClient.Orientation;
ScrollableState scrollable = qpClient.Scrollable;
```
The following are the description of states:
- **VisibleState**: The visible state of Quickpanel service window. The three possible values for VisibleState are `Unknown`, `Shown`, or `Hidden`.
- **Orientation**: The orientation of Quickpanel service window. The four possible orientation angles are `Portrait`, `Landscape`, `PortraitInverse`, or `LandscapeInverse`.
- **ScrollableState**: The scrollable state of Quickpanel service window. The possible values for scrollable states are:
    - `Unknown`: Unknown state.
    - `Set`: Set the Quickpanel service window as scrollable.
    - `Unset`: Set the Quickpanel service window as not scrollable.
    - `Retain`: Follow the scrollable state of beneath Quickpanel client window. If there is no other Quickpanel client window under, keep the previous scrollable state.

## Set scrollable state of Quickpanel window
Quickpanel client window can control scrollable state of the Quickpanel service window. If the `Scrollable` is set to `Unset`, then the Quickpanel window does not allow the user to scroll in the Quickpanel region. To change the scrollable state, use the following code:


```
// To Unset the Scrollable state after creating qpClient
qpClient.Scrollable = QuickPanelClient.ScrollableState.Unset;

// Do something with Quickpanel that not scrollable

// To Set the Scrollable state
qpClient.Scrollable = QuickPanelClient.ScrollableState.Set;
```

## Register a changed event for Quickpanel window
To get notified about the state changes, implement the `VisibleChanged` or `OrientationChanged` event callback function.
### VisibleChanged
If you want to change your application’s behavior to match the visibility of the Quickpanel service window, you need to handle the state change event. To handle the state change event, use the following code:
```
public void OnVisibleEvent(object sender, QuickPanelClient.VisibleState visibleState)
{
    // Do something with visibleState
}

public void afterQPClientCreated()
{
    qpClient.VisibleChanged += OnVisibleEvent;
}
```

### OrientationChanged
Alternatively, to change your application's behavior with the orientation changes of the Quickpanel service window, you need to handle the orientation changed event. To handle the state change event, use the following code:
```
public void OnOrientationEvent(object sender, Window.WindowOrientation orientationState)
{
    // Do something with orientationState
}

public void afterQPClientCreated()
{
    qpClient.OrientationChanged += OnOrientationEvent;
}
```

## Related information
- Dependencies
  - Tizen 6.0 and Higher
  - Tizen .NET SDK 1.1.5 and Higher

