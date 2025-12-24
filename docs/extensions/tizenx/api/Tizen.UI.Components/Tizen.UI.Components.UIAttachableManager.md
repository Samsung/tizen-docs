### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## UIAttachableManager Class

Manages attachable data on views.

```csharp
public static class UIAttachableManager
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; UIAttachableManager
### Fields

<a name='Tizen.UI.Components.UIAttachableManager.DisabledEffectKey'></a>

## UIAttachableManager.DisabledEffectKey Field

The key used to attach disabled effect data to a view.

```csharp
public static readonly string DisabledEffectKey;
```

#### Field Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.UIAttachableManager.SoundEffectKey'></a>

## UIAttachableManager.SoundEffectKey Field

The key used to attach sound effect data to a view.

```csharp
public static readonly string SoundEffectKey;
```

#### Field Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.UIAttachableManager.TouchEffectKey'></a>

## UIAttachableManager.TouchEffectKey Field

The key used to attach touch effect data to a view.

```csharp
public static readonly string TouchEffectKey;
```

#### Field Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')
### Methods

<a name='Tizen.UI.Components.UIAttachableManager.Attach(thisTizen.UI.View,string,Tizen.UI.Components.UIAttachable)'></a>

## UIAttachableManager.Attach(this View, string, UIAttachable) Method

Attaches data to a view. If there is already an attachable with the same key, it will be replaced.

```csharp
public static void Attach(this Tizen.UI.View view, string key, Tizen.UI.Components.UIAttachable attachable);
```
#### Parameters

<a name='Tizen.UI.Components.UIAttachableManager.Attach(thisTizen.UI.View,string,Tizen.UI.Components.UIAttachable).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view to attach data to.

<a name='Tizen.UI.Components.UIAttachableManager.Attach(thisTizen.UI.View,string,Tizen.UI.Components.UIAttachable).key'></a>

`key` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The key of the attachable.

<a name='Tizen.UI.Components.UIAttachableManager.Attach(thisTizen.UI.View,string,Tizen.UI.Components.UIAttachable).attachable'></a>

`attachable` [UIAttachable](Tizen.UI.Components.UIAttachable.md 'Tizen.UI.Components.UIAttachable')

The attachable data to attach.

#### Exceptions

[System.ArgumentNullException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentNullException 'System.ArgumentNullException')  
Thrown when view or attachable is null.

[System.ArgumentException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentException 'System.ArgumentException')  
Thrown when key is null or empty.

<a name='Tizen.UI.Components.UIAttachableManager.ClearAttachables(thisTizen.UI.View)'></a>

## UIAttachableManager.ClearAttachables(this View) Method

Clears all attached data from a view.

```csharp
public static void ClearAttachables(this Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.Components.UIAttachableManager.ClearAttachables(thisTizen.UI.View).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view to clear data from.

<a name='Tizen.UI.Components.UIAttachableManager.Detach(thisTizen.UI.View,string)'></a>

## UIAttachableManager.Detach(this View, string) Method

Detaches data from a view. If there is no attachable with the given key, nothing happens.

```csharp
public static void Detach(this Tizen.UI.View view, string key);
```
#### Parameters

<a name='Tizen.UI.Components.UIAttachableManager.Detach(thisTizen.UI.View,string).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view to detach data from.

<a name='Tizen.UI.Components.UIAttachableManager.Detach(thisTizen.UI.View,string).key'></a>

`key` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The key of the attachable to detach.

#### Exceptions

[System.ArgumentNullException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentNullException 'System.ArgumentNullException')  
Thrown when view is null.

[System.ArgumentException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentException 'System.ArgumentException')  
Thrown when key is null or empty.

<a name='Tizen.UI.Components.UIAttachableManager.GetAttachable(thisTizen.UI.View,string)'></a>

## UIAttachableManager.GetAttachable(this View, string) Method

Gets the currently attached data for a view.

```csharp
public static Tizen.UI.Components.UIAttachable GetAttachable(this Tizen.UI.View view, string key);
```
#### Parameters

<a name='Tizen.UI.Components.UIAttachableManager.GetAttachable(thisTizen.UI.View,string).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view to get data from.

<a name='Tizen.UI.Components.UIAttachableManager.GetAttachable(thisTizen.UI.View,string).key'></a>

`key` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The key of the attachable to get.

#### Returns
[UIAttachable](Tizen.UI.Components.UIAttachable.md 'Tizen.UI.Components.UIAttachable')


























































