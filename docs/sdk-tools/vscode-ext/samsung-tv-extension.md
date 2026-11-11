# Install Samsung Smart TV Extension

The Samsung Smart TV Extension allows developers to create applications for Samsung Smart TVs and emulate them for testing purposes. It is an add-on SDK, which is installed using the Tizen Package Manager.

## Install from a repository URL

1. In the **Tizen** panel, under **Baseline Tools**, select **Package Manager**.
2. Select **Repository** to open **Repository Configuration**. The default TV repository URL is displayed next to **TV repository**.
3. Keep the default TV repository URL or change it. If you change it, select **Apply**. If you keep it, **Apply** remains disabled.

   ![TV repository URL in Repository Configuration](../vstools/media/tv-extension-url.png)

4. If you changed the URL, wait for the repository update to complete automatically.

   ![Repository configuration applied successfully](../vstools/media/repository-updated.png)

5. Select **Advanced SDK Installation**, then select **Install** next to the TV version that you need. Wait for the installation to complete.

   ![TV SDK Installation](../vstools/media/install-tv-extension.png)

6. In the **Tizen** panel, under **Baseline Tools**, select **Emulator Manager**, then select **Launch** next to the TV emulator.

   ![TV emulator listed in Tizen Emulator Manager](../vstools/media/emulator-manager-tv-emulator.png)

7. Check that the TV emulator gets launched.

   ![Launched TV emulator](../vstools/media/tv-emulator-launched.png)

## Install from a local ZIP file

1. In the **Tizen** panel, under **Baseline Tools**, select **Package Manager**.
2. Select **Repository** to open **Repository Configuration**.
3. Select **Browse** next to **TV repository**, select a local TV SDK `.zip` file, and select **Apply**.

   ![Select a local TV ZIP file using the Browse button](media/TV_ZIP.png)

   ![Local TV ZIP selected with the Apply button highlighted](../vstools/media/tv-zip-selected.png)

4. Wait for the repository update to complete automatically.

   ![Repository configuration applied successfully](../vstools/media/repository-updated.png)

5. In the **Tizen** panel, under **Baseline Tools**, select **Emulator Manager**, then select **Launch** next to the TV emulator.

   ![TV emulator listed in Tizen Emulator Manager](../vstools/media/emulator-manager-tv-emulator.png)

6. Check that the TV emulator gets launched.

   ![Launched TV emulator](../vstools/media/tv-emulator-launched.png)
