
# Navigation

## Overview

Tizen.UI provides a system to organize screens and navigate between them.

`Scaffold` class helps to organize a screen as a formatted full screen.
`DialogContainer` class helps to show a dialog on the screen.

`Navigator` class helps to navigate between views. `Navigator` has a LIFO structure to manage views by asynchronous stack methods such as `PushAsync` and `PopAsync` methods. `CurrentView` of `Navigator`, which has been pushed last, is displayed on the screen by overlapping the previous view.

## Navigator

`Navigator` class helps to navigate between views. `Navigator` has a LIFO structure to manage views by asynchronous stack methods such as `PushAsync` and `PopAsync` methods. `CurrentView` of `Navigator`, which has been pushed last, is displayed on the screen by overlapping the previous view.

> [!IMPORTANT]
> A view pushed onto the stack of `Navigator` can get its direct `Navigator` (the closest ancestor `Navigator`) by using `View` extension method `GetNavigation()`.
> A view pushed onto the stack of `Navigator` can get its root `Navigator` (the farthest ancestor `Navigator`) by using `View` extension method `GetRootNavigation()`.
> ```
> // Push a new view to Navigator.
> view.GetNavigation().PushAsync(newView);
> ```
> ```
> // Navigate back (pop a view) from root Navigator.
> // Root Navigator requests its CurrentView to handle back navigation and then handles back navigation if its CurrentView does not handle back navigation.
> // Therefore, NavigateBack() should be called by root Navigator for nested Navigator case.
> // Otherwise, child Navigator cannot be popped from its parent Navigator when nothing to be popped by child Navigator.
> view.GetRootNavigation().NavigateBack();
> ```

### Push Navigation

`PushAsync` is an asynchronous method to push a view onto the stack of `Navigator`.

```csharp
navigator.PushAsync(scaffold);
```

`PushModalAsync` is an asynchronous method to push a modal view such as dialog onto the stack of `Navigator`.

```csharp
navigator.PushModalAsync(dialogContainer);
```

### Pop Navigation

`PopAsync` is an asynchronous method to pop a view from the stack of `Navigator`.

```csharp
navigator.PopAsync();
```

`PopModalAsync` is an asynchronous method to pop a modal view such as dialog from the stack of `Navigator`.

```csharp
navigator.PopModalAsync();
```

> [!IMPORTANT]
> `PopAsync` and `PopModalAsync` are called for back navigation.
> To enable `CurrentView` to customize its actions to back navigation, please call `NavigateBack` instead of calling `PopAsync` and `PopModalAsync` directly.

### Back Navigation

`NavigateBack` is a method to navigate back by user command such as tapping hardware back button.

> [!IMPORTANT]
> `NavigateBack` calls `PopModalAsync` and returns true if `CurrentView` is a modal view.
> `NavigateBack` calls `PopAsync` and returns true if `CurrentView` is not a modal view and there are at least two views in the stack of `Navigator`.
> `NavigateBack` returns false without pop navigation if none of the above conditions is satisfied.

To navigate back by tapping hardward back button, application needs to implement as follows.

```csharp
window.KeyEvent += OnKeyEvent;
```

```csharp
private void OnKeyEvent(object sender, KeyEventArgs e)
{
    if (e.KeyEvent.State == KeyState.Up && e.KeyEvent.KeyPressedName == "XF86Back")
    {
        if (navigator.NavigateBack() == false)
        {
            // If NavigateBack does nothing because pop naviation is not appropriate, then terminate the application.
            Exit();
        }
    }
}
```

To make a view customize its action to navigating back, application needs to implement `INavigateBackHandler` as follows.

```csharp
public bool HandleNavigateBack()
{
    if (...)
    {
        // Return true if back navigation is handled by this view.
        // If so, navigator does not handle back navigation. (does not pop this view)
        return true;
    }

    // Return false if back navigation is not handled by this view.
    // If so, navigator handles back navigation. (pops this view)
    return false;
}
```

### Current View

`CurrentView` is a property that returns the top view of the stack of `Navigator`.

### Dispose Popped View

To dispose popped view, application needs to implement `INavigationTransition` as follows.

```csharp
public void WillAppear(bool byPopNavigation)
{
}

public void WillDisappear(bool byPopNavigation)
{
}

public void DidAppear(bool byPopNavigation)
{
}

public void DidDisappear(bool byPopNavigation)
{
    if (byPopNavigation)
    {
        // Dispose this view when this view has disappeared by pop navigation.
        Dispose();
    }
}
```

> [!IMPORTANT]
> Application can dispose a view pushed onto the stack of `Navigator` only if either it has disappeared by pop navigation or it is removed from `Navigator`.
