# NUI Hello World Tutorial

The tutorial shows how to create and display "Hello World" using a text label.

For an introduction to NUI, see the [NUI Overview](NUIoverview.md).

<a name="tutorial"></a>
## Tutorial Details 

The following steps are required to display text:

1.  Initialize the NUI library.
2.  Create a view with a text label.
3.  Add the text label to the application main window.

This tutorial also demonstrates the triggering of the `Touch` window application event.

### Namespaces

The required system and NUI namespaces are imported through the following `using` declarations:

``` 
using System;
using System.Runtime.InteropServices;
using Tizen.NUI;
using Tizen.NUI.UIComponents;
using Tizen.NUI.BaseComponents;
using Tizen.NUI.Constants;
```

This application is scoped to the `HelloTest` namespace.

### Main Method

The `Main()` method consists of 2 steps:

1.  Create the application through the default constructor:

    ``` 
    Example example = new Example();
    ```

    The application is derived from the `NUIApplication` class:

    ``` 
    class Example : NUIApplication
    ```

    The `NUIApplication` class also includes constructors enabling application creation with stylesheets and window modes.

2.  Start the application main loop.

    The main loop must be started to run the application. This ensures that images are displayed, and that events and signals are dispatched and captured.

    ``` 
    example.Run(args);
    ```

    In this simple tutorial, the `Main()` method resides within the class. For significant application development, the `Main()` method must be placed in a separate `.cs` file.

### Creation Method - OnCreate()

The `OnCreate` method of the Hello World application overrides the NUIApplication `OnCreate` method:

``` 
protected override void OnCreate()
{
    base.OnCreate();
    Initialize();
}
```

Hence you can incorporate the required initialization behavior in your application.

> **Note**   
> Calling `base.OnCreate()` is necessary, to invoke the `Created` event.

### Initialization Method - Initialize()

The initialization code contains the following simple steps:

1.  Create the text label member variable:

    ``` 
    _text = new TextLabel("Hello World");
    ```

2.  Position the text in the centre of the application window. The `ParentOrigin` property defines a point within the parent view area. If the text label size is not specified, the text label is at least as wide as the screen.

    ``` 
    _text.ParentOrigin = ParentOrigin.CenterLeft;
    ```

3.  Align the text horizontally to the center of the available area:

    ``` 
    _text.HorizontalAlignment = HorizontalAlignment.Center;
    ```

4.  Set the label background color to illustrate the label width:

    ``` 
    _text.BackgroundColor = Color.Red;
    ```

5.  Set the text size (the size of the font is given in points):

    ``` 
    _text.PointSize = 32.0f;
    ```

    For more information on key properties of the `TextLabel` class, see [TextLabel](textlabel.md).

6.  Add the `TouchEvent` event handler to the main application window. This event handler is invoked on any click in the application window.

    ``` 
    Window window = Window.Instance;
    window.TouchEvent += WindowTouched;
    ```

    Alternatively, you can add the event handler using the lambda expression syntax:

    ``` 
    window.TouchEvent += (object src, Window.TouchEventArgs args) =>
    {
        _text.Text = "I have been touched!";
    };
    ```

7.  Add the text label to the root layer:

    ``` 
    window.Add(_text);
    ```

    The window adds the view to the root layer.

### TouchEvent event handler

The user can click anywhere in the application window to change the text in the label:

``` 
private void WindowTouched(object sender, Window.TouchEventArgs e)
{
    _text.Text = "I have been touched!";
}
```

### Closing the Application - OnTerminate()

`OnTerminate` is invoked when the application is about to terminate and when the window close button is clicked.

``` 
protected override void OnTerminate()
{
    base.OnTerminate();
    _text = null;
}
```

> **Note**   
> Calling `base.OnTerminate()` is necessary to invoke the `Deleted` event.

### Building and Running the Application

To build and run the application, use Visual Studio on a Windows platform, and Visual Studio Code on Linux.

The [NUI development setup guide](setup-ubuntu.md) describes setting up the NUI development environment on Ubuntu, using this tutorial as an example project.

<a name="fullcode"></a>
## Full Example Source Code 

``` 
using System;
using System.Runtime.InteropServices;
using Tizen.NUI;
using Tizen.NUI.UIComponents;
using Tizen.NUI.BaseComponents;
using Tizen.NUI.Constants;

namespace HelloTest
{
    class Example : NUIApplication
    {
        TextLabel _text;

        protected override void OnCreate()
        {
            base.OnCreate();
            Initialize();
        }

        private void Initialize()
        {
            // Add a simple text label to the main window
            _text = new TextLabel("Hello World");
            _text.ParentOrigin = ParentOrigin.CenterLeft;
            _text.HorizontalAlignment = HorizontalAlignment.Center;
        _text.BackgroundColor = Color.Red;
            _text.PointSize = 32.0f;

            // Connect the signal callback for a touch signal
            Window window = Window.Instance;
            window.TouchEvent += WindowTouched;

            window.Add(_text);
        }

        // Callback for main window touched signal handling
        private void WindowTouched(object sender, Window.TouchEventArgs e)
        {
            _text.Text = "I have been touched!";
        }

        protected override void OnTerminate()
        {
            base.OnTerminate();
            _text = null;
        }

        static void Main(string[] args)
        {
            Example example = new Example();
            example.Run(args);
        }
    }
}
```

<a name="output"></a>
## Example Output

After running the example, the following output should appear:

![Hello world](media/hello-world.png)

