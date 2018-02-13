# Tizen 2.2.1

Release Date: 09 Nov, 2013



The Tizen 2.2.1 release provides developers with the Tizen kernel, device drivers, middleware subsystems, and Web/Native APIs, necessary to develop future Tizen compliant solutions.



## Release Details

- [Getting source code](http://review.tizen.org/git/) (Tizen 2.2.1 source codes are under **tizen_2.2** branch.)
- [Getting binaries and images](http://download.tizen.org/releases/2.2.1/tizen-2.2.1)
- [How to flash to a device](https://wiki.tizen.org/wiki/Flash_Tizen_2.2_Image_to_Reference_Device)



## Release Notes

Tizen is an open source, standards-based software platform supported by leading mobile operators, device manufacturers, and chip suppliers for multiple device categories, including smartphones, tablets, netbooks, in-vehicle infotainment devices, and smart TVs.

The Tizen Platform consists of the Web framework (APIs), native framework (APIs), and core system.

The Tizen Software Development Kit (SDK) is a comprehensive set of tools for developing Web applications, native applications, and the platform component for Tizen. The SDK contains an install manager, IDE, tools, documents, samples, and a platform image.



### Tizen Platform

#### Common

##### New Features

- Privacy control
  - In Settings, the **Privacy** menu is added.
- System framework
  - Applications can be installed in SD cards.
  - Firmware download supports the USB.org framework test tool and Mac OS X.

#### Web Framework

##### Changed Features

- For Tizen Web API change details, see [Tizen API Change Notes](http://developer.tizen.org/downloads/sdk/2.2.1-api-change-notes).
- Web UI framework
  - Pop-up animation is smoother during the orientation change.
  - Focus navigation using a host keyboard is supported.

##### Fixed Bugs

- Web Runtime
  - Misbehaving issue with W3C permission (such as geolocation and storage quota) pop-up selection has been fixed.
  - Blinking issue with the resize, refresh, and pd open operations in the Web Dynamic Box has been fixed.
  - Web application upgrade issue when the Web Dynamic Box instance is created has been fixed.
- Web UI framework
  - Page content top and bottom padding are set to 0.
  - Text-ellipsis is added to the list item text.
  - Slider winset release problem has been fixed.
  - Unnecessary scroll view calculation has been removed.
  - Entry autofocus behavior has been fixed.
  - Scroll view scroll position problem has been fixed.

#### Native Framework

##### Changed Features

- Tizen::*
  - The E_USER_NOT_CONSENTED exception has been added to privacy-related APIs.
- Tizen::App
  - The [http://tizen.org/privilege/datacontrol.consumer](http://tizen.org/privilege/datacontrol.consumer) privilege is required to use DataControl.
  - The following APIs have been added in the [http://tizen.org/privilege/datacontrol.consumer](http://tizen.org/privilege/datacontrol.consumer) privilege.Tizen::App::MapDataControl::AddValue (const Tizen::Base::String &dataId, const Tizen::Base::String &key, const Tizen::Base::String &value, RequestId &reqId)Tizen::App::MapDataControl::GetValue (const Tizen::Base::String &dataId, const Tizen::Base::String &key, RequestId &reqId, int pageNo=1, int countPerPage=20)Tizen::App::MapDataControl::RemoveValue (const Tizen::Base::String &dataId, const Tizen::Base::String &key, const Tizen::Base::String &value, RequestId &reqId)Tizen::App::MapDataControl::SetValue (const Tizen::Base::String &dataId, const Tizen::Base::String &key, const Tizen::Base::String &oldValue, const Tizen::Base::String &newValue, RequestId &reqId)Tizen::App::SqlDataControl::Delete (const Tizen::Base::String &dataId, const Tizen::Base::String *pWhere, RequestId &reqId)Tizen::App::SqlDataControl::Insert (const Tizen::Base::String &dataId, const Tizen::Base::Collection::IMap &insertMap, RequestId &reqId)Tizen::App::SqlDataControl::Select (const Tizen::Base::String &dataId, const Tizen::Base::Collection::IList *pColumnList, const Tizen::Base::String *pWhere, const Tizen::Base::String *pOrder, RequestId &reqId, int pageNo=1, int countPerPage=20)Tizen::App::SqlDataControl::Update (const Tizen::Base::String &dataId, const Tizen::Base::Collection::IMap &updateMap, const Tizen::Base::String *pWhere, RequestId &reqId)
  - The following APIs have been added in [http://tizen.org/privilege/application.launch](http://tizen.org/privilege/application.launch) privilege.Tizen::App::AppControl::Stop (void)
- Tizen::Media
  - The following APIs have been added in [http://tizen.org/privilege/audiorecorder](http://tizen.org/privilege/audiorecorder) privilege.Tizen::Media::AudioIn::Prepare (AudioSampleType audioSampleType, AudioChannelType audioChannelType, int audioSampleRate)Tizen::Media::AudioIn::Reset (void)Tizen::Media::AudioIn::Start (void)Tizen::Media::AudioIn::Stop (void)Tizen::Media::AudioIn::Unprepare (void)
- Tizen::System
  - The following SystemInfo keys have been added:
    - [http://tizen.org/feature/screen.size.normal.240.400](http://tizen.org/feature/screen.size.normal.240.400)
    - [http://tizen.org/feature/screen.size.normal.320.480](http://tizen.org/feature/screen.size.normal.320.480)
    - [http://tizen.org/feature/screen.size.normal.540.960](http://tizen.org/feature/screen.size.normal.540.960)
    - [http://tizen.org/feature/screen.size.normal.600.1024](http://tizen.org/feature/screen.size.normal.600.1024)
    - [http://tizen.org/feature/screen.size.normal.1080.1920](http://tizen.org/feature/screen.size.normal.1080.1920)
    - [http://tizen.org/feature/screen.size.all](http://tizen.org/feature/screen.size.all)
- Tizen::Ui
  - Launching time and FPS performance has been enhanced.
  - Touch response has been enhanced.
  - The GUI has been extensively revised for Tizen 2.2.1. Many GUI enhancements to improve clarity and legibility have been made. Some changes, such as adding an effect for controls have been made.
  - The requirements for surrounding texts in SIP (Soft Input Panel) have been changed.

##### Fixed Bugs

- Tizen::App
  - Service application issue with receiving the language setting changed event has been fixed.
- Tizen::Base
  - The case where 2 String objects sharing a string buffer and one of them calling the Replace() method resulted in replacing both String objects if the input-param to be replaced was a whole string has been fixed.
  - The issue with the Contains() method blocking the operation for a long time with a very long string has been fixed.
- Tizen::Base::Utility
  - The issue of failing to get the host of the Uri having only the "?" character without a query has been fixed.
  - Memory leak of the Scanner class has been fixed. The elements in the IList were not removed internally.
- Tizen::Content
  - In some cases, the ContentManager::CreateContent() method returned the E_INVALID_ARG exception even though it had succeeded. This issue has been fixed.
  - The issue of removing the source file when the ContentManager::CreateContent() method fails has been fixed.
  - The issue of the ContentInfo::GetCoordinates() method returning an improper value in some locales has been fixed.
  - The issue of the ContentSearch::SearchN() method not working properly for DateTime type columns has been fixed.
- Tizen::Media
  - AudioIn
    - The audiorecorder privilege is added in the Prepare(), Unprepare(), Start(), Stop(), and Reset() methods.
  - Camera and Player
    - Camera and video play performance enhancements are supported.
- Tizen::Shell
  - The issue of the notification light (LED) not blinking as specified has been fixed.
  - The issue of the Dynamic Box not updating its text when the language setting is changed has been fixed.
  - The issue of the Dynamic Box being removed when the application is upgraded has been fixed.
  - The issue of the Dynamic Box not working properly when the user adds multiple Dynamic Boxes for a single application has been fixed.
- Tizen::Social
  - The issue of not getting the recurrence of an event if the event does not have mandatory recurring information has been fixed.
  - The issue of the initial calendar ID of CalEvent and CalTodo instances not being E_INVALID_RECORD_ID has been fixed.
  - The issue of contact updates failing if some properties of the contact have been removed by another application has been fixed.
  - The issue of Addressbook APIs failing when the caller thread cannot get the database lock in a certain time has been fixed.
- Tizen::Ui::Scenes
  - The issue of application crashing when the scene transition is finished due to the SD card being ejected manually has been fixed.
- Tizen::Ui::Ime
  - The issue of an IME application crashing when accessing a setting value using the Tizen::App::AppSetting class has been fixed.

##### Known Issues

- Tizen::Media
  - When several AudioOut instances are used in an application, the performance can deteriorate. In this case, use OpenAL instead of the AudioOut class.
  - Keep the number of simultaneous working handles in the system, including the AudioOut and Player classes, under 30.

### IDE and Tools

#### New Features

- Common tools
  - Smart Development Bridge (SDB)
    - Password lock mode of the target is supported.
    - SDB timeout setting to has been added to Tizen preferences (default: 5 minutes).
- Web IDE and tools
  - Hybrid multi-app packaging is supported.
  - Configuration editor
    - A feature list is supported.
    - Validation checks for the icon, version, and content elements have been refined and added.
  - jQuery Mobile templates have been updated to jQuery Mobile version 1.3.2.
- Native IDE and tools
  - Debugging
    - The GDB (GNU Debugger) pretty-print feature for basic STL library and Tizen string type is supported, enabling users to debug the value of these types in a human-readable format.
  - Unit Test and Code coverage
    - The code coverage feature in Windows has been defined by filtering the garbage value of the gcda path.

#### Changed Features

- Common tools
  - Smart Development Bridge (SDB)
    - The PATH setting <tizen-sdk>/tools in Linux when SDB is installed has been removed. Run the SDB in the <tizen-sdk>/tools directory or set the PATH variable yourself.
    - Displaying the target name in the connect command is supported.

#### Fixed Bugs

- Common tools
  - The slowness of pushing files in the **Connection Explorer** has been fixed.
  - Smart Development Bridge (SDB)
    - Device detection and CPU drain problem in Mac OS X has been fixed.
- Web IDE and tools
  - The issue of live reload not working in the file mode has been fixed.
  - The issue of 2nd launch not running in the RDS mode has been fixed.
- Native IDE and tools
  - The issue of drag-and-drop failing from the **Connection Explorer** to the **Package Explorer** has been fixed.

#### Known Issues

- Native IDE and tools
  - Debugging of the LaunchOnBoot applications is not supported. If you select the **Launch the application automatically at start-up** option in the **Manifest Editor** or directly set the LaunchOnBoot option to true, debugging can fail.
  - Unit Test
    - Launching to debug using the **Run Checked** option in the **Test Explorer** view can fail depending on the OS, when the command to be executed has many arguments.
- Native UI Builder
  - The text function as ellipsis and line-break is sometimes displayed differently with an actuality operation.
