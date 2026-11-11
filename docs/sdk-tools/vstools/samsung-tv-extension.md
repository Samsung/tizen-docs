# Install Samsung Smart TV Extension

The Samsung Smart TV Extension allows developers to create applications for Samsung Smart TVs and emulate them for testing purposes.
It is an add-on SDK, which is installed using the Tizen Package Manager.

## Install from a repository URL

1. In the Visual Studio menu, select **Tools > Tizen > Tizen Package Manager**.
2. Select **Repository** to open **Repository Configuration**. The default TV repository URL is displayed next to **TV repository**.
3. Keep or change the TV repository URL.

   ![TV repository URL in Repository Configuration](media/tv-extension-url.png)

4. Select **Apply** and wait for the repository update to complete automatically.

   ![Repository configuration applied successfully](media/repository-updated.png)

5. Select **Advanced SDK Installation**, then select **Install** next to the TV version that you need. Wait for the installation to complete.

   ![TV SDK Installation](media/install-tv-extension.png)

6. Open **Tools > Tizen > Tizen Emulator Manager**. The TV emulator appears there.

   ![TV emulator listed in Tizen Emulator Manager](media/emulator-manager-tv-emulator.png)

## Install from a local ZIP file

1. In the Visual Studio menu, select **Tools > Tizen > Tizen Package Manager**.
2. Select **Repository** to open **Repository Configuration**.
3. Select **Browse** next to **TV repository** and select a local TV SDK `.zip` file.

   ![Select a local TV ZIP file using the Browse button](../vscode-ext/media/TV_ZIP.png)

4. Select **Apply** and wait for the repository update to complete automatically.

   ![Repository configuration applied successfully](media/repository-updated.png)

5. Open **Tools > Tizen > Tizen Emulator Manager**. The TV emulator appears there.

   ![TV emulator listed in Tizen Emulator Manager](media/emulator-manager-tv-emulator.png)
