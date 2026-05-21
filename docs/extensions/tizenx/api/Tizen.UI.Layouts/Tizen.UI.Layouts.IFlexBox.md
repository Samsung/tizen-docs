### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## IFlexBox Interface

Defines the contract for a FlexBox layout, extending ILayout with FlexBox-specific layout operations.

```csharp
public interface IFlexBox :
Tizen.UI.Layouts.ILayout
```

Derived  
&#8627; [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox')

Implements [ILayout](Tizen.UI.Layouts.ILayout.md 'Tizen.UI.Layouts.ILayout')
### Methods

<a name='Tizen.UI.Layouts.IFlexBox.Layout(float,float)'></a>

## IFlexBox.Layout(float, float) Method

Performs the layout calculation for the FlexBox and its children.  
This method is used by the FlexLayoutManager to arrange and measure the FlexBox.

```csharp
void Layout(float width, float height);
```
#### Parameters

<a name='Tizen.UI.Layouts.IFlexBox.Layout(float,float).width'></a>

`width` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available width for the layout.

<a name='Tizen.UI.Layouts.IFlexBox.Layout(float,float).height'></a>

`height` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available height for the layout.






























































