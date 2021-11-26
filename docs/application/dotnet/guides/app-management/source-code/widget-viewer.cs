using Tizen.NUI;
using Tizen.NUI.BaseComponents;

namespace NUIWidgetViewer
{
    class Program : NUIApplication
    {
        private readonly string LogTag = "NUIWidgetViewer";

        protected override void OnCreate()
        {
            base.OnCreate();
            Initialize();
        }

        void Initialize()
        {
            var appWindow = Window.Instance;
    
            ImageView background = new ImageView(DirectoryInfo.Resource + "/images/bg.png");
            appWindow.Add(background);

            //Setting the background parameters so that it occupies the entire application window
            background.Size2D = new Size2D(appWindow.Size.Width, appWindow.Size.Height);
            background.Position2D = new Position2D(0, 0);

            View widgetsList = new View()
            {
                WidthResizePolicy = ResizePolicyType.FillToParent,
                HeightResizePolicy = ResizePolicyType.FillToParent,
                Layout = new LinearLayout()
                {
                    LinearAlignment = LinearLayout.Alignment.CenterVertical,
                    LinearOrientation = LinearLayout.Orientation.Horizontal,
                    CellPadding = new Size2D(20, 20),
                    Padding = new Extents(30, 30, 30, 30)
                }
            };

            WidgetViewManager widgetViewManager = new WidgetViewManager(this, this.ApplicationInfo.ApplicationId);

            var galleryWidget = widgetViewManager.AddWidget("org.tizen.gallery.widget", "", 
                    Window.Instance.WindowSize.Width / 2 - 40, Window.Instance.WindowSize.Height, 0);
            var contactsWidget = widgetViewManager.AddWidget("org.tizen.contacts.widget", "", 
                    Window.Instance.WindowSize.Width / 2 - 40, Window.Instance.WindowSize.Height, 0);
            
            widgetsList.Add(galleryWidget);
            widgetsList.Add(contactsWidget);

            Window.Instance.GetDefaultLayer().Add(widgetsList);
        }

        public void OnKeyEvent(object sender, Window.KeyEventArgs e)
        {
            if (e.Key.State == Key.StateType.Down && (e.Key.KeyPressedName == "XF86Back" || e.Key.KeyPressedName == "Escape"))
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
