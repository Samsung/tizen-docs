# Uninstall Tizen Studio

This section explains how to uninstall Tizen Studio. Tizen Studio uninstaller removes all Tizen platforms and the tools that you have installed.
You can uninstall Tizen Studio in one of the following methods: 
- Using GUI uninstaller
- Using CLI uninstaller

> **Note**
>  
> For more information on how to remove a single package or multiple packages, see [Updating Tizen Studio](update-sdk.md).

You can uninstall Tizen Studio either using the GUI uninstaller or using the CLI Package Manager.

## GUI Uninstaller

To uninstall Tizen Studio using GUI uninstaller, follow these steps:

1. You have to back up all the data and the files in case you want to keep them for future refrence. 
   > **Note**
   >
   > Once you start uninstallation process, the process is irreversible. You cannot restore the removed files.
2. Launch Tizen Studio uninstaller.

3. Select the components to uninstall. 

   - **SDK data**  
   The SDK data directory typically contains user-created data files, including emulator images, log files, and tool configuration files.

   - **KeyStore**  
   The keystore directory is located inside the SDK data directory and contains the author and distributor certificate files. If the certificate files are deleted, you cannot restore them from any Tizen seller market site. If you plan to install another Tizen Studio version or reinstall Tizen Studio later, it is strongly recommended that you back up the certificate files or keep the keystore directory by unchecking the **KeyStore** component.

     > **Note**  
     > 
     > If you do not select SDK data or KeyStore components, you can keep the SDK data or KeyStore files in their directories for future re-use.

3. To remove the installed platforms and the tools, and the user-created data and the files, click **Uninstall**.

   ![Uninstaller selections](./media/uninstall_sdk_selection.png)

4. If you have selected to uninstall the SDK data or the KeyStore components, they are removed in the uninstalling process.

   ![Uninstallation in progress](./media/uninstall_sdk_progress.png)

## CLI Uninstaller

Run the CLI Package Manager with the `uninstall` command using the following syntax:

```
package-manager-cli uninstall [-p <password>] <package name>[,...] | [--all]
```

The following table explains various command parameters to uninstall:

**Table: Uninstall command parameters**

| Parameter                   | Description                              |
|---------------------------|----------------------------------------|
| `-p, --password <password>` | Administrator (sudo) password for authentication.<br> Works in Ubuntu only. |
| `--all`                     | Uninstalls the entire Tizen Studio with tools and platforms including user-created data, emulator images, and settings. |
| `<package name>[,...]`        | Name of the package you want to uninstall. You can enter multiple package names such as **NativeIDE** and **Emulator**.<br>To retrieve the names of the uninstallable packages, use the following command:<br>`package-manager-cli show-pkgs` |

## Related Information
-  Dependencies
  - Tizen Studio 1.0 and Higher
