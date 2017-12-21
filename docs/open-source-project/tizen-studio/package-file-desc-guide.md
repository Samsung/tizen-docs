# Package File Description Guide

When you have configured Tizen Studio and Git, you are ready to start developing Tizen Studio extensions. There are extension points for development in the Web IDE, the native IDE, and the emulator.

To develop Tizen Studio extensions, you need to follow certain packaging rules:

1. Directory and file structure
2. Required files and contents
3. Metapackage configuration

Once your extension conforms to the package file convention, you can proceed with the local build.

## Directory and File Structure

Project structure for developing, packaging, and building extensions requires the following files:

- `package/pkginfo.manifest`: package Information
- `package/changelog`
- `package/script`
  - `build.<BUILD HOST OS>`: build script
  - `<package name>.install.<TARGET OS>`: post-install script
  - `<package name>.remove.<TARGET OS>`: post-removal script


### `pkginfo.manifest` File

This file contains information about the packages created by the source build. It consists of sections and fields:
  
Sections are separated by 2 newline characters (`\n \n`), and each section contains various fields:
- The Common section contains the following fields:
  - Source name
  - Version (required)
  - Maintenance manager information (Maintainer) (required)
- The package-specific section contains the following fields:
  - Package name (required)
  - Installation OS information (required)
  - Build host OS information (required)
  - Install dependency
  - Build dependency
  - Source dependency
  - Attribute information
  - Description
  - C-Prerequisites  
    - Given as `C-Prerequisites : Library name`. If more than 1 library is needed, separate them with `,`.
    - If a library needs to be used for more than 1 version:
      - The library needs to be used in all Ubuntu versions:  
        `C-Prerequisites : libpixman-1-0, libpng12-0`
      - The library needs to be used in a single Ubuntu version:  
        `C-Prerequisites : libxcb-keysyms1 [12.04]`
      - The library needs to be used in multiple Ubuntu versions (separated by a space):  
        `C-Prerequisites : qemu-user-static [11.04 11.10 12.04 12.10 13.04 13.10]`
  
  ```
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


### `build.<OS>` File

This file consists of a shell script. You need to implement some of the following functions:

```bash
clean() {
    // Code clean 
    rm -rf $SRCDIR/*.zip
    rm -rf $SRCDIR/package/testGitA.package.$TARGET_OS
}
build() {
    // Building Source
    echo "TESTGITA : Good job !!!"
    sleep 3
    cat $SRCDIR/a
}
install() {
    // Package Directory Set up
    INSTALL_DIRA=$SRCDIR/package/testGitA.package.$TARGET_OS/data
    mkdir -p $INSTALL_DIRA
    cp $SRCDIR/a $INSTALL_DIRA
}
```

### `changelog` File

This file is included in the package file (.zip). When a new package is deployed, the changelog is updated.

```text
 * 1.0.12    // Same as pkginfo.manifest version
- Title, Desc ,,
==  John Doe <John@abcd.com> 20XX-XX-XX
```

## Package Name Creation Rules

Your package must comply with the extension package name creation rules:

- Package name: `<Profile>-<Version>-<Product-name>-<Package-Name>`
- One of the following types specified with the metapackage name postfix (required):
  - Web: `WebAppDevelopment`  
    For example, `tv-2.4-samsung-public-WebAppDevelopment`
  - Native: `NativeAppDevelopment`  
    For example, `mobile-2.4-product-NativeAppDevelopment`
  - Emulator: `Emulator`  
    For example, `tv-2.4-samsung-public-Emulator`

The list of supported environments in Tizen Studio:
  - Profile: Mobile, Wearable, or TV
  - Platform version: 2.4 or 3.0
  - Development environment: Native IDE, Web IDE, Emulator (CLI will be supported)
