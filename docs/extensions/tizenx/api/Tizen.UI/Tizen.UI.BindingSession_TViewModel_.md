### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## BindingSession&lt;TViewModel> Class

BindingSession class provides a mechanism for binding properties of a view model to a view.

```csharp
public class BindingSession&lt;TViewModel> :
System.ComponentModel.INotifyPropertyChanged,
System.IDisposable
```
#### Type parameters

<a name='Tizen.UI.BindingSession_TViewModel_.TViewModel'></a>

`TViewModel`

The type of the view model.

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; BindingSession&lt;TViewModel>

Implements [System.ComponentModel.INotifyPropertyChanged](https://docs.microsoft.com/en-us/dotnet/api/System.ComponentModel.INotifyPropertyChanged 'System.ComponentModel.INotifyPropertyChanged'), [System.IDisposable](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable 'System.IDisposable')
### Properties

<a name='Tizen.UI.BindingSession_TViewModel_.ViewModel'></a>

## BindingSession&lt;TViewModel>.ViewModel Property

Gets or sets the view model.

```csharp
public TViewModel ViewModel { get; set; }
```

#### Property Value
[TViewModel](Tizen.UI.BindingSession_TViewModel_.md#Tizen.UI.BindingSession_TViewModel_.TViewModel 'Tizen.UI.BindingSession&lt;TViewModel>.TViewModel')
### Methods

<a name='Tizen.UI.BindingSession_TViewModel_.AddBinding(System.Action_TViewModel_,string)'></a>

## BindingSession&lt;TViewModel>.AddBinding(Action&lt;TViewModel>, string) Method

Adds a binding between a property of the view model and a property of the view.

```csharp
public void AddBinding(System.Action&lt;TViewModel> setter, string path);
```
#### Parameters

<a name='Tizen.UI.BindingSession_TViewModel_.AddBinding(System.Action_TViewModel_,string).setter'></a>

`setter` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')[TViewModel](Tizen.UI.BindingSession_TViewModel_.md#Tizen.UI.BindingSession_TViewModel_.TViewModel 'Tizen.UI.BindingSession&lt;TViewModel>.TViewModel')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')

The setter method of the view.

<a name='Tizen.UI.BindingSession_TViewModel_.AddBinding(System.Action_TViewModel_,string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path of the property to bind.

<a name='Tizen.UI.BindingSession_TViewModel_.AddTwoWayBinding_T_(System.Action_System.Action_,System.Action_System.Action_,System.Action_TViewModel_,System.Func_T_,string)'></a>

## BindingSession&lt;TViewModel>.AddTwoWayBinding&lt;T>(Action&lt;Action>, Action&lt;Action>, Action&lt;TViewModel>, Func&lt;T>, string) Method

Adds a two-way binding between a property of the view model and a property of the view.

```csharp
public void AddTwoWayBinding&lt;T>(System.Action&lt;System.Action> register, System.Action&lt;System.Action> unregister, System.Action&lt;TViewModel> setter, System.Func&lt;T> getter, string path);
```
#### Type parameters

<a name='Tizen.UI.BindingSession_TViewModel_.AddTwoWayBinding_T_(System.Action_System.Action_,System.Action_System.Action_,System.Action_TViewModel_,System.Func_T_,string).T'></a>

`T`

The type of the property to bind.
#### Parameters

<a name='Tizen.UI.BindingSession_TViewModel_.AddTwoWayBinding_T_(System.Action_System.Action_,System.Action_System.Action_,System.Action_TViewModel_,System.Func_T_,string).register'></a>

`register` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')[System.Action](https://docs.microsoft.com/en-us/dotnet/api/System.Action 'System.Action')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')

The registration method of the observer.

<a name='Tizen.UI.BindingSession_TViewModel_.AddTwoWayBinding_T_(System.Action_System.Action_,System.Action_System.Action_,System.Action_TViewModel_,System.Func_T_,string).unregister'></a>

`unregister` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')[System.Action](https://docs.microsoft.com/en-us/dotnet/api/System.Action 'System.Action')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')

The unregistration method of the observer.

<a name='Tizen.UI.BindingSession_TViewModel_.AddTwoWayBinding_T_(System.Action_System.Action_,System.Action_System.Action_,System.Action_TViewModel_,System.Func_T_,string).setter'></a>

`setter` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')[TViewModel](Tizen.UI.BindingSession_TViewModel_.md#Tizen.UI.BindingSession_TViewModel_.TViewModel 'Tizen.UI.BindingSession&lt;TViewModel>.TViewModel')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')

The setter method of the view.

<a name='Tizen.UI.BindingSession_TViewModel_.AddTwoWayBinding_T_(System.Action_System.Action_,System.Action_System.Action_,System.Action_TViewModel_,System.Func_T_,string).getter'></a>

`getter` [System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')[T](Tizen.UI.BindingSession_TViewModel_.md#Tizen.UI.BindingSession_TViewModel_.AddTwoWayBinding_T_(System.Action_System.Action_,System.Action_System.Action_,System.Action_TViewModel_,System.Func_T_,string).T 'Tizen.UI.BindingSession&lt;TViewModel>.AddTwoWayBinding&lt;T>(System.Action&lt;System.Action>, System.Action&lt;System.Action>, System.Action&lt;TViewModel>, System.Func&lt;T>, string).T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-1 'System.Func`1')

The getter method of the view.

<a name='Tizen.UI.BindingSession_TViewModel_.AddTwoWayBinding_T_(System.Action_System.Action_,System.Action_System.Action_,System.Action_TViewModel_,System.Func_T_,string).path'></a>

`path` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path of the property to bind.

<a name='Tizen.UI.BindingSession_TViewModel_.ClearBinding()'></a>

## BindingSession&lt;TViewModel>.ClearBinding() Method

Clears all bindings.

```csharp
public void ClearBinding();
```

<a name='Tizen.UI.BindingSession_TViewModel_.Dispose()'></a>

## BindingSession&lt;TViewModel>.Dispose() Method

Releases all resources used by the current instance of the BindingSession class.

```csharp
public void Dispose();
```

Implements [Dispose()](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable.Dispose 'System.IDisposable.Dispose')

<a name='Tizen.UI.BindingSession_TViewModel_.GetValue(string)'></a>

## BindingSession&lt;TViewModel>.GetValue(string) Method

Gets the value of a property of the view model.

```csharp
public object GetValue(string name);
```
#### Parameters

<a name='Tizen.UI.BindingSession_TViewModel_.GetValue(string).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the property.

#### Returns
[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')  
The value of the property.

<a name='Tizen.UI.BindingSession_TViewModel_.SetValue(object,string)'></a>

## BindingSession&lt;TViewModel>.SetValue(object, string) Method

Sets the value of a property of the view model.

```csharp
public void SetValue(object obj, string name);
```
#### Parameters

<a name='Tizen.UI.BindingSession_TViewModel_.SetValue(object,string).obj'></a>

`obj` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The value to set.

<a name='Tizen.UI.BindingSession_TViewModel_.SetValue(object,string).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the property.

<a name='Tizen.UI.BindingSession_TViewModel_.UpdateViewModel()'></a>

## BindingSession&lt;TViewModel>.UpdateViewModel() Method

Updates the view model.

```csharp
public void UpdateViewModel();
```

<a name='Tizen.UI.BindingSession_TViewModel_.UpdateViewModel(TViewModel)'></a>

## BindingSession&lt;TViewModel>.UpdateViewModel(TViewModel) Method

Updates the view model.

```csharp
public void UpdateViewModel(TViewModel vm);
```
#### Parameters

<a name='Tizen.UI.BindingSession_TViewModel_.UpdateViewModel(TViewModel).vm'></a>

`vm` [TViewModel](Tizen.UI.BindingSession_TViewModel_.md#Tizen.UI.BindingSession_TViewModel_.TViewModel 'Tizen.UI.BindingSession&lt;TViewModel>.TViewModel')

The view model to update.
### Events

<a name='Tizen.UI.BindingSession_TViewModel_.PropertyChanged'></a>

## BindingSession&lt;TViewModel>.PropertyChanged Event

Represents an event that is raised when a property value changes.

```csharp
public event PropertyChangedEventHandler PropertyChanged;
```

Implements [PropertyChanged](https://docs.microsoft.com/en-us/dotnet/api/System.ComponentModel.INotifyPropertyChanged.PropertyChanged 'System.ComponentModel.INotifyPropertyChanged.PropertyChanged')

#### Event Type
[System.ComponentModel.PropertyChangedEventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.ComponentModel.PropertyChangedEventHandler 'System.ComponentModel.PropertyChangedEventHandler')






