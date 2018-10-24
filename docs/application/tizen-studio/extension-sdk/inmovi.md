# InMobi Tizen Ad SDK Programing Guide

## InMobi Tizen Ad SDK

The InMobi Tizen Ad SDK allows you to monetize your Tizen application with a wide range of advertisement formats. From banner ads to full-screen interstitial ads, you can deliver ads from the InMobi network for a better user experience.

This site introduces InMobi Tizen Ads for Tizen Web applications, native applications, and Unity games.

- **Tizen Web application**: Tizen Web applications use the Tizen Web Framework to interact with the Web subsystems. The application is built using Web languages, such as HTML5, CSS, and JavaScript.
- **Tizen Native application**: Tizen Native application uses EFL (Enlightenment Foundation Libraries) for the application UI. The application is developed using C and it can access advanced device-specific features.
- **Unity game on Tizen**: To use Tizen Ads in your Unity game, you need the Unity SDK version 5.4.1 or above for privilege addition support. The game is developed using C#.

InMobi Tizen Ads allows application sellers to monetize Tizen applications and games with the ads provided by InMobi. The following ad sizes are supported:

- Small banner: 320 X 50 pixels (InMobi slot #15)
- Big banner: 300 X 250 pixels (InMobi slot #10)
- Interstitial: 320 X 480 pixels (InMobi slot #14)

You can [**download the attached zip file**](media/tizen_inmobi_sdk_0831.zip) which has **inmobi-tizen-adsdk_1.0.3.zip, api references for native, unity, and web adlibraries, 3 sample apps, and Unityadlib.unitypackage** at the end of this page.

## Getting Started with InMobi Tizen Ads

To start off, please follow the below steps to create account and register your app with Inmobi.

Step 1 - Send an email to [tizen.onboarding@inmobi.com](mailto:tizen.onboarding@inmobi.com)

Step 2 - You will receive a document stating the terms and conditions for app monetization with InMobi along with a list of details required for account creation and site ids approval

Step 3 - Fill in the required details (only to be TYPED, not handwritten) and share a signed copy with InMobi. A scanned copy should be shared on the above mentioned email id and a hard copy should be mailed to the below mentioned address
  ```text
  Legal Team, INMOBI, 7th Floor, Cessna Business Park,
  Kadubishanahalli, Sarjapur - Outer Ring Road,
  BANGALORE, KARNATAKA 560103
  India
  ```

Step 4 - Once the details are approved, the InMobi team will get back to you within 2 working days with account details and site ids.

Step 5 - Proceed with technical integration as mentioned in the sections below

## Adding the SDK to Your Project

To add the SDK to your project:

- [Download the attached zip file](media/tizen_inmobi_sdk_0831.zip) which has inmobi-tizen-adsdk_1.0.3.zip, api references for native, unity, and web adlibraries, 3 sample apps, and Unityadlib.unitypackage.

1. Choose the InMobi Tizen Ads SDK depending on your application type: native application, Web application, or Unity game:
   - **Tizen Web applications**: Include the InMobi JavaScript file in the application
   - **Native applications**: The InMobi Tizen Ads extension SDK (inmobi-tizen-adsdk_1.0.3.zip)
   - **Unity games**: The InMobi Tizen Ads asset (Unityadlib.unitypackage)
2. Check the following sample applications and games and refer to the code snippets in this tutorial.
   - Unity game sample (UnityAdSample.7z)
   - Native application sample (NativeAdSample.7z)
   - Web application sample (WebAdSample.7z)
3. We recommend you to use the blog on Tizen Ads on [Tizen community](https://samsung.tizenforum.com/) for any issues. If you still face issues, send them to [tizen.ads@samsung.com](mailto:tizen.ads@samsung.com). The API version of the tizen applications using AdSDK should be mandatorily 2.4 or more, otherwise the tizenstore will reject the applications.

## InMobi Tizen Ads for Web Applications

To use InMobi Tizen Ads in Web applications:

1. For Web applications, include the InMobi JavaScript file to use InMobi Tizen ads:

   ```
   <script type="text/javascript" src="https://i.l.inmobicdn.net/sdk/jsac/p1/inmobi.js">
   </script>
   ```

2. Request permission by adding the following privileges and access feature to the config.xml file:  
   ```
   <!--To fetch ads from the InMobi Tizen Ads server-->
   <tizen:privilege name="http://tizen.org/privilege/internet"/>
   <!--To launch the browser for showing ads-->
   <tizen:privilege name="http://tizen.org/privilege/application.launch"/>
   <!--To access cross domains-->
   <access origin="*" subdomains="true"></access>
   ```

3. Configure the parameters for the InMobi Tizen ad \<div\> element:
   - siteid: Two IDs are provided during registration, one for banner ads and one for interstitial ads. Use the respective IDs for the type of ad to be created (Mandatory)
   - slot: Corresponds to the dimensions of the slot or box where the ads appear in your application. (Mandatory)  
     Currently supported slot numbers are 10 (300x250), 14 (320x480), and 15 (320x50).
   - test: This parameter must be true during development and testing phase. It must be made false before publishing the application to receive the live ads.
   - manual: This parameter must be set to true, otherwise it takes the default false value and the ad is rendered before the Web application page is rendered.
   - autoRefresh: This is the auto refresh time in seconds. The minimum accepted value is 20.
   - uIdMap: InMobi Tizen ad id as per user settings for personalized ads.  
   
   ```
   <script type="text/javascript">
       var ad_id = '00000000-0000-0000-000000000000';
   </script>
   
   <script type="text/javascript">
       function requestAd() {
           var inmobi_conf = {
               siteid: "YOUR BANNER SITEID", /* Your banner site ID from InMobi registration */
               slot: '15',
               test: false,
               manual: true,
               autoRefresh: 20, /* In seconds, the minimum accepted value is 20 */
               uIdMap: {TI: ad_id}
           };
           _inmobi.getNewAd(document.getElementById('tizen_15'), inmobi_conf);
       }
   
       function onSuccess(ad) {
           ad_id = ad.id;
           requestAd();
       }
   
       function onError(error) {
           ad_id = '00000000-0000-0000-0000-000000000000';
           requestAd();
       }
   
       function getAdId() {
           try {
               tizen.systeminfo.getPropertyValue('ADS', onSuccess, onError);
           } catch (err) {
               ad_id = '00000000-0000-0000-0000-000000000000';
               requestAd();
           }
       }
   </script>
   
   <body onload="getAdId()">
     <div id="tizen_15">
      <script type="text/javascript" src="https://i.l.inmobicdn.net/sdk/jsac/p1/inmobi.js"></script>
   </div>
   ```

## InMobi Tizen Ads for Native Applications

This section describes the InMobi Tizen Ads APIs for Tizen native (EFL) applications. Familiarize yourself with Tizen native application development and EFL UI development before attempting to integrate the Ads SDK.

The InMobi Tizen Ads SDK (inmobi-tizen-adsdk_1.0.3.zip) includes 1 library (Adlib) and 1 header file. To get started, [download the Tizen studio](https://developer.tizen.org/development/tizen-studio/download). For more information on adding extension SDKs, see [Extension SDKs](../setup/advanced-configuration.md).

To create InMobi Tizen ads in native applications:

1. Request permission by adding the following privileges to the tizen-manifest.xml file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/network.get</privilege>
      <privilege>http://tizen.org/privilege/internet</privilege>
      <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
   </privileges>
   ```

2. Enums that are defined in header to set position, set ad size and error codes.

   ```
   enum banner_adposition_e;

   enum banner_ad_size_e;

   enum adlib_err;
   ```

3. Initialize Adlib.

   To use the functions and data types of Adlib, include the <adlib.h> header file in your application and give reference of adlib library in C++ Linker libraries under project settings.

   The Adlib has to be initialized by passing valid banner and interstitial site IDs obtained in the InMobi registration.

   ```
   #include <adlib.h>

   adlib_err ret;
   ret = adlib_init(const char *banner_site_id, const char *interstitial_site_id, const char *js_namespace, const char *js_src_url, const char *ad_conf_str_name);
   banner_site_id: "YOUR BANNER SITEID" /* Your banner site id from InMobi*/
   interstitial_site_id: "YOUR INTERSTITIAL SITEID" /* Your interstitial site id from InMobi*/
   js_namespace: "_inmobi" /*same string has to be passed*/
   js_src_url: "https://i.l.inmobicdn.net/sdk/jsac/p1/inmobi.js" /*same string has to be passed*/
   ad_conf_str_name: "inmobi_conf" /*same string has to be passed*/
   ```

   To deinitialize Adlib, call the adlib_deinit() function. This is required when exiting the application to free the resources.

   ```
   ret = adlib_deinit();
   ```

4. Create banner ad:

   - Create ad:

     1. Ad object can be added on applications main window or on user defined layout as per application requirement. Add the banner ad by specifying the type of ad along with the layout or window in which the banner ad must be displayed:

        ```
        Evas_Object *ad_obj = NULL;

        adlib_err result = adview_ad_banner_ad(&ad_obj, ad->layout, BANNER_AD_SIZE_BIG);
        ```

     2. Load the created banner ad by calling the adview_banner_load() function:

        ```
        result = adview_banner_load(ad_obj);
        ```

     3. Adlib has a callback mechanism to update the application about the ad state. The following example shows the callbacks the application has to register.

        ```
        void
        set_listeners(void *appdata)
        {
            banner_ad_event_callback_s callback = {0,};
            callback.banner_ad_opened = on_ad_opened;
            callback.banner_ad_load_request_failed = on_request_failed;
            callback.banner_ad_load_request_succeeded = on_request_succeeded;
            adview_banner_ad_register_callbacks(banner_ad_obj, &callback, appdata);
        }
        ```

     4. The adview can be swallowed in to the layout or can be shown as an overlay above the current layout. In the later case, application has to manage the show state of the adview explicitly. On successfull load of bannerad, banner_ad_load_request_succeeded callback will be triggered in which application needs to call the show of bannerad object using native api evas_object_show(). Also while navigating between the views or during loadFailure, application can choose to handle based on its logic, for example it can hide the adview by calling evas_object_hide() or it can show the adview with the old ad

        ```
        void on_request_succeeded(Evas_Object *obj, void *userdata)
        {
        	evas_object_show(obj);
        }
        void on_request_failed(Evas_Object *obj, adlib_err err, void *userdata)
        {
        	evas_object_hide(obj);
        }
        void on_ad_opened(Evas_Object *obj, void *userdata)
        {
        	// Application logic
        }
        ```

   - Manage ad:

     1. By default, the auto refresh option is enabled for banner ads and the ads are refreshed every 30 seconds provided a new ad is downloaded from the server. The application can control the refresh timer as well as disable the auto refresh option as shown in the following example.

        ```
        result = adview_banner_set_enable_auto_refresh(ad_obj, EINA_FALSE);
        result = adview_banner_set_refresh_interval(ad_obj, 40);
        ```

     2. If the application has not swallowed the banner_ad_obj object into the edc part, it can position the ad at predefined positions using the banner_adposition_e enumeration:

        ```
        result = adview_banner_ad_set_position(ad_obj, BANNER_AD_POSITION_TOP_CENTER);
        ```

        Adlib handles the repositioning of the ad object when the device orientation changes. If the application changes the position of the banner_ad_obj object using Evas functions, such as evas_object_move(), the application is responsible for handling device orientation changes.

        By default, the ad object is placed at BANNER_AD_POSITION_BOTTOM_CENTER.

5. Create an interstitial ad:

   - Create ad:

     1. Add the interstitial ad by specifying the layout or window on which interstitial ad has to be displayed:

        ```
        adlib_err result = adview_add_interstitial_ad(ad->layout);
        ```

     2. The application needs to load the interstitial ad, and on successful load, it needs to call show. Once the load is successful, the interstitial_ad_load_request_succeeded callback is triggered. After this, the interstitial ad is ready to be shown.
        ```
        result = adview_interstitial_load();
        ```
        After receiving the interstitial_ad_load_request_succeeded callback, the application can show the ad at any time as per application logic.
        ```
        result = adview_interstitial_show(); /* Show the interstitial ad */
        ```
        Contrary to the banner ad, the call to load does not take care of showing the interstitial ad.

     3. Adlib has a callback mechanism to update the application about the interstitial ad state. The following example shows the callbacks the application has to register.

        ```
        void
        set_listeners(void *appdata)
        {
            interstitial_ad_event_callback_s callback = {0,};
            callback.interstitial_ad_opened = on_ad_opened;
            callback.interstitial_ad_closed = on_ad_closed;
            callback.interstitial_ad_load_request_failed = on_request_failed;
            callback.interstitial_ad_load_request_succeeded = on_request_succeeded;
            adlib_interstitial_ad_register_callbacks(&callback, appdata);
        }
        void on_request_succeeded(void *userdata)
        {
        	// Application logic
        }
        void on_request_failed(adlib_err err, void *userdata)
        {
        	// Application logic
        }
        void on_ad_opened(void *userdata)
        {
        	// Application logic
        }
        void on_ad_closed(void *userdata)
        {
        	// Application logic
        }
        ```

## InMobi Tizen Ads for Unity Games

This section describes the InMobi Tizen Ads APIs for Tizen Unity games.

To get started, the Unity package ('Unityadlib.unitypackage' in the attached zip file) is needed. For more information on setting up the Unity SDK for Tizen, see the [Unity documentation](https://docs.unity3d.com/Manual/index.html). The minimum Unity SDK version for integrating with Tizen is 5.4.1.

To create InMobi Tizen ads for Unity games:

1. The game needs the following capabilities for the Unity game in the Tizen build settings:

   - Network Get
   - Internet
   - AppManagerLaunch

2. Enums that are defined in header to set position, set ad size and error codes:

   ```
   public enum ErrorType

   public enum BannerAdSize

   public enum BannerAdPosition
   ```

3. Initialize Adlib.

   To use the functions of Adlib, get the AdProvider instance by writing the following code in the script file:

   ```
   Using Tizen.AdLib;
   AdProvider adobject = AdProvider.Instance;
   ```

   Initialize Adlib by passing valid banner and interstitial site IDs obtained from the InMobi registration.

   ```
   ErrorType result = adobject.InitAdlib("YOUR BANNER SITEID","YOUR INTERSTITIAL SITEID","_inmobi","https://i.l.inmobicdn.net/sdk/jsac/p1/inmobi.js","inmobi_conf"); // Your banner and interstitial site IDs from InMobi
   ```

   To deinitialize Adlib, call the following function. This is required when exiting the game to free the resources and to destroy the created adviews.

   ```
   result = adobject.DeinitAdlib();
   ```

4. Create banner ads:

   - Create ad:

     1. Add the banner ad by calling the following function:

        ```
        IntPtr adhandle;
        result = adobject.AddBannerAd(BANNER_AD_SIZE_SMALL, out adhandle);
        ```

     2. Load the created banner ad using the BannerAdLoad() function:
        `result = adobject.BannerAdLoad(adhandle);`

     3. The visibility of the ad view has to be managed by the game while switching between views using the following function:

        ```
        result = adobject.BannerAdSetVisibility(adhandle, false);
        ```

     4. Adlib has a callback mechanism to update the game about the ad state. The game has to register the callbacks with Adlib using the following functions:

        ```
        // Implement the BannerAdListener interface

        public class AdListener:BannerAdListener
        {
            public void OnAdLoadSucceeded(IntPtr handle)
            {
                Debug.Log("Entered in to OnAdLoadSucceeded handle is" + handle);
                adobject.BannerAdSetVisibility(handle, true);
            }
            public void OnAdLoadFailed(IntPtr handle, ErrorType error)
            {
                Debug.Log("Entered in to OnAdLoadFailed");
                adobject.BannerAdSetVisibility(handle, false);
            }
            public void OnAdClicked(IntPtr handle)
            {
                Debug.Log("Entered in to OnAdClicked handle is" + handle);
            }
        }

        // Pass the listener object to the AdProvider

        public AdListener adListener = new AdListener();
        ErrorType ret = adobject.SetBannerAdListener(adhandle, adlistener);
        ```

   - Manage ad:

     1. By default, the auto refresh option is enabled for banner ads and the ads are refreshed every 30 seconds provided a new ad is downloaded from the server. The game can control the refresh timer as well as disable the auto refresh option as shown in the following example.

        ```
        result = adobject.BannerAdEnableAutoRefresh(adhandle, false);
        result = adobject.BannerAdSetRefreshInterval(adhandle, 40);
        ```

     2. The game can positon ads at predefined positions using the BannerAdSetPosition() function. Adlib takes care of device orientation changes.

        ```
        result = adobject.BannerAdSetPosition(adhandle, BANNER_AD_POS_TOP_CENTER);
        ```

        The game can positon the ad to any (x, y) position using the BannerAdSetMove() function. The game is responsible for handling the device orientation changes in this situation.

        ```
        result = adobject.BannerAdSetMove(adhandle, 100, 200);
        ```

        By default, the ad object is placed at BANNER_AD_POS_BOTTOM_CENTER.

5. Create an interstitial ad:

   - Create ad:

     1. Add an interstitial ad by calling the following function:

        ```
        ErrorType result = adobject.AddInterstitialAd();
        ```

     2. The game needs to load the interstitial ad and on successful load, it needs to call show. Once the load is successful, the OnAdLoadSucceeded callback is triggered by the Adlib. After this the interstitial ad is ready to be shown.
        ```
        result = adobject.InterstitialAdLoad();
        ```
        After receiving the OnAdLoadSucceeded callback, the game can show the ad at any time.
        ```
        result = adobject.InterstitialAdShow(); // Show the interstitial ad
        ```
        Contrary to the banner ad, the call to load does not take care of showing the interstitial ad.

     3. Adlib has a callback mechanism to update the game about the interstitial ad state. The game has to register listener callbacks with Adlib using the following functions:

        ```
        // Implement the InterstitialAdListener interface

        public class AdListener:InterstitialAdListener
        {
            public void OnAdLoadSucceeded(IntPtr handle)
            {
                Debug.Log("Entered in to OnAdLoadSucceeded handle is" + handle);
            }
                public void OnAdLoadFailed(IntPtr handle, ErrorType error)
            {
                Debug.Log("Entered in to OnAdLoadFailed");
            }
            public void OnAdOpened(IntPtr handle)
            {
                Debug.Log("Entered in to OnAdOpened handle is" + handle);
            }
            public void OnAdClosed(IntPtr handle)
            {
                Debug.Log("Entered in to OnAdClicked handle is"+ handle);
            }
        }

        // Create the listener object and set it to AdObject
        AdListener myListener = new AdListener();
        result = adobject.SetInterstitialAdListener(myListener);
        ```

## Developer Testcases

Please use the testcases for sanity testing after integrating the adlib to your app.

Category: AdFunctionality

1. Clicking on the Ad should open details in Browser window separately.
2. If the orientation of the application changes, the adview should be resized according to current orientation.
3. While loading interstitial ads or interacting with them no sluggish behavior should be observed.

Category: User Experience

1. Sample ads resolution should be proper. They should not be stretched or skewed.
2. Application layout should be designed in such a way that user experience should not be disturbed when ads are not loaded (no white patches).
3. If network is not available and when ads are not displayed, app's user experience should not be impacted.
4. Banner ad position should be handled by app in such a way that it should not cause any hinderance to the buttons or menus.
5. Application should manage to show the banner ad once it receives the adloadsuccess callback. Navigation between views should maintain the showstate as per app design.
6. Ensure that interstitial ad load is successful and then only call show of the adview and pause application events.
7. While navigating between different views of the application, the ads should be hidden/shown properly as per app design.
8. Terminating the application in any scenario (with or without mobile data) should not cause any force closure of the app.
9. During the app pause and resume the ads rendering should be proper.
10. Incase of a list shown in the app, ensure that the list items are not hidden by the ads.

## SDK update

This page will always host the latest version of the Inmobi Tizen Ad SDK. Advertizement service for older versions of the Ad SDK will be supported for only 90 days. When developer receives an email notice to udpate the Ad SDK, it is adviced to update quickly.
