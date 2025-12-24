### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## Navigator Class

Navigator is a container class that supports view navigation with the stack data structure.  
Navigator manages two types of stacks, navigation stack and modal stack.  
The modal stack contains modal views such as dialog.  
The navigation stack contains the rest of the views.  
The views in the modal stack are above the views in the navigation stack.  
Views pushed by the modal methods such as [PushModalAsync(View)](Tizen.UI.Components.Navigator.md#Tizen.UI.Components.Navigator.PushModalAsync(Tizen.UI.View) 'Tizen.UI.Components.Navigator.PushModalAsync(Tizen.UI.View)') are pushed onto the modal stack as modal views.

```csharp
public class Navigator : Tizen.UI.ContentView,
Tizen.UI.Components.INavigation,
Tizen.UI.Components.INavigationAnimation,
Tizen.UI.Components.INavigateBackHandler,
Tizen.UI.Components.INavigationTransition
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; Navigator

Implements [INavigation](Tizen.UI.Components.INavigation.md 'Tizen.UI.Components.INavigation'), [INavigationAnimation](Tizen.UI.Components.INavigationAnimation.md 'Tizen.UI.Components.INavigationAnimation'), [INavigateBackHandler](Tizen.UI.Components.INavigateBackHandler.md 'Tizen.UI.Components.INavigateBackHandler'), [INavigationTransition](Tizen.UI.Components.INavigationTransition.md 'Tizen.UI.Components.INavigationTransition')
### Constructors

<a name='Tizen.UI.Components.Navigator.Navigator()'></a>

## Navigator() Constructor

Constructor for the Navigator class.

```csharp
public Navigator();
```
### Properties

<a name='Tizen.UI.Components.Navigator.CurrentView'></a>

## Navigator.CurrentView Property

Gets the top view from the navigation stack and the modal stack.

```csharp
public Tizen.UI.View CurrentView { get; }
```

#### Property Value
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

<a name='Tizen.UI.Components.Navigator.ModalStack'></a>

## Navigator.ModalStack Property

Gets the list of views pushed onto the modal stack.  
[PushModalAsync(View)](Tizen.UI.Components.Navigator.md#Tizen.UI.Components.Navigator.PushModalAsync(Tizen.UI.View) 'Tizen.UI.Components.Navigator.PushModalAsync(Tizen.UI.View)') pushes a view onto the modal stack.  
[PopModalAsync()](Tizen.UI.Components.Navigator.md#Tizen.UI.Components.Navigator.PopModalAsync() 'Tizen.UI.Components.Navigator.PopModalAsync()') pops a view off the modal stack.

```csharp
public System.Collections.Generic.IReadOnlyList&lt;Tizen.UI.View> ModalStack { get; }
```

Implements [ModalStack](Tizen.UI.Components.INavigation.md#Tizen.UI.Components.INavigation.ModalStack 'Tizen.UI.Components.INavigation.ModalStack')

#### Property Value
[System.Collections.Generic.IReadOnlyList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyList-1 'System.Collections.Generic.IReadOnlyList`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyList-1 'System.Collections.Generic.IReadOnlyList`1')

<a name='Tizen.UI.Components.Navigator.NavigationStack'></a>

## Navigator.NavigationStack Property

Gets the list of views pushed onto the navigation stack.  
[PushAsync(View)](Tizen.UI.Components.Navigator.md#Tizen.UI.Components.Navigator.PushAsync(Tizen.UI.View) 'Tizen.UI.Components.Navigator.PushAsync(Tizen.UI.View)') pushes a view onto the navigation stack.  
[InsertBefore(View, View)](Tizen.UI.Components.Navigator.md#Tizen.UI.Components.Navigator.InsertBefore(Tizen.UI.View,Tizen.UI.View) 'Tizen.UI.Components.Navigator.InsertBefore(Tizen.UI.View, Tizen.UI.View)') inserts a view to the navigation stack.  
[PopAsync()](Tizen.UI.Components.Navigator.md#Tizen.UI.Components.Navigator.PopAsync() 'Tizen.UI.Components.Navigator.PopAsync()') pops a view off the navigation stack.  
[Remove(View)](Tizen.UI.Components.Navigator.md#Tizen.UI.Components.Navigator.Remove(Tizen.UI.View) 'Tizen.UI.Components.Navigator.Remove(Tizen.UI.View)') removes a view from the navigation stack.

```csharp
public System.Collections.Generic.IReadOnlyList&lt;Tizen.UI.View> NavigationStack { get; }
```

Implements [NavigationStack](Tizen.UI.Components.INavigation.md#Tizen.UI.Components.INavigation.NavigationStack 'Tizen.UI.Components.INavigation.NavigationStack')

#### Property Value
[System.Collections.Generic.IReadOnlyList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyList-1 'System.Collections.Generic.IReadOnlyList`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyList-1 'System.Collections.Generic.IReadOnlyList`1')

<a name='Tizen.UI.Components.Navigator.PopAnimation'></a>

## Navigator.PopAnimation Property

```csharp
public System.Func&lt;Tizen.UI.View,Tizen.UI.View,Tizen.UI.Components.INavigationAnimationController> PopAnimation { get; }
```

Implements [PopAnimation](Tizen.UI.Components.INavigationAnimation.md#Tizen.UI.Components.INavigationAnimation.PopAnimation 'Tizen.UI.Components.INavigationAnimation.PopAnimation')

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[INavigationAnimationController](Tizen.UI.Components.INavigationAnimationController.md 'Tizen.UI.Components.INavigationAnimationController')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')

<a name='Tizen.UI.Components.Navigator.PopModalAnimation'></a>

## Navigator.PopModalAnimation Property

Function called for transition animation when INavigation.PopModalAsync is called.  
If a view implements this function, Navigator calls the view's function instead of the default transition animation for modal pop.  
Function's first parameter View is the view which will appear on the screen.  
Function's second parameter View is the view which will disappear on the screen.  
Function's return value is the navigation animation controller which supports PlayAsync and Stop.

```csharp
public System.Func&lt;Tizen.UI.View,Tizen.UI.View,Tizen.UI.Components.INavigationAnimationController> PopModalAnimation { get; }
```

Implements [PopModalAnimation](Tizen.UI.Components.INavigationAnimation.md#Tizen.UI.Components.INavigationAnimation.PopModalAnimation 'Tizen.UI.Components.INavigationAnimation.PopModalAnimation')

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[INavigationAnimationController](Tizen.UI.Components.INavigationAnimationController.md 'Tizen.UI.Components.INavigationAnimationController')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')

<a name='Tizen.UI.Components.Navigator.PushAnimation'></a>

## Navigator.PushAnimation Property

Function called for transition animation when INavigation.PushAsync is called.  
If a view implements this function, Navigator calls the view's function instead of the default transition animation for navigation push.  
Function's first parameter View is the view which will appear on the screen.  
Function's second parameter View is the view which will disappear on the screen.  
Function's return value is the navigation animation controller which supports PlayAsync and Stop.

```csharp
public System.Func&lt;Tizen.UI.View,Tizen.UI.View,Tizen.UI.Components.INavigationAnimationController> PushAnimation { get; }
```

Implements [PushAnimation](Tizen.UI.Components.INavigationAnimation.md#Tizen.UI.Components.INavigationAnimation.PushAnimation 'Tizen.UI.Components.INavigationAnimation.PushAnimation')

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[INavigationAnimationController](Tizen.UI.Components.INavigationAnimationController.md 'Tizen.UI.Components.INavigationAnimationController')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')

<a name='Tizen.UI.Components.Navigator.PushModalAnimation'></a>

## Navigator.PushModalAnimation Property

Function called for transition animation when INavigation.PushModalAsync is called.  
If a view implements this function, Navigator calls the view's function instead of the default transition animation for modal push.  
Function's first parameter View is the view which will appear on the screen.  
Function's second parameter View is the view which will disappear on the screen.  
Function's return value is the navigation animation controller which supports PlayAsync and Stop.

```csharp
public System.Func&lt;Tizen.UI.View,Tizen.UI.View,Tizen.UI.Components.INavigationAnimationController> PushModalAnimation { get; }
```

Implements [PushModalAnimation](Tizen.UI.Components.INavigationAnimation.md#Tizen.UI.Components.INavigationAnimation.PushModalAnimation 'Tizen.UI.Components.INavigationAnimation.PushModalAnimation')

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[INavigationAnimationController](Tizen.UI.Components.INavigationAnimationController.md 'Tizen.UI.Components.INavigationAnimationController')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')
### Methods

<a name='Tizen.UI.Components.Navigator.DidAppear(bool)'></a>

## Navigator.DidAppear(bool) Method

Called right after appearing by navigation transition.

```csharp
public virtual void DidAppear(bool byPopNavigation);
```
#### Parameters

<a name='Tizen.UI.Components.Navigator.DidAppear(bool).byPopNavigation'></a>

`byPopNavigation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

If true, it is called by pop navigation.

Implements [DidAppear(bool)](Tizen.UI.Components.INavigationTransition.md#Tizen.UI.Components.INavigationTransition.DidAppear(bool) 'Tizen.UI.Components.INavigationTransition.DidAppear(bool)')

<a name='Tizen.UI.Components.Navigator.DidDisappear(bool)'></a>

## Navigator.DidDisappear(bool) Method

Called right after disappearing by navigation transition.

```csharp
public virtual void DidDisappear(bool byPopNavigation);
```
#### Parameters

<a name='Tizen.UI.Components.Navigator.DidDisappear(bool).byPopNavigation'></a>

`byPopNavigation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

If true, it is called by pop navigation.

Implements [DidDisappear(bool)](Tizen.UI.Components.INavigationTransition.md#Tizen.UI.Components.INavigationTransition.DidDisappear(bool) 'Tizen.UI.Components.INavigationTransition.DidDisappear(bool)')

### Remarks
A view disappeared by pop navigation can be disposed if the view is not used anymore.

<a name='Tizen.UI.Components.Navigator.InsertBefore(Tizen.UI.View,Tizen.UI.View)'></a>

## Navigator.InsertBefore(View, View) Method

Inserts a view to the navigation stack right before the given view `before`.

```csharp
public void InsertBefore(Tizen.UI.View view, Tizen.UI.View before);
```
#### Parameters

<a name='Tizen.UI.Components.Navigator.InsertBefore(Tizen.UI.View,Tizen.UI.View).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view to be inserted to the navigation stack right before the given view `before`.

<a name='Tizen.UI.Components.Navigator.InsertBefore(Tizen.UI.View,Tizen.UI.View).before'></a>

`before` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view existing in the navigation stack and will be the next view of the inserted view.

Implements [InsertBefore(View, View)](Tizen.UI.Components.INavigation.md#Tizen.UI.Components.INavigation.InsertBefore(Tizen.UI.View,Tizen.UI.View) 'Tizen.UI.Components.INavigation.InsertBefore(Tizen.UI.View, Tizen.UI.View)')

#### Exceptions

[System.ArgumentNullException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentNullException 'System.ArgumentNullException')  
Thrown if `view` is null.

[System.ArgumentNullException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentNullException 'System.ArgumentNullException')  
Thrown if `before` is null.

[System.ArgumentException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentException 'System.ArgumentException')  
Thrown if `before` does not exist in the navigation stack.

<a name='Tizen.UI.Components.Navigator.NavigateBack()'></a>

## Navigator.NavigateBack() Method

Navigate back to the previous view.

```csharp
public bool NavigateBack();
```

Implements [NavigateBack()](Tizen.UI.Components.INavigation.md#Tizen.UI.Components.INavigation.NavigateBack() 'Tizen.UI.Components.INavigation.NavigateBack()')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the navigation back was handled, otherwise false.

<a name='Tizen.UI.Components.Navigator.PopAsync()'></a>

## Navigator.PopAsync() Method

Pops the top view off the navigation stack.  
After this method is finished, the previous top view in the navigation stack becomes visible.

```csharp
public System.Threading.Tasks.Task&lt;Tizen.UI.View> PopAsync();
```

Implements [PopAsync()](Tizen.UI.Components.INavigation.md#Tizen.UI.Components.INavigation.PopAsync() 'Tizen.UI.Components.INavigation.PopAsync()')

#### Returns
[System.Threading.Tasks.Task&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')  
The view popped off the navigation stack.

#### Exceptions

[System.InvalidOperationException](https://docs.microsoft.com/en-us/dotnet/api/System.InvalidOperationException 'System.InvalidOperationException')  
Thrown if there is no view in the navigation stack.

<a name='Tizen.UI.Components.Navigator.PopAsync(bool)'></a>

## Navigator.PopAsync(bool) Method

Pops the top view off the navigation stack with or without the transition animation.  
After this method is finished, the previous top view in the navigation stack becomes visible.

```csharp
public System.Threading.Tasks.Task&lt;Tizen.UI.View> PopAsync(bool animated);
```
#### Parameters

<a name='Tizen.UI.Components.Navigator.PopAsync(bool).animated'></a>

`animated` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True to play the transition animation during navigation.

Implements [PopAsync(bool)](Tizen.UI.Components.INavigation.md#Tizen.UI.Components.INavigation.PopAsync(bool) 'Tizen.UI.Components.INavigation.PopAsync(bool)')

#### Returns
[System.Threading.Tasks.Task&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')  
The view popped off the navigation stack.

#### Exceptions

[System.InvalidOperationException](https://docs.microsoft.com/en-us/dotnet/api/System.InvalidOperationException 'System.InvalidOperationException')  
Thrown if there is no view in the navigation stack.

<a name='Tizen.UI.Components.Navigator.PopModalAsync()'></a>

## Navigator.PopModalAsync() Method

Pops the top modal view such as dialog off the modal stack.

```csharp
public System.Threading.Tasks.Task&lt;Tizen.UI.View> PopModalAsync();
```

Implements [PopModalAsync()](Tizen.UI.Components.INavigation.md#Tizen.UI.Components.INavigation.PopModalAsync() 'Tizen.UI.Components.INavigation.PopModalAsync()')

#### Returns
[System.Threading.Tasks.Task&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')  
The modal view popped off the modal stack.

#### Exceptions

[System.InvalidOperationException](https://docs.microsoft.com/en-us/dotnet/api/System.InvalidOperationException 'System.InvalidOperationException')  
Thrown if there is no view in the modal stack.

<a name='Tizen.UI.Components.Navigator.PopModalAsync(bool)'></a>

## Navigator.PopModalAsync(bool) Method

Pops the top modal view such as dialog off the modal stack with or without the transition animation.

```csharp
public System.Threading.Tasks.Task&lt;Tizen.UI.View> PopModalAsync(bool animated);
```
#### Parameters

<a name='Tizen.UI.Components.Navigator.PopModalAsync(bool).animated'></a>

`animated` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True to play the transition animation during navigation.

Implements [PopModalAsync(bool)](Tizen.UI.Components.INavigation.md#Tizen.UI.Components.INavigation.PopModalAsync(bool) 'Tizen.UI.Components.INavigation.PopModalAsync(bool)')

#### Returns
[System.Threading.Tasks.Task&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')  
The modal view popped off the modal stack.

#### Exceptions

[System.InvalidOperationException](https://docs.microsoft.com/en-us/dotnet/api/System.InvalidOperationException 'System.InvalidOperationException')  
Thrown if there is no view in the modal stack.

<a name='Tizen.UI.Components.Navigator.PushAsync(Tizen.UI.View)'></a>

## Navigator.PushAsync(View) Method

Pushes a view onto the navigation stack.  
After this method is finished, the previous top view in the navigation stack becomes invisible.  
If the view exists in the navigation stack already, then it is not pushed.

```csharp
public System.Threading.Tasks.Task PushAsync(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.Components.Navigator.PushAsync(Tizen.UI.View).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view to be pushed onto the navigation stack.

Implements [PushAsync(View)](Tizen.UI.Components.INavigation.md#Tizen.UI.Components.INavigation.PushAsync(Tizen.UI.View) 'Tizen.UI.Components.INavigation.PushAsync(Tizen.UI.View)')

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')

#### Exceptions

[System.ArgumentNullException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentNullException 'System.ArgumentNullException')  
Thrown if `view` is null.

[System.ArgumentException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentException 'System.ArgumentException')  
Thrown if `view` already exists in the navigation stack.

<a name='Tizen.UI.Components.Navigator.PushAsync(Tizen.UI.View,bool)'></a>

## Navigator.PushAsync(View, bool) Method

Pushes a view onto the navigation stack with or without the transition animation.  
After this method is finished, the previous top view in the navigation stack becomes invisible.  
If the view exists in the navigation stack already, then it is not pushed.

```csharp
public System.Threading.Tasks.Task PushAsync(Tizen.UI.View view, bool animated);
```
#### Parameters

<a name='Tizen.UI.Components.Navigator.PushAsync(Tizen.UI.View,bool).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view to be pushed onto the navigation stack.

<a name='Tizen.UI.Components.Navigator.PushAsync(Tizen.UI.View,bool).animated'></a>

`animated` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True to play the transition animation during navigation.

Implements [PushAsync(View, bool)](Tizen.UI.Components.INavigation.md#Tizen.UI.Components.INavigation.PushAsync(Tizen.UI.View,bool) 'Tizen.UI.Components.INavigation.PushAsync(Tizen.UI.View, bool)')

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')

#### Exceptions

[System.ArgumentNullException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentNullException 'System.ArgumentNullException')  
Thrown if `view` is null.

[System.ArgumentException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentException 'System.ArgumentException')  
Thrown if `view` already exists in the modal stack.

<a name='Tizen.UI.Components.Navigator.PushModalAsync(Tizen.UI.View)'></a>

## Navigator.PushModalAsync(View) Method

Pushes a modal view such as dialog onto the modal stack.  
If the view exists in the modal stack already, then it is not pushed.

```csharp
public System.Threading.Tasks.Task PushModalAsync(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.Components.Navigator.PushModalAsync(Tizen.UI.View).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view to be pushed onto the modal stack.

Implements [PushModalAsync(View)](Tizen.UI.Components.INavigation.md#Tizen.UI.Components.INavigation.PushModalAsync(Tizen.UI.View) 'Tizen.UI.Components.INavigation.PushModalAsync(Tizen.UI.View)')

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')

#### Exceptions

[System.ArgumentNullException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentNullException 'System.ArgumentNullException')  
Thrown if `view` is null.

[System.ArgumentException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentException 'System.ArgumentException')  
Thrown if `view` already exists in the modal stack.

<a name='Tizen.UI.Components.Navigator.PushModalAsync(Tizen.UI.View,bool)'></a>

## Navigator.PushModalAsync(View, bool) Method

Pushes a modal view such as dialog onto the modal stack with or without the transition animation.  
If the view exists in the modal stack already, then it is not pushed.

```csharp
public System.Threading.Tasks.Task PushModalAsync(Tizen.UI.View view, bool animated);
```
#### Parameters

<a name='Tizen.UI.Components.Navigator.PushModalAsync(Tizen.UI.View,bool).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view to be pushed onto the modal stack.

<a name='Tizen.UI.Components.Navigator.PushModalAsync(Tizen.UI.View,bool).animated'></a>

`animated` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True to play the transition animation during navigation.

Implements [PushModalAsync(View, bool)](Tizen.UI.Components.INavigation.md#Tizen.UI.Components.INavigation.PushModalAsync(Tizen.UI.View,bool) 'Tizen.UI.Components.INavigation.PushModalAsync(Tizen.UI.View, bool)')

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')

#### Exceptions

[System.ArgumentNullException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentNullException 'System.ArgumentNullException')  
Thrown if `view` is null.

[System.ArgumentException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentException 'System.ArgumentException')  
Thrown if `view` already exists in the navigation stack.

<a name='Tizen.UI.Components.Navigator.Remove(Tizen.UI.View)'></a>

## Navigator.Remove(View) Method

Removes the specified view from the navigation stack or modal stack.

```csharp
public void Remove(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.Components.Navigator.Remove(Tizen.UI.View).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view to be removed from the navigation stack or modal stack.

Implements [Remove(View)](Tizen.UI.Components.INavigation.md#Tizen.UI.Components.INavigation.Remove(Tizen.UI.View) 'Tizen.UI.Components.INavigation.Remove(Tizen.UI.View)'), [Remove(View)](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IParentObject.Remove#Tizen_UI_IParentObject_Remove_Tizen_UI_View_ 'Tizen.UI.IParentObject.Remove(Tizen.UI.View)')

<a name='Tizen.UI.Components.Navigator.WillAppear(bool)'></a>

## Navigator.WillAppear(bool) Method

Called right before appearing by navigation transition.

```csharp
public virtual void WillAppear(bool byPopNavigation);
```
#### Parameters

<a name='Tizen.UI.Components.Navigator.WillAppear(bool).byPopNavigation'></a>

`byPopNavigation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

If true, it is called by pop navigation.

Implements [WillAppear(bool)](Tizen.UI.Components.INavigationTransition.md#Tizen.UI.Components.INavigationTransition.WillAppear(bool) 'Tizen.UI.Components.INavigationTransition.WillAppear(bool)')

<a name='Tizen.UI.Components.Navigator.WillDisappear(bool)'></a>

## Navigator.WillDisappear(bool) Method

Called right before disappearing by navigation transition.

```csharp
public virtual void WillDisappear(bool byPopNavigation);
```
#### Parameters

<a name='Tizen.UI.Components.Navigator.WillDisappear(bool).byPopNavigation'></a>

`byPopNavigation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

If true, it is called by pop navigation.

Implements [WillDisappear(bool)](Tizen.UI.Components.INavigationTransition.md#Tizen.UI.Components.INavigationTransition.WillDisappear(bool) 'Tizen.UI.Components.INavigationTransition.WillDisappear(bool)')
### Explicit Interface Implementations

<a name='Tizen.UI.Components.Navigator.Tizen.UI.Components.INavigateBackHandler.HandleNavigateBack()'></a>

## Navigator.Tizen.UI.Components.INavigateBackHandler.HandleNavigateBack() Method

Handles navigating back.  
If navigating back is not consumed, then the Navigation object of this object will handle navigating back instead.

```csharp
bool Tizen.UI.Components.INavigateBackHandler.HandleNavigateBack();
```

Implements [HandleNavigateBack()](Tizen.UI.Components.INavigateBackHandler.md#Tizen.UI.Components.INavigateBackHandler.HandleNavigateBack() 'Tizen.UI.Components.INavigateBackHandler.HandleNavigateBack()')


























































