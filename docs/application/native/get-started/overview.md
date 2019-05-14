# Get Started with Native Applications

<style>
#main:before, #main:after {
    content: "";
    display: table;
}

.docs-ui-started [class^="docs-ui-"] {
    width: 25%; 
    height: auto;
    padding: 40px 0;
    text-align: center;
    border: 0 none;
    border-top: 1px solid #dadada;
    border-bottom: 1px solid #dadada;
    box-sizing: border-box;
    position: relative;
    float: left;
    margin: 0 auto 20px;
}

.docs-ui-started [class^="docs-ui-"]>span {
    display: block;
    color: #333;
    line-height: 29px;
    position: relative;
	
}

@media (max-width: 780px)
.docs-ui-started .docs-ui-wearable:before, .docs-ui-started .docs-ui-widget:before, .docs-ui-started .docs-ui-watch:before, .docs-ui-started .docs-ui-mobile:before {
    height: 85px;
    margin: 0 auto 25px;
    align: center;
    background-position: 0 6px;
}
.docs-ui-started .docs-ui-wearable:before {
    content: "";
    display: block;
    margin: auto;
    position: relative;
    width: 70px;
    height: 90px;
    background: url(./media/wearable_getstarted.png) no-repeat center top;
    background-position: 0 0 !important;
}
.docs-ui-started .docs-ui-wearable {
    width: 25%;
    padding-left: 50;
    /* border-right: 1px solid #d1d1d1; */
}

.docs-ui-started .docs-ui-widget:before {
    content: "";
    margin: auto;
    position: relative;
    display: block;
    width: 85px;
    height: 90px;
    background: url(./media/widget_getstarted.png) no-repeat center top;
    background-position: 0 0 !important;
}
.docs-ui-started .docs-ui-widget {
    width: 25%;
    padding-left: 50;
}

.docs-ui-started .docs-ui-watch:before {
    content: "";
    margin: auto;
    position: relative;
    display: block;
    width: 85px;
    height: 90px;
    background: url(./media/watch_getstarted.png) no-repeat center top;
    background-position: 0 0 !important;
}
.docs-ui-started .docs-ui-watch {
    width: 25%;
    padding-left: 50;
}

.docs-ui-started .docs-ui-mobile:before {
    content: "";
    margin: auto;
    position: relative;
    display: block;
    width: 70px;
    height: 90px;
    background: url(./media/mobile_getstarted.png) no-repeat center top;
    background-position: 0 0 !important;
	
}
.docs-ui-started.docs-ui-mobile {
    width: 25%;
    padding-left: 50px;
	
}

div {
    display: block;
}

a.docs-btn-more {
    display: inline-block;
    font-size: 14px;
    color: #008aee;
}
</style>

<section id ="main">
Tizen Native applications are developed in C. You can use the available native API modules to have advanced system settings and additional functionalities.

To create your first Tizen Native application, the following profiles are available:
<div class="docs-ui-started">
  <div class="docs-ui-wearable">
    <span>
    <a href="wearable/first-app.md" class="docs-btn-more">Wearable Native Application</a>
	<p> Applications targeted to run on smart watches. It can be optimized for small screens. </p>
    </span>
  </div>

   <div class="docs-ui-watch">
    <span>
     <a href="wearable-watch/first-app-watch.md" class="docs-btn-more">Wearable Native Watch Application</a>
	 <p> Applications that are customized watch faces that appear as the device home screen. </p>
    </span>
  </div>
  
  <div class="docs-ui-widget">
    <span>
     <a href="wearable-widget/first-app-widget.md" class="docs-btn-more">Wearable Native Widget Application</a>
	 <p> Applications that can be shown by specific UI applications such as home screen. </p>
    </span>
  </div>
  
   <div class="docs-ui-mobile">
    <span>
    <a href="mobile/first-app.md" class="docs-btn-more">Mobile Native Application</a>
	<p> Applications targeted to run on smart phones. It can take advantage of the functionalities available on smart phones. </p>
    </span>
  </div>

</div>
</section>

The examples in each profile explains a simple application with a basic UI and minimal functionality.
Get familiar with the example first, and then you can build more complex applications.


