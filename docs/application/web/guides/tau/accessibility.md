# Accessibility

The [WAI-ARIA](http://www.w3.org/TR/wai-aria/) (Web Accessibility Initiative - Accessible Rich Internet Applications) is a standard to support easy access to Web content in Web applications. The WAI-ARIA is composed of a role, states, and property, and its current version is 1.0. The Tizen screen reader sends the screen information to the user with the text-to-speech technology from WAI-ARIA data.

This feature is supported in mobile and wearable applications only.

You must define the role, states, and property of the HTML elements in order to enable the Tizen screen reader.

The Tizen screen reader reads HTML elements in the following order:

1. Content		

   The actual element content is read first.

2. Other attributes than `role` and `aria-label`

3. `role` attribute

4. `aria-label` attribute

The following examples show how WAI-ARIA code is read using the text-to-speech functionality of the screen reader:

- Result: checkbox checked, double tap to uncheck

  ```
  <div role="checkbox" aria-checked="true" aria-label="double tap to uncheck"></div>
  ```

- Result: test button, double tap to click

  ```
  <div role="button" aria-label="double tap to click">test</div>
  ```

When creating applications that use the Tizen screen reader, keep in mind the following exceptions:

- If the `aria-hidden` attribute of an element is set to `true`, the screen reader does not read the content of the element or its child elements.  
  In the following snippet, the screen reader reads "on", but not "off" or "child".

  ```
  <div tabindex="0">
     <div>on</div>
     <div aria-hidden="true">
        off
        <div>child</div>
     </div>
  </div>
  ```

- If the `role` attribute is not defined, it is not read.  
  In the following snippet, the screen reader reads "test", but not "link".

  ```
  <a role="" href="test.html">test</a>
  ```

- The screen reader does not read elements that are hidden, for example, if the `display` property is set to `none`.

The `<img>` element supports the image alt text through the `alt` attribute:

```
<img src="icon.jpg" alt="icon">
```

## Related Information
* Dependencies
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
