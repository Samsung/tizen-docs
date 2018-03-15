# Properties


A property is a value used by an object. It can be modified or read using the `Dali::Handle::GetProperty()` or `Dali::Handle::SetProperty()` functions.

The difference between properties and ordinary C++ member variables is that a property can be dynamically added to or removed from an existing object at runtime, enabling more flexible, script-like programming with DALi.

The `Dali::Handle` class (in [mobile](../../../api/mobile/latest/classDali_1_1Handle.html) and [wearable](../../../api/wearable/latest/classDali_1_1Handle.html) applications) provides functions to manage properties. Because of this, the DALi classes that inherit from the `Dali::Handle` class (most of classes that you use) have a number of predefined properties and can have any number of user-defined custom properties.

## Accessing Property Values

Property values of an object can usually be accessed in 2 ways: by its class member functions or by property getters and setters (`GetProperty()` and `SetProperty()` function of the `Dali::Handle` class).

For example, the following table lists the predefined properties of the `Dali::Actor` class (in [mobile](../../../api/mobile/latest/classDali_1_1Actor.html) and [wearable](../../../api/wearable/latest/classDali_1_1Actor.html) applications).

**Table: Dali::Actor properties**

| Property index (enumeration) | Member functions                         |
|------------------------------|------------------------------------------|
| `Dali::Actor::POSITION`      | `Dali::Actor::GetCurrentPosition()` / `SetPosition()` |
| `Dali::Actor::ORIENTATION`   | `Dali::Actor::GetCurrentOrientation()` / `SetOrientation()` |
| `Dali::Actor::SIZE`          | `Dali::Actor::GetCurrentSize()` / `SetSize()` |
| `Dali::Actor::COLOR`         | `Dali::Actor::GetCurrentColor()` / `SetColor()` |
| `Dali::Actor::NAME`          | `Dali::Actor::GetName()` / `SetName()`   |

You can access the properties in both ways:

```
Actor actor = Actor::New();
actor.SetName( "test actor" );
std::cout << actor.GetName() << std::endl; // "test actor"
```

```
Actor actor = Actor::New();
actor.SetProperty( Actor::Property::NAME, "test actor" );
// "test actor"
std::cout << actor.GetProperty( Actor::Property::NAME ) << std::endl;
// "test actor"
std::cout << actor.GetProperty<std::string>( Actor::Property::NAME ) << std::endl;
// "test actor"
std::cout << actor.GetProperty( Actor::Property::NAME ).Get<std::string>() << std::endl;
```

## Using Properties

### Registering User-defined Custom Properties to Objects

Properties can be registered and deregistered at runtime using the functions of the `Dali::Handle` class. This enables script-like programming in the DALi application, such as adding custom member data to an instance of a DALi class without subclassing the class or maintaining another pool of custom data.

For example, you can set your own custom data to `PushButton` objects and use them later when the buttons are clicked:

```
void Create( Application& application )
{
  for( int i = 0; i < 5; ++i )
  {
    Toolkit::PushButton button = Toolkit::PushButton::New();
    button.SetSize( 100, 100 );
    button.SetPosition( 100 * i + 50, 50 );
    button.ClickedSignal().Connect( this, OnButtonClicked );

    // Register a custom property having button index
    // Store the property index so you can look it up later
    // Note: This is much faster than looking the property up by property name
    // and must be used if possible
    // As all control types are the same (PushButtons),
    // the indices to the unique custom property are all same
    Property::Value data( i );
    mCustomDataIndex = button.RegisterProperty( "custom-data", data );

    Stage::GetCurrent().Add( button );
  }
}

bool OnButtonClicked( Toolkit::Button button )
{
  // Look up the custom property by the stored property index
  // Note: If the property belongs to a control in another library,
  // or you do not know the index, you can look the index up first with:
  // Property::Index index = button.GetPropertyIndex( "custom-data" );
  cout << button.GetProperty( mCustomDataIndex ) << endl;

  return true;
}
```

### Animating Objects

The `Dali::Animation` class (in [mobile](../../../api/mobile/latest/classDali_1_1Animation.html) and [wearable](../../../api/wearable/latest/classDali_1_1Animation.html) applications) is used to [animate the properties](animation.md) of any number of objects.

For example, the following code animates the value of the `POSITION` property of a radio button to (100.0, 200.0, 0.0) for 2 seconds:

```
RadioButton actor = RadioButton::New();
Stage::GetCurrent().Add( actor );
Animation animation = Animation::New( 2.0f ); // Duration 2 seconds
animation.AnimateTo( Property( actor, Actor::Property::POSITION ), Vector3( 100.0f, 200.0f, 0.0f ) );
animation.Play();
```

### Imposing Constraints on Objects

The `Dali::Constraint` class (in [mobile](../../../api/mobile/latest/classDali_1_1Constraint.html) and [wearable](../../../api/wearable/latest/classDali_1_1Constraint.html) applications) is used to [modify the property of an object based on other properties of other objects](constraints.md).

For example, the following code makes the `SIZE` property value of an actor the same as the `SIZE` property value of its parent actor:

```
Constraint constraint = Constraint::New<Vector3>( actor, Actor::Property::SIZE, EqualToConstraint() );
constraint.AddSource( ParentSource( Actor::Property::SIZE ) );
constraint.Apply();
```

## Managing Property Attributes

A property has the following attributes:

- Index: Enumeration number indicating the property. The property index is usually used to access properties.
- Type: Type of the property. Retrieved with the `Dali::Handle::GetPropertyType()` function.
- Name: Name of the property. Retrieved with the `Dali::Handle::GetPropertyName()` function.
- Writable: If `true`, the property value can be written. Retrieved with the `Dali::Handle::IsPropertyWritable()` function.
- Animatable: If `true`, the property can be animated using the `Dali::Animation` class. Retrieved with the `Dali::Handle::IsPropertyAnimatable()` function.
- Constraint-Input: If `true`, the property can be used as constraint input. Retrieved with the `Dali::Handle::IsPropertyAConstraintInput()` function.

The following table lists the type and name attributes of the `Dali::Actor` properties.

**Table: Dali::Actor property attributes**

| Property index (enumeration) | Property type | Property name |
|------------------------------|---------------|---------------|
| `Dali::Actor::POSITION`      | Vector3       | "position"    |
| `Dali::Actor::ORIENTATION`   | Quaternion    | "orientation" |
| `Dali::Actor::SIZE`          | Vector3       | "size"        |
| `Dali::Actor::COLOR`         | Vector4       | "color"       |
| `Dali::Actor::NAME`          | std::string   | "name"        |

For more information on properties, see the API reference of each class. For example, for the `Dali::Actor` class, see the `Dali::Actor::Property` struct (in [mobile](../../../api/mobile/latest/structDali_1_1Actor_1_1Property.html) and [wearable](../../../api/wearable/latest/structDali_1_1Actor_1_1Property.html) applications). For information on the supported property types, see `Dali::Property::Type` (in [mobile](../../../api/mobile/latest/classDali_1_1Property.html#acb569f557811bc94d2e98b5c880d759c) and [wearable](../../../api/wearable/latest/classDali_1_1Property.html#acb569f557811bc94d2e98b5c880d759c) applications) and `Dali::PropertyTypes` (in [mobile](../../../api/mobile/latest/namespaceDali_1_1PropertyTypes.html) and [wearable](../../../api/wearable/latest/namespaceDali_1_1PropertyTypes.html) applications).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
