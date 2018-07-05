# User Interface

The W3C specifications provide HTML and CSS, which are the core technologies for building Web pages and Web applications. With HTML, you can define the structure of the application screens, while CSS allows you to define the look and feel of the screens.

The main HTML and CSS features are:

- **HTML features**

  HTML is the language for describing the structure of the Web pages.

  - [HTML Priorities](./html-priority.md)

    Enables you to use CSS and JavaScript code effectively with HTML elements.

  - [HTML5 Forms](./html5forms.md) 	

    Enables you to easily implement Web forms for user input using HTML5 elements.

  - [Selectors API (Level 1 and 2)](./selector.md) 	

    Enables you to select element nodes in the DOM tree by matching them against a group of selectors.

  - [Media Queries](./media-query.md) 	

    Enables you to define media features for specific output devices using the CSS media queries.

  - [HTML5 Session History](./session-history.md)

    Enables you to manage the browsing history of a device.

  - [Multiple Screen Support](./multiple-screens.md) **in mobile applications only**

    Allows you to create an application that is both scalable and adaptive to multiple screen resolutions.

  - [Multiple UI Layouts](./ui-layout.md) **in wearable applications only**

  - Allows you to design your application layout so that your application can run on multiple Tizen devices.

  - [Frame Flattening](./frame-flattening.md) **in mobile applications only**

    Allows you to improve the scrollability of small screens.

  - [Clipboard API and events](./clipboard.md) **in mobile applications only**

    Enables you to copy content and paste it in an editable area.

  - [HTML5 Drag and Drop](./drag-drop.md) **in mobile applications only**

    Enables you to create and manage draggable elements and implement drag events.

- **CSS features**

  CSS is the language for describing the presentation of the Web pages, including colors, layout, and fonts.

  - [CSS Transforms](./transform.md)

    Enables you to move, rotate, stretch, and scale elements using the CSS3 `transform` property.

  - [CSS Animations Module (Level 3)](./animation.md) 	

    Enables you to create animations using the CSS3 `animation` property.

  - [CSS Transitions Module (Level 3)](./transition.md) 	

    Enables you to add effects when changing the style of an element using the CSS3 `transition` property.

  - [CSS Color Module (Level 3)](./color.md)

    Enables you to specify the color and opacity of HTML elements using CSS properties.

  - [CSS Backgrounds and Borders Module (Level 3)](./background.md) 	

    Enables you to specify the border and background styles of HTML elements using CSS properties.

  - [CSS Flexible Box Layout Module](./flexible.md) 	

    Enables you to create flexible layouts for Web applications.

  - [CSS Text Module (Level 3)](./text-module.md)

    Enables you to apply various text effects.

  - [CSS Basic User Interface Module (Level 3)](./basic-ui.md) 	

    Enables you to apply styles to HTML documents.

  - [CSS Fonts Module (Level 3)](./font.md) 	

    Enables you to change the text fonts.

  - [WOFF File Format (1.0 and 2.0)](./woff.md)

    Enables you to encode and decode font data easily.

  - [CSS Multi-column Layout Module](./multi.md) **in mobile and TV applications only**

    Enables you to create multi-column layouts for Web applications.

- **Designing for multiple screens**

  Tizen supports various device types with several different screen sizes.
  
  To provide an optimal user experience, it is important to design your application to support different screen sizes. In addition to different devices, you must also consider system configuration changes, such as the default home screen layout and system fonts after OS upgrades, since they can change the size of the viewable content screen. Such changes affect the application layout, and can lead to an undesirable UI design layout. Use the following topics to design your application to be highly flexible and adaptive against these possibilities.

  - [CSS Fonts Module (Level 3)](./font.md)

    Enables you to define the font-face and font-family, to avoid layout incompatibility due to the default system font changes after OS upgrades.

  - [Multiple Screen Support](./multiple-screens.md) **in mobile applications only**

    Allows you to create an application that is both scalable and adaptive to multiple screen resolutions.

  - [Multiple UI Layouts](./ui-layout.md) **in wearable applications only**

    Allows you to design your application layout so that your application can run on multiple Tizen devices.

## Related Information
* Dependencies    
    - Tizen 2.4 and Higher for Mobile
    - Tizen 2.3.1 and Higher for Wearable
    - Tizen 3.0 and Higher for TV
