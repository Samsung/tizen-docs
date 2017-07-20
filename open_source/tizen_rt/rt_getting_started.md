# Tizen RT Getting Started



## Installing the GNU ARM Toolchain

**※ Only the 4.9.2 and 4.9.3 versions are currently supported and tested.**

1. Get the built-in binaries and libraries (`gcc-arm-none-eabi-4_9-2015q3-20150921-linux.tar`) from [https://launchpad.net/gcc-arm-embedded/4.9/4.9-2015-q3-update](https://launchpad.net/gcc-arm-embedded/4.9/4.9-2015-q3-update).
2. Untar the `gcc-arm-none-eabi-4_9-2015q3-20150921-linux.tar` file and export the path:`export PATH=/home/xyz/currentwork/workcommon/toolchain/armgcc492/bin:$PATH`**※ The above command is an example only - do not copy-paste it directly. If you have multiple toolchains, place the new path in front of $PATH.**

In Ubuntu 13.10 and higher, if you cannot execute 32-bit packages, use the following command:

`sudo apt-get install -y lib32z1 lib32ncurses5 lib32bz2-1.0`

## Getting Source Codes from Git

Run the following commands:


The `TINYARA_BASEDIR` environment variable is meant for reference and is used later.

**※ To get the source codes from GitHub, use the following command instead of **`git clone ssh://...`**:**

`$ git clone https://github.com/Samsung/TinyAra.git`

## Building Tizen RT

1. Configure the build from the `$TINYARA_BASEDIR/os/tools` directory:`$ ./configure.sh <board>/<configuration_set>`For list of supported boards and configuration sets, see [Appendix A](https://source.tizen.org/documentation/tizen-rt/tizen-rt-getting-started#Appendix.A).For example: `./configure.sh sidk_s5jt200/hello_with_tash`The command copies the configuration set for the particular board into the `$TINYARA_BASEDIR/os` directory. The configuration can be modified through the `make menuconfig` command from the `$TINYARA_BASEDIR/os` directory.
2. Initiate the build from the `$TINYARA_BASEDIR/os` directory:`$ make`The built binaries are located in the `$TINYARA_BASEDIR/build/output/bin` directory.

## Appendix A

**Board**


**Configuration Sets**

