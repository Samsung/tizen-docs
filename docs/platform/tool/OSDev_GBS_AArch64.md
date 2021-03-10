Using GBS tool for AArch64 build
================================

Please be noticed that project is now stabilizing and may be
inconsistent and fail builds, so please check project config from time
to time until project is declared stable. This page only shows how to
configure GBS tool for AArch64 build, if you want full manual please
refer to [gbs
page](https://source.tizen.org/documentation/reference/git-build-system)

Configuration
-------------

To use aarch64 build you need to add AArch64 repositories to your
gbs.conf file and get a project config to use

### gbs.conf

`[profile.aarch64]`\
`buildconf = ${work_dir}/tizen-conf/aarch64_build.conf`\
`obs = obs.tizen`\
`repos = repo.tizen_aarch64`

`[obs.tizen]`\
`url = `[`https://api.tizen.org`](https://api.tizen.org)\
`user = xxxx`\
`passwd = xxxx`

`[repo.tizen_aarch64]`\
`url = `[`https://download.tizen.org/live/devel:/arm_toolchain:/Mobile:/Tizen_Common/arm64-wayland`](https://download.tizen.org/live/devel:/arm_toolchain:/Mobile:/Tizen_Common/arm64-wayland)

### project config

As AArch64 project is not officially released yet, project config is not
published at *download.tizen.org* and therefore can\'t be downloaded by
gbs automatically. So user needs to download it and provide it to gbs
tool manually. There are two ways to get project config:

#### With osc tool

Import project config using *osc meta*

`osc meta prjconf devel:arm_toolchain:Mobile:Tizen_Common >  ${work_dir}/tizen-conf/aarch64_build.conf`

#### Using browser

Project config is also available through web-interface, so you may open
[Project
config](https://build.tizen.org/project/prjconf?project=devel:arm_toolchain:Mobile:Tizen_Common)
page and copy config from there.

[Category:Tool](Category:Tool "wikilink")
