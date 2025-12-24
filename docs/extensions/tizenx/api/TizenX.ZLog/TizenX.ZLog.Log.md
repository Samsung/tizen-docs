### [TizenX.ZLog](TizenX.ZLog.md 'TizenX.ZLog')

## Log Class

```csharp
public static class Log
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Log
### Methods

<a name='TizenX.ZLog.Log.Debug(string,string,string,string,int)'></a>

## Log.Debug(string, string, string, string, int) Method

Prints a regular log message with the DEBUG priority.

```csharp
public static void Debug(string tag, string message, string file="", string func="", int line=0);
```
#### Parameters

<a name='TizenX.ZLog.Log.Debug(string,string,string,string,int).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag name of the log message.

<a name='TizenX.ZLog.Log.Debug(string,string,string,string,int).message'></a>

`message` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The log message to print.

<a name='TizenX.ZLog.Log.Debug(string,string,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file path of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Debug(string,string,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The function name of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Debug(string,string,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The line number of the calling position. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Debug(string,System.ReadOnlySpan_char_,string,string,int)'></a>

## Log.Debug(string, ReadOnlySpan&lt;char>, string, string, int) Method

Prints a regular log message with the DEBUG priority.

```csharp
public static void Debug(string tag, System.ReadOnlySpan&lt;char> message, string file="", string func="", int line=0);
```
#### Parameters

<a name='TizenX.ZLog.Log.Debug(string,System.ReadOnlySpan_char_,string,string,int).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag name of the log message.

<a name='TizenX.ZLog.Log.Debug(string,System.ReadOnlySpan_char_,string,string,int).message'></a>

`message` [System.ReadOnlySpan&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.ReadOnlySpan-1 'System.ReadOnlySpan`1')[System.Char](https://docs.microsoft.com/en-us/dotnet/api/System.Char 'System.Char')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.ReadOnlySpan-1 'System.ReadOnlySpan`1')

The log message to print.

<a name='TizenX.ZLog.Log.Debug(string,System.ReadOnlySpan_char_,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file path of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Debug(string,System.ReadOnlySpan_char_,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The function name of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Debug(string,System.ReadOnlySpan_char_,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The line number of the calling position. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Debug(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int)'></a>

## Log.Debug(string, LogInterpolatedStringHandler, string, string, int) Method

Prints a regular log message with the DEBUG priority.

```csharp
public static void Debug(string tag, TizenX.ZLog.LogInterpolatedStringHandler message, string file="", string func="", int line=0);
```
#### Parameters

<a name='TizenX.ZLog.Log.Debug(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag name of the log message.

<a name='TizenX.ZLog.Log.Debug(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).message'></a>

`message` TizenX.ZLog.LogInterpolatedStringHandler

The log message to print.

<a name='TizenX.ZLog.Log.Debug(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file path of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Debug(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The function name of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Debug(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The line number of the calling position. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Error(string,string,string,string,int)'></a>

## Log.Error(string, string, string, string, int) Method

Prints a regular log message with the ERROR priority.

```csharp
public static void Error(string tag, string message, string file="", string func="", int line=0);
```
#### Parameters

<a name='TizenX.ZLog.Log.Error(string,string,string,string,int).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag name of the log message.

<a name='TizenX.ZLog.Log.Error(string,string,string,string,int).message'></a>

`message` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The log message to print.

<a name='TizenX.ZLog.Log.Error(string,string,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file path of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Error(string,string,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The function name of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Error(string,string,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The line number of the calling position. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Error(string,System.ReadOnlySpan_char_,string,string,int)'></a>

## Log.Error(string, ReadOnlySpan&lt;char>, string, string, int) Method

Prints a regular log message with the ERROR priority.

```csharp
public static void Error(string tag, System.ReadOnlySpan&lt;char> message, string file="", string func="", int line=0);
```
#### Parameters

<a name='TizenX.ZLog.Log.Error(string,System.ReadOnlySpan_char_,string,string,int).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag name of the log message.

<a name='TizenX.ZLog.Log.Error(string,System.ReadOnlySpan_char_,string,string,int).message'></a>

`message` [System.ReadOnlySpan&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.ReadOnlySpan-1 'System.ReadOnlySpan`1')[System.Char](https://docs.microsoft.com/en-us/dotnet/api/System.Char 'System.Char')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.ReadOnlySpan-1 'System.ReadOnlySpan`1')

The log message to print.

<a name='TizenX.ZLog.Log.Error(string,System.ReadOnlySpan_char_,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file path of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Error(string,System.ReadOnlySpan_char_,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The function name of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Error(string,System.ReadOnlySpan_char_,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The line number of the calling position. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Error(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int)'></a>

## Log.Error(string, LogInterpolatedStringHandler, string, string, int) Method

Prints a regular log message with the ERROR priority.

```csharp
public static void Error(string tag, TizenX.ZLog.LogInterpolatedStringHandler message, string file="", string func="", int line=0);
```
#### Parameters

<a name='TizenX.ZLog.Log.Error(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag name of the log message.

<a name='TizenX.ZLog.Log.Error(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).message'></a>

`message` TizenX.ZLog.LogInterpolatedStringHandler

The log message to print.

<a name='TizenX.ZLog.Log.Error(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file path of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Error(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The function name of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Error(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The line number of the calling position. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Fatal(string,string,string,string,int)'></a>

## Log.Fatal(string, string, string, string, int) Method

Prints a regular log message with the FATAL priority.

```csharp
public static void Fatal(string tag, string message, string file="", string func="", int line=0);
```
#### Parameters

<a name='TizenX.ZLog.Log.Fatal(string,string,string,string,int).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag name of the log message.

<a name='TizenX.ZLog.Log.Fatal(string,string,string,string,int).message'></a>

`message` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The log message to print.

<a name='TizenX.ZLog.Log.Fatal(string,string,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file path of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Fatal(string,string,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The function name of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Fatal(string,string,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The line number of the calling position. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Fatal(string,System.ReadOnlySpan_char_,string,string,int)'></a>

## Log.Fatal(string, ReadOnlySpan&lt;char>, string, string, int) Method

Prints a regular log message with the FATAL priority.

```csharp
public static void Fatal(string tag, System.ReadOnlySpan&lt;char> message, string file="", string func="", int line=0);
```
#### Parameters

<a name='TizenX.ZLog.Log.Fatal(string,System.ReadOnlySpan_char_,string,string,int).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag name of the log message.

<a name='TizenX.ZLog.Log.Fatal(string,System.ReadOnlySpan_char_,string,string,int).message'></a>

`message` [System.ReadOnlySpan&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.ReadOnlySpan-1 'System.ReadOnlySpan`1')[System.Char](https://docs.microsoft.com/en-us/dotnet/api/System.Char 'System.Char')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.ReadOnlySpan-1 'System.ReadOnlySpan`1')

The log message to print.

<a name='TizenX.ZLog.Log.Fatal(string,System.ReadOnlySpan_char_,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file path of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Fatal(string,System.ReadOnlySpan_char_,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The function name of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Fatal(string,System.ReadOnlySpan_char_,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The line number of the calling position. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Fatal(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int)'></a>

## Log.Fatal(string, LogInterpolatedStringHandler, string, string, int) Method

Prints a regular log message with the FATAL priority.

```csharp
public static void Fatal(string tag, TizenX.ZLog.LogInterpolatedStringHandler message, string file="", string func="", int line=0);
```
#### Parameters

<a name='TizenX.ZLog.Log.Fatal(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag name of the log message.

<a name='TizenX.ZLog.Log.Fatal(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).message'></a>

`message` TizenX.ZLog.LogInterpolatedStringHandler

The log message to print.

<a name='TizenX.ZLog.Log.Fatal(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file path of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Fatal(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The function name of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Fatal(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The line number of the calling position. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Info(string,string,string,string,int)'></a>

## Log.Info(string, string, string, string, int) Method

Prints a regular log message with the INFO priority.

```csharp
public static void Info(string tag, string message, string file="", string func="", int line=0);
```
#### Parameters

<a name='TizenX.ZLog.Log.Info(string,string,string,string,int).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag name of the log message.

<a name='TizenX.ZLog.Log.Info(string,string,string,string,int).message'></a>

`message` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The log message to print.

<a name='TizenX.ZLog.Log.Info(string,string,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file path of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Info(string,string,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The function name of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Info(string,string,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The line number of the calling position. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Info(string,System.ReadOnlySpan_char_,string,string,int)'></a>

## Log.Info(string, ReadOnlySpan&lt;char>, string, string, int) Method

Prints a regular log message with the INFO priority.

```csharp
public static void Info(string tag, System.ReadOnlySpan&lt;char> message, string file="", string func="", int line=0);
```
#### Parameters

<a name='TizenX.ZLog.Log.Info(string,System.ReadOnlySpan_char_,string,string,int).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag name of the log message.

<a name='TizenX.ZLog.Log.Info(string,System.ReadOnlySpan_char_,string,string,int).message'></a>

`message` [System.ReadOnlySpan&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.ReadOnlySpan-1 'System.ReadOnlySpan`1')[System.Char](https://docs.microsoft.com/en-us/dotnet/api/System.Char 'System.Char')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.ReadOnlySpan-1 'System.ReadOnlySpan`1')

The log message to print.

<a name='TizenX.ZLog.Log.Info(string,System.ReadOnlySpan_char_,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file path of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Info(string,System.ReadOnlySpan_char_,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The function name of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Info(string,System.ReadOnlySpan_char_,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The line number of the calling position. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Info(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int)'></a>

## Log.Info(string, LogInterpolatedStringHandler, string, string, int) Method

Prints a regular log message with the INFO priority.

```csharp
public static void Info(string tag, TizenX.ZLog.LogInterpolatedStringHandler message, string file="", string func="", int line=0);
```
#### Parameters

<a name='TizenX.ZLog.Log.Info(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag name of the log message.

<a name='TizenX.ZLog.Log.Info(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).message'></a>

`message` TizenX.ZLog.LogInterpolatedStringHandler

The log message to print.

<a name='TizenX.ZLog.Log.Info(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file path of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Info(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The function name of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Info(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The line number of the calling position. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Verbose(string,string,string,string,int)'></a>

## Log.Verbose(string, string, string, string, int) Method

Prints a regular log message with the VERBOSE priority.

```csharp
public static void Verbose(string tag, string message, string file="", string func="", int line=0);
```
#### Parameters

<a name='TizenX.ZLog.Log.Verbose(string,string,string,string,int).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag name of the log message.

<a name='TizenX.ZLog.Log.Verbose(string,string,string,string,int).message'></a>

`message` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The log message to print.

<a name='TizenX.ZLog.Log.Verbose(string,string,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file path of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Verbose(string,string,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The function name of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Verbose(string,string,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The line number of the calling position. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Verbose(string,System.ReadOnlySpan_char_,string,string,int)'></a>

## Log.Verbose(string, ReadOnlySpan&lt;char>, string, string, int) Method

Prints a regular log message with the VERBOSE priority.

```csharp
public static void Verbose(string tag, System.ReadOnlySpan&lt;char> message, string file="", string func="", int line=0);
```
#### Parameters

<a name='TizenX.ZLog.Log.Verbose(string,System.ReadOnlySpan_char_,string,string,int).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag name of the log message.

<a name='TizenX.ZLog.Log.Verbose(string,System.ReadOnlySpan_char_,string,string,int).message'></a>

`message` [System.ReadOnlySpan&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.ReadOnlySpan-1 'System.ReadOnlySpan`1')[System.Char](https://docs.microsoft.com/en-us/dotnet/api/System.Char 'System.Char')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.ReadOnlySpan-1 'System.ReadOnlySpan`1')

The log message to print.

<a name='TizenX.ZLog.Log.Verbose(string,System.ReadOnlySpan_char_,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file path of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Verbose(string,System.ReadOnlySpan_char_,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The function name of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Verbose(string,System.ReadOnlySpan_char_,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The line number of the calling position. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Verbose(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int)'></a>

## Log.Verbose(string, LogInterpolatedStringHandler, string, string, int) Method

Prints a regular log message with the VERBOSE priority.

```csharp
public static void Verbose(string tag, TizenX.ZLog.LogInterpolatedStringHandler message, string file="", string func="", int line=0);
```
#### Parameters

<a name='TizenX.ZLog.Log.Verbose(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag name of the log message.

<a name='TizenX.ZLog.Log.Verbose(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).message'></a>

`message` TizenX.ZLog.LogInterpolatedStringHandler

The log message to print.

<a name='TizenX.ZLog.Log.Verbose(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file path of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Verbose(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The function name of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Verbose(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The line number of the calling position. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Warn(string,string,string,string,int)'></a>

## Log.Warn(string, string, string, string, int) Method

Prints a regular log message with the WARNING priority.

```csharp
public static void Warn(string tag, string message, string file="", string func="", int line=0);
```
#### Parameters

<a name='TizenX.ZLog.Log.Warn(string,string,string,string,int).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag name of the log message.

<a name='TizenX.ZLog.Log.Warn(string,string,string,string,int).message'></a>

`message` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The log message to print.

<a name='TizenX.ZLog.Log.Warn(string,string,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file path of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Warn(string,string,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The function name of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Warn(string,string,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The line number of the calling position. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Warn(string,System.ReadOnlySpan_char_,string,string,int)'></a>

## Log.Warn(string, ReadOnlySpan&lt;char>, string, string, int) Method

Prints a regular log message with the WARNING priority.

```csharp
public static void Warn(string tag, System.ReadOnlySpan&lt;char> message, string file="", string func="", int line=0);
```
#### Parameters

<a name='TizenX.ZLog.Log.Warn(string,System.ReadOnlySpan_char_,string,string,int).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag name of the log message.

<a name='TizenX.ZLog.Log.Warn(string,System.ReadOnlySpan_char_,string,string,int).message'></a>

`message` [System.ReadOnlySpan&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.ReadOnlySpan-1 'System.ReadOnlySpan`1')[System.Char](https://docs.microsoft.com/en-us/dotnet/api/System.Char 'System.Char')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.ReadOnlySpan-1 'System.ReadOnlySpan`1')

The log message to print.

<a name='TizenX.ZLog.Log.Warn(string,System.ReadOnlySpan_char_,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file path of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Warn(string,System.ReadOnlySpan_char_,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The function name of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Warn(string,System.ReadOnlySpan_char_,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The line number of the calling position. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Warn(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int)'></a>

## Log.Warn(string, LogInterpolatedStringHandler, string, string, int) Method

Prints a regular log message with the WARNING priority.

```csharp
public static void Warn(string tag, TizenX.ZLog.LogInterpolatedStringHandler message, string file="", string func="", int line=0);
```
#### Parameters

<a name='TizenX.ZLog.Log.Warn(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag name of the log message.

<a name='TizenX.ZLog.Log.Warn(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).message'></a>

`message` TizenX.ZLog.LogInterpolatedStringHandler

The log message to print.

<a name='TizenX.ZLog.Log.Warn(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).file'></a>

`file` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The source file path of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Warn(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).func'></a>

`func` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The function name of the caller function. This argument will be set automatically by the compiler.

<a name='TizenX.ZLog.Log.Warn(string,TizenX.ZLog.LogInterpolatedStringHandler,string,string,int).line'></a>

`line` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The line number of the calling position. This argument will be set automatically by the compiler.

