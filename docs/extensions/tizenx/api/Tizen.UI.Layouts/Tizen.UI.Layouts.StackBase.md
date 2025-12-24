### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## StackBase Class

The StackBase class is an abstract class that represents a layout container. It is used to arrange child elements in a vertical or horizontal stack.

```csharp
public abstract class StackBase : Tizen.UI.Layouts.Layout,
Tizen.UI.Layouts.IStackLayout,
Tizen.UI.Layouts.ILayout
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ViewGroup &#129106; [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') &#129106; StackBase

Derived  
&#8627; [HStack](Tizen.UI.Layouts.HStack.md 'Tizen.UI.Layouts.HStack')  
&#8627; [VStack](Tizen.UI.Layouts.VStack.md 'Tizen.UI.Layouts.VStack')

Implements [IStackLayout](Tizen.UI.Layouts.IStackLayout.md 'Tizen.UI.Layouts.IStackLayout'), [ILayout](Tizen.UI.Layouts.ILayout.md 'Tizen.UI.Layouts.ILayout')
### Properties

<a name='Tizen.UI.Layouts.StackBase.ItemAlignment'></a>

## StackBase.ItemAlignment Property

Gets or sets the alignment of the child elements within the stack.

```csharp
public Tizen.UI.Layouts.LayoutAlignment ItemAlignment { get; set; }
```

Implements [ItemAlignment](Tizen.UI.Layouts.IStackLayout.md#Tizen.UI.Layouts.IStackLayout.ItemAlignment 'Tizen.UI.Layouts.IStackLayout.ItemAlignment')

#### Property Value
[LayoutAlignment](Tizen.UI.Layouts.LayoutAlignment.md 'Tizen.UI.Layouts.LayoutAlignment')

<a name='Tizen.UI.Layouts.StackBase.Spacing'></a>

## StackBase.Spacing Property

Gets or sets the spacing between child elements in the stack.

```csharp
public float Spacing { get; set; }
```

Implements [Spacing](Tizen.UI.Layouts.IStackLayout.md#Tizen.UI.Layouts.IStackLayout.Spacing 'Tizen.UI.Layouts.IStackLayout.Spacing')

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')































































