### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## EditableTextBindings&lt;T> Class

Provides a set of static properties that represent the data-binding capabilities of the [IText](Tizen.UI.IText.md 'Tizen.UI.IText') and [ITextEditable](Tizen.UI.ITextEditable.md 'Tizen.UI.ITextEditable') interface.

```csharp
public static class EditableTextBindings&lt;T>
    where T : Tizen.UI.View, Tizen.UI.IText, Tizen.UI.ITextEditable
```
#### Type parameters

<a name='Tizen.UI.EditableTextBindings_T_.T'></a>

`T`

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; EditableTextBindings&lt;T>
### Properties

<a name='Tizen.UI.EditableTextBindings_T_.TextProperty'></a>

## EditableTextBindings&lt;T>.TextProperty Property

The TextProperty is a two-way bindable property that indicates the text displayed in the [Itext](https://docs.microsoft.com/en-us/dotnet/api/Itext 'Itext') control.

```csharp
public static Tizen.UI.TwoWayBindingProperty&lt;T,string> TextProperty { get; }
```

#### Property Value
[Tizen.UI.TwoWayBindingProperty&lt;](Tizen.UI.TwoWayBindingProperty_TView,TValue_.md 'Tizen.UI.TwoWayBindingProperty&lt;TView,TValue>')[T](Tizen.UI.EditableTextBindings_T_.md#Tizen.UI.EditableTextBindings_T_.T 'Tizen.UI.EditableTextBindings&lt;T>.T')[,](Tizen.UI.TwoWayBindingProperty_TView,TValue_.md 'Tizen.UI.TwoWayBindingProperty&lt;TView,TValue>')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[&gt;](Tizen.UI.TwoWayBindingProperty_TView,TValue_.md 'Tizen.UI.TwoWayBindingProperty&lt;TView,TValue>')






