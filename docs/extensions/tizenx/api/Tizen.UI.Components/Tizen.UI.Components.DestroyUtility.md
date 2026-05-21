### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## DestroyUtility Class

Provides extension methods for disposables.

```csharp
public static class DestroyUtility
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; DestroyUtility
### Methods

<a name='Tizen.UI.Components.DestroyUtility.Destroy_T_(System.Collections.Generic.IEnumerable_T_)'></a>

## DestroyUtility.Destroy&lt;T>(IEnumerable&lt;T>) Method

Dispose all items in disposable list and make reference null.

```csharp
public static void Destroy&lt;T>(ref System.Collections.Generic.IEnumerable&lt;T> enumerable)
    where T : class, System.IDisposable;
```
#### Type parameters

<a name='Tizen.UI.Components.DestroyUtility.Destroy_T_(System.Collections.Generic.IEnumerable_T_).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.DestroyUtility.Destroy_T_(System.Collections.Generic.IEnumerable_T_).enumerable'></a>

`enumerable` [System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[T](Tizen.UI.Components.DestroyUtility.md#Tizen.UI.Components.DestroyUtility.Destroy_T_(System.Collections.Generic.IEnumerable_T_).T 'Tizen.UI.Components.DestroyUtility.Destroy&lt;T>(System.Collections.Generic.IEnumerable&lt;T>).T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')

<a name='Tizen.UI.Components.DestroyUtility.Destroy_T_(T)'></a>

## DestroyUtility.Destroy&lt;T>(T) Method

Dispose a disposable and make reference null.

```csharp
public static void Destroy&lt;T>(ref T disposable)
    where T : class, System.IDisposable;
```
#### Type parameters

<a name='Tizen.UI.Components.DestroyUtility.Destroy_T_(T).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.DestroyUtility.Destroy_T_(T).disposable'></a>

`disposable` [T](Tizen.UI.Components.DestroyUtility.md#Tizen.UI.Components.DestroyUtility.Destroy_T_(T).T 'Tizen.UI.Components.DestroyUtility.Destroy&lt;T>(T).T')

<a name='Tizen.UI.Components.DestroyUtility.Destroy_T_(thisSystem.Collections.Generic.IEnumerable_T_)'></a>

## DestroyUtility.Destroy&lt;T>(this IEnumerable&lt;T>) Method

Dispose all items in disposable list.

```csharp
public static void Destroy&lt;T>(this System.Collections.Generic.IEnumerable&lt;T> enumerable)
    where T : class, System.IDisposable;
```
#### Type parameters

<a name='Tizen.UI.Components.DestroyUtility.Destroy_T_(thisSystem.Collections.Generic.IEnumerable_T_).T'></a>

`T`
#### Parameters

<a name='Tizen.UI.Components.DestroyUtility.Destroy_T_(thisSystem.Collections.Generic.IEnumerable_T_).enumerable'></a>

`enumerable` [System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[T](Tizen.UI.Components.DestroyUtility.md#Tizen.UI.Components.DestroyUtility.Destroy_T_(thisSystem.Collections.Generic.IEnumerable_T_).T 'Tizen.UI.Components.DestroyUtility.Destroy&lt;T>(this System.Collections.Generic.IEnumerable&lt;T>).T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')


























































