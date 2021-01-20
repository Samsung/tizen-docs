# FAQs

This page answers to the most commonly asked questions or errors that you may encounter while installing or developing apps in Tizen Studio.

 <style>
         pre {
  display: block;
  font-family: monospace;
  white-space: pre-line;
  margin: 20 em 70;
  /*! white-space:pre-wrap; */
}

label {
         font-size: 18px;
         cursor: pointer;
         padding: 0em 0em 0.8em 6px;
         }
         label:hover {
         color: ##008aee;
         }
         label:hover:before {
         background: #e6e6e6;
         }
         label:before {
         text-align: center;
         content: counter(li);
         border: 10px solid #008aee;
         border-radius: 40px;
         display: inline-block;
         width: 47px;
         height: 45px;
         line-height: 28px;
         font-size: 18px;
         margin: 4px 0.5em 0px 0px;
         color:#008aee;
         }
         .css-accordion {
         list-style-type: none;
         counter-reset: li;
         padding: 20px;
         margin: 20px;
         width: 600px;
         repeat top left;
         /*---- End .accordion-item ----*/
         }
         .css-accordion .accordion-item {
         counter-increment: li;
         padding: 0;
         margin: 0;
         }
         .css-accordion .accordion-item .item-content-container {
         border-left: 9px solid #008aee;
         padding: 7px 0px;
         margin: -23px 0px -4px 25px;
         }
         .css-accordion .accordion-item .item-content-container .item-content {
         background: #eee;
         padding: 0px 0em;
         overflow: hidden;
         margin: 11px 0 0px 40px;
         border-radius: 2px;
         box-shadow: inset 0 2px 8px rgba(241, 235, 235, 0.5), 0 1px 2px rgba(255, 255, 255, 0.9);
         }
         .css-accordion .accordion-item .item-content-container .item-content p {
         margin: 0.5em 0;
         font-size: 14px
         text-shadow: 0 1px 1px rgba(181, 99, 99, 0.9);
         color: #090808;
         }
         .css-accordion .accordion-item input[type=radio] {
         display: none;
         /*---- End &:checked ----*/
         }
         .css-accordion .accordion-item input[type=radio] ~ .item-content-container {
         overflow: hidden;
         }
         .css-accordion .accordion-item input[type=radio] ~ .item-content-container .item-content {
         height: 0;
         transition: all 0.3s linear;
         }
         .css-accordion .accordion-item input[type=radio]:checked ~ .item-content-container {
         height: auto;
         overflow: visible;
         }
         .css-accordion .accordion-item input[type=radio]:checked ~ .item-content-container .item-content {
         height: inherit;
         /*! overflow-y: auto; */
         transition: all 0.5s linear;
         }
         .css-accordion .accordion-item input[type=radio]:checked + label {
         color: #008aee;
         }
         .css-accordion .accordion-item input[type=radio]:checked + label:before {
         background: #f3f3f3;
         }
      
      </style>
   </head>
<body>
   <ol class="css-accordion user-journey">
      <li class="accordion-item stage-1">
         <input type="radio" name="accordion-control" id="stage-1-control" checked="">
            <label for="stage-1-control">How to run Tizen Studio on Ubuntu 18.04?</label>
               <div class="item-content-container">
                  <div class="item-content">
                     <p>Tizen Studio is supported on Ubuntu 18.04. However, Ubuntu 18.04 distribution does not include the runtime library <b>libpng12-0</b>.
                     <p>For optimal installation experience, it is recommend to install the runtime library and run the following command:
                        <pre>
                           $ wget http://mirrors.kernel.org/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1_amd64.deb
                           $ sudo dpkg -i libpng12-0_1.2.54-1ubuntu1_amd64.deb
                        </pre>
                     </p>
                     Generally, installing packages from older distributions may break the `apt` installation system, but since these dependencies are also present in Ubuntu 18.04, the `apt` installation system works flawlessly.</p>
                  </div>
               </div>
      </li>
      <li class="accordion-item stage-2">
         <input type="radio" name="accordion-control" id="stage-2-control">
            <label for="stage-2-control">How to manage certificates on different versions of Ubuntu?</label>
               <div class="item-content-container">
                  <div class="item-content">
                     <p>
                      On Ubuntu, Tizen Certificate Manager stores the passwords of the certificates in the <b>gnome-keyring</b> application. Therefore, you must enable the <b>gnome-keyring</b> application to ensure that Tizen Studio functions smoothly. </p>
                     <p>The remote login in a Linux desktop system does not have the <b>DBUS_SESSION_BUS_ADDRESS</b> variable set in the session. </p>
                     <p>To store and lookup passwords in the <b>host login keyring</b>, you must set the <b>DBUS_SESSION_BUS_ADDRESS</b> variable.</p>
                     <p>For more information, see <a href="https://developer.tizen.org/community/tip-tech/how-manage-certificates-and-package-applications-different-ubuntu-setups)">Manage certificates. </a>
                     </p>
                </div>
             </div>
      </li> 
      <li class="accordion-item stage-3">
         <input type="radio" name="accordion-control" id="stage-3-control">
            <label for="stage-3-control">How to efficiently validate form data in Tizen Web app?</label>
               <div class="item-content-container">
                  <div class="item-content">
                     <p>Form Validation typically occurs at the server end. If the data entered is incorrect or the data is missing, the server responds and you need to re-submit the form with correct information. The whole process incurs lot of time but to effectively validate the form data, see <a href="https://developer.tizen.org/community/tip-tech/form-validation-using-tizen-web">simple form validation in Tizen Web app.</a></p>             
                  </div>
               </div>
      </li>
      <li class="accordion-item stage-4">
         <input type="radio" name="accordion-control" id="stage-4-control">
            <label for="stage-4-control">How to implement vibration API in Tizen Web app?</label>
               <div class="item-content-container">
                  <div class="item-content">
                     <p>Vibration API adds to the user experience and improves overall perception of the application. With vibration API, no third party library is required to implement vibration feature. For more information on implemtation of Tizen Vibration API, see <a href="https://developer.tizen.org/community/tip-tech/vibration-api-tizen-web-app">Vibration API.</a></p>
                  </div>
               </div>
      </li>
      <li class="accordion-item stage-5">
         <input type="radio" name="accordion-control" id="stage-5-control">
            <label for="stage-5-control">How to fix compatibility issues with Tizen Studio?</label>
               <div class="item-content-container">
                  <div class="item-content">
                     <p>Following are the various conditions that can cause compatibility issues:
                        <ul>
                           <li>Using an older workspace in the installed version of Tizen Studio.</li>
                           <li>Using Tizen Web, Tizen Native, and Tizen Native UI Builder perspectives</li>
                           <li>The Tizen Native or Tizen Native Builder perspectives were previously used.</li>
                           <li>After installing the latest version of Tizen Studio and using the installer without installing other tools from Package Manager.</li>
                     </p>
                        </ul>
                           <p>
                           For more information, see <a href="https://developer.tizen.org/community/tip-tech/trouble-shooting-compatibility-previous-versions-tizen-studio">troubleshooting for compatibility.</a>
                           </p>
                  </div>
               </div>
      </li>
         <li class="accordion-item stage-6">
            <input type="radio" name="accordion-control" id="stage-6-control">
            <label for="stage-6-control">How to update Package Manager using CLI?</label>
            <div class="item-content-container">
               <div class="item-content">
                  <p>To update Tizen Studio using CLI Package Manager, use the update command with the following syntax:
                  <pre>package-manager-cli update [--accept-license] [--no-java-check] [--proxy <value>] [-f <file path>] [-p <password>] [--latest] </pre>
                  For information on the command switches, see <a href="https://docs.tizen.org/application/tizen-studio/setup/update-sdk#updating-with-the-cli-package-manager">Updating with CLI Package Manager.</a>
               </div>
            </div>
        </li>
   </ol>