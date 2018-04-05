# Getting Started

The Tizen Studio for RT allows you to easily develop and test your RT application:

1. [Install the Tizen Studio for RT](install.md) on your computer.
2. [Manage the project](create.md), including creating a new Tizen Studio for RT project, creating application resources, and building the project.
3. [Flash the project](flash.md) on the board.
4. [Use the serial terminal](terminal.md) to communicate with the board.
5. [Debug the project](debug.md) to avoid runtime problems.


## Prerequisites

Check the following prerequisites before installing the Tizen Studio for RT:

- Java Development Kit (JDK) requirements

  You must install a JDK 8 or 9 to use the Tizen Studio. Do not install OpenJDK.

  To install the appropriate JDK version for your Ubuntu system, go to the Ubuntu Web site and follow the detailed instructions for installing the OracleA&reg; JDK version 8 or 9.


- Operating system and hardware requirements

  The following table lists the supported operating systems and hardware requirements for the Tizen Studio for RT.

  **Table: Operating system and hardware requirements**

 <table>
 <tr>
  <th rowspan="2"> OS </th>
  <th> Versioin </th>
  <td> Ubuntu 16.04 / 14.04 </td>
 </tr>
 <tr>
  <th> Bit </th>
  <td> 64 bit / 32 bit </td>
 </tr>
 <tr>
  <th rowspan="4">  Hardware</th>
  <th> CPU </th>
  <td>  Dual Core, 2 GHz or faster</td>
</tr>
<tr>
  <th> Architecture </th>
  <td> x64</td>
</tr>
<tr>
  <th>  Memory </th>
  <td>  3 GB or more</td>
</tr>
<tr>
  <th>  Disk space</th>
  <td> 6 GB or more</td>
</tr>
</table>


- RT platform requirements

  For the additional requirements and guides related to building and flashing an RT application, see:

  - [Tizen RT Github](https://github.com/Samsung/TizenRT)
  - [Supported boards](https://github.com/Samsung/TizenRT#supported-board--emulator)

- Package requirements for developing applications in Ubuntu

  You must install the webkitgtk package. At the terminal prompt, enter the following command:

  `$ sudo apt-get install libwebkitgtk-1.0-0`


## Related Information
* Dependencies  
  - Ubuntu Only
