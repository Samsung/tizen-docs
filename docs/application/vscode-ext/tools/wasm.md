# Introduction

WebAssembly (WASM) provides a way to run C and C++ code (among others) on the Web at near Native speed. WebAssembly is designed to complement and run alongside JavaScript. By using the WebAssembly JavaScript APIs, you can load WebAssembly modules into a JavaScript smart device application, and share functionality between the two. WebAssembly is being developed as a Web standard via the W3C WebAssembly Working Group and Community Group with active participation from all major browser vendors.

[Click here](https://developer.samsung.com/smarttv/develop/extension-libraries/webassembly/webassembly.html) for more information on Tizen WebAssembly and it's application structure.

VS Code extension for Tizen supports **Tizen WebAssembly application** developers, it also helps to generate, update and package an application, as well as run and debug an application on Tizen targets.

## Prerequisites

Below are the prerequisites for using **Tizen WebAssembly (WASM)** in Visual Studio Code:

- Make sure that Tizen Studio Version 6.0 or above is installed.
- Make sure to set Tizen Studio path with the installed 6.0 or above by using VS Code command: **Tizen: Wizard to set Tizen Baseline SDK path or install a new one**.
- Make sure that latest [Visual Studio Code](https://code.visualstudio.com) is installed.
- Make sure that **Tizen Extension** from the market place is installed. **Tizen Extension** can be installed by searching in the extensions view (Ctrl+Shift+X).
- Make sure Tizen Emscripten SDK setup is done.

## Tizen Emscripten SDK Setup  
1. Download and extract the [Tizen Emscripten SDK](https://developer.samsung.com/smarttv/develop/extension-libraries/webassembly/download.html) suitable for your OS. 
2. Setup Tizen Emscripten and use it with Visual Studio Code.
   > [!NOTE]
   > These steps guide to use *emsdk* without changing development host environment variables permanently.

   - Open the **command palette** and select **Tizen Web: Wizard to set Tizen WASM emsdk path**.
     - It launches a wizard to browse the folder and set it.
     - Browse the *emsdk* directory and set it.

    ![Select dotnet-gcdump](media/wasm-emsdk-path-set.png)

   - Open the **command palette** and select **Tizen Web: Activate Tizen WASM emsdk path**.
     - It activates the *emsdk* tool to be used by Tizen VS Code extension.

    ![Select dotnet-gcdump](media/wasm-emsdk-activate.png)


## To develop a Tizen WASM application
The following section demonstrates the steps essential for developing a Tizen WASM application using *Tizen* extension.

> [!NOTE]
> Use `CTRL+SHIFT+P` to activate the *command palette*.

1. Create an empty Tizen web project:
    - In VS Code, click **View** > **command palette**.
    - In the input field of the **Command Palette** that appears, type **Tizen : Create Tizen Project** and press **Enter**.
    - Select **Web** from the project type list and press **Enter**.
    - Select a **profile** and press **Enter**.
    - Select a **profile version** and press **Enter**.
    - Select a **template** and press **Enter**.
    - Provide the name of the project and press **Enter**.
    - Make the body tag empty (if not empty already) of the index.html file.


2. Add a WASM module choosing from existing sample:
    - Run Add WASM Module:

     ![wasm add module](media/wasm-add-module.png)

    - Choose the language:

     ![wasm select module language](media/wasm-select-lang.png)

    - Provide the name for WASM module:

    ![wasm set module name](media/wasm-set-name.png)

    - Select the module mode:

    ![Select wasm module mode](media/wasm-select-template.png)

    - Choose **Hello Triangle**

    ![Select wasm module template](media/wasm-select-template-type.png)

    - If everything is okay, then the WASM module is added to Tizen Web project and a success message is shown in VS Code.

    ![Select wasm module template](media/wasm-add-module-success.png)


3. Build the WASM module.
    - Run Build WASM Module:
    
     ![wasm build module](media/wasm-build-module.png)
    
    - Select Build Mode:
    
     ![wasm build module](media/wasm-build-config.png)

    - If everything is okay, then the WASM module build starts and build messages are shown in the output console of VS Code.
    - Once build is completed, it shows the build success message.
      > [!NOTE]
      >      First WASM module build after *emsdk* activation may take take upto 15-20 minutes (to create emscripten cache files), depending on the type of the OS (Windows/Linux/MAC).

     ![Select wasm module template](media/wasm-build-success.png)


4. Running the Web WASM Application:
    - Run Tizen Application:
    
     ![wasm build module](media/wasm-run-app.png)
    
    - Application is built, packaged and launched on the connected Tizen Emulator/Device:

     ![Select wasm module template](media/wasm-app-running.png)