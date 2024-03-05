This page represents **SWAP Python tools** API description.

Python tool API description
---------------------------

### Config files description

**SWAP Pyton tool** sources contain an example of tool configuration
files, located at <swap-manager>`/src/cli/example/`. The folder contains
several config files:

+-----------------------------------+-----------------------------------+
| File                              | Content description               |
+===================================+===================================+
| emulator.py                       |     # Provides target device/emul |
|                                   | ator configuration.               |
|                                   |                                   |
|                                   |     api_version = '1.0'           |
|                                   |     # Used to verify compatibilit |
|                                   | y of different config files;      |
|                                   |                                   |
|                                   |     connection = {                |
|                                   |     # Dictionary, containing data |
|                                   |  about the connection with the ta |
|                                   | rget;                             |
|                                   |                                   |
|                                   |         'ip': "127.0.0.1",        |
|                                   |     # target IP address;          |
|                                   |                                   |
|                                   |         'type': "sdb",            |
|                                   |     # target connection type. Pos |
|                                   | sible values:                     |
|                                   |     # ssh - for SSH connection;   |
|                                   |     # sdb - for SDB connection;   |
|                                   |     # alone - for standalone prof |
|                                   | iling;                            |
|                                   |                                   |
|                                   |         'type_info': {            |
|                                   |             'target': 'emulator', |
|                                   |         },                        |
|                                   |     # information about selected  |
|                                   | connection type, differs for diff |
|                                   | erent type:                       |
|                                   |     # for sdb:                    |
|                                   |     # target - target type, emula |
|                                   | tor, device and serial are suppor |
|                                   | ted;                              |
|                                   |     # for ssh:                    |
|                                   |     # params - SSH connection par |
|                                   | ameters;                          |
|                                   |     # username - SSH username.    |
|                                   |     }                             |
+-----------------------------------+-----------------------------------+
| example\_conf.py                  |     # Provides application's prof |
|                                   | iling session configuration.      |
|                                   |                                   |
|                                   |     api_version = '1.0'           |
|                                   |     # Used to verify compatibilit |
|                                   | y of different config files;      |
|                                   |                                   |
|                                   |     sampling = {                  |
|                                   |     # Turns on SWAP sampling feat |
|                                   | ure and contains its options;     |
|                                   |                                   |
|                                   |         "period": 50,             |
|                                   |     # Period of sampling;         |
|                                   |     }                             |
|                                   |                                   |
|                                   |                                   |
|                                   |                                   |
|                                   |     features = [                  |
|                                   |     # Features, that doesn't requ |
|                                   | ire additional options, are turne |
|                                   | d on by including to this list. A |
|                                   | vailable features are:            |
|                                   |         'memory',          # memo |
|                                   | ry API profiling feature for targ |
|                                   | et binaries;                      |
|                                   |         'file',            # file |
|                                   |  API profiling feature for target |
|                                   |  binaries;                        |
|                                   |         'network',         # netw |
|                                   | ork API profiling feature for tar |
|                                   | get binaries;                     |
|                                   |         'thread',          # thre |
|                                   | ad API profiling feature for targ |
|                                   | et binaries;                      |
|                                   |         'opengl',          # Open |
|                                   | GL API profiling feature;         |
|                                   |         'memory_for_all',  # memo |
|                                   | ry API profiling for all process  |
|                                   | binaries;                         |
|                                   |         'file_for_all',    # file |
|                                   |  API profiling for all process bi |
|                                   | naries;                           |
|                                   |         'network_for_all', # netw |
|                                   | ork API profiling for all process |
|                                   |  binaries;                        |
|                                   |         'context_switch',  # cont |
|                                   | ext switch profiling;             |
|                                   |         'lsan'             # Leak |
|                                   |  Sanitizer feature;               |
|                                   |     ]                             |
|                                   |                                   |
|                                   |     app = {                       |
|                                   |     # Dictionary that contains ap |
|                                   | plication profiling data and opti |
|                                   | ons;                              |
|                                   |                                   |
|                                   |         'app_info': {             |
|                                   |     # Dictionary that specifies a |
|                                   | pplication for profiling;         |
|                                   |                                   |
|                                   |             'type': 'NATIVE',     |
|                                   |     # Application type, possible  |
|                                   | values are:                       |
|                                   |     # NATIVE - for Tizen native a |
|                                   | pplications;                      |
|                                   |     # COMMON - for console applic |
|                                   | ations (isn't supported by SWAP); |
|                                   |     # RUNNING - for already runni |
|                                   | ng applications (isn't supported  |
|                                   | by SWAP);                         |
|                                   |     # WEB - for Tizen web applica |
|                                   | tions (doesn't supported now);    |
|                                   |                                   |
|                                   |             'id': 'org.example.fi |
|                                   | lemanager',                       |
|                                   |     # The second parameter depend |
|                                   | s on the type value:              |
|                                   |     # for NATIVE:                 |
|                                   |     # id - Tizen native applicati |
|                                   | on ID;                            |
|                                   |     # for COMMON:                 |
|                                   |     # path - path where applicati |
|                                   | on binary is located;             |
|                                   |     # for RUNNING:                |
|                                   |     # pid - PID of the target pro |
|                                   | cess. There is a special case for |
|                                   |  'pid': -1 - this causes system-w |
|                                   | ide instrumentation for all proce |
|                                   | sses;                             |
|                                   |     # id - Tizen ID of the target |
|                                   |  application;                     |
|                                   |     # path - path where applicati |
|                                   | on binary is located;             |
|                                   |     # for WEB:                    |
|                                   |     # id - Tizen web application  |
|                                   | ID.                               |
|                                   |                                   |
|                                   |         },                        |
|                                   |         'function_inst': {        |
|                                   |     # Dictionary that contains in |
|                                   | formation about binary instrument |
|                                   | ation probes;                     |
|                                   |                                   |
|                                   |             '/opt/usr/globalapps/ |
|                                   | org.example.filemanager/bin/filem |
|                                   | anager': [                        |
|                                   |     # Each key of a dictionary is |
|                                   |  a path to binary for profiling;  |
|                                   |                                   |
|                                   |                 ('main', 'xxxx',  |
|                                   | 'd'),                             |
|                                   |             ],                    |
|                                   |     # Each value is an array for  |
|                                   | the key binary that contains tupl |
|                                   | es of the following format:       |
|                                   |     # function name in '' or addr |
|                                   | ess;                              |
|                                   |     # string that describes argum |
|                                   | ents of a target function, one ch |
|                                   | aracter for each argument. The fo |
|                                   | llowing values are accepted:      |
|                                   |     # b - for bool value;         |
|                                   |     # c - for char value;         |
|                                   |     # f - for float value;        |
|                                   |     # d - for int value;          |
|                                   |     # x - for long value;         |
|                                   |     # p - for pointer value;      |
|                                   |     # w - for double value;       |
|                                   |     # s - for C-string;           |
|                                   |     # character that describes re |
|                                   | turned value. Accepted all charac |
|                                   | ters for arguments and more:      |
|                                   |     # v and n - for function retu |
|                                   | rns void                          |
+-----------------------------------+-----------------------------------+

### Python API and usage description

**SWAP Python tool** example also contains tools API usage example in
`example.py` file:

+-----------------------------------+-----------------------------------+
| File                              | Content description               |
+===================================+===================================+
| example.py                        |     #!/usr/bin/python2            |
|                                   |                                   |
|                                   |     import time                   |
|                                   |     from swap_cli import swap     |
|                                   |     # To use SWAP Python tool swa |
|                                   | p module should be imported from  |
|                                   | swap_cli folder.                  |
|                                   |                                   |
|                                   |     def simple_cb(data):          |
|                                   |         pass                      |
|                                   |                                   |
|                                   |     # load configs                |
|                                   |     c = swap.Client('example/emul |
|                                   | ator.py')                         |
|                                   |     c.load_config(['example/examp |
|                                   | le_conf.py'])                     |
|                                   |     # SWAP Python tool interface  |
|                                   | is provided via Client class obje |
|                                   | ct. Client class object construct |
|                                   | or takes path to the target confi |
|                                   | g as an argument, so the user sho |
|                                   | uld have one Client for each targ |
|                                   | et. To provide profiling session  |
|                                   | configuration, load_config() meth |
|                                   | od is used, it takes profiling se |
|                                   | ssion config file as an argument. |
|                                   |                                   |
|                                   |     c.set_event_cb('MSG_PROCESS_I |
|                                   | NFO', simple_cb)                  |
|                                   |     # After necessary configurati |
|                                   | ons are loaded, some additional p |
|                                   | reparations can be done, for exam |
|                                   | ple, in this example callback is  |
|                                   | set on MSG_PROCESS_INFO - it will |
|                                   |  be called when MSG_PROCESS_INFO  |
|                                   | will be received.                 |
|                                   |                                   |
|                                   |     # instrumentation             |
|                                   |     c.start('/tmp/outdir')        |
|                                   |     # Profiling is started by sta |
|                                   | rt() method, it takes output fold |
|                                   | er path as an argument. In an out |
|                                   | put folder, you can find trace an |
|                                   | d another additional data (LSan r |
|                                   | eports) after profiling.          |
|                                   |                                   |
|                                   |     time.sleep(60)                |
|                                   |     c.stop()                      |
|                                   |     # Profiling is finished by ca |
|                                   | lling stop() method.              |
+-----------------------------------+-----------------------------------+

The whole **SWAP Python tool** API is described below:

+-----------------+-----------------+-----------------+-----------------+
| API name        | Arguments       | Return value    | Description     |
+=================+=================+=================+=================+
|     class Clien | `target_conf`\  | object of       | The class       |
| t               | string path to  | `Client class`  | provides all    |
|                 | a file, that    |                 | **SWAP Python   |
|     (constructo | contains target |                 | tool**          |
| r) (target conf | device/emulator |                 | functionality,  |
| )               | config (see     |                 | which is        |
|                 | above           |                 | implemented as  |
|                 | description of  |                 | methods of the  |
|                 | `emulator.py`   |                 | class.\         |
|                 | for details)    |                 | The class       |
|                 |                 |                 | constructor     |
|                 |                 |                 | takes target    |
|                 |                 |                 | configuration   |
|                 |                 |                 | file path as an |
|                 |                 |                 | argument, so,   |
|                 |                 |                 | if several      |
|                 |                 |                 | different       |
|                 |                 |                 | targets are     |
|                 |                 |                 | used for        |
|                 |                 |                 | profiling,      |
|                 |                 |                 | several         |
|                 |                 |                 | `Client` class  |
|                 |                 |                 | objects should  |
|                 |                 |                 | be created.     |
|                 |                 |                 | Configuration   |
|                 |                 |                 | file            |
|                 |                 |                 | description and |
|                 |                 |                 | details can be  |
|                 |                 |                 | found above as  |
|                 |                 |                 | a description   |
|                 |                 |                 | of              |
|                 |                 |                 | `emulator.py`.  |
+-----------------+-----------------+-----------------+-----------------+
|     get_version | None            | string that     | Returns **SWAP  |
| ()              |                 | matches **SWAP  | Python tool**   |
|                 |                 | Python tool**   | version.        |
|                 |                 | version         |                 |
+-----------------+-----------------+-----------------+-----------------+
|     load_config | `path`\         | None            | This function   |
| (path)          | string, path to |                 | is used to load |
|                 | a file that     |                 | application\'s  |
|                 | contains        |                 | profiling data, |
|                 | profiling       |                 | i.e. which      |
|                 | session         |                 | application is  |
|                 | configuration   |                 | a target one,   |
|                 | (see above      |                 | which features  |
|                 | description of  |                 | should be used. |
|                 | `example_conf.p |                 | `example_conf.p |
|                 | y`              |                 | y`              |
|                 | for details)    |                 | can be used as  |
|                 |                 |                 | an example of   |
|                 |                 |                 | this            |
|                 |                 |                 | configuration   |
|                 |                 |                 | file, its       |
|                 |                 |                 | description     |
|                 |                 |                 | above covers    |
|                 |                 |                 | all of the      |
|                 |                 |                 | possible        |
|                 |                 |                 | meanings.       |
+-----------------+-----------------+-----------------+-----------------+
|     set_event_c | `event`\        | None            | This function   |
| allback(event,  | string, that    |                 | allows          |
| callback)       | matches message |                 | registering     |
|                 | name\           |                 | user-defined    |
|                 | `callback`\     |                 | callback on any |
|                 | pointer to a    |                 | received SWAP   |
|                 | function that   |                 | message. Event  |
|                 | will be called  |                 | name depends on |
|                 | when event      |                 | a protocol that |
|                 | message is      |                 | is being used   |
|                 | received        |                 | and can be      |
|                 |                 |                 | received from   |
|                 |                 |                 | protocol        |
|                 |                 |                 | description.    |
|                 |                 |                 | For example,    |
|                 |                 |                 | protocol 4.2    |
|                 |                 |                 | supports the    |
|                 |                 |                 | following event |
|                 |                 |                 | names:          |
|                 |                 |                 |                 |
|                 |                 |                 | -   MSG\_PROCES |
|                 |                 |                 | S\_INFO         |
|                 |                 |                 | -   MSG\_TERMIN |
|                 |                 |                 | ATE             |
|                 |                 |                 | -   MSG\_ERROR  |
|                 |                 |                 | -   MSG\_SAMPLE |
|                 |                 |                 | -   MSG\_SYSTEM |
|                 |                 |                 | -   MSG\_FUNCTI |
|                 |                 |                 | ON\_ENTRY       |
|                 |                 |                 | -   MSG\_FUNCTI |
|                 |                 |                 | ON\_EXIT        |
|                 |                 |                 | -   MSG\_SYSCAL |
|                 |                 |                 | L\_ENTRY        |
|                 |                 |                 | -   MSG\_SYSCAL |
|                 |                 |                 | L\_EXIT         |
|                 |                 |                 | -   MSG\_FILE\_ |
|                 |                 |                 | FUNCTION\_ENTRY |
|                 |                 |                 | -   MSG\_FILE\_ |
|                 |                 |                 | FUNCTION\_EXIT  |
|                 |                 |                 | -   MSG\_PROCES |
|                 |                 |                 | S\_STATUS\_INFO |
|                 |                 |                 | -   MSG\_CONTEX |
|                 |                 |                 | T\_SWITCH\_ENTR |
|                 |                 |                 | Y               |
|                 |                 |                 | -   MSG\_CONTEX |
|                 |                 |                 | T\_SWITCH\_EXIT |
|                 |                 |                 | -   MSG\_PROCES |
|                 |                 |                 | S\_MAP          |
|                 |                 |                 | -   MSG\_PROCES |
|                 |                 |                 | S\_UNMAP        |
|                 |                 |                 | -   MSG\_WEB\_S |
|                 |                 |                 | AMPLING         |
|                 |                 |                 | -   MSG\_APP\_S |
|                 |                 |                 | ETUP\_STAGE     |
|                 |                 |                 | -   MSG\_WEB\_A |
|                 |                 |                 | PP\_SETUP\_STAG |
|                 |                 |                 | E               |
|                 |                 |                 | -   MSG\_FBI    |
|                 |                 |                 | -   MSG\_UI\_HI |
|                 |                 |                 | ERARCHY         |
|                 |                 |                 | -   MSG\_PROBE\ |
|                 |                 |                 | _MEMORY         |
|                 |                 |                 | -   MSG\_PROBE\ |
|                 |                 |                 | _UIEVENT        |
|                 |                 |                 | -   MSG\_PROBE\ |
|                 |                 |                 | _RESOURCE       |
|                 |                 |                 | -   MSG\_PROBE\ |
|                 |                 |                 | _LIFECYCLE      |
|                 |                 |                 | -   MSG\_PROBE\ |
|                 |                 |                 | _SCREENSHOT     |
|                 |                 |                 | -   MSG\_PROBE\ |
|                 |                 |                 | _THREAD         |
|                 |                 |                 | -   MSG\_PROBE\ |
|                 |                 |                 | _SYNC           |
|                 |                 |                 | -   MSG\_PROBE\ |
|                 |                 |                 | _NETWORK        |
|                 |                 |                 | -   MSG\_PROBE\ |
|                 |                 |                 | _GL             |
|                 |                 |                 | -   MSG\_LSAN   |
|                 |                 |                 |                 |
|                 |                 |                 | To get          |
|                 |                 |                 | description     |
|                 |                 |                 | which message   |
|                 |                 |                 | stands for      |
|                 |                 |                 | which event,    |
|                 |                 |                 | please refer to |
|                 |                 |                 | the protocol    |
|                 |                 |                 | description.\   |
|                 |                 |                 | `callback` is a |
|                 |                 |                 | pointer to the  |
|                 |                 |                 | callback        |
|                 |                 |                 | function which  |
|                 |                 |                 | should be       |
|                 |                 |                 | called when     |
|                 |                 |                 | `event` message |
|                 |                 |                 | is received.    |
|                 |                 |                 | The callback    |
|                 |                 |                 | function should |
|                 |                 |                 | have the        |
|                 |                 |                 | following       |
|                 |                 |                 | signature:\     |
|                 |                 |                 | `callback(data) |
|                 |                 |                 | `\              |
|                 |                 |                 | where `data` is |
|                 |                 |                 | message         |
|                 |                 |                 | payload.        |
|                 |                 |                 | Payload has a   |
|                 |                 |                 | protocol- and   |
|                 |                 |                 | message-specifi |
|                 |                 |                 | c               |
|                 |                 |                 | format, so,     |
|                 |                 |                 | please refer to |
|                 |                 |                 | the protocol    |
|                 |                 |                 | description for |
|                 |                 |                 | details.        |
+-----------------+-----------------+-----------------+-----------------+
|     start(outdi | `outdir`\       | None            | It establishes  |
| r)              | string with     |                 | connection      |
|                 | path to an      |                 | between **SWAP  |
|                 | output          |                 | Python tool**   |
|                 | directory where |                 | on host and     |
|                 | trace, LSan     |                 | **SWAP** on     |
|                 | reports,        |                 | target and      |
|                 | necessary       |                 | starts          |
|                 | target info     |                 | profiling       |
|                 | etc. will be    |                 | target          |
|                 | located. The    |                 | application.    |
|                 | directory will  |                 | After workflow  |
|                 | be created if   |                 | has returned    |
|                 | it doesn\'t     |                 | from `start()`  |
|                 | exist.          |                 | **SWAP** is     |
|                 |                 |                 | supposed to be  |
|                 |                 |                 | executed on     |
|                 |                 |                 | target. Trace   |
|                 |                 |                 | is saved to     |
|                 |                 |                 | <outdir>`/trace |
|                 |                 |                 | .bin file`.     |
+-----------------+-----------------+-----------------+-----------------+
|     is_alive()  | None            | bool - True if  | Function checks |
|                 |                 | **SWAP** has    | if connection   |
|                 |                 | returned        | with target     |
|                 |                 | response, False | **SWAP** works  |
|                 |                 | otherwise       | and if **SWAP** |
|                 |                 |                 | responds on     |
|                 |                 |                 | host\'s         |
|                 |                 |                 | requests.       |
+-----------------+-----------------+-----------------+-----------------+
|     stop()      | None            | None            | Stops tracing,  |
|                 |                 |                 | closes          |
|                 |                 |                 | connection with |
|                 |                 |                 | the target      |
|                 |                 |                 | **SWAP**.       |
+-----------------+-----------------+-----------------+-----------------+

Trace Parser API description
----------------------------

Besides **SWAP** trace, **Trace Parser** also requires some additional
data about gathered trace: trace protocol version, target
device/emulator info about CPU cores count and count of energy devices
located on target (its top energy consumers, like LCD, CPU, WiFI and so
on). Optionally, API map list can be added from the target: it provides
additional data about gathered API functions.\
User can specify trace data manually or, which is most preferable, take
it from output directory of **SWAP tool** with the trace. File named
`session_data.json` contains all the necessary data for tracing.\
API map list file can also be found at the output of **SWAP tool**,
it\'s named `api_map_list`.

### Protocol versions

**Trace Parser** supports the following protocol versions:

-   3.0
-   4.0
-   4.1
-   4.2

Protocol version should be chosen the same as one on the target where
the trace was gathered. For detailed information and protocol
description, please refer to Protocol Description located at
`swap-manager/docs/protocol.rst` or at **swap-manager** README file.\
If the user hasn\'t specified any protocol version, **4.2** protocol
version will be used as default.

### Output types

**Trace Parser** supports the following output types:

  Type     Short   Description
  -------- ------- ----------------------------------------
  text     t       Output in human-readable text format
  python   p       Output is formatted like python module
  json     j       Output in JSON format
  csv      c       Output in comma-separated value format

The user can specify the type by its name (*Type column*) or short name
(*Short column*).

#### Text output format

    msg_id = 0x1                            //message ID number in hex format
    seq_num = 0                             //message sequence number
    sec = 1510680912                        //second when event has occurred
    usec = 436919901                        //microsecond when event has occurred
    payload_len = 8617                      //length of message specific data
    ...                                     // Rest is message specific information
    =============================           // Such line separates messages

#### Python output format

    trace_info = {                          # Contains data about parsed trace
        'protocol_version': 42              # Trace's protocol version
    }
    trace obj = [                           # Array that contains all trace messages. Each message is a dictionary
        {
            'msg_id': 0x1,                  # Message ID number in hex
            'seq_num': 0,                   # Message sequence number
            'sec': 1510680912,              # Second when event has occurred
            'usec': 436919901,              # Microsecond when event has occurred
            'payload_len': 8617,            # Length of message specific data
            ...,                            # Message specific data
        },
        ...                                 # Other messages
    ]

#### JSON output format

    {
    "trace_info" : {                        # Contains data about parsed trace
        "protocol_version" : 42             # Trace's protocol version
    },
    "trace_obj" : [                         # Contains all trace messages
        {
            "msg_id" : 1,                   # Message ID number
            "seq_num': 0,                   # Message sequence number
            "sec": 1510680912,              # Second when event has occurred
            "usec": 436919901,              # Microsecond when event has occurred
            "payload_len": 8617,            # Length of message specific data
            ...                             # Message specific data
        },
        ...                                 # Other messages
    ]

#### CSV output format

  Message ID   Sequence number   Second        Microsecond   Length   Message specific data
  ------------ ----------------- ------------- ------------- -------- -----------------------
  0x1,         0,                1510680912,   436919901,    8617,    \...

### Arguments description

**Trace Parser** supports the following command-line arguments:

  Argument           Options                 Description
  ------------------ ----------------------- -------------------------------------------------------------------------------------------------------------------------------
  \--help, -h                                Print usage
  \--input, -i       input file path         Path to trace file. If not specified, trace is taken from `stdio`. **Optional**
  \--output, -o      output file path        Path to output file. If not specified, data outputted to `stdout`. **Optional**
  \--session, -s     session data file       Path to `session_data.json` file. If not specified, target data is taken from command line arguments or default. **Optional**
  \--api\_map, -a    API map list file       Path to `api_map_list` file. **Optional**
  \--cpu\_num, -c    CPUs number             Number of CPUs at the target device. If not specified, is taken from `session_data.json` or default. **Optional**
  \--devs\_num, -d   energy devices number   Number of energy devices on target. If not specified, is taken from `session_data.json` or default. **Optional**
  \--version, -v     protocol version        Protocol version. If not specified, is taken from `session_data.json` or default. **Optional**
  \--type, -t        output type             Output format

You can run **Trace Parser** by running the following command in a
directory, which contains `swap_parser` executable and `libspp.so`
library. For example, with `session_data.json` and `api_map_list`
specified:

    $ ./swap_parser -i trace.bin -o trace.txt -s session_data.json -a api_map_list -t text

This command will read `trace.bin`, parse it into text format and output
to `trace.txt`. The same command, if target info data is specified
manually:

    $ ./swap_parser -i trace.bin -o trace.txt -c 4 -d 5 -v 4.2 -a api_map_list -t text

If user wants to use default data, it will be like the following:

    $ ./swap_parser -i trace.bin -o trace.txt -t text

Or the minimum command, that expects trace at `stdin` and outputs it to
`stdout`:

    $ ./swap_parser -t text

For **Development and support** guide see attached ![Trace Parser
maintain readme](MAINTAIN.pdf "fig:Trace Parser maintain readme").

Advanced usage examples
-----------------------

All the examples below expects that the preparation work has been
already done and that current directory is <swap-manager>`/src/cli/`.

### Function profiling on emulator, storing data in human-readable format

-   Creating target configuration file, saved as `target_conf.py`:

<!-- -->

    api_version = '1.0'

    connection = {
            'ip': "127.0.0.1",

            'type': "sdb",
            'type_info': {
                    'target': 'emulator',
            },
    }

-   Creating profiling session configuration file, saved as
    `session_conf.py`:

<!-- -->

    api_version = '1.0'

    env = {
            'apps_path': "/opt/usr/globalapps/",
    }

    features = [
    ]

    app = {
        'app_info': {
            'type': 'NATIVE', 'id': 'org.example.filemanager',
        },

        'function_inst': {
            '/opt/usr/globalapps/org.example.filemanager/bin/filemanager': [
                ('main', 'xxxx', 'd'),
            ],
            '/lib/libc.so.6': [
                ('malloc', 'd', 'p'),
            ],
        },
    }

-   Creating execution script, saved as `run_script.py`:

<!-- -->

    #!/usr/bin/python2

    import time
    from swap_cli import swap

    # load configs
    c = swap.Client('target_conf.py')
    c.load_config(['session_conf.py'])

    # instrumentation
    c.start('/tmp/outdir')
    time.sleep(60)
    c.stop()

-   Execute run\_script.py and wait till it finished;
-   Parse binary trace to human-readable format:

<!-- -->

    $ trace_parser/bin/swap_parser -i /tmp/outdir/trace.bin -o /tmp/parsed_trace.txt -t t -s /tmp/outdir/session_info.json

-   Now parsed trace is stored at `/tmp/parsed_trace.txt`.

### Memory profiling on device, storing data in Python module format

-   Modifying created `target_conf.py`:

<!-- -->

    api_version = '1.0'

    connection = {
            'ip': "127.0.0.1",

            'type': "sdb",
            'type_info': {
                    'target': 'device',
            },
    }

-   Modifying created `session_conf.py`:

<!-- -->

    api_version = '1.0'

    env = {
            'apps_path': "/opt/usr/globalapps/",
    }

    features = [
        'memory'
    ]

    app = {
        'app_info': {
            'type': 'NATIVE', 'id': 'org.example.filemanager',
        },
    }

-   Execute `run_script.py` and wait till it finished;
-   Parse binary trace to Python module format:

<!-- -->

    $ trace_parser/bin/swap_parser -i /tmp/outdir/trace.bin -o /tmp/parsed_trace.py -t p -s /tmp/outdir/session_info.json

-   Now parsed trace is located at `/tmp/parsed_trace.py`, it can be
    imported at any Python script with the code like, depending on the
    Python script location:

<!-- -->

    import parsed_trace

### Counting malloc()\'s for the application on device

-   Modifying `session_conf.py`:

<!-- -->

    api_version = '1.0'

    env = {
            'apps_path': "/opt/usr/globalapps/",
    }

    features = [
    ]

    app = {
        'app_info': {
            'type': 'NATIVE', 'id': 'org.example.filemanager',
        },

        'function_inst': {
            '/lib/libc.so.6': [
                ('malloc', 'd', 'p'),
            ],
        },
    }

-   Modifying execution script `run_script.py`:

<!-- -->

    #!/usr/bin/python2

    import time
    from swap_cli import swap

    malloc_cnt = 0

    def malloc_cb(data):
        malloc_cnt += 1

    # load configs
    c = swap.Client('target_conf.py')
    c.load_config(['session_conf.py'])
    c.set_event_cb('MSG_FUNCTION_ENTRY', malloc_cb)

    # instrumentation
    c.start('/tmp/outdir')
    time.sleep(60)
    c.stop()

    print "Malloc count = " + malloc_cnt

-   Execute `run_script.py` and wait till it finished
-   At the end, `malloc()`\'s count is printed in `stdout`.

[Category:Tool](Category:Tool "wikilink")
