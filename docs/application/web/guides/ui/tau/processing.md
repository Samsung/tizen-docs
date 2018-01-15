# Creating Full Size Processing Components

You can create a full size processing component with the Processing API.

This feature is supported in wearable applications only.

The following figure shows the layout of the processing component in a rectangular and circular UI.

**Figure: Processing component on rectangular and circular devices**

![Processing component on a rectangular device](./media/rectangular_processing.png) ![Processing component on a circular device](./media/round_processing.png)

To implement the processing component:

1. Edit the HTML code to add the processing component to your application screen:

   ```
   <div class="ui-page ui-page-active" id="pageProcessing" data-enable-page-scroll="false">
      <header class="ui-header">
         <h2 class="ui-title">Processing</h2>
      </header>
      <div class="ui-content content-padding">
         <div class="ui-processing"></div>
         <div class="ui-processing-text">
            Description about progress
         </div>
      </div>
      <div class="ui-processing ui-processing-full-size"></div>
   </div>
   ```

2. Edit the CSS code to set the visual style of the processing component:

   ```
   .ui-processing-full-size {
      display: none;
   }

   @media all and (-tizen-geometric-shape: circle) {
      .ui-processing {
         display: none;
      }
      .ui-processing.ui-processing-full-size {
         display: block;
      }
   }
   ```

## Related Information
* Dependencies   
   - Tizen 2.3.1 and Higher for Wearable
