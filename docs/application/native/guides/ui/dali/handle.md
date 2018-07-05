# Handle/Body Pattern


DALi widely adopts the handle/body pattern (also known as the pimpl pattern), which separates the implementation details (body class) from its interface (handle class).

The `Dali::BaseHandle` class (in [mobile](../../../api/mobile/latest/classDali_1_1BaseHandle.html) and [wearable](../../../api/wearable/latest/classDali_1_1BaseHandle.html) applications) is a base class for handle classes in DALi. It additionally provides smart-pointer semantics, which manage internal objects with reference counts. Most of the classes in the DALi public API are handle classes, which means they inherit from the `Dali::BaseHandle` class.

The handle/body pattern structure is beneficial for both DALi users and developers:

- **Easier memory management**

  Each internal implementation class (body class) contains a single reference count object, which can be initialized with the static "New" functions in the DALi public API. This means that C++ new/delete operators do not have to be used in your code. (The internal body classes inherit from the `Dali::BaseObject` class, but you do not need to use this class directly.)

- **Better encapsulation**

  The danger of API/ABI breaks is reduced, since the implementation of a class can be changed without modifying the public API, thus without recompiling code using the public API. This can also reduce the build time.

The following examples show how to use the handles:

- No need to call destructors:

  ```
  class HandleTest
  {
    HandleTest()
    {
      mActor = Actor::New();
    }

    ~HandleTest() {} // Actor object is destroyed automatically

    Actor mActor;
  };
  ```

- Can be stored in STL containers:

  ```
  class HandleTest
  {
    HandleTest()
    {
      mActors.push_back( Actor::New() );
      mActors.push_back( Actor::New() );
    }

    ~HandleTest() {} // Actors are destroyed automatically

    std::vector<Actor> mActors;
  };
  ```

- Passing by value is encouraged:

  ```
  void SomeFunction( Actor actor )
  {
    if( actor )
    {
      actor.SomeMethod();
    }
  }
  ```

- Validity check:

  ```
  {
    Actor actor;  // Create a NULL object

    // At this stage, you cannot call any of the Actor functions
    if( !actor ) // This test passes, since the actor is NULL
    {
      actor = Actor::New();
    }
  }
  ```

- Equality operators:

  ```
  {
    Actor handle1;
    Actor handle2;
    cout << handle1 == handle2 << endl; // "true", both handles are empty

    handle2 = Actor::New();
    cout << handle1 == handle2 << endl; // "false", one handle is empty

    handle1 = Actor::New();
    cout << handle1 == handle2 << endl; // "false", handles to different objects

    handle1 = handle2;
    cout << handle1 == handle2 << endl; // "true", handles to same object
  }
  ```

- Reference counting examples:

  ```
  class AnimationTest
  {
    private:
      Animation mAnimation; // Animation handle
  };

  void AnimationTest::Initialize()
  {
    // Reference count is 1, the animation object stays alive when the function returns
    mAnimation = Animation::New( 10.0f );
  }

  void AnimationTest::SetAnimation( Animation anim )
  {
    // Reference count of the original animation decreased,
    // 'anim' is referenced instead
    // If nobody else had a reference on the initial animation,
    // the object is destroyed
    mAnimation = anim;
  }
  ```

  ```
  // At this point, you own a Dali::Actor named "container"
  // Enter a code block
  {
    // Create an text label
    TextLabel actor = TextLabel::New( "test" );
    // Add the text label to a container
    container.Add( actor );
  }
  // Exit the code block
  // At this stage, the text label is still alive
  // You do not keep the handle to the text label,
  // but it can be retrieved from the container
  ```

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
