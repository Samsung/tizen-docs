# WebView

You can access web pages and web content in your application using the WebView functionality. You can also use various other features for Web browsing, such as loading and displaying web pages, and navigating through the browsing history.

The main features of WebView are as follows:

- Initializing and Creating WebView

    You can [initialize a WebView](#initialize) and [create a WebView object](#initialize).

- Managing Web Page Loading

    You can [load a web page](#load) with requested URL and [register event handlers](#load) for loading events.

- Managing Cookie

    You can [set the cookie policy and the storage](#cookie) for the cookie.

- Executing JavaScript

    You can [execute the JavaScript code](#eval) in the context of the current WebView.

- Finalizing WebView

    You can [shut down the WebView](#finalize) and clean up the resources.

## Prerequisites

To enable your application to use WebView functionality:

1. To use the [Tizen.WebView](/application/dotnet/api/TizenFX/latest/api/Tizen.WebView.html) namespace, create the `ElmSharp-Beta` project using the [Project Wizard](../../../vstools/tools/project-wizard.md) of Visual Studio.

2. To use the class of the `Tizen.WebView` namespace, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

   ```XML
   <privileges>
       <!--To use the Internet connection-->
       <privilege>http://tizen.org/privilege/internet</privilege>

       <!--To access media storage-->
       <privilege>http://tizen.org/privilege/mediastorage</privilege>

       <!--To access, read, and write to the external storage-->
       <privilege>http://tizen.org/privilege/externalstorage</privilege>
   </privileges>
   ```

3. To use the methods and properties of the `Tizen.WebView` namespace, include it in your application:
    ```csharp
    using Tizen.WebView;
    ```

<a name="initialize"></a>
## Initializing and Creating WebView

To Initialize WebView and create a WebView object, follow these steps:

1. To use the `Tizen.WebView` namespace in your application, call the `Tizen.WebView.Chromium.Initialize` method before the start of the main loop:

    ```csharp
    Elementary.Initialize();
    Elementary.ThemeOverlay();
    Chromium.Initialize();
    App app = new App();
    app.Run(args);
    ```

2. To create a WebView object, use the constructor of [Tizen.WebView.WebView](/application/dotnet/api/TizenFX/latest/api/Tizen.WebView.WebView.html) with `ElmSharp.Window`:
    ```csharp
    var webView = new WebView(window)
    {
        AlignmentX = -1,
        AlignmentY = -1,
        WeightX = 1,
        WeightY = 1
    };
    webView.Show();
    ```

<a name="load"></a>
## Managing Web Page Loading

To load a web page and add an event handler to loading events:

- To load a web page, use the `Tizen.WebView.WebView.LoadUrl` method with an appropriate URL:

    ```csharp
    webView.LoadUrl("https://www.tizen.org/");
    ```

- The following table lists the loading events provided by the `Tizen.WebView.WebView` class:

  **Table: Loading Events**

  | Event            | Description                                                       | Argument                                 |
  |------------------|-------------------------------------------------------------------|------------------------------------------|
  | `LoadStarted`    | This event occurs when the page loading has started.              | -                                        |
  | `LoadFinished`   | This event occurs when the page loading has completed.            | -                                        |
  | `LoadError`      | This event occurs when the page loading has failed with an error. | Tizen.WebView.SmartCallbackLoadErrorArgs |

- Add an event handler to handle each loading event:

    ```csharp
    webView.LoadStarted += (s, e) =>
    {
        /* Handle LoadStarted event here */
    };

    webView.LoadFinished += (s, e) =>
    {
        /* Handle LoadFinished event here */
    };

    webView.LoadError += (s, e) =>
    {
        /* Handle LoadError event here */

        // error code
        var code = e.Code;

        // description
        var desc = e.Description;

        // URL
        var url = e.Url;
    };
    ```

<a name='cookie'></a>
## Managing Cookie

To manage and set the cookie options, use the [Tizen.WebView.CookieManager](/application/dotnet/api/TizenFX/latest/api/Tizen.WebView.CookieManager.html) class.

- To get the `Tizen.WebView.CookieManager` object from WebView, use `Tizen.WebView.WebView.GetContext` and `Tizen.WebView.Context.GetCookieManager`:

    ```csharp
    CookieManager cookieManager = webView.GetContext().GetCookieManager();
    ```

- To set the cookie acceptance policy, use the `Tizen.WebView.CookieManager.SetCookieAcceptPolicy` method:

    ```csharp
    /* Accepts every cookie sent from any page */
    cookieManager.SetCookieAcceptPolicy(CookieAcceptPolicy.Always);

    /* Rejects all the cookies */
    cookieManager.SetCookieAcceptPolicy(CookieAcceptPolicy.Never);

    /* Accepts only cookies set by the main document that is loaded */
    cookieManager.SetCookieAcceptPolicy(CookieAcceptPolicy.NoThirdParty);
    ```

- To set the persistent storage for the cookie, use the `Tizen.WebView.CookieManager.SetPersistentStorage` method:

    ```csharp
    cookieManager.SetPersistentStorage(DirectoryInfo.Data, CookiePersistentStorage.SqlLite);
    ```

<a name="eval"></a>
## Executing JavaScript

To execute the JavaScript code, use the `Tizen.WebView.Eval` and `Tizen.WebView.EvalAsync` methods.

The following example shows the HTML file used:


```HTML
<html>
<body>
    <div id="main" class="page">
        <div class="contents">
            <span id="content-text">Basic</span>
        </div>
    </div>
</body>
</html>
```

- If you need a return value, use the `Tizen.WebView.EvalAsync` method:

    ```csharp
    string result = await webView.EvalAsync("document.getElementById('content-text').innerHTML");
    ```
- If you do not need a return value, use the `Tizen.WebView.Eval` method:

    ```csharp
    webView.Eval("document.getElementById('content-text').innerHTML = 'Tizen'");
    ```

<a name="finalize"></a>
## Finalizing WebView
To clean up the allocated resources, call the `Tizen.WebView.Chromium.Shutdown` method after the end of the main loop:

```csharp
App app = new App();
app.Run(args);
Chromium.Shutdown();
```



## Related Information
  - Dependencies
      - Tizen 4.0 and Higher
