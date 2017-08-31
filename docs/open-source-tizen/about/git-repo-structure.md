# Git Repository Structure

The following is the git repository structure for Tizen 3.0 and higher.

| 1ST DEPTH | 2ND DEPTH  | 3RD DEPTH | DESCRIPTION                              |
| --------- | ---------- | --------- | ---------------------------------------- |
| Platform  |            |           | Platform Component                       |
|           | upstream   |           | Code from upstream open source (Wayland, GStreamer, .NET Engine and etc) |
|           | adaptation |           | Adaptation layer for supporting various kind of devices |
|           | framework  |           | Web Framework etc                        |
|           |            | web       | Web Framework (Web Engine)               |
|           | core       |           | Core Framework                           |
|           |            | api       | Native APIs for Core Framework           |
|           |            | csapi     | Platform-Specific API for Tizen .NET (C#) |
|           |            | webapi    | Web APIs for Web Framework               |
|           | kernel     |           | Kernel for supporting various kind of devices |
| Apps      |            |           | Common Application                       |
|           | native     |           | Common Native Application                |
|           | Web        |           | Common Web Application                   |
| Tools     |            |           | Tools constituting Tizen platform development environment |
|           | Upstream   |           | Code from upstream open source (valgrind, oprofile) |
| Services  |            |           | Services constituting Tizen build services. |
| SDK       |            |           | SDK                                      |
|           | ide        |           | IDE tools which the user can develop Tizen Applications with. |
| SCM       |            |           | Privileges setting & metadata for configuration |
| Test      |            |           | Code for testing a profile (ex Common)   |
|           | tools      |           | Tools for testing a profile              |
| Profile   |            |           | Profile Specific                         |
|           | Mobile     |           | Mobile Profile Specific                  |
|           |            | platform  | Platform Component                       |
|           |            | apps      | Mobile Profile Specific Application      |
|           |            | sdk       | SDK                                      |
|           |            | scm       | Privileges setting & metadata for configuration |
|           |            | test      | Code for testing a profile (ex Common)   |
|           | wearable   |           | Wearable Profile Specific                |
|           |            | platform  | Platform Component                       |
|           |            | apps      | Wearable Profile Specific Application    |
|           |            | sdk       | SDK                                      |
|           |            | scm       | Privileges setting & metadata for configuration |
|           |            | test      | Code for testing a profile (ex Common)   |
|           | common     |           | Common Profile Specific                  |
|           |            | platform  | Platform Component                       |
|           |            | apps      | Common Profile Specific Application      |
|           |            | sdk       | SDK                                      |
|           |            | scm       | Privileges setting & metadata for configuration |
|           |            | test      | Code for testing a profile (ex Common)   |
|           | ivi        |           | ivi specific                             |
|           |            | platform  | Platform Component                       |
|           |            | apps      | Mobile Profile Specific Application      |
|           |            | sdk       | SDK                                      |
|           |            | scm       | Privileges setting & metadata for configuration |
|           |            | test      | Code for testing a profile (ex Common)   |
| Product   |            |           | Product Specific                         |
|           | upstream   |           | Code from upstream open source           |

**Note** Any git repository except above these directories does not belong to Tizen 3.0 and higher.
