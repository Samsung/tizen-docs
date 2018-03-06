# Getting Started with Tizen RT


## Installing the GNU ARM Toolchain

To install the GNU ARM toolchain:

> **Note**
>
> Only the 4.9.2 and 4.9.3 versions are currently supported and tested.

1. Download the built-in binaries and libraries (`gcc-arm-none-eabi-4_9-2015q3-20150921-linux.tar`) from [https://launchpad.net/gcc-arm-embedded/4.9/4.9-2015-q3-update](https://launchpad.net/gcc-arm-embedded/4.9/4.9-2015-q3-update).
2. Untar the `gcc-arm-none-eabi-4_9-2015q3-20150921-linux.tar` file and export to the following path:  
`export PATH=/home/xyz/currentwork/workcommon/toolchain/armgcc492/bin:$PATH`

    > **Note**
    >
	> The above command is an example only - do not copy-paste it directly. If you have multiple toolchains, modify the path appropriately.

    In Ubuntu 13.10 and higher, if you cannot execute 32-bit packages, use the following command:

    ```bash
	sudo apt-get install -y lib32z1 lib32ncurses5 lib32bz2-1.0
	```

## Getting Source Code from Git

To get the source code, run the following commands:

```bash
    $ git clone ssh://<Your ID>@review.tizen.org:29418/rtos/tinyara
    $ cd tinyara
    $ TINYARA_BASEDIR="$PWD"
    $ cd "$TINYARA_BASEDIR"
```
The `TINYARA_BASEDIR` environment variable is meant for reference and is used later.

> **Note**
>
> To get the source code from GitHub, instead of `git clone ssh://...`, use the following command:  
> ```bash
> $ git clone https://github.com/Samsung/TinyAra.git
> ```

## Building Tizen RT
To build Tizen RT:

1. Configure the build from the `$TINYARA_BASEDIR/os/tools` directory:

   ```bash
   $ ./configure.sh <board>/<configuration_set>
   ```

    For example:  

   ```bash
   ./configure.sh sidk_s5jt200/hello_with_tash
   ```

    The command copies the configuration set for the particular board into the `$TINYARA_BASEDIR/os` directory. The configuration can be modified by running the `make menuconfig` command from the `$TINYARA_BASEDIR/os` directory.
1. Initiate the build from the `$TINYARA_BASEDIR/os` directory:

   ```bash
   $ make
   ```

    The built binaries are located in the `$TINYARA_BASEDIR/build/output/bin` directory.

The following boards and configuration sets are supported:

- Boards

  Tizen RT currently supports 1 board, the sidk_s5jt200 (Samsung IoT Development Kit for S5JT200 chipset).  This board is not yet available in public markets. sidk_s5jt200 and other boards for Tizen RT are coming soon.

- Configuration sets

  There are 3 configuration sets for sidk_s5jt200:
  - `tc` for running unit test cases
  - `kernel_sample` for running kernel functions
  - `hello_with_tash` for running a hello example

  You can modify the configuration by using the `menuconfig` tool in the `os` folder, but not all configuration combinations are fully tested yet.

  The IPv4 network stack based on LWIP is included, but Wi-Fi-related code, such as `wpa_supplicant`, is not included. Wi-Fi is to be added in 2017.
