### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## FlexLayoutManager Class

Provides a layout manager for FlexBox layout.

```csharp
public class FlexLayoutManager :
Tizen.UI.Layouts.ILayoutManager
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; FlexLayoutManager

Implements [ILayoutManager](Tizen.UI.Layouts.ILayoutManager.md 'Tizen.UI.Layouts.ILayoutManager')
### Constructors

<a name='Tizen.UI.Layouts.FlexLayoutManager.FlexLayoutManager(Tizen.UI.Layouts.IFlexBox)'></a>

## FlexLayoutManager(IFlexBox) Constructor

Initializes a new instance of the FlexLayoutManager class.

```csharp
public FlexLayoutManager(Tizen.UI.Layouts.IFlexBox flexLayout);
```
#### Parameters

<a name='Tizen.UI.Layouts.FlexLayoutManager.FlexLayoutManager(Tizen.UI.Layouts.IFlexBox).flexLayout'></a>

`flexLayout` [IFlexBox](Tizen.UI.Layouts.IFlexBox.md 'Tizen.UI.Layouts.IFlexBox')

The IFlexBox instance to be managed by this layout manager.
### Methods

<a name='Tizen.UI.Layouts.FlexLayoutManager.ArrangeChildren(Tizen.UI.Rect)'></a>

## FlexLayoutManager.ArrangeChildren(Rect) Method

Arranges the children of the FlexBox according to the layout rules.

```csharp
public Tizen.UI.Size ArrangeChildren(Tizen.UI.Rect bounds);
```
#### Parameters

<a name='Tizen.UI.Layouts.FlexLayoutManager.ArrangeChildren(Tizen.UI.Rect).bounds'></a>

`bounds` Tizen.UI.Rect

The available space for the layout.

Implements [ArrangeChildren(Rect)](Tizen.UI.Layouts.ILayoutManager.md#Tizen.UI.Layouts.ILayoutManager.ArrangeChildren(Tizen.UI.Rect) 'Tizen.UI.Layouts.ILayoutManager.ArrangeChildren(Tizen.UI.Rect)')

#### Returns
Tizen.UI.Size  
The final size of the FlexBox after arranging its children.































































