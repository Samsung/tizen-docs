### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## ViewTemplateSelector Class

This class represents a view template selector used to create reusable view

```csharp
public abstract class ViewTemplateSelector : Tizen.UI.ViewTemplate
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.Template&lt;](Tizen.UI.Template_T_.md 'Tizen.UI.Template&lt;T>')[View](Tizen.UI.View.md 'Tizen.UI.View')[&gt;](Tizen.UI.Template_T_.md 'Tizen.UI.Template&lt;T>') &#129106; [ViewTemplate](Tizen.UI.ViewTemplate.md 'Tizen.UI.ViewTemplate') &#129106; ViewTemplateSelector
### Methods

<a name='Tizen.UI.ViewTemplateSelector.SelectTemplate(object,Tizen.UI.View)'></a>

## ViewTemplateSelector.SelectTemplate(object, View) Method

Selects the appropriate view template for the specified object based on some custom logic.

```csharp
public Tizen.UI.ViewTemplate SelectTemplate(object item, Tizen.UI.View container);
```
#### Parameters

<a name='Tizen.UI.ViewTemplateSelector.SelectTemplate(object,Tizen.UI.View).item'></a>

`item` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

An object that represents the item being templated.

<a name='Tizen.UI.ViewTemplateSelector.SelectTemplate(object,Tizen.UI.View).container'></a>

`container` [View](Tizen.UI.View.md 'Tizen.UI.View')

A [View](Tizen.UI.View.md 'Tizen.UI.View') that is the container in which the template will be applied.

#### Returns
[ViewTemplate](Tizen.UI.ViewTemplate.md 'Tizen.UI.ViewTemplate')  
A [ViewTemplate](Tizen.UI.ViewTemplate.md 'Tizen.UI.ViewTemplate') instance that represents the selected template for the specified object.




