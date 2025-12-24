### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## INavigationAnimation Interface

The INavigationAnimation interface defines functions called for the transition animation during navigation.

```csharp
public interface INavigationAnimation
```

Derived  
&#8627; [Navigator](Tizen.UI.Components.Navigator.md 'Tizen.UI.Components.Navigator')
### Properties

<a name='Tizen.UI.Components.INavigationAnimation.PopAnimation'></a>

## INavigationAnimation.PopAnimation Property

Function called for transition animation of navigation pop.

```csharp
System.Func&lt;Tizen.UI.View,Tizen.UI.View,Tizen.UI.Components.INavigationAnimationController> PopAnimation { get; }
```

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[INavigationAnimationController](Tizen.UI.Components.INavigationAnimationController.md 'Tizen.UI.Components.INavigationAnimationController')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')

### Remarks
The first View of Func is the view to be popped. The fist View will be removed from the navigation stack.

<a name='Tizen.UI.Components.INavigationAnimation.PopModalAnimation'></a>

## INavigationAnimation.PopModalAnimation Property

Function called for transition animation of modal pop.

```csharp
System.Func&lt;Tizen.UI.View,Tizen.UI.View,Tizen.UI.Components.INavigationAnimationController> PopModalAnimation { get; }
```

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[INavigationAnimationController](Tizen.UI.Components.INavigationAnimationController.md 'Tizen.UI.Components.INavigationAnimationController')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')

### Remarks
The first View of Func is the modal view to be popped. The fist View will be removed from the modal stack.

<a name='Tizen.UI.Components.INavigationAnimation.PushAnimation'></a>

## INavigationAnimation.PushAnimation Property

Function called for transition animation of navigation push.

```csharp
System.Func&lt;Tizen.UI.View,Tizen.UI.View,Tizen.UI.Components.INavigationAnimationController> PushAnimation { get; }
```

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[INavigationAnimationController](Tizen.UI.Components.INavigationAnimationController.md 'Tizen.UI.Components.INavigationAnimationController')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')

### Remarks
The first View of Func is the view to be pushed. The fist View will be the top view.

<a name='Tizen.UI.Components.INavigationAnimation.PushModalAnimation'></a>

## INavigationAnimation.PushModalAnimation Property

Function called for transition animation of modal push.

```csharp
System.Func&lt;Tizen.UI.View,Tizen.UI.View,Tizen.UI.Components.INavigationAnimationController> PushModalAnimation { get; }
```

#### Property Value
[System.Func&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')[INavigationAnimationController](Tizen.UI.Components.INavigationAnimationController.md 'Tizen.UI.Components.INavigationAnimationController')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Func-3 'System.Func`3')

### Remarks
The first View of Func is the modal view to be pushed. The fist View will be the top view.


























































