# MIC Reference

MIC supports the following image formats:

- Loop
  - Each loop corresponds to 1 partition.
  - A file system is created inside the image.
  - For a configuration with multiple partitions (specified in the kickstart file), MIC generates multiple loop images.
  - Multiple loop images can be packed into a single archive file.
- Raw
  - "Raw" format basically means hard disk dumping.
  - It includes a partition table and all the partitions.
  - The image is bootable directly.
- Livecd and liveusb
  - It is mainly used for an ia32 build.
  - It can be burned to a CD or USB stick, which can be booted into a live system or installation UI.
- fs
  - "fs" means file-system.
  - MIC can install all the Tizen files to a specified directory, which can be used directly as a chroot environment.

## Creating an Image

To create a basic image, use the following command syntax:

```bash
$ mic create(cr) SUBCOMMAND <ksfile> [OPTION]
```

In the command:

- `SUBCOMMAND` specifies the image format:

  ```bash
  fs                 create fs image, which is also a chroot directory
  livecd             create live CD image, used for CD booting
  liveusb            create live USB image, used for USB booting
  loop               create loop image, including multi-partitions
  raw                create raw image, containing multi-partitions
  ```

- `<ksfile>` specifies the kickstart file.

  The kickstart file is a simple text file, containing a list of items about, for example, image partition, setup, Bootloader, and packages to be installed. Each item is identified by a key word.


- `OPTION` can be used to specify various details:

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
  --pack-to=PACK_TO   Pack the images together into the specified archive,
                      extension supported: .zip, .tar, .tar.gz, .tar.bz2,
                      etc. by default, .tar will be used
  --copy-kernel       Copy kernel files from image /boot directory to the
                      image output directory.
  --install-pkgs=INSTALL_PKGS
                      Specify what type of packages to be installed, valid:
                      source, debuginfo, debugsource
  ```

  Other options include:

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

For example, to create a loop image, use the following command:

```bash
$ mic cr loop tizen.ks
```

### Example of Creating a Loop Image

To create a loop image:

1. Prepare the kickstart file.

   To create an image, you need a proper `.ks` file:

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

   The above file can be used to create a minimum Tizen image. For other repositories, replace the URL. For example:

   ```bash
   $ repo --name=REPO-NAME --baseurl=https://username:passwd@yourrepo.com/ia32/packages/ --save  --ssl_verify=no
   ```

1. Create the loop image with the following command in the terminal:

   ```bash
   $ sudo mic create loop tizen-min.ks
   ```

### Example of Creating an Image with a Local RPM Package

If you want to install your own RPM into the image, to be able to test your package with the image, using a local package path can be helpful. For example, if your `hello.rpm` file is under the `localpath` directory, use the following command:

```bash
$ sudo mic create loop test.ks --local-pkgs-path=localpath
```

The command output states `Marked 'hello.rpm' as installed`, and the `hello.rpm` file is installed in the image. Make sure that your RPM is not in the `.ks` file's repository and that your RPM version is newer or equal to the repository RPM version.

### Example of Creating an Image with a Specific Archive Format

You can use MIC to archive the image with a specific format, such as `.zip`, `.tar` (default), `.tar.gz`, or `.tar.bz2`.

To use a specific archive format:

```bash
$ sudo mic create loop test.ks --pack-to=@NAME@.tar.gz
```

## Chrooting Inside an Image

The MIC `chroot` command is a great enhancement over the basic `chroot` command in the Linux system.

To chroot inside the image, use the following command syntax:

```bash
$ mic chroot(ch) [OPTION] <imgfile>
```

In the command:

- `OPTION` can be used to specify various details:
  ```
  -h, --help          Show this help message and exit
  -s SAVETO, --saveto=SAVETO
                      Save the unpacked image to a specified dir
  ```
- `<imgfile>` specifies the image file.
  
For example:

```bash
$ mic ch loop.img
$ mic ch tizen.iso
$ mic ch -s tizenfs tizen.usbimg
```

## Converting an Image

To convert an image to another format, use the following command syntax:

```bash
mic convert(cv) [OPTION] <imagefile> <destformat>
```

In the command:

- `OPTION` can be used to specify various details:
  ```bash
  -h, --help   Show this help message and exit
  -S, --shell  Launch shell before packaging the converted image
  ```
- `<imgfile>` specifies the image file.
- `<destformat>` specifies the destination format.

For example:

```bash
$ mic cv tizen.iso liveusb
$ mic cv tizen.usbimg livecd
$ mic cv --shell tizen.iso liveusb
```

## Setting a Proxy

You can set a proxy in various ways:

- Proxy variable in bash

  It is common to use a proxy variable in bash. In general, you can set the following environment variables to enable proxy support:

  ```bash
  export http_proxy=http://proxy.com:port
  export https_proxy=http://proxy.com:port
  export ftp_proxy=http://proxy.com:port
  export no_proxy=localhost,127.0.0.0/8,.company.com
  ```

  You do not need all the variables, so check which ones you need and only export those. When the repository URL in your `.ks` file starts with `https`, MIC uses the `https_proxy` variable. Be careful when setting the `no_proxy` variable, because it indicates which domain must be accessed directly. Do not leave any blank spaces in the string.

  MIC needs the sudo privilege. To keep the proxy environment, set `/etc/sudoers` to add the proxy variables to `env_keep`:

  ```
  Defaults        env_keep += "http_proxy https_proxy ftp_proxy no_proxy"
  ```

  > **Note**
  >
  > Use `visudo` to modify `/etc/sudoers`.

  If you do not want to change your `/etc/sudoers`, you can set the proxy in the `mic.conf` file, as described below.

- Proxy setting in the `mic.conf` file

  The proxy environment variables can disturb other programs, so to enable proxy support only for MIC, set the proxy in the `etc/mic/mic.conf`file:

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

- Proxy setting in the `.ks` file

  If you need to enable proxy support for a special repository URL only, leaving others at their existing proxy setting:

  ```bash
  $ repo --name=oss --baseurl=http://www.example.com/repos/oss/packages/ --proxy=http://host:port
  ```

## Getting Help

To get help:

- Use the `man`command:
  ```bash
  $ man mic
  ```

- Use the `--help` options:
  ```bash
  $ mic --help
  $ mic create --help
  $ mic help create
  $ mic create loop --help
  $ mic create help loop
  ```
