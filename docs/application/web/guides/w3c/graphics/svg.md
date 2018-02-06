# SVG
The HTML5 SVG supports 2D graphics through SVG (Scalable Vector Graphics). Prior to HTML5, SVG functioned based on XML, so it was only used in XHTML or with a separate SVG plug-in. Since HTML5, however, an `svg` tag is used in XML, and can be added as an inline element in HTML.

The main SVG API features include:

- Creating text and images

  You can [add text and images](#creating-text-and-images) to your application as SVG elements.

- Making shapes

  You can [create various shapes](#making-shapes) as graphic elements, such as lines, rectangles, and circles.

- Grouping SVG elements

  You can [group various SVG elements](#grouping-svg-elements) together for easier management.

- Animating SVG elements

  You can [animate SVG elements](#animating-svg-elements) to create motions or change element properties, such as color.

- Controlling SVG elements through scripting

  You can [control events related to SVG elements using scripts](#controlling-svg-elements-through-scripting).

For more information on using SVG, see [Scalable Vector Graphics (SVG) Tiny 1.2 Specification](http://www.w3.org/TR/2008/REC-SVGTiny12-20081222/).

## Creating Text and Images

To create text and images, use the `svg` tag in HTML `<body>` element:

- Text

  Define the textual content and the location on the screen:

  ```
  <svg xmlns="http://www.w3.org/2000/svg">
     <text x="60" y="150">Hello World</text>
  </svg>
  ```

- Images

  Define the image file, the image location on the screen, and the image size:

  ```
  <svg xmlns="http://www.w3.org/2000/svg">
     <image xlink:href="http://developer.tizen.org/sites/all/themes/tizen_theme/logo.png"
            x="10" y="10" width="224" height="74"/>
  </svg>
  ```

## Making Shapes

To create shapes as inline SVG elements:

1. Create the SVG element with the `svg` tag.

2. Use the graphic elements to create various shapes. The absolute coordinates of the graphics element determine the size of the SVG. You can define the shape, size, location on the screen, line width, and the line and fill colors for the shapes.

   - To create a line between 2 assigned coordinates, use the `<line>` element:

     ```
     <svg xmlns="http://www.w3.org/2000/svg" width="300px" height="200px">
        <line x1="20" y1="20" x2="220" y2="120" stroke="blue" stroke-width="5"/>
     </svg>
     ```

   - To create a rectangle at the assigned coordinates, use the `<rect>` element:

     ```
     <svg xmlns="http://www.w3.org/2000/svg" width="300px" height="200px">
        <rect x="1" y="1" width="120" height="40"
              fill="blue" stroke="red" stroke-width="2"/>
     </svg>
     ```

   - To create a circle with the assigned barycentric coordinate and radius, use the `<circle>` element:

     ```
     <svg xmlns="http://www.w3.org/2000/svg" width="300px" height="200px">
        <circle cx="150" cy="100" r="50" fill="blue" stroke="red" stroke-width="3"/>
     </svg>
     ```

   - To create an ellipse with the assigned barycentric coordinate and the X and Y axis radius, use the `<ellipse>` element:

     ```
     <svg xmlns="http://www.w3.org/2000/svg" width="300px" height="200px">
        <ellipse  cx="130" cy="80" rx="125" ry="50" fill="blue"/>
     </svg>
     ```

   - To create a polygon consisting of a set of assigned coordinates, use the `<polygon>` element:

     ```
     <svg xmlns="http://www.w3.org/2000/svg" width="300px" height="200px">
        <polygon fill-rule="evenodd" fill="blue" stroke="black"
                 points="148,16 116,96 196,48 100,48 180,96"/>
     </svg>
     ```

### Source Code

For the complete source code related to this use case, see the following file:

- [svg_shape.html](http://download.tizen.org/misc/examples/w3c_html5/graphics/html5_svg)

## Grouping SVG Elements

To group inline SVG elements:

1. Combine various SVG elements in a group using the `<g>` container element, whose `id` attribute must be defined.

   If you assign a presentation attribute to the group, all the child elements inherit it. For example, in the following example, the stroke color black is defined for the group, which means that both the rectangle and circle elements within the group use the black stroke color.

   ```
   <svg xmlns="http://www.w3.org/2000/svg" width="600px" height="600px">
      <g id="shape-group" stroke="black">
         <desc>Shape Group</desc>
         <rect x="0.5" y="0.5"  fill="blue"  width="275" height="168"/>
         <circle fill="red" stroke-width="4" cx="245" cy="159" r="93"/>
      </g>
   ```

2. You can reference the group using the `id` attribute:

   ```
      <use xlink:href="#shape-group" x="20" y="40"/>
      <use xlink:href="#shape-group" x="40" y="60"/>
      <use xlink:href="#shape-group" x="60" y="80"/>
   </svg>
   ```

3. If you have multiple groups, use the `<defs>` element as a container for them:

   ```
   <svg xmlns="http://www.w3.org/2000/svg" width="600px" height="600px">
      <defs>
         <g id="shape-group" stroke="black">
            <desc>Shape Group 1</desc>
            <rect x="0.5" y="0.5"  fill="blue"  width="275" height="168"/>
            <circle fill="red" stroke-width="4" cx="245" cy="159" r="93"/>
         </g>
         <g id="shape-group2" stroke="black">
            <desc>Shape Group 2</desc>
            <rect x="0.5" y="0.5"  fill="red"  width="275" height="168"/>
            <circle fill="blue" stroke-width="4" cx="245" cy="159" r="93"/>
         </g>
      </defs>
      <g>
         <desc>Shape Group 3</desc>
         <use xlink:href="#shape-group" x="60" y="80 "/>
         <use xlink:href="#shape-group2" transform="rotate(40)" x="120" y="70"/>
         <use xlink:href="#shape-group" transform="rotate(15)" x="190" y="120"/>
         <use xlink:href="#shape-group2" transform="rotate(20)" x="120" y="70"/>
      </g>
   </svg>
   ```

### Source Code

For the complete source code related to this use case, see the following file:

- [svg_group.html](http://download.tizen.org/misc/examples/w3c_html5/graphics/html5_svg)

## Animating SVG Elements

To animate inline SVG elements:

1. To animate a specific element attribute based on time, use the `<animate>` element:

   ```
   <svg xmlns="http://www.w3.org/2000/svg" width="300px" height="200px">
      <rect x="1" y="1" width="120" height="40" fill="blue" stroke="red" stroke-width="2">
         <animate attributeName="width" to="300" dur="5s" repeatCount="1" fill="remove"/>
      </rect>
      <rect x="1" y="50" width="120" height="40" fill="blue" stroke="red" stroke-width="2">
         <animate attributeName="width" to="300" dur="5s" repeatCount="1" fill="freeze"/>
      </rect>
   </svg>
   ```

2. To change the (fill or line) color of the element, use the `<animateColor>` element:

   ```
   <svg xmlns="http://www.w3.org/2000/svg" width="300px" height="200px">
      <rect x="1" y="1" width="120" height="40" fill="blue" stroke="red" stroke-width="2">
         <animateColor to="red" attributeName="fill" dur="5s" repeatCount="indefinite"/>
      </rect>
   </svg>
   ```

3. To create a motion animation, use the `<animateMotion>` element. The element assigns the parent element to the `<mpath>` as reference element, and animates according to the shape of the `<mpath>` element.

   ```
   <svg xmlns="http://www.w3.org/2000/svg" width="300px" height="200px">
      <path d="M-12.5, -6.75 L12.5, -6.75 L0, -43.75 z"
            fill="blue" stroke="gray" stroke-width="3">
         <animateMotion dur="6s" repeatCount="indefinite" rotate="auto">
            <mpath xlink:href="#path1"/>
         </animateMotion>
      </path>
      <path id="path1" d="M25, 100 Q50, 20 75, 70 T135, 70 T185, 70 T235, 70 T275, 70"
            fill="none" stroke="blue" stroke-width="3"/>
   </svg>
   ```

### Source Code

For the complete source code related to this use case, see the following file:

- [svg_animation.html](http://download.tizen.org/misc/examples/w3c_html5/graphics/html5_svg)

## Controlling SVG Elements through Scripting

To use scripts to manage events related to SVG elements:

1. Define an SVG element:

   ```
   <svg xmlns="http://www.w3.org/2000/svg" width="300px" height="200px">
      <rect x="1" y="1" width="120" height="40" fill="blue"
            stroke="red" stroke-width="2"/>
   </svg>
   ```

2. Use the `<script>` element to handle events related to the SVG elements.

   The script usage is similar to handling DOM as a script. The following example controls the SVG element's `width` attribute through the click event.

   ```
   <script>
       var rectElemt = document.getElementById('rect')
       rectElemt.addEventListener('click', rect_click);

       function rect_click(event) {
           var target = event.target
           var targetWidth = target.getAttribute('width');
           if (targetWidth == 120) {
               target.setAttribute('width', targetWidth * 2);
           } else {
               target.setAttribute('width', targetWidth * 0.5);
           }
       }
   </script>
   ```

### Source Code

For the complete source code related to this use case, see the following file:

- [svg_script.html](http://download.tizen.org/misc/examples/w3c_html5/graphics/html5_svg)

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
