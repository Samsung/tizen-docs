# Creating Expandable Headers

You can create an expandable header component for your application. The expandable header offers events to support interactivity with other components.

This feature is supported in wearable applications only.

The following figure shows the layout of the header component in a rectangular and circular UI.

**Figure: Header component on rectangular and circular devices**

![Header component on a rectangular device](./media/rectangular_header.png) ![Header component on a circular device](./media/round_header.png)

To implement the header component, edit the HTML code to add the header component to your application screen:

```
<div class="ui-page ui-page-active" id="headerPage">
   <header class="ui-header" id="myHeader">
      <h2 class="ui-title">Long title with ExpandableHeader</h2>
   </header>
   <div class="ui-content content-padding">
      Header is expandable in Circular UI.
   </div>
</div>
```

The header component supports the following events.

**Table: Header component events**

| Event name             | Description                              |
| ---------------------- | ---------------------------------------- |
| `headerexpand`         | Triggered when the header starts to expand. |
| `headerexpandcomplete` | Triggered after the header has fully expanded. |
| `headercollapse`       | Triggered when the header returns to the state before expanding. |

You can use the `headerexpand` and `headercollapse` events if you need to do something when the header expands and collapses.

The following examples show header events with Marquee.

```
var page = document.querySelector('#myPage');

page.addEventListener('pagebeforeshow', function() {
    var textElement = page.querySelector('.ui-title'),
        marquee = new tau.widget.Marquee(textElement);
}, false);

page.addEventListener('headercollapse', function() {
    if (marquee) {
        marquee.reset();
    }
}, false);

page.addEventListener('headerexpandcomplete', function() {
    if (marquee) {
        marquee.start();
    }
}, false);
```

## Related Information
* Dependencies
  - Tizen 2.3.1 and Higher for Wearable
