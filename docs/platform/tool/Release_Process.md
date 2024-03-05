Introduction

Intruction
----------

This document describe basic process for Tizen Tools Release.

Currently, this document only apply for
[GBS](GBS "wikilink")/[MIC](MIC "wikilink"). jenkin-job/IRIS can be
added in the future.

This document cover release process, start point is release branch for
for pre-release version has been created, and the final point is new
tools have been deployed on server and latest repo has been published to
external download.tizen.org/tools.

This document will cover the following content:

` - Roles Defination`\
` - Pre-Release testing & development`\
` - Internal Release & Testing`\
` - Pre-deployment Testing`\
` - Deployment`\
` - Publish to external repository server`\
` - Sync internal code to external github and tizen.org`\
` - Send announcement to mailling list`

The drivers of the whole release process are the maintainer of GBS/MIC,
that means they should control & assign different AR to different people
on different stages.

Roles Defination
----------------

:   Developer: Tools developer, responsible for features development and
    bug fix
:   Maintainer: Responsible for defining roadmap, control release
    process.Developer take this maintainer role in our case.
:   Tester: Responsible for doing feature/bug/system/pre-depolyment
    testing
:   Admin: Responsible for accepting deployment tickets and deploying
    tools on backend server

Pre-release testing & development
---------------------------------

0\. Discuss next release contents (Roadmap) with Admin: which tickets
will before included in this release, reach agreement before taking
further actions.Do a final check before taking in use ppfarm, in case
the review happened at the beginning of the development cycle, to ensure
that no changes to the initial plan went untracked.

1\. Maintainer create \'release\*\' branch and bump to RC release

:   

    :   

` $ git checkout devel`\
` $ update packaging/${mic,gbs}.spec and debian/changelog to bump to rc1`\
` $ submit to gerrit`\
` $ git push origin HEAD:refs/heads/release-{version} # create release branch`

2\. Maintainer notify tester to do pre-release testing

`  Details Input:`\
`  1) Which tools repo should be tested?`\
`  2) Which types of testing should be done? eg: upgrade/install/full system testing.`\
`  3) How long time test should be taken?`\
`  4) Email to tester to do testing, if no response in five minutes,push F2F directly`

3\. Tester test tools in corresponding live repo:

`  Details Output:`\
`  1) Reply testing request email. Communicate with developer about the testing time, make sure test report can be finished in time;`\
`  2) Finish Test report in Jenkins testing job`\
`  3) Basic summary of testing report, it's better to give basic analysis and root cause it.`\
`  4) Send email to developer/Maintainer, if no response from maintainer, push developer F2F directly`

4\. Developer/Maintainer Review test report:

`  1) If some issues found, submit hotfix and bump to new RC version`\
`        goto 2;`\
`  2) If no issue found, bump to official version after the following`\
`      checking:`\
`      ::`\
`         New version information`\
`         New release notes content verification`

Internal Release
----------------

1\. Maintainer update \'master\' branch using \'release-\*\' branch and
create tag

`  $ git checkout release-${version}`\
`  $ git tag ${version} -m "release for ${version}"`\
`  $ git push --tags origin`\
`  $ git push origin releaes-${version}:refs/heads/master -f --tags`

2\. Maintainer trigger

``   `https:// ``<jenkins>`` /job/Tools-release/` job to publish Tools live repo to internal staging repo:  ``[`https://`](https://)<internal>`/staging/tools/.`

`  The following testing should base on this staging repo`

3\. Developer notify tester to do internal release testing

`  Details Input:`\
``   1) Which types of testing should be done? upgrade/install/full system testing. For gbs `local full build testing` is needed ``\
`  2) How long time test should be taken?`\
`  3) Email to tester to do testing, if no response in five mins, push F2F directly`

4\. Tester test tools in corresponding internal staging repo:

`  1) Reply testing request email. Communicate with developer about then testing time, make sure test report can be finished in time`\
`  2) Finish Test report in Jenkins testing job`\
`  3) Basic summary of testing report, it's better to give basic analysis and root cause it`\
`  4) Send email to developer/Maintainer, if no response, push developer F2F directly`

5\. Developer/Maintainer Review test report:

`  1) If some source issues found, bump to new release version and continue to fix it in 'release-*' branch, then goto pre-release testing`\
`  2) if some 3rd part dependency issue found, fix them in Tools project directly then goto 2`

6\. Maintainer ensures that all the new code is compliant with Intel

`  Publishing policies:`\
`  1) licenses are in place and compatible`\
`  2) if new components are present, they have been approved by Legal PDT`\
`  3) new code has been checked with the scanning tool and all problems are`\
`    fixed`

7\. Maintainer creates external archive repo using staging repo

Pre-Deployment Testing
----------------------

All pre-deployment testing are based on external archive repo.

### GBS

Pre-deployment testing should be done in ppfarm test environment.

Tester need following these steps:

1\. Sync code from tizen.org \`Tizen:IVI\` project to ppfarm OBS.

`  1)Login build-pptest host, run:`\
`    #!/bin/bash`\
``     for pkg in `osc -A  ``[`https://build-pptest.fi.intel.com:444`](https://build-pptest.fi.intel.com:444)``  ls tizen.org:Tizen:IVI`; ``\
`    do`\
`      osc -A `[`https://build-pptest.fi.intel.com:444`](https://build-pptest.fi.intel.com:444)` copypac tizen.org:Tizen:IVI $pkg  Tizen:IVI`\
`      sleep 1`\
`      osc -A `[`https://build-pptest.fi.intel.com:444`](https://build-pptest.fi.intel.com:444)` service remoterun Tizen:IVI $pkg`\
`    done`\
`   `\
`   2)Re-copypac broken packages:`\
``      for pkg in `osc -A  ``[`https://build-pptest.fi.intel.com:444`](https://build-pptest.fi.intel.com:444)``  prjresults -c -s B Tizen:IVI | cut -d\; -f1`; ``\
`     do`\
`       osc -A `[`https://build-pptest.fi.intel.com:444`](https://build-pptest.fi.intel.com:444)` copypac tizen.org:Tizen:IVI $pkg Tizen:IVI`\
`       sleep 1`\
`       osc -A `[`https://build-pptest.fi.intel.com:444`](https://build-pptest.fi.intel.com:444)` service remoterun Tizen:IVI $pkg`\
`     done`

2\. Monitor GBS-Test:Tizen:IVI project and wait it build succeeded.

3\. Check the following jenkins job.

GBS-Test:Tizen:IVI project build will trigger the following jobs:

` - create-snapshot`\
` - image-creator`\
` - image-tester`

GBS Tester need find the build report at image-tester job.

### MIC

MIC is deployed as a mic-appliance, so pre-deployment test should be
done as an appliance

1\. Build a mic-appliance with the latest release(Instructions required -
PUT THE PACKER SCRIPTS AND TEMPLATE UNDER MIC PROJECT)

2\. Upload new mic-appliance to otctools server. Use jenkins job
(https://<jenkins>/job/MIC-appliance-release/),choose download.otctools
and provide a URL. (JENKINS JOB not available yet on tizen)

3\. Test on ppfarm. Provide the mic-appliance location URL on
download.otctools to ppfarm jenkins, and ask Maintainer to trigger test.

4\. Use the same jenkins job as step4 (choose download.tizen.org as
destination) to sync the new mic-appliance to tizen.org.

Deployment
----------

1\. Maintainer creates/updates deployment ticket, assigns it to reviewer.

`  The ticket must include:`\
`  1) deployment instructions (repos, user ids, ets)`\
`  2) simple means for Admin to confirm that the deployment appears successful`\
`  3) rollback instructions, to follow in case the deployment fails`\
`    (refer only to data/packages from repos - no local data backup)`\
`    In case the deployment affects also data/configurations stored somewhere,`\
`    these too must be included in the rollback.`

2\. Prepare \"Release notes\" for testing results verification

`  Release Notes must contain:`\
`  1) Content description (bugs & features delivered)`\
`     For each bugfix and feature included in the release, the corresponding`\
`     tracker must be adequately updated:`\
`     - description of the bug/feature`\
`     - means of verification and expected results`\
`     - results effectively obtained from testing`\
`  2) Statement that the code is compliant with Intel legal requirements`\
`     - link to scanning results for new code`\
`     - statement that new components (if any) are approved by Legal PDT,`\
`      if needed - this includes also using 3rd party code with different license.`\
`  3) Links to build & verification chain:`\
`     OBS -> jenkins image(s) creation and validation`

3\. Notify reviewer that deployment ticket release notes are ready for
review.

4\. After release note review, reviewer transfer the ticket to Admin.
Different test report must be listed in email.

`  1) GBS`\
`    - gbs local full build report`\
`    - ppfarm 'image-tester' job report`\
`    - gbs install&&upgrade report`\
`    - itest cases report`\
`    -  deploy ticket link`

`  2) MIC`\
`    - ppfarm pre-deployment 'image-tester' job report`\
`    - mic install&&upgrade report`\
`    - itest cases report`\
`    - deploy ticket link`

5\. Admin deployment tools follow corresponding tickets.

6\. Maintainer check the final results and close the tickets finally.

7\. Update Tools-Announcement:

`  `[`https://wiki.tizen.org/wiki/GBS#Tools_Announcement`](https://wiki.tizen.org/wiki/GBS#Tools_Announcement)

Publish release
---------------

1\. Developer/Maintainer monitor status of deployment ticket

2\. If ticket has been closed, that means deployment work has been done

3\. Developer/Maintainer trigger release jenkins job to publish repo to
external latest-release folder

Sync latest code to external github
-----------------------------------

### github

`  $ cd path/to/{gbs,mic}`\
`  $ git push github:01org/{gbs,mic} release-xx:release-0.xx --tags`\
`  $ git push github:01org/{gbs,mic} master:master`

Sync latest code to external github
-----------------------------------

Once repo has been published, Super maintainer responsible for sending
annoucement to the following mailing list:

`  - general@lists.tizen.org`\
`  - dev@lists.tizen.org`\
`  - operations@lists.tizendev.org`

[Category:Tool](Category:Tool "wikilink")
