# MIC Reference

MIC offers three major functions:

- creating an image with a different format
- converting an image to another format
- chrooting into an image

### Getting help

You can also use `$ mic --help` or `$ mic <subcmd> --help`  to get the help message.

How to get help:

- using 'man':
  ```bash
  $ man mic
  ```

- using '--help' options:
  ```bash
  $ mic --help
  $ mic create --help
  $ mic help create
  $ mic create loop --help
  $ mic create help loop
  ```

## Image formulation support

- Loop

  - Each loop corresponds to one partition
  - A file system will be created inside the image
  - For a configuration with multiple partitions, which is specified in the kickstartfile, mic will generate multiple loop images
  - And multiple loop images can be packed into a single archive file

- Raw

  - “raw” format means something like hard disk dumping
  - Including partition table and all the partitions
  - The image is bootable directly

- Livecd/liveusb

  - Mainly used for an ia32 build, it can be burned to CD or usbstick, which can be booted into a live system or installation UI

- fs

  - “fs” means file-system
  - mic can install all the Tizen files to the specified directory, which can be used directly as chroot env

## Create image

### Basic usage

- Command line for image creation:

```bash
  $ mic create(cr) SUBCOMMAND <ksfile> [OPTION]
```

- Sub-commands, to specify image format, include:

```
   help(?)            give detailed help on a specific sub-command
   fs                 create fs image, which is also a chroot directory
   livecd             create live CD image, used for CD booting
   liveusb            create live USB image, used for USB booting
   loop               create loop image, including multi-partitions
   raw                create raw image, containing multi-partitions
```

- <ksfile>:

The kickstart file is a simple text file, containing a list of items about image partition, setup, Bootloader, packages to be installed, etc, each identified by a keyword.

In Tizen, the released image will have a ks file along with image. For example, you can download the ks file from: [http://download.tizen.org/releases/daily/trunk/ivi/latest/images/ivi-min...](http://download.tizen.org/releases/daily/trunk/ivi/latest/images/ivi-min-pc/ivi-min-pc-tizen_20120926.2.ks)

- Options include:

```
   -h, --help          Show this help message and exit
   --logfile=LOGFILE   Path of logfile
   -c CONFIG, --config=CONFIG
                       Specify config file for MIC
   -k CACHEDIR, --cachedir=CACHEDIR
                       Cache directory to store downloaded files
   -o OUTDIR, --outdir=OUTDIR
                       Output directory
   -A ARCH, --arch=ARCH
                       Specify repo architecture
   --release=RID       Generate a release of RID with all necessary files.
                       When @BUILD_ID@ is contained in kickstart file, it
                       will be replaced by RID.
   --record-pkgs=RECORD_PKGS
                       Record the info of installed packages. Multiple values
                       can be specified which joined by ",", valid values:
                       "name", "content", "license", "vcs".
   --pkgmgr=PKGMGR     Specify backend package manager
   --local-pkgs-path=LOCAL_PKGS_PATH
                       Path for local pkgs(rpms) to be installed
   --pack-to=PACK_TO   Pack the images together into the specified achive,
                       extension supported: .zip, .tar, .tar.gz, .tar.bz2,
                       etc. by default, .tar will be used
   --copy-kernel       Copy kernel files from image /boot directory to the
                       image output directory.
   --install-pkgs=INSTALL_PKGS
                       Specify what type of packages to be installed, valid:
                       source, debuginfo, debugsource
```

- Other options:

```
   --runtime=RUNTIME_MODE
                       Sets runtime mode, the default is bootstrap mode, valid
                       values: "native", "bootstrap". "native" means mic uses
                       localhost environment to create image, while "bootstrap"
                       means mic uses one tizen chroot environment to create image.
   --compress-image=COMPRESS_IMAGE (for loop & raw)
                       Sets the disk image compression. Note: The available
                       values might depend on the used filesystem type.
   --compress-disk-image=COMPRESS_IMAGE
                       Same with --compress-image
   --shrink (for loop)
                       Whether to shrink loop images to minimal size
   --generate-bmap (for raw)
                       Generate the block map file
   --fstab-entry=FSTAB_ENTRY (for raw)
                       Set fstab entry, 'name' means using device names,
                       'uuid' means using filesystem uuid
```

- Examples:

  - create a loop image

    ```bash
    $ mic cr loop tizen.ks
    ```

### How to create an image

- Prepare kickstart file

To create an image, you need a proper ks file.

Here's a simple example:

```bash
# filename: tizen-min.ks
lang en_US.UTF-8
keyboard us
timezone --utc America/Los_Angeles
 
part / --size 1824 --ondisk sda --fstype=ext3
 
rootpw tizen
bootloader  --timeout=0  --append="rootdelay=5"
 
desktop --autologinuser=tizen
user --name tizen  --groups audio,video --password 'tizen'
 
repo --name=Tizen-base --baseurl=http://download.tizen.org/snapshots/trunk/common/latest/repos/base/ia32/packages/
repo --name=Tizen-main --baseurl=http://download.tizen.org/snapshots/trunk/common/latest/repos/main/ia32/packages/
 
%packages --ignoremissing
@tizen-bootstrap
%end
 
%post
rm -rf /var/lib/rpm/__db*
rpm --rebuilddb
%end
 
%post --nochroot
%end
```

The ks file above can be used to create a minimum Tizen image. For other repositories, you can replace it with the appropriate repository url.

For example:

```bash
$ repo --name=REPO-NAME --baseurl=https://username:passwd@yourrepo.com/ia32/packages/ --save  --ssl_verify=no
```

- Create an loop image

  To create an image, run MIC in the terminal:

  ```bash
  $ sudo mic create loop tizen-min.ks
  ```

### Create an image with a local rpm package

"How can I install my own rpm into the image, so I can test my package with the image?"

In such a case, using a local package path would be very helpful. For example, if your rpm 'hello.rpm' is under directory 'localpath', run MIC, like below:

```bash
$ sudo mic create loop test.ks --local-pkgs-path=localpath
```

From the output, MIC will tell you "Marked 'hello.rpm' as installed", and it will install hello.rpm in the image. Be sure your rpm is not in the ks file's repo and that your rpm's version is newer or equal to the repo rpm version.

### Create image with specific archive format

MIC can help archive the image with a specific format, including: .zip, .tar, .tar.gz, .tar.bz2, etc.
By default, .tar will be used.

```bash
$ sudo mic create loop test.ks --pack-to=@NAME@.tar.gz
```

## Chroot

This command is used to chroot inside the image. It's a great enhancement of the chroot command in the Linux system.

- Usage:

  ```bash
  $ mic chroot(ch) <imgfile>
  ```

- Options:

  ```
   -h, --help          Show this help message and exit
   -s SAVETO, --saveto=SAVETO
                       Save the unpacked image to a specified dir
  ```

- Examples:

  ```bash
  $ mic ch loop.img   mic ch tizen.iso   mic ch -s tizenfs tizen.usbimg
  ```

## Convert

This command is used for converting an image to another format.

- Usage:

  ```bash
  mic convert(cv) <imagefile> <destformat>
  ```

- Options:

  ```bash
   -h, --help   Show this help message and exit
   -S, --shell  Launch shell before packaging the converted image
  ```

- Examples:

  ```bash
   $ mic cv tizen.iso liveusb
   $ mic cv tizen.usbimg livecd
   $ mic cv --shell tizen.iso liveusb
  ```

## How to set a proxy

- Proxy variable in bash

  It's common to use the proxy variable in bash. In general, you can set the following environment variables to enable proxy support:

  ```bash
  export http_proxy=http://proxy.com:port
  export https_proxy=http://proxy.com:port
  export ftp_proxy=http://proxy.com:port
  export no_proxy=localhost,127.0.0.0/8,.company.com
  ```

  You don't need all the variables. Check which ones you do need. When your repo url in your ks file starts with 'https', MIC will use https_proxy. Be especially aware of when you set no_proxy because it indicates which domain should be accessed directly. Don't leave any blank spaces in the string.

  MIC needs sudo privilege, so to keep the proxy environment, you need to set '/etc/sudoers' to add those proxy variables to "env_keep":

  ```
  Defaults        env_keep += "http_proxy https_proxy ftp_proxy no_proxy"
  ```

  > **Note**
  > Use "visudo" to modify /etc/sudoers

  If you don't want to change your /etc/sudoers, there is an alternative for you to set the proxy in mic.conf. See the next section.

- Proxy setting in mic.conf

  The proxy environment variables may disturb other programs, so if you would like to enable proxy support only for MIC, set the proxy in /etc/mic/mic.conf like this:

  ```bash
   [create]
   ; settings for create subcommand
   tmpdir= /var/tmp/mic
   cachedir= /var/tmp/mic/cache
   outdir= .
   pkgmgr = zypp
   proxy = http://proxy.yourcompany.com:8080/
   no_proxy = localhost,127.0.0.0/8,.yourcompany.com
  ```

- Proxy setting in ks file

  It's likely that you will need to enable proxy support only for a special repo url, and other things would remain at their existing proxy setting.

  Here's how to handle that case:

  ```bash
  $ repo --name=oss --baseurl=http://www.example.com/repos/oss/packages/ --proxy=http://host:port
  ```