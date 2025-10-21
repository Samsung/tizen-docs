# Tizen Resource Package

## Overview

Tizen Resource Package (RPK) is a feature that allows packages to share read-only resources with access control and version control. There are two ways to share resources in RPK:

- **Global Share**: Resources are shared with all packages without access control
- **Allowed Share**: Resources are shared with specific packages under access control

To access resources from an RPK, an application needs to declare the `<res-control>` tag in its manifest (tizen-manifest.xml). The resources in the RPK package are mounted in their own resource directory, making them available for use within the application.

### What is Overlayfs?

Overlayfs is a union mount filesystem for Linux that combines multiple directories into a single unified view. For RPK, Overlayfs enables applications to access resources from RPK packages as if they were part of the application's own filesystem.

### Single merged view by Overlayfs
Overlayfs combines multiple layers into a single merged view.

```
Lower Layer 1         Lower Layer 2         Upper Layer              Merge (What app sees)
===============       ===============       ==================       =====================
                      a.txt                 a.txt                    a.txt (From Upper Layer)
b.txt                                                                b.txt (From Lower Layer1)
c.txt                 c.txt                                          c.txt (From Lower Layer2)
```

## Creating RPK Project

Use the Tizen CLI **create** command to create a project.

```bash
tizen create resource-project -t rpk_app -n {project_name} -v {api_version} -- {working_directory}
```

**Parameters:**
- `{project_name}`: Name of your RPK project
- `{api_version}`: Tizen API version (e.g., 6.5)
- `{working_directory}`: Directory where the project will be created

**Example:**
```bash
tizen create resource-project -t rpk_app -n MyResourcePackage -v 6.5 -- /home/user/projects
```

After creating the project, the initial structure will be:
```
.
├── project_def.prop
├── shared
│   └── res
│       └── MyResourcePackage.png
└── tizen-manifest.xml
```

You should create `res/allowed/{res-type}` or `res/global/{res-type}` directories to share resources:
```
.
├── project_def.prop
├── res
│   ├── allowed
│   │   └── tizen.sample.resource
│   │       └── sample_resource
│   └── global
│       └── tizen.sample.resource
│           └── sample_resource
├── shared
│   └── res
│       └── MyResourcePackage.png
└── tizen-manifest.xml
```

## Writing tizen-manifest.xml for RPK
The tizen-manifest.xml file of an RPK has two additional attributes in the `<manifest>` tag

### res-type
Specifies the name of the resource type provided by the RPK. Should match the `{res-type}` portion of the path where resources are installed (`res/global/{res-type}` or `res/allowed/{res-type}`)

### res-version
Specifies the version of the resource package in the format "x.y.z"

### Example of tizen-manifest.xml (RPK)

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<manifest xmlns="http://tizen.org/ns/packages" package="org.example.myrpk" version="1.0.0" res-type="org.example.MyResourcePackage" res-version="1.0.0">
    <label>org.example.myrpk</label>
    <icon>org.example.myrpk</icon>
    <metadata key="testkey" value="testvalue"/>
</manifest>
```

### Global Resources
If you want to share resources as global share, install the resources at `res/global/{res-type}/`. The `{res-type}` indicates the name of the resource type, which could be any string that identifies the type of resources provided by the RPK.

### Allowed Resources
If you want to share resources as allowed share, install the resources at `res/allowed/{res-type}/`. Add the `<allowed-package>` tag to the RPK's tizen-manifest.xml file, with the "id" attribute set to the package ID of the package that you want to grant access to. You can also use a wildcard ('*') to allow access for packages under specific domains.

The `<allowed-package>` tag can have a `<required-privileges>` tag for access control with privileges:

### Example of tizen-manifest.xml (RPK)

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<manifest xmlns="http://tizen.org/ns/packages" package="org.example.myrpk" version="1.0.0" res-type="org.example.MyResourcePackage" res-version="1.0.0">
     <label>org.example.myrpk</label>
     <icon>org.example.myrpk</icon>
     <allowed-package id="org.example.*">
        <required-privileges>
            <privilege>http://tizen.org/privilege/content.read</privilege>
            <privilege>http://tizen.org/privilege/download</privilege>
        </required-privileges>
    </allowed-package>
</manifest>
```

In this example, the allowed package `org.example.*` requires the `http://tizen.org/privilege/content.read` and `http://tizen.org/privilege/download` privileges to access the resources in the RPK.



## Packaging RPK Project

Use the Tizen CLI **package** command to package the project. Since the project contains only resources, it does not require to be built:

```bash
tizen package -t rpk -s {security_profile} -- {working_directory}\{rpk_package_project_name}
```

**Parameters:**
- `{security_profile}`: Security profile (optional, can be omitted to use default)
- `{path}`: Path to the project directory

**Example:**
```bash
tizen package -t rpk -s my-security-profile -- /home/user/projects/MyResourcePackage
```

## Installing RPK Project

Use the Tizen CLI **install** command to install the package on the device:

```bash
tizen install -n {package_name} -- {working_directory}\{rpk_package_project_name}\Package
```

## Writing tizen-manifest.xml to Access Resources of RPK

To access resources of an RPK, declare a `<res-control>` tag in the tizen-manifest.xml file of the package that wants to access the resources.

### Attributes of `<res-control>` tag:

- **resource-type**: Specifies the name of the resource type provided by the RPK
- **min-res-version**: Minimum version of the resource package required (optional)
- **max-res-version**: Maximum version of the resource package required (optional)
- **auto-close**: Whether the application should automatically close when the RPK is updated or uninstalled (optional, default: "false")

### Example of tizen-manifest.xml (TPK)
```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns="http://tizen.org/ns/packages" api-version="6.5" package="org.example.allowed_basic" version="1.0.0">
    <profile name="mobile" />
    <ui-application appid="org.example.allowed_basic" exec="allowed_basic" type="capp" multiple="false" taskmanage="true" nodisplay="false" launch_mode="single">
        <icon>allowed_basic.png</icon>
        <label>allowed_basic</label>
        <res-control resource-type="org.example.MyResourcePackage" min-res-version="1.2.0" max-res-version="2.0.0" auto-close="true"></res-control>
    </ui-application>
</manifest>
```
### Accessing Resources of an RPK

```c
#include <app_common.h>

void get_rpk_resource_path(char *path;) {
    int ret = app_get_res_control_allowed_resource_path("org.example.MyResourcePackage", &path);
    // ...
}
```

## Multiple RPK Packages with Same Resource Type

Multiple RPKs with the same resource type and different resource versions can be installed, but only one RPK is selected. A package that wants to access an RPK can specify `min-res-version` and `max-res-version` to select the appropriate RPK.

### Example Selection Logic

Assume the following RPK packages with the same resource type are installed:
- pkgid: `org.example.rpk1`, res-type: `org.example.MyResourcePackage`, res-version: `1.5.0`
- pkgid: `org.example.rpk2`, res-type: `org.example.MyResourcePackage`, res-version: `2.0.0`
- pkgid: `org.example.rpk3`, res-type: `org.example.MyResourcePackage`, res-version: `3.0.0`

For an application `org.example.app` that declares the following res-controls:
- With `<res-control resource-type="org.example.MyResourcePackage" max-res-version="1.5.0"/>`, `org.example.rpk1` will be selected
- With `<res-control resource-type="org.example.MyResourcePackage" min-res-version="1.5.0" max-res-version="2.5.0"/>`, `org.example.rpk2` will be selected
- With `<res-control resource-type="org.example.MyResourcePackage"/>`, `org.example.rpk3` will be selected (the highest res-version)


## Resource Access Priority for Library Type RPKs

When using library type RPKs, the order of `<res-control>` entries determines the priority. If multiple RPKs provide libraries with the same file name, the RPK referred to by the first `<res-control>` entry has the highest priority, and its version of the file will be mounted and used.

### Example
```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns="http://tizen.org/ns/packages" api-version="7.0" package="org.example.samplerpkconsumer" version="1.0.0">
    <profile name="tizen" />
    <ui-application appid="org.example.samplerpkconsumer" exec="samplerpkconsumer" type="capp" multiple="false" taskmanage="true" nodisplay="false" launch_mode="single">
        <icon>samplerpkconsumer.png</icon>
        <label>samplerpkconsumer</label>
        <res-control resource-type="tizen.sample.rpk1" auto-close="false" />
        <res-control resource-type="tizen.sample.rpk2" auto-close="false" />
        <res-control resource-type="tizen.sample.rpk3" auto-close="false" />
    </ui-application>
</manifest>
```

In this example, if those RPKs contain `libcustom.so`, the file from `tizen.sample.rpk1` will be used, because it is listed first.

## System Requirements

- **Tizen Platform**: Version 6.5 or higher
- **File System**: Overlayfs support
- **Tizen Studio**: 4.5 and Higher


## Related APIs

| API Function | Description |
|--------------|-------------|
| `package_info_get_res_type()` | Retrieves the resource type of an RPK |
| `package_info_get_res_version()` | Retrieves the resource version of an RPK |
| `package_info_foreach_res_allowed_package()` | Iterates through allowed packages of an RPK |
| `package_info_foreach_required_privilege()` | Iterates through required privileges of an allowed package |
| `app_get_res_control_allowed_resource_path()` | Gets the absolute path to the application's resource control directory used to share the allowed resources |
| `app_get_res_control_global_resource_path()` | Gets the absolute path to the application's resource control directory used to share the global resources |


## Related Information

For more information on CLI commands, see [Command Line Interface Commands](../common-tools/command-line-interface.md).

For further details, refer to the official Tizen documentation: [Tizen Resource Package Documentation](https://docs.tizen.org/application/native/guides/app-management/resource-packages/)