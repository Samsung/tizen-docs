# System recovery

Each Tizen 4.0 comes with three different root filesystems, each for
different purpose.

| Label | Purpose |
| ----- | ------- |
| `rootfs` | The main root filesystem |
| `ramdisk` | Regular boot ramdisk |
| `ramdisk-recovery` | System recovery ramdisk |

This section describes operation and how to customize the system
recovery ramdisk.

The boot process starts with a bootloader (u-boot or s-boot) loading
appropriate kernel and ramdisk images dedicated for the system
recovery process (methods of control of bootleaders are beyond the
scope of this document). With both images loaded into RAM the kernel
initialisation begins. When the initialisation is over, kernel passes
control to the init process i.e. `/sbin/init` (a.k.a. PID#1).

In case of recovery ramdisk this is a symlink to
`/usr/libexec/initrd-recovery/init` which is a shell script, that comes
from the `initrd-recovery` package. The script mounts several kernel
filesystems and the inform partition (if it exists) and parses the
kernel command line options (`/proc/cmdline`) to find `bootmode`
parameter. If the parameter is present, one of `/sbin/*-init` scripts is
started. With the boot mode set to recovery,
`/usr/libexec/system-recovery/recovery-init` is started.

The `recovery-init` script mounts the real root file-system under
the `/system` directory and other file-systems below it (e.g. `/opt`,
`/opt/usr`), starts a shell on the serial console and launches the
`system-recovery` programme.

The `system-recovery` programme can work as either an interactive GUI or
a non-interactive dispatcher, that executes one (non-interactive) or
more (interactive) actions. The actions are configured in
`/usr/share/system-recovery/system-recovery.cfg`.

## Configuration file

The configuration file allows to customise two aspects of
system-recovery operation: GUI and actions. Let's take a closer look
at the latter. The file is parsed using `libconfig`. Please refer to
libconfig documentation for detailed [description of the
grammar](http://hyperrealm.com/libconfig/libconfig_manual.html#Configuration-File-Grammar).

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

Actions (names) are refered further in the `menus` dictionary. The
`menus` dictionary comprises all pages of the menu system presented by
`system-recovery`. The `main` entry is the one the programme displays
at startup. The rest should be linked in tree-like structure.

### `menus`

Each menu entry comprises the following fields

* pos_x, pox_y - position on a screen,
* style - reference to menu_styles dictionary,
* actions - and array of actions available in this menu,
* item_default - action to highlight when opening the menu.

An action may be handled in one of two ways: run an action handler or
switch to another screen. There is a reserved screen name BACK, that
means switching to the previous screen (see screen_back in the screens
dictionary).

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

NOTE: The system-recovery.cfg.m4.in source file provides
confirm_action m4 macro to define *Yes/No* style actions array. *Yes*
executes an action, *No* switches to a previous screen. Use this macro
when adding an action to the config file in the repository.

For example
```
actions = confirm_action(`safeboot', 1);
```
expands to

```
actions = ({
    label = "Yes";
    action_handler = "safeboot";
    exit_after_action = 1;
},{
    label = "No";
    screen_switch_to = "BACK";
});
```

The first argument of the macro is an action, the second is the value
to assign to the `exit_after_action` element.

### `screens`

As mentioned above, each action can either execute an action handler
(a shell command) or switch to a screen. Screens are configured in
their dictionary as follows.

```
screens = {
    main = {
        style = "common";
        menu = "main";
        rulers = "main";
	description = "main";
        images = ("background_default", "menu_title");
        screen_back = "CURRENT";
    };
    reboot = {
        style = "common";
        menu = "reboot";
        description = "reboot"
        rulers = "confirm" ;
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

There are two groups of parameters in the entries above. The first
group is reposponsible for the look of a screen. These won't be
described further in this document.

* style - element of screen_styles dictionary
* rulers - element of rulers dictionary
* images - list of elements of images dictionary
* animations - element of animations dictionary

The other group comprises parameters that describe logic.

* menu - a menu that display, an element of menus dictionary,
* description - a description text and a screen title that to display,
  an element of description dictionary,
* screen_back - the screen to switch to when swiching to screen BACK,
* allow_force_reboot - reboot after executing an action.


### `descriptions`

The elements of the `descriptions` dictionary hold screen titles and
brief descriptions for screen entries (see above).

* title - short (on line) title displayed at the top of a screen,
* description - brief explanation of actions available on the screen.

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

## Non-GUI operation

If system-recovery is compiled without GUI support only two parameters
in the configuration file that control how the programme behaves:

* action_handlers - list of shell commands,
* headless_action - the action to execute by default.

Before system-recovery reads the `headless_action` parameter it looks
for the action to execute in in two other places:

* tizen.recovery kernel command line option (e.g. tizen.recovery=factory-reset),
* /opt/.recovery.action.


```
headless_action = "factory-reset";
```

## Adding new action

To add a new action you need to define the action handler in the
`action_handlers` dictionary.

```
action_handlers = {
    factory-reset-minimal = "/usr/bin/factory-reset-minimal.sh"
    // [...]
};
```

Then take the `factory` entry from the `menus` dictionary and adapt it.

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
    // [...]
};
```

Add two new entries in the `screens` dictionary.

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
    // [...]
};
```

and in the `descriptions` dictionary.

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
	// [...]
};
```

Finally add an action to the `main` menu, that switches to the
`factory-minimal` screen.

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

## Look-and-feel related options.

Below you can find the rest of the configuration file that is controls
the look-and-feel of the system recovery menus.

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
