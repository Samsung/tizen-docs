Maintaining Tools Packages in Git
---------------------------------

### General

All Tizen Tools packages are to be maintained in Git (tizen.org),
utilizing the git-buildpackage tool. This provides, among other things:

-   proper version control / history tracking of all packages
-   consistent packaging and maintenance model of all packages

` easy to contribute to any package`\
` Git and OBS are always kept in sync`

-   clear separation of upstream and Tizen changes (for non-native
    packages)
-   proper packaging of Deb packages, without hacks

The OBS build infrastructure utilizes git-buildpackage
obs-source-service for exporting the packaging files automatically and
directly from Git. Mapping of Git branches to OBS projects is:

-   master -\> Tools
-   devel -\> Tools:Devel
-   release\* -\> Tools:Pre-release
-   test-<BRANCH> -\> home:tester:Tools-<PACKAGE>-test-<BRANCH>, where
    BRANCH is one of master, devel or release

The difference to the current scheme is not radically different, except
for NO changes to packages (package sources) should be done directly in
OBS. All changes are made in Git. Jenkins monitors Git and updates the
package in OBS automatically when some references are changed. Also,
native and non-native packages should be maintained in different ways,
similarly to Tizen 3.0.

### Converting packages to support git-buildpackage and obs-service-git-buildpackage

Short summary for requirements:

-   Git repository in tizen.org Gerrit
-   Jenkins job in tizen.org monitoring the corresponding Gerrit project
    (either a per-package job or the default job configured to track the
    repo)
-   git-buildpackage configuration (.gbp.conf) for the package

1\. Git repository

If the package does not yet have one, ask Eduard Bartosh to create it.
The repository name should match the name of the upstream repository
(non-native) or package name (native).

All tools packages should be under tools/ namespace in tizen.org Gerrit,
New git repositories should be created directly under tools/. We will
start moving existing repositories there soon.

2\. Jenkins job

2.1 3rd party and other \"simple\" packages There is now a default
jenkins job (Tools-Tester-Default) that is supposed to handle all
packages that do not need to track python unit test or coverage results.
That is especially all non-native (3rd party) packages in tiezn.org,
e.g. build, devscripts etc. For all of these packages the only
requirement is that the default job (Tools-Tester-Default) is configured
to monitor their Gerrit project.

2.2 Individual per-package jobs Only needed if you want to track python
unit test and/or coverage results, or, for some other reason to easily
monitor the package build history in Jenkins.

Basic Jenkins configuration is very easy, see the default job as an
example: JENKINS\_HOST/ci/job/Tools-Tester-Default/

In job configuration, you need to have at least:

-   Gerrit trigger -\> Dynamic trigger configuration configured
    correctly.

` you need to track the correct gerrit project, e.g. 'python-coverage'`\
` you need to track all relevant branches (i.e. 'master', 'devel', 'release*' and 'test-*')`

-   Build -\> Execute shell configured for the package (package name and
    git repo URL set correctly with \'-u\'), e.g.:

` /usr/bin/otc-tools-tester-run-test-kvm.sh python-coverage Tools -u HOSTNAME/python-coverage.git`

3\. Git and configuring git-buildpackage In order for git-buildpackage to
know how your package is maintained you need to create a .gbp.conf file
in the root directory of the source code tree. And, commit it into Git.

Remember that you need to have separate Git branches for each OBS
project, i.e. devel, release and master branches. You can have multiple
release branches, but a change to any of those will be submitted to OBS
Tools:Pre-release project.

3.1 Native packages This is very straightforward. You don\'t necessarily
need to change anything in the package. You only need to have one branch
(per OBS project) and necessarily no .gbp.conf.

You need to remove all Makefile etc. hacks from packaging, though. All
packaging files need to be exportable directly from Git without running
any generation/mangling scripts. You can test exporting RPM packaging
simply by running:

` $ git-buildpackage-rpm --git-ignore-branch --git-builder=osc --git-export-only --git-export-dir=`<export-dir>

Examples of native packages:

-   tizen.org/obs-service-git-buildpackage

3.2 Non-native packages Non-native packages must be maintained similarly
to non-native packages in Tizen-3.0. That is:

-   have separate upstream branch for upstream sources
-   upstream tags for upstream releases
-   patch-generation enabled

` However, git-buildpackage is more flexible than gbs in supporting different maintenance models so you need to explicitly configure it for each package.`

An example of .gbp.conf:

` [DEFAULT]`\
` # Set upstream tag format to v`<VERSION>\
` upstream-tag = v%(version)s`\
` # Enable patch generation`\
` patch-export = True`\
` # Don't generate patches out of changes to these files`\
` patch-export-ignore-path = (.gbp.conf|.gbs.conf|packaging/.*|debian/.*|.gitignore)`\
` # Directory for RPM packaging files`\
` packaging-dir = packaging`\
` # If there are multiple spec files and gbp cannot guess correctly`\
` spec-file = packaging/mypackage.spec`

You can test exporting the packaging files with git-buildpackage-rpm
similarly to native packages above.

Examples of already converted packages:

-   HOSTNAME/devscripts (RPM-only)
-   HOSTNAME/librpm-tizen (RPM + Debian)
-   HOSTNAME/python-coverage (RPM-only)
-   HOSTNAME/xdelta1 (RPM-only)

3.3 Debian packaging The OBS source service will automatically export
debian packaging files, too, if it finds debian/ directory in the source
tree. It utilizes the git-buildpackage (the non-rpm variant) and
dpkg-source tools to generate the debian packaging files. Thus, you need
to have proper Debian packaging (under debian/) if you want to build
your package for Deb-based distributions, i.e. Ubuntu in our case.

For non-native packages, you need to use the 1.0 Debian source package
format. For non-native Debian (1.0) packages no individual patches are
generated. Instead, a monolithic diff between the upstream tag and the
branch head is generated.

NOTE!: You need to remove all debian packaging files from the (rpm)
packaging/ directory! E.g. packaging/my-pkg.dsc. This is needed in order
to not confuse OBS.

NOTE-2!: You need to \"declare\" the package as non-native by having the
version field in debian/changelog following the format
<VERSION>-<REVISION>, e.g.:

` git-buildpackage (0.6.3-tizen20130822) unstable; urgency=low`

`   * Version bump to 0.6.3`

You can test exporting the Debian sources with git-buildpackage with:

` $ git-buildpackage --git-ignore-branch --git-no-hooks --git-export-dir=`<export-dir>` --git-purge --git-builder=dpkg-source -b .`

3.4 Testing in OBS You can test your package by using the test-devel
branch. See that the package builds and tests pass by checking the
results from the tester Jenkins job.

After you\'re satisfied, you can deploy the new packaging by just
pushing to the devel branch. Package in Tools:Devel will be
automatically updated (if Jenkins is correctly configured).

Maintaining packages with git-buildpackage
------------------------------------------

### General

This documentation contains some otctools specifics. The official
git-buildpackage documentation can be found here:

-   Debian tools:
    <http://honk.sigxcpu.org/projects/git-buildpackage/manual-html/gbp.html>
-   RPM tools: <http://marquiz.github.io/git-buildpackage-rpm/>

### Building packages

RPM: git-buildpackage-rpm Your package needs to be buildable with
git-buildpackage-rpm without virtually any command line options because
the source service is used (it calls git-buildpackage-rpm with basically
\--git-ignore-branch only). Thus, you just possibly need to do some
per-package configuration in .gbp.conf (e.g. upstream tag format,
packaging directory, pristine-tar on/off etc). After that building
locally is easy:

` $ git-buildpackage-rpm --git-ignore-branch`

By default, git-buildpackage-rpm refuses to build if you\'re not on the
main packaging/release branch (master by default), to avoid this you
need to use the \--git-ignore-branch option. You possibly want to set
this in your global config file (\~/.gbp.conf). Also, by default
git-buildpackage-rpm refuses to build if there are uncommitted changes -
see the \--ignore-new and \--ignore-untracked options.

For more details on the multitude of options please try:

` $ git-buildpackage-rpm --help`

Deb: git-buildpackage Building the Debian package with git-buildpackage
is basically similar to git-buildpackage-rpm: you need to have correct
package-specific configuration. Of course, you probably need to run it
inside a Debian-based Linux distribution if you want to test building
binary packages. In an RPM-based distribution you should be able to test
building the Deb source package if you just have the Debian devscripts
installed:

` $ git-buildpackage --git-ignore-branch --git-no-hooks --git-export-dir=../deb-build-area --git-purge --git-builder=dpkg-source -b .`

### Maintaining changelog(s)

Currently, there are separate tools for maintaining rpm and deb
changelogs. Hopefully, somewhere in the future, these could be combined
into one consolidated tool that would handle both at the same time.

RPM: git-rpm-ch git-rpm-ch is designed for updating the rpm changelog.
It can handle both separate .changes file or update the changelog
directly in the .spec file, but, we\'re interested in the former option
only. Currently, it doesn\'t handle changelog files in the \"openSUSE
format\" that osc produces.

git-rpm-ch tries to guess the range of commits which to include in the
new changelog section. You can use the \--since option to define the
exact start point.

One useful option is \--changelog-revision which defines the revision
field in the changelog header. It is a python format string which may
have the following keys:

-   \"%(upstreamversion)s\" the upstream version (Version: tag from the
    .spec file)
-   \"%(release)s\" rpm release/patchlevel (Release: tag from the .spec
    file)
-   \"%(epoch)s\" rpm epoch (Epoch: tag from the .spec file)
-   \"%(version)s\" the full rpm package version
-   \"%(vendor)s\" the distribution vendor from gbp configuration
-   \"%(tagname)s\" what git-describe gives you

` Using "%(tagname)s" is very nice because it makes git-rpm-ch always guess correctly.`

You can use the \--tag option to create release tags (a.k.a. packaging
tag in gbp terms). This will commit the changelog update (and all other
changes added to git index) and tag it. You can configure the packaging
tag format with \--packaging-tag. This is nice in because you will get
the correct tag name in the rpm changelog, too (assuming you use
\"\--changelog-revisio=%(tagname)s\"). If you need to re-tag (i.e.
overwrite the old tag because you changed something) later, you can use
git-buildpackage-rpm \--git-tag \--git-tag-only \--git-retag.

gbp-rpm-ch also detects some meta-tags from the commit messages:

-   \"Gbp-Rpm-Ch: <command>\" -- available commands:

`   "Ignore" ignore this commit from the changelog`\
`   "Full" use the full commit message instead of the header only`\
`   "Short" only use the header of this commit (for overriding the --full command line option)`

-   {Close\|Closes\|Fix\|Fixes}: <bts_reference>

` automatically picks these bug-tracking-system references to the commit message`

See \"git-rpm-ch \--help\" for more details about the multitude of
different options.

Deb: git-dchgit-dch is fairly similar to git-rpm-ch. Many of its options
are tightly tied with the Debian debchange tool. Some notable
differences are to git-rpm-ch are:

-   you should use \'\--release\' when releasing a new version
-   by default, git-dch only spawns an editor if you use \'\--release\'
-   no \--tag option

git-dch also detects some meta tags: \"Git-Dch: {Ignore\|Full\|Short}\"
\"Closes: <bts_reference>\" An example workflow for joint RPM-Deb
packaging

` $ # Edit source code`\
` ...`\
` $ # Build and test locally`\
` $ git-buildpackage-rpm`\
` ...`\
` $ # Update Debian changelog and stage the changes`\
` $ git-dch --release --since=HEAD~10`\
` $ git add debian/changelog`\
` $ # Update RPM changelog, commit and tag in one go`\
` $ git-rpm-ch --since=HEAD~10 --tag`\
` $ # Push change for review/testing`\
` $ # When merged, push the release tag, too`

### Example config files

\~/.gbp.conf (global configuration)

` [DEFAULT]`\
` # Don't fail if the current branch does not match the main packaging branch`\
` ignore-branch = True`

.gbp.conf (package-specific configuration)

` [DEFAULT]`\
` # Vendor/Distro name`\
` vendor = Tizen`\
` `\
` # Upstream tag (use "real" upstream release tags directly)`\
` upstream-tag = debian/%(version)s`

` # Don't use pristine-tar`\
` pristine-tar = False`

` # Tag format for releases`\
` packaging-tag = tizen/%(upstreamversion)s-%(nowtime)s`

` # Subdir for RPM packaging data`\
` packaging-dir = packaging`

` # Auto-generate patches against upstream`\
` patch-export = True`

` # Don't generate patches from changes in packaging or gbp config`\
` patch-export-ignore-path = (.gbp.conf|packaging/.*|debian/.*)`

` [git-rpm-ch]`\
` # Use a separate changelog file`\
` changelog-file=CHANGES`

` # Format for the revision field in RPM changelog`\
` changelog-revision = %(tagname)s`

[Category:Tool](Category:Tool "wikilink")
