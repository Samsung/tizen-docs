### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## AccessibilityActionReceivedEventArgs Class

Provides the data for the View.AccessibilityActionReceived event.

```csharp
public class AccessibilityActionReceivedEventArgs : System.EventArgs
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs') &#129106; AccessibilityActionReceivedEventArgs
### Properties

<a name='Tizen.UI.AccessibilityActionReceivedEventArgs.ActionType'></a>

## AccessibilityActionReceivedEventArgs.ActionType Property

The [AccessibilityAction](Tizen.UI.AccessibilityAction.md 'Tizen.UI.AccessibilityAction') enum indicates what kind of action should be performed on the target view.

```csharp
public Tizen.UI.AccessibilityAction ActionType { get; set; }
```

#### Property Value
[AccessibilityAction](Tizen.UI.AccessibilityAction.md 'Tizen.UI.AccessibilityAction')

<a name='Tizen.UI.AccessibilityActionReceivedEventArgs.Target'></a>

## AccessibilityActionReceivedEventArgs.Target Property

The target view for the action. this is typically null and only set  
when the action semantically requires a concrete child target (e.g., ScrollToChild).

```csharp
public Tizen.UI.View Target { get; set; }
```

#### Property Value
[View](Tizen.UI.View.md 'Tizen.UI.View')






