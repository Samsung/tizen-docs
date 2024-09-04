UI Design
---------

### cmdln options of mic create

One more command line option: \--runtime, valid values base on provided
plugins

Example::

` mic cr loop abc.ks [--runtime bootstrap]`

### config file

One more key in config file: runtime, value can be invalid in the case
corresponding plugin not available. The default value can be \"native\",
which is a special and basic runtime mode.

Add \[bootstrap\] subsection to save official repo url for creating
bootstrap Example::

` [create]`\
` ...`\
` runtime = bootstrap`\
` [bootstrap]`\
` bootstrap1_ID=BS1`\
` bootstrap1_repo1=...`\
` bootstrap1_repo2=...`\
` bootstrap1_rpmversion=4.8`\
` .`\
` .`\
` bootstrap2_ID=BS2`\
` bootstrap2_repo=...`\
` bootstrap2_rpmversion=4.9`

For bootstrap section, we would config several bootstrap using
bootstrapN\_\*, and each bootstrap, would contains ID, repo url, and
rpmversion. rpmversion is used to compare with ks file user specified to
create image.

### new subcommand of mic: runtime

This new subcommand: runtime, is for create/manage/cleanup runtime
environments for all the valid runtime plugins.

The command line options design as blow::

-   mic runtime listmode

` List all the supported runtime mode, e.g. boottrap, kvm. Decided by loaded`\
` plugins.`

-   mic runtime list \[-l\] {mode}

` List all available runtime environments of this {mode}, the {mode} is one of`\
` the supported runtime mode.`\
` All envs will be listed as folder path, and with a numbering prefix, like ::`

`   > 1 /var/tmp/mic/bootstrap/1.netbook-ia32`\
`     2 /var/tmp/mic/bootstrap/2.ivi-ia32`

` or for kvm ::`

`   > 1 /var/tmp/mic/kvm/1.netbook-ia32`

` The optional "> " prefix means the default selection to be used.`

` Optional "-l" is for more details, e.g. datetime of creation, datetime of`\
` last update, repos, etc.`

-   mic runtime create {mode} \<\--ks\|\--repo\|\--ID\>

` Create a runtime env for specified {mode}, and need to specify kickstart`\
` file by "--ks" or repo URL by "--repo", or bootstrap ID from config file.`

-   mic runtime clean {mode} \[number\]

` Clean up the exist runtime env of {mode}. User might need to specify the`\
` number of envs by argument, if multiple ones exist. W/o `<number>`, it should`\
` ask user to select which one to be cleaned up.`

-   mic runtime udpate {mode} \[number\]

` Update the specified runtime env of {mode}. If the [number] argument not`\
` specified, the default one will be updated, but w/ warning message if`\
` multiple ones exist.`

` After each update, the updated one will be selected as the default one by`\
` default.`

Some Ideas for Implementation
-----------------------------

As Chengui\'s original proposals, make the runtime level as a separate
daemon is not a good idea. Even making it as a separate process is also
not good enough. We need to keep the code and logic simple to avoid
unnecessary complicate.

Before the final design nailed down, several ideas from our discussion:

-   When re-launching \"mic\" in runtime env, we should avoid to modify
    current

command line string or configuration file. And we can this by the
following pseudo code ::

` if detect_current_runtime() == "native":`\
`   if opts.runmode == 'bootstrap':`\
`     do_the_steps_for_bootstrap`\
`     exit`\
`   elif opts.runmode == 'kvm':`\
`     do_the_steps_for_kvm`\
`     exit`

` # the following is the normal path`\
` ...`

-   We\'d better place all runtime envs files under the specified
    tmpdir, the /var/tmp/mic/ as the default.

<!-- -->

-   How to copy mic running code to runtime environment? It\'s not good
    enough

if we hard-coded the file path in code. Let\'s refer the method of
virtualenv tools, it\'s a nice solution.

-   Create a separate prj/repo only for mic bootstrap creation

<!-- -->

-   Basic workflow for bootstrap mode:

`   1. Check if any ready bootstrap env, if have continue, or goto 4`\
`   2. Check each bootstrap and get the rpmversion for each bootstrap, then`\
`      get the rpm version for target image, check if any bootstrap's rpm`\
`      version match with target image rpm vesion, if have, continue, or goto 4.`\
`   3. Use that bootstrap to create image, go to 5;`\
`   4. Check bootstrap section of config file, and select correct bootstrap info:`\
`      bootstrap_ID, bootstrap_repo, bootstrap_rpmversion, where target image rpm`\
`      version should match with bootstrap_rpmversion. Two choice here, one is`\
`      show waring to ask user to create bootstrap manually, bootstrap ID should`\
`      be show; another choise is create bootstrap directly. Then, goto 3;`\
`   5. finished`

[Category:Tool](Category:Tool "wikilink")
