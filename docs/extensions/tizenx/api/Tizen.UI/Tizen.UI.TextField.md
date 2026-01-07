### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## TextField Class

A text field is an interactive object that the user can enter text into.

```csharp
public class TextField : Tizen.UI.InputView,
Tizen.UI.Internal.ITextFieldSignalHandler
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; [View](Tizen.UI.View.md 'Tizen.UI.View') &#129106; [InputView](Tizen.UI.InputView.md 'Tizen.UI.InputView') &#129106; TextField

Implements Tizen.UI.Internal.ITextFieldSignalHandler
### Constructors

<a name='Tizen.UI.TextField.TextField()'></a>

## TextField() Constructor

Initializes a new instance of the [TextField](Tizen.UI.TextField.md 'Tizen.UI.TextField') class.

```csharp
public TextField();
```
### Properties

<a name='Tizen.UI.TextField.IsPassword'></a>

## TextField.IsPassword Property

Gets or sets a value indicating whether the text field is a password field.

```csharp
public bool IsPassword { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.TextField.TextOverflow'></a>

## TextField.TextOverflow Property

Gets or sets the TextOverflow of the text.

```csharp
public Tizen.UI.TextOverflow TextOverflow { get; set; }
```

#### Property Value
[TextOverflow](Tizen.UI.TextOverflow.md 'Tizen.UI.TextOverflow')
### Methods

<a name='Tizen.UI.TextField.SetInputMethodSetting(Tizen.UI.InputMethodSetting)'></a>

## TextField.SetInputMethodSetting(InputMethodSetting) Method

Sets the input method settings.

```csharp
public override void SetInputMethodSetting(Tizen.UI.InputMethodSetting setting);
```
#### Parameters

<a name='Tizen.UI.TextField.SetInputMethodSetting(Tizen.UI.InputMethodSetting).setting'></a>

`setting` [InputMethodSetting](Tizen.UI.InputMethodSetting.md 'Tizen.UI.InputMethodSetting')

The input method settings.





