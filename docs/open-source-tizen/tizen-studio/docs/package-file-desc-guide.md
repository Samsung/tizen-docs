# Package File Description Guide

 Are you finished with Tizen studio and Git configuration? You are ready to develop the Tizen Studio Extension.<br>
We have opened up points that can be extended to the Web IDE, Native IDE and Emulator.

To develop, you need to follow some rules.
1. Directory and file Structure
2. Required files and contents
3. Configuring the metapackage

If you have been created according to the package file convention, you can proceed with the local build.

## Step 1 : Structure and Required files and contents
Describe the project structure for developing, packaging, and building extensions.

- Required files
    - package/pkginfo.manifest : Package Information
    - package/changelog
    - package/script
        - build.{BUILD HOST OS} : build script
        - {package name}.install.{TARGET OS} : post install script
        - {package name}.remove.{TARGET OS} : post remove script


#### **pkginfo.manifest** file
- This file contains various information about the packages that are created by the source build
- Section and Fields
    - A Section is separated by two newline characters "\ n \ n", and one section contains various Fields.
        - Common Section
            - Source name, Version(required), Maintenance manager information(Maintainer)(required).
        - Package-specific Section
            - Package name(required), Installation OS information(required), Build host OS information(required)
            - Install-dependency information, Build-dependency, Source-dependency, Various attribute information, Description
```text
Package : facebook-sdk-back
Label : Facebook SDK for Tizen
Version : 1.3.0
OS : Ubuntu-32
Build-host-os : Ubuntu-64
Maintainer : 
Install-dependency : test
Build-dependency : 
Description : SDK extension for Facebook
C-Prerequisites : libpixman-1-0, qemu-user-static[11.04 11.10]
```
Technical description of C-Prerequisites : 

- C-Prerequisites : Library name, If more than one library is needed, use "," to distinguish. 
- If one library needs to be used for more than one version, write it in [Ubuntu version: Ubuntu version].
    - Should be applied to Ubuntu as a whole
C-Prerequisites: libpixman-1-0, libpng12-0
    - Should only be used in a single specific version
C-Prerequisites: libxcb-keysyms1 [12.04]
    - should be used multiple versions [separated by a "space"]
C-Prerequisites: qemu-user-static [11.04 11.10 12.04 12.10 13.04 13.10]

#### **build.{os}** file
The script consists of a shell script, and you need to implement some of the following functions inside.       

```java

clean() {
    //code clean 
    rm -rf $SRCDIR/\*.zip
    rm -rf $SRCDIR/package/testGitA.package.$TARGET_OS
}
build() {
    // Building Source
    echo "TESTGITA : Good job !!!"
    sleep 3
    cat $SRCDIR/a
}
intall() {
    // Package Directory Set up
    INSTALL_DIRA=$SRCDIR/package/testGitA.package.$TARGET_OS/data
    mkdir -p $INSTALL_DIRA
    cp $SRCDIR/a $INSTALL_DIRA
}
```
#### **changelog** file

- Included in package file (zip)
- Update changelog when new package is deployed. <Version Up required>

```text
 * 1.0.12    // Same as pkginfo.manifest version
- Titile, Desc ,,
== Sujin Lee <lee.sujin@samsung.com> 20XX-XX-XX
```


## Step 2 :Package name creation rule
- List of supported environments in Tizen Studio
    - Platform Version : 2.4 / 3.0
    - Profile : Mobile / Wearable / TV
    - Development Environment : Native IDE, Web IDE, Emulator (CLI will be supported.)

- Compliance with extension package name creation rules
    - Package name : \<Profile\>-\<Version\>-\<Product-name\>-\<Package-Name\>
    - Specify the type below with the postfix name of the metapackage (required)
        - Web : WebAppDevelopment
            - (e.g) tv-2.4-samsung-public-WebAppDevelopment
        - Native: NativeAppDevelopment
            - (e.g) mobile-2.4-product-NativeAppDevelopment
        - Emulator : Emulator
            - (e.g) tv-2.4-samsung-public-Emulator

