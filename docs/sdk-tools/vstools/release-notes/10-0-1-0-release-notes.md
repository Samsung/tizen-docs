# Tizen VS Extension 10.0.1.0 Release Notes

**Release Date:** July 30, 2026

### Features

- **Redesign Extension**  
  Redesigned the Visual Studio extension architecture around an Express-based Server, replacing the previous standalone model.

- **Initial Setup Method Changed**  
  On first launch after installing the extension, user is prompted to set the SDK resource path, the directory where Tizen SDK packages and tools are stored. After setting this path, the server and core apps are installed.

### Bug Fixes

- Fix build failure when whitespace is in project path and update server link to target market server