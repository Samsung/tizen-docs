# Building the SmartThings&trade; Project

You must build your project before flashing or debugging it.

You can build a Tizen RT project in 2 ways: using a batch build or build project command.

## Using Batch Build

To build your project using the batch build command:

1. Select the project in the **Project Explorer** view.

2. To build the selected project, use one of the following:

	* In the Tizen Studio for RT menu, select **Project &gt; Batch Build Project**.  
      ![Building the project](media/rt_build_smartthings.png)

	* In the Tizen Studio for RT toolbar, click the **Build TizenRT Project** icon (![Build icon](media/rt_icon_build.png)).  
      ![Building the project](media/rt_build_smartthings_menu.png)

3. In the Build TizenRT Project Wizard, select the board (`artik053`) and build option (`st_things`) for building your project, and click **OK**.  
   ![Board and build option](media/rt_build_option_smartthings.png)


You can check the build logs in the **Console** view.

**Figure: Build logs**   
![Build logs](media/rt_build_logs_smartthings.png)

## Using Build Project

To build your project using the build project command:

1. In the **Project Explorer** view, select the project.
2. In the Tizen Studio for RT toolbar, click the arrow next to the **Build TizenRT Project** icon (![Build icon](media/rt_icon_build.png)) and select **Select Board**.    
  ![Build drop-down icon](media/rt_build_dropdown_menu.png)

3. In the Select Board and PreDefine Option window, select the board (`artik053`) and build option (`st_things`) for building your project, and click **OK**.  
  ![Board and build option](media/rt_build_option_smartthings.png)

4. In the Tizen Studio for RT toolbar, build the project by selecting **Project &gt; Build Project**.  
  ![Board Project menu option](media/rt_build_build_project.png)

You can check the build logs in the **Console** view.

**Figure: Build logs**  
![Build logs](media/rt_build_logs_smartthings.png)

## Related Information
* Dependencies
  - Ubuntu Only
