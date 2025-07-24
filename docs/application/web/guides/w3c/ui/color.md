# CSS Color Module (Level 3)

You can manage the CSS properties for [specifying the color and opacity of an HTML element](#specifying-a-color-for-an-element), and the CSS color value type. To increase user satisfaction, you can also [create color generators](#creating-a-color-generator) to allow the user to set the color.

You can specify the color of an element with the following formats:

- Keyword values

  You can use basic keywords, such as `red`, `green`, `blue`, or `deepskyblue`, as defined in [Extended color keywords](http://www.w3.org/TR/css3-color/#svg-color).

  The `currentColor` keyword can be used with all properties that accept a color value (borders, box shadows, outlines, or backgrounds). The computed value of the `currentColor` keyword is the computed value of the `color` property. If the `currentColor` keyword is set on the `color` property itself, it is treated as `color: inherit`.

  You can use the `transparent` keyword with all properties that accept a color value (borders, box shadows, outlines, or backgrounds), to turn the element in question transparent (invisible).

- RGB values

  - In hexadecimal notation

    The format is '#' followed by either 3 or 6 hexadecimal characters. The 3-digit RGB notation (#rgb) is converted into a 6-digit form (#rrggbb) by replicating digits. For example, `#fc0` expands to `#ffcc00`.

  - In functional notation

    The format is 'rgb(' followed by a comma-separated list of 3 numerical values (integer or percentage) followed by ')'. The integer value 255 corresponds to 100%, and to F or FF in a hexadecimal notation: `rgb(255, 255, 255)` = `rgb(100%, 100%, 100%)` = `#FFF`. White space characters are allowed around the numerical values.

- RGBA values

  The RGB color model is extended to include "alpha" to allow the color opacity to be specified. The RGBA values are defined using functional notation where the final value is the alpha (range from 0.1 to 1). For example: `rgba(255, 0, 0, 0.7)`.

- HSL value

  You can use numerical hue-saturation-lightness (HSL) colors as an alternative to numerical RGB colors. The HSL colors are encoded as a triple (hue, saturation, lightness). The hue is represented as the angle of the color circle, where by definition red=0°=360° and other colors are spread around the circle. The saturation and lightness are represented as percentages, where 100% is full saturation or black lightness, and 0% is a shade of gray or white lightness. 50% lightness is "normal". For example: `hsl(0, 100%, 50%)`.

- HSLA value

  The HSL color model is extended to include "alpha" to allow the color opacity to be specified. The HSLA values are defined using the HSL notation where a final alpha value is added (range from 0.1 to 1). For example: `hsla(120, 100%, 50%, 0.8)`.

> **Note**  
> The CSS2 System Color values have been deprecated in favor of the CSS3 UI 'appearance' property.

## Specifying a Color for an Element

To define a color for an element, you can use various color formats in the CSS properties:

```
<!--Keywords-->
#one {
   color: blue;
   background: white;
   border: 1px solid springgreen;
}
#one span {
   background: currentColor;
}
#one span.hide {
   color: transparent;
}

<!--RGB-->
#two {
    color: #ff0000;
}

<!--RGBA-->
#three {
   color: rgba(100%, 0, 0, 0.5);
}

<!--HSL-->
#four {
   color: hsl(0, 100%, 50%);
}

<!--HSLA-->
#five {
   color: hsla(0, 100%, 50%, 0.5);
}
```

### Source Code

For the complete source code related to this use case, see the following files:

- [color.html](http://download.tizen.org/misc/examples/w3c_html5/dom_forms_and_styles/css_color_module_level_3)
- [current_color.html](http://download.tizen.org/misc/examples/w3c_html5/dom_forms_and_styles/css_color_module_level_3)
- [hsl_color.html](http://download.tizen.org/misc/examples/w3c_html5/dom_forms_and_styles/css_color_module_level_3)
- [hsla_color.html](http://download.tizen.org/misc/examples/w3c_html5/dom_forms_and_styles/css_color_module_level_3)
- [rgb_color.html](http://download.tizen.org/misc/examples/w3c_html5/dom_forms_and_styles/css_color_module_level_3)
- [rgba_color.html](http://download.tizen.org/misc/examples/w3c_html5/dom_forms_and_styles/css_color_module_level_3)
- [transparent.html](http://download.tizen.org/misc/examples/w3c_html5/dom_forms_and_styles/css_color_module_level_3)

## Creating a Color Generator

To enhance the coloring of the UI elements in your application, you must learn to generate color values in the HSLA format:

**Figure: HSLA color generator**

![HSLA color generator](./media/css_color_tutorial1.png)

1. To create the color generator, define 2 `<div>` elements for displaying the HSLA value as text and in a color box. You also need 4 slider inputs for defining the HSLA color:

   - The first input has a range of 0 - 360 and represents hue.
   - The second and third inputs have a range of 0 - 100 and represent saturation and lightness.
   - The last input has a range of 0 - 10 and represents alpha transparency.  
      The range should be 0.1 - 1, but the minimum value of the `min` attribute is 0 so the value can be divided by 10.

   ```
   <div id="color-generator">
      <div id="text-box"></div>
      <div id="color-box"></div>

      <label>Hue</label>
      <input id="hue" value="0" type="range" min="0" max="360">

      <label>Saturation</label>
      <input id="saturation" value="100" type="range" min="0" max="100">

      <label>Lightness</label>
      <input id="lightness" value="50" type="range" min="0" max="100">

      <label>Alpha</label>
      <input id="alpha" value="10" type="range" min="0" max="10">
   </div>
   ```

2. Obtain the values from the slider inputs with the `getElementById()` method. Remember to divide the alpha value by 10 to reach the correct range of 0.1 - 1.

   ```
   var h = document.getElementById('hue').value,
       s = document.getElementById('saturation').value,
       l = document.getElementById('lightness').value,
       a = document.getElementById('alpha').value / 10,
   ```

3. Set the HSLA text and the color of the color box by defining the color from the inputs in the HSL and HSLA formats.

   If the alpha is 1, the HSL format is displayed. Otherwise, the HSLA format is used.

   ```
       /* Define formats */
       hsl = 'hsl(' + h + ', ' + s + '%, ' + l + '%)',
       hsla = 'hsla(' + h + ', ' + s + '%, ' + l + '%, ' + a + ')',

       /* Set the color of the box */
       cBox = document.querySelector('#color-box'),

       /* Set the text */
       tBox = document.querySelector('#text-box');
   ```

4. Add an event handler to the input sliders to change the displayed text and color box color when the slider values change.

   ```
   var inputs = document.querySelectorAll('#color-generator input[type=range]');

   for (i = 0; i < inputs.length; i++) {
       inputs[i].onchange = function() {
           /* Show color */
       };
   }
   ```

### Source Code

For the complete source code related to this use case, see the following file:

- [css_color.html](http://download.tizen.org/misc/examples/w3c_html5/dom_forms_and_styles/css_color_module_level_3)

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
