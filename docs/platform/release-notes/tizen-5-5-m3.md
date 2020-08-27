# Tizen 5.5 Public M3

Release date: Aug. 27, 2020


The Tizen 5.5 Public M3 release provides new features for wearable, such as AOD viewer, Sticker framework, Aurum for UI test automation, and Battery-Monitor framework.


## Release Details

- [Getting source code](http://review.tizen.org/git/) (Tizen 5.5 M2 source codes are under **tizen_5.5** branch.)

- Getting binaries and images

  - Base: [http://download.tizen.org/releases/milestone/tizen/5.5-base/tizen-5.5-base_20200621.1/](http://download.tizen.org/releases/milestone/tizen/5.5-base/tizen-5.5-base_20200621.1/)
  - Profile(Wearable): [http://download.tizen.org/releases/milestone/tizen/5.5-unified/tizen-5.5-unified_20200812.1/](http://download.tizen.org/releases/milestone/tizen/5.5-unified/tizen-5.5-unified_20200812.1/)

- [How to flash to a device](../developing/flashing.md)


## Release Notes

### Application framework

#### New and changed features

- App-defined-loader
  - The new API set for preparing a specific app-defined loader has been provided.
- Added widget-service API set
  - Functions to enable and disable by widget class have been provided.
- API set for watch viewer
  - The new API set for watch viewer has been provided.
- API set for AOD viewer
  - The new API set for AOD viewer has been provided.
- Watchface-complication
  - The additional API set for watchface-complication has been provided.


### Window System

#### New and changed features

- tzsh-quickpanel
  - tzsh_quickpanel_scrollable_state_set/get API and enumeration have been added.
  - tzsh_quickpanel_scrollable_set/get API has been deprecated.


### UI framework

#### New and changed features

- Aurum, an automation framework for UI testing has been added.
- efl-theme-tizen-wearable has been updated with new UX.
- Sticker framework
  - Support for API to set/get display type of sticker (emoji, wallpaper) has been added.
  - Support for API to delete sticker using URI has been added.
  - API set for managing recent stickers history has been added.
  - A new API for registering any change in sticker info has been added.


### Network and Connectivity

#### New and changed features

- C# API Changes
  - Tizen.Network.Bluetooth
    - IBluetoothServerSocket
      - API for sending data in byte has been added.
      - API for sending data in string has been deprecated.
    - SocketData
      - API to get data in byte has been added.
      - API to get data in string has been deprecated.


### Service framework

#### New and changed features

- Battery-Monitor framework
  - Support for fetching battery information for custom period has been added.
  - Battery monitor API set has been changed to return usage in mAh instead of percentage.
  - Support for C# API set for battery monitor has been added.
  - Support for estimating battery information for external tools has been added.
    - Support for estimating approximate power usage per application ID has been added.
    - Support for estimating power usage per system resource has been added.
    - Per-app statistics of state and events has been added.
  - The API set to provide custom time period support and return usage in mAh has been changed.
    - API for fetching information for an application for a particular resource over a certain duration of time has been updated.
    - API for fetching total battery usage information of an application, combining all the resources over certain duration of time has been updated.
    - API for fetching battery usage values for all the resources separately used by an application ID for a certain duration has been updated.
    - API for fetching battery usage values for a particular resource over certain duration of time has been updated.
- Contact Framework
  - Support for getting count for contact records has been added for better performance.
    - API for fetching count of searched records has been added.
    - API for fetching count of searched record with range has been added.
    - API set for fetching count for searched record with query has been added.


### Tizen .NET

#### New and changed features

- Xamarin.Forms
  - Support for Xamarin.Forms 4.6.0 has been added.
- Tizen.CircularUI
  - Support for Wearable UI extension (Tizen.Wearable.CircularUI) 1.5.0 has been added.
