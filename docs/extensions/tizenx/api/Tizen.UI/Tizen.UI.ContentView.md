### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## ContentView Class

ContentView is a view that displays body view as its content.

```csharp
public class ContentView : Tizen.UI.View,
Tizen.UI.IParentObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; [View](Tizen.UI.View.md 'Tizen.UI.View') &#129106; ContentView

Implements [IParentObject](Tizen.UI.IParentObject.md 'Tizen.UI.IParentObject')
### Constructors

<a name='Tizen.UI.ContentView.ContentView()'></a>

## ContentView() Constructor

Creates an instance of a ContentView.

```csharp
public ContentView();
```
### Methods

<a name='Tizen.UI.ContentView.Measure(float,float)'></a>

## ContentView.Measure(float, float) Method

Measures the size requirements of the view for the given constraints.

```csharp
public override Tizen.UI.Size Measure(float availableWidth, float availableHeight);
```
#### Parameters

<a name='Tizen.UI.ContentView.Measure(float,float).availableWidth'></a>

`availableWidth` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available width for the view.

<a name='Tizen.UI.ContentView.Measure(float,float).availableHeight'></a>

`availableHeight` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available height for the view.

#### Returns
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')  
The measured size requirements of the view.






