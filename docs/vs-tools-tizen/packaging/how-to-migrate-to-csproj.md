## Migration from a project from Preview version ##

### 1. Create new project in latest VS Tools ###
   * New Project → Tizen → Xamarin Forms, NUI or ElmSharp

### 2. Delete ```*.cs``` files which were created automatically

### 3. Copy all ```.cs``` files and ```tizen-manifest.file``` from old project to new project

### 4. Change file extension in Exec field of ```tizen-manifest.file```

### 5. Define whether you will make Tizen package or not
   * Make Tizen package (Default) : Define ```<TizenCreateTpkOnBuild>true</TizenCreateTpkOnBuild>``` in ```.csproj```
   * NOT need Tizen package : Define ```<TizenCreateTpkOnBuild>false</TizenCreateTpkOnBuild>``` in ```.csproj```

### 6. Define Nuget libraries
   * Go to ```Manage Nuget Package``` (Project → Press right mouse button → Manage Nuget Package)
   * Include all Nuget libraries all dependencies defined in ```project.json``` of old project

### 7. Define Project Reference
   * Go to ```Project → Dependencies → Add reference```
   * Include all reference projects defined with ```<ProjectReference>``` in ```.csproj```

---

### Mapping Table between ```project.json``` and ```.csproj``` ###
* See [A mapping between project.json and csproj properties of Tizen.NET projects](https://github.com/dotnet/docs/blob/master/docs/core/tools/project-json-to-csproj.md) for a comparison of project.json and csproj formats.


### Tips ###
* Remove ``` <Compile>,<EmbeddedResource>,<None> ```tag : In CPS, Visual Studio can check source code if the source codes are included in solution.
   * [Microsoft Reference Site](https://docs.microsoft.com/en-us/dotnet/core/tools/csproj#default-compilation-includes-in-net-core-projects)
* Remove *.project.json : CPS cannot use .project.json any more.
* Remove AssemblyInfo.cs : It will be generate automatically 
* Don't use hint path for dll reference : Should use project reference. If the solution use hint path, dotnet CLI cannot detect it.
    ```xml
        <Reference Include="ResourceBaseComponent, Version=1.0.0.0, Culture=neutral, processorArchitecture=MSIL">
          <SpecificVersion>False</SpecificVersion>
          <HintPath>..\Resources\ResourceBaseComponent\bin\Debug\ResourceBaseComponent.dll</HintPath>
        </Reference>
    ```
    It is recommended that you change to the Project reference type as shown below.

    ```xml
        <ProjectReference Include="..\Resources\ResourceBaseComponent\ResourceBaseComponent.csproj" />
    ```
* The final output after the project change is a dll file, and the dll files are packaged in tpk. Therefore, it is necessary to change the Exec from the manifest file to xxxx.exe -> xxxx.dll.
* Enable generating TPK on Build
    * Set the TizenCreateTpkOnBuild value to `true` for tpk creation in Build Project. `False` if you do not want to
    * tizen-manifest.xml file should be exist on project root.
    ```xml
      <PropertyGroup>
        <TizenCreateTpkOnBuild>true</TizenCreateTpkOnBuild>
      </PropertyGroup>
    ```
    
* Signing TPK
    * [How to Create tpk](how-to-create-tpk.md)
    * Set certificates information into the build property allows tpk signing.
    * By default, when VisualStudoToolsForTizen.vsix is ​​installed, default certificate information is automatically applied. Here's how to add it separately:

    ```
    dotnet build /p:"AuthorPath=abc.p12;AuthorPass=test" /p:"DistributorPath=def.p12;DistributorPass=hello"
    ```
    or
    ```xml
    <PropertyGroup>
     <TizenCreateTpkOnBuild>true</TizenCreateTpkOnBuild>
     <AuthorPath>author_test.p12</AuthorPath>
     <AuthorPass>author_test</AuthorPass>
     <DistributorPath>tizen-distributor-signer.p12</DistributorPath>
     <DistributorPass>tizenpkcs12passfordsigner</DistributorPass>
    </PropertyGroup>
    ```

* Customize TPK (Exclude dll)
    * It is possible to exclude the files included in tpk and to change the location of the dll file directory.
    * [How to customize tpk](how-to-customize-tpk.md)
    * If you don't want to add the referenced package in tpk, you can use ```<PrivateAssets="All">```

* Portable Project Debugging
    * If you cannot hit a breakpoint in Portable project, check the debug type in ```.csproj```
    ```
    <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Debug|AnyCPU' ">
    ...
    <DebugType>portable</DebugType>
    ...
    </PropertyGroup>
    ```