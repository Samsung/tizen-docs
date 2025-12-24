### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## INavigation Interface

The INavigation interface defines methods to navigate views with the stack data structure.

```csharp
public interface INavigation
```

Derived  
&#8627; [Navigator](Tizen.UI.Components.Navigator.md 'Tizen.UI.Components.Navigator')
### Properties

<a name='Tizen.UI.Components.INavigation.ModalStack'></a>

## INavigation.ModalStack Property

Gets the list of views pushed onto the modal stack.

```csharp
System.Collections.Generic.IReadOnlyList&lt;Tizen.UI.View> ModalStack { get; }
```

#### Property Value
[System.Collections.Generic.IReadOnlyList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyList-1 'System.Collections.Generic.IReadOnlyList`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyList-1 'System.Collections.Generic.IReadOnlyList`1')

<a name='Tizen.UI.Components.INavigation.NavigationStack'></a>

## INavigation.NavigationStack Property

Gets the list of views pushed onto the navigation stack.

```csharp
System.Collections.Generic.IReadOnlyList&lt;Tizen.UI.View> NavigationStack { get; }
```

#### Property Value
[System.Collections.Generic.IReadOnlyList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyList-1 'System.Collections.Generic.IReadOnlyList`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyList-1 'System.Collections.Generic.IReadOnlyList`1')
### Methods

<a name='Tizen.UI.Components.INavigation.InsertBefore(Tizen.UI.View,Tizen.UI.View)'></a>

## INavigation.InsertBefore(View, View) Method

Inserts a view to the navigation stack right before the given view `before`.

```csharp
void InsertBefore(Tizen.UI.View view, Tizen.UI.View before);
```
#### Parameters

<a name='Tizen.UI.Components.INavigation.InsertBefore(Tizen.UI.View,Tizen.UI.View).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view to be inserted to the navigation stack right before the given view `before`.

<a name='Tizen.UI.Components.INavigation.InsertBefore(Tizen.UI.View,Tizen.UI.View).before'></a>

`before` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view existing in the navigation stack and will be the next view of the inserted view.

<a name='Tizen.UI.Components.INavigation.NavigateBack()'></a>

## INavigation.NavigateBack() Method

Navigate back to the previous view.

```csharp
bool NavigateBack();
```

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the navigation back was handled, otherwise false.

<a name='Tizen.UI.Components.INavigation.PopAsync()'></a>

## INavigation.PopAsync() Method

Pops the top view off the navigation stack.

```csharp
System.Threading.Tasks.Task&lt;Tizen.UI.View> PopAsync();
```

#### Returns
[System.Threading.Tasks.Task&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')  
The view popped off the navigation stack.

<a name='Tizen.UI.Components.INavigation.PopAsync(bool)'></a>

## INavigation.PopAsync(bool) Method

Pops the top view off the navigation stack with or without the transition animation.

```csharp
System.Threading.Tasks.Task&lt;Tizen.UI.View> PopAsync(bool animated);
```
#### Parameters

<a name='Tizen.UI.Components.INavigation.PopAsync(bool).animated'></a>

`animated` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True to play the transition animation during navigation.

#### Returns
[System.Threading.Tasks.Task&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')  
The view popped off the navigation stack.

<a name='Tizen.UI.Components.INavigation.PopModalAsync()'></a>

## INavigation.PopModalAsync() Method

Pops the top modal view such as dialog off the modal stack.

```csharp
System.Threading.Tasks.Task&lt;Tizen.UI.View> PopModalAsync();
```

#### Returns
[System.Threading.Tasks.Task&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')  
The modal view popped off the modal stack.

<a name='Tizen.UI.Components.INavigation.PopModalAsync(bool)'></a>

## INavigation.PopModalAsync(bool) Method

Pops the top modal view such as dialog off the modal stack with or without the transition animation.

```csharp
System.Threading.Tasks.Task&lt;Tizen.UI.View> PopModalAsync(bool animated);
```
#### Parameters

<a name='Tizen.UI.Components.INavigation.PopModalAsync(bool).animated'></a>

`animated` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True to play the transition animation during navigation.

#### Returns
[System.Threading.Tasks.Task&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')  
The modal view popped off the modal stack.

<a name='Tizen.UI.Components.INavigation.PushAsync(Tizen.UI.View)'></a>

## INavigation.PushAsync(View) Method

Pushes a view onto the navigation stack.

```csharp
System.Threading.Tasks.Task PushAsync(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.Components.INavigation.PushAsync(Tizen.UI.View).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view to be pushed onto the navigation stack.

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')

<a name='Tizen.UI.Components.INavigation.PushAsync(Tizen.UI.View,bool)'></a>

## INavigation.PushAsync(View, bool) Method

Pushes a view onto the navigation stack with or without the transition animation.

```csharp
System.Threading.Tasks.Task PushAsync(Tizen.UI.View view, bool animated);
```
#### Parameters

<a name='Tizen.UI.Components.INavigation.PushAsync(Tizen.UI.View,bool).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view to be pushed onto the navigation stack.

<a name='Tizen.UI.Components.INavigation.PushAsync(Tizen.UI.View,bool).animated'></a>

`animated` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True to play the transition animation during navigation.

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')

<a name='Tizen.UI.Components.INavigation.PushModalAsync(Tizen.UI.View)'></a>

## INavigation.PushModalAsync(View) Method

Pushes a modal view such as dialog onto the modal stack.

```csharp
System.Threading.Tasks.Task PushModalAsync(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.Components.INavigation.PushModalAsync(Tizen.UI.View).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view to be pushed onto the modal stack.

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')

<a name='Tizen.UI.Components.INavigation.PushModalAsync(Tizen.UI.View,bool)'></a>

## INavigation.PushModalAsync(View, bool) Method

Pushes a modal view such as dialog onto the modal stack with or without the transition animation.

```csharp
System.Threading.Tasks.Task PushModalAsync(Tizen.UI.View view, bool animated);
```
#### Parameters

<a name='Tizen.UI.Components.INavigation.PushModalAsync(Tizen.UI.View,bool).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view to be pushed onto the modal stack.

<a name='Tizen.UI.Components.INavigation.PushModalAsync(Tizen.UI.View,bool).animated'></a>

`animated` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True to play the transition animation during navigation.

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')

<a name='Tizen.UI.Components.INavigation.Remove(Tizen.UI.View)'></a>

## INavigation.Remove(View) Method

Removes the specified view from the navigation stack or modal stack.

```csharp
void Remove(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.Components.INavigation.Remove(Tizen.UI.View).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view to be removed from the navigation stack or modal stack.


























































