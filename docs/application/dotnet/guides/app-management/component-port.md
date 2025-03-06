# Component Port

Tizen components of the component-based applications can communicate with each other using component ports. Components can send and receive serializable objects through component port communication.

The main feature of the `Tizen.Applications.ComponentBased.ComponentPort` class includes the following:

-   Managing component port

    You can set up the component ports to [send and receive requests](#port) between components of component-based applications with the `Tizen.Applications.ComponentBased.ComponentPort` class.

-   Using component task

    You can set up the component tasks to [run tasks](#task) and wait for events from other components with the `Tizen.Applications.ComponentBased.ComponentTask` class.

## Prerequisites

To enable your component to use the component port functionality, follow these steps:

1.  You need two components to communicate with each other through the component port.
2.  To use the methods and properties of the [Tizen.Applications.ComponentBased.ComponentPort](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ComponentBased.ComponentPort.html) and [Tizen.Applications.ComponentBased.ComponentTask](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ComponentBased.ComponentTask.html) classes, include the [Tizen.Applications.ComponentBased](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ComponentBased.html) namespace in your component:- API Reference
  - [Tizen.Applications.ComponentBased](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ComponentBased) namespace
  - [Tizen.Applications.ComponentBased.ComponentPort](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ComponentBased.ComponentPort) class
  - [Tizen.Applications.ComponentBased.ComponentTask](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ComponentBased.ComponentTask) class

    ```csharp
    using Tizen.Applications.ComponentBased;
    ```

<a name="port"></a>
## Manage component port

To send a request from one component `ClientService.Tizen` to another `ServerService.Tizen` component, use the [Tizen.Applications.ComponentBased.ComponentPort](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ComponentBased.ComponentPort.html) class as follows:

1.  Create a component port instance for sending component `ClientService.Tizen` as follows:

    ```csharp
    namespace ClientService.Tizen
    {
        [Serializable]
        public class Request
        {
            public Request(string command, int sequence, string message)
            {
                Command = command;
                Sequence = sequence;
                Message = message;
            }

            public string Command
            {
                get; set;
            }

            public string Message
            {
                get; set;
            }

            public int Sequence
            {
                get; set;
            }
        }

        [Serializable]
        public class Response
        {
            public Response(string command, int sequence, int result)
            {
                Command = command;
                Sequence = sequence;
                Result = result;
            }

            public string Command
            {
                get; set;
            }

            public int Sequence
            {
                get; set;
            }

            public int Result
            {
                get; set;
            }
        }

        public class ClientService : ServiceComponent
        {
            private static string LogTag = "ClientService";
            private static int _seq = 0;
            private ComponentPort _port;

            public override override OnCreate()
            {
                Log.Info("OnCreate()");
                base.OnCreate();
                _port = new ComponentPort("ClientService");
                return true;
            }

            public override void OnStartCommand(AppControl appControl, bool restarted)
            {
                Log.Info("OnStartCommand()");
                base.OnStartCommand(appControl, restarted);
            }

            public override void OnDestroy()
            {
                Log.Info("OnDestroy()");
                base.OnDestroy();

                if (_port != null)
                {
                    _port.Dispose();
                    _port = null;
                }
            }
        }
    }
    ```

2. Create a component port instance for receiving component `ServerService.Tizen` as follows:

    ```csharp
    namespace ServerService.Tizen
    {
        [Serializable]
        public class Request
        {
            public Request(string command, int sequence, string message)
            {
                Command = command;
                Sequence = sequence;
                Message = message;
            }

            public string Command
            {
                get; set;
            }

            public string Message
            {
                get; set;
            }

            public int Sequence
            {
                get; set;
            }
        }

        [Serializable]
        public class Response
        {
            public Response(string command, int sequence, int result)
            {
                Command = command;
                Sequence = sequence;
                Result = result;
            }

            public string Command
            {
                get; set;
            }

            public int Sequence
            {
                get; set;
            }

            public int Result
            {
                get; set;
            }
        }

        public class ServerService : ServiceComponent
        {
            private static string LogTag = "ServerService";
            private ComponentPort _port;
            private Thread _thread;

            private void OnRequestedReceived(object sender, RequestEventArgs args)
            {
                Log.Info("Sender: " + args.Sender);
                var request = args.Request;
                if (request.GetType() == typeof(Request))
                {
                    var req = (Request)request;
                    Log.Info("Command: " + req.Command);
                    Log.Info("Sequence: " + req.Sequence);
                    Log.Info("Message: " + req.Message);

                    if (args.IsReplyRequested)
                    {
                        args.Reply = new Response(req.Command, req.Sequence, 0);
                    }
                }
            }

            private void OnThread()
            {
                Log.Info("OnTrhead()");
                _port.WaitForEvent();
            }

            public override override OnCreate()
            {
                Log.Info("OnCreate()");
                base.OnCreate();
                _port = new ComponentPort("ServerService");
                _port.RequestReceived += OnRequestReceived;
                _thread = new Thread(new ThreadStart(OnThread));
                _thread.Start();
                return true;
            }

            public override void OnStartCommand(AppControl appControl, bool restarted)
            {
                Log.Info("OnStartCommand()");
                base.OnStartCommand(appControl, restarted);
            }

            public override void OnDestroy()
            {
                Log.Info("OnDestroy()");
                base.OnDestroy();

                if (_port != null)
                {
                    _port.RequestReceived -= OnRequestReceived;
                    _port.Dispose();
                    _port = null;
                }
            }
        }
    }
    ```

3.  Set up the receiving thread of the component by following these steps:

    1. To have the receiving thread of the component wait for incoming requests, call `WaitForEvent()` of the `Tizen.Applications.ComponentBased.ComponentPort` class.
    2. If `WaitForEvent()` is called in the main thread, then `WaitForEvent()` can not be called until the `Cancel()` is called.
    3. `WaitForEvent()` starts the main loop to wait for events from other components. To avoid blocking the main thread, it is recommended to use the `Tizen.Applications.ComponentBased.ComponentTask` class.
    4. To handle the access control, call `AddPrivilege()` of the `Tizen.Applications.ComponentBased.ComponentPort` class. If a client does not have permission, the request is rejected with the permission denied error.
    5. To handle the received request, define and register an event handler for the `RequestReceived` event of the `Tizen.Applications.ComponentBased.ComponentPort` class as follows:

        ```csharp
        {
            _port = new ComponentPort("ServerService");
            _port.RequestReceived += OnRequestReceived;
            _port.AddPrivilege("http://tizen.org/privilege/datasharing");
            _thread = new Thread(new ThreadStart(OnThread));
            _thread.Start();
        }

        private void OnThread()
        {
            Log.Info("OnTrhead()");
            _port.WaitForEvent();
        }

        private void OnRequestedReceived(object sender, RequestEventArgs args)
        {
            Log.Info("Sender: + args.Sender);
            var request = args.Request;
            if (request.GetType() == typeof(Request))
            {
                var req = (Request)request;
                Log.Info("Command: " + req.Command);
                Log.Info("Sequence: " + req.Sequence);
                Log.Info("Message: " + req.Message);

                if (args.IsReplyRequested)
                {
                    args.Reply = new Response(req.Command, req.Sequence, 0);
                }
            }
        }
        ```

4.  Send the request in the sending component as follows:

    1. Call `WaitForEvent()` of the `Tizen.Applications.ComponentBased.ComponentPort` class in the thread, if you want to receive the reply from `ServerService.Tizen`.
    2. Call `WaitForPort`() of the `Tizen.Applications.ComponentBased.ComponentPort` class to wait until the target port is ready.
    3. Use `Send()` of the `Tizen.Applications.ComponentBased.ComponentPort` class to send the request.
    4. Provide the request to be sent as an instance of the `ClientService.Tizen.Request` class as follows:

        ```csharp
        {
            _port = new ComponentPort("ClientService");
            _port.RequestReceived += OnRequestReceived;
            _thread = new Thread(new ThreadStart(OnThread));
            _thread.Start();
            ...
            await ComponentPort.WaitForPort("ServerService");
            try
            {
                var request = new Request("TestCommand", _seq++, "TestMessage");
                _port.Send("ServerService", 5000, request);
            }
            catch
            {
                Log.Error("Failed to send request");
            }
                ...
        }

        private void OnThread()
        {
            Log.Info("OnTrhead()");
            _port.WaitForEvent();
        }

        private void OnRequestedReceived(object sender, RequestEventArgs args)
        {
            Log.Info("Sender: + args.Sender);
            var response = args.Request;
            if (response.GetType() == typeof(Response))
            {
                var req = (Response)request;
                Log.Info("Command: " + req.Command);
                Log.Info("Sequence: " + req.Sequence);
                Log.Info("Result: " + req.Result);
            }
        }
        ```

<a name="task"></a>
## Use component task

Using [Tizen.Applications.ComponentBased.ComponentTask](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ComponentBased.ComponentTask.html) class, a component can run a task to wait for events from other components properly.

1. Create a component task instance for receiving component `ServerService.Tizen` as follows:
    ```csharp
    namespace ServerService.Tizen
    {
        [Serializable]
        public class Request
        {
            public Request(string command, int sequence, string message)
            {
                Command = command;
                Sequence = sequence;
                Message = message;
            }

            public string Command
            {
                get; set;
            }

            public string Message
            {
                get; set;
            }

            public int Sequence
            {
                get; set;
            }
        }

        [Serializable]
        public class Response
        {
            public Response(string command, int sequence, int result)
            {
                Command = command;
                Sequence = sequence;
                Result = result;
            }

            public string Command
            {
                get; set;
            }

            public int Sequence
            {
                get; set;
            }

            public int Result
            {
                get; set;
            }
        }

        public class ServerService : ServiceComponent
        {
            private static string LogTag = "ServerService";
            private ComponentPort _port;
            private ComponentTask _task;

            private void OnRequestedReceived(object sender, RequestEventArgs args)
            {
                Log.Info("Sender: + args.Sender);
                var request = args.Request;
                if (request.GetType() == typeof(Request))
                {
                    var req = (Request)request;
                    Log.Info("Command: " + req.Command);
                    Log.Info("Sequence: " + req.Sequence);
                    Log.Info("Message: " + req.Message);

                    if (args.IsReplyRequested)
                    {
                        args.Reply = new Response(req.Command, req.Sequence, 0);
                    }
                }
            }

            public override override OnCreate()
            {
                Log.Info("OnCreate()");
                base.OnCreate();
                _port = new ComponentPort("ServerService");
                _port.RequestReceived += OnRequestReceived;
                _task = new ComponentTask(_port);
                _task.Start();
                return true;
            }

            public override void OnStartCommand(AppControl appControl, bool restarted)
            {
                Log.Info("OnStartCommand()");
                base.OnStartCommand(appControl, restarted);
            }

            public override void OnDestroy()
            {
                Log.Info("OnDestroy()");
                base.OnDestroy();

                if (_task != null)
                {
                    _task.Stop();
                    _task = null;
                }

                if (_port != null)
                {
                    _port.RequestReceived -= OnRequestReceived;
                    _port.Dispose();
                    _port = null;
                }
            }
        }
    }
    ```

2. To run the task, call the `Start` method of the `Tizen.Applications.ComponentBased.ComponentTask` class as follows:

    ```csharp
    _port = new ComponentPort("ServerService");
    _port.RequestReceived += OnRequestReceived;
    _task = new ComponentTask(_port);
    _task.Start();
    ```

## Related information
- Dependencies
  -   Tizen 6.5 and Higher
- API Reference
  - [Tizen.Applications.ComponentBased](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ComponentBased) namespace
  - [Tizen.Applications.ComponentBased.ComponentPort](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ComponentBased.ComponentPort) class
  - [Tizen.Applications.ComponentBased.ComponentTask](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ComponentBased.ComponentTask) class
