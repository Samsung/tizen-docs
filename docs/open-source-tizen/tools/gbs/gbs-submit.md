# gbs submit

Use the `gbs submit` subcommand to create or push tags to Gerrit. This triggers a code push from Gerrit to OBS.

For command usage details, enter:

```bash
$ gbs submit --help
```

Examples:

- Create a tag on a current working branch and submit it directly:

  ```bash
  $ gbs submit -m 'release for 0.1'
  ```

  GBS creates an annotated tag named "submit/${cur_branch_name}/${date}.${time}" on HEAD commit, and submits it directly.

- Use the `-c` option to submit a specific commit:

  ```bash
  $ gbs submit -c <commit_ID> -m 'release for 0.2'
  ```

- Use the `--target` option to specify the target version to submit:

  ```bash
  $ gbs submit --target=trunk -m 'release for 0.2.1'
  ```

  >  **Note**
  >
  >  The `--target` options allows you to specify the target version. By default, the version is `trunk`. The valid value of `--target` must be matched with the remote branch name. The backend service uses this branch information to create the SR and submit it to the correct OBS project.

- Use the `-r` option to specify the remote Gerrit server to submit. By default, the server is `origin`.

  ```bash
  $ gbs submit -r tizen:public/base/gcc -m 'release for 0.4'
  ```

- If your gpg key has been set, use the `-s` option to create a signed tag:

  ```bash
  $ gbs submit -m 'release for 0.3' -s
  ```
