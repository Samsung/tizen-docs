# Flutter Application

The flutter-tizen project aims to offer productive tooling and extensive support for running cross-platform [Flutter](https://flutter.dev) applications on Tizen devices.

The project source code is licensed under the [BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause) license and is publicly available at https://github.com/flutter-tizen.

The project is an official product by Samsung and maintained by engineers at [Samsung Research](https://research.samsung.com). We also welcome support and contributions from the open source community.

#### The project's major components include:

- [The flutter-tizen tool](https://github.com/flutter-tizen/flutter-tizen): A command line tool for building and deploying Flutter apps to Tizen devices. This is an unofficial add-on to the [Flutter CLI tools](https://github.com/flutter/flutter/tree/master/packages/flutter_tools).
- [The flutter-tizen plugins](https://github.com/flutter-tizen/plugins): Flutter plugins based on Tizen native APIs. Published packages are also available on [pub.dev](https://pub.dev).
- [The tizen-interop plugin](https://github.com/flutter-tizen/tizen_interop): A Flutter plugin that allows Flutter apps to use Tizen native libraries.

#### Supported devices

- **Smart TV**: [Tizen 6.0 (2021) or later](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html)
- **RPi 3/4/5**: Tizen 6.0 or later

#### Installation

- [Linux (x64)](./guides/flutter-tizen/doc/linux-install.md)
- [Windows (x64)](./guides/flutter-tizen/doc/windows-install.md)
- [macOS (x64)](./guides/flutter-tizen/doc/macos-install.md)

#### Tizen basics
- [Setting up Tizen SDK](./guides/flutter-tizen/doc/install-tizen-sdk.md)
- [Configuring Tizen devices for development](./guides/flutter-tizen/doc/configure-device.md)

#### App development
- [Getting started](./guides/flutter-tizen/doc/get-started.md)
- [Debugging apps](./guides/flutter-tizen/doc/debug-app.md)
- [Developing plugins with C++](./guides/flutter-tizen/doc/develop-plugin.md)
- [Developing plugins with C#](./guides/flutter-tizen/doc/develop-plugin-csharp.md)

#### Additional Resources
- For more information on app, plugin developments, engine builds, and contributing to flutter-tizen, please refer to the [Flutter-tizen Wiki](https://github.com/flutter-tizen/flutter-tizen/wiki) page.

# Release plans

The project's target framework version is synched up with the [latest stable release](https://docs.flutter.dev/development/tools/sdk/releases) of the Flutter framework. All other updates are offered on a best-efforts basis. Not all functions are fully tested, and there could be bugs or [missing features](https://github.com/flutter-tizen/flutter-tizen/wiki/Limitations) although we try to minimize them. Therefore, we recommend using the [most recently released version](https://github.com/flutter-tizen/flutter-tizen/releases) rather than the latest commit on the flutter-tizen master branch.
