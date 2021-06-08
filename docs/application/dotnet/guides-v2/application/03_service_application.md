1. Nie ma callbacka onPaused() i onResume()
2. Po co jest service application ??? 

Napisałbym tak: servicy są po to żeby robić jakieś rzeczy w tle, ale ważne jest żeby te rzeczy działały po zamknięciu aplikacji. 
Service jest więc komponentem, który działa w tle bez reakzji z userem. 

Np: aplikacja mierząca aktywność podczas ćwiczeń z funkcją zapisywania trasy.

Podzial aplikacji na serwisy pozwala na modularnosc aplikacji. Raz napisany serwis mozna wykorzystac w kilku aplikacjach
Np. Serwis monitorujący prędkość i logujący pozycję odczytaną z GPS może być wykorzystany w aplikacji mierzącej aktywność fizyczna, w aplikacji monitorującej położenie samochodu, i w wielu innych przypadkach.

Warto rozwazyc wydzielenie oddzielnego serwisu w aplikacji aby uproscic jej logikę, stworzyć reużywalne komponenty. Aby zrozumieć działanie serwisu należy zapoznać się z rozdziałem o wymianie danych między aplikacjami oraz o tym jak uruchamiać inne aplikacje z poziomu pisanej aplikacji.

Kod poniżej został wygenerowany z template. Kod domyslny nie ma callbacków OnPause() i OnResume(). 
Domyslnie obslugiwane są callbacki z appcontrola.

Przyklady kodu pokazuja dwie aplikacje, jedna z nich uruchamia service, druga jest serwisem działającym w tle.

```csharp
using Tizen.Applications;
```

W przypadku servicu nie musimy nalezy zainkludowac inny namespace. Nie jest to aplikacja powiązana z oknem i interfejsem użytkownika więc należy skorzuscaz z bazowej klasy `Tizen.Applications`. Dostaracza ona callbacki wywolywane podczas dzialania aplikacji typu service. Niektore z nich takie jak `OnCreate()`, `OnTerminate()`, `OnLowBattery()`, `OnLowMemory()`, `OnLocaleChanged()` często są przeciążane także w aplikacjach z UI. W tym przypadku nie przeciąża się metod `OnPause()` in `OnResume()`

```csharp
namespace servicesample
{
    class App : ServiceApplication
    {
        protected override void OnCreate()
        {
            base.OnCreate();
        }
```

```csharp
        protected override void OnAppControlReceived(AppControlReceivedEventArgs e)
        {
            base.OnAppControlReceived(e);
        }
```

```csharp
        protected override void OnLocaleChanged(LocaleChangedEventArgs e)
        {
            base.OnLocaleChanged(e);
        }

        protected override void OnLowBattery(LowBatteryEventArgs e)
        {
            base.OnLowBattery(e);
        }

        protected override void OnLowMemory(LowMemoryEventArgs e)
        {
            base.OnLowMemory(e);
        }

        protected override void OnRegionFormatChanged(RegionFormatChangedEventArgs e)
        {
            base.OnRegionFormatChanged(e);
        }

        protected override void OnTerminate()
        {
            base.OnTerminate();
        }
```

```csharp
        static void Main(string[] args)
        {
            App app = new App();
            app.Run(args);
        }
    }
}
```

Implementacja callbacka OnAppControlReceived() to pontencjalnie najważniejsza funkcja w prezentowanym serwisie. Jest to punk wymiany danych pomiędzy 


# Service Applications 

Servive applications are Tizen .NET applications with no graphical user interface that run in the background. The can be very useful in performing activities (such as getting sensor data in the background) that need to run periodically or continuously, but do not require any user intervention. 

The main Service Application API features include: 
-  Application States:

    A Tizen native service application has several different states which it transitions through during its life-cycle
- Event Callbacks:
  
  The service application can receive both basic system events and application state change events. You can register handlers for these events to react them. 

Service appliction can ve explicitly launched by a UI aplication. They can also be launched conditionally. 

The user cann check the running service applications in the task switcher, however, no events occur if the user selects a service application from the task switcher. The main menu does not contain icons for service applications. Multiple service applications can be running simultaneously with other service and UI applications. 

Application States 
Trzeba narysowac: 
Ready -> create() Created-> app control cb -> Runing . Terminated -> 

Zrobic tabelke z opisem stanów 
READY -> application is launcher 
Created -> application started the main loop
Running -> applicaiton runs in the background 
Terminated -> application is terminated 

Because a service application has no UI, neither does it have a pause state.  Basically, the service application is running in the background by its nature; so the platform does not allow running the service application.

Event Callbacks
You can control the service application execution by monitoring and reacting to application state change and system events.

The following table lists the application state change events.

Table: Application states

Callback	Description
`OnCreate`	Used to take necessary actions before the main event loop starts. Place the initialization code here.

`OnAppControlReceived()`	Used to take necessary actions when a service call arrives from another application.

`OnTerminate()` Used to take necessary actions when the application is terminating. Release all resources, especially any allocations and shared resources, so that other running applications can fully any shared resources.
The following table lists the system events.

Table: System events

Callback	Description
`OnLowMemory()`	Used to take necessary actions in low memory situations.
Save data in the main memory to a persistent memory or storage, to avoid data loss in case the Tizen platform Low Memory Killer kills your application to get more free memory. Release any cached data in the main memory to secure more free memory.
`OnLowBattery`() Used to take necessary actions in low battery situations.
Save data in the main memory to a persistent memory or storage, to avoid data loss in case the power goes off completely. Stop heavy CPU consumption or power consumption activities to save the remaining power.


## Application Attributes
Describe your service application attributes in the manifest file. The attributes determine the application behavior. The following code example illustrates how you can define the attributes:

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns="http://tizen.org/ns/packages" api-version="6" package="org.tizen.example.servicesample" version="1.0.0">
  <profile name="common" />
  <service-application appid="org.tizen.example.servicesample"
					exec="servicesample.dll"
					type="dotnet"
					multiple="false"
					taskmanage="false"
					nodisplay="true"
                    api-version="8">
    <label>servicesample</label>
    <icon>servicesample.png</icon>
  </service-application>
</manifest>
```

Pay specific attention to the following attributes:

auto-restart

If set to true, the application restarts whenever it terminates abnormally. If the application is running, it is launched after installing or updating the package.

on-boot

If set to true, the application launches on boot time, and after installing or updating the package. The application does not start if this attribute is removed after updating the package.

he following table defines the behaviors resulting from the attribute combinations:

Table: Attribute combinations

auto-restart	on-boot	After normal termination	On forced close	On Reboot	After package installation	After package update
FALSE	FALSE	Not launched automatically	Not launched automatically	Not launched after reboot	Not launched	Not launched automatically
FALSE	TRUE	Not launched automatically	Not launched automatically	Launched automatically after reboot	Launched	Launched automatically
TRUE	FALSE	Launched automatically	Launched automatically	Not launched after reboot	Not launched	Launched automatically
TRUE	TRUE	Launched automatically	Launched automatically	Launched automatically after reboot	Launched	Launched automatically

Monitoring Events
To monitor application state change and system events:

Add callbacks for application state change events:

Service application initialization callback

This callback is called when the application is launched. Use the callback to write the necessary initialization code, such as setting up the dbus connection.

The callback returns a Boolean value. If there is a critical error during the launch, the return is false, thereby cancelling the launch. Otherwise, the return is true.

bool
service_app_create(void *data)
{
    dlog_print(DLOG_DEBUG, LOG_TAG, "%s", __func__);

    return true;
}
Service application termination callback

This callback is called when the application terminates. Use the callback to release all resources, especially any allocations and shared resources used by other applications.

The service_app_exit() function quits the application main loop internally.

void
service_app_terminate(void *data)
{
    dlog_print(DLOG_DEBUG, LOG_TAG, "%s", __func__);
    service_app_exit();

    return;
}
Service request callback

This callback is called when the service application receives an app_control service request from another application.

void
service_app_control(app_control_h app_control, void *data)
{
    dlog_print(DLOG_DEBUG, LOG_TAG, "%s", __func__);
    service_app_exit();

    return;
}
Add callbacks for system events:

Low memory callback

This callback is called when the device is low on memory.

void
service_app_low_memory_callback(void *data)
{
    dlog_print(DLOG_DEBUG, LOG_TAG, "%s", __func__);
    service_app_exit();

    return;
}
Low battery callback

This callback is called when the device is low on battery power.

void
service_app_low_battery_callback(void *data)
{
    dlog_print(DLOG_DEBUG, LOG_TAG, "%s", __func__);
    service_app_exit();

    return;
}
Set the application state change event callbacks in the service_app_event_callback_s structure. The structure is passed to the function that starts the service application.

You can register the system event callbacks with the service_app_add_event_handler() function.

int
main(int argc, char* argv[])
{
    appdata_s ad = {0,};
    service_app_lifecycle_callback_s event_callback = {0,};

    dlog_print(DLOG_DEBUG, LOG_TAG, "%s", __func__);

    event_callback.create = service_app_create;
    event_callback.terminate = service_app_terminate;
    event_callback.app_control = service_app_control;

    dlog_print(DLOG_DEBUG, LOG_TAG, "service_app_main() is called.");

    return service_app_main(argc, argv, &event_callback, &ad);
}
