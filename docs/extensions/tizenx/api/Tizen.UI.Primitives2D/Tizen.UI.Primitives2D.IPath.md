### [Tizen.UI.Primitives2D](Tizen.UI.Primitives2D.md 'Tizen.UI.Primitives2D')

## IPath Interface

Defines a command that can be executed on a [Shape](Tizen.UI.Primitives2D.Shape.md 'Tizen.UI.Primitives2D.Shape') object.

```csharp
public interface IPath
```

Derived  
&#8627; [ArcTo](Tizen.UI.Primitives2D.ArcTo.md 'Tizen.UI.Primitives2D.ArcTo')  
&#8627; [BezierTo](Tizen.UI.Primitives2D.BezierTo.md 'Tizen.UI.Primitives2D.BezierTo')  
&#8627; [Close](Tizen.UI.Primitives2D.Close.md 'Tizen.UI.Primitives2D.Close')  
&#8627; [DrawCircle](Tizen.UI.Primitives2D.DrawCircle.md 'Tizen.UI.Primitives2D.DrawCircle')  
&#8627; [DrawOval](Tizen.UI.Primitives2D.DrawOval.md 'Tizen.UI.Primitives2D.DrawOval')  
&#8627; [DrawRect](Tizen.UI.Primitives2D.DrawRect.md 'Tizen.UI.Primitives2D.DrawRect')  
&#8627; [DrawRoundRect](Tizen.UI.Primitives2D.DrawRoundRect.md 'Tizen.UI.Primitives2D.DrawRoundRect')  
&#8627; [LineTo](Tizen.UI.Primitives2D.LineTo.md 'Tizen.UI.Primitives2D.LineTo')  
&#8627; [MoveTo](Tizen.UI.Primitives2D.MoveTo.md 'Tizen.UI.Primitives2D.MoveTo')
### Methods

<a name='Tizen.UI.Primitives2D.IPath.Execute(Tizen.UI.Primitives2D.Shape)'></a>

## IPath.Execute(Shape) Method

Executes the command on the specified [Shape](Tizen.UI.Primitives2D.Shape.md 'Tizen.UI.Primitives2D.Shape') object.

```csharp
void Execute(Tizen.UI.Primitives2D.Shape shape);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.IPath.Execute(Tizen.UI.Primitives2D.Shape).shape'></a>

`shape` [Shape](Tizen.UI.Primitives2D.Shape.md 'Tizen.UI.Primitives2D.Shape')

The Shape object on which the command should be executed.


















































