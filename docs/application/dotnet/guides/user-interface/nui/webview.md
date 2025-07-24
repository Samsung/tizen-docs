# WebView

NUI `WebView` is a special component for showing web content. It supports interaction with web content through touch or key inputs so that you can browse multiple web pages.

## Load Web Content

You can load the Web content as follows:

- Set the `Url` property.

   In normal case, a web page is expressed as an internet address. You can set the address in the `Url` property:

    ```csharp
    var webview = new WebView()
    {
        Size = new Size(1280, 960),
        Url = "https://docs.tizen.org"
    };

    NUIApplication.GetDefaultWindow().Add(webview);
    ```

    In the preceding code snippet, connection to the internet is required and the application needs an internet privilege: `http://tizen.org/privilege/internet`. 
    You can also load a local resource file as a content of a `WebView`:

    ```csharp
    var webview = new WebView()
    {
        Size = new Size(1280, 960),
        Url = Tizen.Applications.Application.Current.DirectoryInfo.Resource + "hello.html"
    };

    NUIApplication.GetDefaultWindow().Add(webview);
    ```

- Call the `LoadUrl`.  Calling `LoadUrl` is equivalent to setting the `Url` property. The first example code snippet can be changed as follows:

    ```csharp
    var webview = new WebView()
    {
        Size = new Size(1280, 960),
    };

    webview.LoadUrl("https://docs.tizen.org");
    NUIApplication.GetDefaultWindow().Add(webview);
    ```

- Specify a web code in a string instead of the `Url`. You can write the web code directly:

    ```csharp
    var webview = new WebView()
    {
        Size = new Size(1280, 960),
    };

    webview.LoadHtmlString("<p>Hello World!</p>");

    NUIApplication.GetDefaultWindow().Add(webview);
    ```

    From the simple HTML text to the complicated web page, you can load the content using `LoadHtmlString`.

## Events

WebView provides several events. The following are the most commonly used events in WebView:

| Event                | Description                                                   |
|----------------------|---------------------------------------------------------------|
| `PageLoadStarted`    | This event is emitted when the page loading has started.      |
| `PageLoadFinished`   | This event is emitted when the page loading has completed.    |
| `PageLoadError`      | This event is emitted when the page loading has failed.       |
| `UrlChanged`         | This event is emitted when the page url is changed.           |


- Add an event handler:

    ```csharp
    void OnPageLoded(object sender, EventArgs e)
    {
        Tizen.Log.Info(tag, "Web page has been loaded.");
    }
    ```
    ```csharp
    webview.PageLoadFinished += OnPageLoded;
    ```

- Remove an event handler:

    ```csharp
    webview.PageLoadFinished -= OnPageLoded;
    ```

## WebView with JavaScript

NUI `WebView` provides several APIs to control JavaScript in a currently loaded web page.

- `EvaluateJavaScript`

    This API enables executing JavaScript code on a web page. For example, the following code can change the document's background color of a loaded web page to yellow:
    ```csharp
    var webview = new WebView()
    {
        Size = new Size(1280, 960)
    };

    webview.PageLoadFinished += (s, e) =>
    {
        webview.EvaluateJavaScript("document.body.style.backgroundColor = 'yellow';");
    };

    webview.LoadUrl("https://docs.tizen.org");

    NUIApplication.GetDefaultWindow().Add(webview);
    ```

- `AddJavaScriptMessageHandler`

    This API provides a way to inject a C# method as a JavaScript function named `postMessage` to a web page. The following example shows how to inject a C# method. To execute injected method, it uses `EvaluateJavaScript`:

    ```csharp
    void InjectedMethod(string message)
    {
        Tizen.Log.Info("TestWebView", "Message: " + message);
    }
    ```
    ```csharp
    var webview = new WebView()
    {
        Size = new Size(1280, 960),
    };

    mWebView.AddJavaScriptMessageHandler("InjectedObject", InjectedMethod);

    webview.LoadUrl("https://docs.tizen.org");

    webview.PageLoadFinished += (s, e) =>
    {
        webview.EvaluateJavaScript("InjectedObject.postMessage('Hello World!');");
    };

    NUIApplication.GetDefaultWindow().Add(webview);
    ```

    As a result of the code execution, you get a log message in a Tizen device as follows:
    ```
    I/TestWebView (3524): WebViewTest.cs: InjectedMethod(49) > Message: Hello World!
    ```

## Related information
- Dependencies
  -   Tizen 6.5 and Higher
