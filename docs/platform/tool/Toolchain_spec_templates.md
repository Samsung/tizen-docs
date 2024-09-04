[Back to Porting Tizen](https://wiki.tizen.org/wiki/MIPS)

### qemu-accel

` %define gcc_version         483`\
` %define gcc_suffix          4.8.3`\
` %define CROSS_COMPILER_PATH /opt/toolchains/gcc-%{gcc_suffix}`\
` %define tizen_arch          your_new_arch`\
` %define libc                your_libc`\
` # spec file for package qemu-accel-%{tizen_arch}`\
` #`\
` # Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.`\
` #`\
` # All modifications and additions to the file contributed by third parties`\
` # remain the property of their copyright owners, unless otherwise agreed`\
` # upon. The license for this file, and modifications and additions to the`\
` # file, is the same license as for the pristine package itself (unless the`\
` # license for the pristine package is not an Open Source License, in which`\
` # case the license is the MIT License). An "Open Source License" is a`\
` # license that conforms to the Open Source Definition (Version 1.9)`\
` # published by the Open Source Initiative.`\
` # Please submit bugfixes or comments via `[`http://bugs.opensuse.org/`](http://bugs.opensuse.org/)\
` # Choose which gcc hijack method (if any) to use.`\
` # Only select one of the two at a time!`\
` %define hijack_gcc         1`\
` %if 0%{?_with_perl_and_python_emul}`\
` Name:             qemu-accel-%{tizen_arch}-cross`\
` %else`\
` Name:             qemu-accel-%{tizen_arch}`\
` %endif`\
` Version:          0.4`\
` Release:          0`\
` AutoReqProv:      off`\
` BuildRequires:    gcc-%{libc}`\
` BuildRequires:    fdupes`\
` BuildRequires:    glibc-locale`\
` BuildRequires:    gcc-c++`\
` BuildRequires:    gettext-runtime`\
` BuildRequires:    gettext-tools`\
` BuildRequires:    m4`\
` BuildRequires:    gawk`\
` BuildRequires:    flex`\
` BuildRequires:    cmake`\
` %if 0%{?_with_perl_and_python_emul}`\
` BuildRequires:    perl`\
` BuildRequires:    python`\
` %endif`\
` # required for xxd`\
` BuildRequires:    vim`\
` BuildRequires:    patchelf`\
` #BuildRequires:    rpmlint-mini`\
` BuildRequires:    qemu-linux-user`\
` Requires:         coreutils`\
` Summary:          Native binaries for speeding up cross compile`\
` License:          GPL-2.0`\
` Group:            Development/Libraries/Cross`\
` ExclusiveArch:    %ix86`\
` # default path in qemu`\
` %define HOST_ARCH %(echo %{_host_cpu} | sed -e "s/i.86/i586/;s/ppc/powerpc/;s/sparc64.*/sparc64/;s/sparcv.*/sparc/;")`\
` %define our_path /emul/%{HOST_ARCH}-for-%{tizen_arch}`\
` %define %{tizen_arch}_cross_env gcc-%{gcc_suffix}`\
` %description`\
` This package is used in %{tizen_arch} architecture builds using qemu to speed up builds`\
` with native binaries.`\
` This should not be installed on systems, it is just intended for qemu environments.`\
` %prep`\
` %setup -q -D -T -n .`\
` %build`\
` %install`\
` binaries="/%_lib/libnsl.so.1 /%_lib/libnss_compat.so.2 %{_libdir}/rpm-plugins/msm.so" # loaded via dlopen by glibc`\
` %ifarch %ix86`\
`     LD="/lib/ld-linux.so.2"`\
` %else`\
`     echo "ERROR unhandled arch"`\
`     exit 1`\
` %endif`\
` for executable in $LD \`\
`     /usr/bin/{bash,rpm,rpmdb} \`\
`     /usr/bin/{gzip,grep,egrep,sed,tar} \`\
`     /usr/lib/libnssdbm3.so /usr/lib/libsoftokn3.so /lib/libfreebl3.so \`\
`     /usr/bin/{bzip2,cat,expr,make,m4,mkdir,msgexec,msgfmt,msgcat,msgmerge,mv,patch,rm,rmdir,rpmbuild,xz,xzdec} \`\
`     /usr/bin/{awk,gawk} \`\
`     /usr/bin/flex \`\
` %if 0%{?_with_perl_and_python_emul}`\
`     /usr/bin/{a2p,perl,perl5.16.3} \`\
`     /usr/bin/python \`\
` %endif`\
`     /usr/bin/{cmake,ccmake,cpack,ctest} `\
` do    `\
`     # add lib dependencies`\
``      binaries="$binaries $executable `ldd $executable | sed -n 's,.*=>  ``$/[^ ]*$``  .*,\1,p'`" ``\
` done`\
` %if %hijack_gcc`\
` for executable in %{CROSS_COMPILER_PATH}/bin/* \`\
` %{CROSS_COMPILER_PATH}/%{tizen_arch}-linux/bin/* \`\
` %{CROSS_COMPILER_PATH}/lib/gcc/%{tizen_arch}-linux/%{gcc_suffix}/* \`\
` %{CROSS_COMPILER_PATH}/libexec/gcc/%{tizen_arch}-linux/%{gcc_suffix}/*`\
` do`\
`     [ -d $executable ] && continue`\
`     binaries="$binaries $executable"`\
` done`\
` %endif`\
` for binary in $binaries`\
` do`\
`     outfile=%buildroot%{our_path}$(echo $binary | sed 's:/opt/toolchains/gcc-%{gcc_suffix}:/usr:;s:%{%{tizen_arch}_cross_env}:/usr:;s:%{tizen_arch}-linux-::')`\
`     [ -f $outfile ] && continue`\
`     mkdir -p ${outfile%/*}`\
`     cp -aL $binary $outfile `\
`     objdump -s -j .rodata -j .data $outfile | sed 's/^ *`$[a-z0-9]*$`/\1:/' | \`\
`         grep ': ' | grep -v 'file format' | grep -v 'Contents of section' | \`\
`         xxd -g4 -r - $outfile.data`\
`     if grep -q "%{HOST_ARCH}"$outfile.data; then`\
`         echo "ERROR file $binary leaks host information into the guest"`\
`         exit 1`\
`     fi`\
`     rm -f $outfile.data`\
`     [ "$binary" == "$LD" ] && continue`\
`     if `[`|`` ``"$outfile"`` ``==`` ``*".a"`` ``||`` ``"$outfile"`` ``==`` ``*".la"`` `]("$outfile"_==_*".o" "wikilink")` ; then`\
`         continue`\
`     fi`\
`     patchelf --debug --set-rpath "%our_path/%_lib:%our_path%_libdir" $outfile`\
`     # not all binaries have an .interp section`\
`     if patchelf --print-interpreter $outfile; then`\
`         patchelf --debug --set-interpreter %{our_path}$LD $outfile`\
`     fi`\
` done`\
` pushd %{buildroot}%{our_path} &&    ln -s usr/bin && popd`\
` %if %hijack_gcc`\
`     # create symlinks for lib64 / lib mappings (gcc!)`\
`     mkdir -p "%{buildroot}%{our_path}/usr/lib/"`\
`     mkdir -p "%{buildroot}%{our_path}/usr/lib/gcc/%{tizen_arch}-linux/%{gcc_suffix}"`\
`     mkdir -p "%{buildroot}%{our_path}/usr/libexec/gcc"`\
`     mkdir -p "%{buildroot}%{our_path}/usr/%{tizen_arch}-linux"`\
`     cp "%{buildroot}%{our_path}/usr/bin/gcc" "%{buildroot}%{our_path}/usr/bin/cc"`\
`     ln -s ../bin/cpp %{buildroot}%{our_path}/usr/lib`\
`     rm -rf %{buildroot}%{our_path}/usr/bin/%{tizen_arch}-linux-*`\
`     ln -sf ../bin %{buildroot}%{our_path}/usr/%{tizen_arch}-linux/bin`\
`     ln -sf bash %{buildroot}%{our_path}/bin/sh`\
`     # allow abuild to do the mv`\
`     chmod 777 %{buildroot}/emul`\
` %endif`\
` # Make QEMU available through /qemu`\
` mkdir %buildroot/qemu`\
` cp -L /usr/bin/qemu-%{tizen_arch}{,-binfmt} %buildroot/qemu/`\
` %fdupes -s %{buildroot}`\
` export NO_BRP_CHECK_RPATH="true"`\
` %files`\
` %defattr(-,root,root)    `\
` %dir`\
` /emul`\
` /qemu`

### libc

` %define gcc_version         483`\
` %define gcc_suffix          4.8.3`\
` %define CROSS_COMPILER_PATH /opt/toolchains/gcc-%{gcc_suffix}`\
` %define tizen_arch          your_new_arch`\
` %define libc                your_libc`\
` Name:           %{libc}`\
` Summary:        Standard Shared Libraries (from the GNU C Library)`\
` License:        LGPL-2.1+ and LGPL-2.1+-with-GCC-exception and GPL-2.0+`\
` Group:          Base/Libraries`\
` AutoReq:        0`\
` BuildRequires:  fdupes`\
` BuildRequires:  xz`\
` BuildRequires:  gcc-%{libc}`\
` Version:        2.18`\
` Release:        0`\
` Url:            `[`http://www.gnu.org/software/libc/libc.html`](http://www.gnu.org/software/libc/libc.html)\
` Source5:        nsswitch.conf`\
` Source7:        bindresvport.blacklist`\
` # For systemd `\
` Source20:       nscd.conf`\
` Source21:       nscd.service`\
` Requires(pre):  filesystem`\
` Requires:       /usr/bin/sed`\
` Provides:       rtld(GNU_HASH)`\
` Provides:       ldconfig`\
` # The dynamic linker supports DT_GNU_HASH`\
` Provides:       rtld(GNU_HASH)`\
` Provides:       glibc`\
` Provides:       kernel-headers`\
` Provides:       linux-kernel-headers = 3.1.0`\
` ExclusiveArch:  %ix86 %{tizen_arch}`\
` %description`\
` The GNU C Library provides the most important standard libraries used`\
` by nearly all programs: the standard C library, the standard math`\
` library, and the POSIX thread library. A system is not functional`\
` without these libraries.`\
` %package         locale`\
` Summary:         Locale Data for Localized Programs`\
` License:         GPL-2.0+ and MIT and LGPL-2.1+`\
` Requires(post):  /usr/bin/cat`\
` Requires:        %{libc} = %{version}`\
` Provides:        glibc-locale`\
` %description locale`\
` Locale data for the internationalisation features of the GNU C library.`\
` %package         devel`\
` Summary:         Include Files and Libraries Mandatory for Development`\
` License:         BSD-3-Clause and LGPL-2.1+ and LGPL-2.1+-with-GCC-exception and GPL-2.0+`\
` Requires:        %{libc} = %{version}`\
` Provides:        glibc-devel`\
` Provides:        glibc-devel-32bit`\
` %description devel`\
` These libraries are needed to develop programs which use the standard C`\
` library.`\
` %package         devel-static`\
` Summary:         C library static libraries for -static linking`\
` License:         BSD-3-Clause and LGPL-2.1+ and LGPL-2.1+-with-GCC-exception and GPL-2.0+`\
` Requires:        %{name}-devel = %{version}`\
` Provides:        %{name}-static = %version`\
` Provides:        glibc-devel-static`\
` %description     devel-static`\
` The glibc-devel-static package contains the C library static libraries`\
` for -static linking.  You don't need these, unless you link statically,`\
` which is highly discouraged.`\
` %prep`\
` %setup -q -D -T -n .`\
` %build`\
` %install`\
` # We don't want to strip the .symtab from our libraries in find-debuginfo.sh,`\
` # certainly not from libpthread.so.* because it is used by libthread_db to find`\
` # some non-exported symbols in order to detect if threading support`\
` # should be enabled.  These symbols are _not_ exported, and we can't easily`\
` # export them retroactively without changing the ABI.  So we have to`\
` # continue to "export" them via .symtab, instead of .dynsym :-(`\
` # But we also want to keep .symtab and .strtab of other libraries since some`\
` # debugging tools currently require these sections directly inside the main`\
` # files - specifically valgrind and PurifyPlus.`\
` export STRIP_KEEP_SYMTAB=*.so*`\
` # Make sure we will create the gconv-modules.cache`\
` mkdir -p %{buildroot}%{_libdir}/gconv`\
` touch    %{buildroot}%{_libdir}/gconv/gconv-modules.cache`\
` # Install base glibc`\
` mkdir -p %buildroot%{_libdir}`\
` cp -rf   %{CROSS_COMPILER_PATH}/%{tizen_arch}-linux/sys-root/lib/*     %buildroot%{_libdir}`\
` cp -rf   %{CROSS_COMPILER_PATH}/%{tizen_arch}-linux/lib/lib*         %buildroot%{_libdir}`\
` rm -rf   %buildroot/%{_libdir}/*.a`\
` rm -rf   %buildroot/%{_libdir}/*.la`\
` # Miscelanna:`\
` mkdir -p %{buildroot}/etc`\
` install -m 644 %{SOURCE7} %{buildroot}/etc`\
` install -m 644 %{SOURCE5} %{buildroot}/etc`\
` # Create ld.so.conf`\
` cat > %{buildroot}/etc/ld.so.conf <<EOF`\
` /usr/local/lib`\
` include /etc/ld.so.conf.d/*.conf`\
` EOF`\
` # Add ldconfig cache directory for directory ownership`\
` mkdir -p %{buildroot}/var/cache/ldconfig`\
` # Empty the ld.so.cache:`\
` rm -f %{buildroot}/etc/ld.so.cache`\
` touch %{buildroot}/etc/ld.so.cache`\
` # Remove timezone data, now coming in standalone package:`\
` for i in sbin/sln usr/bin/tzselect usr/sbin/zic usr/sbin/zdump etc/localtime; do`\
`     rm -f  %{buildroot}/$i`\
` done`\
` rm -rf     %{buildroot}%{_datadir}/zoneinfo`\
` mkdir   -p %{buildroot}/usr/lib/tmpfiles.d/`\
` install -m 644 %{SOURCE20}  %{buildroot}/usr/lib/tmpfiles.d/`\
` mkdir   -p %{buildroot}/usr/lib/systemd/system`\
` install -m 644 %{SOURCE21}  %{buildroot}/usr/lib/systemd/system`\
` mkdir   -p %{buildroot}/usr/bin`\
` mkdir   -p %{buildroot}/sbin`\
` install -m 655 %{CROSS_COMPILER_PATH}/%{tizen_arch}-linux/sys-root/sbin/ldconfig     %{buildroot}/sbin`\
` install -m 655 %{CROSS_COMPILER_PATH}/%{tizen_arch}-linux/sys-root/usr/bin/ldd       %{buildroot}/usr/bin`\
` install -m 655 %{CROSS_COMPILER_PATH}/%{tizen_arch}-linux/sys-root/usr/bin/getconf   %{buildroot}/usr/bin`\
` install -m 655 %{CROSS_COMPILER_PATH}/%{tizen_arch}-linux/sys-root/usr/bin/iconv     %{buildroot}/usr/bin`\
` install -m 655 %{CROSS_COMPILER_PATH}/%{tizen_arch}-linux/sys-root/usr/bin/getent    %{buildroot}/usr/bin`\
` %files`\
` # glibc`\
` %defattr(-,root,root)`\
` %config(noreplace)  /etc/bindresvport.blacklist`\
` %config             /etc/ld.so.conf`\
` %config             /etc/nsswitch.conf`\
` %attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /etc/ld.so.cache`\
` /usr/bin/ldd`\
` /usr/bin/iconv`\
` /usr/bin/getconf`\
` /usr/bin/getent`\
` /sbin/ldconfig`\
` %{_libdir}/*`\
` %files locale`\
` %defattr(-,root,root)`\
` %files devel`\
` %defattr(-,root,root)`\
` #%{_includedir}/*`\
` #%{_libdir}/*.o`\
` #%{_libdir}/*.so`

### gcc

` %define gcc_version         483`\
` %define gcc_suffix          4.8.3`\
` %define CROSS_COMPILER_PATH /opt/toolchains/gcc-%{gcc_suffix}`\
` %define tizen_arch          your_new_arch`\
` %define libc                your_libc`\
` Name:           gcc%{gcc_version}`\
` URL:            `[`http://gcc.gnu.org/`](http://gcc.gnu.org/)\
` Version:        %{gcc_suffix}`\
` Release:        1`\
` ExclusiveArch:  %ix86 %{tizen_arch}`\
` Group:          Development/Toolchain`\
` AutoReq:        0`\
` BuildRequires:  gcc-%{libc}`\
` Summary:        The GNU C Compiler and Support Files`\
` License:        GPL-3.0+`\
` Provides:       gcc%{gcc_version}`\
` %description`\
` Core package for the GNU Compiler Collection, including the C language`\
` frontend.`\
` Language frontends other than C are split to different sub-packages,`\
` namely gcc-ada, gcc-c++, gcc-fortran, gcc-java, gcc-objc and`\
` gcc-obj-c++.`\
` %package -n     gcc%{gcc_version}-cross`\
` Summary:        The GNU C Compiler and Support Files`\
` License:        GPL-3.0+`\
` %description -n gcc%{gcc_version}-cross`\
` Fake rpm that emulate crosscomipler, needed for refsw compilation.`\
` %package -n     cpp%{gcc_version}`\
` Summary:        The system GNU Preprocessor`\
` License:        GPL-3.0+`\
` %description -n cpp%{gcc_version}`\
` The system GNU Preprocessor.`\
` %package -n     gcc%{gcc_version}-locale`\
` Summary:        The system GNU Compiler locale files`\
` License:        GPL-3.0+`\
` %description -n gcc%{gcc_version}-locale`\
` The system GNU Compiler locale files.`\
` %package -n     gcc%{gcc_version}-info`\
` Summary:        The system GNU Compiler documentation`\
` License:        GFDL-1.2`\
` %description -n gcc%{gcc_version}-info`\
` The system GNU Compiler documentation.`\
` %package -n     gcc%{gcc_version}-c++`\
` Summary:        The system GNU C++ Compiler`\
` License:        GPL-3.0+`\
` Provides:       c++_compiler`\
` %description -n gcc%{gcc_version}-c++`\
` The system GNU C++ Compiler.`\
` %package -n     libstdc++%{gcc_version}-devel`\
` Summary:        The system GNU C++ development files`\
` License:        GPL-3.0-with-GCC-exception`\
` %description -n libstdc++%{gcc_version}-devel`\
` The system GNU C++ development files.`\
` %prep`\
` %setup -q -D -T -n .`\
` %build`\
` %install`\
` mkdir -p %buildroot/usr/bin`\
` rm -rf   %buildroot/usr/%{tizen_arch}-linux/bin`\
` mkdir -p %buildroot/usr/%{tizen_arch}-linux/bin`\
` # create fake binaries`\
` for executable in %buildroot/usr/bin/{c++,c++filt,cc,cpp,g++,gcc,gcc-%{gcc_suffix},gcj,gcov,gprof,jcf-dump,ld,run,size,strip,sstrip,strings}`\
` do`\
`     ln -sf fake_binary $executable`\
` done`\
` # prepare folders without fake executables`\
` cp -rf %{CROSS_COMPILER_PATH}/include   %buildroot/usr`\
` cp -rf %{CROSS_COMPILER_PATH}/share     %buildroot/usr`\
` cp -rf %{CROSS_COMPILER_PATH}/lib       %buildroot/usr`\
` ln -sf /usr/bin/cpp                     %buildroot/usr/lib/cpp`\
` #prepare folders with fake executables`\
` mkdir -p %buildroot/usr/libexec/gcc/%{tizen_arch}-linux/%{gcc_suffix}`\
` cp     %{CROSS_COMPILER_PATH}/libexec/gcc/%{tizen_arch}-linux/%{gcc_suffix}/liblto_plugin.so* %buildroot/usr/libexec/gcc/%{tizen_arch}-linux/%{gcc_suffix}/`\
` for executable in %buildroot/usr/libexec/gcc/%{tizen_arch}-linux/%{gcc_suffix}/{cc1,cc1obj,cc1plus,collect2,f951,jc1,jvgenmain,lto1,lto-wrapper}`\
` do`\
`    ln -sf /usr/bin/fake_binary $executable`\
` done`\
` mkdir -p %buildroot/usr/%{tizen_arch}-linux/bin`\
` cp -rf   %{CROSS_COMPILER_PATH}/%{tizen_arch}-linux/include                    %buildroot/usr/%{tizen_arch}-linux`\
` cp -rf   %{CROSS_COMPILER_PATH}/%{tizen_arch}-linux/lib                        %buildroot/usr/%{tizen_arch}-linux`\
` cp -r    %{CROSS_COMPILER_PATH}/%{tizen_arch}-linux/sys-root/usr/include/*     %buildroot/usr/include`\
` cp -r    %{CROSS_COMPILER_PATH}/%{tizen_arch}-linux/sys-root/usr/lib/*         %buildroot/usr/lib`\
` ln -sf /usr/bin/fake_binary %buildroot/usr/%{tizen_arch}-linux/bin/fake_binary`\
` ln -sf ../../               %buildroot/usr/%{tizen_arch}-linux/sys-root`\
` for executable in %buildroot/usr/%{tizen_arch}-linux/bin/{ar,as,c++,g++,gcc,gfortran,ld,nm,objcopy,objdump,ranlib,strip}`\
` do`\
`    ln -sf /usr/bin/fake_binary $executable`\
` done`\
` # create wrappers on standard tools`\
` for i in ld gcc c++ cpp ar nm strip objcopy objdump ranlib readelf; do`\
`     echo '#!/bin/bash`\
`     exec '$i' "$@"`\
`     ' > %{buildroot}/usr/bin/%{tizen_arch}-linux-$i`\
`     chmod +x %{buildroot}/usr/bin/%{tizen_arch}-linux-$i`\
` done`\
` #clean unnecessary files`\
` rm -rf %buildroot/usr/share/info`\
` rm -rf %buildroot/usr/share/man`\
` rm -rf %buildroot/usr/share/gdb`\
``  rm -rf `find %buildroot/usr| grep "\.la$"` ``\
` %files`\
` %defattr(-,root,root)`\
` /usr/bin/c++`\
` /usr/bin/c++filt`\
` /usr/bin/cc`\
` /usr/bin/cpp`\
` /usr/bin/g++`\
` /usr/bin/gcc`\
` /usr/bin/gcc-%{gcc_suffix}`\
` /usr/bin/gcj`\
` /usr/bin/gcov`\
` /usr/bin/gprof`\
` /usr/bin/jcf-dump`\
` /usr/bin/ld`\
` /usr/bin/run`\
` /usr/bin/size`\
` /usr/bin/strip`\
` /usr/bin/sstrip`\
` /usr/bin/strings`\
` /usr/include/*`\
` /usr/lib/*`\
` /usr/libexec/*`\
` /usr/%{tizen_arch}-linux/*`\
` /usr/share/locale/*`\
` /usr/share/gcc-%{gcc_suffix}/*`\
` %files -n gcc%{gcc_version}-cross`\
` %defattr(-,root,root)`\
` /usr/bin/%{tizen_arch}-linux-*`\
` %files -n cpp%{gcc_version}`\
` %defattr(-,root,root)`\
` %files -n gcc%{gcc_version}-c++`\
` %defattr(-,root,root)`\
` %files -n gcc%{gcc_version}-locale`\
` %defattr(-,root,root)`\
` %files -n gcc%{gcc_version}-info`\
` %defattr(-,root,root)`\
` %files -n libstdc++%{gcc_version}-devel`\
` %defattr(-,root,root)`

### fake\_binutils

` %define gcc_version          483`\
` %define gcc_suffix           4.8.3`\
` %define CROSS_COMPILER_PATH  /opt/toolchains/gcc-%{gcc_suffix}`\
` %define tizen_arch           your_new_arch`\
` %define libc                 your_libc`\
` Name:           fake_binutils`\
` Version:        2.19.92`\
` Release:        0`\
` Url:            `[`http://www.gnu.org/software/binutils/`](http://www.gnu.org/software/binutils/)\
` Summary:        GNU Binutils`\
` License:        GFDL-1.3 and GPL-3.0+`\
` Group:          Development/Tools/Building`\
` AutoReq:        0`\
` BuildRequires:  gcc-%{libc}`\
` Provides:       binutils`\
` ExclusiveArch:  %ix86 %{tizen_arch}`\
` %description`\
` C compiler utilities: ar, as, gprof, ld, nm, objcopy, objdump, ranlib,`\
` size, strings, and strip. These utilities are needed whenever you want`\
` to compile a program or kernel.`\
` %package        devel`\
` Summary:        The GNU Binutils devel`\
` License:        GPL-3.0+`\
` Provides:       binutils-devel`\
` %description    devel`\
` Fake package to resolve dependencies`\
` %prep`\
` %setup -q -D -T -n .`\
` %build`\
` echo 'int printf(char *, ...);int main(int argc, char **argv){printf("\nThis is fake \"%s\". If you see this message that smth is wrong with qemu\n", argv[0]);return 0;}' > fake_binary.c`\
` %ifarch %{tizen_arch}`\
`     gcc -o fake_binary fake_binary.c`\
` %endif`\
` %ifarch %ix86`\
`     %{CROSS_COMPILER_PATH}/bin/%{tizen_arch}-linux-gcc -o fake_binary fake_binary.c`\
` %endif`\
` cp fake_binary %_sourcedir/`\
` %install`\
` mkdir -p  %buildroot/usr/bin`\
` cp -rf    %_sourcedir/fake_binary     %buildroot/usr/bin`\
` chmod a+x %buildroot/usr/bin/fake_binary`\
` rm    -rf %buildroot/usr/%{tizen_arch}-linux/bin`\
` mkdir -p  %buildroot/usr/%{tizen_arch}-linux/bin`\
` for executable in %buildroot/usr/bin/{ar,as,ld,ld.gold,ld.bfd,nm,ranlib,strip,addr2line,objcopy,objdump,readelf}`\
` do`\
`     ln -sf fake_binary $executable`\
` done`\
` # add linker scripts`\
` mkdir -p %buildroot/%{_libdir}`\
` cp -rf   %{CROSS_COMPILER_PATH}/%{tizen_arch}-linux/lib/ldscripts %buildroot/%{_libdir}`\
` mkdir -p %buildroot/usr/%{tizen_arch}-linux/lib/`\
` %post`\
` %files `\
` %defattr(-,root,root)`\
` %{_libdir}/ldscripts`\
` %{_bindir}/*`\
` %files devel`\
` %defattr(-,root,root)`\
` %changelog`

[Category:Tool](Category:Tool "wikilink")
