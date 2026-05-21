### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## InputTextBaseImpl Class

Basic DALi input text object wrapper.

```csharp
public abstract class InputTextBaseImpl : Tizen.UI.Components.TextBaseImpl
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [TextBaseImpl](Tizen.UI.Components.TextBaseImpl.md 'Tizen.UI.Components.TextBaseImpl') &#129106; InputTextBaseImpl

Derived  
&#8627; [InputEditorImpl](Tizen.UI.Components.InputEditorImpl.md 'Tizen.UI.Components.InputEditorImpl')  
&#8627; [InputFieldImpl](Tizen.UI.Components.InputFieldImpl.md 'Tizen.UI.Components.InputFieldImpl')
### Constructors

<a name='Tizen.UI.Components.InputTextBaseImpl.InputTextBaseImpl()'></a>

## InputTextBaseImpl() Constructor

Constructs a new instance.

```csharp
public InputTextBaseImpl();
```
### Properties

<a name='Tizen.UI.Components.InputTextBaseImpl.CursorPosition'></a>

## InputTextBaseImpl.CursorPosition Property

Gets or sets the cursor position.

```csharp
public int CursorPosition { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.InputTextBaseImpl.InputColor'></a>

## InputTextBaseImpl.InputColor Property

Gets or sets the input color for the text will be added to the input area from now on.

```csharp
public Tizen.UI.Color InputColor { get; set; }
```

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Components.InputTextBaseImpl.InputFontFamily'></a>

## InputTextBaseImpl.InputFontFamily Property

Gets or sets the input font family for the text will be added to the input area from now on.

```csharp
public string InputFontFamily { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.InputTextBaseImpl.InputFontSize'></a>

## InputTextBaseImpl.InputFontSize Property

Gets or sets the input font size for the text will be added to the input area from now on.

```csharp
public float InputFontSize { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.InputTextBaseImpl.InputFontSlant'></a>

## InputTextBaseImpl.InputFontSlant Property

Gets or sets the input font style weight such as Tizen.UI.FontSlant.Italic for the text will be added to the input area from now on..

```csharp
public Tizen.UI.FontSlant InputFontSlant { get; set; }
```

#### Property Value
Tizen.UI.FontSlant

<a name='Tizen.UI.Components.InputTextBaseImpl.InputFontWeight'></a>

## InputTextBaseImpl.InputFontWeight Property

Gets or sets the input font style weight such as Tizen.UI.FontWeight.Bold for the text will be added to the input area from now on..

```csharp
public Tizen.UI.FontWeight InputFontWeight { get; set; }
```

#### Property Value
Tizen.UI.FontWeight

<a name='Tizen.UI.Components.InputTextBaseImpl.InputFontWidth'></a>

## InputTextBaseImpl.InputFontWidth Property

Gets or sets the input font style width such as Tizen.UI.FontWidth.Condensed for the text will be added to the input area from now on..

```csharp
public Tizen.UI.FontWidth InputFontWidth { get; set; }
```

#### Property Value
Tizen.UI.FontWidth

<a name='Tizen.UI.Components.InputTextBaseImpl.InputMethodContext'></a>

## InputTextBaseImpl.InputMethodContext Property

Gets the input method context.

```csharp
public Tizen.UI.InputMethodContext InputMethodContext { get; }
```

#### Property Value
Tizen.UI.InputMethodContext

<a name='Tizen.UI.Components.InputTextBaseImpl.IsEditable'></a>

## InputTextBaseImpl.IsEditable Property

Gets or sets whether the text can be edited.

```csharp
public bool IsEditable { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.InputTextBaseImpl.MaximumLength'></a>

## InputTextBaseImpl.MaximumLength Property

Gets or sets the maximum length of the text.

```csharp
public int MaximumLength { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.InputTextBaseImpl.Placeholder'></a>

## InputTextBaseImpl.Placeholder Property

Gets or sets the placeholder text.

```csharp
public string Placeholder { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.InputTextBaseImpl.PlaceholderColor'></a>

## InputTextBaseImpl.PlaceholderColor Property

Gets or sets the placeholder text color.

```csharp
public Tizen.UI.Color PlaceholderColor { get; set; }
```

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Components.InputTextBaseImpl.SelectedText'></a>

## InputTextBaseImpl.SelectedText Property

Gets the currently selected text.

```csharp
public string SelectedText { get; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.InputTextBaseImpl.SelectedTextIndex'></a>

## InputTextBaseImpl.SelectedTextIndex Property

Gets the index range of the currently selected text.

```csharp
public Tizen.UI.Components.ClosedRange&lt;int> SelectedTextIndex { get; }
```

#### Property Value
[Tizen.UI.Components.ClosedRange&lt;](Tizen.UI.Components.ClosedRange_T_.md 'Tizen.UI.Components.ClosedRange&lt;T>')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[&gt;](Tizen.UI.Components.ClosedRange_T_.md 'Tizen.UI.Components.ClosedRange&lt;T>')

<a name='Tizen.UI.Components.InputTextBaseImpl.SelectionEnabled'></a>

## InputTextBaseImpl.SelectionEnabled Property

Gets or sets whether the text selection is enabled.

```csharp
public bool SelectionEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')
### Methods

<a name='Tizen.UI.Components.InputTextBaseImpl.ClearSelection()'></a>

## InputTextBaseImpl.ClearSelection() Method

Clears the current selection.

```csharp
public void ClearSelection();
```

<a name='Tizen.UI.Components.InputTextBaseImpl.EnableGrabHandle(bool)'></a>

## InputTextBaseImpl.EnableGrabHandle(bool) Method

Enable the grab handle.

```csharp
public void EnableGrabHandle(bool enable);
```
#### Parameters

<a name='Tizen.UI.Components.InputTextBaseImpl.EnableGrabHandle(bool).enable'></a>

`enable` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.InputTextBaseImpl.EnableGrabHandlePopup(bool)'></a>

## InputTextBaseImpl.EnableGrabHandlePopup(bool) Method

Enable the grab handle popup.

```csharp
public void EnableGrabHandlePopup(bool enable);
```
#### Parameters

<a name='Tizen.UI.Components.InputTextBaseImpl.EnableGrabHandlePopup(bool).enable'></a>

`enable` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.InputTextBaseImpl.SelectText(int,int)'></a>

## InputTextBaseImpl.SelectText(int, int) Method

Selects the text within the specified index range.

```csharp
public void SelectText(int startIndex, int endIndex);
```
#### Parameters

<a name='Tizen.UI.Components.InputTextBaseImpl.SelectText(int,int).startIndex'></a>

`startIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The start index of the selection.

<a name='Tizen.UI.Components.InputTextBaseImpl.SelectText(int,int).endIndex'></a>

`endIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The end index of the selection.

<a name='Tizen.UI.Components.InputTextBaseImpl.SelectWholeText()'></a>

## InputTextBaseImpl.SelectWholeText() Method

Selects the whole text.

```csharp
public void SelectWholeText();
```

<a name='Tizen.UI.Components.InputTextBaseImpl.SetCursorBlink(float,float)'></a>

## InputTextBaseImpl.SetCursorBlink(float, float) Method

Enables cursor blink.

```csharp
public void SetCursorBlink(float interval, float duration);
```
#### Parameters

<a name='Tizen.UI.Components.InputTextBaseImpl.SetCursorBlink(float,float).interval'></a>

`interval` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The interval between blinks.

<a name='Tizen.UI.Components.InputTextBaseImpl.SetCursorBlink(float,float).duration'></a>

`duration` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The duration of each blink.

<a name='Tizen.UI.Components.InputTextBaseImpl.SetCursorColor(Tizen.UI.Color)'></a>

## InputTextBaseImpl.SetCursorColor(Color) Method

Sets the cursor color.

```csharp
public void SetCursorColor(Tizen.UI.Color value);
```
#### Parameters

<a name='Tizen.UI.Components.InputTextBaseImpl.SetCursorColor(Tizen.UI.Color).value'></a>

`value` Tizen.UI.Color

<a name='Tizen.UI.Components.InputTextBaseImpl.SetCursorWidth(int)'></a>

## InputTextBaseImpl.SetCursorWidth(int) Method

Sets the cursor width.

```csharp
public void SetCursorWidth(int value);
```
#### Parameters

<a name='Tizen.UI.Components.InputTextBaseImpl.SetCursorWidth(int).value'></a>

`value` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The width of the cursor.

<a name='Tizen.UI.Components.InputTextBaseImpl.SetInputMethodActionButtonTitle(Tizen.UI.ActionButtonTitle)'></a>

## InputTextBaseImpl.SetInputMethodActionButtonTitle(ActionButtonTitle) Method

Sets the input method's action button title.

```csharp
public void SetInputMethodActionButtonTitle(Tizen.UI.ActionButtonTitle actionButtonTitle);
```
#### Parameters

<a name='Tizen.UI.Components.InputTextBaseImpl.SetInputMethodActionButtonTitle(Tizen.UI.ActionButtonTitle).actionButtonTitle'></a>

`actionButtonTitle` Tizen.UI.ActionButtonTitle

The title of the action button.

<a name='Tizen.UI.Components.InputTextBaseImpl.SetInputMethodCapitalMode(Tizen.UI.AutoCapital)'></a>

## InputTextBaseImpl.SetInputMethodCapitalMode(AutoCapital) Method

Sets the input method's capital mode.

```csharp
public void SetInputMethodCapitalMode(Tizen.UI.AutoCapital capitalMode);
```
#### Parameters

<a name='Tizen.UI.Components.InputTextBaseImpl.SetInputMethodCapitalMode(Tizen.UI.AutoCapital).capitalMode'></a>

`capitalMode` Tizen.UI.AutoCapital

The capital mode of the input method.

<a name='Tizen.UI.Components.InputTextBaseImpl.SetInputMethodPanelType(Tizen.UI.PanelLayout)'></a>

## InputTextBaseImpl.SetInputMethodPanelType(PanelLayout) Method

Sets the input method's panel layout.

```csharp
public void SetInputMethodPanelType(Tizen.UI.PanelLayout panelLayout);
```
#### Parameters

<a name='Tizen.UI.Components.InputTextBaseImpl.SetInputMethodPanelType(Tizen.UI.PanelLayout).panelLayout'></a>

`panelLayout` Tizen.UI.PanelLayout

The panel layout of the input method.

<a name='Tizen.UI.Components.InputTextBaseImpl.SetSecondaryCursorColor(Tizen.UI.Color)'></a>

## InputTextBaseImpl.SetSecondaryCursorColor(Color) Method

Sets the secondary cursor color.

```csharp
public void SetSecondaryCursorColor(Tizen.UI.Color value);
```
#### Parameters

<a name='Tizen.UI.Components.InputTextBaseImpl.SetSecondaryCursorColor(Tizen.UI.Color).value'></a>

`value` Tizen.UI.Color

<a name='Tizen.UI.Components.InputTextBaseImpl.SetSelectionColor(Tizen.UI.Color)'></a>

## InputTextBaseImpl.SetSelectionColor(Color) Method

Sets the selection area color.

```csharp
public void SetSelectionColor(Tizen.UI.Color color);
```
#### Parameters

<a name='Tizen.UI.Components.InputTextBaseImpl.SetSelectionColor(Tizen.UI.Color).color'></a>

`color` Tizen.UI.Color

<a name='Tizen.UI.Components.InputTextBaseImpl.SetSelectionHandleImage(string,string)'></a>

## InputTextBaseImpl.SetSelectionHandleImage(string, string) Method

Sets the selection handle images.

```csharp
public void SetSelectionHandleImage(string leftResourceUrl, string rightResourceUrl);
```
#### Parameters

<a name='Tizen.UI.Components.InputTextBaseImpl.SetSelectionHandleImage(string,string).leftResourceUrl'></a>

`leftResourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The Url of the image for the left handle.

<a name='Tizen.UI.Components.InputTextBaseImpl.SetSelectionHandleImage(string,string).rightResourceUrl'></a>

`rightResourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The Url of the image for the right handle.

<a name='Tizen.UI.Components.InputTextBaseImpl.SetSelectionHandlePressedImage(string,string)'></a>

## InputTextBaseImpl.SetSelectionHandlePressedImage(string, string) Method

Sets the pressed selection handle images.

```csharp
public void SetSelectionHandlePressedImage(string leftResourceUrl, string rightResourceUrl);
```
#### Parameters

<a name='Tizen.UI.Components.InputTextBaseImpl.SetSelectionHandlePressedImage(string,string).leftResourceUrl'></a>

`leftResourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The Url of the image for the left handle.

<a name='Tizen.UI.Components.InputTextBaseImpl.SetSelectionHandlePressedImage(string,string).rightResourceUrl'></a>

`rightResourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The Url of the image for the right handle.

<a name='Tizen.UI.Components.InputTextBaseImpl.UnsetCursorBlink()'></a>

## InputTextBaseImpl.UnsetCursorBlink() Method

Disables the cursor blink.

```csharp
public void UnsetCursorBlink();
```
### Events

<a name='Tizen.UI.Components.InputTextBaseImpl.CursorMoved'></a>

## InputTextBaseImpl.CursorMoved Event

Occurs when the cursor moved.

```csharp
public event EventHandler CursorMoved;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.InputTextBaseImpl.MaximumLengthReached'></a>

## InputTextBaseImpl.MaximumLengthReached Event

Occurs when the text has reached to the specified maximum length.

```csharp
public event EventHandler MaximumLengthReached;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.InputTextBaseImpl.SelectionChanged'></a>

## InputTextBaseImpl.SelectionChanged Event

Occurs when the seledction changed.

```csharp
public event EventHandler SelectionChanged;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.InputTextBaseImpl.SelectionCleared'></a>

## InputTextBaseImpl.SelectionCleared Event

Occurs when the selection is cleared.

```csharp
public event EventHandler SelectionCleared;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.InputTextBaseImpl.SelectionStarted'></a>

## InputTextBaseImpl.SelectionStarted Event

Occurs when the selection is started.

```csharp
public event EventHandler SelectionStarted;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.InputTextBaseImpl.TextChanged'></a>

## InputTextBaseImpl.TextChanged Event

Occurs when the text is changed.

```csharp
public event EventHandler TextChanged;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')



























































