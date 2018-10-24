# UI Components

Each UI component in TAU has its own selector for autodetecting in an HTML file. The most popular selector is `class`. The old selector style is the `data-role`, which is deprecated. Some UI components have also simple HTML selectors, such as `button` (button component), or `input[type=checkbox]` (CheckboxRadio component).

This feature is supported in mobile and wearable applications only.

## Defining UI Components

You can define UI components in 2 different ways using selectors:

- With a `class` selector

  It is recommended to use the `class` selector for each component. Class selectors in TAU are composed with a `ui-`prefix and <COMPONENT_NAME>.
  
  The following example shows the creation of some components with a `class` selector:

  ```
  <!--Create an Expandable component-->
  <div class="ui-expandable" id="expandable-test">
     <h1>Expandable head</h1>
     <div>Content</div>
  </div>

  <!--Create a ToggleSwitch component-->
  <select class="ui-toggleswitch">
     <option value="off"></option>
     <option value="on"></option>
  </select>
  ```

- With a `data-role` selector

  The `data-role` selector in TAU is composed with <COMPONENT_NAME> in lowercase.
  
  The following example shows the creation of some components with a `data-role` selector:

  ```
  <!--Create a TextEnveloper component-->
  <div data-role="textenveloper"></div>

  <!--Create a Drawer component-->
  <div data-role="drawer">
     <ul data-role="listview">
        <li><a href="#">List item 1</a></li>
     </ul>
  </div>
  ```

## Setting UI Component Options

TAU supports several ways of setting options for a UI component. For more information, see [Mobile UI Components](../../api/latest/ui_fw_api/Mobile_UIComponents/mobile_component_list.htm) and [Wearable UI Components](../../api/latest/ui_fw_api/Wearable_UIComponents/wearable_component_list.htm).

To set the options:

- Initializing options with the `data-` attribute

  Various options can be set with `data-` attribute when the component is being created. You can set options this way only when the component is created. After creating the component, changing the data attributes on the HTML element does not change the component options.
  
  The following example shows a SectionChanger code with a `data-` option:

  ```
  <div id="hasSectionchangerPage" class="ui-page">
     <header class="ui-header">
        <h2 class="ui-title">SectionChanger</h2>
     </header>
     <div class="ui-section-changer" data-orientation="horizontal" data-circular="true" data-use-tab="true">
        <div>
           <section>
              <h3>LEFT1 PAGE</h3>
           </section>
           <section class="ui-section-active">
              <h3>MAIN PAGE</h3>
           </section>
           <section>
        </div>
     </div>
  </div>
  ```

  The `data-circular` and `data-use-tab` attributes are the initial options for creating a SectionChanger.

- Setting options with a manual constructor

  Options can be set as arguments to the component constructor. When using options as arguments, you must use the camelCase name.

  The following example shows the use of a manual constructor:

  ```
  <div id="hasSectionchangerPage" class="ui-page">
     <header class="ui-header">
        <h2 class="ui-title">SectionChanger</h2>
     </header>
     <div class="ui-section-changer" id="sectionchanger">
        <div>
           <section>
              <h3>LEFT1 PAGE</h3>
           </section>
           <section class="ui-section-active">
              <h3>MAIN PAGE</h3>
           </section>
        </div>
     </div>
  </div>

  <script>
      var sectionEl = document.getElementById('sectionchanger'),
          sectionChangerWidget = tau.widget.SectionChanger(sectionEl, {
              orientation: 'horizontal',
              circular: true
              useTab: true
          });
  </script>
  ```

- Setting options with a method call

  To set options dynamically, use the `option`() method.

  ```
  <div id="hasSectionchangerPage" class="ui-page">
     <header class="ui-header">
        <h2 class="ui-title">SectionChanger</h2>
     </header>
     <div class="ui-section-changer" data-orientation="horizontal" data-circular="true" data-use-tab="true">
        <div>
           <section>
              <h3>LEFT1 PAGE</h3>
           </section>
           <section class="ui-section-active">
              <h3>MAIN PAGE</h3>
           </section>
           <section>
        </div>
     </div>
  </div>

  <script>
      var sectionEl = document.getElementById('sectionchanger'),
          sectionChangerWidget = tau.widget.SectionChanger(sectionEl);

      sectionChangerWidget.option('circular', true);
  </script>
  ```

## Managing UI Components with jQuery

You can use jQuery with TAU for convenience. Also for backward compatibility, TAU supports the jQuery interface for UI components. However, it is strongly recommended to use the new TAU style.

To manage the UI components if the jQuery library is loaded:

1. Create the UI component:

   ```
   <div class="ui-indexscrollbar" id="indexscrollbar"></div>
   <script>
       $('#indexscrollbar').indexscrollbar();
   </script>
   ```

2. Use the call methods:

   ```
   $('.selector').componentName('methodName', argument1, argument2, ...);
   ```

   ```
   <div class="ui-indexscrollbar" id="indexscrollbar"></div>
   <script>
       /* If the IndexScrollBar component is created */
       $('#indexscrollbar').indexscrollbar('destroy');
   </script>
   ```

## Related Information
* Dependencies   
   - Tizen 2.4 and Higher for Mobile
   - Tizen 2.3.1 and Higher for Wearable
