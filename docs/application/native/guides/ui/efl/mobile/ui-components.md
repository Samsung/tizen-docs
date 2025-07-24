# Mobile UI Components

EFL Elementary is a set of fast, finger-friendly, scalable, and themeable UI component libraries. The number of supported UI components is around 80, including both [containers](../ui-layouts.md) and non-containers (listed in this topic). Originally, Elementary was developed as part of the Window Manager development on desktop devices. For the mobile profile, Tizen reused the proper UI components and created new ones, and then enhanced and adjusted all of them for Tizen native applications.

This feature is supported in mobile applications only.

The UI components are mobile-friendly: for example, the naviframe container component supports multiple view management, the entry component supports various modes (such as password, single-line or multi-line, edit or no-edit), the index component supports quick access to another group of UI items, and the toolbar component shows a menu when an item is selected.

The mobile UI components are designed to allow the user to interact with touch screen-equipped mobile devices. Therefore, when developing mobile applications, you can easily use them through the mobile-related infrastructure in company with view management, and when reacting to touch events and the user finger size.

**Table: Available UI components**

| Category             | Component name                         | Description                            |
|----------------------|----------------------------------------|----------------------------------------|
| Navigation elements  | [Toolbar](./component-toolbar.md) | The  toolbar component is a scrollable list of items. It can also show a menu when  an item is selected. Only one item can be selected at a time. |
| Navigation elements  | [Index](./component-index.md) | The  index component provides an index for quick access to another group of UI  items. |
| Navigation elements  | [Segmentcontrol](./component-segmentcontrol.md) | The  segmentcontrol component is a horizontal control made of multiple segment  items, each segment item functioning similarly as a discrete 2-state button. |
| Presentation views   | [Win](./component-win.md) | The  win component is the root window component often used in an application. It  allows you to create some content in it, and it is handled by the window  manager. |
| Presentation views   | [Background](./component-background.md) | The  background component can be used to set a solid background decoration to a  window or a container object. It works like an image, but has some  background-specific properties, such as setting it to a tiled, centered,  scaled, or stretched mode. |
| Presentation views   | [Genlist](./component-genlist.md) | The  genlist component displays a scrollable list of items. It can hold a lot of  items while still being fast and memory-efficient (since only the visible  items are allocated memory). |
| Presentation views   | [Gengrid](./component-gengrid.md) | The  gengrid component displays objects on a grid layout and renders only the  visible objects. |
| Presentation views   | [Panel](./component-panel.md) | The  panel component is an animated object that can contain child objects. It can  be expanded or collapsed by clicking the button on its edge. |
| Presentation views   | [List](./component-list.md) | The  list component is a very simple list for managing a small number of items. If  you need to manage a lot of items, use the genlist component instead. |
| Presentation views   | [Label](./component-label.md) | The  label component displays text with simple HTML-like markup. |
| Presentation views   | [Image](./component-image.md) | The  image component can load and display an image from a file or memory. |
| Presentation views   | [Icon](./component-icon.md) | The  icon component inherits from the image component. It is used to display  images in an icon context. |
| Presentation views   | [Progressbar](./component-progressbar.md) | The  progressbar component can be used to display the progress status of a given  job. |
| Presentation views   | [Photocam](./component-photocam.md) | The  photocam component is designed to display high-resolution photos taken with a  digital camera. It allows you to zoom photos, load photos quickly, and fit  photos. It is optimized for JPEG images and has a low memory footprint. |
| User input            | [Button](./component-button.md) | The  button component is a simple push button. It is composed of a label icon and  an icon object, and has an auto-repeat feature. |
| User input  | [Check](./component-check.md) | The  check component toggles the Boolean value between true and false. |
| User input  | [Radio](./component-radio.md) | The  radio component can display 1 or more options, while the user can only select  one of them. The UI component is composed of an indicator (selected or  unselected), an optional icon, and an optional label. Even though it is  usually grouped with 2 or more other radio components, it can also be used  alone. |
| User input  | [Entry](./component-entry.md) | The  entry component is a box to which the user can enter text. |
| User input  | [Slider](./component-slider.md) | The  slider component is a draggable bar that is used to select a value from a  range of values. |
| User input  | [Datetime](./component-datetime.md) | The  datetime component can display and accept input for date and time values. |
| User input  | [Colorselector](./component-colorselector.md) | The  colorselector component provides a color selection solution to the user. It  has different modes, each of them showing a different configuration of the  color selection. |
| User input  | [Spinner](./component-spinner.md) | The  spinner component enables the user to increase or decrease a numeric value by  using arrow buttons. |
| User input      | [Flipselector](./component-flipselector.md) | The  flipselector component shows a set of text items one at a time. The user can  flip the selector up or down to change the text on it. |
| User input  | [Calendar](./component-calendar.md) | The  calendar component displays and manipulates month views. |
| Assist views    | [Popup](./component-popup.md) | The  popup component shows a pop-up area that can contain a title area, a content  area, and an action area. |
| Assist views    | [Ctxpopup](./component-ctxpopup.md) | The  ctxpopup component is a contextual popup that can show a list of items. |
| Assist views    | [Notify](./component-notify.md) | The  notify component displays a container in a specific region of the parent  object. It can receive some content, and it can be automatically hidden after  a certain amount of time. |
| Assist views    | [Tooltip](./component-tooltip.md) | The  tooltip component is a smart object used to show tips or information about a  parent object when the mouse hovers over the parent object. |
| Assist views    | [Hoversel](./component-hoversel.md) | The  hoversel component is a button that pops up a list of items. |
| Transition             | Transit                                  | The  transit component can apply several transition effects to an Evas object,  such as translations and rotations. |
| Assist views           | [Flip](./component-flip.md) | The  flip component can hold 2 Evas objects and let the user flip between these  objects using a variety of predefined animations. |
| Hardware  acceleration | [GLView](./component-glview.md) | The  GLView component can render OpenGL&reg; in an Elementary object, hiding EvasGL  complexity. |
| Miscellaneous          | [Map](./component-map.md) | The map component can  display a geographic map. The default map data is provided by the  [OpenStreetMap project](http://www.openstreetmap.org/). |
| Miscellaneous         | [Plug](./component-plug.md) | The  plug component allows you to show an Evas object created by another process.  It can be used anywhere like any other Elementary UI component. |

> **Note**
>
> Except as noted, this content is licensed under [LGPLv2.1+](http://opensource.org/licenses/LGPL-2.1).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
