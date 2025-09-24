# Flutter Application

The flutter-tizen project aims to offer productive tooling and extensive support for running cross-platform [Flutter](https://flutter.dev) applications on Tizen devices.

The project source code is licensed under the [BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause) license and is publicly available at https://github.com/flutter-tizen.

The project is an official product by Samsung and maintained by engineers at [Samsung Research](https://research.samsung.com). We also welcome support and contributions from the open source community.

#### The project's major components include:

- [The flutter-tizen tool](./guides/flutter-tizen/flutter-tizen.md): A command line tool for building and deploying Flutter apps to Tizen devices. This is an unofficial add-on to the [Flutter CLI tools](https://github.com/flutter/flutter/tree/master/packages/flutter_tools).
- [The flutter-tizen plugins](./guides/plugins/plugins.md): Flutter plugins based on Tizen native APIs. Published packages are also available on [pub.dev](https://pub.dev).
- [The tizen-interop plugin](./guides/tizen_interop/tizen_interop.md): A Flutter plugin that allows Flutter apps to use Tizen native libraries.

#### Tizen basics
- [Setting up Tizen SDK](./guides/flutter-tizen/doc/install-tizen-sdk.md)
- [Configuring Tizen devices for development](./guides/flutter-tizen/doc/configure-device.md)

#### App development
- [Getting started](./guides/flutter-tizen/doc/get-started.md)
    - [Installing for Linux (x64)](./guides/flutter-tizen/doc/linux-install.md)
    - [Installing for Windows (x64)](./guides/flutter-tizen/doc/windows-install.md)
    - [Installing for macOS (x64)](./guides/flutter-tizen/doc/macos-install.md)
- [Debugging apps](./guides/flutter-tizen/doc/debug-app.md)
- [Developing plugins](./guides/flutter-tizen/doc/develop-plugin.md)
- [Flutter Docs](https://docs.flutter.dev)

#### Miscellaneous
- [Publishing apps on Samsung Galaxy Store and TV Seller Office](./guides/flutter-tizen/doc/publish-app.md)
- [Flutter-tizen Wiki](https://github.com/flutter-tizen/flutter-tizen/wiki)

# Release plans

This project doesn't have its own release schedule. The project's target framework version is synched up with the [latest stable release](https://docs.flutter.dev/development/tools/sdk/releases) of the Flutter framework. All other updates are offered on a best-efforts basis. Not all functions are fully tested, and there could be bugs or [missing features](https://github.com/flutter-tizen/flutter-tizen/wiki/Limitations) although we try to minimize them. Therefore, we recommend using the [most recently released version](https://github.com/flutter-tizen/flutter-tizen/releases) rather than the latest commit on the flutter-tizen master branch.

You can update your local flutter-tizen installation by pulling (`git pull`) its latest commit.