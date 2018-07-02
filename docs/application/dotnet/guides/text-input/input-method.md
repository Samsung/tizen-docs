# Input Method


The input method editor (IME) is an input panel (keyboard) that lets the user input text and the platform receive the entered data. The user can select an IME as their default keyboard in the device Settings application.

You can create an application that provides a new IME. You can start the IME application life-cycle, interact with the current IME UI state, and retrieve attributes and events.

The main features of the Tizen.Uix.InputMethod namespace include:

-   Managing the IME life-cycle

    The system can have multiple keyboards, and the user can choose which one to use as the default keyboard. The IME application [starts its life-cycle](#start) when it is selected as the default keyboard. The following figure shows the IME application life-cycle.

    **Figure: IME application life-cycle**

    ![IME application life-cycle](./media/ime_lifecycle_cs.png)

    The IME application runs in the following way:

    1.  Once the IME application is started, the `Create()` event handler is called.
    2.  When a text input UI control receives focus, the `Show()` event handler is called.

        The IME application can call `Tizen.Uix.InputMethod` methods to interact with the UI control. The event handlers are called when the UI control state changes. When the text input UI control loses focus, the `Hide()` event handler is called.

    3.  When the IME application is finished, the `Terminate()` event handler is called.

-   Managing the main loop and event handlers

    The IME application must implement the `Main()` method. It is the main entry point, in which you can register event handlers and call the `Run()` method of the [Tizen.Uix.InputMethod.InputMethodEditor](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Uix.InputMethod.InputMethodEditor.html) class to start the main loop.

    During its life-cycle, the IME application can receive a number of events from the Tizen input service framework through the event handlers. You must register the mandatory `Create()`, `Terminate()`, `Show()`, and `Hide()` event handlers. Other event handlers can be registered as required by the specific IME application.

-   Showing and hiding the keyboard

    When an associated text input UI control has focus, the active keyboard is shown. When the text input UI control loses focus, the keyboard is hidden.

    The `Show()` and `Hide()` event handlers are used to manage the keyboard visibility, and the IME application must register both of them when starting the IME main loop.

    The client application can set various configurations for each text input UI control, such as the cursor position, key layout type, return key type, and flags for predictive text. The configurations are delivered to the IME application through the `Show()` event handler, to allow the keyboard to show the correct appearance to the user.

## Prerequisites

To enable your application to use the input method functionality:

1.  To use the [Tizen.Uix.InputMethod](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Uix.InputMethod.html) namespace, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/ime</privilege>
    </privileges>
    ```

2.  To use the methods and properties of the Tizen.Uix.InputMethod namespace, include it in your application:

    ```
    using Tizen.Uix.InputMethod;
    ```

<a name="start"></a>
## Starting the IME Life-cycle

To start the IME application life-cycle:

1.  Register the mandatory `Create()`, `Terminate()`, `Show()`, and `Hide()` event handlers:

    ```
    internal static void Create() {}
    internal static void Terminate() {}
    internal static void Show(InputMethodEditor.ContextId id, InputMethodContext ctx) {}
    internal static void Hide(InputMethodEditor.ContextId id) {}
    ```

2.  Implement the `Main()` method as the main entry point of the IME application:

    ```
    static void Main(string[] args)
    {
    ```

    The method is called when the user selects the IME as default from the IME selector menu.

3.  Inside the `Main()` method, add the required event handlers and call the `Run()` method to start the application:

    ```
        InputMethodEditor.Run(Create, Terminate, Show, Hide);
    }
    ```


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
