# Tab Elements
Tab elements provide easy possibility to explore and switch between different views or functional aspects of an application or to browse categorized data sets.

You can handle a Tab by adding TabBar, TabButton, TabContent, and TabView. A Tab can contain one or more TabViews with View.


![Tab](./media/tab.png) ![Tab](./media/tab2.png)

## Add namespace
To implement any Tab element, include `Tizen.NUI.Components` namespace in your application:

```csharp
using Tizen.NUI;
using Tizen.NUI.Components;
```

```xaml
xmlns:base="clr-namespace:Tizen.NUI.BaseComponents;assembly=Tizen.NUI"
xmlns:comp="clr-namespace:Tizen.NUI.Components;assembly=Tizen.NUI.Components"
```

# TabView

TabView is a class which contains a TabBar and TabContent.
TabView adds TabButtons and Views to TabBar and TabContent in TabView.
TabView can also remove TabButtons and Views from TabBar and TabContent in TabView.
TabView selects a view from the TabContent according to the selected TabButton in the TabBar.

To create a base TabView, follow these steps:

1.  Create TabView with size matching parent element in XAML:

```xaml
<comp:TabView x:Name="tabView" WidthSpecification="-1" HeightSpecification="-1"/>
```

2.  Add Tab to TabView:

```csharp
tabView.AddTab(tab_btn1, contentView1);
tabView.AddTab(tab_btn2, contentView2);
tabView.AddTab(tab_btn3, contentView3);
```

## TabButton

TabButton is a class which is used for selecting a content in the TabView.

Create a TabButton using the following code:

   ```csharp
   TabButton tab_btn = TabButton() 
      { 
         Text = "Tab ",
      };
   ```

## TabContent

TabContent is a class which contains a set of Views and has one of them selected.

Create View with properties using the following code:

   ```csharp
   var contentView1 = new View()
   {
       Layout = new LinearLayout()
       {
           LinearOrientation = LinearLayout.Orientation.Vertical,
           LinearAlignment = LinearLayout.Alignment.Center,
           CellPadding = new Size2D(0, 20),
       },
       BackgroundColor = backgroundColor,
       WidthSpecification = LayoutParamPolicies.MatchParent,
       HeightSpecification = LayoutParamPolicies.MatchParent,
   };

   var buttonAddTab = new Button()
   {
       Text = "Add Tab",
       BackgroundColor = buttonBackgroundColor,
   };
   contentView1.Add(buttonAddTab);

   var buttonRemoveTab = new Button()
   {
       Text = "Remove Tab",
       BackgroundColor = buttonBackgroundColor,
   };
   contentView1.Add(buttonRemoveTab);

   ```

## Respond to TabButton selected event
When you click TabButton, it receives the selected event.
You can declare the selected event handler as follows:

```xaml
<comp:TabView x:Name="tab" TabButtonSelected="tabButtonSelectedHandler"/>;
```

```csharp
private void tabButtonSelectedHandler(object sender, TabButtonSelectedEventArgs args)
{
    //Create Tab just by properties
}
```

## Related information
- Dependencies
  -   Tizen 6.5 and Higher


