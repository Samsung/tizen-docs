### [TizenX.Aurum](TizenX.Aurum.md 'TizenX.Aurum')

## UIDevice Class

Represents the UI device interface for performing user interactions and UI automation.
This class provides methods for simulating user input such as touches, clicks, key presses,
and for finding UI elements on the screen. It serves as the main entry point for UI testing.

```csharp
public class UIDevice : Searchable, IDisposable
```

### Properties

<a name='TizenX.Aurum.UIDevice.Instance'></a>

## Instance

Gets the singleton instance of UIDevice.

```csharp
public static UIDevice Instance { get; }
```
#### Property Value

UIDevice

### Methods

<a name='TizenX.Aurum.UIDevice.Click.System.Int32.System.Int32.'></a>

## Click(int, int)

Clicks at a given point on the screen.

```csharp
public bool Click(int x, int y)
```
#### Parameters

`x` int

X coordinate of the point.

`y` int

Y coordinate of the point.

#### Returns

bool

True if the operation was successful, otherwise false.

<a name='TizenX.Aurum.UIDevice.Click.System.Int32.System.Int32.System.UInt32.'></a>

## Click(int, int, uint)

Clicks at a given point on the screen with a specified duration.

```csharp
public bool Click(int x, int y, uint durationMs)
```
#### Parameters

`x` int

X coordinate of the point.

`y` int

Y coordinate of the point.

`durationMs` uint

Duration of the click in milliseconds.

#### Returns

bool

True if the operation was successful, otherwise false.

<a name='TizenX.Aurum.UIDevice.Dispose.System.Boolean.'></a>

## Dispose(bool)

```csharp
protected override void Dispose(bool disposing)
```
#### Parameters

`disposing` bool

<a name='TizenX.Aurum.UIDevice.Drag.System.Int32.System.Int32.System.Int32.System.Int32.System.Int32.System.Int32.'></a>

## Drag(int, int, int, int, int, int)

Drags from one point to another on the screen with a specified number of steps and duration.

```csharp
public bool Drag(int sx, int sy, int ex, int ey, int steps, int durationMs)
```
#### Parameters

`sx` int

X coordinate of the start point.

`sy` int

Y coordinate of the start point.

`ex` int

X coordinate of the end point.

`ey` int

Y coordinate of the end point.

`steps` int

Number of steps for the drag action.

`durationMs` int

Duration of the drag action in milliseconds.

#### Returns

bool

True if the operation was successful, otherwise false.

<a name='TizenX.Aurum.UIDevice.FindObject.TizenX.Aurum.UISelector.'></a>

## FindObject(UISelector)

Finds an object matching the given selector on the screen. If multiple objects match the selector, the first one is returned. If no object matches the selector, null is returned.

```csharp
public override UIObject FindObject(UISelector selector)
```
#### Parameters

`selector` UISelector

#### Returns

UIObject

Returns the UIObject that matches the selector or null if no object matches the selector.

<a name='TizenX.Aurum.UIDevice.FindObjects.TizenX.Aurum.UISelector.'></a>

## FindObjects(UISelector)

```csharp
public override UIObjectVector FindObjects(UISelector selector)
```
#### Parameters

`selector` UISelector

#### Returns

UIObjectVector

<a name='TizenX.Aurum.UIDevice.GenerateKey.TizenX.Aurum.KeyType.TizenX.Aurum.KeyRequestType.'></a>

## GenerateKey(KeyType, KeyRequestType)

```csharp
public bool GenerateKey(KeyType keyType, KeyRequestType keyReqestType)
```
#### Parameters

`keyType` KeyType

`keyReqestType` KeyRequestType

#### Returns

bool

<a name='TizenX.Aurum.UIDevice.GetExternalAppLaunched'></a>

## GetExternalAppLaunched()

```csharp
public bool GetExternalAppLaunched()
```
#### Returns

bool

<a name='TizenX.Aurum.UIDevice.GetMatches.TizenX.Aurum.UISelector.System.Boolean.'></a>

## GetMatches(UISelector, bool)

```csharp
public override UIObjectVector GetMatches(UISelector selector, bool earlyReturn)
```
#### Parameters

`selector` UISelector

`earlyReturn` bool

#### Returns

UIObjectVector

<a name='TizenX.Aurum.UIDevice.GetMatchesInMatches.TizenX.Aurum.UISelector.TizenX.Aurum.UISelector.System.Boolean.'></a>

## GetMatchesInMatches(UISelector, UISelector, bool)

```csharp
public override UIObjectVector GetMatchesInMatches(UISelector firstSelector, UISelector secondSelector, bool earlyReturn)
```
#### Parameters

`firstSelector` UISelector

`secondSelector` UISelector

`earlyReturn` bool

#### Returns

UIObjectVector

<a name='TizenX.Aurum.UIDevice.GetScreenSize'></a>

## GetScreenSize()

Gets the size of the screen.

```csharp
public Size2D GetScreenSize()
```
#### Returns

Size2D

Returns the size of the screen as a Size2D object.

<a name='TizenX.Aurum.UIDevice.GetSystemTime.TizenX.Aurum.TimeRequestType.'></a>

## GetSystemTime(TimeRequestType)

Gets the system time in milliseconds.

```csharp
public long GetSystemTime(TimeRequestType type)
```
#### Parameters

`type` TimeRequestType

#### Returns

long

Returns the system time in milliseconds.

<a name='TizenX.Aurum.UIDevice.GetTargetAngle'></a>

## GetTargetAngle()

```csharp
public int GetTargetAngle()
```
#### Returns

int

<a name='TizenX.Aurum.UIDevice.GetWindowAngle'></a>

## GetWindowAngle()

```csharp
public int GetWindowAngle()
```
#### Returns

int

<a name='TizenX.Aurum.UIDevice.HasObject.TizenX.Aurum.UISelector.'></a>

## HasObject(UISelector)

Checks if an object matching the given selector exists on the screen.

```csharp
public override bool HasObject(UISelector selector)
```
#### Parameters

`selector` UISelector

#### Returns

bool

Returns true if the object exists, otherwise false.

<a name='TizenX.Aurum.UIDevice.MouseDown.System.Int32.System.Int32.System.Int32.'></a>

## MouseDown(int, int, int)

Mouse down at a given point on the screen with a specified button.

```csharp
public bool MouseDown(int x, int y, int button)
```
#### Parameters

`x` int

`y` int

`button` int

#### Returns

bool

Returns true if the operation was successful, otherwise false.

<a name='TizenX.Aurum.UIDevice.MouseMove.System.Int32.System.Int32.System.Int32.'></a>

## MouseMove(int, int, int)

Mouse move at a given point on the screen with a specified button.

```csharp
public bool MouseMove(int x, int y, int button)
```
#### Parameters

`x` int

`y` int

`button` int

#### Returns

bool

The following example demonstrates how to use the MouseMove method.

<a name='TizenX.Aurum.UIDevice.MouseUp.System.Int32.System.Int32.System.Int32.'></a>

## MouseUp(int, int, int)

Mouse up at a given point on the screen with a specified button.

```csharp
public bool MouseUp(int x, int y, int button)
```
#### Parameters

`x` int

`y` int

`button` int

#### Returns

bool

The following example demonstrates how to use the MouseUp method.

<a name='TizenX.Aurum.UIDevice.PressBack.TizenX.Aurum.KeyRequestType.'></a>

## PressBack(KeyRequestType)

```csharp
public bool PressBack(KeyRequestType type)
```
#### Parameters

`type` KeyRequestType

#### Returns

bool

<a name='TizenX.Aurum.UIDevice.PressHome.TizenX.Aurum.KeyRequestType.'></a>

## PressHome(KeyRequestType)

```csharp
public bool PressHome(KeyRequestType type)
```
#### Parameters

`type` KeyRequestType

#### Returns

bool

<a name='TizenX.Aurum.UIDevice.PressKeyCode.System.String.TizenX.Aurum.KeyRequestType.'></a>

## PressKeyCode(string, KeyRequestType)

Presses a key code with a specified request type.

```csharp
public bool PressKeyCode(string keycode, KeyRequestType type)
```
#### Parameters

`keycode` string

`type` KeyRequestType

#### Returns

bool

Returns true if the operation was successful, otherwise false.

<a name='TizenX.Aurum.UIDevice.PressMenu.TizenX.Aurum.KeyRequestType.'></a>

## PressMenu(KeyRequestType)

```csharp
public bool PressMenu(KeyRequestType type)
```
#### Parameters

`type` KeyRequestType

#### Returns

bool

<a name='TizenX.Aurum.UIDevice.PressPower.TizenX.Aurum.KeyRequestType.'></a>

## PressPower(KeyRequestType)

```csharp
public bool PressPower(KeyRequestType type)
```
#### Parameters

`type` KeyRequestType

#### Returns

bool

<a name='TizenX.Aurum.UIDevice.PressVolDown.TizenX.Aurum.KeyRequestType.'></a>

## PressVolDown(KeyRequestType)

```csharp
public bool PressVolDown(KeyRequestType type)
```
#### Parameters

`type` KeyRequestType

#### Returns

bool

<a name='TizenX.Aurum.UIDevice.PressVolUp.TizenX.Aurum.KeyRequestType.'></a>

## PressVolUp(KeyRequestType)

```csharp
public bool PressVolUp(KeyRequestType type)
```
#### Parameters

`type` KeyRequestType

#### Returns

bool

<a name='TizenX.Aurum.UIDevice.RepeatKeyCode.System.String.System.Int32.System.Int32.'></a>

## RepeatKeyCode(string, int, int)

Repeats a key code with a specified interval and duration.

```csharp
public bool RepeatKeyCode(string keycode, int intervalMs, int durationMs)
```
#### Parameters

`keycode` string

`intervalMs` int

`durationMs` int

#### Returns

bool

Returns true if the operation was successful, otherwise false.

<a name='TizenX.Aurum.UIDevice.SendKeyAndWaitForEvents.System.String.TizenX.Aurum.A11yEventType.System.Int32.'></a>

## SendKeyAndWaitForEvents(string, A11yEventType, int)

```csharp
public bool SendKeyAndWaitForEvents(string keycode, A11yEventType type, int timeout)
```
#### Parameters

`keycode` string

`type` A11yEventType

`timeout` int

#### Returns

bool

<a name='TizenX.Aurum.UIDevice.SendKeyAndWaitForEvents.System.String.TizenX.Aurum.A11yEventType.System.Int32.System.String.'></a>

## SendKeyAndWaitForEvents(string, A11yEventType, int, string)

```csharp
public bool SendKeyAndWaitForEvents(string keycode, A11yEventType type, int timeout, string packageName)
```
#### Parameters

`keycode` string

`type` A11yEventType

`timeout` int

`packageName` string

#### Returns

bool

<a name='TizenX.Aurum.UIDevice.TakeScreenshot.System.String.'></a>

## TakeScreenshot(string)

Takes a screenshot of the current screen and saves it to a file.

```csharp
public bool TakeScreenshot(string path)
```
#### Parameters

`path` string

#### Returns

bool

Returns true if the operation was successful, otherwise false.

<a name='TizenX.Aurum.UIDevice.TouchDown.System.Int32.System.Int32.'></a>

## TouchDown(int, int)

Touch down at a given point on the screen. Returns sequence number of the touch event.

```csharp
public int TouchDown(int x, int y)
```
#### Parameters

`x` int

`y` int

#### Returns

int

Sequence number of the touch event

<a name='TizenX.Aurum.UIDevice.TouchMove.System.Int32.System.Int32.System.Int32.'></a>

## TouchMove(int, int, int)

Touch move at a given point on the screen with a specified sequence number.

```csharp
public bool TouchMove(int x, int y, int seq)
```
#### Parameters

`x` int

`y` int

`seq` int

#### Returns

bool

Returns true if the operation was successful, otherwise false.

<a name='TizenX.Aurum.UIDevice.TouchUp.System.Int32.System.Int32.System.Int32.'></a>

## TouchUp(int, int, int)

Touch up at a given point on the screen with a specified sequence number.

```csharp
public bool TouchUp(int x, int y, int seq)
```
#### Parameters

`x` int

`y` int

`seq` int

#### Returns

bool

Returns true if the operation was successful, otherwise false.

<a name='TizenX.Aurum.UIDevice.WaitFor.TizenX.Aurum.FindObjectFunction.'></a>

## WaitFor(FindObjectFunction)

```csharp
public UIObject WaitFor(FindObjectFunction condition)
```
#### Parameters

`condition` FindObjectFunction

#### Returns

UIObject

<a name='TizenX.Aurum.UIDevice.WaitFor.TizenX.Aurum.HasObjectFunction.'></a>

## WaitFor(HasObjectFunction)

```csharp
public bool WaitFor(HasObjectFunction condition)
```
#### Parameters

`condition` HasObjectFunction

#### Returns

bool

<a name='TizenX.Aurum.UIDevice.WaitForEvents.TizenX.Aurum.A11yEventType.System.Int32.'></a>

## WaitForEvents(A11yEventType, int)

```csharp
public bool WaitForEvents(A11yEventType type, int timeout)
```
#### Parameters

`type` A11yEventType

`timeout` int

#### Returns

bool

<a name='TizenX.Aurum.UIDevice.WaitForEvents.TizenX.Aurum.A11yEventType.System.Int32.System.String.'></a>

## WaitForEvents(A11yEventType, int, string)

```csharp
public bool WaitForEvents(A11yEventType type, int timeout, string packageName)
```
#### Parameters

`type` A11yEventType

`timeout` int

`packageName` string

#### Returns

bool

<a name='TizenX.Aurum.UIDevice.WheelDown.System.Int32.System.Int32.'></a>

## WheelDown(int, int)

Wheel down with a specified amount and duration.

```csharp
public bool WheelDown(int amount, int durationMs)
```
#### Parameters

`amount` int

`durationMs` int

#### Returns

bool

Returns true if the operation was successful, otherwise false.

<a name='TizenX.Aurum.UIDevice.WheelUp.System.Int32.System.Int32.'></a>

## WheelUp(int, int)

Wheel up with a specified amount and duration.

```csharp
public bool WheelUp(int amount, int durationMs)
```
#### Parameters

`amount` int

`durationMs` int

#### Returns

bool

Returns true if the operation was successful, otherwise false.

