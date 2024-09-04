The purpose of this page is to explain how to
[Maintain](Maintain "wikilink") packages by updating to new versions
according to various situations.

Chart
=====

![Updating packages
chart](Updating-packages-medium.png "Updating packages chart")

Source:
[updating-packages.svg](https://drive.google.com/file/d/0B5ClyE_v6LT1SDAyNF9rckVTMkE/view?usp=sharing)

Steps
=====

1. Clone project
----------------

`git clone review.tizen.org:`<project>

2. Use git
----------

Add the remote repository:

`git remote add upstream `<repo-url>

Fetch the sources:

`git fetch --all`\
`git checkout -b upstream-git upstream/master`

Upload them to tizen :

`git push origin upstream-git:upstream-git`

Or

`git push origin upstream-git:sandbox/$USER/upstream-git`

Update packaging :

Add a local .gbs.conf file (if it doesn\'t exist):

    [general]
    upstream_branch = upstream-git
    upstream_tag = ${upstreamversion}

This one is assuming tags from upstream are matching version numbers, it
can be adjusted, for example, if the upsteam tag uses the form
\"v<version>\" the .gbs.conf becomes:

    [general]
    upstream_branch = upstream-git
    upstream_tag = v${upstreamversion}

Alternatively you can tag the revision you want to use as the base of
the Tizen package (in this case you don\'t need a local .gbs.conf):

`git tag upstream/`<new-version>` [`<commit>`/`<upstream-tag>`]`

Rebase the tizen branch atop of the new upstream version; using the
\"-i\" option allows you to ditch non-needed commits:

`git rebase -i `<new-version>

Check example :

<https://review.tizen.org/gerrit/#/c/32102/2>

You can also insert a \"pseudo meta information\" to mention the
upstream\'s repo in the spec file, for example:

`#X-Vcs-Url:     `[`git://git.%{name}.org/%{name}`](git://git.%%7Bname%7D.org/%%7Bname%7D)

(https://review.tizen.org/gerrit/\#/c/29574/1/packaging/rsync.spec)

Maybe this information could move to a new standardized meta data
file\...

### Using gitmodules

Git in git (\~ svn externals) used for common code among projects

Commit this script in packaging subfolder :

-   <https://gitorious.org/tizen/tizen-helper/raw/master:bin/gitmodules.sh>

Usage :

` git rebase -i ${upstream_tag} # ie v1.2.3 keep only changes from tizen branch`\
` sh packaging/gitmodules.sh `\
` git commit -sam 'packaging: gitmodules refresh' packaging/*.tar.bz2`

References :

-   <https://review.tizen.org/gerrit/gitweb?p=platform/upstream/gstreamer-vaapi.git;a=summary>

See page 29 :

-   <http://www.slideshare.net/rzrfreefr/tizen-upstreamcooptdc2014pcoval#>
    p29

3. Use tarball
--------------

Download the tarball of the version of the package you want to update.

Import it in the git tree:

`git checkout `<upstream-branch-name>\
`gbs import `<tarball>

Rebase the tizen branch:

`git checkout tizen`\
`git rebase upstream/`<version>

4. Local build & push sandbox
-----------------------------

**Update the package version in the spec file**

`grep Version packaging/*.spec`

**Test your changes locally and make the appropriate changes for the
package to build.** Note that when switching from a tarball source to a
git one, it is generally needed to generate the configure files
(configure, Makefile.in\...) which aren\'t provided in the git (but are
provided in the tarball). The preferred way to generate those files is
to do it in the spec file (for example by replacing \"%configure\" with
\"%reconfigure\" or calling the bootstrap script provided).

Commit your changes:

`git commit -as`

Push your branch in your sandbox:

`git push origin HEAD:sandbox/`<your-gerrit-id>`/`<remote-branch-name>

\"<remote-branch-name>\" can be anything you want.

5. Make corrections
-------------------

If the packages fails to build in the OBS or break other packages, fix
them (or alert the maintainers of the broken packages to get their
help).

6. Push (for maintainers)
-------------------------

Check this page for Maintainer\'s tasks :

<https://wiki.tizen.org/wiki/Maintain>

**If the build doesn\'t break anything (this needs to be tested with an
OBS), you can push the changes in the git repository.**

If the tizen branch wasn\'t using the upstream branch, rename it and
create a new tizen branch :

`git branch -m tizen previous/tizen`\
`git checkout -b tizen`

Push your work:

`git push -f`\
`git push --tags`

Then submit the package to be released in repo using \"gbs sr\":

`profile=tizen_common`\
`gbs sr -t ${profile}`

Extra : make sure you\'re pushing the right tag if not you need to
delete to remote (and local) tag (see hints :
<https://bugs.tizen.org/jira/browse/TC-2015> )

FAQ
===

What if the package to update needs another package to be updated ?
-------------------------------------------------------------------

-   If no bug report regarding the package to update has been opened,
    open one.
-   Mark this bug as blocking the update of your package.

What if the new updated package requires a new dependency ?
-----------------------------------------------------------

-   Open a bug in Jira requesting for this new package to be added to
    the Tizen project. Please also specify the version needed.
-   Mark this bug as blocking the update of your package.

What if the updated package breaks a package that depends on it ?
-----------------------------------------------------------------

-   Open a bug in Jira and provides the logs and the sandbox containing
    the updated package so anyone can reproduce the error.

LINKS
=====

-   <http://www.slideshare.net/rzrfreefr/tizen-upstreamcooptdc2014pcoval>
-   <https://wiki.tizen.org/wiki/Talk:Packaging/Guidelines>

[Category:Development](Category:Development "wikilink")
[Category:Platform](Category:Platform "wikilink")
[Category:Platform\_Development](Category:Platform_Development "wikilink")
[Category:Tool](Category:Tool "wikilink")
