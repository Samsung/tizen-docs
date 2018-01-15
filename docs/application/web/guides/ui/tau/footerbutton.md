# Creating Footer Buttons

You can create a footer button component that is supported in both a rectangular and circular UI.

This feature is supported in wearable applications only.

The following figures show the layout of the footer button component in a rectangular and circular UI.

**Figure: Footer button component on rectangular and circular devices**

![Footer button on a rectangular device](./media/rectangular_footer.png) ![Footer button on a circular device](./media/round_footer.png)

**Figure: Multiple footer buttons on rectangular and circular devices**

![Multiple footer buttons on a rectangular device](./media/rectangular_multibtn.png) ![Multiple footer buttons on a circular device](./media/round_multibtn.png)

The footer button on the circular UI has the `ui-bottom-button` class. When there are multiple buttons, the other buttons except for the first button use the drawer component in the circular UI.

To implement footer buttons:

- To implement a single footer button:

  Edit the HTML code to add the footer button component to your application screen.

  ```xml
  <div class="ui-page ui-page-active" id="bottomButtonPage">
     <header class="ui-header">
        <h2 class="ui-title">Bottom Button</h2>
     </header>
     <div class="ui-content content-padding">
        It was a real pleasure for me to finally get to meet you. My colleagues join me in sending you our holiday greetings.
     </div>
     <footer class="ui-footer ui-bottom-button">
        <a href="#" class="ui-btn">Button</a>
     </footer>
  </div>
  ```

- To implement multiple footer buttons:

  1. Edit the HTML code to add the footer button components to your application screen.

     When there are multiple buttons, the buttons (except for the first button) use the drawer in the circular UI.

     ```xml
     <div class="ui-page ui-page-active" id="bottomButtonWithMorePage">
        <header class="ui-header">
           <h2 class="ui-title">Multiple Buttons</h2>
        </header>
        <div class="ui-content content-padding">
           It was a real pleasure for me to finally get to meet you. My colleagues join me in sending you our holiday greetings.
        </div>

        <a class="drawer-handler"></a>

        <!--Circle profile-->
        <div id="moreoptionsDrawer" class="ui-drawer drawer-elem" data-drawer-target="#bottomButtonWithMorePage" data-position="right" data-enable="true" data-drag-edge="1">
           <div id="selector" class="ui-selector">
              <div class="ui-item show-icon" data-title="2"></div>
              <div class="ui-item human-icon" data-title="3"></div>
           </div>
        </div>

        <footer class="ui-footer ui-grid-col-3 ui-bottom-button">
           <a href="#" class="ui-btn">1</a>
           <a href="#" class="ui-btn">2</a>
           <a href="#" class="ui-btn">3</a>
        </footer>
     </div>
     ```

  2. Edit the CSS code to set the visual style of the buttons:

     ```css
     .drawer-elem {
        display: none;
     }

     @media all and (-tizen-geometric-shape: circle) {
        .drawer-handler {
           width: 24px;
           height: 115px;
           position: fixed;
           top: 122px;
           right: 0;
           color: transparent;
           background-color: #a4a4a4;
           -webkit-mask-image: url(/* Image path */);
           -webkit-mask-size: 18px 36px;
           -webkit-mask-repeat: no-repeat;
           -webkit-mask-position: 0 40px;
        }
        .ui-bottom-button a + a {
            display: none;
        }
     }
     ```

  3. Edit the JavaScript code to manage the footer button events and other functionalities:

     ```javascript
     (function() {
         var page = document.querySelector('#bottomButtonWithMorePage'),
             drawer = page.querySelector('#moreoptionsDrawer'),
             handler = page.querySelector('.ui-more');

         page.addEventListener('pagebeforeshow', function() {
             if (tau.support.shape.circle) {
                 tau.helper.DrawerMoreStyle.create(drawer, {
                     handler: '.drawer-handler',
                 });
             }
         });
     })();
     ```

## Related Information
* Dependencies     
  - Tizen 2.3.1 and Higher for Wearable
