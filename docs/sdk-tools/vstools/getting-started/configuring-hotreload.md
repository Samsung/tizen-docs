# Tizen .NET Hot Reload

## Overview
Tizen .NET Hot Reload allows you to modify your app’s managed source code while debugging, without stopping or restarting the application. Once debugging has started on an emulator or a real device, you can apply changes directly to the running app.

### How It Works
- Changes take effect the next time the updated code is executed, either by user action or a timer trigger.
- Hot Reload applies changes only when the modified function is re-entered.
- If a change is not supported, a prompt will notify you, requiring a manual restart to apply the update.


## Enable Tizen .NET Hot Reload
To enable Hot Reload in Visual Studio:
1. Go to **Tools > Options** in Visual Studio.
<img alt="Tools/options" src="/docs/application/vstools/media/vs2022_hotreload_1.png" />

2. **Enable Hot Reload for Tizen:**
    - Navigate to **Tizen > Tools**.
    - Check the Enable Hot Reload checkbox.
    <img alt="Enable hot reload for tizen" src="/docs/application/vstools/media/vs2022_hotreload_2.png" />
3. **Enable .NET/C++ Hot Reload:**
    - Navigate to **Debugging > .NET/C++ Hot Reload**.
    - Check all available checkboxes.
    <img alt="Enable .NET/C++ hot reload" src="/docs/application/vstools/media/vs2022_hotreload_3.png" />

## Supported Architectures & Limitations
Tizen .NET Hot Reload supports **aarch64** (64-bit ARM) and **armv7l** (32-bit ARM) architectures. However, certain code modifications are not supported at runtime. If an unsupported change is detected, a rude edit dialog will prompt you to restart the application to apply the changes.[Supported Edits in Tizen .NET Hot Reload](https://github.com/dotnet/roslyn/blob/main/docs/wiki/EnC-Supported-Edits.md){:target="_blank"}


## Examples of Tizen .NET Hot Reload Usage

1. **Tizen .NET Hot Reload Without Breakpoint**<br>
This example demonstrates using Hot Reload in a **Tizen ElmSharp-based UI** application.
    - A callback method is assigned to a button click event.
    - The app is launched in debug mode on a target device.
    - The callback method is modified and saved (Ctrl+S), applying Hot Reload without restarting.
[![Demo Video: Hot reload without breakpoint](/docs/application/vstools/media/hotreload_without_bp.png)](/docs/application/vstools/media/Hotreload_Without_Breakpoint.mp4 "Reload example video without breakpoint")
<br>

2. **Tizen .NET Hot Reload With Breakpoint**<br>
This example demonstrates Hot Reload usage with a breakpoint in a **Tizen ElmSharp-based UI** application.
    - A breakpoint is set in the main method on a static method call.
    - The app is launched in debug mode on a target device.
    - The method is modified and saved (Ctrl+S), applying Hot Reload while debugging.
[![Demo Video: Hot reload with breakpoint](/docs/application/vstools/media/hotreload_with_bp.png)](/docs/application/vstools/media/Hotreload_With_Breakpoint.mp4 "Reload example video with breakpoint")
