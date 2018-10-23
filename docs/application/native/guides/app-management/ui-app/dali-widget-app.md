# DALi Widget Application


You can create a widget application with DALi to display small version of application on the home screen.

To create a DALi widget application, you must:

- Use the [Dali::WidgetApplication class](#widget-application-api).

	> **Note**
	> - The implementation of DALi widget application is similar to [DALi basic UI application](dali-basic-app.md), because the [Dali::WidgetApplication](../../../api/mobile/latest/classDali_1_1WidgetApplication.html) class inherits from the [Dali::Application](../../../api/mobile/latest/classDali_1_1Application.html) class.
  > - Ensure you are familiar with the basic UI application details before tackling a widget application.

- Ensure you start the event loop.

- To implement your own widget class inherit the `Dali::Widget` class.

![DALi widget application](./media/dali_widget_application.png)

**Figure: DALi widget application**

For more information on basics of creating a DALi widget application, see [The steps to create a DALi widget application](#create).

<a name="widget-application-api"></a>
## Widget Application Class

If you want to use DALi for your widget application, you must create the application with the `Dali::WidgetApplication` class. This class provides the means for initializing the resources required by DALi.

The table list the main functions to manage widget instance:

**Table: Main functions**

| Function                             | Description                              |
|--------------------------------------|------------------------------------------|
| `mainloop()`                         | The mainloop() function is used to start the event loop. If you do not call the function and start the event loop, DALi cannot call any callback functions for application events.  |
| `RegisterWidgetCreatingFunction()`   | This function is used to register create function to create widget instance. When widget viewer application requests, then the widget application creates widget instance using the function |

<a name="widget-api"></a>
## Widget Class

`Dali::Widget` class provides interface for creating custom widget.

The table list the main functions to manage widget instance:

**Table: Main functions**

| Function           | Description                                                                                   |
|--------------------|-----------------------------------------------------------------------------------------------|
| `OnCreate()`       | This function is called after the widget instance is created.                                 |
| `OnTerminate()`    | This function is called after the widget instance is terminated.                              |
| `OnPause()`        | This function is called when the widget is invisible.                                         |
| `OnResume()`       | This function is called when the widget is visible.                                           |
| `OnResize()`       | This function is called before the widget size is changed.                                    |
| `OnUpdate()`       | This function is called when an event for updating the widget is received.                    |
| `SetContentInfo()` | This function sends data about current state of widget instance to widget viewer application. |

Most of functions are used for managing widget instance lifecycle. You can describe what will be done on each lifecycle functions.

Widget instance can send data to widget viewer application using `SetContentInfo()` function. If you want to save the current state of widget before deleting it, view the current state of the widget and delete it.

<a name="create"></a>
## The steps to create a DALi widget application:

1. Initialize the widget application:

   To create the `Dali::WidgetApplication` class instance, initialize and set up DALi for a widget application:
   ```
   int DALI_EXPORT_API main( int argc, char **argv )
   {
     WidgetApplication application = WidgetApplication::New( &argc, &argv, "" );

     WidgetApplicationExample test( application );

     application.MainLoop();

     return 0;
   }
   ```

2. Connect signals to keep yourself informed when certain system events occur.

   To manage signal connection safely, DALi provides the `Dali::ConnectionTracker` class. A typical way to start a DALi application is to create a class derived from the `Dali::ConnectionTracker` class and use its member functions as callback functions for DALi signals. When the application receives the `InitSignal()` function, it can create user interface components. Additionally, connect the callback `WidgetApplicationExample::Create()` function to the `Dali::WidgetApplication::InitSignal()` function:
   ```
    class WidgetApplicationExample : public ConnectionTracker
    {
      public:
        WidgetApplicationExample( WidgetApplication& application )
          : mApplication( application )
        {
          mApplication.InitSignal().Connect( this, &WidgetApplicationExample::Create );
        }

        void Create( Application& application )
        {
          // Register widget creating function here.
        }

      private:
        WidgetApplication& mApplication;
    }
   ```

3. Create a widget class

   On starting, ensure that you must have background knowledge on [Handle/Body Pattern: Basic Way of Using DALi Objects](../../ui/dali/handle.md).

   Additionally, for this pattern you need to construct two classes for custom widget:

   * Handle class
   * Body class

   In this step, implement `Demo::SampleWidget` class and `Demo::Internal::SampleWidget` class as handle/body class.

   1. To create handle class of custom widget include `<sample-widget.h>` header file in your application:
      ```
      #include <dali/public-api/adaptor-framework/widget.h>

      namespace Demo
      {
      namespace Internal
      {
        class SampleWidget;
      }
      class SampleWidget : public Dali::Widget    // Inherit widget class
      {
      public:
        SampleWidget();
        static SampleWidget New();
        ~SampleWidget();
        SampleWidget( const SampleWidget& sampleWidget );
        SampleWidget& operator=( const SampleWidget& sampleWidget );
      public:
        explicit SampleWidget( Internal::SampleWidget* sampleWidget );
      };
      }
      ```

   2. To create body class of the custom widget use `<sample-widget-impl.h>` header file in your application:

      ```
      #include <dali/public-api/adaptor-framework/widget-impl.h>

      // HANDLE INCLUDES
      #include "sample-widget.h"

      namespace Demo
      {
      namespace Internal
      {
      class SampleWidget : public Dali::Internal::Adaptor::Widget
      {
      public:
        SampleWidget();
        ~SampleWidget();
        static Demo::SampleWidget New();
        virtual void OnCreate( const std::string& contentInfo, Dali::Window window );
        virtual void OnTerminate( const std::string& contentInfo, Dali::Widget::Termination type );
        virtual void OnPause();
        virtual void OnResume();
        virtual void OnResize( Dali::Window window );
        virtual void OnUpdate( const std::string& contentInfo, int force );

      protected:
        // Undefined
        SampleWidget(const SampleWidget&);
        SampleWidget& operator=(SampleWidget&);
      };
      } // namespace Internal
      } // namespace Dali
      ```

   3. To implement each lifecycle function:

      ```
      #include "sample-widget-impl.h"
      #include <dali-toolkit/dali-toolkit.h>
      #include <dali/integration-api/debug.h>

      using namespace Dali;
      using namespace Dali::Toolkit;

      namespace Demo
      {
      namespace Internal
      {

      Demo::CustomWidget SampleWidget::New()
      {
        IntrusivePtr<SampleWidget> impl = new SampleWidget();
        Demo::SampleWidget handle = Demo::SampleWidget( impl.Get() );
        return handle;
      }

      SampleWidget::SampleWidget(){}

      SampleWidget::~SampleWidget(){}

      void SampleWidget::OnCreate( const std::string& contentInfo, Dali::Window window )
      {
        // This widget will draw "Hello world!" text when widget is loaded.

        TextLabel label = TextLabel::New("Hello world\n");
        Dali::Stage::GetCurrent().Add(label);
      }

      void SampleWidget::OnTerminate( const std::string& contentInfo, Dali::Widget::Termination type )
      {
        DALI_LOG_ERROR("Widget instance terminated\n");
      }

      void SampleWidget::OnPause()
      {
        DALI_LOG_ERROR("Widget instance paused\n");
      }

      void SampleWidget::OnResume()
      {
        DALI_LOG_ERROR("Widget instance resumed\n");
      }

      void SampleWidget::OnResize( Dali::Window window )
      {
        DALI_LOG_ERROR("Widget instance resized\n");
      }

      void SampleWidget::OnUpdate( const std::string& contentInfo, int force )
      {
        DALI_LOG_ERROR("Widget instance updated\n");
      }

      } // Internal
      } // Dali
      ```

   4. For custom widget include custom widget header. Also, add Widget `CreatingWidgetFunction()` function:

      ```
      #include "sample-widget.h"

      class WidgetApplicationExample : public ConnectionTracker
      {
        public:
          WidgetApplicationExample( WatchApplication& application )
          : mApplication( application )
          {
            mApplication.InitSignal().Connect( this, &WidgetApplicationExample::Create );
          }

          static Dali::Widget CreatingWidgetFunction(const std::string& widgetName)
          {
            Demo::SampleWidget widget = Demo::SampleWidget::New();
            return widget;
          }

          void Create( Application& application )
          {
            mApplication.RegisterWidgetCreatingFunction( "widget-dali.example", CreatingWidgetFunction );
          }

        private:
          WidgetApplication& mApplication;
      };
      ```

## Related Information
- Dependencies
  - Tizen 4.0 and Higher for Mobile
  - Tizen 4.0 and Higher for Wearable