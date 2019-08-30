# Simple example of XAML for introduction

Using the XAML to layout, you need three steps: write the XAML file, write code to load your XAML file, and put your XAML file into appropriate file directory.

## Write XAML

![AmbientPage](./Pictures/AmbientPage.PNG)

Using XAML can implement the above layout easily, here is the corresponding XAML：

``` xml
<ContentPage x:Class="Tizen.NUI.Examples.AmbientPage"
  xmlns="http://tizen.org/Tizen.NUI/2018/XAML"
  xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml">

  <ImageView Name="photo1" ResourceUrl="../../res/images/ambient/default/picture_07.jpg" Position2D="47,52" Size2D="440,440" >
  <ImageView Name="photo2" ResourceUrl="../../res/images/ambient/default/picture_08.jpg" Position2D="47,512" Size2D="440,520" >

  <ImageView Name="photo3" ResourceUrl="../../res/images/ambient/default/picture_02.jpg" Position2D="970,50" Size2D="440,560" >
  <ImageView Name="photo4" ResourceUrl="../../res/images/ambient/default/picture_03.jpg" Position2D="970,630" Size2D="440,400" >
  <ImageView Name="photo5" ResourceUrl="../../res/images/ambient/default/picture_04.jpg" Position2D="510,50" Size2D="440,280" >
  <ImageView Name="photo6" ResourceUrl="../../res/images/ambient/default/picture_05.jpg" Position2D="510,350" Size2D="440,340" >
  <ImageView Name="photo7" ResourceUrl="../../res/images/ambient/default/picture_06.jpg" Position2D="510,710" Size2D="440,320" >

  <ImageView Name="photo0" ResourceUrl="../../res/images/ambient/bg_textbox_w.png" Position2D="1431,51" Size2D="440,600" >
  <View Name="num_area" Size2D="440,160" Position2D="1431,51">
    <ImageView Name="photo01" ResourceUrl="../../res/images/ambient/num/num_w_0.png" Position2D="0,0" Size2D="110,160" >
    <ImageView Name="photo02" ResourceUrl="../../res/images/ambient/num/num_w_8.png" Position2D="110,0" Size2D="110,160" >
    <ImageView Name="photo03" ResourceUrl="../../res/images/ambient/num/num_w_th.png" Position2D="220,0" Size2D="220,160" >
  </View>
  <View Name="mon_area" Size2D="440,194" Position2D="1431,211">
    <ImageView Name="photo10" ResourceUrl="../../res/images/ambient/mon/mon_w_4.png" Position2D="0,0" Size2D="440,194" />
  </View>
  <View Name="year_area" Size2D="440,210" Position2D="1431,425">
    <ImageView Name="photo21" ResourceUrl="../../res/images/ambient/year/year_w_2.png" Position2D="0,0" Size2D="110,210" />
    <ImageView Name="photo22" ResourceUrl="../../res/images/ambient/year/year_w_0.png" Position2D="110,0" Size2D="110,210" />
    <ImageView Name="photo23" ResourceUrl="../../res/images/ambient/year/year_w_1.png" Position2D="220,0" Size2D="110,210" />
    <ImageView Name="photo24" ResourceUrl="../../res/images/ambient/year/year_w_8.png" Position2D="330,0" Size2D="110,210" />
  </View>
  <ImageView Name="photo8" ResourceUrl="../../res/images/ambient/default/picture_01.jpg" Position2D="1431,671" Size2D="440,360" />
</ContentPage>
```

In the above example, we used the relative path for the image resources(relative to the location of the exe file), you can also use the absolute path on the target.

### Write code to load XAML

For the above example, you need to load the XAML file in your app code. First, you need define a class named the "AmbientPage" in "Tizen.NUI.Examples" namespace(this class name should match the x:class that you defined in the XAML file), like this:

``` csharp
namespace Tizen.NUI.Examples
{
    public class AmbientPage : ContentPage
    {
        public AmbientPage(Window win) : base (win)
        {
            InitializeComponent();
        }

        protected override void Dispose(DisposeTypes type)
        {
            if (disposed)
            {
                return;
            }
            if (type == DisposeTypes.Explicit)
            {
            }
            base.Dispose(type);
        }
    }
}
```

The <code> AmbientPage </code> should inherit form the <code>ContentPage</code>. And all the UI components that you defined in the above XAML file will be added to this contentPage, and then add to the <code>Window</code>. As you can see the root node of the XAML file is also a <code>ContentPage</code>, which is consistent with the code. All the pages in your application should inherit from the <code>ContentPage</code>.

Then you can load the xaml in the app like this:

``` csharp
namespace Tizen.NUI.Examples
{
    class AmbientPageDemo : NUIApplication
    {
        private Window window;
        private ContentPage myPage;
        protected override void OnCreate()
        {
            base.OnCreate();
            window = Window.Instance;
            myPage = new AmbientPage(window);
            myPage.SetFocus();
        }
    }
}
```

**Requirements**:

1. The <code> x:Class </code> specifies the namespace and class name for a class defined in XAML. The class name must match the class name of the code-behind file.

    ``` xml
    <ContentPage x:Class="Tizen.NUI.Examples.AmbientPage"
      xmlns="http://tizen.org/Tizen.NUI/2018/XAML"
      xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml">
      ...
      ...
    </ContentPage>
    ```
  
    ``` csharp
    namespace Tizen.NUI.Examples
    {
        public class AmbientPage : ContentPage
        {
            public AmbientPage(Window win) : base (win)
            {
                InitializeComponent();
            }
            ...
        }
    }
    ```

2. The filename of the XAML file should be same with the class name.

    See [Getting started with XAML](./FirstProject.md) for detail information.  

### Put XAML files

To support the multi window size， we recommend you to create different folder to keep the xaml for different device targets which have different window size.

For example, create the "res/layout/1920x1080/" folder and "res/layout/720X1280/" folder, when your application runs on "1920x1080" target, it will load the xaml files from "res/layout/1920x1080/" folder. When it runs on "720X1280" target, it will load the xaml files from "res/layout/720X1280/" folder.

If you donn't care about the different window size, please make "res/layout/" folder, and put all your xaml files in this folder.

See [Getting started with XAML](./FirstProject.md) for detail information.

### Benefit of XAML

1. Don’t need to compile and deploy if user want to update the UI.
2. UI and business are not coupling, user can update them individually.
3. User can set different layout-xaml files for different configurations(For example: resolution 1080 and 720), when the configuration changed, the display layout will change automatically.
