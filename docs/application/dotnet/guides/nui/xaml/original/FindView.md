# How to get the object created by XAML in code

``` xml
<ContentPage x:Class="Tizen.NUI.Examples.xNameDemoPage"
  xmlns="http://tizen.org/Tizen.NUI/2018/XAML"
  xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml">

  <ImageView x:Name="ImageOne" Name="title" Position2D="0,0" Size2D="400,400" ResourceUrl="../../res/images/AmbientScreenUXControl/Cut/traffic_content.png"  />

</ContentPage>
```

For the above XAML, Tizen.NUI support two ways to access the ImageView instance in sample or app code:

1. View.FindChildByName
2. NameScopeExtensions.FindByName&lt;T&gt;

``` csharp
ContentPage myPage = new xNameDemoPage(window);
Extensions.LoadFromXaml(myPage, typeof(xNameDemoPage));

ImageView title = myPage.Root.FindChildByName("title") as ImageView;

ImageView imageOne = NameScopeExtensions.FindByName<Tizen.NUI.BaseComponents.ImageView>(myPage, "ImageOne");
```

For the first method, you should set the <code> Name </code> property of the control, such as <code>Name="title"</code>. For the second method, you should set the <code>x:Name</code> of the element, such as <code>x:Name="ImageOne"</code>.

We recommend you use the second way, it has better performance.

**Attention:** If you add Tizen.NUI.XamlBuild nuget package into project, and set the xaml file is "Embedded Resource", it will be generate to .g.cs file. In the .g.cs file, every node with x:Name in XAML has a variable that is generated with the same name as its x:Name.
You can use it directly in your .xaml.cs file.
