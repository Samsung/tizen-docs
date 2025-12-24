### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## ViewTemplate Class

This class represents a view template used to create reusable views.

```csharp
public class ViewTemplate : Tizen.UI.Template&lt;Tizen.UI.View>
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.Template&lt;](Tizen.UI.Template_T_.md 'Tizen.UI.Template&lt;T>')[View](Tizen.UI.View.md 'Tizen.UI.View')[&gt;](Tizen.UI.Template_T_.md 'Tizen.UI.Template&lt;T>') &#129106; ViewTemplate

Derived  
&#8627; [ViewTemplateSelector](Tizen.UI.ViewTemplateSelector.md 'Tizen.UI.ViewTemplateSelector')
### Constructors

<a name='Tizen.UI.ViewTemplate.ViewTemplate(System.Func_Tizen.UI.View_)'></a>

## ViewTemplate(Func&lt;View>) Constructor

Constructor for the ViewTemplate class that takes a loadTemplate function parameter.

```csharp
public ViewTemplate(System.Func&lt;Tizen.UI.View> loadTemplate);
```
#### Parameters

<a name='Tizen.UI.ViewTemplate.ViewTemplate(System.Func_Tizen.UI.View_).loadTemplate'></a>

`loadTemplate` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')[View](Tizen.UI.View.md 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')

A function that returns a [View](Tizen.UI.View.md 'Tizen.UI.View') instance.

<a name='Tizen.UI.ViewTemplate.ViewTemplate(System.Type)'></a>

## ViewTemplate(Type) Constructor

Constructor for the ViewTemplate class that takes a type parameter and creates a view instance from the given type.

```csharp
public ViewTemplate(System.Type type);
```
#### Parameters

<a name='Tizen.UI.ViewTemplate.ViewTemplate(System.Type).type'></a>

`type` [System.Type](https://docs.microsoft.com/en-us/dotnet/api/System.Type 'System.Type')

The type of the view that the template will generate.




