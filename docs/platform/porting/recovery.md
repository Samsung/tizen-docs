# System Recovery

Tizen 4.0 comes with 3 different root filesystems, each designed for a different purpose.

**Table: Root filesystems**

| Label | Purpose |
| ----- | ------- |
| `rootfs` | Main root filesystem |
| `ramdisk` | Regular boot ramdisk |
| `ramdisk-recovery` | System recovery ramdisk |

This topic describes operation and customization options of the system
recovery ramdisk.

The following steps describe the boot process:

1. The boot process starts with a bootloader (u-boot or s-boot) loading
appropriate kernel and ramdisk images dedicated for the system
recovery process (methods for controlling bootloader actions are beyond the
scope of this document). With both images loaded into RAM, the kernel
initialization begins. When the initialization is complete, the kernel passes
control to the init process, such as `/sbin/init` (PID#1).

2. In the case of the recovery ramdisk, `/sbin/init` is a symlink to
`/usr/libexec/initrd-recovery/init` (a shell script that comes
from the `initrd-recovery` package). The script mounts several kernel
filesystems and the inform partition (if it exists), and parses the
kernel command line options (`/proc/cmdline`) to find the `bootmode`
parameter. If the parameter is present, one of the `/sbin/*-init` scripts is
started. If the boot mode is set to `recovery`,
`/usr/libexec/system-recovery/recovery-init` is started.

3. The `recovery-init` script mounts the real root filesystem under
the `/system` directory, and other filesystems (such as `/opt` and
`/opt/usr`) below the `/system` directory. The script starts a shell on the serial console and launches the
`system-recovery` program.

4. The `system-recovery` program can work as either an interactive GUI or
a non-interactive dispatcher, executing 1 (non-interactive) or
more (interactive) actions. The actions are configured in the
`/usr/share/system-recovery/system-recovery.cfg` file.

## Configuration File

The configuration file allows you to customize 2 aspects of
the system-recovery operation: GUI and actions. The following sections take a closer look
at the actions.

The configuration file is parsed using `libconfig`. For a detailed description of the
grammar, see the [libconfig documentation](http://hyperrealm.com/libconfig/libconfig_manual.html#Configuration-File-Grammar).

### `action_handlers`

`action_handlers` is a dictionary, in which shell commands (action
handlers) are assigned names (actions). The names are used later in
the configuration to refer to commands. The dictionary can be edited
and actions can be added or removed. The names must be unique.

```
action_handlers = {
    reboot = "reboot -f";
    factory-reset = "touch -f /opt/.factoryreset";
    safeboot = "touch -f /opt/etc/.safeboot";
}
```

### `menus`

Actions (names) are used in the `menus` dictionary, which
comprises all pages of the menu system presented by
`system-recovery`. The `main` entry is the one the program displays
at startup. The rest must be linked in a tree-like structure.

Each menu entry consists of the following fields:

- `pos_x` and `pox_y`: Position on a screen
- `style`: Reference to the `menu_styles` dictionary
- `actions`: Array of actions available in this menu
- `item_default`: Action to highlight when opening the menu

The `system-recovery` program can handle an action in 2 ways: it can run an action handler
or switch to another screen. There is a reserved screen name **BACK**, which
means switching to the previous screen (for more information, see `screen_back` in the [screens
dictionary](#screens)).

```
menus = {
    main = {
        pos_x = 0;
        pos_y = 100;
        style = "common";
        actions = ({
            label = "Reboot system now";
            screen_switch_to = "reboot";
        },{
            label = "Safe mode";
            screen_switch_to = "safe";
        },{
            label = "Phone reinitialisation";
            screen_switch_to = "factory";
        });
    };
    reboot = {
        pos_x = 0;
        pos_y = 480;
        style = "common";
        item_default = 1;
        actions = ({
            label = "Yes";
            action_handler = "reboot";
            exit_after_action = 0;
        },{
            label = "No";
            screen_switch_to = "BACK";
        });
    };
    safe = {
        pos_x = 0;
        pos_y = 480;
        style = "common";
        item_default = 1;
        actions = ({
            label = "Yes";
            action_handler = "safeboot";
            exit_after_action = 1;
        },{
            label = "No";
            screen_switch_to = "BACK";
        });
    };
    factory = {
        pos_x = 0;
        pos_y = 480;
        style = "common";
        item_default = 1;
        actions = ({
            label = "Yes";
            screen_switch_to = "factory-run";
            action_handler = "factory-reset";
            exit_after_action = 1;
        },{
            label = "No";
            screen_switch_to = "BACK";
        });
    };
};
```

> **Note**
>
> The `system-recovery.cfg.m4.in` source file provides the `confirm_action` m4 macro to define a **Yes/No** style action array:
> - **Yes** executes an action.
> - **No** switches to a previous screen.
>
> Use this macro when adding an action to the config file in the repository.
>
> For example:
> ```
> actions = confirm_action('safeboot', 1);
> ```
> Expands to:
> ```
> actions = ({
>     label = "Yes";
>     action_handler = "safeboot";
>     exit_after_action = 1;
> },{
>     label = "No";
>     screen_switch_to = "BACK";
> });
> ```
>
> The first argument of the macro is an action, and the second is the value to assign to the `exit_after_action` element.

### `screens`

Each action can either execute an action handler (a shell command) or switch to a screen. The screens are configured in
their dictionary as follows:

```
screens = {
    main = {
        style = "common";
        menu = "main";
        description = "main";
        rulers = "main";
        images = ("background_default", "menu_title");
        screen_back = "CURRENT";
    };
    reboot = {
        style = "common";
        menu = "reboot";
        description = "reboot"
        rulers = "confirm";
        images = ("background_default", "menu_title");
        screen_back = "main";
    };
    safe = {
        style = "common";
        menu = "safe";
        description = "safe";
        rulers = "confirm";
        images = ("background_default", "menu_title");
        screen_back = "main";
    };
    factory = {
        style = "common";
        menu = "factory";
        description = "factory";
        rulers = "confirm";
        images = ("background_default", "menu_title");
        screen_back = "main";
    };
    factory-run = {
        style = "common";
        description = "factory-run";
        rulers = "confirm";
        images = ("background_default", "menu_title");
        animations = ("working");
        screen_back = "main";
        allow_force_reboot = 1;
    };
};
```

The above entries contain 2 parameter groups:

- The first group is responsible for the look of a screen:
  - `style`: Element of the `screen_styles` dictionary
  - `rulers`: Element of the `rulers` dictionary
  - `images`: List of elements of the `images` dictionary
  - `animations`: Element of the `animations` dictionary

  These parameters are not described in detail in this document.
- The second group comprises parameters that describe logic:
  - `menu`: Menu to display (an element of the `menus` dictionary)
  - `description`: Description text and screen title to display (an element of the `descriptions` dictionary)
  - `screen_back`: Screen to switch to when switching **BACK**
  - `allow_force_reboot`: Reboot after executing an action


### `descriptions`

The elements of the `descriptions` dictionary hold screen titles and
brief descriptions for screen entries:

- `title`: Short (one line) title displayed at the top of a screen
- `description`: Brief explanation of actions available on the screen

```
descriptions = {
    main = {
        pos_x = 15;
        pos_y = 480;
        style = "common";
        title = "Controls:";
        text = "Volume Up/Down to move menu cursor\n"
            "Power button to select";
    };

    reboot = {
        pos_x = 15;
        pos_y = 100;
        title = "The phone will be restarted.";
        text = "Continue?";
        style = "common";
    };

    safe = {
        pos_x = 15;
        pos_y = 100;
        title = "Safe mode:",
        text = "The phone will be started in safe mode.\n"
            "Home screen will be changed to default\n"
            "setting and just allow a user to use\n"
            "only preloaded applications.\n"
            "Continue?";
        style = "common";
    };

    factory = {
        pos_x = 15;
        pos_y = 100;
        title = "Factory reset (except SD-card)";
        text = "This will erase all data from your\n"
            "phone's internal storage, including\n"
            "settings of downloaded and preloaded\n"
            "applications and system configuration.\n"
            "Continue?";
        style = "common";
    };

    factory-run = {
        pos_x = 15;
        pos_y = 100;
        style = "common";
        title = "Restoring settings to factory default.";
        text = "Please wait. Do not turn off.\n"
            "(Hold power button for 3 seconds\n"
            "to reboot the device. Not recommended.)";
    }
};
```

## Non-interactive Operation

If the `system-recovery` program is compiled without GUI support, only 2 parameters
in the configuration file control how the program behaves:

- `action_handlers`: List of shell commands
- `headless_action`: Action to execute by default

Before `system-recovery` reads the `headless_action` parameter, it looks
for the action to execute in 2 other places:

- `tizen.recovery` kernel command line option (such as `tizen.recovery=factory-reset`)
- `/opt/.recovery.action`


```
headless_action = "factory-reset";
```

## Adding New Actions

To add a new action:

1. Define an action handler in the `action_handlers` dictionary:
   ```
   action_handlers = {
       factory-reset-minimal = "/usr/bin/factory-reset-minimal.sh"
   };
   ```
2. Take the `factory` entry from the `menus` dictionary and adapt it:
   ```
   menus = {
       factory-minimal = {
           pos_x = 0;
           pos_y = 480;
           style = "common";
           item_default = 1;
           actions = ({
               label = "Yes";
               screen_switch_to = "factory-run-minimal";
               action_handler = "factory-reset-minimal";
               exit_after_action = 1;
           },{
               label = "No";
               screen_switch_to = "BACK";
           });
       };
   };
   ```
3. Add 2 new entries in the `screens` dictionary:
   ```
   screens = {
       factory-minimal = {
           style = "common";
           menu = "factory-minimal";
           description = "factory-minimal";
           rulers = "confirm";
           images = ("background_default", "menu_title");
           screen_back = "main";
       };
       factory-run-minimal = {
           style = "common";
           description = "factory-run-minimal";
           rulers = "confirm";
           images = ("background_default", "menu_title");
           animations = ("working");
           screen_back = "main";
           allow_force_reboot = 1;
       };
   };
   ```
4. Add 2 new entries in the `descriptions` dictionary:
   ```
   descriptions = {
       factory-minimal = {
           pos_x = 15;
           pos_y = 100;
           title = "Factory reset (except SD-card)";
           text = "This will erase SOME data from your\n"
               "phone's internal storage, including\n"
               "settings of downloaded and preloaded\n"
               "applications and system configuration.\n"
               "Continue?";
           style = "common";
       };
       factory-run-minimal = {
           pos_x = 15;
           pos_y = 100;
           style = "common";
           title = "Restoring SOME settings to factory default.";
           text = "Please wait. Do not turn off.\n"
               "(Hold power button for 3 seconds\n"
               "to reboot the device. Not recommended.)";
       };
   };
   ```
5. Add an action to the `main` menu that switches to the `factory-minimal` screen:
   ```
   main = {
       pos_x = 0;
       pos_y = 100;
       style = "common";
       actions = ({
           label = "Reboot system now";
           screen_switch_to = "reboot";
       },{
           label = "Safe mode";
           screen_switch_to = "safe";
       },{
           label = "Phone reinitialisation";
           screen_switch_to = "factory";
       },{
           label = "Minimal phone reinitialisation";
           screen_switch_to = "factory-minimal";
       });
   };
   ```

## Look-and-feel Options

The following example shows the remaining parts of the configuration file, containing options that control the look-and-feel of the system recovery menus:

```
colors = {
    background = "#000000ff";
    title = "#1bc7ccff";
    ruler = "#1bc7ccff";
    white = "#ffffffff";
};

ruler_styles = {
    common = {
        c_ruler = "ruler";
    };
};

menu_styles = {
    common = {
        item_height = 80;
        item_spacing = 8;
        text_pos_x = 15;
        c_bg_selected = "title";
        c_bg_unselected = "background";
        c_text_selected = "white";
        c_text_unselected = "white";
    };
};

screen_styles = {
    common = {
        c_background = "background";
    };
};

description_styles = {
    common = {
        c_title = "title";
        c_text = "white";
    };
};

rulers = {
    main = (
    {
        pos_x = 0;
        pos_y = 80;
        height = 2;
        style = "common";
    }, {
        pos_x = 0;
        pos_y = 420;
        height = 2;
        style = "common";
    });

    confirm = (
    {
        pos_x = 0;
        pos_y = 80;
        height = 2;
        style = "common";
    });
};

images = {
    background_default = {
        fname = "/usr/share/system-recovery/res/images/warning.png";
        c_bg = "background"; // reference to colors
        align_hor = "center";
        align_ver = "bottom";
        offset_x = 0;
        offset_y = 0;
        img_type = "alpha"; // alt: "no-alpha";
    };
    menu_title = {
        fname = "/usr/share/system-recovery/res/images/menu-title.png";
        c_bg = "title";
        align_hor = "center";
        align_ver = "top";
        offset_x = 0;
        offset_y = 20;
        img_type = "no-alpha"; // alt: "no-alpha";
    };
};

animations = {
    working = {
        fname = "/usr/share/system-recovery/res/images/tizen-anim.png";
        c_bg = "background";
        align_hor = "center";
        align_ver = "middle";
        offset_x = 0;
        offset_y = 0;
        frames_num = 0;
        current_frame = 0;
        img_type = "no-alpha"; // alt: "no-alpha";
    };
};
```

## Adding New Files to the `ramdisk-recovery` Partition

The `ramdisk-recovery` partition is created along with the `rootfs`
partition (methods for creating images are beyond the scope of this
document):

- Files to be added to the `ramdisk-recovery` partition must
be available in Tizen RPM packages.
- Files are added to the partition by the `mkinitrd-recovery.sh` script, which is started
automatically as a part of the `%posttrans` RPM script of the `initrd-recovery` package.

To install a selected file in the recovery
image, its RPM needs to be installed before `initrd-recovery` is run. The
easiest way to make sure this happens is to list the package as a
dependency in the `initrd-recovery.spec` file.

The `mkinitrd-recovery.sh` script copies or moves files from the
`rootfs` partition to the `initrd-recovery` partition according to
directions provided in configuration files stored in the
`/usr/share/initrd-recovery/initrd.list.d` directory. These files
must be packaged in the RPM packages together with the
files to be put on the `initrd-recovery` partition. The configuration files are
interpreted as shell scripts and can be used to set the following
variables:

- `DIRECTORIES`: Create directories.
- `DIR_SYMLINKS`: Create symbolic links to directories.
- `LIBONLYS`: Copy **only** the libraries required by the listed executable files.
- `MVWITHLIBS`: Move the listed executable files and copy the required libraries.
- `SYMLINKS`: Create symbolic links.
- `VERBATIMS`: Copy the listed files. List non-executable files here.
- `WITHLIBS`: Copy the listed executable files and the required libraries.

The `SYMLINKS` and `DIR_SYMLINKS` variables contain pairs of filenames separated with
colons.

The following section contains examples of the above variables:

```
DIRECTORIES="
/var/tmp
/usr/lib/odbc
"

# LinkFileName:Target
DIR_SYMLINKS="
/lib:usr/lib
/opt:system/opt
"

LIBONLYS="
/bin/bash
/bin/kill
"

MVWITHLIBS="
/usr/libexec/initrd-recovery/minireboot
/usr/libexec/system-recovery/system-recovery.gui
"

WITHLIBS="
/usr/bin/sync
/usr/bin/touch
"

VERBATIMS="
/usr/share/system-recovery/res/images/font.png
/usr/share/system-recovery/res/images/menu-title.png
/usr/share/system-recovery/system-recovery.cfg
"

# LinkFileName:Target
SYMLINKS="
/sbin/recovery-init:/usr/libexec/system-recovery/recovery-init
/usr/lib/bufmgr/libtbm_default.so:libtbm_sprd.so
"
```

The following real-world example comes from the `initrd-recovery`
package. Following this configuration, `mkinitrd-recovery.sh` copies
some basic tools to the `initrd-recovery` partition, moves `init` and
`minireboot`, and creates some symlinks:

```
MVWITHLIBS="
/usr/libexec/initrd-recovery/init
/usr/libexec/initrd-recovery/minireboot
"

WITHLIBS="
/usr/bin/bash
/usr/bin/cat
/usr/bin/mkdir
/usr/bin/mount
/usr/bin/sleep
/usr/bin/sync
/usr/bin/umount
/usr/sbin/blkid
"

# LinkFileName:Target
SYMLINKS="
/bin/sh:bash
/sbin/init:/usr/libexec/initrd-recovery/init
/sbin/minireboot:/usr/libexec/initrd-recovery/minireboot
/sbin/reboot:/usr/libexec/initrd-recovery/minireboot
"
```
