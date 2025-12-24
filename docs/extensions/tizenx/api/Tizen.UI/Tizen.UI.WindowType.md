### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## WindowType Enum

An enum of window types.

```csharp
public enum WindowType
```
### Fields

<a name='Tizen.UI.WindowType.Desktop'></a>

`Desktop` 5

Used for desktop windows.  
This is a desktop type. No other windows can be placed below this type of window.

<a name='Tizen.UI.WindowType.Dialog'></a>

`Dialog` 3

Used for simple dialog windows.

<a name='Tizen.UI.WindowType.Ime'></a>

`Ime` 4

Used for IME window that is used for keyboard window.  
It should be set in UIApplication constructor.  
It does not work with Window.Type, because IME window type can not change in runtime.

### Remarks
See [UIApplication](Tizen.UI.UIApplication.md 'Tizen.UI.UIApplication') for this type. <br/>

<a name='Tizen.UI.WindowType.Normal'></a>

`Normal` 0

A default window type.<br/>  
Indicates a normal or top-level window.  
Almost every window will be created with this type.

<a name='Tizen.UI.WindowType.Notification'></a>

`Notification` 1

A notification window, like a warning about battery life or a new email received.

<a name='Tizen.UI.WindowType.Utility'></a>

`Utility` 2

A persistent utility window, like a toolbox or a palette.

### Remarks
Most of window type can be set, except for IME type.<br/>  
IME type can only be used in one of UIApplication's constrcutors.<br/>




