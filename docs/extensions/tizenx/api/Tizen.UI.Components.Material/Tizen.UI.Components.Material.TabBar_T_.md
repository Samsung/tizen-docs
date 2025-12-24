### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## TabBar&lt;T> Class

TabBar provides a horizontal layout to display TabItems.

```csharp
public class TabBar&lt;T> : Tizen.UI.Components.SelectionGroupBox&lt;T>
    where T : Tizen.UI.View, Tizen.UI.Components.IGroupSelectable
```
#### Type parameters

<a name='Tizen.UI.Components.Material.TabBar_T_.T'></a>

`T`

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ContentView &#129106; Tizen.UI.Components.SelectionGroupBox&lt;[T](Tizen.UI.Components.Material.TabBar_T_.md#Tizen.UI.Components.Material.TabBar_T_.T 'Tizen.UI.Components.Material.TabBar&lt;T>.T')&gt; &#129106; TabBar&lt;T>

Derived  
&#8627; [BottomBar&lt;T&gt;](Tizen.UI.Components.Material.BottomBar_T_.md 'Tizen.UI.Components.Material.BottomBar&lt;T>')  
&#8627; [TabBar](Tizen.UI.Components.Material.TabBar.md 'Tizen.UI.Components.Material.TabBar')
### Constructors

<a name='Tizen.UI.Components.Material.TabBar_T_.TabBar()'></a>

## TabBar() Constructor

Construct a new instance.

```csharp
public TabBar();
```

<a name='Tizen.UI.Components.Material.TabBar_T_.TabBar(Tizen.UI.Components.Material.TabBarVariables)'></a>

## TabBar(TabBarVariables) Constructor

Construct a new instance.

```csharp
public TabBar(Tizen.UI.Components.Material.TabBarVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.TabBar_T_.TabBar(Tizen.UI.Components.Material.TabBarVariables).variables'></a>

`variables` [TabBarVariables](Tizen.UI.Components.Material.TabBarVariables.md 'Tizen.UI.Components.Material.TabBarVariables')

The variables to configure the tab bar.
### Properties

<a name='Tizen.UI.Components.Material.TabBar_T_.ItemAlignment'></a>

## TabBar&lt;T>.ItemAlignment Property

Gets or sets the alignment of the tab items.

```csharp
public Tizen.UI.Layouts.LayoutAlignment ItemAlignment { get; set; }
```

#### Property Value
Tizen.UI.Layouts.LayoutAlignment  
The alignment of the tab items.














































