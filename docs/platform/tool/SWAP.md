Introduction to SWAP
--------------------

**SWAP** is a Tizen dynamic binary instrumentation tool, it allows
developers to trace and profile their applications. The tool supports a
number of Tizen devices and emulators and is supplied as a part of their
firmware. To check if your device contains **SWAP**, you can check is
swap-manager package installed:\
`$ rpm -q swap-manager`\
If the output looks like the following then **SWAP** is installed:\
`swap-manager-3.0-7.6.i686`\
So, if your device or emulator contains **SWAP**, you can start using
it.\
**SWAP** is located on the target device, it is responsible for
gathering run time data about the developer\'s application. When it
works it is connected with a host side tool and communicates with it in
a format described at **SWAP** protocol (you can see it at
<swap-manager>`/docs/`). **SWAP** host side tool controls **SWAP**
execution, provides it with a profiling session options and receives
gathered data. There are two **SWAP** host-side tools:\
\* [**Dynamic
Analyzer**](https://developer.tizen.org/development/tizen-studio/native-tools/debugging-your-app/dynamic-analyzer)
GUI and CLI tools provided with Tizen Studio;

-   **SWAP Python console tool**,  which is provided with the
    **swap-manager**
    ([git](git://git.tizen.org/platform/core/system/swap-manager)).

**SWAP** contains several useful features for developers:

-   Function profiling. This feature allows the developer to trace
    functions of interest of his application. It is based on uprobe
    mechanism. The developer specifies which functions in which binary
    files he wants to trace and when control flow reaches one, the event
    related information is collected: function address, timestamp,
    arguments etc. is generated.
-   Profiling of OpenGL and system APIs related to memory management,
    file operations, network and threading. This feature provides the
    developer information about application\'s system resources usage.
-   [Leak Sanitizer](https://clang.llvm.org/docs/LeakSanitizer.html).
    This feature generates report about memory leaks in the application.
-   Context switch profiling. This feature adds data about context
    switching to the trace.
-   Sampling. Used for point of process execution sampling with the
    specified period.

### SWAP high-level design

![SWAP high-level design](Hdesign.png "fig:SWAP high-level design")
**SWAP** consists of the several parts: user-space daemon, kernel
modules and SWAP library.

-   SWAP kernel modules provides
    [kprobe](https://www.kernel.org/doc/Documentation/kprobes.txt) and
    [uprobe](https://www.kernel.org/doc/Documentation/trace/uprobetracer.txt)
    functionality and sampling feature.
-   SWAP probe library is loaded at the target process memory area, used
    for profiling system APIs and LSan analytic without using the
    expensive uprobe mechanism.
-   The daemon is used for communication between SWAP and host side. It
    is also responsible for executing and killing applications,
    transferring data between kernel- and user-space, communication with
    the SWAP library instances at the target application\'s memory areas
    and sending gathered data to host side.

To use **SWAP** the developer needs **SWAP Python tool** on his
host-side. The developer specifies application for instrumentation, runs
**SWAP Python tool** and gets a gathered binary trace as a result of the
tool\'s work. The developer can use **Trace Parser**, which is also
provided within **swap-manager** sources, to convert binary trace to
more readable and understandable formats.

SWAP Tool User Guide
--------------------

**SWAP tool** consists of two parts: **SWAP Python tool** itself and
**Trace Parser**. (the latest user guide can always be found at
<swap-manager>`/src/cli/swap_cli/docs/` and
<swap-manager>`/src/cli/trace_parser/docs/`).\
**SWAP Python tool** is a python library which implements **SWAP tool**
host-side. It is used for interacting with **SWAP** daemon, located on
target, you can use it if your device contains an installed version of
**SWAP**. **SWAP Python tool** can be used as a part of another
application or, using its example as a reference, as a standalone tool.\
**Trace Parser** is a part of **SWAP tool**. It is used for parsing
binary trace, gathered by System Wide Analyzer Performance (**SWAP**)
and outputting it in a specified format. **Trace Parser** supports
several output types:

-   text output;
-   trace as a python source file output;
-   JSON formatted output;
-   CSV formatted output.

### Getting the tool

**SWAP tool** is provided as a part of **swap-manager**. To get **SWAP
Python tool** please do the following:

-   clone **swap-manager** sources and checkout to *tizen* branch:\

``\
`$ git clone git://git.tizen.org/platform/core/system/swap-manager`\
`$ cd swap-manager && git checkout tizen`\

### Build

To run **SWAP Python tool** example, the user should do the following
steps:

1.  Install target application with debug flag. Applications installed
    without debug flag are restricted for profiling due to security
    reasons;
2.  Edit `emulator.py` according to the user\'s target:
    1.  set proper connection type for the field type in `connection`
        dictionary;
    2.  if the type is ssh, set `ip` and `port` values;
    3.  add information about connection type:
        -   if connection is established via `sdb`, set `emulator`,
            `device` or `serial` value for `target` field of `type_info`
            dictionary;
        -   if connection is established via `ssh`, set SSH connection
            parameters for `params` field and SSH username for
            `username` field of type\_info dictionary;
3.  Edit `example_conf.py` according to the target application data:
    1.  set target application type to field `type` of `app_info`
        dictionary that is contained in `app` dictionary. Now only
        `NATIVE` applications are supported due to security reasons;
    2.  set Tizen application ID to field `id` of `app_info` dictionary;
    3.  add data about features desirable to use:
        -   if the user wants to use Sampling feature, add `sampling`
            dictionary to the file and add `period` field in it with the
            desirable period of sampling;
        -   if the user wants to use any of Memory profiling, File
            profiling, Network profiling, Thread profiling, OpenGL
            profiling, Context switch profiling, Leak Sanitizer
            features, add `features` list somewhere in the file and add
            here
            `'memory', 'file', 'network', 'thread', 'opengl', 'context_switch', 'lsan'`
            values accordingly. For always profiling version of the
            features, add `for_all` for these features;
    4.  add necessary user probes for the binaries of interest. To add
        probe on the binary do the following:
        1.  add a key-value pair to function\_inst dictionary that is
            contained in app dictionary. The key should be a string with
            a full path to the binary, the value should be a list;
        2.  add tuple to the list;
        3.  add name or address of the function of interest to the tuple
            as the first value. Name should be a string, address should
            be an integer;
        4.  add string that represents function arguments to the tuple
            as the second value. For the information about possible
            values, please refer to the Config files
            description section;
        5.  add string with a character that represents return value of
            the function to the tuple as the third value. For the
            information about possible values, please refer to
            the Config files description section;
4.  Change directory to the `cli` directory and execute `example.py`:
        $ cd <swap-manager>/src/cli/ && python -m example.example

5.  All artifacts of the profiling session will be placed at the
    specified `output_dir` on stop. The default <output_dir> is
    `/tmp/outdir/`. As a result of the following command, trace in
    human-readable format will appear in <output_dir>`/trace.txt` file:

<!-- -->

    $ cd <output_dir>
    $ <swap-manager>/src/cli/trace_parser/bin/swap_parser -i trace.bin -o trace.txt -s session_data.json -a api_map_list -t text

For an advanced API description and additional usage examples, please
refer to the [SWAP Python tool API
description](SWAP_Python_tool_API "wikilink") page.

[Category:Tool](Category:Tool "wikilink")
