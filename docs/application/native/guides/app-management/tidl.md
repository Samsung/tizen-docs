
# TIDL

TIDL is a programming language to define interfaces for communicating among applications in Tizen.
It provides methods to create a Remote Procedure Call (RPC) or Remote Method Invocation (RMI) in Tizen.

## TIDLC

**TIDLC** is a compiler for creating stub or proxy code block from **TIDL** file.

### Usage
```
Usage:
  tidlc [OPTION...]

  -h, --help                  Show help options.
  -l, --language=LANGUAGE     Select generating language (C, C++, C#, Java(CION only)).
  -i, --input=INPUT           A tidl interface file.
  -o, --output=OUTPUT         Generate an interface file.
  -p, --proxy                 Generate proxy code.
  -s, --stub                  Generate stub code.
  -r, --rpclib                Generate C# library for rpc-port.
  -t, --thread                Generate thread code with stub code.
  -b, --beta                  Use beta version for private file sharing.
  -c, --cion                  Generate CION code.
  -v, --version               Show version information.

```
> [!NOTE]
> Generating thread option with `-t` or `--thread`, and using beta version options with `-b` or `--beta` are supported since Tizen 6.0.
> Generating cion option with `-c` or `--cion` is supported since Tizen 6.5.

## TIDL Syntax

### 'interface'
It generates an interface to communicate between proxy and stub.

**Syntax**
```csharp
[<attributes>]
interface <interface_id> {
<return_type> <method_name>(
[<empty> | 'in' | 'out' | 'ref']
<type> <parameter_id>, ... [<empty> | 'async' | 'delegate'];
...
}
```
**Example**
```csharp
[privilege="http://tizen.org/privilege/appmanager.launch"]
interface ITest {
	// by default, 'in' is used as direction keyword
	int SetVal(in  int val1, char val2);
	char GetVal(out  int val1, out  char val2);
}
```

### Attributes
It indicates required privileges and trusted signature.
By default, `trusted` is `false`.

**Syntax**
```
[ <key> = <value>, ...]
interface <interface_id> { ... }
<key> :=  privilege | trusted
<value> := <string> | "true" | "false"
```

**Example**
```csharp
// Require launch privilege
[privilege="http://tizen.org/privilege/appmanager.launch"]
interface ITest {}

// Require privilege A , privilege B and trusted signature
[privilege="http://samsung.com/appdefined/A",
 privilege="http://samsung.com/appdefined/B" , trusted  = "true"]
interface ITest2 {}
```

### 'async'
It denotes one-way-call.

>**Note**
>
> Returned type should be `void`
>
> Keyword `out` is not allowed

**Example**
```csharp
interface ITest {
	void  SetValAsync(int val1, char val2) async;
}
```

### 'delegate'
It denotes one-way-call from service.

> **Note**
>
> Returned type should be `void`.
>
> Keyword `out` is not allowed.
>
> Delegate type is regarded as a type in methods but you can't use it in `struct` type.


**Example**
```csharp
interface ITest {
	void OnReceivedEvent(string msg, bundle b) delegate;
	int RegisterEvent(OnReceivedEvent cb);
	int UnregisterEvent(OnReceivedEvent cb);
}
```

### 'struct'
It allows developers to define user-defined types.
It is also possible to be used in `struct` or method syntax.

**Syntax**
```csharp
struct <struct_id> {
    <type> <id>;
    ...
}
```

**Example**
```csharp
struct Student  {
    string name;
    int num;
    bundle data;
}
```

## TIDL Type System
 - Built-in type (`in` direction case)

	| TIDL type   |Size  |C# type |C++ type  |C type|JAVA type|
	|------------|------|--------|----------|------|---------|
	| void   |0|void |void  |void|void|void|
	| char|1|byte|char|char|byte|
	| short|2|short|short int|short int|short|
	| int|4|int |int  |int|int|
	| long|8|long|long long|long long|long|
	| float|4|float|float|float|float
	| double|8|double|double|double|double|
	| bundle|variable|Bundle|Bundle|bundle *|N/A|
	| string|variable|string|std::string|const char *|String|
	| bool|1|bool|bool|bool|boolean|
> [!NOTE]
> bundle type is not supported for CION

 - Container type
	 - **list< [type] >**  or  **array<[type]>**
		- Used when sending list or array of some types
		- Similar to c++ std::list or std::vector
		- Can be nested

	| TIDL type  | C# type| C++ type |C type |JAVA type|
	|--|--|--|--|--|
	| list<>  | LinkedList<> |std::list<> |Handle (pointer)| LinkedList<> |
	| array<> | List<>|std::vector<> |Handle (pointer)| ArrayList<> |

  - User-defined type
	- Name defined by 'struct' syntax

## TIDL Generated Code

### Struct
**TIDL**
```csharp
struct Foo {
	int Age;
	string Name;
}
```

**C++**
```cpp
class Foo final { // Copyable and movable class
  Foo(); // Constructor
  Foo(int age, std::string name); // Constructor
  int GetAge() const; // Getter for property 'Age'
  void SetAge(int age); // Setter for property 'Age'
  const std::string& GetName() const; // Getter for property 'Name'
  void SetName(std::string name); // Setter for property 'Name'
};
```
**C#**
```csharp
public selaed class Foo  { // Class for Foo
	public  int Age { get; set; }  // Property for 'Age'
	public  string Name { get; set; } // Property for 'Name'
};
```
**C**
```c
typedef struct Foo_s *rpc_port_Foo_h; // Handle for Foo
int rpc_port_create_Foo(rpc_port_Foo_h* h); // Constructor for Foo
int rpc_port_destroy_Foo(rpc_port_Foo_h h); // Destructor for Foo
int rpc_port_clone_Foo(rpc_port_Foo_h h, rpc_port_Foo_h* clone); // Copy constructor for Foo
int rpc_port_set_Foo_Age(rpc_port_Foo_h h, int Age); // Setter for property 'Age'
int rpc_port_set_Foo_Name(rpc_port_Foo_h h, const char* Name); // Setter for property 'Name'
int rpc_port_get_Foo_Age(rpc_port_Foo_h h, int* Age); // Getter for property 'Age'
int rpc_port_get_Foo_Name(rpc_port_Foo_h h, char** Name); // Getter for property 'Name'
```

**C (Since TIDL version 1.5.0)**
```c
typedef struct rpc_port_proxy_Foo_s *rpc_port_proxy_Foo_h; // Handle for Foo
int rpc_port_proxy_Foo_create(rpc_port_proxy_Foo_h *h); // Constructor for Foo
int rpc_port_proxy_Foo_destroy(rpc_port_proxy_Foo_h h); // Destructor for Foo
int rpc_port_proxy_Foo_clone(rpc_port_proxy_Foo_h h, rpc_port_proxy_Foo_h *clone); // Copy constructor for Foo
int rpc_port_proxy_Foo_set_Age(rpc_port_proxy_Foo_h h, int value); // Setter for property 'Age'
int rpc_port_proxy_Foo_get_Age(rpc_port_proxy_Foo_h h, int *value); // Getter for property 'Age'
int rpc_port_proxy_Foo_set_Name(rpc_port_proxy_Foo_h h, const char *value); // Setter for property 'Name'
int rpc_port_proxy_Foo_get_Name(rpc_port_proxy_Foo_h h, char **value); // Getter for property 'Name'
```

### Proxy Interface

**TIDL**
```csharp
interface Runnable {
	int Run(Foo foo);
}
```

**C++**
```cpp
class Runnable  {
  class IEventListener { // Events about connection
    virtual void OnConnected() = 0;
    virtual void OnDisconnected() = 0;
    virtual void OnRejected() = 0;
  };

  Runnable(IEventListener* listener, const std::string& target_appid); // Constructor
  virtual ~Runnable(); // Destructor
  int Connect(); // Method for connecting service app
  void Disconnect(); // Method for disconnecting service app (Since Tizen 6.5)
  int Run(Foo foo); //Method  from TIDL
};
```

**C#**
```csharp
public class Runnable : IDisposable  {
	public event EventHandler Connected; // Event handler
	public event EventHandler Disconnected; // Event handler
	public event EventHandler Rejected; // Event handler
	public Runnable(string appId); // Constructor
	public void Connect(); // Method for connecting service app
	public void Disconnect(); // Method for disconnecting service app (Since Tizen 6.5)
	public int Run(Foo foo); //Method from TIDL
	...
};
```

**C**
```c
typedef struct Runnable_s* rpc_port_proxy_Runnable_h; // Handle for 'Runnable'
typedef struct {
	void (*connected)(rpc_port_proxy_Runnable_h h, void* user_data); // Connected event callback
	void (*disconnected)(rpc_port_proxy_Runnable_h h, void* user_data); // Disconnected event callback
	void (*rejected)(rpc_port_proxy_Runnable_h h, void* user_data); // Rejected event callback
} rpc_port_proxy_Runnable_callback_s;

//  Function for creating Runnable proxy handle
int rpc_port_proxy_Runnable_create(const char* stub_appid,rpc_port_proxy_Runnable_callback_s* callback, void* user_data, rpc_port_proxy_Runnable_h* h);

//  Function for connecting to service app
int rpc_port_proxy_Runnable_connect(rpc_port_proxy_Runnable_h h);

//  Function for destroying Runnable proxy handle
int rpc_port_proxy_Runnable_destroy(rpc_port_proxy_Runnable_h h);

// Function from TIDL
int rpc_port_proxy_Runnable_invoke_Run(rpc_port_proxy_Runnable_h h, rpc_port_Foo_h foo);
```

**C (Since TIDL version 1.5.0)**
```c
// The rpc_port_proxy_Runnable handle.
typedef struct rpc_port_proxy_Runnable_s *rpc_port_proxy_Runnable_h;

// Called when the proxy is connected.
typedef void (*rpc_port_proxy_Runnable_connected_cb)(rpc_port_proxy_Runnable_h h, void *user_data);

// Called when the proxy is disconnected.
typedef void (*rpc_port_proxy_Runnable_disconnected_cb)(rpc_port_proxy_Runnable_h h, void *user_data);

// Called when the proxy is rejected.
typedef void (*rpc_port_proxy_Runnable_rejected_cb)(rpc_port_proxy_Runnable_h h, void *user_data);

// The structure type containing the set of callback functions for handling proxy events.
typedef struct {
	rpc_port_proxy_Runnable_connected_cb connected;  /**< This callback function is called when the proxy is connected to the stub. */
	rpc_port_proxy_Runnable_disconnected_cb disconnected;  /**< This callback function is called when the proxy is disconnected from the stub. */
	rpc_port_proxy_Runnable_rejected_cb rejected;  /**< This callback function is called when the proxy is rejected to connect to the stub. */
} rpc_port_proxy_Runnable_callback_s;

// Creates a rpc_port_proxy_Runnable handle.
int rpc_port_proxy_Runnable_create(const char *stub_appid, rpc_port_proxy_Runnable_callback_s *callback, void *user_data, rpc_port_proxy_Runnable_h *h);

// Destroys the rpc_port_proxy_Runnable handle.
int rpc_port_proxy_Runnable_destroy(rpc_port_proxy_Runnable_h h);

// Connects to the stub.
int rpc_port_proxy_Runnable_connect(rpc_port_proxy_Runnable_h h);

// Connects to the stub synchronously.
int rpc_port_proxy_Runnable_connect_sync(rpc_port_proxy_Runnable_h h);

// Disconnects from the stub. (Since Tizen 6.5)
int rpc_port_proxy_Runnable_disconnect(rpc_port_proxy_Runnable_h h);

// Calls the Run() method.
int rpc_port_proxy_Runnable_invoke_Run(rpc_port_proxy_Runnable_h h, rpc_port_proxy_Foo_h foo);
```
<<<<<<< HEAD
=======

**C++ for CION (Since Tizen 6.5)**
```cpp
class Runnable  {
  class IEventListener { // Events about connection
    virtual void OnConnected() = 0;
    virtual void OnDisconnected() = 0;
    virtual void OnRejected() = 0;
    virtual void OnDiscovered() = 0;
    virtual void OnFileReceived(cion_peer_info_h peer_info,
        cion_payload_h file_payload, cion_payload_transfer_status_e status) = 0;


  Runnable(IEventListener* listener, const std::string& target_appid); // Constructor
  virtual ~Runnable(); // Destructor
  int Connect(); // Method for connecting service app
  void Disconnect(); // Method for disconnecting service app
  void Discovery(); // Method for discovery cion server
  void StopDiscovery(); // Method for stop discovery cion server
  int Run(Foo foo); //Method  from TIDL
};
```

**C# for CION (Since Tizen 6.5)**
```csharp
public class Runnable : IDisposable  {
  public event DiscoveredEvent Discovered; // Event handler for cion
  public event DisconnectedEvent Disconnected; // Event handler for cion
  public event FileReceivedEvent FileReceived; // Event handler for cion
  public event ConnectionResultEvent ConnectionResult; // Event handler for cion
  public Runnable(string appId); // Constructor
  public void Connect(); // Method for connecting service app
  public void Disconnect(); // Method for disconnecting service app
  public int Run(Foo foo); //Method from TIDL
  ...
};
```

**C for CION (Since Tizen 6.5)**
```c
// The cion_proxy_Runnable handle.
typedef struct cion_proxy_Runnable_s *cion_proxy_Runnable_h;

// Called when the the connection is accepted or rejected.
typedef void (*cion_proxy_Runnable_connection_result_cb)(cion_proxy_ITest_h h,
    const cion_connection_result_h result, void *user_data);

// Called when the proxy is disconnected.
typedef void (*cion_proxy_Runnable_stub_disconnected_cb)(const cion_peer_info_h peer_info, void *user_data);

// Called when the stub is discovered.
typedef void (*cion_proxy_Runnable_stub_discovered_cb)(const cion_peer_info_h peer_info, void *user_data);

// Called when the payload is received.
typedef void (*cion_proxy_Runnable_file_received_cb)(const cion_peer_info_h peer_info, const cion_payload_h payload,
    cion_payload_transfer_status_e status, void *user_data);

// The structure type containing the set of callback functions for handling proxy events.
typedef struct {
  cion_proxy_Runnable_connection_result_cb connection_result;  /**< This callback function is called when the connection is accepted or rejected.*/
  cion_proxy_Runnable_disconnected_cb disconnected;  /**< This callback function is called when the proxy is disconnected from the stub. */
  cion_proxy_Runnable_stub_discovered_cb discovered;  /**< This callback function is called when the stub is discovered. */
  cion_proxy_Runnable_file_received_cb file_received;  /**< This callback function is called when the payload is received. */
} cion_proxy_Runnable_callback_s;


// Creates a cion_proxy_Runnable handle.
int cion_proxy_Runnable_create(const char *service_name, cion_proxy_Runnable_callback_s *callback, void *user_data, cion_proxy_Runnable_h *h);

// Destroys the cion_proxy_Runnable handle.
int cion_proxy_Runnable_destroy(cion_proxy_Runnable_h h);

// Tries connecting to the stub.
int cion_proxy_Runnable_try_connect(cion_proxy_Runnable_h h, const cion_peer_info_h peer_info);

// Disconnects to the stub.
int cion_proxy_Runnable_disconnect(cion_proxy_Runnable_h h);

// Tries to discover a stub.
int cion_proxy_Runnable_try_discovery(cion_proxy_Runnable_h h);

// Stops to discover a stub.
int cion_proxy_Runnable_stop_discovery(cion_proxy_Runnable_h h);

// Calls the Run() method.
int cion_proxy_Runnable_invoke_Run(cion_proxy_Runnable_h h, cion_proxy_Foo_h foo);
```

**JAVA for CION (Since Tizen 6.5)**
```java
public class Runnable extends ClientBase {
{
    // This method will be invoked when this client gets the response from the server
    @Override
    public void onConnectionResult(PeerInfo peerInfo, ConnectionResult result) {}

    // This method will be invoked when this client is disconnected from the server
    @Override
    public void onDisconnected(PeerInfo peerInfo) {}

    // This method will be invoked when an available server is discovered
    @Override
    public void onDiscovered(PeerInfo peerInfo) {}

    @Override
    public final void onResultReceived(PayloadAsyncResult payloadAsyncResult) {}

    @Override
    public final void onPayloadReceived(IPayload payload, PayloadTransferStatus status) {}

    // This method will be invoked when data for a file is received from the server
    public void onFileReceived(FilePayload payload, PayloadTransferStatus status) {}

    // Disposes delegate objects in this interface
    public void disposeCallback(String tag) {}

    // Constructor.
    public Runnable(Context context, String serviceName) {}

    // Method to implement.
    public int Run(Foo foo);
}
```

>>>>>>> tizen_6.5_prepare
### Stub Interface

**TIDL**
```csharp
interface Runnable {
	int Run(Foo foo);
}
```

**C++**
```cpp
class Runnable {
  class ServiceBase {
    class Factory {
      // The method for making service instances
      virtual std::unique_ptr<ServiceBase> CreateService(std::string sender, std::string instance) = 0;
    };

    virtual ~ServiceBase() = default;

    /// Gets client app ID
    const std::string& GetSender() const;

    /// Gets client instance ID
    const std::string& GetInstance() const;

    /// Sets the client app port
    void SetPort(rpc_port_h port);

    /// Disconnects from the client app (Since Tizen 6.5)
    void Disconnect();

    /// This method will be called when the client is connected
    virtual void OnCreate() = 0;

    /// This method will be called when the client is disconnected
    virtual void OnTerminate() = 0;

    virtual int Run(Foo foo) = 0;
  };

  Runnable();
  ~Runnable();

  /// Listens to client apps
  void Listen(std::shared_ptr<ServiceBase::Factory> service_factory);

  /// Gets service objects which are connected
  const std::list<std::shared_ptr<ServiceBase>>& GetServices();
  ...
};
```

**C#**
```csharp
public sealed class Runnable : IDisposable {
	public abstract class ServiceBase { // Abstract class for RPC service
		public abstract void OnCreate(); // Called when service object is created
		public abstract void OnTerminate(); // Called when service object is terminated
		public void Disconnect(); // Method for disconnecting port (Since Tizen 6.5)
		public abstract int Run(Foo foo); // Method to implement
		...
	};
	public Runnable(); // Constructor
	public  void Listen(Type serviceType); // Method for listening
	...
};
```

**C**
```c
// Handle for 'Runnable'
typedef struct Runnable_context_s* rpc_port_stub_Runnable_context_h;

// Set extra data into the context
int rpc_port_stub_Runnable_context_set_tag(rpc_port_stub_Runnable_context_h ctx, void* tag);

// Get extra data from the context
int rpc_port_stub_Runnable_context_get_tag(rpc_port_stub_Runnable_context_h ctx, void** tag);

typedef struct {
	// Called when service object is created
	void (*create)(rpc_port_stub_Runnable_context_h context, void* user_data);

	// Called when service object is terminated
	void (*terminate)(rpc_port_stub_Runnable_context_h context, void* user_data);

	// Called when proxy app send the request for 'Run'
	int (*Run)(rpc_port_stub_Runnable_context_h context, rpc_port_Foo_h foo, void *user_data);
} rpc_port_stub_Runnable_callback_s;

// Initialize interface 'Runnable'
int rpc_port_stub_Runnable_register(rpc_port_stub_Runnable_callback_s* callback, void* user_data);

// Deinitialize interface 'Runnable'
int rpc_port_stub_Runnable_unregister(void);
```

**C (Since TIDL version 1.5.0)**
```c
// The rpc_port_stub_Runnable_context handle.
typedef struct rpc_port_stub_Runnable_context_s *rpc_port_stub_Runnable_context_h;

// Called when the proxy is connected.
typedef void (*rpc_port_stub_Runnable_create_cb)(rpc_port_stub_Runnable_context_h context, void *user_data);

// Called when the proxy is disconnected.
typedef void (*rpc_port_stub_Runnable_terminate_cb)(rpc_port_stub_Runnable_context_h context, void *user_data);

// Called to get the proxy context once for each connected proxy.
typedef bool (*rpc_port_stub_Runnable_context_cb)(rpc_port_stub_Runnable_context_h context, void *user_data);

// Called when the request of the proxy is delivered.
typedef int (*rpc_port_stub_Runnable_Run_cb)(rpc_port_stub_Runnable_context_h context, rpc_port_stub_Foo_h foo, void *user_data);

// Sets the tag to the context handle.
int rpc_port_stub_Runnable_context_set_tag(rpc_port_stub_Runnable_context_h context, void *tag);

// Gets the tag from the context handle.
int rpc_port_stub_Runnable_context_get_tag(rpc_port_stub_Runnable_context_h context, void **tag);

// Gets the sender ID from the context handle.
int rpc_port_stub_Runnable_context_get_sender(rpc_port_stub_Runnable_context_h context, char **sender);

// Gets the instance ID from the context handle.
int rpc_port_stub_Runnable_context_get_instance(rpc_port_stub_Runnable_context_h context, char **instance);

// Disconnects from the proxy. (Since Tizen 6.5)
int rpc_port_stub_Runnable_context_disconnect(rpc_port_stub_Runnable_context_h context);

// The structure type containing the set of callback functions for handling stub events.
typedef struct {
	rpc_port_stub_Runnable_create_cb create;  /**< This callback function is invoked when the proxy is connected. */
	rpc_port_stub_Runnable_terminate_cb terminate;  /**< This callback function is invoked when the proxy is disconnected. */
	rpc_port_stub_Runnable_Run_cb Run;  /**< This callback function is invoked when the Run request is delivered. */
} rpc_port_stub_Runnable_callback_s;

// Registers the set of the callback functions and the port.
int rpc_port_stub_Runnable_register(rpc_port_stub_Runnable_callback_s *callback, void *user_data);

// Unregisters the registered port.
int rpc_port_stub_Runnable_unregister(void);

// Retrieves the connected context handles.
int rpc_port_stub_Runnable_foreach_context(rpc_port_stub_Runnable_context_cb callback, void *user_data);

// Gets the number of connected clients.
int rpc_port_stub_Runnable_get_client_number(unsigned int *client_number);
```

**C++ for CION (Since Tizen 6.5)**
```cpp
class Runnable {
  class ServiceBase {
    class Factory {
      // The method for making service instances
      virtual std::shared_ptr<ServiceBase> CreateService(cion_peer_info_h peer) = 0;
    };

    virtual ~ServiceBase() = default;

    const cion_peer_info_h GetPeer() const {
      return peer_;
    }

    /// <summary>
    /// This method will be called when file receieved from client app
    /// </summary>
    virtual void OnFileReceived(cion_peer_info_h peer_info,
        cion_payload_h file_payload, cion_payload_transfer_status_e status) = 0;

    /// <summary>
    /// This method will be called when the client is connection requested
    /// </summary>
    virtual void OnRequested(std::shared_ptr<ServiceBase> s) = 0;

    /// <summary>
    /// This method will be called when the client is connected
    /// </summary>
    virtual void OnCreate() = 0;

    /// <summary>
    /// This method will be called when the client is disconnected
    /// </summary>
    virtual void OnTerminate() = 0;

    virtual int Run(Foo foo) = 0;
  };

  Runnable();
  ~Runnable();

  /// Listens to client apps
  void Listen(std::shared_ptr<ServiceBase::Factory> service_factory);

  /// Accepts client apps
  void Accept(std::shared_ptr<ServiceBase> service);

  /// Rejects client apps
  void Reject(std::shared_ptr<ServiceBase> service, std::string reason);

  /// Disconnects client apps
  void Disconnect(std::shared_ptr<ServiceBase> service);

  /// Sets the stub display name.
  void SetDisplayName(std::string display_name);

  /// Sets on-demand launch state
  void SetOndemandLaunchEnable(bool enabled);

  /// Gets service objects which are connected
  const std::list<std::shared_ptr<ServiceBase>>& GetServices();
  ...
};
```

**C# for CION (Since Tizen 6.5)**
```csharp
public sealed class Runnable : IDisposable {
  public abstract class ServiceBase { // Abstract class for RPC service
    /// This method will be called when connection requested from the client
    public abstract void OnConnectionRequest();

    /// This method will be called when received file payload.
    public abstract void OnFilePayloadReceived(FilePayload file, PayloadTransferStatus status);

    /// This method will be called when the client is disconnected
    public abstract void OnTerminate();

    /// This method will be called when the client is connected
    public abstract void OnConnected();

    public abstract int Run(Foo foo); // Method to implement
    ...
  };
  public Runnable(string serviceName, string displayName); // Constructor
  public void Listen(Type serviceType); // Method for listening
  public new void Stop() // Stops the listen operation.
  ...
};
```

**C for CION (Since Tizen 6.5)**
```c
// Called when the proxy is connected.
typedef void (*cion_stub_Runnable_connection_result_cb)(const cion_peer_info_h peer_info,
    const cion_connection_result_h result, void *user_data);

// Called when the payload is received.
typedef void (*cion_stub_Runnable_file_received_cb)(const cion_peer_info_h peer_info, const cion_payload_h payload,
    cion_payload_transfer_status_e status, void *user_data);

// Called when the proxy is disconnected.
typedef void (*cion_stub_Runnable_disconnected_cb)(const cion_peer_info_h peer_info, void *user_data);

// Called when a connection is requested.
typedef void (*cion_stub_Runnable_connection_request_cb)(const cion_peer_info_h peer_info, void *user_data);

// Called to get the proxy once for each connected proxy.
typedef bool (*cion_stub_Runnable_peer_info_cb)(const cion_peer_info_h peer_info, void *user_data);

// Called when the request of the proxy is delivered.
typedef int (*cion_stub_Runnable_Run_cb)(cion_stub_Runnable_context_h context, cion_stub_Foo_h foo, void *user_data);


// The structure type containing the set of callback functions for handling stub events.
typedef struct {
  cion_stub_Runnable_connection_result_cb connection_result;/**< This callback function is invoked when the proxy is connected to the stub. */
  cion_stub_Runnable_file_received_cb file_received;/**< This callback function is invoked when the payload is received. */
  cion_stub_Runnable_disconnected_cb disconnected;/**< This callback function is invoked when the proxy is disconnected. */
  cion_stub_Runnable_connection_request_cb connection_request;/**< This callback function is invoked when a connection is requested */
  cion_stub_Runnable_Run_cb Run; /**< This callback function is invoked when the Run request is delivered. */
} cion_stub_Runnable_callback_s;

// Registers the set of the callback functions.
int cion_stub_Runnable_register(const char *service_name, const char *display_name, cion_stub_Runnable_callback_s *callback, void *user_data);

// Unregisters the registered port.
int cion_stub_Runnable_unregister(void);

// Retrieves the connected peer_info handles.
int cion_stub_Runnable_foreach_peer_info(cion_stub_Runnable_peer_info_cb callback, void *user_data);

// Accepts the connection request from a peer.
int cion_stub_MessageStubCCion_Runnable_accept(const cion_peer_info_h peer_info);

// Rejects the connection request from a peer.
int cion_stub_Runnable_reject(const cion_peer_info_h peer_info, const char *reason);

// Sets the stub display name.
int cion_stub_Runnable_set_display_name(const char *display_name);

// Sets on-demand launch state.
int cion_stub_Runnable_set_ondemand_launch_enable(bool enable);
```

**JAVA for CION (Since Tizen 6.5)**
```java

public class Runnable extends ServerBase {
{
    // Abstract class for making a service.
    public abstract class ServiceBase {
      public String getServiceName();
      public String getDisplayName();
      public PeerInfo getClient();
      public void disconnect();
      public void accept();
      public void reject(String reason);
      public abstract void onConnectionRequest();
      public abstract void onFilePayloadReceived(FilePayload file, PayloadTransferStatus status);
      public abstract void onTerminate();
      public abstract void onConnected();
      public abstract int Run(Foo foo);
    }

    @Override
    public final void onPayloadReceived(PeerInfo info, IPayload data, PayloadTransferStatus status) {}

    @Override
    public final byte[] onDataReceived(PeerInfo info, byte[] data) {}

    @Override
    public void onConnectionRequest(PeerInfo peerInfo) {}

    @Override
    public void onDisconnected(PeerInfo peerInfo) {}

    @Override
    public void onConnectionResult(PeerInfo peerInfo, ConnectionResult result) {}

    @Override
    public final void onResultReceived(PayloadAsyncResult payloadAsyncResult) {}

    // Constructor.
    public Runnable(Context context, String serviceName, String displayName) {}

    // Listens for proxy peers.
    public void listen(Class<?> serviceType) {}

    // Stops the listen operation
    @Override
    public void stop() {}

    // Gets service objects which are connected
    public List<ServiceBase> getServices() {}
}
```

## Related Information
- Dependencies
  - Tizen 4.0 and Higher for Mobile
  - Tizen 5.0 and Higher for Wearable
