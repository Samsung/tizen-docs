# Creating Applications with Animation

You can create a simple application using TAU Animation. With the following example, you can learn how to import TAU Animation into your application and create a basic simple application with animation.

This feature is supported in mobile and wearable applications only.

## Loading a TAU Animation

You can import the TAU Animation module with HTML:

```xml
<head>
   <title>TAU Animation Sample</title>
   <script src="lib/tau/animation/tau.animation.min.js" type="text/javascript"></script>
</head>
```

`tau.animation` is the namespace of the TAU Animation module. You can call TAU Animation methods through this namespace.

> **Note**  
> To get the `tau.animation.min.js` library, create a new project from the [UIComponent](https://developer.tizen.org/development/sample/web/UI/TAU_UI_Components) sample. The library is included in the sample's `lib/tau/animation` directory.

## Creating TAU Animations

The following code snippet shows how to create a TAU Animation:

```xml
<div id="redBox" style="background-color: 'red'; position:absolute; width:100px; height:100px;"></div>
<div id="blueBox" style="background-color: 'blue'; position:absolute; width:100px; height:100px; left: 200px;"></div>
```

```javascript
var t = tau.animation.target;
t('#redBox').tween('swing', 1000);
t('#blueBox').tween({rotateZ: 120}, 1000).tween({translateX: 400}, 1000);
```

If you want to animate the HTML element directly, you can use `mixin`. You can animate any effect, transform, or CSS property. You can use the 'target' method. Like in CSS selectors, '.' is a class selector and '\#' is an ID selector. Also, a pure HTML element can be a parameter of the target method.

Available animation methods:

- Predefined effects

  When the first parameter of the `tween()` method indicates a string (such as 'swing' above) instead of an object, it is a predefined effect animation. Various [predefined effects](./animation.md#predefined-effects) are available.

- Chaining

  The `blueBox` animation above is a type of a connected animation. If animations are connected to the same target object, it is added to the queue. And if the `play()` method is invoked, all animations in the queue are called in the sequence order.

- Tween

  `tween()` is a TAU Animation method. It animates a target object based on parameters. The following example shows the use of the `tween()` method:

  ```
  tween({animation}, {option})
  ```

  - `animation` is the part moving, such as a transform, CSS, or predefined effect.

  - `transform` options:  
    `translateX`, `translateY`, `translateZ`, `rotateX`, `rotateY`, `rotateZ`, `scaleX`, `scaleY`, `skewX`, `skewY`

  - `css` options:  
    `left`, `top`, `width`, `height`, `background-color`, `color`, `border`, `border-width`, `border-color`, `margin`, `marginTop`, `marginRight`, `marginBottom`, `marginLeft`, `padding`, `paddingTop`, `paddingRight`, `paddingBottom`, `paddingLeft`, `font-size`, `line-height`, `clip-path`, `background-position`, `background-size`, `box-shadow`

  ```xml
  <div id="redBox" style="background-color: 'red'; position:absolute; width:100px; height:100px;"></div>
  ```

  ```javascript
  var t = tau.animation.target;
  t('#redBox').tween({rotateZ: 120}, 1000); /* Transform */
  /* CSS property */
  t('#redBox').tween({backgroundColor: 'red', border: '10px 10px 10px 3px white'}, 1000);
  t('#redBox').tween('swing', 1000).tween('tada', 1000); /* Predefined effect */
  ```

- Option

  An `option` consists of a duration, ease, delay, callback, and stagger. In order to provide better usage, if you want to use only duration, you can set the duration as a number value like in the previous examples. If any other options are needed, you must make an `{option}` object and insert the `duration: value` into the object.

  ```xml
  <div id="redBox" style="background-color: 'red'; position:absolute; width:100px; height:100px;"></div>
  <div id="blueBox" style="background-color: 'blue'; position:absolute; width:100px; height:100px; left: 200px;"></div>
  <div class="box"></div>
  <div class="box"></div>
  <div class="box"></div>
  <div class="box"></div>
  ```

  ```javascript
  var t = tau.animation.target;
  t('#redBox').tween({rotateZ: 120}, 1000);
  t('#redBox').tween({rotateZ: 120}, {duration: 1000});
  /* Result of this tween method is identical with the above method */
  t('#blueBox').tween({rotateZ: 120}, {duration: 1000, ease: 'bounceInOut'});
  /* After 500ms, blueBox is rotated */
  t('#blueBox').tween({rotateZ: 120}, {duration: 1000, delay: 500});
  t('#blueBox').tween({rotateZ: 120}, {
      duration: 1000,
      onStart: function() {
          /* Before animation, the text is inserted into blueBox */
          t('#blueBox').style.innerText = 'start';
      }, onComplete: function() {
          /* After animation, blueBox is animated with a predefined effect */
          t('#blueBox').tween('swing', 1000);
      }
  });
  /*
     All boxes that include the className 'box' are
     rotated sequentially with a 200ms time difference
  */
  t('.box').tween({rotateZ: 120}, {duration: 1000, stagger: 200});
  ```

The following example shows the full code for the first animation described above.

```xml
<!DOCTYPE html>
<html>
<head>
   <style>
      .box {
         position: absolute;
         width: 100px;
         height: 100px;
         background-color: red;
         left: 100px;
         top: 100px;
      }
   </style>

   <title>TAU Animation Sample</title>

   <!--Load TAU Animation-->
   <script src="lib/tau/animation/tau.animation.min.js" type="text/javascript"></script>
</head>
<body>
   <div id="redBox" style="background-color: 'red'; position:absolute; width:100px; height:100px;"></div>
   <div id="blueBox" style="background-color: 'blue'; position:absolute; width:100px; height:100px;"></div>
   <div class="box"></div>
   <div class="box"></div>
   <div class="box"></div>
   <div class="box"></div>

   <script>
       var t = tau.animation.target;
       /* Single animation */
       t('#redBox').tween('swing', 1000);
       /* Single animation */
       t('#blueBox').tween({rotateZ: 120}, 1000).tween({translateX: 400}, 1000);
       /* Group animation */
       t('.box').tween({translateY: 500}, {duration: 1000, stagger: 200});
   </script>
</body>
</html>
```

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
