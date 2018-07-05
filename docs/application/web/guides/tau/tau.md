# Tizen Advanced UI

The Tizen Advanced UI Framework components allow you to create and manage various kinds of UI components. The components represent a visual UI element, such as a button or slider, which gives you interaction and manipulation features.

This feature is supported in mobile and wearable applications only.

TAU is the standard Web UI library for Tizen platform, originated from the Tizen Web UI Framework Library (standard library for Tizen 2.2.1), which was mainly an extension to jQuery Mobile. The key features of the Web UI Framework Library were coding simplification and application creation speed.  The purpose of TAU is to be the "framework advanced to the next level".

> **Note**  
> Tizen Advanced UI Framework is **optional**, but recommended for making Web applications for Tizen.

With TAU, you can take advantage of the following benefits in your code:

- TAU is a standalone library, so no additional libraries are needed.
- TAU can be used with jQuery, as it exposes a special API to the jQuery object identical to jQuery Mobile. Migration is painless.
- TAU has been written with speed in mind, and all the code is tweaked for maximum performance.
- Applications can be built to dramatically improve startup performance.
- TAU is ECMAScript5- and HTML5-compliant.
- TAU has a large and open API, TAU methods and core functions (event utility functions) are available and not hidden.
- TAU is customizable and easy to extend (to create new UI components).
- TAU is optimized for wearable, mobile, and TV devices.
- TAU supports various profiles (mobile, wearable, and TV).

> **Note**  
> TAU (Tizen Advanced UI) is the new name of the `tizen-web-ui-fw`. In all documents and source code, TAU is used instead of `tizen-web-ui-fw`.  
> Since 2.3, `tizen-web-ui-fw` has been deprecated (including `tizen-web-ui-fw.js`, `tizen-web-ui-fw-libs.js`, and `tizen-web-ui-fw.css`). Since 2.4, `tizen-web-ui-fw` is fully deleted and not supported anymore.

To learn to use the TAU features in your application UI, see the following topics:

- [Downloading TAU](./download-tau.md)

  Enables you to download and build the TAU library.

- [Hello World](./helloworld.md)

  Enables you to make a Web application using TAU.

- [Managing Pages](./managing-page.md)

  Enables you to manage TAU pages.

- [Event Handling](./event-handling.md)

  Enables you to handle user events and interaction.

- [UI Components](./ui-component.md)

  Enables you to create and manage UI components.

- [Creating a Notepad UI Application](./notepad.md)

  Enables you to create a notepad application with TAU.

- [Applications for Circular UI](./circular-ui.md) **in wearable applications only**

  Enables you to apply a circular UI to a wearable application.

- [Accessibility](./accessibility.md)

  Enables you to manage application accessibility.

- [Globalization](./globalization.md)

  Enables you to localize and globalize applications.

- [Animation](./animation.md)

  Enables you to create animations without other animation libraries.

- [2.4 Porting Guide](./tau-porting.md) **in mobile applications only**

  Enables you to migrate a TAU element from Tizen version 2.3 to 2.4.

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
