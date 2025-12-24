### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## AlertDialog Class

An alert dialog component containing [Title](Tizen.UI.Components.Material.AlertDialog.md#Tizen.UI.Components.Material.AlertDialog.Title 'Tizen.UI.Components.Material.AlertDialog.Title'), [Message](Tizen.UI.Components.Material.AlertDialog.md#Tizen.UI.Components.Material.AlertDialog.Message 'Tizen.UI.Components.Material.AlertDialog.Message'), and action buttons.  
AlertDialog can be set to [ModalContent](Tizen.UI.Components.Material.DialogContainer.md#Tizen.UI.Components.Material.DialogContainer.ModalContent 'Tizen.UI.Components.Material.DialogContainer.ModalContent') to be shown as modal dialog.

```csharp
public class AlertDialog : Tizen.UI.Components.Material.Dialog
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; [Dialog](Tizen.UI.Components.Material.Dialog.md 'Tizen.UI.Components.Material.Dialog') &#129106; AlertDialog
### Constructors

<a name='Tizen.UI.Components.Material.AlertDialog.AlertDialog()'></a>

## AlertDialog() Constructor

Constructs a alert dialog.

```csharp
public AlertDialog();
```

<a name='Tizen.UI.Components.Material.AlertDialog.AlertDialog(Tizen.UI.Components.Material.AlertDialogVariables)'></a>

## AlertDialog(AlertDialogVariables) Constructor

Constructs an alert dialog.

```csharp
public AlertDialog(Tizen.UI.Components.Material.AlertDialogVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.AlertDialog.AlertDialog(Tizen.UI.Components.Material.AlertDialogVariables).variables'></a>

`variables` [AlertDialogVariables](Tizen.UI.Components.Material.AlertDialogVariables.md 'Tizen.UI.Components.Material.AlertDialogVariables')

The variables to apply to the alert dialog.
### Properties

<a name='Tizen.UI.Components.Material.AlertDialog.Message'></a>

## AlertDialog.Message Property

Text string of alert dialog message.

```csharp
public string Message { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
Text string of alert dialog message.

<a name='Tizen.UI.Components.Material.AlertDialog.Title'></a>

## AlertDialog.Title Property

Text string of alert dialog title.

```csharp
public string Title { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
Text string of alert dialog title.













































