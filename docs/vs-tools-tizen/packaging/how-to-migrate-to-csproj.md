# Migration from a Preview Version Project

To migrate your project:

1. Create a new project in the latest Visual Studio Tools.  
   Select **New Project &gt; Tizen &gt; Xamarin Forms**, **NUI** or **ElmSharp**.
2. Delete all automatically created `.cs` files.
3. Copy all `.cs` files and the `tizen-manifest.xml` file from the old project into the new project.
4. Change the file extension in the Exec field of the `tizen-manifest.xml` file.
5. Determine whether you intend to make Tizen packages:
   - To create Tizen packages, define `<TizenCreateTpkOnBuild>true</TizenCreateTpkOnBuild>` in the `.csproj` file. This is the default value.
   - If you do not intend to make Tizen packages, define `<TizenCreateTpkOnBuild>false</TizenCreateTpkOnBuild>` in the `.csproj` file.
6. Define Nuget libraries:
   1. Go to `Manage Nuget Package` by right-clicking the project and selecting **Manage Nuget Package**.
   2. Include all the Nuget libraries for the dependencies defined in the `project.json` file of the old project.
7. Define project references:
   1. Go to **Project &gt; Dependencies &gt; Add reference**
   2. Include all reference projects defined with `<ProjectReference>` in the `.csproj` file.


## Mapping Between `project.json` and `.csproj`

For a comparison of `project.json` and `csproj` formats, see [A mapping between project.json and csproj properties](https://github.com/dotnet/docs/blob/master/docs/core/tools/project-json-to-csproj.md).


## Tips

The following tips help you to optimize the migration:

- Remove the ` <Compile>,<EmbeddedResource>,<None>` tag.  
  In CPS, Visual Studio can check source code if the source code is included in a solution. For more information, see [Microsoft Reference Site](https://docs.microsoft.com/en-us/dotnet/core/tools/csproj#default-compilation-includes-in-net-core-projects).
- Remove `*.project.json`.  
  CPS no longer uses the `.project.json` file.
- Remove `AssemblyInfo.cs`.  
  This file is now generated automatically.
- Do not use a hint path for dll reference.  
  Use a project reference instead of a hint path. If the solution uses a hint path, the .NET CLI cannot detect it.
    ```xml
    <Reference Include="ResourceBaseComponent, Version=1.0.0.0, Culture=neutral, processorArchitecture=MSIL">
       <SpecificVersion>False</SpecificVersion>
       <HintPath>..\Resources\ResourceBaseComponent\bin\Debug\ResourceBaseComponent.dll</HintPath>
    </Reference>
    ```
    It is recommended that you change to the Project reference type:

    ```xml
    <ProjectReference Include="..\Resources\ResourceBaseComponent\ResourceBaseComponent.csproj" />
    ```
- The final output after the project change is a `.dll` file, and the `.dll` files are packaged in TPK. Therefore, it is necessary to change the Exec field in the manifest file from `xxxx.exe` to `xxxx.dll`.
- Enable generating TPK on build.  
  Set the `TizenCreateTpkOnBuild` value to `true` to enable TPK creation on project build, or to `false` to disable it.
  
  The `tizen-manifest.xml` file must be exist in the project root folder.
    ```xml
    <PropertyGroup>
       <TizenCreateTpkOnBuild>true</TizenCreateTpkOnBuild>
    </PropertyGroup>
    ```
 - Signing TPK packages:
    * For more information on creating TPK packages, see [Creating a TPK Package](how-to-create-tpk.md).
    * Set certificate information in the build property to allow TPK signing.
    * By default, when `VisualStudoToolsForTizen.vsix` is installed, default certificate information is automatically applied. To add it separately:

      ```bash
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

- Customize TPK (exclude the `.dll` file):
  - It is possible to exclude the files included in a TPK file and to change the location of the `.dll` file directory.
  - For more information on customizing TPK contents, see [Customizing TPK Packages](how-to-customize-tpk.md).
  - If you do not want to add the referenced package in a TPK file, use `<PrivateAssets="All">`.

- Portable project debugging:  
  If you cannot hit a breakpoint in a portable project, check the debug type in the `.csproj` file.
  ```
  <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Debug|AnyCPU' ">
     ...
     <DebugType>portable</DebugType>
     ...
  </PropertyGroup>
  ```