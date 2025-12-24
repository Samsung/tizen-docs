### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## IModalContainer Interface

A container that can show a modal content. It should have a scrim to block the background.

```csharp
public interface IModalContainer
```
### Properties

<a name='Tizen.UI.Components.IModalContainer.ModalContent'></a>

## IModalContainer.ModalContent Property

A modal content to be shown in this container.

```csharp
Tizen.UI.View ModalContent { get; set; }
```

#### Property Value
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')  
UIView to be shown or hidden as modal content

<a name='Tizen.UI.Components.IModalContainer.Scrim'></a>

## IModalContainer.Scrim Property

A scrim to block the background when the modal content is shown.

```csharp
Tizen.UI.View Scrim { get; set; }
```

#### Property Value
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')  
UIView with dimmed background color


























































