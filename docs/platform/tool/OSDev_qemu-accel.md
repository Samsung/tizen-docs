qemu-accel
----------

`qemu-accel` is a build-acceleration system used in Tizen.

Reason
------

Tizen is built for many platforms, including non-x86 `armv7l` and
`aarch64` ones, but still OBS servers and most of developers\'
workstations and `x86_64`, so appropriate `qemu-user` is used to execute
binaries in buildroots.

But running all the build under `qemu-user` is not reasonable since
it\'s an interpreter and gives huge performance overhead. To reduce the
overhead the cross-compiler and build tools are used.

Implementation
--------------

The straightforward solution to implement this approach is to replace
native binaries in buildroot with `x86_64` cross-tools, this approach
has been used in early versions of Tizen (lots of `*-x86-arm` packages),
but it causes a mix of libraries in buildroot, requires lots of efforts
for maintenance and improvement.

Existing `qemu-accel` approach is based on Linux Kernel Support for
miscellaneous Binary Formats
[1](https://www.kernel.org/doc/html/latest/admin-guide/binfmt-misc.html):
the cross-toolchain, tools, and libraries they depend on, are placed
into special `/emul` directory and patched using `patchelf` tool to
support new location, and additional wrapper tool is registered as a
binary format interpreter for Tizen architectures.

The entry point is an interpreter binary named `qemu-binfmt`, which
checks if there is a replacement for executed binary tool in `/emul` and
runs it instead of native tool in that case.

If you have any issues with acceleration system you can just remove the
`/emul` directory from buildroot and all the tools will be executed in
native mode.

### Sample workflow

Suppose user runs compiler binary:

`/home/abuild $ /usr/bin/gcc test.c`

Kernel checks what the `/usr/bin/gcc` is, founds that it\'s an `armv7l`
binary and looks though the registered interpreters. Since
`qemu-arm-binfmt` is registered as interpreter, the following command is
executed:

`/usr/bin/qemu-arm-binfmt /usr/bin/gcc test.c`

The interpreter checks `/emul` and founds that there is
`/emul/usr/bin/gcc` there, so command evaluates to

`/emul/usr/bin/gcc test.c`

Now suppose the binary executed is not supported by `qemu-accel`:

`/home/abuild $ ./configure . . .`\
`/home/abuild $ # Script compiles and runs test`\
`/home/abuild $ gcc conftest.c -o conftest && ./conftest`

The `qemu-arm-binfmt` can\'t find the `conftest` binary in `/emul`
therefore it evaluates into

`/usr/bin/qemu-arm /home/abuild/conftest`

and the binary is executed in interpreted mode.

### Supported tools

List of accelerated binaries can be found in `qemu-accel` git at
review.tizen.org
[2](https://review.tizen.org/gerrit/gitweb?p=platform/upstream/qemu-accel.git;a=blob;f=packaging/qemu-accel.spec.in;hb=refs/heads/tizen_base#l126)

Currently the whole toolchain is accelerated, most of `coreutils` (ls,
mv, cat, and so on), tools which are widely used in build (compressors,
script interpreters) and package management tools (rpm with
dependencies).

Clang and Python acceleration are supported as well, but placed in
separate packages (`clang-accel` and `python-accel` respectively) to
reduce size of `qemu-accel` which is installed into every buildroot. If
your application uses `clang` compiler or runs heavy scripts in python
(some build systems, like gyp and SCons, use it), you might consider
adding corresponding section to your `.spec`:

`# Accelerate python`\
`%ifarch armv7l`\
`BuildRequires: python-accel-armv7l-cross-arm`\
`%endif # arm7l`\
`%ifarch aarch64`\
`BuildRequires: python-accel-aarch64-cross-aarch64`\
`%endif # aarch64`

for python, or

`# Accelerate clang`\
`%ifarch armv7l`\
`BuildRequires: clang-accel-armv7l-cross-arm`\
`%endif # arm7l`\
`%ifarch aarch64`\
`BuildRequires: clang-accel-aarch64-cross-aarch64`\
`%endif # aarch64`

for Clang compiler.

Troubleshooting
---------------

Unfortunately, some OSes use binary format interpreters for own purposes
which leads to interpreters registered by default which conflict with
Tizen `qemu-binfmt` and lead to errors.

*Example error 1*:

`[ 131s] configure: error: C compiler cannot create executables`\
`[ 451s] /usr/lib/gcc/armv7l-tizen-linux-gnueabi/6.2.1/../../../../armv7l-tizen-linux-gnueabi/bin/ld:`\
`[ 451s] /usr/lib/gcc/armv7l-tizen-linux-gnueabi/6.2.1/liblto_plugin.so: error`\
`[ 451s] loading plugin:`\
`[ 451s] /usr/lib/gcc/armv7l-tizen-linux-gnueabi/6.2.1/liblto_plugin.so: wrong ELF`\
`[ 451s] class: ELFCLASS64`

*Example error 2*: \[ 149s\] meson.build:1:0: ERROR: Unable to determine
dynamic linker.

*Root cause*: `qemu-arm` was registered by OS instead of `qemu-binfmt`,
the native `armv7l` binary of GCC has been executed, but found the LTO
plugin prepared for `x86_64` compiler and failed.

*Solution*: switch a default handlers off.

### Switching off default binfmt\_misc handlers

#### For newbie

Just reboot, If you are a newbie on Ubuntu distribution If you reboot
your Ubuntu machine, This issue will be automatically fixed because the
/proc/sys/fs/binfmt\_misc/\* files are re-initialized whenever rebooting
the Ubuntu machine.

#### For developers

**Method 1:** If you are using Ubuntu 18.04, Please run the below
statements.

`sudo /usr/sbin/update-binfmts --disable`\
`sudo systemctl disable binfmt-support.service`

**Method 2:** Or, you can fix the issue by manipulating the
**/proc/sys/fs/binfmt\_misc/qemu-arm** manually.

Currently registered handlers can be seen using the following command:

`ls /proc/sys/fs/binfmt_misc/`

the right output should only show 5 files:

`arch64 arm armeb register status`

If your output shows more than it, you have to unregister the wrong
handlers by echoing value -1 to the control files.

For example, The below command unregisters the `qemu-arm` interpreter.

`/home/user $ echo -1 | sudo tee /proc/sys/fs/binfmt_misc/qemu-arm `

**Method 3:** Let\'s remove all bin-fmt files. Since the below statement
removes all files, the GBS command sets up an interpreter again while
establishing a build stage with QEMU.

`find /proc/sys/fs/binfmt_misc/ -not -name status -not -name register -type f -exec sh -c "echo -1 | sudo tee {}" \;`

And, In case that you build multiple packages all together, you need to
specify \"-name qemu-\*\"

`find /proc/sys/fs/binfmt_misc/ -name qemu-* -type f -exec sh -c "echo -1 | sudo tee {}" \;`

[Category:Platform](Category:Platform "wikilink")
