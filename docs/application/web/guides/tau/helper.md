# Using the Helper Script

You can use the TAU helper script to support some components for the Web applications. SnapListMarqueeStyle allows you to create a marquee-able and expandable list style with the SnapListview.

This feature is supported in wearable applications only.

You can use the helper script as follows:

```
<script>
    var helperInstance = tau.helper.<NameSpace>;
</script>
```

The SnapListMarqueeStyle helper provides a helper script to support creating some usable components for the list style. It supports making the list view more effective using the [SnapListview](../../api/latest/ui_fw_api/Wearable_UIComponents/wearable_snaplistview.htm) and [Marquee](../../api/latest/ui_fw_api/Wearable_UIComponents/wearable_marquee.htm) components.

> **Note**  
> This helper script is supported since Tizen 2.3.

The following example shows how to create your own listview style with SnapListMarqueeStyle. In the example, the list item text scrolls horizontally and the sub text appears if the list item is placed in the middle of the screen.

To create a SnapListMarqueeStyle:

1. Edit the HTML code to add the SnapListMarqueeStyle component to your application screen.

   You can add a multiline style listview as follows.

   ```
   <div class="ui-page ui-page-active" id="snaplistTest">
      <header class="ui-header">
         <h2 class="ui-title">Bottom Button</h2>
      </header>
      <div class="ui-content">
         <ul class="ui-listview ui-snap-listview expand-list" id="snapList">
            <li class="li-has-2line">
               <div class="ui-marquee ui-marquee-gradient">1.SnapListview with Marquee SnapListview with Marquee</div>
               <div class="li-text-sub ui-li-sub-text">sub-text</div>
            </li>
            <li class="li-has-2line">
               <div class="ui-marquee ui-marquee-gradient">2.SnapListview with Marquee SnapListview with Marquee</div>
               <div class="li-text-sub ui-li-sub-text">sub-text</div>
            </li>
            <li class="li-has-2line">
               <div class="ui-marquee ui-marquee-gradient">3.SnapListview with Marquee SnapListview with Marquee</div>
               <div class="li-text-sub ui-li-sub-text">sub-text</div>
            </li>
            <li class="li-has-2line">
               <div class="ui-marquee ui-marquee-gradient">4.SnapListview with Marquee SnapListview with Marquee</div>
               <div class="li-text-sub ui-li-sub-text">sub-text</div>
            </li>
         </ul>
      </div>
   </div>
   ```

2. Edit the CSS code to set your list animation style:

   ```
   .ui-listview.expand-list li.li-has-2line .ui-marquee {
      -webkit-transform: translate3d(0, 16px, 0);
      -webkit-transition: all ease .5s;
   }
   .ui-listview.expand-list li.li-has-2line.ui-snap-listview-selected .ui-marquee {
      -webkit-transform: translate3d(0, 0, 0);
      -webkit-transition: all ease 1s;
   }

   .ui-listview.expand-list li.li-has-2line .ui-li-sub-text {
      -webkit-transform: translate3d(0, -20px, 0);
      opacity: 0;
      -webkit-transition: all ease .5s;
   }
   .ui-listview.expand-list li.li-has-2line.ui-snap-listview-selected .ui-li-sub-text {
      -webkit-transform: translate3d(0, 0, 0);
      opacity: 1;
      -webkit-transition: all ease 1s;
   }
   ```

3. Edit the JavaScript code to make your list into a SnapListMarqueeStyle component and manage the list events:

   ```
   <script>
   var page = document.getElementById('snaplistTest'),
       list = document.getElementById('snapList'),
       listHelper;

   page.addEventListener('pageshow', function() {
       listHelper = tau.helper.SnapListMarqueeStyle.create(list, {marqueeDelay: 1000});
   });

   page.addEventListener('pagehide', function() {
       listHelper.destroy();
   });
   </script>
   ```

The following table shows the options you have in creating your SnapListMarqueeStyle component.

**Table: SnapListMarqueeStyle component options**

| Option         | Input type | Default value | Description                              |
| -------------- | ---------- | ------------- | ---------------------------------------- |
| `marqueeDelay` | number     | 0             | Sets the delay time (in milliseconds) for the marquee component. |

You can use the following methods with the SnapListMarqueeStyle:

- `create()`

  Creates the related components for SnapListMarqueeStyle.

  This method is supported since Tizen 2.3.

  The following code example shows the use of the method:
  
    ```
    <ul class="ui-listview ui-snap-listview" id="snapList">
       <li>some element or text</li>
    </ul>

    <script>
       var list = document.getElementById('snapList'),
           listHelper;

       /* Create the helper */
       listHelper = tau.helper.SnapListMarqueeStyle.create(list, {marqueeDelay: 1000});
    </script>
    ```

- `destroy()`

  Destroys the related components for SnapListMarqueeStyle.

  This method is supported since Tizen 2.3. It has no return value.

  The following code example shows the use of the method:

  ```
  <ul class="ui-listview ui-snap-listview" id="snapList">
     <li>some element or text</li>
  </ul>

  <script>
      var list = document.getElementById('snapList'),
          listHelper;

      /* Create the helper */
      listHelper = tau.helper.SnapListMarqueeStyle.create(list, {marqueeDelay: 1000});

      /* Destroy the helper */
      listHelper.destroy();
  </script>
  ```

## Related Information
* Dependencies  
  - Tizen 2.3.1 and Higher for Wearable
