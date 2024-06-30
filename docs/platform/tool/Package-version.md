Package versioning
------------------

Purpose of this page is to collect versioning practices, used in
different projects and come up with equal package versioning policy.
After that policy should be put into
[Development\_and\_release\_process](Jenkins-development-workflow-ppt "wikilink")
and become a requirement for all our projects.

### git-buildpackage, xdelta, pristine-tar

RPM packaging

Currently, the upstream version number is used directly and OBS handles
setting the Release tag.

This has a clear drawback: the package version numbers are not in sync
between Tools:Devel, Tools:Pre-release and Tools projects in OBS.

Debian packaging

The packages are changed to \"non-native\" by changing the version
number in debian/changelog - i.e. appending a \"revision\" field to the
version number.

E.g. if the original entry from upstream has \"git-buildpackage (0.6.6)
unstable; urgency=low\", this will be first in devel branch changed to
something like:

` git-buildpackage (0.6.6-tizen20131107) UNRELEASED; urgency=low`

Then, before doing a release the changelog is updated (along with the
version number) to something like:

` git-buildpackage (0.6.6-tizen20131127) unstable; urgency=low`

### mic, gbs, depanneur

RPM packaging

-   version bump rules

<!-- -->

-   rc release

`   Version:        0.19`\
`   Release:        0.rc1.`<CI_CNT>`.`<B_CNT>

-   official release

`   Version:        0.19`\
`   Release:        1`

Debian packaging

-   rc release

`   gbs(0.19~rc1) UNRELEASED; urgency=low`

Note: We need use \'\~\' instead of \'-\' during rc release, because
gbp-service will consider \'-\' as an none native package during
packaging to OBS. MIC and GBS need follow this rule.

-   official release

`   gbs(0.19) stable; urgency=low`

### Services project. jenkins-\[scripts, jobs, plugins\] packages

Note, that this project doesn\'t use Debian packages as OpenSUSE is the
only target distro at the moment.

RPM versions

Devel branch:
-------------

Version in devel branch is <version>-0.dev.<CI_CNT>.<B_CNT> for OpenSUSE
and <version>-0.dev for the rest of rpm distros Here is what we have in
the spec to achieve this:

` Version:        0.15`\
` %if 0%{?opensuse_bs}`\
` Release:        0.dev.`<CI_CNT>`.`<B_CNT>\
` %else`\
` Release:        0`\
` %endif`

release- branches
-----------------

Version in release branches is <version>-1.<CI_CNT>.<B_CNT> for OpenSUSE
and <version>-1 for the rest of rpm distros Here is what we have in the
spec to achieve this: Version: 0.14

` %if 0%{?opensuse_bs}`\
` Release:        1.`<CI_CNT>`.`<B_CNT>\
` %else`\
` Release:        1`\
` %endif`

Workflow

`1.Version is set to `<version>`-0.dev.`<CI_CNT>`.`<B_CNT>` in devel`\
`2.release-`<number>` branch is created when code in devel is feature complete and ready for the release or work for the next release is about to start in devel.`\
`3.Immediately after release branch is created`\
`  1.Version in devel is incremented to <version+1>-0.dev.`<CI_CNT>`.`<B_CNT>\
`  2.Version in release branch is changed to `<version>`-1.`<CI_CNT>`.`<B_CNT>`, so it's always higher than `<version>`-0.dev.`<CI_CNT>`.`<B_CNT>\
`4.Bugfix releases go to the same release branch. Bugfix number is added to the version, for example version 1.2-1.`<CI_CNT>`.`<B_CNT>` becomes 1.2.1-1.`<CI_CNT>`.`<B_CNT>` for the first bugfix release, 1.2.2-1.`<CI_CNT>`.`<B_CNT>` for the second bugfix release and so on.`\
`5.When release is done it's tagged and master branch reseted to the tag, so master branch always points to the latest released code`

OBS source services: obs-service-git-buildpackage, obs-service-gbs

NOTE! these projects are only built for openSUSE.

The Release tag is dependent on the release status. From spec file, in
development phase:

` # Set to 0 if "normal release" `\
` %define pre_release 0pre1`\
` Version:        0.4`\
` %if 0%{?opensuse_bs} && "%{pre_release}" != "0" `\
` Release:        %{pre_release}.`<CI_CNT>`.`<B_CNT>\
` %else`\
` Release:        %{pre_release}`\
` %endif`

When doing a release %pre\_release is changed from 0preX to 0. Thus, the
package (full) version is changed from e.g. 0.4-0pre1.3.2 to 0.4-4.1
when building in OBS

[Category:Tool](Category:Tool "wikilink")
