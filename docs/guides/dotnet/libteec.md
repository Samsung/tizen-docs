TEE Communication
=================

## Dependencies

- Tizen 4.0 and Higher

You can create secure communications by executing your application in a
trusted execution environment (TEE), and communicating with other
applications within that environment. To implement TEE communication,
you can use the libteec API, which is based on the GlobalPlatform® [TEE
Client API](https://www.globalplatform.org/specificationsdevice.asp).

You can run applications in 2 environments: a rich world (like Linux)
with client applications (CA) and a secure world with trusted
applications (TA).

**Figure: TEE communication architecture**

![TEE communication architecture](../images/libteec_architecture.png)

The main features of the Tizen.Security.TEEC namespace include:

-   Connecting to a trusted application

    You can securely [connect to a trusted
    application](#connecting_applications) by creating a new session.

- Sending commands to a trusted application

    You can [pass commands from a client application to a trusted
    application](#sending_secure_commands), including [using shared
    memory blocks](#using_shared_memory).


Prerequisites
-------------

To enable your application to use the TEE communication functionality:

1.  To make your application visible in the Tizen Store only for devices
    that support TEE communication, the application must specify the
    following feature in the `tizen-manifest.xml` file:

    ``` {.prettyprint}
    <feature name="http://tizen.org/feature/security.tee"/>
    ```

    You can also check whether a device supports the Tizen.Security.TEEC
    namespace by using the `TryGetValue()` method of the
    [Tizen.System.SystemInfo](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1SystemInfo.html)
    class and, accordingly, enabling or disabling the code requiring the
    namespace:

    ``` {.prettyprint}
    const string TEEC_FEATURE_KEY = "http://tizen.org/feature/security.tee";
    bool ret;

    if (SystemInfo.TryGetValue<bool>(TEEC_FEATURE_KEY, out ret) == false)
    {
        /// Error handling
    }
    ```

    **Note** In TV applications, you can test the TEE communication
    functionality on an emulator only. Most target devices do not
    currently support this feature.

    ​

2. To use the methods and properties of the
    [Tizen.Security.TEEC](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Security_1_1TEEC.html)
    namespace, include it in your application:

    ``` {.prettyprint}
    using Tizen.Security.TEEC;
    ```

3. Initialize a new TEEC context by creating an instance of the
    [Tizen.Security.TEEC.Context](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Security_1_1TEEC_1_1Context.html)
    class:

    ``` {.prettyprint}
    Context ctx = new Context(null);
    ```

    When it is no longer needed, destroy the TEEC context:

    ``` {.prettyprint}
    ctx.Dispose();
    ```


Connecting Applications <a id="connecting_applications"></a>
-----------------------

To communicate between applications, you must connect a client
application to a trusted application by creating a session:

1.  Open a session with the `OpenSession()` method of the
    [Tizen.Security.TEEC.Context](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Security_1_1TEEC_1_1Context.html)
    class, which returns the session as a new instance of the
    [Tizen.Security.TEEC.Session](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Security_1_1TEEC_1_1Session.html) class.

    ``` {.prettyprint}
    Guid ta_uuid = new Guid("  "); /// Trusted application GUID
    try
    {
        Session ses = ctx.OpenSession(ta_uuid);
    ```

2. When it is no longer needed, close the session with the `Close()`
    method of the `Tizen.Security.TEEC.Session` class:

    ``` {.prettyprint}
        ses.Close();
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```


Sending Secure Commands <a id="sending_secure_commands"></a>
-----------------------

After opening a session with a trusted application, a client application
can execute functions in the trusted application by sending secure
commands to the trusted application.

To send function call commands:

-   To send a command for invoking a function without parameters, use
    the `InvokeCommand()` method of the
    [Tizen.Security.TEEC.Session](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Security_1_1TEEC_1_1Session.html)
    class, with the first parameter identifying the function to be
    executed by the trusted application:

    ``` {.prettyprint}
    try
    {
        ses.InvokeCommand(1, null);
    }
    catch (Exception e)
    {
        /// Error handling
    }
    ```

- To send a command for invoking a function with simple integer
    parameters:
    1.  Create the parameters as new instances of the
        [Tizen.Security.TEEC.Value](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Security_1_1TEEC_1_1Value.html)
        class:

        ``` {.prettyprint}
        try
        {
            Value p1 = new Value(1, 2, TEFValueType.InOut);
            Value p2 = new Value(10, 200, TEFValueType.InOut);
        ```

    2. Send the command to the trusted application with the
        `InvokeCommand()` method of the
        `Tizen.Security.TEEC.Session` class. The second parameter is a
        new instance of the
        [Tizen.Security.TEEC.Parameter](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Security_1_1TEEC_1_1Parameter.html)
        class containing the 2 integer parameter values.

        ``` {.prettyprint}
            ses.InvokeCommand(1, new Parameter[] {p1, p2});
        }
        catch (Exception e)
        {
            /// Error handling
        }
        ```

- To send a command for invoking a function with a local memory
    reference as a parameter:
    1.  Create a temporary memory reference as a new instance of the
        [Tizen.Security.TEEC.TempMemoryReference](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Security_1_1TEEC_1_1TempMemoryReference.html)
        class:

        ``` {.prettyprint}
        try
        {
            long val = 10;
            TempMemoryReference p1 = new TempMemoryReference((IntPtr)(&val), 1024, TEFTempMemoryType.InOut);
        ```

    2. Send the command to the trusted application with the
        `InvokeCommand()` method of the
        `Tizen.Security.TEEC.Session` class. The second parameter is a
        new instance of the `Tizen.Security.TEEC.Parameter` class
        containing the memory reference.

        ``` {.prettyprint}
            ses.InvokeCommand(1, new Parameter[] {p1});
        }
        catch (Exception e)
        {
            /// Error handling
        }
        ```


Using Shared Memory <a id="using_shared_memory"></a>
-------------------

To share a memory block between a client application and a trusted
application:

-   To send a function call command to the trusted application,
    including an allocated shared memory reference:
    1.  Allocate a new memory block as shared memory with the
        `AllocateSharedMemory()` method of the
        [Tizen.Security.TEEC.Context](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Security_1_1TEEC_1_1Context.html)
        class, which returns the block as a new instance of the
        [Tizen.Security.TEEC.SharedMemory](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Security_1_1TEEC_1_1SharedMemory.html)
        class:

        ``` {.prettyprint}
        try
        {
            SharedMemory shm = ctx.AllocateSharedMemory(1024, SharedMemoryFlags.InOut);
        ```

    2. Register a memory reference based on the shared memory block by
        creating a new instance of the
        [Tizen.Security.TEEC.RegisteredMemoryReference](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Security_1_1TEEC_1_1RegisteredMemoryReference.html)
        class, and send the function call command to the trusted
        application with the `InvokeCommand()` method of the
        [Tizen.Security.TEEC.Session](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Security_1_1TEEC_1_1Session.html) class.
        The registered memory reference is passed in a new instance of
        the
        [Tizen.Security.TEEC.Parameter](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Security_1_1TEEC_1_1Parameter.html) class.

        ``` {.prettyprint}
            RegisteredMemoryReference p1 = new RegisteredMemoryReference(shm, 1024, 0, RegisteredMemoryReference.InOut);
            ses.InvokeCommand(1, new Parameter[] {p1});
        ```

    3. Release the shared memory:

        ``` {.prettyprint}
            ctx.ReleaseSharedMemory(shm);
        }
        catch (Exception e)
        {
            /// Error handling
        }
        ```

- To send a function call command to the trusted application,
    including an external shared memory reference:
    1.  Register a block of existing client application memory as shared
        memory with the `RegisterSharedMemory()` method of the
        `Tizen.Security.TEEC.Context` class, which returns the block as
        a new instance of the `Tizen.Security.TEEC.SharedMemory` class:

        ``` {.prettyprint}
        try
        {
            IntPtr memaddr = <Some memory address>;
            SharedMemory shm = ctx.RegisterSharedMemory(memaddr, 1024, SharedMemoryFlags.InOut);
        ```

    2. Register a memory reference based on the shared memory block by
        creating a new instance of the
        `Tizen.Security.TEEC.RegisteredMemoryReference` class, and send
        the function call command to the trusted application with the
        `InvokeCommand()` method of the
        `Tizen.Security.TEEC.Session` class. The registered memory
        reference is passed in a new instance of the
        `Tizen.Security.TEEC.Parameter` class.

        ``` {.prettyprint}
            RegisteredMemoryReference p1 = new RegisteredMemoryReference(shm, 1024, 0, RegisteredMemoryReference.InOut);
            ses.InvokeCommand(1, new Parameter[] {p1});
        ```

    3. Release the shared memory:

        ``` {.prettyprint}
            ctx.ReleaseSharedMemory(shm);
        }
        catch (Exception e)
        {
            /// Error handling
        }
        ```


