### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## KeyGrabMode Enum

Enumeration for the key grab mode for platform-level APIs.

```csharp
public enum KeyGrabMode
```
### Fields

<a name='Tizen.UI.KeyGrabMode.Exclusive'></a>

`Exclusive` 3

Grabs a key exclusively regardless of the grabbing-window's position on the window stack mode.

<a name='Tizen.UI.KeyGrabMode.OverrideExclusive'></a>

`OverrideExclusive` 2

Grabs a key exclusively regardless of the grabbing-window's position on the window stack with the possibility of overriding the grab by the other client window mode.

<a name='Tizen.UI.KeyGrabMode.Shared'></a>

`Shared` 1

Grabs a key together with the other client window(s) mode.

<a name='Tizen.UI.KeyGrabMode.Topmost'></a>

`Topmost` 0

Grabs a key only when on the top of the grabbing-window stack mode.






