# Tizen Resource Package

Tizen Resource Package(RPK) is available from Tizen 6.5 platform onwards, it is a package dedicated to resources only. It is currently supported only in Tizen CLI.

## Creating RPK Project

Use the Tizen CLI **create** command to create a project.
Syntax as below:
```
tizen create resource-project -t rpk_app -n {rpk_package_project_name} -- {working_directory}
```

## Packaging RPK Project

Use the Tizen CLI **package** command to package the project.
Since the project contains only resources hence the project does not require to be built.
Syntax as below:
```
tizen package -t rpk -s {security_profile} -- {working_directory}\{rpk_package_project_name}
```

## Installing RPK Project

Use the Tizen CLI **install** command to install the package on the device.
Syntax as below:
```
 tizen install -n {package_name} -- {working_directory}\{rpk_package_project_name}\Package
```

## Related Information
* Dependencies
  - Tizen Studio 4.5 and Higher
  - Tizen 6.5 and Higher
