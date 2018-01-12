# Flashing the Project

To upload your project on the board, you need to flash it:

1. Connect the board to your computer.

   The following figure shows the Artik 051 board.

   ![Connecting the board](media/rt_flash_connect.png)

2. Select the project in the **Project Explorer** view.

3. To flash the Tizen RT project, use one of the following:

   - In the Tizen Studio for RT menu, select **Project > Flash**.
   - In the Tizen Studio for RT toolbar, click the **Flash** icon (![Flash icon](media/rt_icon_flash.png)).

     ![Flashing the project](media/rt_flash.png)

   If you have not built the project yet, an error popup appears.

   ![Flashing without building error](media/rt_flash_build_error.png)

4. In the Flash TizenRT Project Wizard, select the Flash option and click **Flash**.

   ![Flash option](media/rt_flash_option.png)

If the board is not connected to the computer or the flash environment is not properly configured, the **Console** view displays the flash failure log.

**Figure: Flash failure**

![Flash failure](media/rt_flash_failure.png)

If the flashing is successful, the success log is shown.

**Figure: Flash success**

![Flash success](media/rt_flash_success.png)

## Related Information
* Dependencies
  - Ubuntu Only
