### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## IAnchoredModal Interface

A modal content to be poped up from the anchor object.

```csharp
public interface IAnchoredModal
```
### Properties

<a name='Tizen.UI.Components.IAnchoredModal.ModalPivot'></a>

## IAnchoredModal.ModalPivot Property

Gets the modal pivot.

```csharp
Tizen.UI.Components.ModalPivot ModalPivot { get; }
```

#### Property Value
[ModalPivot](Tizen.UI.Components.ModalPivot.md 'Tizen.UI.Components.ModalPivot')
### Methods

<a name='Tizen.UI.Components.IAnchoredModal.Post(Tizen.UI.Window,Tizen.UI.Rect)'></a>

## IAnchoredModal.Post(Window, Rect) Method

Post as a modal to the given window with anchor data.

```csharp
void Post(Tizen.UI.Window window, Tizen.UI.Rect anchorBounds);
```
#### Parameters

<a name='Tizen.UI.Components.IAnchoredModal.Post(Tizen.UI.Window,Tizen.UI.Rect).window'></a>

`window` Tizen.UI.Window

<a name='Tizen.UI.Components.IAnchoredModal.Post(Tizen.UI.Window,Tizen.UI.Rect).anchorBounds'></a>

`anchorBounds` Tizen.UI.Rect
### Events

<a name='Tizen.UI.Components.IAnchoredModal.Dismissed'></a>

## IAnchoredModal.Dismissed Event

Occurred when the dismissed.

```csharp
event EventHandler Dismissed;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')



























































