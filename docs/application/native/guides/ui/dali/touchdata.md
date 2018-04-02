# Touch Data



DALi informs you with a callback when the user touches the screen and when the touch ends. The information is encapsulated in the `Dali::TouchData` class, which is a collection of points at a specific moment in time. When a multi-touch event occurs, each point represents the points that are currently being touched or the points where a touch has stopped.

The `Dali::TouchData` class replaces the old deprecated `Dali::TouchEvent` struct. It contains functions for retrieving the information that the `Dali::TouchEvent` struct provided, but also adds the radius, touch pressure, and angle information.

> **Note**  
> Do not use the `Dali::TouchData` class in a container.
>
> As the `Dali::TouchData` class is a handle to an internal object, it must not be copied (or used in a container) as all that happens is that the handle is copied to the same object, and the internal object can change unexpectedly. If the data must be stored in the application, save only the required data (retrieved using the class functions).

The first point that the user touches is the primary point and the one that is used for hit-testing. Hit-testing is the process of determining whether a user-controlled cursor (such as a mouse cursor or touch-point) intersects a given graphical object drawn on the screen. There are many different algorithms that can be used for hit-testing, with different performance or accuracy outcomes. For more information on DALi hit-testing, see the Detailed Description for the `Dali::Actor` class (in [mobile](../../../api/mobile/latest/classDali_1_1Actor.html#details) and [wearable](../../../api/mobile/latest/classDali_1_1Actor.html#details) applications).

## Detecting Touches on Actors

To establish a connection to a touch data signal:

1. Connect to the actor's touch signal:

   1. Create your touch handling function:

      ```
      class MyApplication : public ConnectionTracker
      {
        bool OnTouch( Actor actor, TouchData& touch );
      };
      ```

   2. Connect to the required actor's touch signal (this is normally done when the init signal is received).

      Ensure that your `MyApplication` class is set up to connect to signals, and that it inherits from the `ConnectionTracker` class (in [mobile](../../../api/mobile/latest/classDali_1_1ConnectionTracker.html) and [wearable](../../../api/wearable/latest/classDali_1_1ConnectionTracker.html) applications). The `ConnectionTracker` provides a way of automatically disconnecting from the connected signals when the application dies. This is more useful for application objects that exist only temporarily.

      ```
      Actor actor = Actor::New();
      actor.TouchSignal().Connect( this, &MyApplication::OnTouch );
      ```

      The first parameter of the `Connect()` function (`this`) refers to an object of the `MyApplication*` class. The `Connect()` function connects between `this` and the `OnTouch()` member function.

2. Implement the touch handler.

   When your touch handler is called, you can retrieve a lot of information about how the user has interacted with your actor:

   - To retrieve the point count (the total number of points in the touch data), and the state of a specific point, use the `GetPointCount()` and `GetState()` functions:

     ```
     bool MyApplication::OnTouch( Actor actor, TouchData& touch )
     {
       const std::size_t pointCount = touch.GetPointCount();
       if( pointCount == 1 )
       {
         // Single touch event

         // Get touch state of the primary point
         PointState::Type pointState = touch.GetState( 0 );
         if( pointState == PointState::DOWN )
         {
           // User has just pressed on the device
         }
         else if( pointState == PointState::UP )
         {
           // User has just released their finger from the device
         }
       }
       else
       {
         // Multi-touch event
       }

       return true; // Touch handled
     }
     ```

   - To retrieve the time the touch occurred, use the `GetTime()` function.  
   You can also get the ID of the device that a particular touch originated from. It is useful when multiple touch points are pressed or released.

     ```
     unsigned long touchTime = touchData.GetTime();
     int32_t touchDeviceId = touchData.GetDeviceId( 0 );
     ```

   - To retrieve the hit actor (the actor that was underneath a specific point), use the `GetHitActor()` function. The hit actor can be useful, as it can be a child of the actor that has been given as a parameter.

     `Actor hitActor = touchData.GetHitActor( 0 );`

   - To retrieve the local hit actor and screen positions, use the `GetLocalPosition()` and `GetScreenPosition()` functions. The function returns the coordinates relative to the top left of the hit actor or screen at the specific point.

     ```
     const Vector2& screen = touchData.GetScreenPosition( 0 );
     const Vector2& local = touchData.GetLocalPosition( 0 );
     ```

   - To retrieve the pressure with which the user touched the screen, use the `GetPressure()` function.  
   The pressure range starts at 0.0f and normal pressure is defined as 1.0f. A value between 0.0f and 1.0f means light pressure has been applied, whereas a value greater than 1.0f means that more pressure than normal has been applied.

     `float touchPressure = touchData.GetPressure( 0 );`

   - To retrieve the radius of the touch point, use the `GetRadius()` or `GetEllipseRadius()` function. The first returns a `float` which is the average of both the horizontal and the vertical radii of the pressed point, while the second returns a `Vector2` which stores both the horizontal and the vertical radii of the pressed point.

     ```
     float averageRadius = touchData.GetRadius( 0 );
     const Vector2& ellipseRadii = touchData.GetEllipseRadius( 0 );
     ```

   - To retrieve the angle of the user's finger when touching the screen, use the `GetAngle()` function. The return value is the angle relative to the Y axis.

     `Degree angle = touchData.GetAngle( 0 );`

## Related Information
- Dependencies
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
