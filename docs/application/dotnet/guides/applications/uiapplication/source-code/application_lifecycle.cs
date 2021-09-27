namespace lifecycle
{
    class Program : NUIApplication
    {
        private Accelerometer SensorAccelerometer = null;

        protected override void OnCreate()
        {
            Tizen.Log.Info("LifecycleTest", "OnCreate()");
            base.OnCreate();
            InitSensors();
            InitUI();
        }
        
        void InitSensors()
        {
            SensorAccelerometer = new Accelerometer();
            SensorAccelerometer.Interval = 1000;
            SensorAccelerometer.DataUpdated += OnAccelerometer;
            SensorAccelerometer.Start();
        }

        void InitUI()
        {
            Window.Instance.KeyEvent += OnKeyEvent;

            TextLabel test = new TextLabel("Lifecycle test...")
            {
                HorizontalAlignment = HorizontalAlignment.Center,
                VerticalAlignment = VerticalAlignment.Center,
                TextColor = Color.Blue,
                PointSize = 12.0f,
                HeightResizePolicy = ResizePolicyType.FillToParent,
                WidthResizePolicy = ResizePolicyType.FillToParent
            };

            Window.Instance.GetDefaultLayer().Add(test);
        }
        
        protected override void OnTerminate()
        {
            Tizen.Log.Info("LifecycleTest", "OnTerminate()");
            base.OnTerminate();
        }
        
        protected override void OnPause()
        {
            Tizen.Log.Info("LifecycleTest", "OnPause()");
            base.OnPause();

            if (SensorAccelerometer != null) SensorAccelerometer.Stop();
        }
        
        protected override void OnResume()
        {
            Tizen.Log.Info("LifecycleTest", "OnResume()");
            base.OnResume();

            if (SensorAccelerometer != null) SensorAccelerometer.Start();
        }

        void OnAccelerometer(object sender, AccelerometerDataUpdatedEventArgs args)
        {
            Tizen.Log.Info("LifecycleTest", string.Format("X: {0}, Y: {1}, Z: {2}", args.X, args.Y, args.Z));
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