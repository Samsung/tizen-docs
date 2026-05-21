### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## Log Class

Provides methods for logging messages with different levels of importance.

```csharp
public static class Log
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Log
### Properties

<a name='Tizen.UI.Log.Tag'></a>

## Log.Tag Property

Gets or sets the tag used for logging.

```csharp
public static string Tag { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')
### Methods

<a name='Tizen.UI.Log.Debug(string,string,string,int)'></a>

## Log.Debug(string, string, string, int) Method

Writes a debug message to the log.

```csharp
public static void Debug(string message, string file="", string func="", int line=0);
```
#### Parameters

<a name='Tizen.UI.Log.Debug(string,string,string,int).message'></a>

`message` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The message to write.

<a name='Tizen.UI.Log.Debug(string,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file name where the method is called.

<a name='Tizen.UI.Log.Debug(string,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The method name where the method is called.

<a name='Tizen.UI.Log.Debug(string,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The line number in the source file where the method is called.

<a name='Tizen.UI.Log.Error(string,string,string,int)'></a>

## Log.Error(string, string, string, int) Method

Writes an error message to the log.

```csharp
public static void Error(string message, string file="", string func="", int line=0);
```
#### Parameters

<a name='Tizen.UI.Log.Error(string,string,string,int).message'></a>

`message` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The message to write.

<a name='Tizen.UI.Log.Error(string,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file name where the method is called.

<a name='Tizen.UI.Log.Error(string,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The method name where the method is called.

<a name='Tizen.UI.Log.Error(string,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The line number in the source file where the method is called.

<a name='Tizen.UI.Log.Info(string,string,string,int)'></a>

## Log.Info(string, string, string, int) Method

Writes an informational message to the log.

```csharp
public static void Info(string message, string file="", string func="", int line=0);
```
#### Parameters

<a name='Tizen.UI.Log.Info(string,string,string,int).message'></a>

`message` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The message to write.

<a name='Tizen.UI.Log.Info(string,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file name where the method is called.

<a name='Tizen.UI.Log.Info(string,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The method name where the method is called.

<a name='Tizen.UI.Log.Info(string,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Log.Warn(string,string,string,int)'></a>

## Log.Warn(string, string, string, int) Method

Writes a warning message to the log.

```csharp
public static void Warn(string message, string file="", string func="", int line=0);
```
#### Parameters

<a name='Tizen.UI.Log.Warn(string,string,string,int).message'></a>

`message` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The message to write.

<a name='Tizen.UI.Log.Warn(string,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file name where the method is called.

<a name='Tizen.UI.Log.Warn(string,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The method name where the method is called.

<a name='Tizen.UI.Log.Warn(string,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The line number in the source file where the method is called.






