# Debugger Setting (Native)

This guide provides a step-by-step process for setting up the debugger for Native applications. 
Follow the instructions specific to your application to set up debugging.

## Debugger Setup for Native Applications

### Steps

1. **Open Your Project**
   - Open Visual Studio Code.
   - Load your native project by selecting `File` -> `Open Folder`.

2. **Configure Launch.json file**
   - In Visual Studio Code, open the `.vscode` folder in your project directory.
   - Create a `launch.json` file if it doesn't exist.
   - Click "Add Configuration" and select "Tizen Native Debug:Launch (gdb)".

   ![Debug Configuration for Native](media/native-debug-1.png)

3. **Set Breakpoints**
   - Open your source code files.
   - Set breakpoints by clicking on the gutter next to the line numbers where you want to pause execution.

4. **Start Debugging**
   - Make sure to set the debug configuration to "Tizen Native Debug:Launch (gdb)" in the dropdown menu.
   - Click the play button with a bug icon in the top toolbar or press `F5`.

   ![Debug Configuration for Native](media/native-debug-2.png)

   - The debugger will start and your application will run until it hits a breakpoint.
   - You can now inspect variables, step through code, and analyze the state of your application.

   ![Debug Configuration for Native](media/native-debug-3.png)