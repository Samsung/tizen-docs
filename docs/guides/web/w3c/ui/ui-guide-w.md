# User Interface

## Dependencies

- Tizen 2.4 and Higher for Mobile
- Tizen 2.3.1 and Higher for Wearable

The W3C specifications provide HTML and CSS, which are the core technologies for building Web pages and Web applications. With HTML, you can define the structure of the application screens, while CSS allows you to define the look and feel of the screens.

The main HTML and CSS features are:

- **HTML features**

  HTML is the language for describing the structure of the Web pages.

  - [HTML Priorities](./w3c/ui/html-priority-w.md) **in mobile and wearable applications only**	

    Enables you to use CSS and JavaScript code effectively with HTML elements.

  - [HTML5 Forms](./w3c/ui/html5forms-w.md) **in mobile and wearable applications only**	

    Enables you to easily implement Web forms for user input using HTML5 elements.

  - [Selectors API (Level 1 and 2)](./w3c/ui/selector-w.md) **in mobile and wearable applications only**	

    Enables you to select element nodes in the DOM tree by matching them against a group of selectors.

  - [Media Queries](./w3c/ui/media-query-w.md) **in mobile and wearable applications only**	

    Enables you to define media features for specific output devices using the CSS media queries.

  - [Multiple Screen Support](./w3c/ui/multiple-screens-mw.md) **in mobile applications only**	

    Allows you to create an application that is both scalable and adaptive to multiple screen resolutions.

  - [Multiple UI Layouts](./w3c/ui/ui-layout-ww.md) **in wearable applications only**	

  - Allows you to design your application layout so that your application can run on multiple Tizen devices.

  - [Frame Flattening](./w3c/ui/frame-flattening-mw.md) **in mobile applications only**	

    Allows you to improve the scrollability of small screens.

  - [HTML5 Session History](./w3c/ui/session-history-w.md) **in mobile and wearable applications only**	

    Enables you to manage the browsing history of a device.

  - [Clipboard API and events](./w3c/ui/clipboard-mw.md) **in mobile applications only**	

    Enables you to copy content and paste it in an editable area.

  - [HTML5 Drag and Drop](./w3c/ui/drag-drop-mw.md) **in mobile applications only**	

    Enables you to create and manage draggable elements and implement drag events.

- **CSS features**

  CSS is the language for describing the presentation of the Web pages, including colors, layout, and fonts.

  - [CSS Transforms](./w3c/ui/transform-w.md) **in mobile and wearable applications only**	

    Enables you to move, rotate, stretch, and scale elements using the CSS3 `transform` property.

  - [CSS Animations Module (Level 3)](./w3c/ui/animation-w.md) **in mobile and wearable applications only**	

    Enables you to create animations using the CSS3 `animation` property.

  - [CSS Transitions Module (Level 3)](./w3c/ui/transition-w.md) **in mobile and wearable applications only**	

    Enables you to add effects when changing the style of an element using the CSS3 `transition` property.

  - [CSS Color Module (Level 3)](./w3c/ui/color-w.md) **in mobile and wearable applications only**	

    Enables you to specify the color and opacity of HTML elements using CSS properties.

  - [CSS Backgrounds and Borders Module (Level 3)](./w3c/ui/background-w.md) **in mobile and wearable applications only**	

    Enables you to specify the border and background styles of HTML elements using CSS properties.

  - [CSS Flexible Box Layout Module](./w3c/ui/flexible-w.md) **in mobile and wearable applications only**	

    Enables you to create flexible layouts for Web applications.

  - [CSS Multi-column Layout Module](./w3c/ui/multi-mw.md) **in mobile applications only**	

    Enables you to create multi-column layouts for Web applications.

  - [CSS Text Module (Level 3)](./w3c/ui/text-module-w.md) **in mobile and wearable applications only**	

    Enables you to apply various text effects.

  - [CSS Basic User Interface Module (Level 3)](./w3c/ui/basic-ui-w.md) **in mobile and wearable applications only**	

    Enables you to apply styles to HTML documents.

  - [CSS Fonts Module (Level 3)](./w3c/ui/font-w.md) **in mobile and wearable applications only**	

    Enables you to change the text fonts.

  - [WOFF File Format (1.0 and 2.0)](./w3c/ui/woff-w.md) **in mobile and wearable applications only**	

    Enables you to encode and decode font data easily.

- **Designing for multiple screens**

  Tizen supports various device types with several different screen sizes.To provide optimal user experiences, it is important to design your application to support different screen sizes. In addition to different devices, you must also consider system configuration changes, such as the default home screen layout and system fonts after OS upgrades, since they can change the size of the viewable content screen. Such changes affect the application layout, and can lead to an undesirable UI design layout. Use the following topics to design your application to be highly flexible and adaptive against these possibilities.

  - [Multiple UI Layouts](./w3c/ui/ui-layout-ww.md) **in wearable applications only**	

    Allows you to design your application layout so that your application can run on multiple Tizen devices.

  - [Multiple Screen Support](./w3c/ui/multiple-screens-mw.md) **in mobile applications only**	

    Allows you to create an application that is both scalable and adaptive to multiple screen resolutions.

  - [CSS Fonts Module (Level 3)](./w3c/ui/font-w.md) **in mobile and wearable applications only**	

    Enables you to define the font-face and font-family, to avoid layout incompatibility due to the default system font changes after OS upgrades.