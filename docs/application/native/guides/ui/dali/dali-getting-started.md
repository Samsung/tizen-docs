# Getting Started


This page describes how to start DALi UI programming.

## Creating a DALi Application

To create a 'Hello World' application with Dali:

1. Create a DALi project:

   1. In the Tizen Studio menu, go to **File > New > Tizen Project**.
   2. In the Project Wizard, select **Template > Mobile or Wearable > Native Application > Basic UI with DALi**.
   3. Click **Finish**, and your project is created at the default location. If you want to change the location, uncheck **Use default location** and set a new location. For more information, see [Creating the Application Project](../../../tutorials/process/app-dev-process.md#creating).![Create a DALi project](./media/tizen_project_dali.png)
   4. The new project is shown in the **Project Explorer** view of the Tizen Studio. If you open the `src/basicuiwithdali.cpp` file, you can see the source code of the basic DALi application:

    ```
    #include <dali-toolkit/dali-toolkit.h>

    using namespace Dali;
    using namespace Dali::Toolkit;

    // This example shows how to create and display Hello World
    // using a simple TextLabel

    class HelloWorldExample : public ConnectionTracker
    {
      public:
        HelloWorldExample( Application& application )
          : mApplication( application )
        {
          // Connect to the application's init signal
          mApplication.InitSignal().Connect( this, &HelloWorldExample::Create );
        }

        ~HelloWorldExample()
        {
          // Nothing to do here
        }

        // Init signal is received once (only) during the application lifetime
        void Create( Application& application )
        {
          // Get a handle to the stage
          Stage stage = Stage::GetCurrent();
          stage.SetBackgroundColor( Color::WHITE );

          TextLabel textLabel = TextLabel::New( "Hello World" );
          textLabel.SetSize( stage.GetSize() );
          textLabel.SetAnchorPoint( AnchorPoint::TOP_LEFT );
          textLabel.SetProperty( TextLabel::Property::HORIZONTAL_ALIGNMENT, "CENTER" );
          textLabel.SetProperty( TextLabel::Property::VERTICAL_ALIGNMENT, "CENTER" );
          stage.Add( textLabel );

          // Connect to touch and key event signals
          stage.GetRootLayer().TouchSignal().Connect( this, &HelloWorldExample::OnTouch );
          stage.KeyEventSignal().Connect( this, &HelloWorldExample::OnKeyEvent );
        }

        bool OnTouch( Actor actor, const TouchData& touch )
        {
          // Quit the application
          mApplication.Quit();

          return true;
        }

        void OnKeyEvent( const KeyEvent& event )
        {
          if( event.state == KeyEvent::Down )
          {
            if( IsKey( event, DALI_KEY_ESCAPE ) || IsKey( event, DALI_KEY_BACK ) )
            {
              mApplication.Quit();
            }
          }
        }

      private:
        Application& mApplication;
    };

    // Entry point for DALi applications
    int main( int argc, char **argv )
    {
      Application application = Application::New( &argc, &argv );
      HelloWorldExample test( application );
      application.MainLoop();

      return 0;
    }
    ```

2. Initialize the DALi application:

   - To use the DALi APIs, you only need to include the `dali-toolkit.h` file. It includes the header files of DALi Core and DALi Adaptor as well as DALi Toolkit.

     ```
     #include <dali-toolkit/dali-toolkit.h>
     ```

     Using the following 2 using-directives can be convenient, because all DALi APIs are contained in either the `Dali` or `Dali::Toolkit` namespace:

     ```
     using namespace Dali;
     using namespace Dali::Toolkit;
     ```

     Other code samples in the Tizen DALi documentation assume they already have those directives.

   - The `Dali::Application` class (in [mobile](../../../api/mobile/latest/classDali_1_1Application.html) and [wearable](../../../api/wearable/latest/classDali_1_1Application.html) applications) initializes and sets up DALi.

     Create a `Dali::Application` instance:

     ```
     Application application = Application::New( &argc, &argv );
     ```

   - Several signals can be connected to keep you informed when certain platform-related activities occur, and ensure that, upon system events, DALi is called in a thread-safe manner.

     To manage signal connection safely, DALi provides the `Dali::ConnectionTracker` class (in [mobile](../../../api/mobile/latest/classDali_1_1ConnectionTracker.html) and [wearable](../../../api/wearable/latest/classDali_1_1ConnectionTracker.html) applications). A typical way for starting a DALi application is to create a class derived from the `Dali::ConnectionTracker` class and use its member functions as callback functions for DALi signals (for more information, see [Automatic Connection Management](event-handling.md#automatic)). The `HelloWorldExample` class is used in other code samples in the Tizen DALi documentation.

     After getting the initialized signal from the `Dali::Application` instance, you can use the DALi APIs for building the scene graph. Connect the `HelloWorldExample::Create()` callback to the `DALi::Application::InitSignal()` function:

     ```
     mApplication.InitSignal().Connect( this, &HelloWorldExample::Create );
     ```

3. Create an actor and add it to the stage:

   The `Dali::Toolkit::TextLabel` UI component (in [mobile](../../../api/mobile/latest/classDali_1_1Toolkit_1_1TextLabel.html) and [wearable](../../../api/wearable/latest/classDali_1_1Toolkit_1_1TextLabel.html) applications) renders a short text string. To display the `TextLabel` component, add it to a stage. The `stage` instance is a singleton object (the only instance of its class during the lifetime of the program), so you can get it using a static function.

   ```
   Stage stage = Stage::GetCurrent();
   stage.SetBackgroundColor( Color::WHITE );

   TextLabel textLabel = TextLabel::New( "Hello World" );
   textLabel.SetSize( stage.GetSize() );
   textLabel.SetAnchorPoint( AnchorPoint::TOP_LEFT );
   textLabel.SetProperty( TextLabel::Property::HORIZONTAL_ALIGNMENT, "CENTER" );
   textLabel.SetProperty( TextLabel::Property::VERTICAL_ALIGNMENT, "CENTER" );
   stage.Add( textLabel );
   ```

   The above code additionally sets the background color of the `stage` and the anchor point, a point defining a position of a child actor from its parent, of the `textLabel`. The application stores the actor and resource handles. DALi objects are reference-counted, which makes sure they exist only as long as they are needed. Even if the `TextLabel` component is removed from the stage, it remains alive through the reference.

4. Connect to input signals:

   The application can handle touch and key event signals as follows:

   ```
   stage.GetRootLayer().TouchSignal().Connect( this, &HelloWorldExample::OnTouch );
   stage.KeyEventSignal().Connect( this, &HelloWorldExample::OnKeyEvent );
   ```

   Any key inputs and touches on the stage are handled by 2 callback functions, `HelloWorldExample::OnKeyEvent` and `HelloWorldExample::OnTouch`.

   Note that the first parameter of the `HelloWorldExample::OnTouch` callback (`actor`) is passed by a value, not by a reference or a pointer. You can simply pass instances of most DALi classes by value, when the class inherits from the `Dali::BaseHandle` class (in [mobile](../../../api/mobile/latest/classDali_1_1BaseHandle.html) and [wearable](../../../api/wearable/latest/classDali_1_1BaseHandle.html) applications). This is due to the [handle/body pattern](handle.md) widely used in DALi.

   ```
   bool OnTouch( Actor actor, const TouchData& touch )
   ```

5. Start the application main loop:

   To run the application, start its main loop. This ensures that images are displayed, and events as well as signals are dispatched and captured.

   ```
   application.MainLoop();
   ```

6. Build the DALi application:

   To build your application, select **Project > Build Project** or press **F10** in the Tizen Studio.

   The Tizen Studio automatically packages the project after building. Note that you need to register your certificate when building for the first time. For more information, see [Working with the Certificate Profile](../../../../tizen-studio/common-tools/certificate-registration.md) and [Building Applications](../../../tutorials/process/building-app.md).

7. Run the DALi application:

   To run your application, select **Run > Run** or press **Ctrl + F11** in the Tizen Studio.

   For more information, see [Running Applications](../../../tutorials/process/running-app.md).

The following figure illustrates the basic DALi application running on a Tizen emulator.

**Figure: Basic DALi application**

![Basic DALi application](./media/hello_world_dali.png)

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
