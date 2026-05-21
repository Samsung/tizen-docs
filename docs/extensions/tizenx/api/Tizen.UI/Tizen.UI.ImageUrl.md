### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## ImageUrl Class

The ImageUrl class represents an internally loaded image resource by its URI.

```csharp
public class ImageUrl : Tizen.UI.NObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; ImageUrl
### Constructors

<a name='Tizen.UI.ImageUrl.ImageUrl(System.IntPtr,bool)'></a>

## ImageUrl(IntPtr, bool) Constructor

Initializes a new instance of the ImageUrl class with the specified handle to the native image URL object.

```csharp
public ImageUrl(System.IntPtr handle, bool ownsHandle);
```
#### Parameters

<a name='Tizen.UI.ImageUrl.ImageUrl(System.IntPtr,bool).handle'></a>

`handle` [System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')

The handle to the native image URL object.

<a name='Tizen.UI.ImageUrl.ImageUrl(System.IntPtr,bool).ownsHandle'></a>

`ownsHandle` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether the new instance owns the handle.
### Methods

<a name='Tizen.UI.ImageUrl.ToString()'></a>

## ImageUrl.ToString() Method

Gets the URL of the image.

```csharp
public override string ToString();
```

#### Returns
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')  
The URL of the image.






