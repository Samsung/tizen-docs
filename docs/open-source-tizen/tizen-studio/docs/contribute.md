# Contributing to Tizen Studio
Tizen Studio is an open-source project. 
We'd love for you to contribute to our source code and to make Tizen Studio even better than it is today! 

## **Issue Contributions:**
If your issue appears to be a bug, and hasn't been reported, open a new issue. 
Help us to maximize the effort we can spend fixing issues and adding new features, by not reporting duplicate issues. Providing the following information will increase the chances of your issue being dealt with quickly:
- Overview of the Issue [issue tracker](https://github.sec.samsung.net/RS-TizenStudio/home/issues)
- Motivation for or Use Case - explain why this is a bug for you
- Tizen Studio Version, Browsers and Operating System
- Suggest a Fix - if you can't fix the bug yourself, perhaps you can point to what might be causing the problem (line of code or commit)

## **Code Contributions:**
This section will guide you through the contribution process.

### Step 1 : Fork
Fork the project on GitHub and clone your fork locally.
```text
$ git clone git@github.com:username/xxxxxxx.git
$ cd node
$ git remote add upstream https://github.com/RS-TizenStudio/xxxx.git
```

### Step 2 : Branch
Make your changes in a new git branch:
```text
git checkout -b my-fix-branch master 
```

### Step 3 : Develop

- If you want to develop Tizen Studio Extension, please refer to the guide document.
    - [Package File Description Guide](/docs/coding-guild.md)
    - [Web/Navie IDE Extension Development Guide](web-extension-guide.md)
    - [Emulator Extension Development Guide](emulator-extension-guild.md)
    - [Meta Package Description Guide](docs/meta-package.md)
    
### Step 4 : Test / Build

Create your patch, including appropriate test cases.<br>
If you are adding functionality or fixing a bug, please add a test!<br>
Build your changes locally to ensure all the tests pass: 
- [Local Build Guilde](/docs/local-build.md)
- [Pacakge Installation Guide](docs/package-installation-guide.md)

### Step 5 : Commit
```text
$ git add my/changed/files
$ git commit
```

### Step 6 : Rebase
Use git rebase (not git merge) to synchronize your work with the main repository.
```text
$ git fetch upstream
$ git rebase upstream/master
```

### Step 7 : Push 
Push your branch to GitHub:
```text    
git push origin my-fix-branch
```
In GitHub, send a pull request to RS-TizenStudio:<my-fix-branch>. If we suggest changes, then:
- Make the required updates.
- Re-run the Tizen Studio test suite to ensure tests are still passing.
- Commit your changes to your branch (e.g. my-fix-branch).
- Push the changes to your GitHub repository (this will update your Pull Request).

### Step 8 : Review & Update

You will probably get feedback or requests for changes to your Pull Request.
This is a big part of the submission process so don't be discouraged!

To make changes to an existing Pull Request, make the changes to your branch.
When you push that branch to your fork, GitHub will automatically update the
Pull Request.

You can push more commits to your branch:

```text
$ git add my/changed/files
$ git commit
$ git push origin my-branch
```

Or you can rebase against master:

```text
$ git fetch --all
$ git rebase origin/master
$ git push --force-with-lease origin my-branch
```

Or you can amend the last commit (for example if you want to change the commit
log).

```text
$ git add any/changed/files
$ git commit --amend
$ git push --force-with-lease origin my-branch
```
