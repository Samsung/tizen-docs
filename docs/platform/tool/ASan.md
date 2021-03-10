Address Sanitizer
=================

Tizen applications are mainly implemented in unmanaged programming
languages (C and C++) which do not provide any protection against
invalid memory accesses. Such accesses often result in memory corruption
and eventually cause program crashes or other abnormal behavior.
AddressSanitizer (or ASan for short) is a part of Google toolsuite for
program quality assurance (the other tools being ThreadSanitizer,
MemorySanitizer and UBSanitizer). The advantages of ASan are

-   much (\~40x) faster than valgrind
-   actively evolving (in contrast to mudflap which has been recently
    removed from GCC)
-   cross-platform (in contrast to Intel MPX)

Current AddressSanitizer handles the following classes of errors (see
<https://github.com/google/sanitizers/wiki/AddressSanitizer>):

-   use after free (dangling pointer dereference)
-   heap buffer overflow
-   stack buffer overflow
-   global buffer overflow
-   stack use after return
-   initialization order bugs
-   memory leaks (on 64-bit systems only)

Quick start
===========

Build your application as usual adding
`--extra-packs asan-force-options` to gbs flags:

`gbs build -A armv7l --include-all --clean --extra-packs asan-force-options`

Usage details
=============

Enabling sanitized build for single package
-------------------------------------------

### Using gbs build

The `gbs` support is already integrated into Tizen toolchain and the
sanitized build can be performed using

`gbs build -A armv7l --include-all --clean --extra-packs asan-force-options`

If you get build time issues refer the [known issues
section](#Known_issues "wikilink").

### Using manual .spec change

If you want to apply the Address Sanitizer to your application you have
to add the following compiler flags to your package:

`CFLAGS+="-fsanitize=address -fsanitize-recover=address -U_FORTIFY_SOURCE -fno-omit-frame-pointer -fno-common"`\
`CXXFLAGS+="-fsanitize=address -fsanitize-recover=address -U_FORTIFY_SOURCE -fno-omit-frame-pointer -fno-common"`\
`LDFLAGS+="-fsanitize=address"`

Their meaning is following:

-   `-fsanitize=address` switches on injection of special code sections
    to your application (the actual sanitization)
-   `-fsanitize-recover=address` allows application to continue
    execution after ASan report is printed (in the other case the
    application will report error and exit)
-   `-fno-omit-frame-pointer` instructs GCC to leave the frame pointer
    information needed for stack trace printing
-   `-U_FORTIFY_SOURCE` disables GCC source fortification, because it
    doesn\'t work well with ASan (see
    <https://github.com/google/sanitizers/issues/247> for details)
-   `-fno-common` forbids merging of variables with equal names from
    different compilation units to increase report accuracy (see
    [corresponding section for details](#-fno-common_issues "wikilink"))

Running sanitized package on target device
------------------------------------------

### Preparing runtime environment

To be able run your sanitized package on target device (e.g. TM1) you
need:

-   upload and install
    [https://build.tizen.org/build/Tizen:Base/arm/armv7l/linaro-gcc/libasan-6.2.1-6.2.armv7l.rpm
    libasan.rpm](https://build.tizen.org/build/Tizen:Base/arm/armv7l/linaro-gcc/libasan-6.2.1-6.2.armv7l.rpm_libasan.rpm "wikilink")
    and
    [https://build.tizen.org/build/Tizen:Base/arm/armv7l/linaro-gcc/asan-runtime-env-6.2.1-6.2.armv7l.rpm
    asan-runtime-env](https://build.tizen.org/build/Tizen:Base/arm/armv7l/linaro-gcc/asan-runtime-env-6.2.1-6.2.armv7l.rpm_asan-runtime-env "wikilink")
    packages to your device.
-   upload your newly built sanitized package to target device and
    install it.
-   sync and reboot your device.

**※** **asan-runtime-env** inserts **libasan.so** to
**/etc/ld.so.preload** and some ASan defects like SEGV are reported
without rebuilding. If you don\'t want to get ASan report from other
processes not yours, you can set **LD\_PRELOAD** instead of
**/etc/ld.so.preload** to detect your process only.

`LD_PRELOAD=/lib/libasan.so [your process]`

### Tuning ASan runtime

ASan run-time can be tuned using special `/ASAN_OPTIONS` file installed
from `asan-runtime-env rpm package`. The contents of the file is a
colon-separated list of options. Description of all existing options can
be found in
[https://github.com/google/sanitizers/wiki/AddressSanitizerFlags\#run-time-flags
official
wiki](https://github.com/google/sanitizers/wiki/AddressSanitizerFlags#run-time-flags_official_wiki "wikilink").
The most common ones are described in the table below. Default set from
`asan-runtime-env` is appropriate for most Tizen developers:

`cat /ASAN_OPTIONS`\
`halt_on_error=false:start_deactivated=true:print_cmdline=true:quarantine_size_mb=1:detect_leaks=0:log_path=/tmp/asan.log:log_exe_name=1`

  Option                 Value                                               Description
  ---------------------- --------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------
  halt\_on\_error        false                                               **true**: print report and exit application if error found. **false** print report and continue execution if error found.
  start\_deactivated     true                                                **true**: reduce ASan memory overhead as much as possible before the instrumented module is loaded into the process.
  print\_cmdline         true                                                Print application command line to ASan report
  quarantine\_size\_mb   1                                                   Size (in Mb) of quarantine used to detect use-after-free errors. Lower value may reduce memory usage but increase the chance of missing error.
  detect\_leaks          true for 64 bit targets, false for 32 bit targets   Switches off LeakSanitizer since there is no armv7l architecture support yet.
  log\_path              /tmp/asan.log                                       Write logs to \"log\_path.pid\". The special values are \"stdout\" and \"stderr\".
  log\_exe\_name         1                                                   Mention name of executable when reporting error and append executable name to logs (as in \"log\_path.exe\_name.pid\").
                                                                             

  : ASan options description

If you want to tune the flags you can rewrite them in the
`/ASAN_OPTIONS` file inside your build-root, or just export
ASAN\_OPTIONS env variable directly.

  Option                       Value    Description
  ---------------------------- -------- -----------------------------------------------------------------------------
  log\_to\_syslog              false    Write all sanitizer output to syslog in addition to other means of logging.
  fast\_unwind\_on\_malloc     true     If available, use the fast frame-pointer-based unwinder on malloc/free.
  malloc\_context\_size        30       Max number of stack frames kept for each allocation/deallocation.
  allocator\_release\_to\_os   false    Experimental. If true, try to periodically release unused memory to the OS.
  heap\_profile                false    Experimental heap profiler, asan-only.
  html\_cov\_report            false    Generate html coverage report.
  sancov\_path                 sancov   Sancov tool location.
                                        

  : Other interesting options

### Getting result

To perform the check you have to execute the compiled application either
on device or in gbs build root under qemu. If your package has unit
tests running them will do as well. If ASan finds the memory issue it
prints report in the following format

`=================================================================`\
`==369==ERROR: AddressSanitizer: stack-buffer-underflow on address 0xbeca8d9f at pc 0xb6f02813 bp 0xbeca8d40 sp 0xbeca8d44`\
`READ of size 1 at 0xbeca8d9f thread T0`\
`   #0 0xb6f02811  (/usr/sbin/sdbd+0x35811)`\
`   #1 0xb6f059cd  (/usr/sbin/sdbd+0x389cd)`\
`   #2 0xb6f079b5 in service_to_fd (/usr/sbin/sdbd+0x3a9b5)`\
`   #3 0xb6efdc2d in create_local_service_socket (/usr/sbin/sdbd+0x30c2d)`\
`   #4 0xb6ee157f in handle_packet (/usr/sbin/sdbd+0x1457f)`\
`   #5 0xb6eed035  (/usr/sbin/sdbd+0x20035)`\
`   #6 0xb6eeafa9 in fdevent_loop (/usr/sbin/sdbd+0x1dfa9)`\
`   #7 0xb6ee5a6d in sdb_main (/usr/sbin/sdbd+0x18a6d)`\
`   #8 0xb665b4bb in __libc_start_main (/lib/libc.so.6+0x164bb)`\
\
`Address 0xbeca8d9f is located in stack of thread T0 at offset 31 in frame`\
`   #0 0xb6f0257f  (/usr/sbin/sdbd+0x3557f)`\
` This frame has 1 object(s):`\
`   [32, 1056) 'buf' <== Memory access at offset 31 underflows this variable`\
`HINT: this may be a false positive if your program uses some custom stack unwind mechanism or swapcontext`\
`     (longjmp and C++ exceptions *are* supported)`\
`SUMMARY: AddressSanitizer: stack-buffer-underflow (/usr/sbin/sdbd+0x35811) `\
`Shadow bytes around the buggy address:`\
`  0x37d95160: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`\
`  0x37d95170: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`\
`  0x37d95180: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`\
`  0x37d95190: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`\
`  0x37d951a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`\
`=>0x37d951b0: f1 f1 f1[f1]00 00 00 00 00 00 00 00 00 00 00 00`\
`  0x37d951c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`\
`  0x37d951d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`\
`  0x37d951e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`\
`  0x37d951f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`\
`  0x37d95200: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`\
`Shadow byte legend (one shadow byte represents 8 application bytes):`\
` Addressable:           00`\
` Partially addressable: 01 02 03 04 05 06 07 `\
` Heap left redzone:       fa`\
` Heap right redzone:      fb`\
` Freed heap region:       fd`\
` Stack left redzone:      f1`\
` Stack mid redzone:       f2`\
` Stack right redzone:     f3`\
` Stack partial redzone:   f4`\
` Stack after return:      f5`\
` Stack use after scope:   f8`\
` Global redzone:          f9`\
` Global init order:       f6`\
` Poisoned by user:        f7`\
` Container overflow:      fc`\
` Array cookie:            ac`\
` Intra object redzone:    bb`\
` ASan internal:           fe`\
` Left alloca redzone:     ca`\
` Right alloca redzone:    cb`\
`Command: /usr/sbin/sdbd`

### Report symbolization

If symbols are not available in sanitized binaries, ASan log will not
include symbol information in backtraces. To fix this run
`asan_symbolize.py` script under collected log files on host where
symbol files are available. The `asan_symbolize.py` script delivered by
**sanitizer-devel.rpm** package, so you\'ll need to install it to your
buildroot:

`gbs build -A armv7l --include-all --clean --extra-packs asan-force-options,sanitizer-devel`

Then, you\'ll need to chroot to your buildroot and **install** newly
built packages:

`sudo chroot ~/GBS-ROOT/local/BUILD-ROOTS/scratch.armv7l.0`\
`rpm -Uihv --force --nodeps home/abuild/rpmbuild/RPMS/armv7l/sdbd*`

Finally, run `asan_symbolize.py` feeding it with ASan log file:

`asan_symbolize.py < asan.log`

`==379==ERROR: AddressSanitizer: stack-buffer-underflow on address 0xbea74c1f at pc 0xb6f00347 bp 0xbea74bb8 sp 0xbea74bbc`\
`READ of size 1 at 0xbea74c1f thread T0`\
`    #0 0xb6f00345 in get_env /usr/src/debug/sdbd-3.0.13/src/services.c:532`\
`    #1 0xb6f02e15 in create_subproc_thread /usr/src/debug/sdbd-3.0.13/src/services.c:584`\
`    #2 0xb6f056c1 in service_to_fd /usr/src/debug/sdbd-3.0.13/src/services.c:1035`\
`    #3 0xb6efb761 in create_local_service_socket /usr/src/debug/sdbd-3.0.13/src/sockets.c:420`\
`    #4 0xb6ede98d in handle_packet /usr/src/debug/sdbd-3.0.13/src/sdb.c:690 (discriminator 4)`\
`    #5 0xb6eeab69 in transport_socket_events /usr/src/debug/sdbd-3.0.13/src/transport.c:208`\
`    #6 0xb6ee8add in fdevent_loop /usr/src/debug/sdbd-3.0.13/src/fdevent.c:697`\
`    #7 0xb6ee3355 in sdb_main /usr/src/debug/sdbd-3.0.13/src/sdb.c:2286`\
`    #8 0xb64964fb in __libc_start_main ??:? (/lib/libc.so.6+0x164fb)`\
\
`Address 0xbea74c1f is located in stack of thread T0 at offset 31 in frame`\
`    #0 0xb6f000b3 in get_env /usr/src/debug/sdbd-3.0.13/src/services.c:517`\
\
`  This frame has 1 object(s):`\
`    [32, 1056) 'buf' <== Memory access at offset 31 underflows this variable`\
`HINT: this may be a false positive if your program uses some custom stack unwind mechanism or swapcontext`\
`      (longjmp and C++ exceptions *are* supported)`\
`SUMMARY: AddressSanitizer: stack-buffer-underflow (/usr/sbin/sdbd+0x36345)`\
`Shadow bytes around the buggy address:`\
`  0x37d4e930: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`\
`  0x37d4e940: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`\
`  0x37d4e950: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`\
`  0x37d4e960: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`\
`  0x37d4e970: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`\
`=>0x37d4e980: f1 f1 f1[f1]00 00 00 00 00 00 00 00 00 00 00 00`\
`  0x37d4e990: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`\
`  0x37d4e9a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`\
`  0x37d4e9b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`\
`  0x37d4e9c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`\
`  0x37d4e9d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00`\
`Shadow byte legend (one shadow byte represents 8 application bytes):`\
`  Addressable:           00`\
`  Partially addressable: 01 02 03 04 05 06 07`\
`  Heap left redzone:       fa`\
`  Heap right redzone:      fb`\
`  Freed heap region:       fd`\
`  Stack left redzone:      f1`\
`  Stack mid redzone:       f2`\
`  Stack right redzone:     f3`\
`  Stack partial redzone:   f4`\
`  Stack after return:      f5`\
`  Stack use after scope:   f8`\
`  Global redzone:          f9`\
`  Global init order:       f6`\
`  Poisoned by user:        f7`\
`  Container overflow:      fc`\
`  Array cookie:            ac`\
`  Intra object redzone:    bb`\
`  ASan internal:           fe`\
`  Left alloca redzone:     ca`\
`  Right alloca redzone:    cb `\
\
`Command: /usr/sbin/sdb`

ASan + LSan
===========

If you are working with 64 bit emulator, you may want to run ASan and
LSan together. Since Tizen LSan is **disabled by default**, you\'ll need
to enable it manually:

-   If you have `/ASAN_OPTIONS` on your emulator (installed by
    **asan-runtime-env** package or created manually), set
    `detect_leaks=1` into this file, like

` halt_on_error=false:start_deactivated=true:print_cmdline=true:quarantine_size_mb=1:detect_leaks=1:log_path=/tmp/asan.log:log_exe_name=1`

-   Otherwise, just do `export ASAN_OPTIONS=detect_leaks=1` on your
    emulator.

ASan + Fuzzing
==============

ASan may be combined with [Fuzz
testing](https://en.wikipedia.org/wiki/Fuzzing) in order to find even
more bugs. See [Fuzzing](https://wiki.tizen.org/Fuzzing) for details
regarding applying fuzz testing for Tizen components.

Known issues
============

Build issues
------------

### "multiple definition of" linking error due to -fno-common

When `–fno-common` flag is added to compiler (which is default in
asan-force-options) some linking may fail with error like this:

`[    4s] Linking C executable system_server`\
`` [    4s] CMakeFiles/system_server.dir/src/core/predefine.c.o: In function `module_exit': ``\
`` [    4s] /home/abuild/rpmbuild/BUILD/system-server-2.0.0/src/core/predefine.c:118: multiple definition of `g_pm_callback' ``\
`[    4s] CMakeFiles/system_server.dir/src/core/device-change-handler.c.o:/home/abuild/rpmbuild/BUILD/system-server-2.0.0/src/core/device-change-handler.c:325: first defined here`

The reason of the bug is that global is defined in more than one
compilation unit without `extern` or `static`.

When using default `–fcommon` option global variables with the same name
are merged into the same variable without signaling errors. When
`-fno-common` option is enabled all global variables are treated
separately as they supposed to be. It means that each global variable
should be defined only once. Otherwise means an error in source code and
is reported at linking stage. It must be fixed by modifying each
declaration as static or merging into an `extern` declaration and a
definition in a single `.c` file.

As a workaround the option may be excluded for sanitization with
expected reduce of global variables sanitization:

`sudo chroot ~/GBS-ROOT/local/BUILD-ROOTS/scratch.armv7l.0`\
`-bash-3.2$ gcc-unforce-options`\
`-bash-3.2$ gcc-force-options -fsanitize=address -fsanitize-recover=address -U_FORTIFY_SOURCE -fno-omit-frame-pointer`\
`-bash-3.2$ exit`

Then rerun gbs build with additional `-–noinit` option:

` $ gbs build -A  armv7l  --include-all  --noinit`

### "undefined reference to" linking error due to ASan reexports some symbols

Some packages fail to link when built with ASan with such kinds of
errors:

`` [  232s] .libs/module_policy_la-module-policy.o: In function `module_policy_LTX_pa__init': ``\
`` [  232s] /home/abuild/rpmbuild/BUILD/pulseaudio-4.0.73+tv/src/modules/module-policy.c:3081: undefined reference to `dlsym' ``\
`` [  232s] /home/abuild/rpmbuild/BUILD/pulseaudio-4.0.73+tv/src/modules/module-policy.c:3082: undefined reference to `dlsym' ``\
`` [  232s] /home/abuild/rpmbuild/BUILD/pulseaudio-4.0.73+tv/src/modules/module-policy.c:3083: undefined reference to `dlsym' ``\
`` [  233s] /home/abuild/rpmbuild/BUILD/pulseaudio-4.0.73+tv/src/modules/module-policy.c:3084: undefined reference to `dlsym' ``\
`` [  233s] /home/abuild/rpmbuild/BUILD/pulseaudio-4.0.73+tv/src/modules/module-policy.c:3085: undefined reference to `dlsym' ``\
`` [  233s] .libs/module_policy_la-module-policy.o:/home/abuild/rpmbuild/BUILD/pulseaudio-4.0.73+tv/src/modules/module-policy.c:3086: more undefined references to `dlsym' follow ``\
`` [  233s] .libs/module_policy_la-module-policy.o: In function `module_policy_LTX_pa__init': ``\
`` [  233s] /home/abuild/rpmbuild/BUILD/pulseaudio-4.0.73+tv/src/modules/module-policy.c:3107: undefined reference to `dlerror' ``\
`[  233s] collect2: error: ld returned 1 exit status`

This happens because **libasan.so** reexports *dlopen* symbol and
configure tests use it to find out if it\'s needed to link against
**libdl.so**. Since **libasan.so** defines *dlopen* symbol and reexports
it, configure doesn\'t add **-ldl** flag to **\$LIBS** variable used by
make utility and we have undefined references. We can overcome this by
linking against **libdl.so** manually, e.g. by adding missed library to
**\$LIBS**:

`export $LIBS=”$LIBS -ldl”`

The same problems may encounter with **libpthread**, **libm** and
**librt** libraries - just add **-pthread**(**-lm**, **-lrt**) flag to
**\$LIBS**:

`export $LIBS=”$LIBS -pthread”`

or

`export $LIBS=”$LIBS -lm”`

or

`export $LIBS=”$LIBS -lrt”`

### Unresolved symbols with underscore

Some applications like **gzip** may check the compiler for generating
symbol names with a certain convention, e.g. external symbols starts
with **\_** sign. But ASan generates special ASan symbols starting with
**\_symbolname** which breaks the build and causes failure at link time.
Example fix can be seen in **gzip** fix
[1](https://review.tizen.org/gerrit/#/c/143815/1)

### "ERROR: AddressSanitizer setrlimit() failed 1" build error due to OSC sets VMA rlimit for 64-bit architectures

This error frequently arises when user tries to build sanitized package
for 64-bit target (e.g. x86\_64 or aarch64). To overcome the issue, one
need to disable ulimit restriction for GBS build. This would require
deleting **ulimit -v \$limit** line from OSC **/usr/lib/build/build**
script (hacky, but works) on Ubuntu systems. For other systems the
method is the same, although path to **build** might be different.

Now, fixed in GCC [2](https://review.tizen.org/gerrit/#/c/146109/)

### \"ASan runtime does not come first in initial library list; you should either link runtime to your application or manually preload it with LD\_PRELOAD\" runtime error

Add **asan-build-env** package to your GBS build command and rebuild
your package:

` gbs build -A armv7l --include-all --clean --extra-packs asan-force-options,asan-build-env`

**NOTE:** **asan-build-env** will add **libasan.so** library in
**/etc/ld.so.preload** file in your newly created buildroot. Thus, if
you want to chroot into this buildroot and do some stuff, you\'ll need
to remove **/etc/ld.so.preload** file manually:

` $ sudo chroot ~/GBS-ROOT/local/BUILD-ROOTS/scratch.armv7l.0`\
` -bash-3.2$ rm -f /etc/ld.so.preload`

### \"relocation R\_X86\_64\_PC32 against symbol \`\_\_asan\_option\_detect\_stack\_use\_after\_return\' can not be used when making a shared object; recompile with -fPIC\"

Sometimes when linking a shared library with ASan you can get a
following error:

``  relocation R_X86_64_PC32 against symbol `__asan_option_detect_stack_use_after_return' can not be used when making a shared object; recompile with -fPIC ``

This happens because you try to link some object file compiled with
**-fPIE** option to your shared library (this is actually wrong). To
overcome the issue, remove **-fPIE** from compilation flags or replace
it with **-fPIC**.

===gcc-real: error: cannot specify -static with -fsanitize=address===
ASan doesn\'t work with static binaries, consider removing **-static**
from you build flags.

### there\'re mounted directories to build root. Please unmount them manually to avoid being deleted unexpectly

/proc mount: Since even init process (systemd in Tizen) is sanitized,
the environment must be prepared ready for the task, so ASan runtime
library libasan.so was patched to check needed mount points, like /proc
and log path and mounts them when needed:

`sudo umount `**`~/GBS-ROOT/local/BUILD-ROOTS/scratch.armv7l.0/proc/`**

Now, fixed in **depanneur**
tool[3](https://review.tizen.org/gerrit/#/c/177437/) applied in
[4](http://download.tizen.org/tools/archive/18.01.4/Ubuntu_16.04/depanneur_0.16.2.tar.gz)

### error: r7 cannot be used in asm here

ASan requires additional register to make instrumentation work. Calls to
\_\_asan\_load() and \_\_asan\_store() require that register and
therefore register pressure is too high:

`set `**`no_sanitize_address`**` for this function`

or

`set `**`%{?asan:--disable-inline-asm}`**` to the .spec`

Runtime issues
--------------

### \"ASan runtime does not come first in initial library list; you should either link runtime to your application or manually preload it with LD\_PRELOAD\" runtime error

-   Short answer: you probably forgot to install
    [https://build.tizen.org/build/Tizen:Base/arm/armv7l/linaro-gcc/asan-runtime-env-6.2.1-6.2.armv7l.rpm
    asan-runtime-env](https://build.tizen.org/build/Tizen:Base/arm/armv7l/linaro-gcc/asan-runtime-env-6.2.1-6.2.armv7l.rpm_asan-runtime-env "wikilink")
    package. Try to install it to your device.
-   Long answer: One of the main requirements for ASan to work correctly
    is that **libasan.so** library should be **the first in ELF symbol
    search lookup order**
    (https://docs.oracle.com/cd/E19683-01/817-3677/auto25/index.html).
    This could be achieved by preloading libasan.so by exporting
    **LD\_PRELOAD=libasan.so** or writing libasan.so to
    **/etc/ld.so.preload** file:

`cat /etc/ld.so.preload`\
`/usr/lib/libasan.so.3.0.0`

The
[https://build.tizen.org/build/Tizen:Base/arm/armv7l/linaro-gcc/asan-runtime-env-6.2.1-6.2.armv7l.rpm
asan-runtime-env](https://build.tizen.org/build/Tizen:Base/arm/armv7l/linaro-gcc/asan-runtime-env-6.2.1-6.2.armv7l.rpm_asan-runtime-env "wikilink")
package should do it for you automatically, but if you already installed
it and the issue still occurs, try add **libasan.so** to
**/etc/ld.so.preload** manually:

`echo '/usr/lib/libasan.so.3.0.0'  > /etc/ld.so.preload`\
`sync`

### \"Your application is linked against incompatible ASan runtimes.\" runtime error

-   Short answer: you probably try to run the application built with
    \"-static-libasan\" option under dynamic libasan.so preloaded.
-   So, for the application built with \"-static-libasan\" option, you
    need to run without libasan.so to avoid conflict.

`sed -e '/libasan.so/d' -i /etc/ld.so.preload`

[Category:Security](Category:Security "wikilink")
