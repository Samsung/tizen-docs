
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
  -l, --language=LANGUAGE     Select generating language (C, C++, C#).
  -i, --input=INPUT           A tidl interface file.
  -o, --output=OUTPUT         The generated interface file.
  -p, --proxy                 Generate proxy code.
  -s, --stub                  Generate stub code.
  -v, --version               Show version information.

```

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
	void RegisterEvent(OnReceivedEvent cb);
	void UnregisterEvent(OnReceivedEvent cb);
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

	| TIDL type   |Size  |C# type |C++ type  |C type|
	|------------|------|--------|----------|------|
	| void   |0|void |void  |void|void|
	| char|1|byte|char|char|
	| short|2|short|short int|short int|
	| int|4|int |int  |int|
	| long|8|long|long long|long long|
	| float|4|float|float|float|
	| double|8|double|double|double|
	| bundle|variable|Bundle|Bundle|bundle *|
	| string|variable|string|std::string|const char *|
	| bool|1|bool|bool|bool|

 - Container type
	 - **list< [type] >**  or  **array<[type]>**
		- Used when sending list or array of some types
		- Similar to c++ std::list or std::vector
		- Can be nested

	| TIDL type  | C# type| C++ type |C type |
	|--|--|--|--|
	| list<>  | LinkedList<> |std::list<> |Handle (pointer)|
	| array<> | List<>|std::vector<> |Handle (pointer)|

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
		virtual  void OnConnected() = 0;
		virtual  void OnDisconnected() = 0;
		virtual  void OnRejected() = 0;
	};

	Runnable(IEventListener* listener, const std::string& target_appid); // Constructor
	virtual ~Runnable(); // Destructor
	int Connect(); // Method for connecting service app
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
	public  void Connect(); // Method for connecting service app
	public  int Run(Foo foo); //Method  from TIDL
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

### Stub Interface

**TIDL**
```csharp
interface Runnable {
	int Run(Foo foo);
}
```

**C++**
```cpp
class Runnable  {
	class ServiceBase { // Abstract class for RPC service
		class Factory { // Factory class to make real service object
			virtual std::unique_ptr<ServiceBase> CreateService(std::string sender) = 0;
		};

		virtual  void OnCreate() = 0; // Called when service object is created
		virtual  void OnTerminate() = 0; // Called when service object is terminated
		virtual  int Run(Foo foo) = 0; // Method to implement
	};

	Runnable(); // Constructor
	~Runnable(); // Destructor
	void Listen(std::shared_ptr<ServiceBase::Factory> service_factory); // Method for listening
};
```

**C#**
```csharp
public sealed class Runnable : IDisposable {
	public abstract class ServiceBase { // Abstract class for RPC service
		public abstract void OnCreate(); // Called when service object is created
		public abstract void OnTerminate(); // Called when service object is terminated
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

## Related Information
- Dependencies
  - Tizen 4.0 and Higher for Mobile
  - Tizen 5.0 and Higher for Wearable
