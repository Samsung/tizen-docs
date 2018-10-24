# GBS (Git Build System)

GBS (git-build-system) is a command line tool that supports Tizen package development. It is used to generate tarballs based on Git repositories, to do local test buildings, and to submit code to OBS (Tizen's main build service).

Before going into further GBS details, make sure you have [set up the development environment](../../developing/setting-up.md) and learned how to [install and upgrade tools](../../developing/installing.md).

Afterwards, become familiar with GBS by reading the following instructions:

- [GBS Configuration](gbs.conf.md) describes how to modify the GBS configuration.
- [GBS Reference](gbs-reference.md) describes, in more detail, how to use GBS.
- [GBS Frequently Asked Questions](gbs-faq.md) describes frequently asked questions.

## Source Code

The source code is tracked in the [https://github.com/01org/gbs](https://github.com/01org/gbs) repository.

## License
```
Copyright (c) 2012 Intel, Inc.
This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the Free
Software Foundation; version 2 of the License
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
for more details.
You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc., 59
Temple Place - Suite 330, Boston, MA 02111-1307, USA.
```

## Reference
The gbs build references the scripts of the SUSE Linux RPM builds: [https://github.com/openSUSE/obs-build](https://github.com/openSUSE/obs-build).
