# Tizen VS Code Extension Release Notes

**Version:** 10.3.8  
**Release Date:** July 2, 2026


### Features

- Streamline Tizen development using predefined project templates
- Create, build, run, and debug Tizen apps in Visual Studio Code with IntelliSense support
- Automate SDK installation via on-demand downloads and optimized CDN selection
- Configure custom SDK paths and install multiple SDK versions
- Install TV SDK from local ZIP files
- Leverage AddressSanitizer (ASAN) and LeakSanitizer (LSAN) for robust native debugging
- .NET Memory Profiler for memory allocation tracking
- Create, modify, delete, export, reset, and run emulator profiles with custom image editing
- Manage emulator profiles with advanced network configuration
- Emulator Control Panel for TV sensor simulation with remote logging
- Generate Samsung certificates and manage DUIDs for secure app deployment
- Connect to remote devices for real-time log monitoring and debugging
- Import and develop WGT files for widget-based applications
- Modern UI with welcome page, sidebar actions, progress updates, and issue reporting, and cross-platform support

### Known Issues

- Emulator profiles may appear in random order
- Template dropdown is missing from the Device tab in Emulator Edit Mode
- False error messages may appear during emulator package downloads
- Network configuration UI layout issues in Emulator
- Native app build/run fails on Mac M1 (ARM chipset)
- System prerequisites may fail to sometimes install on Ubuntu 22.04
- Address and Leak Sanitizers require the llvm symbolizer package on device
- Native app memory profiling with ASAN/LSAN is incomplete
- Native UTC app does not reload UI after source updates
- Dev package installation notification may appear indefinitely for non-Tizen projects
- api-checker package is missing from native dev package installation
- Import Android certificate opens file picker with normal certificate file extension filter by default (.jks files not shown)