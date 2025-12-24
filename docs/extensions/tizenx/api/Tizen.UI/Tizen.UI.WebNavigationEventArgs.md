### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## WebNavigationEventArgs Class

Provides data for the [NavigationStarted](Tizen.UI.WebView.md#Tizen.UI.WebView.NavigationStarted 'Tizen.UI.WebView.NavigationStarted') or [NavigationCompleted](Tizen.UI.WebView.md#Tizen.UI.WebView.NavigationCompleted 'Tizen.UI.WebView.NavigationCompleted') event.

```csharp
public class WebNavigationEventArgs : System.EventArgs
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs') &#129106; WebNavigationEventArgs
### Constructors

<a name='Tizen.UI.WebNavigationEventArgs.WebNavigationEventArgs(string)'></a>

## WebNavigationEventArgs(string) Constructor

Initializes a new instance of the [WebNavigationEventArgs](Tizen.UI.WebNavigationEventArgs.md 'Tizen.UI.WebNavigationEventArgs') class with the specified url.

```csharp
public WebNavigationEventArgs(string url);
```
#### Parameters

<a name='Tizen.UI.WebNavigationEventArgs.WebNavigationEventArgs(string).url'></a>

`url` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The url.
### Properties

<a name='Tizen.UI.WebNavigationEventArgs.Url'></a>

## WebNavigationEventArgs.Url Property

Gets the destination of the navigation.

```csharp
public string Url { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')




