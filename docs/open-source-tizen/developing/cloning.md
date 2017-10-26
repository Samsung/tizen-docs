# Cloning Tizen Source Files

You can clone Tizen source files over SSH or HTTPS.

> **Note**
>
> The procedures to clone Tizen source files over SSH and HTTPS are almost identical, the only difference being the URL in the Git command. However, you can only contribute code to Tizen using the SSH protocol.

Before cloning source files, study the following instructions:

- [Setting up the Development Environment](setting-up.md)
- [Installing Development Tools](installing.md)

## Cloning over SSH

You can clone source files over SSH, either for a specific project or for all Tizen projects.

To clone a specific project over SSH:

1. Confirm the package name by checking it on Tizen [Project List](https://review.tizen.org/gerrit/#/admin/projects/) or by running the following command:

   ```bash
   $ ssh review.tizen.org gerrit ls-projects
   ```

2. Clone the required package:

   ```bash
   $ git clone [-b <Branch>] ssh://<Username>@review.tizen.org:29418/<Gerrit_Project> [<Local_Project>]
   ```

   For example:

   ```bash
   $ git clone ssh://<Username>@review.tizen.org:29418/platform/core/account/account-common
   ```

To clone all Tizen projects over SSH, see [Cloning All Projects over SSH](building-all.md#cloning-all-projects-over-ssh).

## Cloning over HTTPS

You can clone source files over HTTPS, either for a specific project or for all Tizen projects.

To clone a specific project over HTTPS:

1. Clone the required package:

   ```bash
   $ git clone [-b <Branch>] https://git.tizen.org/cgit/<Gerrit_Project> [<Local_Project>]
   ```

   For example:

   ```bash
   $ git clone https://git.tizen.org/cgit/platform/core/multimedia/avsystem
   ```

To clone all Tizen projects over HTTPS, see [Cloning All Projects over HTTPS](building-all.md#cloning-all-projects-over-https).
