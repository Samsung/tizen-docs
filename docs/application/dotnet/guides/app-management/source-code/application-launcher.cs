using System;
using System.Collections.Generic;

using Tizen.Applications;

using Tizen.NUI;
using Tizen.NUI.BaseComponents;

namespace NUIApplicationLauncher
{
    partial class ApplicationIconClickedEventArgs : EventArgs
    {
        public string AppId = "";

        public ApplicationIconClickedEventArgs(string id)
        {
            AppId = id;
        }
    }

    class ApplicationIcon : View
    {
        public event EventHandler<ApplicationIconClickedEventArgs> ApplicationIconClicked;
        private string AppId;
        private ImageView Icon;
        private Size2D normalSize;

        public ApplicationIcon(string name, string path, Size2D size, string id)
        {
            this.AppId = id;
            normalSize = new Size2D(size.Width - 40, size.Height - 40);

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
                HorizontalAlignment = HorizontalAlignment.Center,
                LinearOrientation = LinearLayout.Orientation.Vertical
            };

            this.Add(Icon);
            this.Add(label);

            this.TouchEvent += OnTouchEvent;
        }

        public bool OnTouchEvent(object sender, TouchEventArgs args)
        {
            var state = args.Touch.GetState(0);

            switch (state)
            {
                case PointStateType.Down:
                    Icon.Size2D = new Size2D((int)(normalSize.Width * 1.1f), (int)(normalSize.Height * 1.1f));
                    break;
                case PointStateType.Finished:
                    Icon.Size2D = normalSize;
                    ApplicationIconClicked.Invoke(this, new ApplicationIconClickedEventArgs(this.AppId));
                    break;
                default:
                    break;
            }

            return false;
        }
    }

    class Program : NUIApplication
    {
        private AppControl AppLauncher;

        private readonly int GridColumns = 8;
        private readonly ushort Padding = 30;

        protected override void OnCreate()
        {
            base.OnCreate();
            Initialize();
        }

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

            View appGrid = new View()
            {
                WidthResizePolicy = ResizePolicyType.FillToParent,
                HeightResizePolicy = ResizePolicyType.FillToParent,
                Layout = new GridLayout()
                {
                    Columns = GridColumns,
                    GridOrientation = GridLayout.Orientation.Horizontal,
                    RowSpacing = 35f,
                    ColumnSpacing = 12f,
                    Padding = new Extents(Padding, Padding, Padding, Padding)
                }
            };

            IEnumerable<Package> packageList = PackageManager.GetPackages();

            foreach (var pkg in packageList)
            {
                var list = pkg.GetApplications();

                foreach (var app in list)
                {
                    if (!app.IsNoDisplay && app.IconPath != null && app.Label != "NUIApplicationLauncher") {
                        var icon = new ApplicationIcon(app.Label, app.IconPath, new Size2D(142, 139), app.ApplicationId);
                        icon.ApplicationIconClicked += OnAppIconClicked;
                        appGrid.Add(icon);
                    }
                }
            }

            appWindow.GetDefaultLayer().Add(appGrid);
        }

        public void OnAppIconClicked(object sender, ApplicationIconClickedEventArgs args)
        {
            AppLauncher.ApplicationId = args.AppId;
            AppLauncher.Operation = AppControlOperations.Default;
            AppControl.SendLaunchRequest(AppLauncher);
        }

        public void OnKeyEvent(object sender, Window.KeyEventArgs args)
        {
            if (args.Key.State == Key.StateType.Down && (args.Key.KeyPressedName == "XF86Back" || args.Key.KeyPressedName == "Escape"))
            {
                Exit();
            }
        }

        static void Main(string[] args)
        {
            var app = new Program();
            app.Run(args);
        }
    }
}
