# Animations and Effects

EFL provides the following animation and effect features:

- **Ecore animators**

  Ecore animators use the Ecore main loop for running animations. To create an Ecore animation, you must first determine the duration of the animation, and then define a callback that performs the animation with that duration.

  For more information, see [Ecore Animations](./ecore-animation.md).

- **Edje animations**

  Edje animations are based on a simple principle: transitioning from one state to another. To animate an object with Edje, you have to first define the start and end states of the animation, and then transition the object from the start state to the end state.

  For more information, see [Edje Animations](./edje-animation.md).

- **Elementary transitions**

  Elementary transitions allow you to apply various transition effects, such as translation and rotation, to Evas objects. Elementary transitions are mostly based on Ecore animators, but provide some transition methods at a higher level of abstraction. Elementary transitions provide a simpler way of animating objects than Ecore animators or Edje animations.

  For more information, see [Elementary Animations](./elementary-animation.md).

- **Evas map effects**

  Evas map animations allow you to apply transformations to all types of objects using UV mapping. In UV mapping, you map points in the source object to 3D space positions in the target object. This allows for rotation, perspective, scale, and other transformation effects, depending on the map. In addition, each map point can carry a multiplier color, which, if properly calculated, can be used to apply 3D shading effects on the target object.

  For more information, see [Transformation with Evas Map](./evas-map-animation.md) and [Creating Evas Map Effects](./evas-map-effects.md).

> **Note**
>
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
