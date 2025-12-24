### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## DialogContainer Class

A container that can show a dialog. It should have a scrim to block the background. It also has animation for showing and hiding dialog.  
[Dialog](Tizen.UI.Components.Material.Dialog.md 'Tizen.UI.Components.Material.Dialog') and [AlertDialog](Tizen.UI.Components.Material.AlertDialog.md 'Tizen.UI.Components.Material.AlertDialog') can be set to [ModalContent](Tizen.UI.Components.Material.DialogContainer.md#Tizen.UI.Components.Material.DialogContainer.ModalContent 'Tizen.UI.Components.Material.DialogContainer.ModalContent') to be shown as modal dialog.

```csharp
public class DialogContainer : Tizen.UI.ContentView,
Tizen.UI.Components.IModalContainer
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; DialogContainer

Implements [Tizen.UI.Components.IModalContainer](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IModalContainer 'Tizen.UI.Components.IModalContainer')
### Constructors

<a name='Tizen.UI.Components.Material.DialogContainer.DialogContainer()'></a>

## DialogContainer() Constructor

Constructs a dialog container.

```csharp
public DialogContainer();
```

<a name='Tizen.UI.Components.Material.DialogContainer.DialogContainer(Tizen.UI.Components.Material.DialogContainerVariables)'></a>

## DialogContainer(DialogContainerVariables) Constructor

Constructs a dialog container.

```csharp
public DialogContainer(Tizen.UI.Components.Material.DialogContainerVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DialogContainer.DialogContainer(Tizen.UI.Components.Material.DialogContainerVariables).variables'></a>

`variables` [DialogContainerVariables](Tizen.UI.Components.Material.DialogContainerVariables.md 'Tizen.UI.Components.Material.DialogContainerVariables')

The variables to apply to the dialog container.
### Properties

<a name='Tizen.UI.Components.Material.DialogContainer.ModalContent'></a>

## DialogContainer.ModalContent Property

A modal content to be shown in this container.  
A dialog is set as modal content.

```csharp
public Tizen.UI.View ModalContent { get; set; }
```

Implements [ModalContent](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IModalContainer.ModalContent 'Tizen.UI.Components.IModalContainer.ModalContent')

#### Property Value
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')  
A dialog

<a name='Tizen.UI.Components.Material.DialogContainer.Scrim'></a>

## DialogContainer.Scrim Property

A scrim to block the background when the modal content is shown.

```csharp
public Tizen.UI.View Scrim { get; set; }
```

Implements [Scrim](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IModalContainer.Scrim 'Tizen.UI.Components.IModalContainer.Scrim')

#### Property Value
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')  
UIView with dimmed background color
### Methods

<a name='Tizen.UI.Components.Material.DialogContainer.SwapModalContent(Tizen.UI.View)'></a>

## DialogContainer.SwapModalContent(View) Method

Sets a modal content to be shown in this container with the content swap animation.  
A dialog is set as modal content.  
If ModalContent is null, it will not show the content swap animation.

```csharp
public System.Threading.Tasks.Task SwapModalContent(Tizen.UI.View newModalContent);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DialogContainer.SwapModalContent(Tizen.UI.View).newModalContent'></a>

`newModalContent` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

New modal content.

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')  
Task of the content swap animation.

### Remarks
For the continuation task, please specify [System.Threading.Tasks.TaskScheduler](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.TaskScheduler 'System.Threading.Tasks.TaskScheduler') as the current synchronization context to ensure that the continuation runs on the UI thread.  
For example,  
  
```csharp  
dialogContainer.SwapModalContent(newModalContent).ContinueWith(finishedCallback, TaskScheduler.FromCurrentSynchronizationContext());  
```













































