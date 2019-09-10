# How to Handle Object Created by XAML
In order to implement various functions in an Application, the instances of objects created in XAML must be referenced and handled in csharp code.

In the following XAML code, Tizen.NUI supports two ways to access the `ImageView` instance in the sample code:

``` xaml
<ContentPage x:Class="Tizen.NUI.Examples.xNameDemoPage"
  xmlns="http://tizen.org/Tizen.NUI/2018/XAML"
  xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml">

  <ImageView x:Name="ImageOne" Name="title" Position2D="0,0" Size2D="400,400" ResourceUrl="../res/xxx.png"/>

</ContentPage>
```

- View.FindChildByName
- NameScopeExtensions.FindByName&lt;T&gt;

``` csharp
ContentPage myPage = new xNameDemoPage(window);
Extensions.LoadFromXaml(myPage, typeof(xNameDemoPage));

ImageView title = myPage.Root.FindChildByName("title") as ImageView;

ImageView imageOne = NameScopeExtensions.FindByName<Tizen.NUI.BaseComponents.ImageView>(myPage, "ImageOne");
```

In `View.FindChildByName` method, set the `Name` property of the control as `Name="title"`. In the `NameScopeExtensions.FindByName<T>` method, set `x:Name` of the element as `x:Name="ImageOne"`.
To have a better performance, it is recommended to use the `NameScopeExtensions.FindByName<T>` method.

> **Note**  
> If you add the Tizen.NUI.XamlBuild nuget package into a project, and set the XAML file as `Embedded Resource`. It will be generated in the **.g.cs** file. In the `.g.cs file`, every node with `x:Name` in XAML has a variable that is generated with the same name as its `x:Name`. You can use it directly in your **.xaml.cs** file.