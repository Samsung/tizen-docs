### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## TwoWayBindingProperty&lt;TView,TValue> Class

This class represents a two-way binding property between a view and its value.

```csharp
public class TwoWayBindingProperty&lt;TView,TValue> : Tizen.UI.BindingProperty&lt;TView, TValue>
```
#### Type parameters

<a name='Tizen.UI.TwoWayBindingProperty_TView,TValue_.TView'></a>

`TView`

The type of the view.

<a name='Tizen.UI.TwoWayBindingProperty_TView,TValue_.TValue'></a>

`TValue`

The type of the value.

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.BindingProperty&lt;](Tizen.UI.BindingProperty_TView,TValue_.md 'Tizen.UI.BindingProperty&lt;TView,TValue>')[TView](Tizen.UI.TwoWayBindingProperty_TView,TValue_.md#Tizen.UI.TwoWayBindingProperty_TView,TValue_.TView 'Tizen.UI.TwoWayBindingProperty&lt;TView,TValue>.TView')[,](Tizen.UI.BindingProperty_TView,TValue_.md 'Tizen.UI.BindingProperty&lt;TView,TValue>')[TValue](Tizen.UI.TwoWayBindingProperty_TView,TValue_.md#Tizen.UI.TwoWayBindingProperty_TView,TValue_.TValue 'Tizen.UI.TwoWayBindingProperty&lt;TView,TValue>.TValue')[&gt;](Tizen.UI.BindingProperty_TView,TValue_.md 'Tizen.UI.BindingProperty&lt;TView,TValue>') &#129106; TwoWayBindingProperty&lt;TView,TValue>
### Properties

<a name='Tizen.UI.TwoWayBindingProperty_TView,TValue_.AddObserver'></a>

## TwoWayBindingProperty&lt;TView,TValue>.AddObserver Property

Gets or sets the action that adds an observer to the view.

```csharp
public System.Action&lt;TView,System.Action> AddObserver { get; set; }
```

#### Property Value
[System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[TView](Tizen.UI.TwoWayBindingProperty_TView,TValue_.md#Tizen.UI.TwoWayBindingProperty_TView,TValue_.TView 'Tizen.UI.TwoWayBindingProperty&lt;TView,TValue>.TView')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Action](https://docs.microsoft.com/en-us/dotnet/api/System.Action 'System.Action')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

<a name='Tizen.UI.TwoWayBindingProperty_TView,TValue_.Getter'></a>

## TwoWayBindingProperty&lt;TView,TValue>.Getter Property

Gets or sets the function that retrieves the value from the view.

```csharp
public System.Func&lt;TView,TValue> Getter { get; set; }
```

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[TView](Tizen.UI.TwoWayBindingProperty_TView,TValue_.md#Tizen.UI.TwoWayBindingProperty_TView,TValue_.TView 'Tizen.UI.TwoWayBindingProperty&lt;TView,TValue>.TView')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')[TValue](Tizen.UI.TwoWayBindingProperty_TView,TValue_.md#Tizen.UI.TwoWayBindingProperty_TView,TValue_.TValue 'Tizen.UI.TwoWayBindingProperty&lt;TView,TValue>.TValue')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-2 'System.Func`2')

<a name='Tizen.UI.TwoWayBindingProperty_TView,TValue_.RemoveObserver'></a>

## TwoWayBindingProperty&lt;TView,TValue>.RemoveObserver Property

Gets or sets the action that removes an observer from the view.

```csharp
public System.Action&lt;TView,System.Action> RemoveObserver { get; set; }
```

#### Property Value
[System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[TView](Tizen.UI.TwoWayBindingProperty_TView,TValue_.md#Tizen.UI.TwoWayBindingProperty_TView,TValue_.TView 'Tizen.UI.TwoWayBindingProperty&lt;TView,TValue>.TView')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Action](https://docs.microsoft.com/en-us/dotnet/api/System.Action 'System.Action')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')






