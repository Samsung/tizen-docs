# Constraints


Constraints are used to modify the property of an actor (**target property**), based on other properties of the same actor; properties of the actor's parent; or properties of another actor altogether (**property input or constraint source**), when the modification needs to be at runtime. Custom functions or functors can be supplied, where the desired value of the property can be calculated. These functions or functors are called in every frame, therefore they must be fast and not too complex, otherwise they can affect performance (**constraint function**).

**Figure: Conceptual diagram for the DALi constraint system**

![Conceptual diagram for the DALi constraint system](./media/constraint-concept.png)

The following pseudocode fragment shows how to set up and apply a constraint:

```
Constraint constraint = Constraint::New< <target-property-type> >( <target-handle>, <target-property>, <constraint-function> );
constraint.AddSource( <property-input-1> );
constraint.AddSource( <property-input-2> );

constraint.Apply();
```

Multiple constraints can be applied to the same actor at the same time. The order in which constraints are applied is important as this is the order in which they are processed in the update thread.

Constraints are applied after animations have been applied. This means that constraints override the values set by animations. Constraints are not applied to off-stage actors.

Not all properties can be used as a constraint input. To check whether a property can be a constraint input, use the `Dali::Handle::IsPropertyAConstraintInput()` function.

## Constraint Source

Certain properties can be used as input sources to the constraint. The constraint takes these values, optionally performs a calculation on them (if using a custom functor), and writes the result to the specified property of the target actor.

The source actor is specified as either the same actor, its parent, or another actor.

A constraint input source can be one of the following types:

- **Local source** (use `Dali::LocalSource`)  
A local source is based on the local properties (such as size, position, scale, orientation, or color) of an actor. For example, the actor's orientation can be used as a constraint input source:

    ```
    ConstraintSource source( LocalSource( Actor::Property::ORIENTATION ) );
    ```
- **Parent source** (use `Dali::ParentSource`)  
A parent source is based on properties of the actor's parent. For example, a parent's position can be used as a constraint input source:

    ```
    ConstraintSource source( ParentSource( Actor::Property::POSITION ) );
    ```

- **Other handle source** (use `Dali::Source`)  
You can base your source on the properties of another handle altogether. For example, a sibling actor's color can be used as a constraint input source:

    ```
    ConstraintSource source( Source( anotherHandle, Actor::Property::COLOR ) );
    ```

## Constraint Function

The signature of the constraint function is:

```
void Function( PropertyType &current, const PropertyInputContainer &inputs );
```

In this function, the `current` parameter is a reference to the target property type, such as `float`, `Vector2`, or `Vector3`. This is an in or out parameter. It represents the current value of the property and the expectation is that it is modified by the function to the desired value.

The `inputs` parameter holds all the constraint input sources. Each element is a pointer to the property input and can be accessed using the indexing operator `[ ]`. The order in which the sources are added is the order in which the property inputs are sorted in the container.

```
constraint.AddSource( LocalSource( Actor::Property::POSITION ) );
constraint.AddSource( LocalSource( Actor::Property::SIZE ) );
constraint.AddSource( ParentSource( Actor::Property::POSITION ) );
constraint.AddSource( ParentSource( Actor::Property::SIZE ) );
```

In the constraint function this equals to:

```
const Vector3& position( inputs[0]->GetVector3() );
const Vector3& size( inputs[1]->GetVector3() );
const Vector3& parentPosition( inputs[2]->GetVector3() );
const Vector3& parentSize( inputs[3]->GetVector3() );
```

### Using C Functions as Constraint Functions

If you do not have any data that is changed at runtime, use a C function as a constraint function.

For example, the color of an actor can be changed based on its position along the X axis. In the following sample, the color of the control is white when its X position is 0.0f, red when its X position is 100.0f, and an interpolated color is used in between:

```
// This sample code is for the HelloWorldExample class
// in Creating a DALi Application

// C function
void MyConstraintFunction( Vector4& current, const PropertyInputContainer& inputs )
{
  const Vector3& position( inputs[0]->GetVector3() );

  float distance = fabs( position.x );
  if( distance > 100.0f ) // More than 100.0f away, color is red
  {
    current.g = current.b = 0.0f;
  }
  else // Otherwise it blends between white and red
  {
    current.g = current.b = ( 100.0f - distance ) / 100.0f;
  }
}

void HelloWorldExample::Create( Application& application )
{
  // Create a control
  Control control = Control::New();
  control.SetParentOrigin( ParentOrigin::CENTER );
  control.SetSize( 100.0f, 100.0f );
  control.SetBackgroundColor( Color::WHITE );
  Stage::GetCurrent().Add( control );

  // Use PanGestureDetector to move the control with touch panning
  mDetector = PanGestureDetector::New();
  mDetector.Attach( control );
  mDetector.DetectedSignal().Connect( this, &HelloWorldExample::OnPan );

  // Create a constraint that targets the control
  Constraint constraint = Constraint::New< Vector4 >( control, Actor::Property::COLOR, MyConstraintFunction );

  // Add the POSITION property of the control as a constraint input
  constraint.AddSource( LocalSource( Actor::Property::POSITION ) );

  // Apply the constraint
  constraint.Apply();
}
```

The following example shows the actual C function:

```
void HelloWorldExample::OnPan( Actor actor, const PanGesture& gesture )
{
  // Move the button using the detected gesture
  actor.TranslateBy( Vector3( gesture.displacement ) );
}
```

For more information, see the `New()` function in the `Dali::Constraint` class (in [mobile](../../../api/mobile/latest/classDali_1_1Constraint.html) and [wearable](../../../api/wearable/latest/classDali_1_1Constraint.html) applications).

### Using Functors as Constraint Functions

If you need to store some data in a struct or class, use a functor.

Reusing the above C example, the color of an actor is changed based on its position along the X axis, but the distance when it is red can be different for each constraint object:

```
struct MyConstraintFunctor
{
  // Constructor which takes the distance at which the actor is red
  MyConstraintFunctor(float distance)
    : mDistance(distance)  {}

  // Functor
  void operator()( Vector4& current, const PropertyInputContainer& inputs )
  {
    const Vector3& position( inputs[0]->GetVector3() );

    float distance = fabs( position.x );
    if( distance > mDistance ) // More than mDistance away, color is red
    {
      current.g = current.b = 0.0f;
    }
    else // Otherwise it blends between white and red
    {
      current.g = current.b = ( mDistance - distance ) / mDistance;
    }
  }

  const float mDistance; // Data
};
```

The `MyConstraintFunctor()` functor can be applied to the `control` as follows:

```
Constraint constraint = Constraint::New< Vector4 >( control, Actor::Property::COLOR, MyConstraintFunctor( 200.0f ) );
```

The `MyConstraintFunctor()` functor can be used also with another constraint with a different distance. Instead of using the default functor (`operator()`), another function can be declared in the class or struct and used as the constraint function. For more information, see the `New()` function in the `Dali::Constraint` class.

### Built-in Constraint Functions

The following built-in constraint functions are available:

- Equal to constraint

  The built-in `Dali::EqualToConstraint()` function can be used if you only need to set a property equal to another property:

  ```
  Constraint constraint = Constraint::New< Vector3 >( actor, Actor::Property::POSITION, EqualToConstraint() );
  constraint.AddSource( Source( anotherActor, Actor::Property::POSITION ) );
  constraint.Apply();
  ```

  Here the `actor`'s position is set to equal the position of `anotherActor`.

- Relative to constraint

  The built-in `Dali::RelativeToConstraint()` and `Dali::RelativeToConstraintFloat()` functions can be used if you only need to set a property relative to another property:

  ```
  Constraint constraint = Constraint::New< Vector3 >( actor, Actor::Property::POSITION, RelativeToConstraint( 2.0f ) );
  constraint.AddSource( Source( anotherActor, Actor::Property::POSITION ) );
  constraint.Apply();
  ```

  Here the `actor`'s position is relative to the position of `anotherActor` (multiplied by a given scale). If `anotherActor` is at (10.0f, 20.0f, 30.0f), `actor` is at (20.0f, 40.0f, 60.0f).

## Removing Constraints

When no longer needed, the actor's constraints can be removed in several ways:

- To remove the constraint itself and stop applying it:

  ```
  constraint.Remove();
  ```

- To remove all constraints applied to an actor:

  ```
  actor.RemoveConstraints();
  ```

- To remove all constraints with the tag from an actor (the tag can be set using the `SetTag()` function):

  ```
  actor.RemoveConstraints( tag );
  ```

## Constraint Usage Tips

Constraints are designed as a way of modifying properties that cannot be modified by any existing built-in functionality, such as animations, size negotiation, parent anchor, or origin settings. As they allow you to execute your own code within the update thread, DALi can no longer guarantee the timeliness of this code, or how optimized it can be.

Generally, do not use constraints with the `size` property as constraining the size and size negotiation are mutually exclusive. The following table provides example use cases for when and when not to use a constraint.

**Table: Constraint use examples**

| Requirement                              | Solution                                 |
|------------------------------------------|------------------------------------------|
| Need a child to be 50% the size of its parent. | Use size negotiation.<br>For more information, see [Layout Management](layout.md). |
| Need to zoom an actor in to the screen using its scale property. | Use an animation.<br>For more information, see [Animation](animation.md). |
| Need an actor to appear centered around the bottom-right corner of its parent. | Use the `Dali::ParentOrigin` (in [mobile](../../../api/mobile/latest/namespaceDali_1_1ParentOrigin.html) and [wearable](../../../api/wearable/latest/namespaceDali_1_1ParentOrigin.html) applications) and `Dali::AnchorPoint` (in [mobile](../../../api/mobile/latest/namespaceDali_1_1AnchorPoint.html) and [wearable](../../../api/wearable/latest/namespaceDali_1_1AnchorPoint.html) applications) namespaces.<br>For more information, see [Positioning Actors](actors.md#positioning-actors). |
| Need to lay out a series of controls with various alignment requirements. | Use either `ParentOrigin` and `AnchorPoint` settings, or the `Dali::Toolkit::TableView` class (in [mobile](../../../api/mobile/latest/classDali_1_1Toolkit_1_1TableView.html) and [wearable](../../../api/wearable/latest/classDali_1_1Toolkit_1_1TableView.html) applications). |
| Need to automatically modify the position property of one actor based on the position property of another actor that is neither a parent nor a child. | Use a constraint.                        |
| Need to position an actor relative to its parent actor in a NON-UNIFORM way, or a non-linear calculation needs to be performed that requires a functor. | Use a constraint.                        |
| Need to modify an actor's property in real time based on some calculations that require additional data to be stored in-between frames. | Use a constraint.<br>The constraint functor can hold any variables within it that need to be preserved frame-to-frame. |

In most general cases, the position and size requirements of a child or parent actor (from its child or parent) can be calculated with size negotiation.

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
