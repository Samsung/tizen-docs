### [Tizen.UI.Internal](Tizen.UI.Internal.md 'Tizen.UI.Internal')

## ResourceManager Class

Provides a method to get the path of a resource file.

```csharp
public static class ResourceManager
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; ResourceManager
### Properties

<a name='Tizen.UI.Internal.ResourceManager.ResourceDirectory'></a>

## ResourceManager.ResourceDirectory Property

Gets the application resource directory.

```csharp
public static string ResourceDirectory { get; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')
### Methods

<a name='Tizen.UI.Internal.ResourceManager.GetCommonPath(string)'></a>

## ResourceManager.GetCommonPath(string) Method

Gets the common path of the specified resource.

```csharp
public static string GetCommonPath(string res);
```
#### Parameters

<a name='Tizen.UI.Internal.ResourceManager.GetCommonPath(string).res'></a>

`res` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the resource.

#### Returns
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
The path of the resource.

<a name='Tizen.UI.Internal.ResourceManager.GetPath(string)'></a>

## ResourceManager.GetPath(string) Method

Gets the path of the specified resource.

```csharp
public static string GetPath(string res);
```
#### Parameters

<a name='Tizen.UI.Internal.ResourceManager.GetPath(string).res'></a>

`res` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the resource.

#### Returns
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
The path of the resource.




