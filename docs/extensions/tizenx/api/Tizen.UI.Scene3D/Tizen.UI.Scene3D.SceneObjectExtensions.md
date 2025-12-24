### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## SceneObjectExtensions Class

```csharp
public static class SceneObjectExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; SceneObjectExtensions
### Methods

<a name='Tizen.UI.Scene3D.SceneObjectExtensions.AddRenderer(thisTizen.UI.Scene3D.SceneObject,Tizen.UI.Internal.Renderer)'></a>

## SceneObjectExtensions.AddRenderer(this SceneObject, Renderer) Method

Adds a renderer to the sceneObject.

```csharp
public static int AddRenderer(this Tizen.UI.Scene3D.SceneObject sceneObject, Tizen.UI.Internal.Renderer renderer);
```
#### Parameters

<a name='Tizen.UI.Scene3D.SceneObjectExtensions.AddRenderer(thisTizen.UI.Scene3D.SceneObject,Tizen.UI.Internal.Renderer).sceneObject'></a>

`sceneObject` [SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject')

<a name='Tizen.UI.Scene3D.SceneObjectExtensions.AddRenderer(thisTizen.UI.Scene3D.SceneObject,Tizen.UI.Internal.Renderer).renderer'></a>

`renderer` [Tizen.UI.Internal.Renderer](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Internal.Renderer 'Tizen.UI.Internal.Renderer')

The renderer to add.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The index of the Renderer that was added to the sceneObject.

<a name='Tizen.UI.Scene3D.SceneObjectExtensions.GetRendererAt(thisTizen.UI.Scene3D.SceneObject,int)'></a>

## SceneObjectExtensions.GetRendererAt(this SceneObject, int) Method

Retrieves the renderer at the specified index.

```csharp
public static Tizen.UI.Internal.Renderer GetRendererAt(this Tizen.UI.Scene3D.SceneObject sceneObject, int index);
```
#### Parameters

<a name='Tizen.UI.Scene3D.SceneObjectExtensions.GetRendererAt(thisTizen.UI.Scene3D.SceneObject,int).sceneObject'></a>

`sceneObject` [SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject')

<a name='Tizen.UI.Scene3D.SceneObjectExtensions.GetRendererAt(thisTizen.UI.Scene3D.SceneObject,int).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index of the renderer to retrieve.

#### Returns
[Tizen.UI.Internal.Renderer](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Internal.Renderer 'Tizen.UI.Internal.Renderer')  
A Renderer object at the specified index.

<a name='Tizen.UI.Scene3D.SceneObjectExtensions.GetRendererCount(thisTizen.UI.Scene3D.SceneObject)'></a>

## SceneObjectExtensions.GetRendererCount(this SceneObject) Method

Gets the number of renderers held by the sceneObject.

```csharp
public static int GetRendererCount(this Tizen.UI.Scene3D.SceneObject sceneObject);
```
#### Parameters

<a name='Tizen.UI.Scene3D.SceneObjectExtensions.GetRendererCount(thisTizen.UI.Scene3D.SceneObject).sceneObject'></a>

`sceneObject` [SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject')

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The number of renderers held by the sceneObject.

<a name='Tizen.UI.Scene3D.SceneObjectExtensions.RemoveRenderer(thisTizen.UI.Scene3D.SceneObject,Tizen.UI.Internal.Renderer)'></a>

## SceneObjectExtensions.RemoveRenderer(this SceneObject, Renderer) Method

Removes a specified renderer from the sceneObject.

```csharp
public static void RemoveRenderer(this Tizen.UI.Scene3D.SceneObject sceneObject, Tizen.UI.Internal.Renderer renderer);
```
#### Parameters

<a name='Tizen.UI.Scene3D.SceneObjectExtensions.RemoveRenderer(thisTizen.UI.Scene3D.SceneObject,Tizen.UI.Internal.Renderer).sceneObject'></a>

`sceneObject` [SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject')

<a name='Tizen.UI.Scene3D.SceneObjectExtensions.RemoveRenderer(thisTizen.UI.Scene3D.SceneObject,Tizen.UI.Internal.Renderer).renderer'></a>

`renderer` [Tizen.UI.Internal.Renderer](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Internal.Renderer 'Tizen.UI.Internal.Renderer')

The renderer to remove.





































