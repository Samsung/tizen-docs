# Tizen Studio

**Tizen Studio 3.2 is now launched!**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![Download](media/ic_docs_download.png)  **Download**](https://developer.tizen.org/development/tizen-studio/download)

<style>
#main:before, #main:after {
    content: "";
    display: table;
}

.docs-ui-started [class^="docs-ui-"] {
    width: 60%; 
    height: 230px;
    padding: 50px 0;
    text-align: center;
    border: 0 none;
    border-top: 1px solid #dadada;
    border-bottom: 1px solid #dadada;
    box-sizing: border-box;
    position: relative;
    float: left;
    margin: 1 auto 20px;
}

.docs-ui-started [class^="docs-ui-"]>span {
    display: block;
    color: #333;
    line-height: 32px;
    position: relative;
    
}

@media (max-width: 800px)
.docs-ui-started .docs-ui-wearable:before, .docs-ui-started .docs-ui-tv:before, .docs-ui-started .docs-ui-mobile:before, .docs-ui-started .docs-ui-widget:before, .docs-ui-started .docs-ui-watch:before {
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
    background: url(media/Download.png) no-repeat center top;
    background-position: 0 0 !important;
}
.docs-ui-started .docs-ui-wearable {
    width: 20%;
    padding-left: 50;
    /* border-right: 1px solid #d1d1d1; */
}

.docs-ui-started .docs-ui-tv:before {
    content: "";
    margin: auto;
    position: relative;
    display: block;
    width: 85px;
    height: 90px;
    background: url(media/Tools.png) no-repeat center top;
    background-position: 0 0 !important;
}
.docs-ui-started .docs-ui-tv {
    width: 20%;
    padding-left: 50;
}


.docs-ui-started .docs-ui-widget:before {
    content: "";
    display: block;
    margin: auto;
    position: relative;
    width: 70px;
    height: 90px;
    background: url(media/SDK.png) no-repeat center top;
    background-position: 0 0 !important;
}
.docs-ui-started .docs-ui-widget {
    width: 20%;
    padding-left: 50;
    /* border-right: 1px solid #d1d1d1; */
}

.docs-ui-started .docs-ui-watch:before {
    content: "";
    display: block;
    margin: auto;
    position: relative;
    width: 90px;
    height: 90px;
    background: url(./media/IDE.png) no-repeat center top;
    background-position: 0 0 !important;
}
.docs-ui-started .docs-ui-watch {
    width: 19%;
    padding-left: 50;
    /* border-right: 1px solid #d1d1d1; */
}


.docs-ui-started.docs-ui-mobile {
    width: 19%;
    padding-left: 50px;
    
}

div {
    display: block;
}

ul.a{
a.docs-btn-more {
    display: inline-block;
    font-size: 13px;
    color: #008aee;
}}
</style>

<section id ="main">

Tizen Studio is an official integrated development environment (IDE) for developing Tizen apps. This environment is built over Eclipse, it presents a unified environment where you can write, edit, debug, build, and publish your app. 

Tizen Studio runs on Windows®, Ubuntu, and in macOS. For more information on the latest release, see the [download] page.

Tizen Studio primarily comprises of: 
- set of fast and feature-rich emulators for devices based on Tizen, for example Smartphone, TV emulator, smart watch
- extensive tool chains to capture performance, usability, version compatibility
- code templates, samples to help you get started 
- components to support new platforms
- system applications and drivers 
- utilities for compiling applications to Tizen RT (Tizen RTOS kernel variant)

Follow these links to explore more about Tizen Studio: 

<div class="docs-ui-started">
  <div class="docs-ui-wearable">
    <span>
    <a href="https://developer.tizen.org/development/tizen-studio/download" class="docs-btn-more">Download</a>
        </span>
  </div>

  <div class="docs-ui-tv">
    <span>
     <a href="native-tools/index.md" class="docs-btn-more">Native Tools</a><br>
          <a href="web-tools/index.md" class="docs-btn-more">Web Tools</a>
    </span>
  </div>
 
   <div class="docs-ui-widget">
    <span>
    <a href="extension-sdk/overview.md" class="docs-btn-more">Extension SDK</a><br>
    <a href="configurable-sdk/configurable-sdk.md " class="docs-btn-more">Configurable SDK</a>
    </span>
  </div>
  
  <div class="docs-ui-widget">
    <span>
    <a href="platform-tools/overview.md" class="docs-btn-more">Platform IDE </a><br>
    <a href="rt-ide/overview.md" class="docs-btn-more">Tizen RT IDE </a>
    </span>
  </div>
  </div>
</section>
