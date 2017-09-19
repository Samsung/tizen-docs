# Emulator extension development guide

## Support for QEMU Extension
- Source management and development methods
    1. Create directory structure
        - For the source directory, you must separate the directory
        - It is also possible to put QEMU git as a submodule for ease of management
    2. Manage configure
        - (QEMU) /tizen/emulator_configure.sh
        - Copy emulator_configure.sh to manage the new configure script
    3. Common Source Management
        - Prevent source fragmentation by pushing QEMU git
        
- How to build
    1. Use configure script to automate the process below.
        - Prepare Extension source directory
            - Link or create an extended source directory under "(QEMU) / tizen / src /"
                - Create a subdirectory using the git submodule or create it using a symbolic link
        - Run configure - make sure the extension source directory is ready before configure
            - Add --extension-path = [extension directory] at configure
            - The extension directory is a relative path starting from '(QEMU) / tizen / src'
    2. Make
        - Execute (QEMU) / tizen / Makefile with make command
        - If you use git submodule to manage QEMU git as a subdirectory, it is convenient to make a wrapper makefile in the parent directory.
        
## Support for kernel Extension
- Source management and development methods
    1. Create directory structure
        - For the source directory, you must separate the directory
        - It is also possible to put QEMU git as a submodule for ease of management
    2. Manage defconfig
        - Create a new defconfig file by referring to the existing defconfig file
    3. Common Source Management
        - Prevent source fragmentation by pushing emulator-kernel git
        
- How to build
    1. Use configure script to automate the process below.
        - Prepare Extension source directory
            - Link or create an extended source directory under "(emulator-kernel)/drivers/maru/"
                - Create a subdirectory using the git submodule or create it using a symbolic link
        - Set CONFIG_MARU_EXTENSION_SOURCE and CONFIG_MARU_EXTENSION_SOURCE_PATH in defconfig
            - When building, you can use a script, or if the extension path is always fixed, it can be put in advance in defconfig
    2. Make
        - Execute Make using defconfig
        - If you use git submodule to manage QEMU git as a subdirectory, it is convenient to make a wrapper makefile in the parent directory.
        
        
## Emulator Manager Extension

![](/docs/image/em-structure.png)

- Emulator Manager Component
    - EM-LIB
        - Manage commonly used parts in UI / CLI
        - Loading Plugin jar file, default property xml file
    - EM-3.0-UI
        - UI sources
        - Using Javafx
        - Loading UI template xml file 
    - EM-CLI
- Emulator Manager Plugin
	- Different parts by platform
		- UI item
		- Options to run the Emulator
	- Plugin exists for each platform
		- em-plugin-mobile.jar, em-plugin-wearable.jar
	- The `template xml` file has platform-specific UI and property property values.
		- X86-standard.xml (default property)
		- X86-standard-template-v2.xml (UI template)
- Extension Point
	- Item-Factory
		- Extend item of property view in UI
		- org.tizen.emulator.manager.ui.item.ViewItemFctory
	- Option-Factory-v2
		- Extend Launch option
		- org.tizen.emulator.manager.vms.option.IOptionFactory2
	- Platform-Resource-Selector
		- Whether to use platform resources
	- You can specify the extension class in the MANIFEST.MF file of the plugin.
	![](/docs/image/em-loading-plugin.png)
	---
	![](/docs/image/em-loading-plugin-func.png)
	
- **Specific explanation**
	- Launch option
		- How to modify Option
			- org.tizen.emulator.managaer.vms.option.Option
			- create class
		- Extend OptionFactoryV2
			- MakeOptionList
				- Add new option to Common option list
			- addOption
				- Change to a new option for a specific item
	- UI Extension

## ECP Extension

### Preferences
- git projects (default, develop branch)
    - Lib/UI/CLI
    	- https://github.sec.samsung.net/RS-TizenStudio/emulator-control-panel
    - Devices
    	- https://github.sec.samsung.net/RS-TizenStudio/emulator-control-panel-devices

### How to build
1. Copy external binaries
2. Copy binaries from `tizen-sdk/tools/emulator/bin` to two project libs folders
    - args4j, jfxrt, jline, json-simple, protobuf
3. Lib/UI/CLI
    - If you enter the shell comment `ant` at the top level of your project, all of `lib/ui/cli` will be built
4. Devices
    - Copy built `libecp`, `emulator-control-panel.jar`, and `emulator-control-panel-cli.jar` under `libs` in the devices project
    - If you enter the shell comment `ant` at the top level of your project, all of `mobile/wearable/tv` will be built
    	- If you want to build each, you can specify `ant -f ECP-DEVICE / build_mobile.xml`.
5. If you configure devices separately, you only need to change the contents of emulator-control-panel-devices.
6. Copy to each location after build
    - `lib/ui/cli` under `sdk/tools/emulator/bin`
    - devices `xml` and `jar`, under `platforms/{version}/{profile}/emulator-resources/plugins`
    	- For `jar`, you need to change the name
	
### Development and Execution
1. Using Eclipse
2. Import all projects
3. In run configuration, Program arguments
    - vm_name=w-0906-1 base_port=26100 platform_version=tizen-2.3.2 profile=wearable
    - The platform version and profile are named directory
        - {tizen-sdk}/platforms/{platform_version}/{profile}
4. In the run configuration, VM arguments
    - `-Ddevelop`, sdk.info file is found based on the sdk installation path specified in FilePath.java
    - For example, `emulator-control-panel/ECP-LIB`
    	- "ln -s ~/tizen-studio/sdk.info sdk.info" 
	
### Example
- [ECPInfo.java](https://github.sec.samsung.net/RS-TizenStudio/emulator-control-panel/blob/develop/ECP-LIB/src/org/tizen/ecp/ECPInfo.java)
- [FilePath.java](https://github.sec.samsung.net/RS-TizenStudio/emulator-control-panel/blob/develop/ECP-LIB/src/org/tizen/ecp/utils/FilePath.java)
- [DeviceManager.java](https://github.sec.samsung.net/RS-TizenStudio/emulator-control-panel/blob/develop/ECP-UI/src/org/tizen/ecp/device/DeviceManager.java)


#### Changes
- (UI) Changing from swt to javafx
    - Not compatible with existing code (including xml)
- Rename plugin
    - `ecp-plugin.xml` -> `ecp-plugin-<profile>-<version>.xml`
- Changing Package structure 
    - Separate the git repository with emulator-control-panel and emulator-control-panel-devices
    - Change the executable file under platforms to Tools
- Changing XML form   
