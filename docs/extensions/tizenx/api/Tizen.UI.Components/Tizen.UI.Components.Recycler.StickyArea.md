### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## StickyArea Class

Sticky area of RecyclerView.

```csharp
public class StickyArea : Tizen.UI.ViewGroup
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ViewGroup](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ViewGroup 'Tizen.UI.ViewGroup') &#129106; StickyArea
### Constructors

<a name='Tizen.UI.Components.Recycler.StickyArea.StickyArea(Tizen.UI.Components.Recycler.RecyclerView)'></a>

## StickyArea(RecyclerView) Constructor

Constructor of StickyArea.

```csharp
public StickyArea(Tizen.UI.Components.Recycler.RecyclerView recyclerView);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.StickyArea.StickyArea(Tizen.UI.Components.Recycler.RecyclerView).recyclerView'></a>

`recyclerView` [RecyclerView](Tizen.UI.Components.Recycler.RecyclerView.md 'Tizen.UI.Components.Recycler.RecyclerView')
### Methods

<a name='Tizen.UI.Components.Recycler.StickyArea.Add(Tizen.UI.Components.Recycler.ViewHolder)'></a>

## StickyArea.Add(ViewHolder) Method

Add the sticky item to the sticky area.

```csharp
public void Add(Tizen.UI.Components.Recycler.ViewHolder holder);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.StickyArea.Add(Tizen.UI.Components.Recycler.ViewHolder).holder'></a>

`holder` [ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')

The ViewHolder of the item to add.

<a name='Tizen.UI.Components.Recycler.StickyArea.CreatePrecedingStickyView(int)'></a>

## StickyArea.CreatePrecedingStickyView(int) Method

Create the preceding sticky view for the specified position. If there is no preceding sticky view, it returns null.

```csharp
public Tizen.UI.Components.Recycler.ViewHolder CreatePrecedingStickyView(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.StickyArea.CreatePrecedingStickyView(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position to create the preceding sticky view.

#### Returns
[ViewHolder](Tizen.UI.Components.Recycler.ViewHolder.md 'Tizen.UI.Components.Recycler.ViewHolder')  
The preceding sticky view for the specified position.

<a name='Tizen.UI.Components.Recycler.StickyArea.Has(int)'></a>

## StickyArea.Has(int) Method

Check if the position is in the sticky area. If it is, the item will be displayed as a sticky item.

```csharp
public bool Has(int position);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.StickyArea.Has(int).position'></a>

`position` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position to check.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the position is in the sticky area, otherwise false.

<a name='Tizen.UI.Components.Recycler.StickyArea.Initialize()'></a>

## StickyArea.Initialize() Method

Initialize the sticky area. It clears all the sticky items and resets the sticky area.

```csharp
public void Initialize();
```

<a name='Tizen.UI.Components.Recycler.StickyArea.Sync()'></a>

## StickyArea.Sync() Method

Sync the sticky area with the RecyclerView. It updates the sticky items based on the current scroll position.

```csharp
public void Sync();
```


























































