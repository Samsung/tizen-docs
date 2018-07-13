# Hello World

You can import TAU into your application and create a basic Hello World page with TAU.

This feature is supported in mobile and wearable applications only.

The following example shows a basic TAU template:

```xml
<!DOCTYPE html>
<html>
   <head>
      <meta name="viewport" content="width=device-width, user-scalable=no"/>
      <link rel="stylesheet" href="./lib/tau/mobile/theme/default/tau.css"/>
      <link rel="stylesheet" href="myapp.css"/>
      <title>Hello TAU</title>
   </head>
   <body>
      <!--HTML BODY CONTENT-->
      <script type="text/javascript" src="./lib/tau/mobile/js/tau.js"></script>
      <script src="myapp.js"></script>
   </body>
</html>
```

## Scaling the UI

The Tizen Advanced UI (TAU)-based template provides 2 scaling methods: device-width and fixed-width.

- Device-width scaling

  This scaling mode is suited for most mobile devices, such as Tizen, iPhone, and Android&trade;. In this mode, the viewport width is set to `device-width`, enabling rem scaling using the Rem and Em units. These units calculate the size of a source element automatically based on the container font size (Em) or the base font size (Rem). In Tizen Web applications, a 320 px screen width is assumed.

  ```
  <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
  ```

- Fixed-width scaling

  This scaling mode is best suited for Tizen devices, since the entire screen can be scaled on the viewport level. In the viewport scaling mode, set the size of all resources to fit the 360 px screen width.

  You can also use fixed-width scaling if you do not want to scale your application or if you want to set your own scale. In this case, declare a viewport but note that the default viewport scaling is overridden by the declared viewport. In the Tizen Web UI components, viewport scaling is set automatically to `device-width`:

  ```
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
  ```

  To enable fixed-width scaling, the header must contain the `<meta name="viewport">` element:

  ```
  <meta name="viewport" content="width=360, initial-scale=1, user-scalable=no">
  ```

## Importing TAU

You can import TAU with HTML. For better performance, all CSS files must be included in the header and all script elements must be put before the body element's close tag:

```xml
<!DOCTYPE html>
<html>
   <head>
      <link rel="stylesheet" href="./lib/tau/mobile/theme/default/tau.css"/>
   </head>
   <body>
      <!--HTML BODY CONTENT-->
      <script type="text/javascript" src="./lib/tau/mobile/js/tau.js"></script>
   </body>
</html>
```

In HTML, use the `<script>` and `<link>` elements. These default elements are used to load the basic Tizen Advanced UI (TAU) libraries that must be included in Tizen Web applications. The loaded libraries are:

- TAU library: `tau(.min).js`  
   This element is mandatory, as it imports the TAU library, which you need to use the TAU JavaScript Interface.
- TAU theme: `tau(.min).css`  
   This element is also mandatory, as it imports the TAU theme.

## Running Custom JavaScript and CSS

You can add an additional `<script src="<CUSTOM_LIBRARY>">` or `<link rel="stylesheet" src="<CUSTOM_CSS>">` element to include your own scripts and style sheets. However, place them **after** the default `<script>` elements, as you can use any TAU APIs provided by the default libraries.

To load your JavaScript file, include the file in the `<script>` element in the HTML header. Since the TAU files are already loaded, you can use any APIs from these libraries as well.

```
<script src="{YOUR_SCRIPT_PATH}"></script>
```

## Creating a Page in the Body

The body section of the HTML file contains 1 or more pages.

To create a page in `<body>`, you can use the `"ui-page"` class with the `<div>` element:

```
<body>
   <div class="ui-page" id="main">
   </div>
</body>
```

Each page has a header, mandatory content, and a footer:

```
<body>
   <div class="ui-page" id="main">
      <div class="ui-header">
         <h1>Hello World</h1>
      </div>
      <div class="ui-content">
         <p>Hello TAU!</p>
      </div>
      <div class="ui-footer">
         <button>OK</button>
      </div>
   </div>
</body>
```

The following example shows a basic sample code for Hello World:

```
<!DOCTYPE html>
<html>
   <head>
      <meta name="viewport" content="width=device-width, user-scalable=no"/>
      <link rel="stylesheet" href="./lib/tau/mobile/theme/default/tau.css"/>
      <link rel="stylesheet" href="myapp.css"/>
      <title>Hello TAU</title>
   </head>
   <body>
      <div class="ui-page" id="main">
         <div class="ui-header">
            <h1>Hello World</h1>
         </div>
         <div class="ui-content">
            <p>Hello TAU!</p>
         </div>
         <div class="ui-footer">
            <button>OK</button>
         </div>
      </div>
      <script type="text/javascript" src="./lib/tau/mobile/js/tau.js"></script>
      <script src="myapp.js"></script>
   </body>
</html>
```

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
