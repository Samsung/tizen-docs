### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## ITextEditable Interface

The ITextEditable interface provides a common set of properties and methods for editable text-based objects.

```csharp
public interface ITextEditable
```

Derived  
&#8627; [InputView](Tizen.UI.InputView.md 'Tizen.UI.InputView')
### Properties

<a name='Tizen.UI.ITextEditable.InputMethodContext'></a>

## ITextEditable.InputMethodContext Property

Gets the input method context.

```csharp
Tizen.UI.InputMethodContext InputMethodContext { get; }
```

#### Property Value
[InputMethodContext](Tizen.UI.InputMethodContext.md 'Tizen.UI.InputMethodContext')

<a name='Tizen.UI.ITextEditable.IsEditable'></a>

## ITextEditable.IsEditable Property

Gets or sets a value indicating whether the text can be editable.

```csharp
bool IsEditable { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.ITextEditable.PlaceholderText'></a>

## ITextEditable.PlaceholderText Property

Gets or sets the placeholder text for the editable text.

```csharp
string PlaceholderText { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')
### Events

<a name='Tizen.UI.ITextEditable.TextChanged'></a>

## ITextEditable.TextChanged Event

Occurs when the Text property changes.

```csharp
event EventHandler TextChanged;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')






