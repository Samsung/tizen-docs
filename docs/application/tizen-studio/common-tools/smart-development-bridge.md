# Connecting Devices over Smart Development Bridge

The Smart Development Bridge (SDB) is a command line tool that communicates with a connected target device (it can be an emulator instance or a real Tizen device).

- The SDB manages multiple connections with the target devices. You can list connected devices and send a command to a specific device with a serial number that is created by the SDB.
- The SDB supplies basic commands for application development, such as file transfer, remote shell command, port forwarding for a debugger, viewing, filtering, and controlling target log output.

The SDB is a client-server program that consists of a client, daemon, and server:

- **Client** sends commands to the server. The client runs on your computer. You can invoke the client from a shell by issuing the `sdb` command at the prompt.
- **Daemon** runs commands on the device. The daemon runs as a background process on each target device.
- **Server** manages communication between the client and the daemon. The server runs as a background process on your computer.

You can find the SDB tools in the `$<TIZEN_STUDIO>/tools/` folder.

## Enabling the SDB

The SDB can communicate with a target over a USB or Wi-Fi connection. To use the SDB over USB, open the system settings of the target device, and enable the **USB debugging** mode in **Settings > More system settings > Developer options** (the location can vary depending on the device).

<a name="command"></a>
## Syntax and Commands

Run the SDB with a shell using the following command:

```
> sdb [option] <command> [parameters]
```

You can specify a target of `<command>` by entering the following in the `[option]`:

- `-d`: Sends the `<command>` to a connected device and returns an error if there are other devices.
- `-e`: Sends the `<command>` to a running emulator instance and returns an error if there are other instances.
- `-s <serial number>`: Sends the `<command>` to a target through `<serial number>`.

For more information on commands and parameters, see the following table.

**Table: SDB commands**

| Command                              | Description                              |
|--------------------------------------|------------------------------------------|
| `devices`                            | Lists all connected target instances.    |
| `connect <host>[:<port>]`            | Connects to a target through TCP/IP.     |
| `disconnect <host>[:<port>]`         | Disconnects from a TCP/IP device. <br>By default, the port 26101 is used if there is no specified port number. If you use this command with no additional arguments, all connected TCP/IP devices are disconnected. |
| `push <local> <remote> [-with-utf8]` | Copies a file or directory recursively from the host computer to the target. |
| `pull <remote> [<local>]`            | Copies a file or directory recursively from the target to the host computer. |
| `shell [<command>]`                  | Launches the shell on the target instance if the `<command>` is not specified. If the `<command>` is specified, runs the `<command>` without entering the SDB remote shell on the target instance. |
| `install <pkg-file>`                 | Pushes the `tpk` package file to the device and installs it. |
| `uninstall <pkg-id>`                 | Uninstalls the application from the device by using its `pkg-id`. |
| `forward <local> <remote>`           | Sets up requests' arbitrary port forwarding from the host's local port to the target's remote port. |
| `dlog [option] [<filter>]`           | Monitors the content of the device log buffers. |
| `start-server [--only-detect-tizen]` | Starts the server. <br>If `[--only-detect-tizen]` is specified, the SDB detects only Tizen devices. |
| `kill-server`                        | Stops the running server.                |
| `get-state`                          | Prints the connection status with the target device: `device` or `offline`. |
| `get-serialno`                       | Prints the serial number for connecting the target device. |
| `status-window`                      | Prints the connection status for a specified device continuously. |
| `root <on`&#124;`off>`               | Switches between the root and developer account mode.The `on` value sets the root mode and the `off` value sets the developer account mode. |
| `version`                            | Shows the version number.                |
| `help`                               | Shows the help message.                  |

## Managing Targets

Before issuing SDB commands, it is helpful to know which target instances are connected to the SDB server. In response to the `devices` command option, the SDB prints the serial number (a string created by the SDB to uniquely identify a target instance) and connection status for each connected device. The connection status can be `offline` (the instance is not connected to the SDB or is not responding) or `device` (the instance is connected to the SDB server).

The output format for each instance is the following:

```
[serialNumber]     [state]    [targetName]
```

The following snippet shows an example of the command output:

```
> sdb devices
List of devices attached
emulator-26100    device    myemulator1
emulator-26200    device    myemulator2
```

By specifying the `[serialNumber]` in the command, you can execute SDB commands on a specific target device. If you execute a command without specifying the target instance while multiple devices are available, the SDB generates an error.

## Transferring Files to and from Targets

You can use the `pull` and `push` command options to copy files to and from the target instance. These options let you copy arbitrary directories and files to any location in the target instance, if you have the right permissions:

- To copy a file or directory (and its sub-directories) from the target to the host computer, use the `pull` option:
```
> sdb pull <remote> [<local>]
```
- To copy a file or directory (and its sub-directories) from the host computer to the target, use the `push` option:`
```
> sdb push <local> <remote> [-with-utf8]
```
The `[-with-utf8]` parameter creates the remote file with the UTF-8 character encoding.

In both commands, the `<local>` and `<remote>` parameters refer to the paths to the target files and directory on your computer (local) and on the target instance (remote). For example:

```
> sdb push foo.txt /tmp/foo.txt
```

## Issuing Shell Commands

You can use the `shell` command option to issue target shell commands, with or without entering the SDB remote shell on the target. To issue a single command without entering a remote shell:

```
> sdb shell <shell_command>
```

You can also enter a remote shell on an emulator or device:

```
> sdb shell
```

To exit from the remote shell, press the **Ctrl + D** key or use the `exit` command to end the remote shell.

You can use all shell commands, such as the following, if you have the right permissions:

```
ls, rm, mv, cd, cp, mkdir, touch, echo, tar, grep, cat, chmod, rpm, find, uname, netstat
```

## Installing and Uninstalling Applications

You can use the SDB to install and uninstall the Tizen package file on the target instance:

- The `install` command option pushes the package file to the target and installs it. The `<path_to_tpk>` parameter defines the path to the TPK file. The following command shows an example:
```
> sdb install /home/tizen/ko983dw33q-1.0.0-i386.tpk
```
- The `uninstall` command option kills the application, if running, and removes the package from the target. The `<pkg-id>` is a unique 10-digit identifier for the application. The following command shows an example:
```
> sdb uninstall ko983dw33q
```

## Forwarding Ports

You can set up arbitrary port forwarding of requests from a specific host port to a specific remote port on a target instance.

The format for the `<local>` and `<remote>` parameters is `tcp:<port>`. The following example shows how to forward requests from the host port 26102 to the device port 9999:

```
> sdb forward tcp:26102 tcp:9999
```

After setting up port forwarding, development tools between the device and host can work remotely. For example, GDB (the GNU Project debugger) on a host/gdbserver on a device, and gdbserver on a device opened with the tcp:9999 port:

```
> sdb shell gdbserver:9999 hellotizen
```

GDB in a host connects to localhost:26102:

```
> gdb hellotizen
...
(gdb) target remote localhost:26102
```

## Controlling Device Log Output

You can see the target log messages using the SDB. To see the log output in your computer or from a remote SDB shell, use the `sdb dlog` or `dlogutil` command, respectively:

```
> sdb dlog [option] [<filter>]
```

The following table shows some options for the `sdb dlog` and `dlogutil` commands:

**Table: Log output options**

<table>
	<thead>
		<tr>
			<th>Option</th>
			<th>Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><code>-f &lt;filename&gt;</code></td>
			<td>Writes the log to the <code>&lt;filename&gt;</code> file. The default file is stdout.</td>
		</tr>
		<tr>
			<td><code>-r &lt;Kbytes&gt;</code></td>
			<td>Rotates the log file every <code>&lt;Kbytes&gt;</code> of output. The default value is 16. This option also requires the <code>-f</code> option.</td>
		</tr>
		<tr>
			<td><code>-n &lt;count&gt;</code></td>
			<td>Sets the maximum number of rotated logs to <code>&lt;count&gt;</code>. The default value is 4. This option also requires the <code>-r</code> option.</td>
		</tr>
		<tr>
			<td><code>-v &lt;format&gt;</code></td>
			<td>Sets the output format for log messages.
			<p>You can define which metadata fields are included in log messages by setting one of the following output formats:</p>
			<ul>
				<li><code>brief</code> (default): Displays the priority/tag and PID of the originating process.</li>
				<li><code>process</code>: Displays the PID only.</li>
				<li><code>tag</code>: Displays the priority/tag only.</li>
				<li><code>thread</code>: Displays the <code>process:thread</code> and priority/tag only.</li>
				<li><code>raw</code>: Displays the raw log message, with no other metadata fields.</li>
				<li><code>time</code>: Displays the date, invocation time, priority/tag, and PID of the originating process.</li>
				<li><code>long</code>: Displays all metadata fields and separate messages with a blank line.</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

The `[<filter>]` parameter defines the tag of interest (the system component from which the message originates) and the minimum level of priority to report for that tag. The format is `<tag>:<priority>`, and multiple filters must be separated with a space. The available priorities (from lowest to highest) are **V** (Verbose), **D** (Debug), **I** (Info), **W** (Warning), **E** (Error), and **F** (Fatal).

For example, to view all log messages of the error and fatal priority in addition to the **MyApp** tag messages of the debug priority (and higher), use the following command:

```
> sdb dlog MyApp:D *:E
```

## Related information
* Dependencies
  - Tizen Studio 1.0 and Higher
