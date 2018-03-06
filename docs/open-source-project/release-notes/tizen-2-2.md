# Tizen 2.2

Release Date: 22 Jul, 2013



The Tizen 2.2 release provides developers with the Tizen kernel, device drivers, middleware subsystems, and Web/Native APIs, necessary to develop future Tizen compliant solutions.



## Release Details

- [Getting source code](http://review.tizen.org/git/) (Tizen 2.2 source codes are under **tizen_2.2** branch.)
- [Getting binaries and images](http://download.tizen.org/releases/2.2/tizen-2.2)
- [How to flash to a device](https://wiki.tizen.org/wiki/Flash_Tizen_2.2_Image_to_Reference_Device)



## Release Notes

Tizen is an open source, standards-based software platform supported by leading mobile operators, device manufacturers, and chip suppliers for multiple device categories, including smartphones, tablets, netbooks, in-vehicle infotainment devices, and smart TVs.

The Tizen Platform consists of the Web framework (APIs), native framework (APIs), and core system.

The Tizen Software Development Kit (SDK) is a comprehensive set of tools for developing Web applications, native applications, and the platform component for Tizen. The SDK contains an install manager, IDE, tools, documents, samples, and a platform image.

### Tizen Platform

#### Web Framework

##### New Features

- Web Runtime

  - New elements: <tizen:content-security-policy>, <tizen:content-security-policy-report-only>, <tizen:allow-navigation>, <tizen:metadata>, <tizen:setting hwkey-event>, and <tizen:box-size use-decoration>
  - New events: appwidgetready and tizenhwkey
  - Web Runtime supports auto-orientation change

- Tizen Web APIs

  - SystemInfo

    - readonly attribute SystemInfoProfile profile;
    - readonly attribute DOMString buildVersion;
    - readonly attribute boolean isAutoRotation;

  - Bluetooth

    - void setChangeListener(BluetoothAdapterChangeCallback listener);
    - void unsetChangeListener();
    - void onstatechanged(boolean powered);
    - void onnamechanged(DOMString name);
    - void onvisibilitychanged(boolean visible);

  - Application

    - ApplicationMetaData[ ] getAppMetaData(optional ApplicationId? id);

  - WebSetting

    - [NoInterfaceObject] interface WebSettingObject

      ​

      ```
      {   readonly attribute WebSettingManager websetting;};
      ```

    - [NoInterfaceObject] interface WebSettingManager

      ​

      ```
      {   void setUserAgentString(DOMString userAgent,                           optional SuccessCallback? successCallback,                           optional ErrorCallback? errorCallback);   void removeAllCookies(optional SuccessCallback? successCallback,                         optional ErrorCallback? errorCallback);};
      ```

  - Notification

    - attribute DOMString? ledColor;
    - attribute unsigned long ledOnPeriod;
    - attribute unsigned long ledOffPeriod;

##### Changed Features

- For Tizen Web API change details, see [Tizen API Change Notes](http://developer.tizen.org/downloads/sdk/2.2-api-change-notes).
- HTML5/W3C
  - Method, attribute, and constructor support updated
    - Media
      - getUserMedia (Partial) - The audio dictionary member (MediaStreamOptions dictionary) is not supported
- Web UI Framework
  - H/W key support
    - H/W key binding support
    - S/W back/menu button is optional
  - Tizen 2.2 UX/GUI
    - New white and black themes
    - Header/footer height is changed
    - Tabbar style is changed
    - Other minor UX changes
- Tizen Web APIs
  - Power : enum "SCREEN_BRIGHT" is deprecated.
    - enum PowerScreenState {"SCREEN_OFF", "SCREEN_DIM", "SCREEN_NORMAL"};

#### Native Framework

##### New Features

- Tizen::App

  - AppControl
    - API for clearing AppControl default selection is added

- Tizen::Media

  - Player
    - SeekVideoKeyFrameCloseTo() method is added to seek the current playback position of the video content to the nearest key frame at the given time if the content contains key frames.

- Tizen::Security

  - SecureElement
    - Supports access to secure elements, such as SIM card, and embedded secure elements
  - Global
    - Security policy is refined
  - Smack
    - A significant number of rules have been removed to allow required access only
    - Mapping Smack rules with native/Web privileges to support better access control on kernel space

- Tizen::Shell

  - Dynamic Box
    - Supports home screen customization
      - Home screen can decorate the Dynamic Box frame
      - Dynamic Box can declare in the manifest file whether such modifications are allowed
  - Notification
    - Supports H/W notification light settings

- Tizen::Social

  - Addressbook
    - Supports storing application launch data in contacts
    - Supports extra data for categories

- Tizen::System

  - SystemInfo
    - http://tizen.org/system/platform.processor and http://tizen.org/system/platform.communication_processor keys are added

- Tizen::Ui

  - UX Update

    - The GUI has been extensively revised for Tizen 2.2. Black theme is now the default theme, and many GUI improvements to improve clarity and legibility have been made. Some changes, such as reduction of height in Header require application to make sure that there is no break in the layout.

  - Touch Effect

    - Supports the Touch Effect to play predefined effects

  - Indicator

    - A new form style for landscape indicator is added (FORM_STYLE_LANDSCAPE_INDICATOR_AUTO_HIDE) and other indicator styles are only for portrait mode. If this new landscape indicator style is not specified for forms, no indicator will be displayed for landscape.

  - Physical menu and back key support

    - Because physical menu and back buttons are mandatory, APIs about back buttons are deprecated and new APIs about menu event handler were added.

  - Controlling effect sounds

    - New APIs are added for enabling and disabling effect sound.

  - Controls

    - New styles for fast scroll are added. (SCROLL_STYLE_FAST_SCROLL_FIXED and TABLE_VIEW_SCROLL_BAR_STYLE_FAST_SCROLL_FIXED for ListView and TableView, respectively). The fast scroll with these new styles will not fade in/out automatically.

      New API to make a password visible is added for EditField.

  - Accessibility and Focus UI

    - Accessibility and Focus UI features are enabled. Accessibility screen reader supports the following languages: English, French, Italian, German, Spanish, and Korean.

##### Changed Features

- For Tizen native API change details, see [Tizen API Change Notes](http://developer.tizen.org/downloads/sdk/2.2-api-change-notes).
- Tizen::Ui
  - Indicator
    - Because indicator UX for landscape is changed, thin indicator for landscape is not supported anymore and the client size is also changed.
  - Controls
    - The height of header is changed and new header and footer styles for large tab are added (HEADER_STYLE_TAB_LARGE and FOOTER_STYLE_TAB_LARGE).
    - The positions of **Cancel** and **No** buttons on MessageBox have changed and are now moved to the left side.

#### Supported Devices

##### Features

- Emulator
  - The Emulator is an x86-based Qemu image which can be run on computers
  - Preloaded applications:
    - Reference Core applications
      - Home and Lock
    - Reference native applications
      - Calculator, Calendar, CalendarService, Camera, Clock, Contacts, Email, Gallery, ImageViewer, Internet, Memo, Messages, MusicPlayer, MyFiles, Phone, Settings, and VideoPlayer
    - Home and Lock applications can be changed from reference core applications to reference native applications with the build configuration.
- Reference target devices
  - The reference target devices are based upon existing commercial target devices
  - Ref.Device-PQ
    - Ref.Device-PQ is a reference target based on Samsung Galaxy S3
  - Preloaded applications:
    - Reference native applications
      - Calculator, Calendar, CalendarService, Camera, Clock, Contacts, Email, Gallery, ImageViewer, Internet, Memo, Messages, MusicPlayer, MyFiles, Phone, Settings, and VideoPlayer

##### Changed Features

- Tizen 2.2 does not support the Ref-210 device due to the absence of H/W keys.
- The Reference Core applications are not updated in Tizen 2.2.

##### Known Issues

- Reference applications are a bit unstable and they will be updated soon.

#### Supported Languages

- The following languages are supported:
  - Armenian
  - Azerbaijani
  - Basque
  - Bulgarian
  - Catalan
  - Chinese
  - Chinese(Singapore)
  - Chinese(HongKong)
  - Chinese(Taiwan)
  - Croatian
  - Czech
  - Danish
  - Dutch
  - English (US)
  - English (UK)
  - English (Philippines)
  - Estonian
  - Finnish
  - French
  - French (Canada)
  - Galician
  - Georgian
  - German
  - Greek
  - Hungarian
  - Icelandic
  - Irish
  - Italian
  - Japanese
  - Kazakh
  - Korean
  - Latvian
  - Lithuanian
  - Macedonian
  - Norwegian
  - Polish
  - Portuguese
  - Portuguese(Brazil)
  - Romanian
  - Russian
  - Serbian
  - Slovak
  - Slovenian
  - Spanish
  - Spanish (Mexico)
  - Swedish
  - Turkish
  - Ukrainian
  - Uzbek
- The following languages are partially supported:
  - Arabic (supports text display and string translation)
  - Hindi (supports text display and string translation)

### IDE and Tools

#### New Features

- General
  - Supports additional signing controls for generating author certificate and distributor1 signature
  - EGit upgraded to 2.3.1 version
- Common Tools
  - Emulator
    - In General Purpose Skin type, the Key window can be docked not only to the right side but also to the left side of the Emulator window.
    - Emulator provides the "3btn Emulator Skin" type for Menu and Back HW key.
  - Emulator Manager
    - Reflects a new user interface
  - Event Injector
  - Install Manager
- Web IDE and Tools
  - Configuration Editor
    - Locale setting and BoxLabel
  - Building and Running
    - Supports Privilege Checker to check the missing privilege and level
      - Shows problems for a missing privilege
      - Quick Fix for adding a missing privilege
      - Shows warning for an unsupported privilege level
    - Supports live editing in Emulator and Simulator
    - Supports Smart Launch
    - Adds an optimization option in Project properties
  - CLI
    - Provides web-build command for building and optimizing Web projects
    - In web-signing command, the -d/--develop option is deprecated. The option is applied by default.
  - Advanced Declaration View
    - Supports HTML editor
      - Shows CSS rules for id/class attributes
      - Shows local source files or preview of local image files for local path attributes
      - Shows declarations of embedded JavaScript code
    - Jump to the Declaration function is added
      - Jump to the Declaration function is added for HTML editor and UI Builder
      - Open Input function for JavaScript editor is changed to Jump to the Declaration function
  - Web UI Builder
    - Supports H/W back key
    - Back Button property is removed on the page
- Native IDE and Tools
  - Debugging
    - Integration with platform launcher
    - Attach Debugging now initially selects the process of the selected project
  - Unit Test and Code Coverage
    - Code Coverage now shows the result automatically when an application is complete
    - Unit Test template is changed for working as a normal UI application
  - CLI
    - Added -f option in *native-gen project* (Overwrite existing files)
    - Refined usage and help messages
  - Added CDT Refactor menu
  - Native UI Builder
    - Supports H/W back key

#### Changed Features

- Supported OS

- The Tizen SDK does not support Ubuntu 11.10 but supports Ubuntu 12.04 and 12.10.

#### Known Issues

- Common IDE
  - Target might not be displayed in Connection Explorer after a target reboot. To fix this issue, run 'sdb kill-server' and 'sdb start-server'.
- Web IDE
  - Tizen Device API does not work in live editing on an Emulator
  - After cleaning the project or restarting IDE, the RDS mode does not work for the first launch.
- Native IDE
  - LLVM-Bitcode/ARM(Experimental) feature is not supported in Windows 64-bit environments
  - Tizen IDE provides 'native-gen makefile' command for some limited cases. So you may need to modify the generated makefile manually.
    - It does not support the subfolders in 'src'; for example, 'Model/file2.cpp'
    - It only supports the default Tizen IDE "Debug" build configuration
- Emulator
  - When the disk storage is full, various incorrect operations may occur
  - The Emulator skin may not be drawn properly on Ubuntu if the graphics driver is not installed or an older version is installed. To fix this issue, update the graphics driver version.
- Dynamic Analyzer
  - Sometimes a screenshot is not taken if the screen or scene change is implemented using an animation technique
  - The analysis of IME and Service Applications is not supported
