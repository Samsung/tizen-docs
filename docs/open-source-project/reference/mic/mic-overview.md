# MIC Image Creator

MIC is an image creator used when creating images for Tizen. With the MIC tool, you can:

- **Create images** of different types for different verticals, such as:
  - Live CD images
  - Live USB images
  - Raw images for KVM
  - Loop images for IVI platforms
  - fs images for chrooting
- **Chroot** into an image using MIC's enhanced `chroot` command.
- **Convert an image** to another image format.

This is a very useful function when handling situations sensitive to image format.

Before going into further MIC details, make sure you have [set up the development environment](../../developing/setting-up.md) and learned how to [install and upgrade tools](../../developing/installing.md).

Afterwards, become familiar with MIC by reading the following instructions:

- [Customizing Images](mic-customize-image.md) describes how to modify the kickstart file to customize an image.
- [MIC Reference](mic-reference.md) describes, in more detail, how to use MIC.
- [MIC Frequently Asked Questions](mic-faq.md) describes frequently asked questions and known issues.
- [Reporting MIC Issues](mic-faq.md#reporting-mic-issues) describes how to report bugs and feature requests.

## Source Code

The source code is tracked in the [https://github.com/01org/mic](https://github.com/01org/mic) repository.

## License

```
Copyright (c) 2012 Intel, Inc.
This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the Free
Software Foundation; version 2 of the License.
This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
for more details.
You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc., 59
Temple Place - Suite 330, Boston, MA 02111-1307, USA.
```
