# 2.4 Porting Guide

This guide describes the changes required to migrate a TAU element from 2.3 to 2.4.

This feature is supported in mobile applications only.

As the Tizen version number changes, TAU has been updated with new features. When migrating from 2.3 to 2.4, consider the following issues:

- Selectors for defining the UI components
- New and deprecated components in 2.4
- Gesture event handling

## Backward Compatibility in TAU

To support backward compatibility, TAU provides the `tau.support-2.3.js` and `tau.support-2.3.css` files.

If you want to use deprecated components, you can import those files. See the following example:

```
<html>
   <head>
      <script type="text/javascript" src="../lib/tau/mobile/js/tau.js"></script>
      <script type="text/javascript" src="../lib/tau/mobile/js/tau.support-2.3.js"></script>
      <link rel="stylesheet" href="../lib/tau/mobile/theme/default/tau.css">
      <link rel="stylesheet" href="../lib/tau/mobile/theme/default/tau.support-2.3.css">
      <link rel="stylesheet" href="css/custom.css">
   </head>
</html>
```

> **Note**  
> The `tau.support-2.3` file is only for backward compatibility. The above components are **DEPRECATED since Tizen 2.4** and are deleted in Tizen 3.0.

## Component Definitions

Since Tizen 2.4, it is strongly recommended to use the `class` selector to define the components in HTML files. The `"data-role"` selector has been deprecated and is no longer supported.

The class selectors in TAU are composed with the `"ui-"` prefix and followed by the `<COMPONENT_NAME>`. For more information, see [UI Component API Reference](../../api/latest/ui_fw_api/Mobile_UIComponents/mobile_component_list.htm).

The following example shows how to define the UI components before and after:

- Before:

  ```
  <!--Create Expandable component-->
  <div data-role="expandable">
     <h1>Expandable head</h1>
     <div>Content</div>
  </div>

  <!--Create ToggleSwitch component-->
  <select data-role="toggleswitch">
     <option value="off"></option>
     <option value="on"></option>
  </select>

  <!--Create SectionChanger component-->
  <div data-role="section-changer">
     <div>
        <section>
           <h3>LEFT1 PAGE</h3>
        </section>
     </div>
  </div>
  ```

  > **Note**  
  > The old selector with `data-role` can still be used in 2.4, but it is **DEPRECATED** and no longer supported in the next version.

- After:

  ```
  <!--Create Expandable component-->
  <div class="ui-expandable">
     <h1>Expandable head</h1>
     <div>Content</div>
  </div>

  <!--Create ToggleSwitch component-->
  <select class="ui-toggleswitch">
     <option value="off"></option>
     <option value="on"></option>
  </select>

  <!--Create SectionChanger component-->
  <div class="ui-section-changer">
     <div>
        <section>
           <h3>LEFT1 PAGE</h3>
        </section>
     </div>
  </div>
  ```

## New Components in 2.4

Some new mobile components are added in TAU since 2.4. Some are renamed from old components (such as Checkbox and Radio) and others are newly added with a new feature and theme (such as Colored ListView). The following table shows the new TAU components in 2.4.

For more information, see the [Mobile UI Component API Reference](../../api/latest/ui_fw_api/Mobile_UIComponents/mobile_component_list.htm).

**Table: New TAU mobile components in 2.4**

| UI component                             | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| [Checkbox](../../api/latest/ui_fw_api/Mobile_UIComponents/mobile_Checkbox.htm) | The checkbox component changes the default browser checkboxes to a form more adapted to the mobile environment. |
| [Colored List View](../../api/latest/ui_fw_api/Mobile_UIComponents/mobile_ColoredListview.htm) | The colored list view component shows each list item with a gradient background color. |
| [Dropdown Menu](../../api/latest/ui_fw_api/Mobile_UIComponents/mobile_DropdownMenu.htm) | The dropdown menu component is used to select one option. It is created as a drop-down list form. |
| [Expandable](../../api/latest/ui_fw_api/Mobile_UIComponents/mobile_Expandable.htm) | The expandable component allows you to expand or collapse content when tapped. |
| [Floating Actions](../../api/latest/ui_fw_api/Mobile_UIComponents/mobile_FloatingActions.htm) | The floating actions component shows a floating action button that can be moved left and right. |
| [Grid View](../../api/latest/ui_fw_api/Mobile_UIComponents/mobile_GridView.htm) | The grid view component provides a grid-type list and presents content that are easily identified as images. |
| [Index Scrollbar](../../api/latest/ui_fw_api/Mobile_UIComponents/mobile_IndexScrollBar.htm) | The index scrollbar component shows a shortcut list that is bound to its parent scrollbar and list view. |
| [Page Indicator](../../api/latest/ui_fw_api/Mobile_UIComponents/mobile_PageIndicator.htm) | The page indicator component presents as a dot-typed indicator. |
| [Panel Changer](../../api/latest/ui_fw_api/Mobile_UIComponents/mobile_PanelChanger.htm) | The panel changer and panel component provide a multi-page layout in a page component. |
| [Radio](../../api/latest/ui_fw_api/Mobile_UIComponents/mobile_Radio.htm) | The radio component changes the default browser radio button to a form more adapted to the mobile environment. |
| [Search Input](../../api/latest/ui_fw_api/Mobile_UIComponents/mobile_SearchInput.htm) | The search input component is used to search for page content. |
| [Section Changer](../../api/latest/ui_fw_api/Mobile_UIComponents/mobile_SectionChanger.htm) | The section changer component provides an application architecture, which has multiple sections on one page. |
| [Tabs](../../api/latest/ui_fw_api/Mobile_UIComponents/mobile_Tabs.htm) | The tabs component shows an unordered list of buttons on the screen wrapped together in a single group. |
| [Text Enveloper](../../api/latest/ui_fw_api/Mobile_UIComponents/mobile_TextEnveloper.htm) | The text enveloper component changes a text item to a button. |

## Deprecated Components

Some mobile components are deprecated and no longer supported since 2.4. Instead of using deprecated components, see the following table and replace the components by new components or an HTML element.

For more information on deprecated components, see the [Mobile Component API Reference](../../api/latest/ui_fw_api/Mobile_UIComponents/mobile_component_list.htm).

**Table: Deprecated TAU mobile components**

| UI component                             | Replace with                             |
| ---------------------------------------- | ---------------------------------------- |
| [Autodividers](../../api/latest/ui_fw_api/Mobile_UIComponents/deprecated/mobile_Autodividers.htm) | -                                        |
| [CheckboxRadio](../../api/latest/ui_fw_api/Mobile_UIComponents/deprecated/mobile_Checkboxradio.htm) | Checkbox component for the checkbox, radio component for the radio button. |
| [Collapsible](../../api/latest/ui_fw_api/Mobile_UIComponents/deprecated/mobile_Collapsible.htm) | Expandable component.                    |
| [ControlGroup](../../api/latest/ui_fw_api/Mobile_UIComponents/deprecated/mobile_Controlgroup.htm) | Implement your own customized application style. |
| [Fast Scroll](../../api/latest/ui_fw_api/Mobile_UIComponents/deprecated/mobile_FastScroll.htm) | Index scrollbar component.               |
| [Gallery](../../api/latest/ui_fw_api/Mobile_UIComponents/deprecated/mobile_Gallery.htm) | Implement your own gallery with the section changer component. |
| [List Divider](../../api/latest/ui_fw_api/Mobile_UIComponents/deprecated/mobile_ListDivider.htm) | Use the `ui-group-index` class for a group index. |
| [Notification](../../api/latest/ui_fw_api/Mobile_UIComponents/deprecated/mobile_Notification.htm) | Popup component with the `ui-popup-toast` class. |
| [Progress Bar](../../api/latest/ui_fw_api/Mobile_UIComponents/deprecated/mobile_ProgressBar.htm) | Progress component with the `data-type="bar"` option. |
| [Scroll Handler](../../api/latest/ui_fw_api/Mobile_UIComponents/deprecated/mobile_ScrollHandler.htm) | -                                        |
| [Search Bar](../../api/latest/ui_fw_api/Mobile_UIComponents/deprecated/mobile_SearchBar.htm) | Search input component.                  |
| [Select Menu](../../api/latest/ui_fw_api/Mobile_UIComponents/deprecated/mobile_SelectMenu.htm) | Dropdown menu component.                 |
| [Swipe](../../api/latest/ui_fw_api/Mobile_UIComponents/deprecated/mobile_Swipe.htm) | -                                        |
| [Tab Bar](../../api/latest/ui_fw_api/Mobile_UIComponents/deprecated/mobile_TabBar.htm) | Tabs component.                          |
| [Token Text Area](../../api/latest/ui_fw_api/Mobile_UIComponents/deprecated/mobile_Tokentextarea.htm) | Text enveloper component.                |

If your application used the above deprecated components, see the following examples for successful migration:

- **CheckboxRadio**            

  Before:

  ```
  <input type="checkbox" name="checkbox-1" id="checkbox-1"/>
  <input type="radio" name="radio-1" id="radio-1"/>

  <script>
      var element1 = document.getElementById('checkbox-1'),
          element2 = document.getElementById('radio-1'),
          checkboxWidget = tau.widget.Checkboxradio(element1),
          radioWidget = tau.widget.Checkboxradio(element2);

      checkboxWidget.enable();
      radioWidget.disable();
  </script>            
  ```

  After:

  ```
  <input type="checkbox" name="checkbox-1" id="checkbox-1"/>
  <input type="radio" name="radio-1" id="radio-1"/>

  <script>
      var element1 = document.getElementById('checkbox-1'),
          element2 = document.getElementById('radio-1'),
          checkboxWidget = tau.widget.Checkbox(element1),
          radioWidget = tau.widget.Radio(element2);

      checkboxWidget.enable();
      radioWidget.disable();
  </script>        
  ```

- **Collapsible**            

  Before:

  ```
  <ul data-role="listview">
     <li id="collapsible" data-role="collapsible" data-inset="false">
        <h2>Collapsible head</h2>
        <!--Sub list in collapsible li-->
        <ul data-role="listview">
           <li>sub list item1</li>
           <li>sub list item2</li>
        </ul>
     </li>
     <!--List item in 1st depth-->
     <li>other list item</li>
     <li>other list item</li>
  </ul>

  <script>
      var collapsibleElement = document.getElementById('collapsible'),
          collapsible = tau.widget.Collapsible(collapsibleElement);
  </script>            
  ```

  After:

  ```
  <div id="expandable" class="ui-expandable" data-collapsed="false">
     <h1>Expandable head</h1>
     <div>Content</div>
  </div>

  <script>
      var expandableEl = document.getElementById('expandable'),
          expandableWidget = tau.widget.Expandable(expandableEl);
  </script>       
  ```

- **Fast Scroll**            

  Before:

  ```
  <div data-role="page" id="main">
     <div data-role="content">
        <ul id="list" data-role="listview" data-fastscroll="true">
           <li data-role="list-divider">A</li>
           <li>Anton</li>
           <li>Arabella</li>
           <li data-role="list-divider">B</li>
           <li>Barry</li>
           <li>Bily</li>
        </ul>
     </div>
  </div>

  <script>
      var fastscroll = tau.widget.FastScroll(document.getElementById('list'));
  </script>            
  ```

  After:

  ```
  <div class="ui-page" id="indexscrollbarPage">
     <div class="ui-indexscrollbar" id="indexscrollbar"></div>
     <div class="ui-content">
        <ul class="ui-listview" id="isbList">
           <li class="ui-group-index">A</li>
           <li class="ui-li-static">Anton</li>
           <li class="ui-li-static">Arabella</li>
           <li class="ui-group-index">B</li>
           <li class="ui-li-static">Barry</li>
           <li class="ui-li-static">Bibi</li>
        </ul>
     </div>
  </div>

  <script>
      var isb = tau.widget.IndexScrollbar(document.getElementById('indexscrollbar'));
  </script>        
  ```

- **Gallery**            

  Before:

  ```
  <div data-role="content" data-scroll="none">
     <div data-role="gallery" id="gallery" data-vertical-align="middle"></div>
  </div>

  <script>
      var galleryWidget = tau.widget.Gallery(document.getElementById('gallery'));

      galleryWidget.add('./images/01.jpg');
      galleryWidget.add('./images/02.jpg');
      galleryWidget.add('./images/03.jpg');
      galleryWidget.refresh(1);
  </script>            
  ```

  After:

  ```
  <div id="gallerySection" class="ui-content ui-section-changer" data-orientation="horizontal">
     <div>
        <section class="gallery-section">
           <img src="images/01.jpg"/>
        </section>
        <section class="gallery-section">
           <img src="images/02.jpg"/>
        </section>
     </div>
  </div>

  <script>
      var sectionChangerElement = document.getElementById('gallerySection'),
          sectionChangerWidget = tau.widget.SectionChanger(sectionChangerElement),
          newSectionElement = document.createElement('section');

      newSectionElement.innerHTML = '<img src="images/03.jpg">';
      sectionsParentNode.appendChild(newSectionElement);
      sectionChangerWidget.refresh();
      sectionChangerWidget.setActiveSection(1);
  </script>       
  ```

- **List Divider**            

  Before:

  ```
  <ul data-role="listview">
     <li data-role="list-divider">Item styles</li>
     <li><a href="#">Normal lists</a></li>
     <li><a href="#">Normal lists</a></li>
     <li><a href="#">Normal lists</a></li>
  </ul>           
  ```

  After:

  ```
  <ul class="ui-listview">
     <li class="ui-group-index">Item styles</li>
     <li class="ui-li-anchor"><a href="#">Normal lists</a></li>
     <li class="ui-li-anchor"><a href="#">Normal lists</a></li>
     <li class="ui-li-anchor"><a href="#">Normal lists</a></li>
  </ul>       
  ```

- **Notification**            

  Before:

  ```
  <div data-role="page" id="demo">
     <div data-role="notification" id="notification" data-type="popup">
        <p>Notification Demo TEST</p>
     </div>
     <div data-role="header" data-position="fixed">
        <h1>Notification</h1>
     </div>
     <div data-role="content">
        <div data-role="button" id="noti-demo">Show small popup</div>
     </div>
  </div>

  <script>
      var notification = tau.widget.Notification(document.getElementById('notification')),
          buttonEl = document.getElementById('noti-demo');

      buttonEl.addEventListener('vclick', function() {
          notification.open();
      });
  </script>            
  ```

  After:

  ```
  <div data-role="content">
     <a class="ui-btn" id="open" data-inline="true">Button</a>
     <div id="popup_toast" data-role="popup" class="ui-popup ui-popup-toast">
        <div class="ui-popup-content">
           Toast popup text Toast popup text
        </div>
     </div>
  </div>

  <script>
      var btn = document.getElementById('open');

      btn.addEventListener('vclick', function() {
          tau.openPopup('#popup_toast');
      });
  </script>       
  ```

- **Progress Bar**            

  Before:

  ```
  <div data-role="progressbar" id="progressbar"></div>

  <script>
      var progressbarWidget = tau.widget.ProgressBar(document.getElementById('progressbar'));

      progressbarWidget.value(30);
  </script>           
  ```

  After:

  ```
  <div class="ui-progress" data-type="bar" id="progressbar"></div>

  <script>
      var progressWidget = tau.widget.Progress(document.getElementById('progressbar'));

      progressWidget.value(30);
  </script>       
  ```

- **Search Bar**            

  Before:

  ```
  <input type="search" name="search" id="search-bar"/>

  <script>
      var searchBarElement = document.getElementById('searchbar'),
          searchBarWidget = tau.widget.SearchBar(searchBarElement);

      value = searchBarWidget.disable();
  </script>           
  ```

  After:

  ```
  <input type="search" id="search-test"/>

  <script>
      var searchEl = document.getElementById('search-test'),
          searchWidget = tau.widget.SearchInput(searchEl);

      searchInputWidget.disable();
  </script>       
  ```

- **Select Menu**            

  Before:

  ```
  <select id="selectmenu" data-native-menu="false">
     <option value="1">Item1</option>
     <option value="2">Item2</option>
     <option value="3">Item3</option>
     <option value="4">Item4</option>
  </select>

  <script>
      var element = document.getElementById('selectmenu'),
          widget = tau.widget.SelectMenu(element);

      widget.open();
  </script>            
  ```

  After:

  ```
  <select id="dropdownmenu" data-native-menu="false">
     <option value="1">Item1</option>
     <option value="2">Item2</option>
     <option value="3">Item3</option>
     <option value="4">Item4</option>
  </select>

  <script>
      var element = document.getElementById('dropdownmenu'),
          widget = tau.widget.DropdownMenu(element);

      widget.open();
  </script>       
  ```

- **Tab Bar**            

  Before:

  ```
  <div data-role="header">
     <div data-role="tabbar" id="tab-bar">
        <ul>
           <li><a href="#">Tabbar1</a></li>
           <li><a href="#">Tabbar2</a></li>
           <li><a href="#">Tabbar3</a></li>
        </ul>
     </div>
  </div>

  <script>
      var tabBar = tau.widget.TabBar(document.getElementById('tab-bar'));
  </script>           
  ```

  After:

  ```
  <!--Tabs component is composed with Tabbar and SectionChanger-->
  <div id="tabs" class="ui-tabs">
     <div class="ui-tabbar">
        <ul>
           <li><a href="#" class="ui-btn-active">Tab1</a></li>
           <li><a href="#">Tab2</a></li>
           <li><a href="#">Tab3</a></li>
        </ul>
     </div>
     <div class="ui-section-changer">
        <div>
           <section class="ui-section-active">
              <p>Tab1</p>
           </section>
           <section>
              <p>Tab2</p>
           </section>
           <section>
              <p>Tab3</p>
           </section>
        </div>
     </div>
  </div>

  <script>
      var tabsElement = document.getElementById('tabs'),
          tabs = tau.widget.Tabs(tabsElement);

      tabs.setIndex(1);
  </script>       
  ```

- **Token Text Area**            

  Before:

  ```
  <div data-role="tokentextarea" id="tokentext"></div>

  <script>
      var tokenWidget = tau.widget.TokenTextarea(document.getElementById('tokentext'));

      tokenWidget.add('foobar');
  </script>           
  ```

  After:

  ```
  <div class="ui-text-enveloper"></div>

  <script>
      var textEnveloperElement = document.getElementById('textenveloper'),
          textEnveloper = tau.component.TextEnveloper(textEnveloperElement);

      textEnveloper.add('hello');
  </script>       
  ```

## Event Handling

Some events have changed. The following examples illustrate how to handle events:

- Swipe event    

  In the previous version, the `swipe` event was triggered in every area in the page automatically, but since 2.4, for efficient trigger and handling, the `swipe` event is only triggered when the Gesture event is created.

  To enable the swipe event, use the `enableGesture()` method. The following example shows how to enable the swipe event on the content area:

  ```
  <!--HTML code-->
  <div class="ui-page ui-page-active" id="pageSwipe">
     <header class="ui-header">
        <h2 class="ui-title">Swipe Event</h2>
     </header>
     <div id="content" class="ui-content></div>
  </div>
  ```

  ```
  (function() {
      var page = document.getElementById('pageSwipe');
      page.addEventListener('pagebeforeshow', function() {
          var content = document.getElementById('content');
          tau.event.enableGesture(content, new tau.event.gesture.Swipe({
              orientation: 'horizontal'
          }));
      });
  }());
  ```

  When the `swipe` event is enabled, the application can handle this event with some event detail data:

  ```
  (function() {
      var content = document.getElementById('content');

      content.addEventListener('swipe', function(e) {
          console.log('swipe direction = ' + e.detail.direction);
      });
  }());
  ```

  For more information, see the [Gesture Event API](../../api/latest/ui_fw_api/Gesture_Events/gesture.htm).

- Tap event    

  Since 2.4, the `tap` event has been deprecated. Use the `click` event instead.

  If the application has one button in the content area:

  ```
  <div class="ui-content">
     <a id="btn" href="#" class="ui-btn">Click me</a>
  </div>
  ```

  Before:

  ```
  var button = document.getElementById('btn');

  button.addEventListener('tap', eventHandler);
  ```

  After:

  ```
  var button = document.getElementById('btn');

  button.addEventListener('click', eventHandler);
  ```

## Related Information
* Dependencies  
  - Tizen 2.4 and Higher for Mobile
