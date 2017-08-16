# Cloning Tizen Sources Files

This topic provides information on how to clone Tizen source files, either over SSH or HTTPS .

**Note:** The procedures to clone Tizen source files over SSH and HTTPS are almost identical. The only difference is the URL in the git command. However, you can only contribute code to Tizen using the SSH protocol.

You must read, understand, and correctly follow the instructions in the following documents before cloning:

- [Setting up Development Environment](https://source.tizen.org/documentation/developer-guide/environment-setup)
- [Installing Development Tools](https://source.tizen.org/documentation/developer-guide/step-step-instructions/installing-development-tools)

## Cloning over SSH

You can clone source files over SSH, either for a specific project or for all Tizen projects.

### Cloning a Specific Project over SSH

To clone a specific project over SSH:

1. Confirm the package name by checking it on Tizen [Project List](https://review.tizen.org/gerrit/#/admin/projects/) or by running the following command:

   ```
   $ ssh review.tizen.org gerrit ls-projects
   ```

2. Clone the required package:

   ```
   $ git clone [-b <Branch>] ssh://<Username>@review.tizen.org:29418/<Gerrit_Project> [<Local_Project>]
   ```

   For example:

   ```
   $ git clone ssh://<Username>@review.tizen.org:29418/platform/core/account/account-common
   ```

### Cloning All Tizen Projects over SSH

To clone all Tizen projects over SSH, see [Cloning All Projects over SSH](https://source.tizen.org/documentation/developer-guide/getting-started-guide/building-all-packages-locally-gbs).

## Cloning over HTTPS

You can clone source files over HTTPS, either for a specific project or for all Tizen projects.

### Cloning a Specific Project over HTTPS

To clone a specific project over HTTPS:

1. Clone the required package:

   ```
   $ git clone [-b <Branch>] https://git.tizen.org/cgit/<Gerrit_Project> [<Local_Project>]
   ```

   For example:

   ```
   $ git clone https://git.tizen.org/cgit/platform/core/multimedia/avsystem
   ```

### Cloning All Tizen Projects over HTTPS

To clone all Tizen projects over HTTPS, see [Cloning All Projects over HTTPS](https://source.tizen.org/documentation/developer-guide/getting-started-guide/building-all-packages-locally-gbs).