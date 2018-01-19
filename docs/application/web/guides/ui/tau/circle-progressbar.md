# Creating Circle-shaped Progress Bars

You can create a circle-shaped progress bar component with the CircleProgressBar API.

This feature is supported in wearable applications only.

The following figure shows the layout of the progress bar component in a rectangular and circular UI.

**Figure: Circle-shaped progress bar component on rectangular and circular devices**

![Circle-shaped progress bar component on a rectangular device](./media/rectangular_progress.png)  ![Circle-shaped progress bar component on a circular device](./media/round_progress.png)

To implement the progress bar component:

1. Edit the HTML code to add the component to your application screen:

   ```
   <div class="ui-page ui-page-active" id="pageCircleProgressBar" data-enable-page-scroll="false">
      <header class="ui-header">
         <h2 class="ui-title">Circle Progress</h2>
      </header>
      <div class="ui-content content-padding">
         <div class="result" id="result"></div>
      </div>
      <footer class="ui-footer ui-grid-col-2">
         <a href="#" class="ui-btn" id="minus">-10%</a>
         <a href="#" class="ui-btn" id="plus">+10%</a>
      </footer>
      <progress class="ui-circle-progress" id="circleprogress" max="100" value="20"></progress>
   </div>
   ```

2. Edit the CSS code to set the visual style of the progress bar:

   ```
   .ui-progressbar-large {
      position: absolute;
      top: 50%;
      left: 50%;
      -webkit-transform: translate3d(-50%, -50%, 0);
   }
   .result {
      font-size: 35px;
      text-align: center;
      top: 33%;
      left: 50%;
      -webkit-transform: translate3d(-50%, -50%, 0);
      position: absolute;
   }

   @media all and (-tizen-geometric-shape: circle) {
      .result {
         top: 50%;
         margin: 0;
      }
      .ui-footer {
         display: none;
      }
   }
   ```

3. Edit the JavaScript code to manage the progress bar events and other functionality:

   ```
   (function() {
       var page = document.getElementById('pageCircleProgressBar'),
           progressBar = document.getElementById('circleprogress'),
           minusBtn = document.getElementById('minus'),
           plusBtn = document.getElementById('plus'),
           resultDiv = document.getElementById('result'),
           isCircle = tau.support.shape.circle,
           progressBarWidget,
           resultText,
           i;

       function printResult() {
          resultText = progressBarWidget.value();
          resultDiv.innerHTML = resultText + '%';
       }

       function clearVariables() {
          page = null;
          progressBar = null;
          minusBtn = null;
          plusBtn = null;
          resultDiv = null;
       }

       function unbindEvents() {
           page.removeEventListener('pageshow', pageBeforeShowHandler);
           page.removeEventListener('pagehide', pageHideHandler);
           if (isCircle) {
               document.removeEventListener('rotarydetent', rotaryDetentHandler);
           } else {
               minusBtn.removeEventListener('click', minusBtnClickHandler);
               plusBtn.removeEventListener('click', plusBtnClickHandler);
           }
       }

       function minusBtnClickHandler() {
           i = i - 10;
           if (i < 0) {
               i = 0;
           }
           progressBarWidget.value(i);
           printResult();
       }

       function plusBtnClickHandler() {
           i = i + 10;
           if (i > 100) {
               i = 100;
           }
           progressBarWidget.value(i);
           printResult();
       }

       function rotaryDetentHandler() {
           /* Get the rotary direction */
           var direction = event.detail.direction,
               value = parseInt(progressBarWidget.value());

           if (direction === 'CW') {
               /* Right direction */
               if (value < 100) {
                   value++;
               } else {
                   value = 100;
               }
           } else if (direction === 'CCW') {
               /* Left direction */
               if (value > 0) {
                   value--;
               } else {
                   value = 0;
               }
           }

           progressBarWidget.value(value);
           printResult();
       }

       function pageBeforeShowHandler() {
           if (isCircle) {
               /* Make the circular progressbar object */
               progressBarWidget = new tau.widget.CircleProgressBar(progressBar, {size: 'full'});
               document.addEventListener('rotarydetent', rotaryDetentHandler);
           } else {
               progressBarWidget = new tau.widget.CircleProgressBar(progressBar, {size: 'large'});
               minusBtn.addEventListener('click', minusBtnClickHandler);
               plusBtn.addEventListener('click', plusBtnClickHandler);
           }

           i = parseInt(progressBarWidget.value());
           resultDiv.innerHTML = i + '%';
       }

       function pageHideHandler() {
           unbindEvents();
           clearVariables();
           /* Release the object */
           progressBarWidget.destroy();
       }

       page.addEventListener('pagebeforeshow', pageBeforeShowHandler);
       page.addEventListener('pagehide', pageHideHandler);
   }());
   ```

## Related Information
* Dependencies   
   - Tizen 2.3.1 and Higher for Wearable
