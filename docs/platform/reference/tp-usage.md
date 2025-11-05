# Tool for Tizen Platform Development

The `tp` (Tizen Platform Development Tool) tool is designed to help manage various aspects of your Tizen platform development projects, including initialization, configuration, and building.

## Install

Download and install the `tp` tool:

```bash
curl -fsSL https://download.tizen.org/tp/0.3.7/install.sh | sh
```

## How to Use

### Support Commands

```
Tizen platform build and management tool

Usage: tp [OPTIONS] [COMMAND]

Commands:
  init     Initialize tp metadata
  config   Generate and update gbs configuration
  project  Manage projects
  help     Print this message or the help of the given subcommand(s)

Options:
  -d, --debug    Enable debug output
  -h, --help     Print help
  -V, --version  Print version
```

### Initialize `tp`

Check requirements tools and SCM connections. If you have already installed and configured, it will be skipped.

```bash
tp init
```

```
Initialize tp metadata

Usage: tp init [OPTIONS]

Options:
  -u, --update  Update existing metadata
  -h, --help    Print help
```

```
> First time running tp, create default config...
check requirements tools...
        - ✔️  git found at /usr/bin/git
        - ✔️  gbs found at /usr/bin/gbs
        - ✔️  mic found at /usr/bin/mic
        - ✔️  python3 found at /usr/bin/python3

> Check review.tizen.org account
If you have a review.tizen.org account:
 - Use ssh://review.tizen.org:29418/ for the SSH protocol.

You don't have a review.tizen.org account.
- Guide: https://docs.tizen.org/platform/developing/setting-up/

If you don't want to register for an account, use git.tizen.org.

review.tizen.org: Gerrit Code Review
    - Supports ssh://review.tizen.org:29418/

git.tizen.org: Read-only mirror of review.tizen.org
    - No account required.
    - Supports git://git.tizen.org and https://git.tizen.org/cgit.
    - 🔔 The HTTPS protocol can be very slow.
    - 🔔 The HTTPS protocol does not support shallow capabilities.

Tools automatically connect in the following order:
    1. ssh://review.tizen.org:29418 (account required)
    2. git://git.tizen.org
    3. https://git.tizen.org/cgit

? Do you have a https://review.tizen.org account? (y/n)
```

```
> Do you have a https://review.tizen.org account? (y/n) Yes
> Configure git clone...
If you haven't set user in ssh config, please add these lines:
# example of ssh config file (~/.ssh/config)

Host tizen review.tizen.org
    Hostname review.tizen.org
    IdentityFile <YOUR SSH PRIV KEY PATH> # ex) ~/.ssh/id_ed25519 or ~/.ssh/id_rsa
    User <YOUR ACCOUNT NAME>
    Port 29418


If you already set user in ssh config, just press enter.

> Enter your review.tizen.org account name? (enter to skip if configured in ssh)
check scm connections...
check public scm connections...
        - check ssh://review.tizen.org:29418/scm/meta/qb connection...
                ✔️  connection success.
Config file not found, creating new one.
> Installing git-repo tools
> Update build meta repositories...
Cloning into '/home/tizen/.tp/meta/public'...
remote: Counting objects: 30949, done.
remote: Finding sources: 100% (30949/30949)
remote: Total 102017 (delta 21303), reused 101873 (delta 21303)
Receiving objects: 100% (102017/102017), 18.79 MiB | 801.00 KiB/s, done.
Resolving deltas: 100% (65203/65203), done.
> Done update build meta repositories...

Welcome to Tizen Platform!
Please run `tp --help` to get more information.
```

`~/.tp` is the default directory for the `tp` tool. If you want to remove `~/.tp`, just delete it.

#### Update project meta data

```bash
tp init -u
```

```
- Updating meta data
> Update build meta repositories...
> Done update build meta repositories...
```

### Generate gbs config

```
Generate and update gbs configuration

Usage: tp config [PROJECT]

Arguments:
  [PROJECT]  Name of the project to configure

Options:
  -s, --snapshot  use fixed snapshot link instead of reference link (reference link is the link pointing to the last stable snapshot.)
  -h, --help      Print help
```

```bash
$ tp config
- update meta data
ssh://review.tizen.org:29418/scm/meta/qb
Already up to date.
? Enter the project name to view its information
> Tizen-Unified: public/TIZEN/Tizen/Tizen-Unified
```

```bash
Updating build metadata
> Update build meta repositories...
> Done update build meta repositories...
> Select project to view information Tizen-Unified: public/TIZEN/Tizen/Tizen-Unified
Generating GBS config at /home/tizen/.tp/gbs-configs/Tizen-Unified
Successfully updated GBS configuration

- supported architectures:
    - standard: armv7l aarch64 x86_64 riscv64
    - standard_gcov: armv7l
    - emulator: x86_64

- Usage: gbs -c <gbs config file> build -A <architecture> [options]

- examples:
    - gbs -c /home/tizen/.tp/gbs-configs/Tizen-Unified build -A armv7l [options]
    build with profile option
    - gbs -c /home/tizen/.tp/gbs-configs/Tizen-Unified build -A armv7l -P tizen-unified-standard [options]
    - gbs -c /home/tizen/.tp/gbs-configs/Tizen-Unified build -A armv7l -P tizen-unified-standard_gcov [options]
    - gbs -c /home/tizen/.tp/gbs-configs/Tizen-Unified build -A armv7l -P tizen-unified-emulator [options]
```

### Project Management

```
Manage projects

Usage: tp project <COMMAND>

Commands:
  list   List available projects
  setup  Set up local project from template
  build  Build project artifacts
  image  Manage project images
  help   Print this message or the help of the given subcommand(s)

Options:
  -h, --help  Print help
```

#### List all projects

```
List available projects

Usage: tp project list

Options:
  -h, --help  Print help
```

```
Tizen-Unified: public/TIZEN/Tizen/Tizen-Unified
Tizen-Base: public/TIZEN/Tizen/Tizen-Base
Tizen-9.0-Unified: public/TIZEN/Tizen-9.0/Tizen-9.0-Unified
Tizen-8.0-Unified: public/TIZEN/Tizen-8.0/Tizen-8.0-Unified
...
```

#### Setup local project

```
Set up local project from template

Usage: tp project setup [OPTIONS] --dest <DEST>

Options:
  -d, --dest <DEST>  Target directory for project setup
  -m, --meta <META>  Metadata template name
  -s, --snapshot     use fixed snapshot link instead of reference link (reference link is the link pointing to the last stable snapshot.)
  -h, --help         Print help
```

Example:

```bash
tp project setup -d Tizen-Unified -m public/TIZEN/Tizen/Tizen-Unified
```

```
$ tp project setup -d Tizen-Unified -m public/TIZEN/Tizen/Tizen-Unified
ssh://review.tizen.org:29418/scm/meta/qb
Already up to date.
Created directory: /home/tizen/Tizen-Unified
Cloning project...
Download source code...
/home/tizen/.tp/git-repo/repo init -u /home/tizen/.tp/meta/public -m TIZEN/Tizen/Tizen-Unified/manifest.xml --depth=1 --repo-url=/home/tizen/.tp/git-repo
Downloading Repo source from /home/tizen/.tp/git-repo
remote: Enumerating objects: 9086, done.
remote: Counting objects: 100% (9086/9086), done.
remote: Compressing objects: 100% (4159/4159), done.
remote: Total 9086 (delta 4845), reused 9086 (delta 4845)

Your identity is: Tizen Dev<tizendev@example.org>
If you want to change this, please re-run 'repo init' with --config-name

repo has been initialized in /home/tizen/Tizen-Unified
/home/tizen/.tp/git-repo/repo sync
Fetching: 52% (576/1107) 0:57 | 8 jobs | 0:27 platform/framework/web/chromium-efl @ platform/framework/web/chromium-ef

<...>

Checking out: 100% (1107/1107), done in 3m3.430s
repo sync has finished successfully.
Create gbs.conf file... to /home/tizen/Tizen-Unified/.gbs.conf

Now, You can build packages by running following command:
    # change directory to project root
    $ cd /home/tizen/Tizen-Unified

    # build all packages by running following command:
    # tp project build -d /home/tizen/Tizen-Unified

    # build specific package by running following command:
    $ gbs build -A <arch> <path_to_package>

    # If you need more options please refer `tp project build --help`

```

```
# after setup, you can find local project at Tizen-Unified
$ cd Tizen-Unified
$ ls
apps  gbs.conf  platform  profile  sdk  tools
```

For a full build, you can run `gbs build` in `Tizen-Unified`. Change the number of threads with the `--threads` option. The default is 1. The `gbs build` command supports building multiple packages in parallel:

```bash
$ gbs build -A armv7l --threads 4
```

Alternatively, use the `tp project build` command.

#### Project build

```
Build project artifacts

Usage: tp project build --dest <DEST>

Options:
  -d, --dest <DEST>  Build output directory
  -h, --help         Print help
```

```bash
$ cd Tizen-Unified
$ tp project build -d .
ssh://review.tizen.org:29418/scm/meta/qb
Already up to date.
Building local project...
.
check .gbs.conf for local project...
✅ .gbs.conf found in project root
check .repo directory for local project...
✅ .repo directory found in project root
? Select repository
  emulator
> standard
  standard_gcov
[↑↓ to move, enter to select, type to filter]
```

#### Project image

```
Manage project images

Usage: tp project image [OPTIONS] --dest <DEST>

Options:
  -d, --dest <DEST>      Output directory for generated images
  -a, --arch <ARCH>      Target architecture (armv7l, aarch64)
  -l, --list             List available base images
  -c, --create <CREATE>  Create specific image type
  -h, --help             Print help
```

##### List available images

```bash
tp project image --list --dest ~/Tizen-Unified
```

##### Create image

```bash
tp project image --create <image_type> --dest ~/Tizen-Unified
```

## External Packages Used by This Project

| Package  | URL                                                                        | License                                |
| -------- | -------------------------------------------------------------------------- | -------------------------------------- |
| git-repo | https://gerrit.googlesource.com/git-repo -b stable --single-branch `v2.53` | [Apache-2.0 license](external/LICENSE) |
