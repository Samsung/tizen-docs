# Tizen VS Code Extension 10.4.0 Release Notes

**Release Date:** July 15, 2026


### Features

- **Flutter-Tizen Extension Development Support**  
  Added support for Flutter-Tizen extension development, enabling developers to build and debug Flutter applications for Tizen devices (#231).

- **Prerequisite Installation Modal & Improved System Prerequisite Handling**  
  Added a modal dialog to install missing system prerequisites, with shared installation logic refactored into a common `BaseInstaller` class (#414).

### Bug Fixes

- **Server Extraction Failure in VSCode v1.128.0**  
  Fixed server extraction failing in VSCode v1.128.0, which ships with Node.js 24.17.0 — a version that broke the `extract-zip` library due to a stream API change. Replaced `extract-zip` with `adm-zip` (already a dependency) and updated it to the latest version (#403).

- **Remote Device Deletion Failure**  
  Fixed an issue where deleting a remote device from the device list would fail with "Device with IP undefined not found or deletion failed" after the active device was reset when switching emulators (#399).

- **Wrong Package Name in Prerequisite Checker**  
  Fixed the system prerequisite checker using the wrong package name (`libv4l-0` instead of `libv4l-0t64`), which caused the prerequisite installation modal to appear repeatedly even when the package was already installed (#410).

- **Modal Display During Emulator Download**  
  Fixed an issue where a modal was incorrectly shown during the emulator download process.

- **Package List Ordering**  
  Fixed an ordering issue in the package list display.