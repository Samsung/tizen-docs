# Tizen VS Code Extension 10.4.3 Release Notes

**Release Date:** October 2, 2026


### Features

- **Standalone Tool View Parameter**  
  Added view parameter support for the standalone tool launcher, enabling commands to open specific views (e.g., Remote Devices, Create Certificate) directly in the Tauri applications.

- **Server Version Selection**  
  Added support for installing a specific server version from VSCode.

- **Server Process Logging**  
  Added a logging mechanism for the server process.

- **Package Manager - Repository Connectivity Validation**  
  Added repository connectivity validation before saving SDK repository settings.

- **Baseline Tool Prerequisite Checking**  
  Added prerequisite checking for baseline tools.

- **Baseline Tools Update**  
  Updated baseline tools to the 10.1.2 release.

- **Emulator Manager on Apple Silicon**  
  Enabled the Emulator Manager on Apple Silicon macOS for special cases.

### Bug Fixes

- **Emulator - Tizen 11.0 on macOS**  
  Fixed QEMU acceleration options and binary path for Tizen 11.0 emulator on macOS.

- **Unified UI - Command Behavior**  
  Fixed "Tizen: Remote Devices" and "Tizen: Create Certificate" commands to open the correct views.

- **Left Sidebar Actions**  
  Fixed left sidebar buttons getting enabled before core packages finish installation.

- **Device Manager - Active Target**  
  Fixed the active target device not updating when selecting another device in Device Manager.

- **Certificate Manager - Samsung Certificate Profile**  
  Fixed Samsung Certificate creation with Partner privilege creating a distributor certificate with the wrong class.

- **RDS - Status Bar on Reconcile**  
  Fixed RDS status bar showing an active icon when reconcile is called while RDS is off.

- **RDS - Build-Needed Status**  
  Fixed RDS not recognizing that a build is needed and not setting stale status when RDS is re-enabled after file changes.

- **System Prerequisite - Logging**  
  Enhanced logging for system prerequisite validation, reducing redundant check noise.

- **Baseline Tools - Ubuntu 22.04**  
  Fixed baseline tools not launching on Ubuntu 22.04 by building Linux executables on Ubuntu 22.

- **Server Installation - ENOTEMPTY**  
  Fixed server installation error (ENOTEMPTY) during temp directory cleanup on Windows.

- **Package Manager - 'New' Label**  
  Fixed the 'New' label persisting on Baseline Tools after a Package Manager update.

- **Package Manager - Update Retry**  
  Fixed the update not working after a single failure, with added network check and package state update fixes.

- **Server - Connection File Publication**  
  Made connection file publication atomic with retry on failure.

- **System Prerequisite - libgtk Alias**  
  Added libgtk-3-0t64 alias to the system prerequisite checker.

- **Snap Environment**  
  Sanitized the snap environment before spawning standalone SDK tools.

- **Server - Debug Log File**  
  Stopped creating a server log file when the server runs in debug mode.