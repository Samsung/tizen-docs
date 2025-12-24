### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## TextEditor Class

A TextEditor is a multi-line text input control that supports various text editing features.

```csharp
public class TextEditor : Tizen.UI.InputView,
Tizen.UI.Internal.ITextEditorSignalHandler
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; [View](Tizen.UI.View.md 'Tizen.UI.View') &#129106; [InputView](Tizen.UI.InputView.md 'Tizen.UI.InputView') &#129106; TextEditor

Implements [Tizen.UI.Internal.ITextEditorSignalHandler](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Internal.ITextEditorSignalHandler 'Tizen.UI.Internal.ITextEditorSignalHandler')
### Constructors

<a name='Tizen.UI.TextEditor.TextEditor()'></a>

## TextEditor() Constructor

Creates a new TextEditor.

```csharp
public TextEditor();
```
### Properties

<a name='Tizen.UI.TextEditor.IsAbsoluteLineHeight'></a>

## TextEditor.IsAbsoluteLineHeight Property

Gets or sets whether the line height is absolute or relative. Default is false.

```csharp
public bool IsAbsoluteLineHeight { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.TextEditor.LineHeight'></a>

## TextEditor.LineHeight Property

Gets or sets the line height of the text.

```csharp
public float LineHeight { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.TextEditor.TextOverflow'></a>

## TextEditor.TextOverflow Property

Gets or sets the TextOverflow of the text.

```csharp
public Tizen.UI.TextOverflow TextOverflow { get; set; }
```

#### Property Value
[TextOverflow](Tizen.UI.TextOverflow.md 'Tizen.UI.TextOverflow')
### Methods

<a name='Tizen.UI.TextEditor.SetInputMethodSetting(Tizen.UI.InputMethodSetting)'></a>

## TextEditor.SetInputMethodSetting(InputMethodSetting) Method

Sets the input method settings.

```csharp
public override void SetInputMethodSetting(Tizen.UI.InputMethodSetting inputMethod);
```
#### Parameters

<a name='Tizen.UI.TextEditor.SetInputMethodSetting(Tizen.UI.InputMethodSetting).inputMethod'></a>

`inputMethod` [InputMethodSetting](Tizen.UI.InputMethodSetting.md 'Tizen.UI.InputMethodSetting')

The input method settings.




