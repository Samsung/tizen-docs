### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## BottomSheetContainer Class

A container that can show a bottom sheet. It should have a scrim to block the background. It also has animation for showing and hiding bottom sheet.  
[BottomSheet](Tizen.UI.Components.Material.BottomSheet.md 'Tizen.UI.Components.Material.BottomSheet') can be set to [ModalContent](Tizen.UI.Components.Material.BottomSheetContainer.md#Tizen.UI.Components.Material.BottomSheetContainer.ModalContent 'Tizen.UI.Components.Material.BottomSheetContainer.ModalContent') to be shown as modal bottom sheet.

```csharp
public class BottomSheetContainer : Tizen.UI.ContentView,
Tizen.UI.Components.IModalContainer,
Tizen.UI.Components.INavigationAnimation
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ContentView &#129106; BottomSheetContainer

Implements Tizen.UI.Components.IModalContainer, Tizen.UI.Components.INavigationAnimation
### Constructors

<a name='Tizen.UI.Components.Material.BottomSheetContainer.BottomSheetContainer()'></a>

## BottomSheetContainer() Constructor

Constructs a bottom sheet container.

```csharp
public BottomSheetContainer();
```

<a name='Tizen.UI.Components.Material.BottomSheetContainer.BottomSheetContainer(Tizen.UI.Components.Material.BottomSheetContainerVariables)'></a>

## BottomSheetContainer(BottomSheetContainerVariables) Constructor

Constructs a bottom sheet container.

```csharp
public BottomSheetContainer(Tizen.UI.Components.Material.BottomSheetContainerVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.BottomSheetContainer.BottomSheetContainer(Tizen.UI.Components.Material.BottomSheetContainerVariables).variables'></a>

`variables` [BottomSheetContainerVariables](Tizen.UI.Components.Material.BottomSheetContainerVariables.md 'Tizen.UI.Components.Material.BottomSheetContainerVariables')

The variables to apply to the bottom sheet container.
### Properties

<a name='Tizen.UI.Components.Material.BottomSheetContainer.ModalContent'></a>

## BottomSheetContainer.ModalContent Property

A modal content to be shown in this container.  
A bottom sheet is set as modal content.

```csharp
public Tizen.UI.View ModalContent { get; set; }
```

Implements ModalContent

#### Property Value
Tizen.UI.View  
A bottom sheet

<a name='Tizen.UI.Components.Material.BottomSheetContainer.PopAnimation'></a>

## BottomSheetContainer.PopAnimation Property

Function called for transition animation of navigation pop.

```csharp
public System.Func&lt;Tizen.UI.View,Tizen.UI.View,Tizen.UI.Components.INavigationAnimationController> PopAnimation { get; }
```

Implements PopAnimation

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')Tizen.UI.View[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')Tizen.UI.View[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')Tizen.UI.Components.INavigationAnimationController[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')

### Remarks
The first View of Func is the view to be popped. The fist View will be removed from the navigation stack.

<a name='Tizen.UI.Components.Material.BottomSheetContainer.PopModalAnimation'></a>

## BottomSheetContainer.PopModalAnimation Property

Function called for transition animation of modal pop.

```csharp
public System.Func&lt;Tizen.UI.View,Tizen.UI.View,Tizen.UI.Components.INavigationAnimationController> PopModalAnimation { get; }
```

Implements PopModalAnimation

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')Tizen.UI.View[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')Tizen.UI.View[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')Tizen.UI.Components.INavigationAnimationController[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')

### Remarks
The first View of Func is the modal view to be popped. The fist View will be removed from the modal stack.

<a name='Tizen.UI.Components.Material.BottomSheetContainer.PushAnimation'></a>

## BottomSheetContainer.PushAnimation Property

Function called for transition animation of navigation push.

```csharp
public System.Func&lt;Tizen.UI.View,Tizen.UI.View,Tizen.UI.Components.INavigationAnimationController> PushAnimation { get; }
```

Implements PushAnimation

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')Tizen.UI.View[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')Tizen.UI.View[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')Tizen.UI.Components.INavigationAnimationController[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')

### Remarks
The first View of Func is the view to be pushed. The fist View will be the top view.

<a name='Tizen.UI.Components.Material.BottomSheetContainer.PushModalAnimation'></a>

## BottomSheetContainer.PushModalAnimation Property

Function called for transition animation of modal push.

```csharp
public System.Func&lt;Tizen.UI.View,Tizen.UI.View,Tizen.UI.Components.INavigationAnimationController> PushModalAnimation { get; }
```

Implements PushModalAnimation

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')Tizen.UI.View[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')Tizen.UI.View[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')Tizen.UI.Components.INavigationAnimationController[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')

### Remarks
The first View of Func is the modal view to be pushed. The fist View will be the top view.

<a name='Tizen.UI.Components.Material.BottomSheetContainer.Scrim'></a>

## BottomSheetContainer.Scrim Property

A scrim to block the background when the modal content is shown.

```csharp
public Tizen.UI.View Scrim { get; set; }
```

Implements Scrim

#### Property Value
Tizen.UI.View  
UIView with dimmed background color














































