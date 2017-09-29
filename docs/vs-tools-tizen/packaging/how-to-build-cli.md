# How to Build a Tizen project in dotnet cli #
This topic provides a step-by-step introduction to building tpk using `Tizen.NET.Sdk` in dotnet cli.
`Tizen.NET.Sdk` provide a feature of tpk packaging and signing.
If Tizen .NET Core project refers to the `Tizen.NET.Sdk` package, TPK file will be created.


### Prerequisites ###
1. Install dotnet core (>=2.0)
    - Install Guide : https://www.microsoft.com/net/core
 
1. Add feed to Nuget.config to restore `Tizen.NET.Sdk`
    - NuGet.Config file location : https://docs.microsoft.com/en-us/nuget/consume-packages/configuring-nuget-behavior#config-file-locations-and-uses
    - Develop channel : https://tizen.myget.org/F/dotnet/api/v3/index.json
    
    ```xml
    <configuration>
      <packageSources>
        <add key="nuget.org" value="https://api.nuget.org/v3/index.json" protocolVersion="3" />
        <add key="TizenMyGET" value="https://tizen.myget.org/F/dotnet/api/v3/index.json" />
      </packageSources>
    </configuration>
    ```

### Create a TPK Package with Dotnet CLI ###

1. Create Console Project 
    ```
    $dotnet new console -n testconsole
    ```

1. Add PackageReference `Tizen.NET.Sdk`
    ```xml
    <ItemGroup>
      <PackageReference Include="Tizen.NET.Sdk" Version="1.0.0-pre1" />
    </ItemGroup>
    ```
    or

    ```
    $dotnet add package Tizen.NET.Sdk --version 1.0.0-pre1 --source https://tizen.myget.org/F/dotnet/api/v3/index.json
    ```

1. Create the `tizen-manifest.xml` file at project root directory
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <manifest xmlns="http://tizen.org/ns/packages" api-version="4" package="org.tizen.example.testconsole" version="1.0.0">
      <profile name="common" />
      <ui-application appid="org.tizen.example.testconsole"
					    exec="testconsole.dll"
					    type="dotnet"
					    multiple="false"
					    taskmanage="true"
					    nodisplay="false"
					    launch_mode="single">
        <label>TestConsol</label>
        <icon>TestConsol.png</icon>
      </ui-application>
    </manifest>
    ```

1. Build Project (with Default Certificates)

    ```
    $ dotnet build
    Microsoft (R) Build Engine version 15.3.409.57025 for .NET Core
    Copyright (C) Microsoft Corporation. All rights reserved.

      testconsole -> /home/tizensdk/develop/testconsole/bin/Debug/netcoreapp2.0/testconsole.dll
      testconsole -> /home/tizensdk/develop/testconsole/bin/Debug/netcoreapp2.0/org.tizen.example.testconsole-1.0.0.tpk

    Build succeeded.
        0 Warning(s)
        0 Error(s)

    Time Elapsed 00:00:02.16

    ```

1. Output Directory 
    ```
    $ tree ./bin

    bin
    └── Debug
        └── netcoreapp2.0
            ├── org.tizen.example.testconsole-1.0.0.tpk
            ├── testconsole.deps.json
            ├── testconsole.dll
            ├── testconsole.pdb
            ├── testconsole.runtimeconfig.dev.json
            ├── testconsole.runtimeconfig.json
            └── tpkroot
                ├── author-signature.xml
                ├── bin
                │   ├── testconsole.dll
                │   └── testconsole.pdb
                ├── lib
                ├── res
                ├── shared
                │   └── res
                ├── signature1.xml
                └── tizen-manifest.xml
    ```

### Signing with custom certificates ###
1. Build Project (with User Certificate Property)
    ```
    $ dotnet clean

    $ dotnet build /p:"AuthorPath=abc.p12;AuthorPass=test" /p:"DistributorPath=def.p12;DistributorPass=hello"
    ```

> INFO : you can also set certificate information .csproj file
>```xml
><PropertyGroup>
>  <AuthorPath>author_test.p12</AuthorPath>
>  <AuthorPass>author_test</AuthorPass>
>  <DistributorPath>tizen-distributor-signer.p12</DistributorPath>
>  <DistributorPass>tizenpkcs12passfordsigner</DistributorPass>
></PropertyGroup>
>```

### See Also ###



