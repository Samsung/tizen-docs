# Web Device API submodule

This repository contains the submodule ***docs/application/web/api/web-device-api***, which keeps current state of related repository used for generation of API reference html files (*\<version>/device_api/\<profile>/tizen/\<module>.html*).

**Content of \<version> directories should not be modified by hand.**

For using submodule you need to be a Samsung employee and have own SPIN server account with proper permissions. If you don't have access to submodule, you are still allowed to refer to html files directly.

## Usage of submodule after cloning the repository:
1. Directory *docs/application/web/api/web-device-api* will be empty initially, to access the content you need to use below command to initialize a submodule repository.

        git submodule update --init --recursive
___
**Important:** to properly gather the content of submodule your user name should be the same as your SPIN account name. In other cases you need to modify url in .gitmodules file to provide user name by hand.

ssh://165.213.149.170:29418/doc/web-device-api &rightarrow; ssh://\<username>@165.213.149.170:29418/doc/web-device-api
___

2. Submodule will be fetched.
3. After entering the direcotry of submodule, all *git* commands refer to submodule repository, after leaving it, commands refer to tizen-docs repo.

## Generation of latest API reference
1. Go to *docs/application/web/api/web-device-api* submodule.
2. Checkout commit to new HEAD commit with *git checkout* command, e.g.:

        git checkout tizen
        git pull
3. Generate docs directly into tizen-docs directories structure (for all versions and profiles), use below command. For more options refer to help of generate.sh script.

        ./generate.sh -a -t

4. Directory docs/application/web/api/ will be updated to latest version generated based on checkouted commit of web-device-api submodule.
5. Check the results of generation and then use 'git add' command to include changes.
6. On change list you will see also new commits in web-device-api. Add updated commits in web-device-api submodule and commit them also.


## Workflow of doing a change in Web API reference
1. Prepare commit for web-device-api submodule and push it to remote repository of submodule.
2. Change need to be reviewed and merged by maintainers.
3. [Generate html files](#generation-of-latest-api-reference) after merging.
4. Prepare commit for tizen-docs repository including newly generated files and updating HEAD of submodule to latest one.
5. Push and create Pull Request for tizen-docs repository.
___
Important: Be aware of updating submodule HEAD to not merged commits. This will be allowed by git, but the repository could not be downloaded by other user.
___
