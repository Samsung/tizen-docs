# Tizen 3.0 Public M4

Release Date: Nov. 30, 2017

Tizen 3.0 public M4 has been released, mainly containing security fixes.

## Release Details

- [Getting source code](http://review.tizen.org/git/) (Tizen 3.0 M4 source codes are under **tizen_3.0** branch.)

- [Getting binaries and images](http://download.tizen.org/releases/milestone/tizen/)
  - Base: [http://download.tizen.org/releases/milestone/tizen/3.0-base/tizen-3.0-base_20171108.1/](http://download.tizen.org/releases/milestone/tizen/3.0-base/tizen-3.0-base_20171108.1/)
  - Mobile: [http://download.tizen.org/releases/milestone/tizen/3.0-mobile/tizen-3.0-mobile_20171119.1/](http://download.tizen.org/releases/milestone/tizen/3.0-mobile/tizen-3.0-mobile_20171119.1/)
  - Wearable: [http://download.tizen.org/releases/milestone/tizen/3.0-wearable/tizen-3.0-wearable_20171121.1/](http://download.tizen.org/releases/milestone/tizen/3.0-wearable/tizen-3.0-wearable_20171121.1/)

- [How to flash to a device](../developing/flashing.md)


## Release Notes

### Security Fixes

- Fixed 32 CVEs and 15 manually detected security vulnerabilities in 13 modules

  For example,

  - CVE 2015-8659 (Score 10.0) has been fixed.
    The idle stream handling in nghttp2 before 1.6.0 allows attackers to have unspecified impact via unknown vectors, aka a heap-use-after-free bug.
  - CVE 2017-10989 (Score 9.8) has been fixed.
    The getNodeSize function in ext/rtree/rtree.c in SQLite through 3.19.3, as used in GDAL and other products, mishandles undersized RTree blobs in a crafted database, leading to a heap-based buffer over-read or possibly unspecified other impact.


## Tizen 3.0 Platforom(API) for Tizen Studio 1.3

Release Date: Oct. 11, 2017


Tizen Studio 1.3 has Tizen 3.0 Platform updates.

### UI Framework

#### New and Changed Features

- An API to support the ScreenReader functionality has been added to the wearable profile

- The elementary API has been added to the wearable profile:

  - The following API allows you to retrieve the window ID:
    - elm_win_window_id_get()

- The efl-extension APIs have been added to the wearable profile:

  - The following APIs allow you to set and get the mirror mode for a circle object:

    - eext_circle_object_mirrored_set()
    - eext_circle_object_mirrored_get()

    The mirror mode means that circle components are rendered in the opposite direction.

### Network and Connectivity

#### New and Changed Features

- Data network privileges have been modified:
  - In the mobile, wearable and TV profiles, the [http://tizen.org/privilege/internet](http://tizen.org/privilege/internet) privilege has been added for use with the NSD (Network Service Discovery) feature.

### Security

#### New and Changed Features

- The Libcynara-creds-self package has been added:
  - A credential helper library has been added for self context used in cynara checks.
- openssl has been upgraded:
  - The openssl version has been upgraded to 1.0.2k to fix the following CVEs:
    - CVE-2017-3731, CVE-2017-3732, CVE-2016-7055, CVE-2017-3733

### Web Framework

#### New and Changed Features

- The WebWidget API has been added to the wearable profile:
  - The WebWidget API enables Web widgets to communicate with Web applications by providing functionalities to set and get data and receive user content.
