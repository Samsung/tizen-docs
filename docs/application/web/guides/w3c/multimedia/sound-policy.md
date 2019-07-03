# Tizen WebKit Tap Sound Policy

To provide responsiveness on user interaction, Tizen WebKit plays sounds when a user taps an element and specific conditions are fulfilled.

This feature is supported in mobile applications only.

Sound is not played on a tap event for:

- HTML elements whose disabled property is set to `disabled`
- HTML `<input>` elements whose type attribute is set to one of the following editable types:  
  *	`date`
  * `datetime`
  * `datetime-local`
  * `email`
  * `month`
  * `number`
  * `password`
  * `range`
  * `search`
  * `tel`
  * `text`
  * `time`
  * `url`
  * `week`		
- HTML `<textarea>` elements

Sound is played on a tap event for:

- HTML `<a>` elements with the `href` attribute
- HTML `<area>` elements with the `href` attribute
- HTML `<button>` elements
- HTML `<input>` elements
- HTML `<keygen>` elements
- HTML `<select>` elements
- HTML `<summary>` elements with a visible heading for the HTML `<details>` element
- HTML elements on which the click event listener is registered
- HTML elements on which the mousedown event listener is registered
- HTML elements on which the mouseup event listener is registered
- HTML elements on which the mouseover event listener is registered
- MediaController objects of the HTML media elements

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
