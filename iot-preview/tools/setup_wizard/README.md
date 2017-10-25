Tizen IoT Setup Wizard
======================

The Tizen IoT Setup Wizard(v0.4.1-preview) is a Tizen Studio Plugin, that can be used for preparing an SD Card for booting Tizen 4.0 your IoT Device with ease. The currently supported devices are Samsung Artik 530 (headed and headless) and Raspberry Pi 3 (headless).

The Setup Wizard binary is a JAR file, that can be installed as a Tizen Studio Plugin. To install a plugin in Tizen Studion using a JAR file, the JAR file should be placed in the ide/dropins folder, in the Tizen Studio installation directory. Please refer to Eclipse documentations about plugins/dropins for more information.

The jar file is provided here in 5 parts due to its large size. Please refer to the instructions below on how to retrieve the JAR file from the parts using the script provided.

JAR File retrieval intructions
------------------------------
1. Download the 5 parts of the plugin JAR and the *combine.sh* script into a single empty directory
2. Execute the script from a bash shell using the command *./combine.sh*
3. The script would produce the JAR file by combining the individual parts


