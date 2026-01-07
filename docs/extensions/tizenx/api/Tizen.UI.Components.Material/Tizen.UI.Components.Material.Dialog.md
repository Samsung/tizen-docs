### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## Dialog Class

A dialog component containing [HeaderView](Tizen.UI.Components.Material.Dialog.md#Tizen.UI.Components.Material.Dialog.HeaderView 'Tizen.UI.Components.Material.Dialog.HeaderView'), [BodyView](Tizen.UI.Components.Material.Dialog.md#Tizen.UI.Components.Material.Dialog.BodyView 'Tizen.UI.Components.Material.Dialog.BodyView'), and [FooterView](Tizen.UI.Components.Material.Dialog.md#Tizen.UI.Components.Material.Dialog.FooterView 'Tizen.UI.Components.Material.Dialog.FooterView').  
Dialog can be set to [ModalContent](Tizen.UI.Components.Material.DialogContainer.md#Tizen.UI.Components.Material.DialogContainer.ModalContent 'Tizen.UI.Components.Material.DialogContainer.ModalContent') to be shown as modal dialog.

```csharp
public class Dialog : Tizen.UI.ContentView
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ContentView &#129106; Dialog

Derived  
&#8627; [AlertDialog](Tizen.UI.Components.Material.AlertDialog.md 'Tizen.UI.Components.Material.AlertDialog')
### Constructors

<a name='Tizen.UI.Components.Material.Dialog.Dialog()'></a>

## Dialog() Constructor

Constructs a dialog.

```csharp
public Dialog();
```

<a name='Tizen.UI.Components.Material.Dialog.Dialog(Tizen.UI.Components.Material.DialogVariables)'></a>

## Dialog(DialogVariables) Constructor

Constructs a dialog.

```csharp
public Dialog(Tizen.UI.Components.Material.DialogVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Dialog.Dialog(Tizen.UI.Components.Material.DialogVariables).variables'></a>

`variables` [DialogVariables](Tizen.UI.Components.Material.DialogVariables.md 'Tizen.UI.Components.Material.DialogVariables')

The variables to apply to the dialog.
### Properties

<a name='Tizen.UI.Components.Material.Dialog.BodyView'></a>

## Dialog.BodyView Property

Body view of the dialog.

```csharp
public Tizen.UI.View BodyView { get; set; }
```

#### Property Value
Tizen.UI.View  
A view of body

<a name='Tizen.UI.Components.Material.Dialog.FooterView'></a>

## Dialog.FooterView Property

Footer view of the dialog.

```csharp
public Tizen.UI.View FooterView { get; set; }
```

#### Property Value
Tizen.UI.View  
A view of footer

<a name='Tizen.UI.Components.Material.Dialog.HeaderView'></a>

## Dialog.HeaderView Property

Header view of the dialog.

```csharp
public Tizen.UI.View HeaderView { get; set; }
```

#### Property Value
Tizen.UI.View  
A view of header














































