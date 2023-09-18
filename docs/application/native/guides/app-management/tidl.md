
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

## Protocol version 2 (Since Tizen 8.0)
To use protocol version 2, you must fill **'protocol 2'** in the .tidl file.
The following features are supported in protocol version 2:
  > [!Note]
  > **TIDLC** will support protocol version 2 since Tizen 8.0

### Enum type
 - **'enum'** type is added.
 - You can declare an **enum** type inside a 'struct' or 'interface' and use it as a member variable or parameter:
   ```tidl
    struct Message {
      enum Type {
        T1 = 0,
        T2,
        T3
      }

      Type t;
      int id;
      string str;
    }

    interface Hello {
      enum Version {
        V1,
        V2,
        V3
      }

      string SayHello(Version ver, string str, Message.Type msg);
    }

- When using a struct's enum type as a method parameter, it must be specified as **"<struct_name>.<enum_type>"**.

### Import another TIDL file
- **'import'** keyword is added.
- You can add and use other TIDL files in the same directory as the current TIDL file using the **'import'** keyword.
- During the compilation process, the contents of other TIDL files are integrated and generated as one code.
- The following example shows how to use the **'import'** keyword:
  ```tidl
    import <another.tidl>

    interface Message {
      int Send(string name, string msg);
    }
  ```

### Method privilege
- The protocol version 2 of TIDL supports the method privilege feature.
- You can set privileges for each method of an interface by writing them as below:
  ```tidl
    interface PackageManager {
      [privilege = "http://tizen.org/privilege/packagemanager.info"]
      int GetPackages(out list<string> packages);

      [privilege = "http://tizen.org/privilege/packagemanager.admin"]
      int Install(file path);

      [privilege = "http://tizen.org/privilege/packagemanager.admin"]
      int Uninstall(string package);
    }
  ```
- To use the GetPackages method in the example, the client application needs to have the privilege that is "[http://tizen.org/privilege/packagemanager.info](http://tizen.org/privilege/packagemanager.info){:target="_blank"}".

### Map and set container type
- You can use map and set container types in TIDL.
- The map type is **'map\<K, V\>'**. The set type is **'set\<K\>'**:
  ```tidl
    struct Message {
      string name;
      map<string, string> envelope;
      set<string> keys;
    }
  ```
  > **Note**
  >
  > The key type of map and set container must be TIDL's built-in types.

### Marshalling type info
- From protocol version 2, the type of information and variable names of method parameters are also transmitted.
- Even if variable names are changed, added, or deleted due to interface modifications, it does not affect communication.
- If there are no variables to be passed, they are passed as initial values.
  - **Example 1:** Original TIDL code:

    ```tidl
      interface Hello {
        int GetPackages(out list<string> packages);
      }
    ```
  - **Example 2:** Revised TIDL code:
    ```tidl
      interface Hello {
        int GetPackages(out list<string> packages, out int size);
      }
    ``````
- In the above example, the `GetPackages()` method has a size parameter added.
- Even if the stub only returns the existing packages parameter, there is no problem with communication.

### Struct inheritance
- **'struct'** inheritance is supported.
- Here is an example that supports **'struct'** inheritance where **MessageDerived** inherits **MessageBase**:
  ```tidl
    struct MessageBase {
      int id;
      string name;
    }

    struct MessageDerived : MessageBase {
      string msg;
    }
  ```
  > [!Note]
  > The inherited struct must not have elements of the base struct.

- If the method of the interface is a base struct, communication can be performed using the derived struct that is inherited: (Polymorphism)
  ```tidl
    struct MessageBase {
      int id;
      string name;
    }

    struct MessageDerived : MessageBase {
      string msg;
    }

    struct Envelope : MessageBase {
      string address;
      string msg;
    }

    interface Message {
      int SendMessage(MessageBase msg);
    }
  ```
- When using the **Message** interface, you can use **Envelope** or **MessageDerived** to call the **`SendMessage()`** method.

### Remote exception
- The stub can use **RemoteException** to throw an exception to the proxy.
- This feature is available when the method operates synchronously.
- When the proxy sends a request and awaits a response, any exception thrown by the stub is forwarded to the proxy.

### Local execution mode
- If the stub that the proxy sends a request to is in the same application, a function call occurs instead of RPC.

### Private sharing
- Since protocol version 2, the **file** keyword can be used without the '-b' option.
- The proxy or the stub can use this to share a specific file in the data directory with the intended recipient for communication.
- The recipient who receives the shared file can access it with read-only permission.

### TIDL generated code for protocol version 2

**TIDL**
```tidl
protocol 2

struct MessageBase {
  int id;
  string name;
  string msg;
}

struct MessageDerived : MessageBase {
  string address;
}

interface Message {
  void OnReceived(string sender, MessageBase message) delegate;

  int Register(string sender, OnReceived callback);
  void Unregister() async;
  int Send(MessageBase message);
}
```
- In the example above, the **MessageDerived** structure inherits from **MessageBase**.
- When calling the Send method of the Message interface, you can use a MessageDerived instance.

#### Proxy interface

**C**
```c
// Handle for 'MessageBase' structure.
typedef void *rpc_port_proxy_MessageBase_h;

// Handle for 'MessageDerived' structure.
typedef void *rpc_port_proxy_MessageDerived_h;

// Handle for Remote Exception.
typedef struct rpc_port_proxy_remote_exception_s *rpc_port_proxy_remote_exception_h;

// Handle for 'Message' interface.
typedef struct rpc_port_proxy_Message_s *rpc_port_proxy_Message_h;

// Handle for 'OnReceived' delegate of 'Message' interface.
typedef struct rpc_port_proxy_Message_OnReceived_s *rpc_port_proxy_Message_OnReceived_h;

// Function for creating MessageBase handle.
int rpc_port_proxy_MessageBase_create(rpc_port_proxy_MessageBase_h *h);

// Function for destroying MessageBase handle.
int rpc_port_proxy_MessageBase_destroy(rpc_port_proxy_MessageBase_h h);

// Function for cloning MessageBase handle.
int rpc_port_proxy_MessageBase_clone(rpc_port_proxy_MessageBase_h h, rpc_port_proxy_MessageBase_h *clone);

// Function for setting id to MessageBase handle.
int rpc_port_proxy_MessageBase_set_id(rpc_port_proxy_MessageBase_h h, int value);

// Function for getting id from MessageBase handle.
int rpc_port_proxy_MessageBase_get_id(rpc_port_proxy_MessageBase_h h, int *value);

// Function for setting name to MessageBase handle.
int rpc_port_proxy_MessageBase_set_name(rpc_port_proxy_MessageBase_h h, const char *value);

// Function for getting name from MessageBase handle.
int rpc_port_proxy_MessageBase_get_name(rpc_port_proxy_MessageBase_h h, char **value);

// Function for setting msg to MessageBase handle.
int rpc_port_proxy_MessageBase_set_msg(rpc_port_proxy_MessageBase_h h, const char *value);

// Function for getting msg from MessageBase handle.
int rpc_port_proxy_MessageBase_get_msg(rpc_port_proxy_MessageBase_h h, char **value);

// Function for creating MessageDerived handle.
int rpc_port_proxy_MessageDerived_create(rpc_port_proxy_MessageDerived_h *h);

// Function for destroying MessageDerived handle.
int rpc_port_proxy_MessageDerived_destroy(rpc_port_proxy_MessageDerived_h h);

// Function for cloning MessageDerived handle.
int rpc_port_proxy_MessageDerived_clone(rpc_port_proxy_MessageDerived_h h, rpc_port_proxy_MessageDerived_h *clone);

// Function for setting id to MessageDerived handle.
int rpc_port_proxy_MessageDerived_set_id(rpc_port_proxy_MessageDerived_h h, int value);

// Function for getting id from MessageDerived handle.
int rpc_port_proxy_MessageDerived_get_id(rpc_port_proxy_MessageDerived_h h, int *value);

// Function for setting id to MessageDerived handle.
int rpc_port_proxy_MessageDerived_set_name(rpc_port_proxy_MessageDerived_h h, const char *value);

// Function for getting name from MessageDerived handle.
int rpc_port_proxy_MessageDerived_get_name(rpc_port_proxy_MessageDerived_h h, char **value);

// Function for setting msg to MessageDerived handle.
int rpc_port_proxy_MessageDerived_set_msg(rpc_port_proxy_MessageDerived_h h, const char *value);

// Function for getting msg from MessageDerived handle.
int rpc_port_proxy_MessageDerived_get_msg(rpc_port_proxy_MessageDerived_h h, char **value);

// Function for setting address to MessageDerived handle.
int rpc_port_proxy_MessageDerived_set_address(rpc_port_proxy_MessageDerived_h h, const char *value);

// Function for getting address from MessageDerived handle.
int rpc_port_proxy_MessageDerived_get_address(rpc_port_proxy_MessageDerived_h h, char **value);

// Function for creating Remote Exception handle.
int rpc_port_proxy_remote_exception_create(rpc_port_proxy_remote_exception_h *h);

// Function for setting cause to Remote Exception handle.
int rpc_port_proxy_remote_exception_set_cause(rpc_port_proxy_remote_exception_h h, int cause);

// Function for setting msessage to Remote Exception handle.
int rpc_port_proxy_remote_exception_set_message(rpc_port_proxy_remote_exception_h h, const char *message);

// Function for getting cause from Remote Exception handle.
int rpc_port_proxy_remote_exception_get_cause(rpc_port_proxy_remote_exception_h h, int *cause);

// Function for getting message from Remote Exception handle.
int rpc_port_proxy_remote_exception_get_message(rpc_port_proxy_remote_exception_h, char **message);

// Function for destroying Remote Exception handle.
int rpc_port_proxy_remote_exception_destroy(rpc_port_proxy_remote_exception_h h);

// Function for getting Remote Exception handle.
int rpc_port_proxy_get_remote_exception(rpc_port_proxy_remote_exception_h *h);

// Callback function for OnReceived of Message interface.
typedef void (*rpc_port_proxy_Message_OnReceived_cb)(void *user_data, const char *sender, rpc_port_proxy_MessageBase_h message);

// Function for creating OnReceived handle.
int rpc_port_proxy_Message_OnReceived_create(rpc_port_proxy_Message_OnReceived_h *h);

// Function for destroying OnReceived handle.
int rpc_port_proxy_Message_OnReceived_destroy(rpc_port_proxy_Message_OnReceived_h h);

// Function for cloning OnReceived handle.
int rpc_port_proxy_Message_OnReceived_clone(rpc_port_proxy_Message_OnReceived_h h, rpc_port_proxy_Message_OnReceived_h *clone);

// Function for setting callback to OnReceived handle.
int rpc_port_proxy_Message_OnReceived_set_callback(rpc_port_proxy_Message_OnReceived_h h, rpc_port_proxy_Message_OnReceived_cb callback, void *user_data);

// Function for setting once flag to OnReceived handle.
int rpc_port_proxy_Message_OnReceived_set_once(rpc_port_proxy_Message_OnReceived_h h, bool once);

// Function for getting id from OnReceived handle.
int rpc_port_proxy_Message_OnReceived_get_id(rpc_port_proxy_Message_OnReceived_h h, int *id);

// Function for getting seq_id from OnReceived handle.
int rpc_port_proxy_Message_OnReceived_get_seq_id(rpc_port_proxy_Message_OnReceived_h h, int *seq_id);

// Function for checking once flag from OnReceived handle.
int rpc_port_proxy_Message_OnReceived_is_once(rpc_port_proxy_Message_OnReceived_h h, bool *once);

// Function for getting tag from OnReceived handle.
int rpc_port_proxy_Message_OnReceived_get_tag(rpc_port_proxy_Message_OnReceived_h h, char **tag);

// Function for dispoing OnReceived handle.
int rpc_port_proxy_Message_OnReceived_dispose(rpc_port_proxy_Message_h proxy, rpc_port_proxy_Message_OnReceived_h h);

// Called when receiving connected event.
typedef void (*rpc_port_proxy_Message_connected_cb)(rpc_port_proxy_Message_h h, void *user_data);

// Called when receiving disconnected event.
typedef void (*rpc_port_proxy_Message_disconnected_cb)(rpc_port_proxy_Message_h h, void *user_data);

// Called when receiving rejected event.
typedef void (*rpc_port_proxy_Message_rejected_cb)(rpc_port_proxy_Message_h h, void *user_data);

// Structure for receiving events of Message interface.
typedef struct {
        rpc_port_proxy_Message_connected_cb connected;
        rpc_port_proxy_Message_disconnected_cb disconnected;
        rpc_port_proxy_Message_rejected_cb rejected;
} rpc_port_proxy_Message_callback_s;

// Function for creating Message handle.
int rpc_port_proxy_Message_create(const char *stub_appid, rpc_port_proxy_Message_callback_s *callback, void *user_data, rpc_port_proxy_Message_h *h);

// Function for destroying Message handle.
int rpc_port_proxy_Message_destroy(rpc_port_proxy_Message_h h);

// Function for connecting to Message server.
int rpc_port_proxy_Message_connect(rpc_port_proxy_Message_h h);

// Function for connecting to Message server synchronously.
int rpc_port_proxy_Message_connect_sync(rpc_port_proxy_Message_h h);

// Function for disconnecting from Message server.
int rpc_port_proxy_Message_disconnect(rpc_port_proxy_Message_h h);

// Function for Register method of Message interface.
int rpc_port_proxy_Message_invoke_Register(rpc_port_proxy_Message_h h, const char *sender, rpc_port_proxy_Message_OnReceived_h callback);

// Function for Unregister method of Message interface.
void rpc_port_proxy_Message_invoke_Unregister(rpc_port_proxy_Message_h h);

// Function for Send method of Message interface.
int rpc_port_proxy_Message_invoke_Send(rpc_port_proxy_Message_h h, rpc_port_proxy_MessageBase_h message);
```

**C++**
```cpp
// Class for Bundle.
class Bundle final {
 public:
  Bundle();
  explicit Bundle(bundle* handle, bool copy = true, bool own = true);
  Bundle(std::string raw);
  ~Bundle();

  Bundle(const Bundle& b);
  Bundle& operator = (const Bundle& b);
  Bundle(Bundle&& b) noexcept;
  Bundle& operator = (Bundle&&) noexcept;

  bundle* GetHandle() const;
  bundle* Detach();
};

// class for File.
class File final {
 public:
  File(std::string filename = "");

  const std::string& GetFileName() const;
  int Share(rpc_port_h port);
};

// class for 'MessageBase' structure.
class MessageBase {
 public:
  MessageBase();
  MessageBase(int id, std::string name, std::string msg);

  int Getid() const;
  void Setid(int id);

  const std::string& Getname() const;
  void Setname(std::string name);

  const std::string& Getmsg() const;
  void Setmsg(std::string msg);
};

// class for 'MessageDerived' structure.
class MessageDerived : public MessageBase {
 public:
  MessageDerived();
  MessageDerived(int id, std::string name, std::string msg, std::string address);

  const std::string& Getaddress() const;
  void Setaddress(std::string address);
};

namespace proxy {
class Exception {};
class NotConnectedSocketException : public Exception {};
class InvalidProtocolException : public Exception {};
class InvalidIOException : public Exception {};
class PermissionDeniedException : public Exception {};
class InvalidIDException : public Exception {};
class InvalidArgumentException : public Exception {};
class OutOfMemoryException : public Exception {};

// class for RemoteException.
class RemoteException : public Exception {
 public:
  RemoteException();
  RemoteException(std::string message);
  RemoteException(int cause, std::string message);

  int GetCause() const;
  const std::string& GetMessage() const;
};

// class for 'Message' interface.
class Message : public LocalExecution::IEvent {
 public:

  class CallbackBase {
   public:
    CallbackBase() = default;
    CallbackBase(int delegate_id, bool once);
    virtual ~CallbackBase() = default;

    virtual void OnReceivedEvent(const UnitMap& unit_map);
    int GetId() const;
    void SetId(int id);
    int GetSeqId() const;
    void SetSeqId(int seq_id);
    bool IsOnce() const;
    void SetOnce(bool once);
    std::string GetTag() const;
  };

  class OnReceived : public CallbackBase {
   public:
    OnReceived(bool once = false);
    virtual void OnReceived(std::string sender, MessageBase message);
  };

  class IEventListener {
   public:
    virtual ~IEventListener() = 0;
    // Called when connected event is delivered.
    virtual void OnConnected() = 0;

    // Called when disconnected event is delivered.
    virtual void OnDisconnected() = 0;

    // Called when rejected event is delivered.
    virtual void OnRejected() = 0;
  };

  // Constructor.
  Message(IEventListener* listener, std::string target_appid);

  // Desctructor.
  virtual ~Message();

  // Method for connecting to 'Message' server.
  void Connect(bool sync = false);

  // Method for disconnecting from 'Message' server.
  void Disconnect();

  // Method for disposing delegate from Message intstance.
  void DisposeCallback(const std::string& tag);

  // Method for 'Register' method of 'Message' interface.
  int Register(std::string sender, std::unique_ptr<OnReceived> callback);

  // Method for 'Unregister' method of 'Message' interface.
  void Unregister();

  // Method for 'Send' method of 'Message' interface.
  int Send(MessageBase message);
};
}  // namespace proxy
```

**C#**
```csharp
// class for 'MessageBase' structure.
public class MessageBase
{
  public int id;
  public string name;
  public string msg;

  public MessageBase();
}

// class for 'MessageDerived' structure.
public class MessageDerived : MessageBase
{
  public string address;

  public MessageDerived();
}

// class for RemoteException.
public class RemoteException : Exception
{
  public RemoteException();
  public RemoteException(string message);
  public RemoteException(string message, int cause);
  public new string Message;
  public int Cause;
}

namespace Proxy
{
  // class for 'Message' interface.
  public class Message : ProxyBase
  {
    public event EventHandler Connected;
    public event EventHandler Disconnected;
    public event EventHandler Rejected;

    public class CallbackBase
    {
      public string Tag;
      public CallbackBase(int delegateId, bool once)
    }

    public sealed class OnReceived : CallbackBase
    {
      public OnReceived(bool once = false) : base((int)DelegateId.OnReceived, once);
      public delegate void Callback(string sender, MessageBase message);
      public event Callback Received;
    }

  // Called when connected event is delivered.
  protected override void OnConnectedEvent(string endPoint, string portName, Port port);

  // Called when disconnected event is delivered.
  protected override void OnDisconnectedEvent(string endPoint, string portName);

  // Called when rejected event is delivered.
  protected override void OnRejectedEvent(string endPoint, string portName);

  // Called when received event is delivered.
  protected override void OnReceivedEvent(string endPoint, string portName);

  // Constructor.
  public Message(string appId);

  // Method for connecting to 'Message' server.
  public void Connect();

  // Method for disconnecting from 'Message' server.
  public void Disconnect();

  // Method for connecting to 'Message' server sychronously.
  public void ConnectSync();

  // Method for disposing delegate from Message instance.
  void DisposeCallback(string tag);

  // Method for 'Register' method of 'Message' interface.
  public int Register(string sender, OnReceived callback);

  // Method for 'Unregister' method of 'Message' interface.
  public void Unregister();

  // Method for 'Send' method of 'Message' interface.
  public int Send(MessageBase message);
  }
}
```


<a name="stub-interface-1"></a>
#### Stub interface

**C**
```c
// Handle for 'MessageBase' structure.
typedef void *rpc_port_stub_MessageBase_h;

// Handle for 'MessageDerived' structure.
typedef void *rpc_port_stub_MessageDerived_h;

// Handle for Remote Exception.
typedef struct rpc_port_stub_remote_exception_s *rpc_port_stub_remote_exception_h;

// Handle for context of 'Message' interface.
typedef struct rpc_port_stub_Message_context_s *rpc_port_stub_Message_context_h;

// Handle for 'OnReceived' delegate of 'Message' interface.
typedef struct rpc_port_stub_Message_OnReceived_s *rpc_port_stub_Message_OnReceived_h;

// Function for creating MessageBase handle.
int rpc_port_stub_MessageBase_create(rpc_port_stub_MessageBase_h *h);

// Function for destroying MessageBase handle.
int rpc_port_stub_MessageBase_destroy(rpc_port_stub_MessageBase_h h);

// Function for cloning MessageBase handle.
int rpc_port_stub_MessageBase_clone(rpc_port_stub_MessageBase_h h, rpc_port_stub_MessageBase_h *clone);

// Function for setting id to MessageBase handle.
int rpc_port_stub_MessageBase_set_id(rpc_port_stub_MessageBase_h h, int value);

// Function for getting id from MessageBase handle.
int rpc_port_stub_MessageBase_get_id(rpc_port_stub_MessageBase_h h, int *value);

// Function for setting name to MessageBase handle.
int rpc_port_stub_MessageBase_set_name(rpc_port_stub_MessageBase_h h, const char *value);

// Function for getting name from MessageBase handle.
int rpc_port_stub_MessageBase_get_name(rpc_port_stub_MessageBase_h h, char **value);

// Function for setting msg to MessageBase handle.
int rpc_port_stub_MessageBase_set_msg(rpc_port_stub_MessageBase_h h, const char *value);

// Function for getting msg to MessageBase handle.
int rpc_port_stub_MessageBase_get_msg(rpc_port_stub_MessageBase_h h, char **value);

// Function for creating MessageDerived handle.
int rpc_port_stub_MessageDerived_create(rpc_port_stub_MessageDerived_h *h);

// Function for destroying MessageDerived handle.
int rpc_port_stub_MessageDerived_destroy(rpc_port_stub_MessageDerived_h h);

// Function for cloning MessageDerived handle.
int rpc_port_stub_MessageDerived_clone(rpc_port_stub_MessageDerived_h h, rpc_port_stub_MessageDerived_h *clone);

// Function for setting id to MessageDerived handle.
int rpc_port_stub_MessageDerived_set_id(rpc_port_stub_MessageDerived_h h, int value);

// Function for getting id from MessageDerived handle.
int rpc_port_stub_MessageDerived_get_id(rpc_port_stub_MessageDerived_h h, int *value);

// Function for setting name to MessageDerived handle.
int rpc_port_stub_MessageDerived_set_name(rpc_port_stub_MessageDerived_h h, const char *value);

// Function for getting name from MessageDerived handle.
int rpc_port_stub_MessageDerived_get_name(rpc_port_stub_MessageDerived_h h, char **value);

// Function for setting msg to MessageDerived handle.
int rpc_port_stub_MessageDerived_set_msg(rpc_port_stub_MessageDerived_h h, const char *value);

// Function for getting msg to MessageDerived handle.
int rpc_port_stub_MessageDerived_get_msg(rpc_port_stub_MessageDerived_h h, char **value);

// Function for setting address to MessageDerived handle.
int rpc_port_stub_MessageDerived_set_address(rpc_port_stub_MessageDerived_h h, const char *value);

// Function for getting address from MessageDerived handle.
int rpc_port_stub_MessageDerived_get_address(rpc_port_stub_MessageDerived_h h, char **value);

// Function for creating Remote Exception handle.
int rpc_port_stub_remote_exception_create(rpc_port_stub_remote_exception_h *h);

// Function for setting cause to Remote Exception handle.
int rpc_port_stub_remote_exception_set_cause(rpc_port_stub_remote_exception_h h, int cause);

// Function for setting message to Remote Exception handle.
int rpc_port_stub_remote_exception_set_message(rpc_port_stub_remote_exception_h h, const char *message);

// Function for getting cause from Remote Exception handle.
int rpc_port_stub_remote_exception_get_cause(rpc_port_stub_remote_exception_h h, int *cause);

// Function for getting message from Remote Exception handle.
int rpc_port_stub_remote_exception_get_message(rpc_port_stub_remote_exception_h, char **message);

// Function for destroying Remote Exception handle.
int rpc_port_stub_remote_exception_destroy(rpc_port_stub_remote_exception_h h);

// Function for throwing Remote Exception handle.
int rpc_port_stub_remote_exception_throw(rpc_port_stub_remote_exception_h h);

// Called when client is connected.
typedef void (*rpc_port_stub_Message_create_cb)(rpc_port_stub_Message_context_h context, void *user_data);

// Called when client is disconnected.
typedef void (*rpc_port_stub_Message_terminate_cb)(rpc_port_stub_Message_context_h context, void *user_data);

// Called when retreiving contexts of Message handle.
typedef bool (*rpc_port_stub_Message_context_cb)(rpc_port_stub_Message_context_h context, void *user_data);

// Called when receiving 'Register' event from client.
typedef int  (*rpc_port_stub_Message_Register_cb)(rpc_port_stub_Message_context_h context, const char *sender, rpc_port_stub_Message_OnReceived_h callback, void *user_data);

// Called when receiving 'Unregister' event from client.
typedef void  (*rpc_port_stub_Message_Unregister_cb)(rpc_port_stub_Message_context_h context, void *user_data);

// Called when receiving 'Send' event from client.
typedef int  (*rpc_port_stub_Message_Send_cb)(rpc_port_stub_Message_context_h context, rpc_port_stub_MessageBase_h message, void *user_data);

// Function for setting tag to Message context handle.
int rpc_port_stub_Message_context_set_tag(rpc_port_stub_Message_context_h context, void *tag);

// Function for getting tag from Message context handle.
int rpc_port_stub_Message_context_get_tag(rpc_port_stub_Message_context_h context, void **tag);

// Function for getting sender from Message context handle.
int rpc_port_stub_Message_context_get_sender(rpc_port_stub_Message_context_h context, char **sender);

// Function for getting instance from Message context handle.
int rpc_port_stub_Message_context_get_instance(rpc_port_stub_Message_context_h context, char **instance);

// Function for disconnecting from client.
int rpc_port_stub_Message_context_disconnect(rpc_port_stub_Message_context_h context);

// Function for creating OnReceived handle.
int rpc_port_stub_Message_OnReceived_create(rpc_port_stub_Message_OnReceived_h *h);

// Function for destroying OnReceived handle.
int rpc_port_stub_Message_OnReceived_destroy(rpc_port_stub_Message_OnReceived_h h);

// Function for cloning OnReceived handle.
int rpc_port_stub_Message_OnReceived_clone(rpc_port_stub_Message_OnReceived_h h, rpc_port_stub_Message_OnReceived_h *clone);

// Function for getting id from OnReceived handle.
int rpc_port_stub_Message_OnReceived_get_id(rpc_port_stub_Message_OnReceived_h h, int *id);

// Function for getting seq_id from OnReceived handle.
int rpc_port_stub_Message_OnReceived_get_seq_id(rpc_port_stub_Message_OnReceived_h h, int *seq_id);

// Function for checking once flag from OnReceived handle.
int rpc_port_stub_Message_OnReceived_is_once(rpc_port_stub_Message_OnReceived_h h, bool *once);

// Function for getting tag from OnReceived handle.
int rpc_port_stub_Message_OnReceived_get_tag(rpc_port_stub_Message_OnReceived_h h, char **tag);

// Function for invoking OnReceived callback function of 'Message' client.
int rpc_port_stub_Message_OnReceived_invoke(rpc_port_stub_Message_OnReceived_h h, const char *sender, rpc_port_stub_MessageBase_h message);

// Structure for receiving events of Message interface.
typedef struct {
        rpc_port_stub_Message_create_cb create;
        rpc_port_stub_Message_terminate_cb terminate;
        rpc_port_stub_Message_Register_cb Register;
        rpc_port_stub_Message_Unregister_cb Unregister;
        rpc_port_stub_Message_Send_cb Send;
} rpc_port_stub_Message_callback_s;

// Function for registering callback functions of Message interface to be invoked when events are received.
int rpc_port_stub_Message_register(rpc_port_stub_Message_callback_s *callback, void *user_data);

// Function for unregistering callback functions of Message interface.
int rpc_port_stub_Message_unregister(void);

// Function for retreving connected context of clients of Message interface.
int rpc_port_stub_Message_foreach_context(rpc_port_stub_Message_context_cb callback, void *user_data);

// Function for getting client number from Message interface.
int rpc_port_stub_Message_get_client_number(unsigned int *client_number);
```

**C++**
```cpp
// class for Bundle.
class Bundle final {
 public:
  Bundle();
  explicit Bundle(bundle* handle, bool copy = true, bool own = true);
  Bundle(std::string raw);
  ~Bundle();

  Bundle(const Bundle& b);
  Bundle& operator = (const Bundle& b);
  Bundle(Bundle&& b) noexcept;
  Bundle& operator = (Bundle&&) noexcept;

  bundle* GetHandle() const;
  bundle* Detach();
};


// class for File.
class File final {
 public:
  File(std::string filename = "");

  const std::string& GetFileName() const;
  int Share(rpc_port_h port);
};

// class for 'MessageBase' structure.
class MessageBase {
 public:
  MessageBase();
  MessageBase(int id, std::string name, std::string msg);

  int Getid() const;
  void Setid(int id);
  const std::string& Getname() const;
  void Setname(std::string name);
  const std::string& Getmsg() const;
  void Setmsg(std::string msg);
};

// class for 'MessageDerived' structure.
class MessageDerived : public MessageBase {
 public:
  MessageDerived();
  MessageDerived(int id, std::string name, std::string msg, std::string address);

  const std::string& Getaddress() const;
  void Setaddress(std::string address);
};

namespace stub {

class Exception {};
class NotConnectedSocketException : public Exception {};
class InvalidProtocolException : public Exception {};
class InvalidIOException : public Exception {};
class PermissionDeniedException : public Exception {};
class InvalidIDException : public Exception {};
class InvalidArgumentException : public Exception {};
class OutOfMemoryException : public Exception {};

// class for Remote Exception.
class RemoteException : public Exception {
 public:
  RemoteException();
  RemoteException(std::string message);
  RemoteException(int cause, std::string message);

  int GetCause() const;
  const std::string& GetMessage() const;
};

// class for 'Message' interface.
class Message : public LocalExecution::IEvent {
 public:
  class ServiceBase;
  class CallbackBase {
   public:
    CallbackBase(int delegate_id, bool once);
    CallbackBase() = default;
    virtual ~CallbackBase() = default;

    int GetId() const;
    void SetId(int id);
    int GetSeqId() const;
    void SetSeqId(int seq_id);
    bool IsOnce() const;
    void SetOnce(bool once);

    std::string GetTag() const;

    void SetContext(void* context);
    void* GetContext() const;
  };

  class OnReceived : public CallbackBase {
   public:
    OnReceived(rpc_port_h callback_port, std::weak_ptr<ServiceBase> service) : CallbackBase(static_cast<int>(DelegateId::OnReceived), false), callback_port_(callback_port), service_(std::move(service)) {}

    void Invoke(std::string sender, MessageBase message);
  };

  class ServiceBase : public std::enable_shared_from_this<ServiceBase> {
   public:
    class Factory {
     public:
      virtual ~Factory() = default;
      virtual std::unique_ptr<ServiceBase> CreateService(std::string sender, std::string instance) = 0;
    };

    virtual ~ServiceBase() = default;
    const std::string& GetSender() const {
      return sender_;
    }
    const std::string& GetInstance() const {
      return instance_;
    }

    void SetPort(rpc_port_h port);
    void Disconnect();
    virtual void OnCreate() = 0;
    virtual void OnTerminate() = 0;
    void SetContext(void* context);
    void* GetContext() const;
    void Dispatch(rpc_port_h port, rpc_port_h callback_port, rpc_port_parcel_h parcel, std::shared_ptr<ServiceBase> service);
    void Dispatch(rpc_port_h port, rpc_port_h callback_port, rpc_port_parcel_h parcel);

    virtual int Register(std::string sender, std::unique_ptr<OnReceived> callback) = 0;
    virtual void Unregister() = 0;
    virtual int Send(MessageBase message) = 0;

   protected:
    ServiceBase(std::string sender, std::string instance);
  };

  // Constructor.
  Message();

  // Destructor.
  ~Message();

  // Method for listening Message events.
  void Listen(std::shared_ptr<ServiceBase::Factory> service_factory);

  // Method for getting instance of ServiceBase of clients.
  const std::list<std::shared_ptr<ServiceBase>>& GetServices() const {
    return services_;
  }
};

}  // namespace stub
```

**C#**
```csharp
// class for 'MessageBase' structure.
public class MessageBase
{
  public int id;
  public string name;
  public string msg;

  public MessageBase();
}

// class for 'MessageDerived' structure.
public class MessageDerived : MessageBase
{
  public string address;

  public MessageDerived();
}

// class for Remote Exception.
public class RemoteException : Exception
{
  public RemoteException();
  public RemoteException(string message);
  public RemoteException(string message, int cause);
  public new string Message;
  public int Cause;
}

namespace Stub
{
  public sealed class Message : StubBase
  {
    public abstract class ServiceBase
    {
      public string Sender;
      public string Instance;
      public Port Port;
      protected ServiceBase();
      public void Disconnect();
      public abstract void OnCreate();
      public abstract void OnTerminate();
      public abstract int Register(string sender, OnReceived callback);
      public abstract void Unregister();
      public abstract int Send(MessageBase message);
    }

    public class CallbackBase
    {
      public string Tag;
      public CallbackBase(int delegateId, bool once);
    }

    public sealed class OnReceived : CallbackBase
    {
      public void Invoke(string sender, MessageBase message);
    }

    // Called when client sends a request.
    protected override bool OnReceivedEvent(string sender, string instance, Port port);

    // Called when client is connected.
    protected override void OnConnectedEvent(string sender, string instance);

    // Called when client is disconnected.
    protected override void OnDisconnectedEvent(string sender, string instance);

    // Constructor.
    public Message();

    // Method for listening events of Message interface.
    public void Listen(Type serviceType);

    // Method for getting instance of connected clients.
    public IEnumerable<ServiceBase> GetServices();

    ...
  }
}
```

## Related Information
- Dependencies
  - Tizen 4.0 and Higher for Mobile
  - Tizen 5.0 and Higher for Wearable
