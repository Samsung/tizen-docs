# Git Repository Structure

The following table describes the Git repository structure for Tizen 3.0 and higher.

**Table: Git repository structure for Tizen 3.0 and higher**

| First depth | Second depth  | Third depth | Description                              |
| --------- | ---------- | --------- | ---------------------------------------- |
| Platform  |            |           | Platform component                       |
|           | upstream   |           | Code from upstream open source (Wayland, GStreamer, .NET Engine) |
|           | adaptation |           | Adaptation layer for supporting various kind of devices |
|           | framework  |           | Web Framework                            |
|           |            | web       | Web Framework (Web Engine)               |
|           | core       |           | Core Framework                           |
|           |            | api       | Native APIs for Core Framework           |
|           |            | csapi     | TizenFX API for Tizen .NET (C#) |
|           |            | webapi    | Web APIs for Web Framework               |
|           | kernel     |           | Kernel for supporting various kind of devices |
| Apps      |            |           | Common application                       |
|           | native     |           | Common native application                |
|           | Web        |           | Common Web application                   |
| Tools     |            |           | Tools constituting the Tizen platform development environment |
|           | Upstream   |           | Code from upstream open source (valgrind, oprofile) |
| Services  |            |           | Services constituting Tizen build services |
| SDK       |            |           | SDK                                      |
|           | ide        |           | IDE tools with which you can develop Tizen applications |
| SCM       |            |           | Privilege setting and metadata for configuration |
| Test      |            |           | Code for testing a profile (ex Common)   |
|           | tools      |           | Tools for testing a profile              |
| Profile   |            |           | Profile-specific                         |
|           | Mobile     |           | Mobile profile-specific                  |
|           |            | platform  | Platform component                       |
|           |            | apps      | Mobile profile-specific application      |
|           |            | sdk       | SDK                                      |
|           |            | scm       | Privilege setting and metadata for configuration |
|           |            | test      | Code for testing a profile (ex Common)   |
|           | wearable   |           | Wearable profile-specific                |
|           |            | platform  | Platform component                       |
|           |            | apps      | Wearable profile-specific application    |
|           |            | sdk       | SDK                                      |
|           |            | scm       | Privilege setting and metadata for configuration |
|           |            | test      | Code for testing a profile (ex Common)   |
|           | common     |           | Common profile-specific                  |
|           |            | platform  | Platform component                       |
|           |            | apps      | Common profile-specific application      |
|           |            | sdk       | SDK                                      |
|           |            | scm       | Privilege setting and metadata for configuration |
|           |            | test      | Code for testing a profile (ex Common)   |
|           | ivi        |           | IVI profile-specific                             |
|           |            | platform  | Platform component                       |
|           |            | apps      | IVI profile-specific application      |
|           |            | sdk       | SDK                                      |
|           |            | scm       | Privilege setting and metadata for configuration |
|           |            | test      | Code for testing a profile (ex Common)   |
| Product   |            |           | Product-specific                         |
|           | upstream   |           | Code from upstream open source           |

> **Note**
>
> If the Git repository is not listed above, it does not belong to Tizen 3.0 and higher.
