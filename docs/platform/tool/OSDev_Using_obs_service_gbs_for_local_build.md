This guide describes using sources and building packages using
[OBS](OBS "wikilink") source service *gbs*.

Installing prerequisites
========================

By default *osc* cannot checkout sources referenced through *gbs*
service. For it to work following packages have to be installed:

-   [obs-service-gbs](https://github.com/01org/obs-service-gbs)

`git clone `[`https://github.com/01org/obs-service-gbs.git`](https://github.com/01org/obs-service-gbs.git)\
`cd obs-service-gbs`\
`python setup.py build`\
`sudo python setup.py install`

-   [obs-service-gbp](https://github.com/01org/obs-service-git-buildpackage)

`git clone `[`https://github.com/01org/obs-service-git-buildpackage.git`](https://github.com/01org/obs-service-git-buildpackage.git)\
`cd obs-service-git-buildpackage`\
`python setup.py build`\
`sudo python setup.py install`

Configuring services
====================

To make services work without root privileges, cache directories have to
be changed. Edit files /etc/obs/services/gbs and
/etc/obs/services/git-buildpackage. Uncomment string containing
repo-cache-dir and change it to place where your user have rights to
write to (/var/tmp for example):

`repo-cache-dir = /var/tmp/git-buildpackage-repos/`

This string can be the same in both files.

Checking out sources and building
=================================

Now you can run command in package directory

`osc service run`

to prepare sources for building and normally run

`osc build $REPO $ARCH`

to build package.

Known issues
============

Multiple .spec files in repo
----------------------------

If you have following error:

`Multiple build description files found:`

build can be fixed by adding one of .spec files as additional parameter
to command line:

`osc build $REPO $ARCH $name.spec`

Upstream branch problem
-----------------------

Following error:

`error: Start commit '*' not an ancestor of end commit '*'`\
`error: Generating upstream tarball and/or generating patches failed. GBS tried this as you have upstream branch in you git tree. Fix the problem by either:`\
`  1. Update your upstream branch and/or fix the spec file. Also, check the upstream tag format.`\
`  2. Remove or rename the upstream branch (change the package to native)`\
`See `[`https://source.tizen.org/documentation/reference/git-build-system/upstream-package`](https://source.tizen.org/documentation/reference/git-build-system/upstream-package)` for more details.`\
`source_service:error: GBS export failed: `<gbs>`Failed to export packaging files from git tree`

caused by upstream branch in git source tree can be fixes by applying
patch to *obs\_service\_gbs*. In file *command.py* in string containing
*no\_patch\_export* change *None* to *1*:

`...`\
`'source_rpm': None,`\
*`'no_patch_export':`` ``1,`*\
`'upstream_branch': None,`\
`...`

Then rebuild and install *obs\_service\_gbs* (step [\#Installing
prerequisites](#Installing_prerequisites "wikilink"))

Configuring ssh
---------------

Errors, caused by ssh:

`source_service:error: RepoCache: Failed to fetch from remote: Error running git fetch: ssh: connect to host review.tizen.org port 22: Connection timed out`\
`fatal: Could not read from remote repository.`\
\
`Please make sure you have the correct access rights`\
`and the repository exists.`

or

`source_service:error: RepoCache: Failed to fetch from remote: Error running git fetch: Permission denied (publickey).`\
`fatal: Could not read from remote repository.`\
\
`Please make sure you have the correct access rights`\
`and the repository exists.`

can be fixed by changing /etc/ssh/ssh\_config file. Add following lines
before **Host \***:

`Host review.tizen.org`\
` IdentityFile /path/to/your/ssh/key`\
` Port 29418`\
` User $username`

[Category:Tool](Category:Tool "wikilink")
