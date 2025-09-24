# [Flutter for Tizen](https://github.com/flutter-tizen/flutter-tizen)

An extension to the [Flutter SDK](https://github.com/flutter/flutter) for building Flutter applications for Tizen devices.

_Flutter and the related logo are trademarks of Google LLC. This project is sponsored and maintained by Samsung Research._

## Supported devices

- **Smart TV**: [Tizen 6.0 (2021) or later](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html)
- **IoT (RPi 3/4)**: Tizen 6.0 or later

## Installation

- [Linux (x64)](doc/linux-install.md)
- [Windows (x64)](doc/windows-install.md)
- [macOS (x64)](doc/macos-install.md)

## Usage

`flutter-tizen` substitutes the original [`flutter`](https://docs.flutter.dev/reference/flutter-cli) CLI command. Only the command line interface is supported.

```sh
# Inspect the installed tooling and list all connected devices.
flutter-tizen doctor -v
flutter-tizen devices

# Set up a new app project, or add Tizen files if the project already exists.
flutter-tizen create myapp
cd myapp

# Build the project and run on a Tizen device (either in debug or release mode).
flutter-tizen run
flutter-tizen run --release
```

- See [Supported commands](doc/commands.md) for all available commands and their basic usage. See `[command] -h` for more information on each command.
- See [Getting started](doc/get-started.md) to create your first app and try **hot reload**.
- To **update** the flutter-tizen tool, run `git pull` in this directory.

## Platform integration
- [Flutter plugins for Tizen](../plugins/plugins.md)
- [Dart bindings for Tizen APIs](../tizen_interop/tizen_interop.md)
