## Environment

## Setting up Tizen Studio Installation Environment
- Prerequisites
    - You must install a Java Development Kit (JDK) 8 or higher to use the Tizen Studio.
    - [System requirements](https://developer.tizen.org/development/tizen-studio/download/installing-tizen-studio/prerequisites#java)
- [Download](https://developer.tizen.org/development/tizen-studio/download)

## Setting up Local Build Environment
- To build the tizen project, you need to install the command line tool `TS-CLI`.
- Only Ubuntu 64 bit is supported.
- To install `TS-CLI`, you need to install Nodejs.
- TS-CLI Download :  http://download.tizen.org/sdk/tizenstudio/opensrc/ts-cli_3.0.17_ubuntu-64.zip \
    ※ The latest version may be updated

```java
// install Nodejs
$ curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
$ sudo apt-get install -y nodejs

// install TS-CLI
$ unzip ts-cli_3.0.17_ubuntu-64.zip
$ mv ./data/dibs ${TS_CLI_PATH}

//install NPM
$ cd ${TS_CLI_PATH}
$ npm install
```
- TS-CLI manual
```text
This tool is command line interface for Tizen Studio develop
Usage: /usr/local/bin/node ./plugins/org.tizen.cli-tools/ts-cli.js <SUBCOMMAND> [OPTS]
Subcommands:
  build               Build a package
  full-build          Full build packages
  create-installer    Create Tizen Studio installer
  create-image        Create Tizen Studio image
  push                Push the packages to local repository
  pull                Pull the packages to local repository from remote repository server
  download            Download the packages to local from remote repository server
Subcommand usage:
  build               ts-cli build --repository <repository path> [--source <source path>] [--clean] [--push-package [--force]]
  full-build          ts-cli full-build --repository <repository path> [--source <source path>] [--clean] [--force] [--exclude <exclude path list>]
  create-instller     ts-cli create-installer --repository <repository path> --meta <meta package list> [--url <base repository URL>]
                             [--exclude-meta <meta package list>] [--title <Installer title>] [--output <installer name>]
  create-image        ts-cli create-image --repository <repository path> [--url <base repository URL>]
                             [--exclude-meta <meta package list>] [--skip-integrity] [--output <image name>]
  push                ts-cli push --package <package file path|list> --local-repo <repository path> [--force]
  pull                ts-cli pull --remote-repo <remote repository URL> --local-repo <repository path> [--force] [--os <os name | all>] [--base-snapshot <snapshot name>]
  download            ts-cli download --repository <repository path> --package <package file path|list> [--os <os name | all>] [--base-snapshot <snapshot name>]
 
Options:
  -h, --help            display help
  -c, --clean           clean build
  -p, --push-package    push the package(s) to local repository
  -P, --package         single package file path or package files with seperator comma. ex) -P test1.zip | -P test1.zip,test2.zip
  -f, --force           skip version comparison and push or pull packages by force. new packages will overwrite existing ones.
  -o, --os              os name ex) all | ubunut-32 | ubuntu-64 | windows-32 | windows-64 | macos-64
  -r, --repository      repository path. local directory path or http url. 
                        ex) ./repository/develop | http://download.tizen.org/sdk/tizenstudio/official
  -u, --url             url
  -s, --source          source path                                                                                                                       [default: "/home/jonghwan/mywork/dibs"]
  -x, --exclude         exclude path list
  -X, --exclude-meta    exclude meta list
  -M, --meta            meta list
  -S, --skip-integrity  check if dependent packages in repository exist or not
  -t, --title           installer title
  -O, --output          image or install output name
  -b, --base-snapshot   base snapshot name for package pull
  --rr, --remote-repo   remote repository url
  --lr, --local-repo    local repository path
```

