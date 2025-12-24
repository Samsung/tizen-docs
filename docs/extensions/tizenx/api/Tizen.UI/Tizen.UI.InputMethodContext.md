### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## InputMethodContext Class

The InputMethodContext class provides functions to control the input method framework.

```csharp
public class InputMethodContext : Tizen.UI.NObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; InputMethodContext
### Properties

<a name='Tizen.UI.InputMethodContext.InputMethodArea'></a>

## InputMethodContext.InputMethodArea Property

Gets the input method area.

```csharp
public Tizen.UI.Rect InputMethodArea { get; }
```

#### Property Value
[Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

<a name='Tizen.UI.InputMethodContext.InputPanelState'></a>

## InputMethodContext.InputPanelState Property

Gets the current input panel state.

```csharp
public Tizen.UI.InputPanelState InputPanelState { get; }
```

#### Property Value
[InputPanelState](Tizen.UI.InputPanelState.md 'Tizen.UI.InputPanelState')

<a name='Tizen.UI.InputMethodContext.TextPrediction'></a>

## InputMethodContext.TextPrediction Property

Gets or sets whether text prediction is allowed.

```csharp
public bool TextPrediction { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')
### Methods

<a name='Tizen.UI.InputMethodContext.Activate()'></a>

## InputMethodContext.Activate() Method

Activates the input method context.

```csharp
public void Activate();
```

<a name='Tizen.UI.InputMethodContext.AutoEnableInputPanel(bool)'></a>

## InputMethodContext.AutoEnableInputPanel(bool) Method

Sets whether the input panel is automatically enabled.

```csharp
public void AutoEnableInputPanel(bool enabled);
```
#### Parameters

<a name='Tizen.UI.InputMethodContext.AutoEnableInputPanel(bool).enabled'></a>

`enabled` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True to enable the input panel automatically, false otherwise.

<a name='Tizen.UI.InputMethodContext.Deactivate()'></a>

## InputMethodContext.Deactivate() Method

Deactivates the input method context.

```csharp
public void Deactivate();
```

<a name='Tizen.UI.InputMethodContext.HideInputPanel()'></a>

## InputMethodContext.HideInputPanel() Method

Hides the input panel.

```csharp
public void HideInputPanel();
```

<a name='Tizen.UI.InputMethodContext.NotifyTextInputMultiLine(bool)'></a>

## InputMethodContext.NotifyTextInputMultiLine(bool) Method

Notifies whether the text input is multi-line.

```csharp
public void NotifyTextInputMultiLine(bool multiLine);
```
#### Parameters

<a name='Tizen.UI.InputMethodContext.NotifyTextInputMultiLine(bool).multiLine'></a>

`multiLine` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True if the text input is multi-line, false otherwise.

<a name='Tizen.UI.InputMethodContext.SetInputPanelLanguage(Tizen.UI.InputPanelLanguage)'></a>

## InputMethodContext.SetInputPanelLanguage(InputPanelLanguage) Method

Sets the language of the input panel.

```csharp
public void SetInputPanelLanguage(Tizen.UI.InputPanelLanguage language);
```
#### Parameters

<a name='Tizen.UI.InputMethodContext.SetInputPanelLanguage(Tizen.UI.InputPanelLanguage).language'></a>

`language` [InputPanelLanguage](Tizen.UI.InputPanelLanguage.md 'Tizen.UI.InputPanelLanguage')

The language to be set to the input panel

<a name='Tizen.UI.InputMethodContext.SetInputPanelPosition(uint,uint)'></a>

## InputMethodContext.SetInputPanelPosition(uint, uint) Method

Sets the input panel position.

```csharp
public void SetInputPanelPosition(uint x, uint y);
```
#### Parameters

<a name='Tizen.UI.InputMethodContext.SetInputPanelPosition(uint,uint).x'></a>

`x` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The x coordinate of the input panel.

<a name='Tizen.UI.InputMethodContext.SetInputPanelPosition(uint,uint).y'></a>

`y` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The y coordinate of the input panel.

<a name='Tizen.UI.InputMethodContext.SetInputPanelUserData(string)'></a>

## InputMethodContext.SetInputPanelUserData(string) Method

Sets the input panel user data.

```csharp
public void SetInputPanelUserData(string text);
```
#### Parameters

<a name='Tizen.UI.InputMethodContext.SetInputPanelUserData(string).text'></a>

`text` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The text to set.

<a name='Tizen.UI.InputMethodContext.SetReturnKeyState(bool)'></a>

## InputMethodContext.SetReturnKeyState(bool) Method

Sets the return key state.

```csharp
public void SetReturnKeyState(bool visible);
```
#### Parameters

<a name='Tizen.UI.InputMethodContext.SetReturnKeyState(bool).visible'></a>

`visible` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True to show the return key, false otherwise.

<a name='Tizen.UI.InputMethodContext.ShowInputPanel()'></a>

## InputMethodContext.ShowInputPanel() Method

Shows the input panel.

```csharp
public void ShowInputPanel();
```
### Events

<a name='Tizen.UI.InputMethodContext.InputPanelStateChanged'></a>

## InputMethodContext.InputPanelStateChanged Event

Occurs when the input panel state is changed.

```csharp
public event EventHandler InputPanelStateChanged;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.InputMethodContext.Resized'></a>

## InputMethodContext.Resized Event

Occurs when the keyboard is resized.

```csharp
public event EventHandler Resized;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')






