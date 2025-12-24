### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## StackLayoutManager Class

Provides a base class for layout managers that arrange child elements in a stack.

```csharp
public abstract class StackLayoutManager : Tizen.UI.Layouts.LayoutManager
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [LayoutManager](Tizen.UI.Layouts.LayoutManager.md 'Tizen.UI.Layouts.LayoutManager') &#129106; StackLayoutManager

Derived  
&#8627; [HStackLayoutManager](Tizen.UI.Layouts.HStackLayoutManager.md 'Tizen.UI.Layouts.HStackLayoutManager')  
&#8627; [VStackLayoutManager](Tizen.UI.Layouts.VStackLayoutManager.md 'Tizen.UI.Layouts.VStackLayoutManager')
### Constructors

<a name='Tizen.UI.Layouts.StackLayoutManager.StackLayoutManager(Tizen.UI.Layouts.IStackLayout)'></a>

## StackLayoutManager(IStackLayout) Constructor

Initializes a new instance of the [StackLayoutManager](Tizen.UI.Layouts.StackLayoutManager.md 'Tizen.UI.Layouts.StackLayoutManager') class.

```csharp
public StackLayoutManager(Tizen.UI.Layouts.IStackLayout stack);
```
#### Parameters

<a name='Tizen.UI.Layouts.StackLayoutManager.StackLayoutManager(Tizen.UI.Layouts.IStackLayout).stack'></a>

`stack` [IStackLayout](Tizen.UI.Layouts.IStackLayout.md 'Tizen.UI.Layouts.IStackLayout')

The stack control that uses this layout manager.
### Properties

<a name='Tizen.UI.Layouts.StackLayoutManager.Stack'></a>

## StackLayoutManager.Stack Property

Gets the stack control that uses this layout manager.

```csharp
public Tizen.UI.Layouts.IStackLayout Stack { get; }
```

#### Property Value
[IStackLayout](Tizen.UI.Layouts.IStackLayout.md 'Tizen.UI.Layouts.IStackLayout')






























































