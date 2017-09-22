# gbs submit

gbs submit can help the user create/push tags to gerrit, which would trigger pushing code from gerrit to OBS. You can get the usage of subcommand submit by:

  ```bash
$ gbs submit --help
  ```

### Examples

1. Create a tag on a current working branch and submit it directly.

  ```bash
  $ gbs submit -m 'release for 0.1'
  ```

GBS would create an annotated tag named 'submit/${cur_branch_name}'/${date}.${time} on 'HEAD' commit, then submit it directly.

1. Use -c option to submit specified commit

  ```bash
  $ gbs submit -c <commit_ID> -m 'release for 0.2'
  ```

2. Use '--target' option to specify the target version to submit

  ```bash
  $ gbs submit --target=trunk -m 'release for 0.2.1'
  ```

  >  **Note**
  >  --target allows the user to specify the target version. By default, it is 'trunk'. The valid value of --target should be matched with the remote branch name. The backend service would use this branch info to create the SR and submit it to the correct OBS project.

3. use -r to specify remote gerrit server to submit. By default '-r' is 'origin'.

  ```bash
  $ gbs submit -r tizen:public/base/gcc -m 'release for 0.4'
  ```

4. If your gpg key has been set, you can use '-s' to create a signed tag.

  ```bash
  $ gbs submit -m 'release for 0.3' -s
  ```

