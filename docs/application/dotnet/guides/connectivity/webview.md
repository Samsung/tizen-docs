# WebView

You can access web pages and web content in your application using the WebView functionality. You can also use various other features for Web browsing, such as loading and displaying web pages, and navigating through the browsing history.

The main features of WebView are as follows:

- Initializing and Creating WebView

    You can [initialize a WebView](#initialize) and [create a WebView object](#initialize).

- Managing Web Page Loading

    You can [load a web page](#load) with requested URL and [register event handlers](#load) for loading events.

- Managing Cookie

    You can [set the cookie policy and the storage](#cookie) for the cookie.

- Finalizing WebView

    You can [shut down the WebView](#finalize) and clean up the resources.

## Prerequisites

1. To use the [Tizen.WebView](https://samsung.github.io/TizenFX/latest/api/Tizen.WebView.html) namespace, create the `ElmSharp-Beta` project using the [Project Wizard](../../../vstools/tools/project-wizard.md) of Visual Studio.

2. To use the class of the `Tizen.WebView` namespace, you must request for permission by adding the following privileges to the `tizen-manifest.xml` file, as shown in the following code snippet:

   ```
   <privileges>
     <!--To use the Internet connection-->
     <privilege>http://tizen.org/privilege/internet</privilege>

     <!--To access media storage-->
     <privilege>http://tizen.org/privilege/mediastorage</privilege>

     <!--To access, read, and write to the external storage-->\
     <privilege>http://tizen.org/privilege/externalstorage</privilege>
   </privileges>
   ```

3. To use the methods and properties of the `Tizen.WebView` namespace, include it in your application, as shown in the following code snippet:
    ```
    using Tizen.WebView;
    ```

<a name="initialize"></a>
## Initializing and Creating WebView

To Initialize WebView and create a WebView object, follow these steps:

1. To use the `Tizen.WebView` namespace in your application, call the `Tizen.WebView.Chromium.Initialize` method before the start of the main loop, as shown in the following code snippet:

    ```
    Elementary.Initialize();
    Elementary.ThemeOverlay();
    Chromium.Initialize();
    App app = new App();
    app.Run(args);
    ```

2. To create a WebView object, use the constructor of [Tizen.WebView.WebView](https://samsung.github.io/TizenFX/latest/api/Tizen.WebView.WebView.html) with `ElmSharp.Window`, as shown in the following code snippet:
    ```
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

- To load a web page, use the `Tizen.WebView.WebView.LoadUrl` method with an appropriate URL, as shown in the following code snippet:

    ```
    webView.LoadUrl("https://www.tizen.org/");
    ```

- The following table lists the loading events provided by the `Tizen.WebView.WebView` class:

**Table: Loading Events**

| Event            | Description                                                       | Argument                                 |
|------------------|-------------------------------------------------------------------|------------------------------------------|
| `LoadStarted`    | This event occurs when the page loading has started.              | -                                        |
| `LoadFinished`   | This event occurs when the page loading has completed.            | -                                        |
| `LoadError`      | This event occurs when the page loading has failed with an error. | Tizen.WebView.SmartCallbackLoadErrorArgs |

- Add an event handler to handle each loading event, as shown in the following code snippet:

    ```
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

To manage and set the cookie options, use the [Tizen.WebView.CookieManager](https://samsung.github.io/TizenFX/latest/api/Tizen.WebView.CookieManager.html) class.

- To get the `Tizen.WebView.CookieManager` object from WebView, use `Tizen.WebView.WebView.GetContext` and `Tizen.WebView.Context.GetCookieManager`, as shown in the following code snippet:

    ```
    CookieManager cookieManager = webView.GetContext().GetCookieManager();
    ```

- To set the cookie acceptance policy, use the `Tizen.WebView.CookieManager.SetCookieAcceptPolicy` method, as shown in the following code snippet:

    ```
    /* Accepts every cookie sent from any page */
    cookieManager.SetCookieAcceptPolicy(CookieAcceptPolicy.Always);

    /* Rejects all the cookies */
    cookieManager.SetCookieAcceptPolicy(CookieAcceptPolicy.Never);

    /* Accepts only cookies set by the main document that is loaded */
    cookieManager.SetCookieAcceptPolicy(CookieAcceptPolicy.NoThirdParty);
    ```

- To set the persistent storage for the cookie, use the `Tizen.WebView.CookieManager.SetPersistentStorage` method, as shown in the following code snippet:

    ```
    cookieManager.SetPersistentStorage(DirectoryInfo.Data, CookiePersistentStorage.SqlLite);
    ```

<a name="finalize"></a>
## Finalizing WebView
To clean up the allocated resources, call the `Tizen.WebView.Chromium.Shutdown` method after the end of the main loop, as shown in the following code snippet:

```
App app = new App();
app.Run(args);
Chromium.Shutdown();
```



## Related Information
  - Dependencies
      - Tizen 4.0 and Higher
