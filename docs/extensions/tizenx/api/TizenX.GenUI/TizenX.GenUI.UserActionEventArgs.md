### [TizenX.GenUI](TizenX.GenUI.md 'TizenX.GenUI')

## UserActionEventArgs Class

Provides data for the UserAction and
UserAction events.
Contains the message describing the user action that was triggered.

```csharp
public class UserActionEventArgs : EventArgs
```

### Properties

<a name='TizenX.GenUI.UserActionEventArgs.Message'></a>

## Message

Gets or sets the message containing the user action details.

```csharp
public JsonObject Message { get; set; }
```
#### Property Value

JsonObject

A JsonObject containing:

