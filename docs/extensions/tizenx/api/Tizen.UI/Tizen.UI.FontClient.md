### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## FontClient Class

```csharp
public class FontClient : Tizen.UI.NObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; FontClient
### Properties

<a name='Tizen.UI.FontClient.Instance'></a>

## FontClient.Instance Property

Gets the singleton instance of the FontClient.

```csharp
public static Tizen.UI.FontClient Instance { get; }
```

#### Property Value
[FontClient](Tizen.UI.FontClient.md 'Tizen.UI.FontClient')
### Methods

<a name='Tizen.UI.FontClient.AddCustomFontDirectory(string)'></a>

## FontClient.AddCustomFontDirectory(string) Method

Adds custom fonts directory.

```csharp
public bool AddCustomFontDirectory(string path);
```
#### Parameters

<a name='Tizen.UI.FontClient.AddCustomFontDirectory(string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

Path to the fonts directory.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the fonts can be added.

<a name='Tizen.UI.FontClient.FontPreLoad(System.Collections.Generic.IEnumerable_string_,System.Collections.Generic.IEnumerable_string_,bool,bool)'></a>

## FontClient.FontPreLoad(IEnumerable&lt;string>, IEnumerable&lt;string>, bool, bool) Method

This is used to pre-load FreeType font face in order to improve the runtime performance of the application.  
> The fonts in the fontPathList perform FT_New_Face during pre-loading, which can provide some performace benefits.<br/>  
> The fonts in the memoryFontPathList read the font file and cache the buffer in memory during pre-load.<br/>  
> This enables the use of FT_New_Memory_Face during runtime and provides a performance boost.<br/>  
> It requires memory equivalent to the size of each font file.

```csharp
public static void FontPreLoad(System.Collections.Generic.IEnumerable&lt;string> fontPathList, System.Collections.Generic.IEnumerable&lt;string> memoryFontPathList, bool useThread, bool syncCreation=true);
```
#### Parameters

<a name='Tizen.UI.FontClient.FontPreLoad(System.Collections.Generic.IEnumerable_string_,System.Collections.Generic.IEnumerable_string_,bool,bool).fontPathList'></a>

`fontPathList` [System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')

A list of font paths to be pre-loaded.

<a name='Tizen.UI.FontClient.FontPreLoad(System.Collections.Generic.IEnumerable_string_,System.Collections.Generic.IEnumerable_string_,bool,bool).memoryFontPathList'></a>

`memoryFontPathList` [System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')

A list of memory font paths to be pre-loaded.

<a name='Tizen.UI.FontClient.FontPreLoad(System.Collections.Generic.IEnumerable_string_,System.Collections.Generic.IEnumerable_string_,bool,bool).useThread'></a>

`useThread` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True if the font client should create thread and perform font pre-loading, false otherwise.

<a name='Tizen.UI.FontClient.FontPreLoad(System.Collections.Generic.IEnumerable_string_,System.Collections.Generic.IEnumerable_string_,bool,bool).syncCreation'></a>

`syncCreation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True if thread creation guarantees syncronization with the main thread, false async creation. Optional, the default value is true.

<a name='Tizen.UI.FontClient.PreCache(System.Collections.Generic.IEnumerable_string_,System.Collections.Generic.IEnumerable_string_,string,bool,bool)'></a>

## FontClient.PreCache(IEnumerable&lt;string>, IEnumerable&lt;string>, string, bool, bool) Method

This is used to pre-cache FontConfig in order to improve the runtime performance of the application.

```csharp
public static void PreCache(System.Collections.Generic.IEnumerable&lt;string> fallbackFamilyList, System.Collections.Generic.IEnumerable&lt;string> extraFamilyList, string localeFamily, bool useThread, bool syncCreation=true);
```
#### Parameters

<a name='Tizen.UI.FontClient.PreCache(System.Collections.Generic.IEnumerable_string_,System.Collections.Generic.IEnumerable_string_,string,bool,bool).fallbackFamilyList'></a>

`fallbackFamilyList` [System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')

A list of fallback font families to be pre-cached.

<a name='Tizen.UI.FontClient.PreCache(System.Collections.Generic.IEnumerable_string_,System.Collections.Generic.IEnumerable_string_,string,bool,bool).extraFamilyList'></a>

`extraFamilyList` [System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')

A list of additional font families to be pre-cached.

<a name='Tizen.UI.FontClient.PreCache(System.Collections.Generic.IEnumerable_string_,System.Collections.Generic.IEnumerable_string_,string,bool,bool).localeFamily'></a>

`localeFamily` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

A locale font family to be pre-cached.

<a name='Tizen.UI.FontClient.PreCache(System.Collections.Generic.IEnumerable_string_,System.Collections.Generic.IEnumerable_string_,string,bool,bool).useThread'></a>

`useThread` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True if the font client should create thread and perform pre-caching, false otherwise.

<a name='Tizen.UI.FontClient.PreCache(System.Collections.Generic.IEnumerable_string_,System.Collections.Generic.IEnumerable_string_,string,bool,bool).syncCreation'></a>

`syncCreation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True if thread creation guarantees syncronization with the main thread, false async creation. Optional, the default value is true.






