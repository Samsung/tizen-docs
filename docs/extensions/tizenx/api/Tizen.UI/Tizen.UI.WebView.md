### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## WebView Class

```csharp
public class WebView : Tizen.UI.View
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; [View](Tizen.UI.View.md 'Tizen.UI.View') &#129106; WebView
### Constructors

<a name='Tizen.UI.WebView.WebView()'></a>

## WebView() Constructor

Initializes a new instance of the WebView class.

```csharp
public WebView();
```
### Properties

<a name='Tizen.UI.WebView.CanGoBack'></a>

## WebView.CanGoBack Property

Gets a value that indicates whether the user can navigate to previous pages.

```csharp
public bool CanGoBack { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.WebView.CanGoForward'></a>

## WebView.CanGoForward Property

Gets a value that indicates whether the user can navigate forward.

```csharp
public bool CanGoForward { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.WebView.Source'></a>

## WebView.Source Property

Gets or sets the [WebViewSource](Tizen.UI.WebViewSource.md 'Tizen.UI.WebViewSource') object that represents the location that this WebView object displays.

```csharp
public Tizen.UI.WebViewSource Source { get; set; }
```

#### Property Value
[WebViewSource](Tizen.UI.WebViewSource.md 'Tizen.UI.WebViewSource')
### Methods

<a name='Tizen.UI.WebView.EvaluateJavaScript(string)'></a>

## WebView.EvaluateJavaScript(string) Method

Evaluates the provided script.

```csharp
public void EvaluateJavaScript(string script);
```
#### Parameters

<a name='Tizen.UI.WebView.EvaluateJavaScript(string).script'></a>

`script` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

A script to evaluate.

<a name='Tizen.UI.WebView.EvaluateJavaScriptAsync(string)'></a>

## WebView.EvaluateJavaScriptAsync(string) Method

Asynchronously evaluates the provided script.

```csharp
public System.Threading.Tasks.Task&lt;string> EvaluateJavaScriptAsync(string script);
```
#### Parameters

<a name='Tizen.UI.WebView.EvaluateJavaScriptAsync(string).script'></a>

`script` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

A script to evaluate.

#### Returns
[System.Threading.Tasks.Task&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')  
A task that contains the result of the evaluation as a string.

<a name='Tizen.UI.WebView.GoBack()'></a>

## WebView.GoBack() Method

Navigates to the previous page in the navigation history.

```csharp
public void GoBack();
```

<a name='Tizen.UI.WebView.GoForward()'></a>

## WebView.GoForward() Method

Navigates to the next page in the navigation history.

```csharp
public void GoForward();
```

<a name='Tizen.UI.WebView.Reload()'></a>

## WebView.Reload() Method

Reloads the current page.

```csharp
public void Reload();
```
### Events

<a name='Tizen.UI.WebView.NavigationCompleted'></a>

## WebView.NavigationCompleted Event

Occurs when the web naviagtion completes.

```csharp
public event EventHandler&lt;WebNavigationEventArgs> NavigationCompleted;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[WebNavigationEventArgs](Tizen.UI.WebNavigationEventArgs.md 'Tizen.UI.WebNavigationEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.WebView.NavigationStarted'></a>

## WebView.NavigationStarted Event

Occurs when the web naviagtion begins.

```csharp
public event EventHandler&lt;WebNavigationEventArgs> NavigationStarted;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[WebNavigationEventArgs](Tizen.UI.WebNavigationEventArgs.md 'Tizen.UI.WebNavigationEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')




