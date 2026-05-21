### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## BottomSheet Class

A bottom sheet component containing [Content](Tizen.UI.Components.Material.BottomSheet.md#Tizen.UI.Components.Material.BottomSheet.Content 'Tizen.UI.Components.Material.BottomSheet.Content').  
BottomSheet can be set to [ModalContent](Tizen.UI.Components.Material.BottomSheetContainer.md#Tizen.UI.Components.Material.BottomSheetContainer.ModalContent 'Tizen.UI.Components.Material.BottomSheetContainer.ModalContent') to be shown as modal bottom sheet.

```csharp
public class BottomSheet : Tizen.UI.ContentView
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ContentView &#129106; BottomSheet
### Constructors

<a name='Tizen.UI.Components.Material.BottomSheet.BottomSheet()'></a>

## BottomSheet() Constructor

Constructs a bottom sheet.

```csharp
public BottomSheet();
```

<a name='Tizen.UI.Components.Material.BottomSheet.BottomSheet(Tizen.UI.Components.Material.BottomSheetVariables)'></a>

## BottomSheet(BottomSheetVariables) Constructor

Constructs a bottom sheet.

```csharp
public BottomSheet(Tizen.UI.Components.Material.BottomSheetVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.BottomSheet.BottomSheet(Tizen.UI.Components.Material.BottomSheetVariables).variables'></a>

`variables` [BottomSheetVariables](Tizen.UI.Components.Material.BottomSheetVariables.md 'Tizen.UI.Components.Material.BottomSheetVariables')

The variables to apply to the bottom sheet.
### Properties

<a name='Tizen.UI.Components.Material.BottomSheet.Anchors'></a>

## BottomSheet.Anchors Property

The list of anchor of the bottom sheet.  
Each anchor indicates the height of the bottom sheet.

```csharp
public System.Collections.Generic.IReadOnlyList&lt;float> Anchors { get; }
```

#### Property Value
[System.Collections.Generic.IReadOnlyList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyList-1 'System.Collections.Generic.IReadOnlyList`1')[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyList-1 'System.Collections.Generic.IReadOnlyList`1')  
The list of anchor

<a name='Tizen.UI.Components.Material.BottomSheet.Content'></a>

## BottomSheet.Content Property

Content view of the bottom sheet.

```csharp
public Tizen.UI.View Content { get; set; }
```

#### Property Value
Tizen.UI.View  
Content view

<a name='Tizen.UI.Components.Material.BottomSheet.DefaultAnchorIndex'></a>

## BottomSheet.DefaultAnchorIndex Property

The default anchor index of [Anchors](Tizen.UI.Components.Material.BottomSheet.md#Tizen.UI.Components.Material.BottomSheet.Anchors 'Tizen.UI.Components.Material.BottomSheet.Anchors').

```csharp
public int DefaultAnchorIndex { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The default anchor index














































