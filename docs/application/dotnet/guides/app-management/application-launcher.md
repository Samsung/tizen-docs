# Application launcher

This guide explains how to create a basic application launcher. The application launcher is a main application that normally starts after system boot. This app is commonly replaced in the platform adjustments process. It is easy to use the .NET APIs in the application launcher implementation.

Every application launcher must be able to:
 - List installed and runnable applications.
 - Run selected application by the user.

You can also implement advanced functionalities such as:
 - grouping installed applications into folders,
 <!-- TBD: when widgets viewer will be pushed unlock this line - [widgets viewer](./widgets_viewer.md), -->
 - removing applications,
 - rearrangement of icons,
 - viewing notifications,

## Prerequisites

To list the installed applications and launch them, the launcher app must have defined privileges in the project manifest file as:

**Snippet: Application launcher priviledges**
```xml
<?xml version="1.0" encoding="utf-8"?>
  <ui-application appid="NUIApplicationLauncher">
    <!-- Auto generated manifest properties -->
  </ui-application>
  <privileges>
    <privilege>http://tizen.org/privilege/packagemanager.info</privilege>
    <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
  </privileges>
```

## Managing app launcher

Following code snippet illustrates how to implement the simple application launcher using:
 - [NUI](/application/dotnet/api/TizenFX/latest/api/Tizen.NUI.html) for the view implementation.
 - [Package MAnager](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.PackageManager.html) to gather installed applications,
- [TizenFX AppControl](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.AppControl.html) to launch an app on touch event

**Figure: NUI application launcher**

![Application launcher](./media/application_launcher_animation.gif)

To use mentioned API's following namespaces have to be included:

```csharp
using System;
using System.Collections.Generic;

using Tizen.Applications;

using Tizen.NUI;
using Tizen.NUI.BaseComponents;
```

To group application launcher responsibilities three classes in the `NUIApplicationLauncher` namespace are defined which represents main application structure:

```csharp
namespace NUIApplicationLauncher
{
    //Each touch event needs additional data like application ID to launch application
    partial class ApplicationIconClickedEventArgs : EventArgs
    {
        //...
    }

    //Application Icon component with ImageView and Label. Also OnTouch Event is handler here.
    class ApplicationIcon : View
    {
        //...
    }

    //Main Application Code
    class Program : NUIApplication
    {
        //...
    }
}
```

Create the event arguments derived class to add an application id field. The application id is used by `AppControl` to launch the application:

```csharp
partial class ApplicationIconClickedEventArgs : EventArgs
    {
        public string AppId = "";

        public ApplicationIconClickedEventArgs(string id)
        {
            AppId = id;
        }
    }
```

The `ApplicationIcon` class stores  the application id. The `Icon` component and `OriginSize` are used to resize `Icon` when it is in the pressed state. The `ApplicationIconClicked` is invoked when touch changes its state to finished:

```csharp
    class ApplicationIcon : View
    {
        private string AppId;

        private ImageView Icon;
        private Size2D OriginSize;

        public event EventHandler<ApplicationIconClickedEventArgs> ApplicationIconClicked;

        //...
    }
```

The `ApplicationIcon` constructor is responsible for:
  - Set `AppId` and `OriginSize`
  - Create view components: `Label` which is used to show an application name and `Icon` which load resource from `path` string and show loaded image.
  - Create `Layout` of the `ApplicationIcon`. In this case the vertical linear layout is used.
  - Setup the `TouchEvent` handler:

```csharp
        public ApplicationIcon(string name, string path, Size2D size, string id)
        {
            this.AppId = id;
            OriginSize = new Size2D(size.Width - 40, size.Height - 40);

            this.Size2D = size;

            TextLabel label = new TextLabel()
            {
                PointSize = 6,
                Text = name,
                MultiLine = true,
                Size2D = new Size2D(size.Width, 40),
                HorizontalAlignment = HorizontalAlignment.Center,
                VerticalAlignment = VerticalAlignment.Center,
            };

            Icon = new ImageView()
            {
                Size2D = new Size2D(size.Height - 40, size.Height - 40),
                ResourceUrl = path,
            };

            this.Layout = new LinearLayout()
            {
                LinearAlignment = LinearLayout.Alignment.CenterHorizontal,
                LinearOrientation = LinearLayout.Orientation.Vertical
            };

            this.Add(Icon);
            this.Add(label);

            this.TouchEvent += OnTouchEvent;
        }
```

**Figure: Application Icons**

![Application Icons](./media/application_launcher_icons.png)

`OnTouchEvent` reads state from the `TouchEventArgs`. If touch is in `PointStateType.Down` state the application icon is resized. Otherwise, it returns to normal size and predefined event is invoked with the proper `AppId`:

```csharp
        public bool OnTouchEvent(object sender, TouchEventArgs args)
        {
            var state = args.Touch.GetState(0);

            switch (state)
            {
                case PointStateType.Down:
                    Icon.Size2D = new Size2D((int)(OriginSize.Width * 1.1f), (int)(OriginSize.Height * 1.1f));
                    break;
                case PointStateType.Finished:
                    Icon.Size2D = OriginSize;
                    ApplicationIconClicked.Invoke(this, new ApplicationIconClickedEventArgs(this.AppId));
                    break;
                default:
                    break;
            }

            return false;
        }
    }
```

The `Program` class derived from NUIApplication to handle all necessary system events ([Application Lifecycle](./01_application_lifecycle.md)). The `AppLauncher` is created in `Initialize()` method and used in an icon touch handler:


```csharp
class Program : NUIApplication
    {
        private AppControl AppLauncher;

        //...
    }

```

The `OnCreate()` method implementation. It is responsible for call `Initialize()` method before main application loop starts:

```csharp
        protected override void OnCreate()
        {
            base.OnCreate();
            Initialize();
        }
```

The `Initialize()` method setup key listener, `AppControl` object and the application background:

```csharp
        void Initialize()
        {
            var appWindow = Window.Instance;
            appWindow.KeyEvent += OnKeyEvent;

            AppLauncher = new AppControl();
            ImageView background = new ImageView(DirectoryInfo.Resource + "/images/bg.png");

            //Setting the background parameters so that it occupies the entire application window
            background.Size2D = new Size2D(appWindow.Size.Width, appWindow.Size.Height);
            background.Position2D = new Position2D(0, 0);
            appWindow.GetDefaultLayer().Add(background);
        }
```

In next step grid component for application icons is created. Grid spacing and columns number is defined in the [GridLayout](/application/dotnet/guides/nui/grid-layout.md) object. The `appGrid` component width and height is set to fill its parent:

```csharp
            View appGrid = new View()
            {
                WidthResizePolicy = ResizePolicyType.FillToParent,
                HeightResizePolicy = ResizePolicyType.FillToParent,
                Layout = new GridLayout()
                {
                    Columns = 8,
                    GridOrientation = GridLayout.Orientation.Horizontal,
                    RowSpacing = 35f,
                    ColumnSpacing = 12f,
                    Padding = new Extents(30, 30, 30, 30)
                }
            };
```
The [PackageManager.GetPackages()](/package-manager.md) is used to obtain all installed packages. Each package may contains several applications. Because of that `pkg.GetApplications()` is used. `ApplicationInfo` object is used to filter apps which should be displayed. In this case `NUIApplicationLauncher`, app with no icon or app with `IsNoDisplay` parameter will not be inserted into `appGrid`:

```csharp
            IEnumerable<Package> packageList = PackageManager.GetPackages();

            foreach (var pkg in packageList)
            {
                var list = pkg.GetApplications();

                foreach (var app in list)
                {
                    if (!app.IsNoDisplay && app.IconPath != null && app.Label != "NUIApplicationLauncher") {
                        var icon = new ApplicationIcon(app.Label, app.IconPath, new Size2D((), 139), app.ApplicationId);
                        icon.ApplicationIconClicked += OnAppIconClicked;
                        appGrid.Add(icon);
                    }
                }
            }
```
Last step is to insert `appGrid` object in the application window:

```csharp
    appWindow.GetDefaultLayer().Add(appGrid);
```

Clicked event setups `AppLauncher` and pass it to [AppControl](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.AppControl.html) `SendLaunchRequest()` API. Now
selected applications starts:

```csharp
        public void OnAppIconClicked(object sender, ApplicationIconClickedEventArgs args)
        {
            AppLauncher.ApplicationId = args.AppId;
            AppLauncher.Operation = AppControlOperations.Default;
            AppControl.SendLaunchRequest(AppLauncher);
        }
```

Common method to handle `back` button pressed event. In this case application exits, but normally the launcher app should don't call `Exit()` API:

```csharp
        public void OnKeyEvent(object sender, Window.KeyEventArgs args)
        {
            Tizen.Log.Info(LogTag, args.Key.ToString());

            if (args.Key.State == Key.StateType.Down && (args.Key.KeyPressedName == "XF86Back" || args.Key.KeyPressedName == "Escape"))
            {
                Exit();
            }
        }
```

The main code of the application:

```csharp
        static void Main(string[] args)
        {
            var app = new Program();
            app.Run(args);
        }
    }
```

Full source code of example above is available [here](./source-code/application-launcher.cs)

## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
