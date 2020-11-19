# Quickstart Guide for TV

This quickstart guide walks you through a default installation of Tizen Studio and how to create a basic TV application. Follow the steps or video demo to get hands-on with TV app development, and get yourself up and running instantly.

<style>
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}
.tabs {
  display: block;
  display: flex;
  -webkit-flex-wrap: wrap;
  -moz-flex-wrap: wrap;
  flex-wrap: wrap;
  margin: 0;
  overflow: hidden; }
  .tabs [class^="tab"] label,
  .tabs [class*=" tab"] label {
    cursor: pointer;
    display: block;
    font-size: 1.1em;
    font-weight: 300;
    line-height: 1em;
    padding: 1rem 0;
    text-align: center; }
  .tabs [class^="tab"] [type="radio"],
  .tabs [class*=" tab"] [type="radio"] {
    border-bottom: 1px solid #008aee;
    cursor: pointer;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    display: block;
    width: 100%;
    -webkit-transition: all 0.3s ease-in-out;
    -moz-transition: all 0.3s ease-in-out;
    -o-transition: all 0.3s ease-in-out;
    transition: all 0.3s ease-in-out; }
    .tabs [class^="tab"] [type="radio"]:hover, .tabs [class^="tab"] [type="radio"]:focus,
    .tabs [class*=" tab"] [type="radio"]:hover,
    .tabs [class*=" tab"] [type="radio"]:focus {
      border-bottom: 5px solid #008aee; }
    .tabs [class^="tab"] [type="radio"]:checked,
    .tabs [class*=" tab"] [type="radio"]:checked {
      border-bottom: 10px solid #008aee; }
    .tabs [class^="tab"] [type="radio"]:checked + div,
    .tabs [class*=" tab"] [type="radio"]:checked + div {
      opacity: 1; }
    .tabs [class^="tab"] [type="radio"] + div,
    .tabs [class*=" tab"] [type="radio"] + div {
      display: block;
      opacity: 0;
      padding: 2rem 0;
      width: 90%;
      -webkit-transition: all 0.3s ease-in-out;
      -moz-transition: all 0.3s ease-in-out;
      -o-transition: all 0.3s ease-in-out;
      transition: all 0.3s ease-in-out; }
  .tabs .tab-2 {
    width: 50%; }
    .tabs .tab-2 [type="radio"] + div {
      width: 200%;
      margin-left: 200%; }
    .tabs .tab-2 [type="radio"]:checked + div {
      margin-left: 0; }
    .tabs .tab-2:last-child [type="radio"] + div {
      margin-left: 100%; }
    .tabs .tab-2:last-child [type="radio"]:checked + div {
      margin-left: -100%; }
.tabs .tab-3 {
    width: 50%; }
    .tabs .tab-3 [type="radio"] + div {
      width: 200%;
      margin-left: 200%; }
    .tabs .tab- [type="radio"]:checked + div {
      margin-left: 0; }
    .tabs .tab-2:last-child [type="radio"] + div {
      margin-left: 100%; }
    .tabs .tab-2:last-child [type="radio"]:checked + div {
      margin-left: -100%; }
video {
  width: 100%;
  height: auto;
}
</style>

<div class="tabs">
  <div class="tab-2">
    <label for="tab2-1"><b>Steps</b></label>
    <input id="tab2-1" name="tabs-two" type="radio" checked="checked">
  <div>  
    
  1.  **Download Tizen Studio**

      Tizen Studio runs on all major operating systems. To download the latest version of Tizen Studio, see the <a href="https://developer.tizen.org/development/tizen-studio/download">Download</a> page.

  2. **Install Tizen Studio**

      To install Tizen Studio on your development hardware, see <a href="../setup/install-sdk.md">Installation</a>, and to ensure seamless development experience, see <a href="../setup/prerequisites.md">Prerequisites</a>.

  3. **Create TV project** 
    
      1. Launch Tizen Studio.
      2. In the Tizen Studio menu, select **File > New > Tizen Project**.
      3. In the **New Tizen Project** window that appears, select the **Template** project type and click **Next**.
      4. In **New Tizen Project** wizard, on **Profile & Version** tab, select the **TV** profile with an appropriate version and click **Next**.
      5. Select the **Web Application** type and click **Next**.
      6. In **New Tizen Project** wizard, on **Template** tab, select the **Basic Project** template and click **Next**.
      7. Define **Project name, Package ID**, select the **Location**, and **Working sets** by clicking **More properties**. 
      8. Click **Finish**.
  
      The **New Project** wizard sets up your TV project and creates the basic application files and folders.
        
      To manage **TV application** configuration and to understand the source code, see [Create Your First Tizen TV Web Application](../../web/get-started/tv/first-app.md). 

       After your application code is ready, you must build the application. The build process performs a validation check and compiles and packages your JavaScript and CSS files.
     
  4. **Build your application**

      1. Select your project in the Project Explorer view.

      2. In the Tizen Studio menu, select **Project > Build Automatically**.
  
  5. **Run your application**
   
      Before you run the application, you must [sign your application package with a certificate profile](../tizen-studio/common-tools/certificate-registration.md) in Tizen Studio.
  
      You can run the Web application on the emulator, Samsung Smart TV Simulator, or a real target device.
   
      - To run the application on the emulator, launch an emulator instance in the Emulator Manager, and follow these steps:

        1. In the Tizen Studio menu, select **Tools > Emulator Manager**.
        2. In the **Emulator Manager**, select a TV emulator from the list and click **Launch**. 
      
           The **Device Manager** window with a TV emulator  appears. 

         3. In the Tizen Studio menu, select **Run > Run As**, select **Tizen Web Application**.
       
      - To run the app on simulator. In the Tizen Studio menu, select **Run > Run As**, select **Tizen Web Simulator Application**.
      - To run your application on a real device, see [Running on a Target Device](../../web/get-started/tv/first-samsung-tv-app.md#run-on-a-target-device).

      This quickstart guide explains how to create a basic TV app. However, if you want to create complex app, see [Create Your First Tizen TV Web Application](../../web/get-started/tv/first-samsung-tv-app.md).
  </div>
</div>

<div class="tab-2">
  <label for="tab2-2"><b>Video Demo</b></label>
    <input id="tab2-2" name="tabs-two" type="radio">
      <div>  
        <video width="auto" height="240" controls>
          <source src="../media/tv.mp4" type="video/mp4">
        </video>
      </div>
    </div>
</div>