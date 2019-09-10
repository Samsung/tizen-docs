# XAML Support for Tizen.NUI
eXtensible Application Markup Language (XAML) allows you to define user interfaces in the Tizen.NUI applications using markup language rather than code. XAML is never required in a Tizen.NUI program, but it is often more succinct and more visually coherent than equivalent code, and potentially toolable. XAML is particularly well suited for using with the popular MVVM (Model-View-ViewModel) application architecture: XAML defines the View that is linked to ViewModel code through XAML-based data bindings.

For more information, see https://docs.microsoft.com/en-us/xamarin/xamarin-forms/xaml/xaml-basics/

XAML is mostly used to define the visual contents of a page and works together with a C# code-behind file. The code-behind file provides adding code logics for the markup.

For more information, see https://docs.microsoft.com/en-us/xamarin/xamarin-forms/xaml/xaml-basics/get-started-with-xaml?tabs=windows

## Creating Solution
To begin editing your first XAML file, use Visual Studio to create a new Tizen.NUI solution.

For more information, see https://docs.microsoft.com/en-us/xamarin/xamarin-forms/xaml/xaml-basics/get-started-with-xaml?tabs=windows

Use Visual Studio to select **File** > **New** > **Project** from the menu. In the **New Project** dialog, select **Tizen** > **Native** at the left, and then **Blank App (Tizen.NUI)** from the list.

![CreateNUIProject](./Pictures/CreateNUIProject.PNG)

Select a location for the solution, give it a name of **XamlSamples** (or whatever you prefer), and press **OK**.

## Creating XAML file
After creating the **XamlSamples** solution, create a XAML file. In the following sample, it is XamlSamplesPage.xaml. Put the XAML file in the **/res/layout/1920x1080/** folder:

![XAMLFilePath](./Pictures/XAMLFilePath.PNG)

If your app runs on a target having different window sizes, such as 720x1080, 480x800, or both then put the XAML file into the corresponding folder. You can also create these folders like **/res/layout/720x1080/** or **/res/layout/480x800/**.
To add any control you want, edit the XamlSamplesPage.xaml file.

![XAMLFile](./Pictures/XAMLFile.PNG)

In this sample, a simple `TextLabel` is added, and the `Text`, `Position2D`, and `Size2D` properties are set.

## Creating C# Code-Behind File
There is a C# code-behind file associated with the XAML file. In this sample XAML file, the `x:Class` attribute specifies a fully qualified class name, the `XamlSamplesPage` class in the `XamlSamples` namespace. This means that this XAML file of **XamlSamplesPage.xaml.cs** defines a new class named `XamlSamplesPage` in the `XamlSamples` namespace that is derived from `ContentPage`.
For this sample, we define that `XamlSamplesPage` class in **XamlSamplesPage.xaml.cs** file.

![XAMLCodeBehindFilePath](./Pictures/XAMLCodeBehindFilePath.PNG)

Both **XamlSamplesPage.xaml** and **XamlSamplesPage.xaml.cs** contribute to class named `XamlSamplesPage` that is derived from `ContentPage`.

``` csharp
using System;
using Tizen.NUI;

namespace XamlSamples
{
    public class XamlSamplesPage : ContentPage
    {
        public XamlSamplesPage (Window win) : base(win)
        {
            InitializeComponent();
        }

        protected override void Dispose(DisposeTypes type)
        {
            if (disposed)
            {
                return;
            }

            base.Dispose(type);
        }

        public override void SetFocus()
        {
            base.SetFocus();
        }
    }
}
```

> **Note**
> The name of the XAML file should be same as the class name.

## Load XAML
After creating the XAML and the C# code-behind files, you can load and show the visual contents that you defined in the XAML file:

``` csharp
using System;
using Tizen.NUI;
using Tizen.NUI.Xaml;

namespace XamlSamples
{
    class Program : NUIApplication
    {
        private Window window;
        private ContentPage myPage;

        protected override void OnCreate()
        {
            base.OnCreate();
            Initialize();
        }

        void Initialize()
        {
            window = Window.Instance;
            myPage = new XamlSamplesPage(window);
            myPage.SetFocus();
        }

        static void Main(string[] args)
        {
            var app = new Program();
            app.Run(args);
        }
    }
}
```

When you compile and run this program, the `TextLabel` element will appear on the window.
