MIC Bootstrap
-------------

### Description

This documentation is to present how to create mic-bootstrap in
technical, it includes baselibs.conf and \_aggregate feature on build
service.

The package \'mic-bootstrap\' is used for mic bootstrap, this package
will be repackaged for i586 and arm libs. it provides a x86 bootstrap
environment for unified usage, especially to speed up the performance of
arm image creation.

As an instance, you can find \'mic-bootstrap\' at \[\#\]\_. Also you can
find \'mic-bootstrap\_aggregate\' at \[\#\]\_.

### Workflow of mic-bootstrap.spec

In this section, it will present the main workflow of
mic-bootstrap.spec:

\- get a list of files to include::

`  $ rpm -qla > filestoinclude1`

\- tar copy to bootstrap directory::

`  $ tar -T filestoinclude1 -cpf - | ( cd %buildroot/bootstrap && tar -xpf - )`

\- generate file list of this rpm::

`  $ find %buildroot | sed -e "s#%{buildroot}##g" | uniq | sort > filestoinclude1`\
``   $ for i in `cat filestoinclude1`; do \ ``\
`  $    if test -h %buildroot/$i || ! test -d %buildroot/$i; then \`\
`  $        echo "$i" >> filestoinclude \`\
`  $    fi \`\
`  $ done`

\- explicit %files with file list::

`  %files -f filestoinclude`

### Mechanism of baselibs.conf

In this section, it will show the mechanism of baselibs.conf used in
mic-bootstrap:

\- specify how to handle mic-bootstrap package::

`  arch i686 targets armv7l:x86-arm i586:x86-arm aarch64:x86-arm`\
`  arch x86_64 targets armv7l:x86-arm x86_64:x86-arm aarch64:x86-arm`

`| it means that subsequent package directives i686 and x86_64 will be repackaged to`\
`| armv7l, i586, aarch64 using `<targettype>`=x86-arm.`

\- declare a package with targettype directives::

`  targettype x86-arm package mic-bootstrap`

`| it means just to create mic-bootstrap-x86-arm package by repackaging mic-bootstrap.`

\- allow filtering of the actions applied::

`    autoreqprov off`\
`    extension -x86-arm`\
`    +/`

`| 'autoreqprov off' means to limit the provides and requires to only those specified.`\
`| 'extension -x86-arm' means the package name uses 'x86-64' as extension.`\
`| '+/' means all files in %buildroot will be repackaged to new package.`

### Build Service baselibs.conf

Open Build Service provides a mechanism that by including a file called
baselibs.conf in the package sources, it can be instructed to create
so-called \"bi-arch\" packages, so that in 32-bit environments, 32-bit
packages need to be created for use with 64-bit environments, and
potentially also vice-versa.

See details at \[\#\]\_.

### Build Service \_aggregate

To avoid rebuilds of packages that are just needed as build requirement
for other packages or just needed because the Project wants to
distribute a complete set of packages for end-users, there is the
\_aggregate feature in Open Build Service.

See details at \[\#\]\_.

### Reference

-   \[\#\]
    <https://build.tizen.org/package/show?package=mic-bootstrap&project=Tizen%3AIVI>
-   \[\#\]
    <https://build.tizen.org/package/show?package=mic-bootstrap_aggregate&project=Tizen%3AIVI>
-   \[\#\]
    <https://en.opensuse.org/openSUSE:Build_Service_baselibs.conf>
-   \[\#\]
    <https://en.opensuse.org/openSUSE:Build_Service_Tips_and_Tricks#link_and_aggregate>

[Category:Tool](Category:Tool "wikilink")
