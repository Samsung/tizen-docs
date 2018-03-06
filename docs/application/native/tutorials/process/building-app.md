
# Building Applications


In the Tizen Studio, different build configurations are available for
different development steps:

-   The **Debug** build is used to debug and test the application.

    The binary, data, and debug files are stored in a `Debug` folder
    under the project in the workspace.

    This is the default build configuration.

    In the debug mode, the debug level is Maximum (-g3) and optimization
    level is None (-O0).

- The **Release** build is used for the tested, release-ready version
    of the application.

    The compiled binary file is stored in a `Release` folder under the
    project in the workspace.

    In the release mode, the debug level is Default (-g) and
    optimization level is Optimize most (-O3).

    The release mode build itself does not strip the debug symbol.
    Stripping is done only in the packaging step for the
    ARM architecture.

    >  **Note**   
    > The Tizen Studio automatically switches application logging
    off in the release mode. To enable logging in the release mode:  
    >   1.  In the Tizen Studio menu, select `Project > Properties`.
    >   2.  In the `Properties` window, go to        `C/C++Build > Settings > C Complier > Debugging`.
    >   3.  Select the `Enable application logging` check box.



To set the target architecture:

1.  In the Tizen Studio menu, select **Project &gt; Properties**.
2.  In the **Properties** window, go to **C/C++Build &gt; Tizen
    Settings &gt; Platform**.
3.  From the **Architecture** drop-down list, select the
    appropriate architecture.


<a name="build"></a>
## Building the Application in the Tizen Studio

To create an application project build:

1.  Select the build configuration:

    a.  Right-click the project in the Tizen Studio **Project        Explorer** view.

    b.  Select **Build Configurations &gt; Set Active**, and select the        build configuration you need.

2. Build the project:

    -   Automatic build

        If you select **Project &gt; Build Automatically** in the Tizen
        Studio menu, whenever you make any change to a source or
        resource and save the project, the Tizen Studio automatically
        recognizes the change and rebuilds the changed source on
        your project.

    - Manual build

        Build the application binaries for executing the code:

        a.  Select the project in the **Project Explorer** view.

        b.  In the Tizen Studio menu, select **Project &gt; Build            Project**.

3. Check your application project source code for any API or privilege
    violations, which are displayed in the **Problems** view.


<a name="prop"></a>
## Build Properties


To build project, you can choose many options. For example, optimization
level, debugging support, or include path and library link options.

To set the build properties:

1.  In the Tizen Studio menu, select **Project &gt; Properties**.
2. In the **Properties** window, go to **C/C++ Build &gt; Tizen
    Settings**.
3. On the **Platform** tab, set the detailed target and
    tool information.
    -   Rootstrap Informations

        Shows the rootstrap-related information:

        -   Platform

            Set the platform version.

        - Architecture

            Set the target architecture.

            To run the application on the x86 emulator, select **X86**.

        - Name

            Set the rootstrap name.

    - Toolchain Informations

        Shows the toolchain-related information:

        -   Platform

            Set the compiler toolchain used to build the application.

4. On the **Framework** tab, set the detailed customization of the
    Tizen framework:
    -   Framework

        Search a framework by name filtering and select the frameworks.

    - Selected Framework

        Shows the all selected frameworks.

    - Description

        Shows the description of the selected framework.

5. In the **Properties** window, go to **C/C++ Build &gt; Settings &gt;    Tool Settings**.

    This tab includes a build toolchain on left tree view. A toolchain
    has 3 main items:

    -   Compiler
    -   Linker
    -   Assembler

    Each tool is configured by selecting its sub-items.

    -   C++ Compiler

        Shows the compiler binary name and summarizes compile options

        -   Preprocessor

            Set the preprocessor option

        - Includes

            Set the include path or files

        - Optimization

            Set optimization options

        - Debugging

            Set debugging options

            > **Note**  
            > The **Enable Application logging** option is
            enabled for the **Debug** build configuration. The option is        disabled in the **Release** configuration.

      - Warnings

            Set warning options

        - Miscellaneous

            Set miscellaneous options

    - C Compiler

        Shows the compiler binary name and summarizes compile options

        -   Preprocessor

            Set the preprocessor option

        - Symbols

            Define or undefine the symbols used in the compilation

        - Includes

            Set the include path or files

        - Optimization

            Set optimization options

        - Debugging

            Set debugging options

        - Warnings

            Set warning options

        - Miscellaneous

            Set miscellaneous options

    - C++ Linker

        Shows the linker binary name and summarizes link options

        -   General

            Set general options

        - Libraries

            Set the library and library paths

        - Miscellaneous

            Set miscellaneous linker options

        - Shared Library Settings

            Set options for shared library linking

    - Assembler

        Shows the assembler binary name and summarizes assembling
        options

For more information on build configuration, see the CDT guide.
