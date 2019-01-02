# Limitations of .NET Standard API on Tizen

Applications  on Tizen have limitations compared to .NET desktop applications.  Following are the limitations of .NET Standard API on Tizen:

1. No support for reading data from the standard output stream and standard error stream of an application.

   An application cannot read data from the standard output stream and  standard error stream because they are redirected. So the APIs that read  characters from the stream, returns an empty or null string. For  example, `Process.StandardOutput.ReadToEnd()`.

   In case of `Process.OutputDataReceived` and `Process.ErrorDataReceived`, an event occurs but null is passed as `DataReceivedEventArgs.Data`. Even these event handlers are not called when the stream is closed.

2. No access to process components for other process resources.

   The APIs, which get other process components such as `Process.GetProcesses()` and `Process.GetProcessesByName()`, throw an exception because an application is not allowed to get information about other processes.

   In addition, `Process.GetProcessById()` with other process ID also throws an exception.

3. Limited support for System.IO.MemoryMappedFile.

   Creating MemoryMappedFile with **execute** access capability is not supported. So `MemoryMappedFile.CreateViewAccessor()` and `MemoryMappedFile.CreateViewStream()` with both `MemoryMappedFileAccess.ReadExecute` and `MemoryMappedFileAccess.ReadWriteExecute` throw an exception.

   In addition, `MemoryMappedFile.CreateNew()` and `MemoryMappedFile.OpenExisting()` are not supported because named maps are not supported.

4. No support for System.Net.NetworkInformation.Ping.

   Sending an Internet Control Message Protocol (ICMP) echo message by `System.Net.NetworkInformation.Ping` is not supported.

5. Limited support for system special folders.

   The following system special folders are supported on Tizen:

   - LocalApplicationData
   - MyMusic
   - MyPictures
   - MyVideos

   Your application needs `http://tizen.org/privilege/mediastorage` privilege to access the special folders. Except LocalApplicationData with **read** or **write** access mode.

   In order to get path of the above folders, you need to call `Environment.GetFolderPath()` with `Environment.SpecialFolderOption.DoNotVerify`.

6. Limited support for System.Security.Cryptography.X509Certificates.X509Store.

   Tizen has limitations on X509Store in `StoreLocation.LocalMachine`. For more information on the limitations, see the **Linux** column of [X509Store in Cross-Platform Cryptography](https://github.com/dotnet/corefx/blob/master/Documentation/architecture/cross-platform-cryptography.md#x509store).

   In addition, Tizen does not support X509Store in `StoreLocation.CurrentUser`.
