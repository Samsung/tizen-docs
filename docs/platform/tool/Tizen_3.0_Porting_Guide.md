Introduction
============

Tizen Architecture
==================

Development Environment Setup
=============================

To set up the Tizen OS Development environment and to obtain information
regarding development, see the following links:

-   [Setup your
    environment](https://source.tizen.org/documentation/developer-guide/environment-setup)
-   [Installing development
    tools](https://source.tizen.org/documentation/developer-guide/installing-development-tools)

Getting the Source Code and Build
=================================

Tizen Bootup Overview
=====================

BSP Customization
=================

Kernel Fundamentals
===================

System
======

Graphics and UI
===============

Multimedia
==========

Connectivity
============

Location
========

Telephony
=========

\
This document covers detailed Telephony architecture including the
various components of Telephony and workflow through Telephony
framework. The document also provides porting guidelines for vendors to
ease the OAL interface development for their hardware.

Tizen Telephony features

-   Telecommunication functionalities, such as call, SS, SMS, SIM,
    network, and packet service
-   Plug-in Architecture

Definitions

-   Core object
    -   Bundle of functions and supportive database information
        designated to specific module, such as call, SS, SIM, network,
        which processes requests, responses, and notifications.
    -   Core objects form the executable component of a Telephony module
        (call, SS, SIM, network)
-   HAL
    -   HAL, Hardware Abstraction Layer, abstracts the actual hardware
        used and ensures that similar functionality is provided by
        various hardware (modems) of the same modem vendor.
    -   All hardware specific changes are controlled and processed by
        HALs.
    -   The modem driver can be required depending on the modem chipset.
-   Hooks
    -   Hooks provide a mechanism to tap requests, responses, and
        notifications of other Telephony modules.
    -   Hooking is a transparent mechanism and does not affect the
        normal processing of requests, responses, and notifications.

Tizen Telephony Architecture
----------------------------

Tizen Telephony supports the plugin architecture, which provides
flexibility to include various types of predefined plugins into the
system with little change.

![](telephony-arch.png "telephony-arch.png"){width="700"}

The 3 major components of Tizen Telephony are the libraries, plugins,
and server.

Telephony Libraries
-------------------

Telephony API (TAPI) library

The TAPI library (or simply TAPI) is a standardized interface provided
to applications to interact with Tizen Telephony. It is provided as a
`libtapi` package. The TAPI executes in the application's context, and
it provides sync and async APIs. The following figure shows the
`libtapi` internal composition.

![](Libtapi.PNG "Libtapi.PNG"){width="500"}

Applications can interface to Telephony features, such as call, SMS, and
network, through the respective module APIs exposed in the `libtapi`
library. Telephony also provides an additional library, `capi-telephony`
for third party applications.

Core Telephony library

The Core Telephony library (or `libtcore`) provides an API framework for
Tizen Telephony to inter-work. It is provided as `libtcore` package. The
following figure shows the internal composition overview of the
`libtcore`.

![](Telephony03.png "Telephony03.png"){width="500"}

With `libtcore`, you can:

-   Create, destroy, and maintain various server components, such as
    server, communicator, HAL, plugin, and core object.
-   Maintain storage, queue mechanism, and general utilities.
-   Support CMUX (creation/destruction/processing).
-   Parse AT.

Telephony Plugins
-----------------

There are 4 kinds of plugins:

-   Communicator plugins
    -   Interfaces TAPI and Telephony Server.
    -   For example, DBUS communicator (`DBUS_TAPI`) is provided by
        default.

:   ![](Telephony04.png "fig:Telephony04.png"){width="200"}

-   Modem plugins
    -   Core functional units providing the Telephony functionality.
    -   Maintain and manage the Telephony states.
    -   Maintain and manage the databases related to Telephony.

:   ![](Telephony05.png "fig:Telephony05.png"){width="300"}

-   Modem interface plugins
    -   Interfaces the telephony server to the communication processor.
    -   Hardware specific plugins which define hardware capabilities and
        usage
    -   Modem interface plugin is also called HAL.

:   ![](Telephony06.png "fig:Telephony06.png"){width="200"}

-   Free Style plugins
    -   Provide completely independent functionality irrespective of
        hardware (communication processor).
    -   For example plugins, such as packetservice, storage, and
        indicator.

:   ![](Telephony07.png "fig:Telephony07.png"){width="300"}

The following figure provides an overview of all the Telephony plugins
together.

![](Telephony08.png "Telephony08.png"){width="500"}

Telephony Server
----------------

Tizen Telephony runs as a Telephony server daemon called
`telephony-daemon`.

The Telephony server executes as a `g-main` loop from the `glib`
library.

![](Telephony09.png "Telephony09.png"){width="800"}

\
\

Porting OAL Interface
---------------------

OEM vendors can port available plugins within Telephony as needed. It is
not mandatory that all the plugins to be ported to support a specific
hardware.

This section provides guidance to OEM vendors to develop various
Telephony plugins.

### Plugin Descriptors

Any telephony plugin is required to provide a descriptor structure
described in the following example.

+-----------------------------------+-----------------------------------+
| Structure                         | Description                       |
+===================================+===================================+
|     struct tcore_plugin_define_de | Structure referred by Telephony   |
| sc {                              | server to load, initialize, and   |
|         gchar *name;              | unload the plugin. This structure |
|         enum tcore_plugin_priorit | defines:                          |
| y priority;                       |                                   |
|         int version;              | 1.  Name of the plugin            |
|         gboolean(*load)();        | 2.  Initializing priority of the  |
|         gboolean(*init)(TcorePlug |     plugin                        |
| in *);                            | 3.  Plugin version                |
|         void (*unload)(TcorePlugi | 4.  Plugin \'load\' function      |
| n *);                             |     reference                     |
|     };                            | 5.  Plugin \'init\' function      |
|                                   |     reference                     |
|                                   | 6.  Plugin \'unload\' function    |
|                                   |     reference                     |
+-----------------------------------+-----------------------------------+

The descriptor structure of each plugin must be named as
`plugin_define_desc`. The server obtains the address of this symbol in
order to provide control to the plugin to execute its defined
functionality.

The order of initialization among various Telephony plugins is defined
based on the plugin's priority.

OEMs need to specifically implement the modem and modem interface
plugins to support their hardware.

### Call Service Operations

The implementation of the functions described in the following example
is required to provide call services.

+-----------------------------------+-----------------------------------+
| Structure                         | Description                       |
+===================================+===================================+
|     struct tcore_call_operations  | The structure referred by the     |
| {                                 | Telephony server to provide call  |
|         TReturn (*dial)(CoreObjec | services. This structure defines: |
| t *o, UserRequest *ur);           |                                   |
|         TReturn (*answer)(CoreObj | 1.  Call \'dial\' function        |
| ect *o, UserRequest *ur);         |     reference                     |
|         TReturn (*end)(CoreObject | 2.  Call \'answer\' function      |
|  *o, UserRequest *ur);            |     reference                     |
|         TReturn (*hold)(CoreObjec | 3.  Call \'end\' function         |
| t *o, UserRequest *ur);           |     reference                     |
|         TReturn (*active)(CoreObj | 4.  Call \'hold\' function        |
| ect *o, UserRequest *ur);         |     reference                     |
|         TReturn (*swap)(CoreObjec | 5.  Call \'active\' function      |
| t *o, UserRequest *ur);           |     reference                     |
|         TReturn (*join)(CoreObjec | 6.  Call \'swap\' function        |
| t *o, UserRequest *ur);           |     reference                     |
|         TReturn (*split)(CoreObje | 7.  Call \'join\' function        |
| ct *o, UserRequest *ur);          |     reference                     |
|     };                            | 8.  Call \'split\' function       |
|                                   |     reference                     |
+-----------------------------------+-----------------------------------+

### SMS Service Operations

The implementation of the functions described in the following example
is required to provide SMS services.

+-----------------------------------+-----------------------------------+
| Structure                         | Description                       |
+===================================+===================================+
|     struct tcore_sms_operations { | Structure referred by the         |
|         TReturn (*send_umts_msg)( | Telephony server to provide       |
| CoreObject *o, UserRequest *ur);  | SMS-related services. This        |
|         TReturn (*send_cdma_msg)( | structure defines:                |
| CoreObject *o, UserRequest *ur);  |                                   |
|         TReturn (*read_msg)(CoreO | 1.  SMS \'send\' function         |
| bject *o, UserRequest *ur);       |     reference                     |
|         TReturn (*save_msg)(CoreO | 2.  SMS \'read\' function         |
| bject *o, UserRequest *ur);       |     reference                     |
|         TReturn (*delete_msg)(Cor | 3.  SMS \'save\' function         |
| eObject *o, UserRequest *ur);     |     reference                     |
|         TReturn (*get_sca)(CoreOb | 4.  SMS \'delete\' function       |
| ject *o, UserRequest *ur);        |     reference                     |
|         TReturn (*set_sca)(CoreOb | 5.  SMS \'get sca\' function      |
| ject *o, UserRequest *ur);        |     reference                     |
|         TReturn (*get_sms_params) | 6.  SMS \'set sca\' function      |
| (CoreObject *o, UserRequest *ur); |     reference                     |
|         TReturn (*set_sms_params) | 7.  SMS \'get sms params\'        |
| (CoreObject *o, UserRequest *ur); |     function reference            |
|     };                            | 8.  SMS \'set sms params\'        |
|                                   |     function reference            |
+-----------------------------------+-----------------------------------+

### Network Service Operations

The implemenation of the functions described in the following example is
required to provide network services.

+-----------------------------------+-----------------------------------+
| Structure                         | Description                       |
+===================================+===================================+
|     struct tcore_network_operatio | Structure referred by the         |
| ns {                              | Telephony server to provide       |
|         TReturn (*search)(CoreObj | network services. This structure  |
| ect *o, UserRequest *ur);         | defines:                          |
|         TReturn (*set_plmn_select |                                   |
| ion_mode)(CoreObject *o, UserRequ | 1.  Network \'search\' function   |
| est *ur);                         |     reference                     |
|         TReturn (*get_plmn_select | 2.  Network \'set plmn selection  |
| ion_mode)(CoreObject *o, UserRequ |     mode\' function reference     |
| est *ur);                         | 3.  Network \'get plmn selection  |
|         TReturn (*set_service_dom |     mode\' function reference     |
| ain)(CoreObject *o, UserRequest * | 4.  Network \'set service         |
| ur);                              |     domain\' function reference   |
|         TReturn (*get_service_dom | 5.  Network \'get service         |
| ain)(CoreObject *o, UserRequest * |     domain\' function reference   |
| ur);                              | 6.  Network \'set band\' function |
|         TReturn (*set_band)(CoreO |     reference                     |
| bject *o, UserRequest *ur);       | 7.  Network \'get band\' function |
|         TReturn (*get_band)(CoreO |     reference                     |
| bject *o, UserRequest *ur);       |                                   |
|     };                            |                                   |
+-----------------------------------+-----------------------------------+

### HAL operations

The implementation of the functions described in the following example
is required to provide HAL operations.

+-----------------------------------+-----------------------------------+
| Structure                         | Description                       |
+===================================+===================================+
|     struct tcore_hal_operations { | Structure referred by Telephony   |
|         TReturn (*power)(TcoreHal | server to provide HAL operations. |
|  *hal, gboolean flag);            | This structure defines:           |
|         TReturn (*send)(TcoreHal  |                                   |
| *hal, unsigned int data_len, void | 1.  HAL \'power\' function        |
|  *data);                          |     reference                     |
|         TReturn (*setup_netif)(Co | 2.  HAL \'send\' function         |
| reObject *co,                     |     reference                     |
|                                Tc | 3.  HAL \'setup network           |
| oreHalSetupNetifCallback func, vo |     interface\' function          |
| id *user_data,                    |     reference                     |
|                                un |                                   |
| signed int cid, gboolean enable); |                                   |
|     };                            |                                   |
+-----------------------------------+-----------------------------------+

Sample implementations of the modem and modem interface plugins is
available in the [Appendix](Tizen_3.0_Porting_Guide#Appendix "wikilink")
section.

Configuration
-------------

There are no specific configurations required for Telephony except for
conforming to the installation paths of various Telephony plugins.

All Telephony plugins need to be installed in the following folders:

-   Modem Plugins: `%{_libdir}/telephony/plugins/modems/`
-   Other Plugins: `%{_libdir}/telephony/plugins/`

References
----------

Tizen source website <http://review.tizen.org/git/>

Telephony packages

-   Telephony daemon

:   `platform/core/telephony/telephony-daemon.git`

-   Telephony core library

:   `platform/core/telephony/libtcore.git`

-   TAPI

:   `platform/core/telephony/libtapi.git`

-   Telephony API for a third party application

:   `platform/core/api/telephony.git`

-   Communicator (`DBUS_TAPI`)

:   `platform/core/telephony/tel-plugin-dbus_tapi.git`

-   Free Style plugin (indicator)

:   `platform/core/telephony/tel-plugin-indicator.git`

-   Free Style plugin (packetservice)

:   `platform/core/telephony/tel-plugin-packetservice.git`

-   Free Style plugin (nitz)

:   `platform/core/telephony/tel-plugin-nitz.git`

-   Free Style plugin (Database)

:   `platform/core/telephony/tel-plugin-vconf.git`

-   Free Style plugin (VCONF)

:   `platform/core/telephony/tel-plugin-database.git`

-   Modem plugin (device)

:   `platform/core/telephony/tel-plugin-imc.git`

-   Modem Interface plugin (device)

:   `platform/core/telephony/tel-plugin-imcmodem.git`

-   Modem plugin (emulator)

:   `platform/core/telephony/tel-plugin-atmodem.git`

-   Modem Interface plugin (emulator)

:   `platform/core/telephony/tel-plugin-vmodem.git`

Appendix
--------

#### Sample Implementation for the Modem Interface Plugin

    /* HAL Operations */
    static struct tcore_hal_operations hal_ops = {
        .power = hal_power,
        .send = hal_send,
        .setup_netif = hal_setup_netif,
    };

    static
    gboolean on_load()
    {
        dbg(" Load!!!");

        return TRUE;
    }

    static 
    gboolean on_init(TcorePlugin *plugin)
    {
        TcoreHal *hal;
        PluginData *user_data;
        struct custom_data *data;

        dbg(" Init!!!");

        if (plugin == NULL) {
            err(" PLug-in is NULL");

            return FALSE;
        }

        /* User data for Modem Interface plugin */
        user_data = g_try_new0(PluginData, 1);
        if (user_data == NULL) {
            err(" Failed to allocate memory for Plugin data");

            return FALSE;
        }

        /* Register to eerver */
        user_data->modem = tcore_server_register_modem(tcore_plugin_ref_server(plugin), plugin);
        if (user_data->modem == NULL) {
            err(" Registration Failed");
            g_free(user_data);
        
            return FALSE;
        }
        dbg(" Registered from Server");


        data = g_try_new0(struct custom_data, 1);
        if (data == NULL) {
            err(" Failed to allocate memory for Custom data");

            /* Unregister from server */
            tcore_server_unregister_modem(tcore_plugin_ref_server(plugin), user_data->modem);

            /* Free plugin data */
            g_free(user_data);

            return FALSE;
        }

        /* Open DPRAM device */
        data->vdpram_fd = vdpram_open();
        if (data->vdpram_fd < 0) {
            /* Free custom data */
            g_free(data);

            /* Unregister from server */
            tcore_server_unregister_modem(tcore_plugin_ref_server(plugin), user_data->modem);

            /* Free plugin data */
            g_free(user_data);

            return FALSE;
        }
        /* Create and initialize HAL */
        hal = tcore_hal_new(plugin, "vmodem", &hal_ops, TCORE_HAL_MODE_AT);
        if (hal == NULL) {
            /* Close VDPRAM device */
            vdpram_close(data->vdpram_fd);

            /* Free custom data */
            g_free(data);

            /* Unregister from server */
            tcore_server_unregister_modem(tcore_plugin_ref_server(plugin), user_data->modem);

            /* Free Plugin data */
            g_free(user_data);

            return FALSE;
        }
        user_data->hal = hal;

        /* Link custom data to HAL user data */
        tcore_hal_link_user_data(hal, data);

        /* Set HAL as Modem Interface plugin's user data */
        tcore_plugin_link_user_data(plugin, user_data);

        /* Register to Watch list */
        data->watch_id_vdpram = __register_gio_watch(hal, data->vdpram_fd, on_recv_vdpram_message);
        dbg(" fd: [%d] Watch ID: [%d]", data->vdpram_fd, data->watch_id_vdpram);

        /* Power ON VDPRAM device */
        if (_modem_power(hal, TRUE) == TCORE_RETURN_SUCCESS) {
            dbg(" Power ON - [SUCCESS]");
        } else {
            err(" Power ON - [FAIL]");
            goto EXIT;
        }

        /* Check CP Power ON */
        g_timeout_add_full(G_PRIORITY_HIGH, SERVER_INIT_WAIT_TIMEOUT, __load_modem_plugin, hal, 0);

        dbg("[VMMODEM] Exit");

        return TRUE;

    EXIT:
        /* Deregister from Watch list */
        __deregister_gio_watch(data->watch_id_vdpram);

        /* Free HAL */
        tcore_hal_free(hal);

        /* Close VDPRAM device */
        vdpram_close(data->vdpram_fd);

        /* Free custom data */
        g_free(data);

        /* Unregister from Server */
        tcore_server_unregister_modem(tcore_plugin_ref_server(plugin), user_data->modem);

        /* Free plugin data */
        g_free(user_data);

        return FALSE;
    }

    static void
    on_unload(TcorePlugin *plugin)
    {
        TcoreHal *hal;
        struct custom_data *data;
        PluginData *user_data;

        dbg(" Unload!!!");

        if (plugin == NULL)
            return;

        user_data = tcore_plugin_ref_user_data(plugin);
        if (user_data == NULL)
            return;

        hal = user_data->hal;

        data = tcore_hal_ref_user_data(hal);
        if (data == NULL)
            return;

        /* Deregister from Watch list */
        __deregister_gio_watch(data->watch_id_vdpram);
        dbg(" Deregistered Watch ID");

        /* Free HAL */
        tcore_hal_free(hal);
        dbg(" Freed HAL");

        /* Close VDPRAM device */
        vdpram_close(data->vdpram_fd);
        dbg(" Closed VDPRAM device");

        /* Free custom data */
        g_free(data);

        tcore_server_unregister_modem(tcore_plugin_ref_server(plugin), user_data->modem);
        dbg(" Unregistered from Server");

        dbg(" Unloaded MODEM");
        g_free(user_data);
    }

    /* VMODEM Descriptor Structure */
    EXPORT_API struct tcore_plugin_define_desc plugin_define_desc = {
        .name = "VMODEM",
        .priority = TCORE_PLUGIN_PRIORITY_HIGH,
        .version = 1,
        .load = on_load,
        .init = on_init,
        .unload = on_unload
    };

#### Sample Implementation for the Modem Plugin

    static
    gboolean on_load()
    {
        dbg("LOAD!!!");

        return TRUE;
    }

    static
    gboolean on_init(TcorePlugin *p)
    {
        TcoreHal *h;

        dbg("INIT!!!");

        if (!p) {
            err("Plug-in is NULL");

            return FALSE;
        }

        h = tcore_server_find_hal(tcore_plugin_ref_server(p), "vmodem");
        if (!h) {
            err("HAL is NULL");

            return FALSE;
        }

        tcore_hal_add_send_hook(h, on_hal_send, p);
        tcore_hal_add_recv_callback(h, on_hal_recv, p);

        /* Initialize Modules */
        s_modem_init(p, h);
        s_network_init(p, h);
        s_sim_init(p, h);
        s_ps_init(p, h);
        s_call_init(p, h);
        s_ss_init(p, h);
        s_sms_init(p, h);
        tcore_hal_set_power(h, TRUE);

        /* Send "CPAS" command to invoke POWER UP NOTI */
        s_modem_send_poweron(p);

        dbg("Init - Successful");

        return TRUE;
    }

    static void
    on_unload(TcorePlugin *p)
    {
        TcoreHal *h;

        dbg("UNLOAD!!!");

        if (!p) {
            err("Plug-in is NULL");
        
            return;
        }

        h = tcore_server_find_hal(tcore_plugin_ref_server(p), "vmodem");
        if (h) {
            tcore_hal_remove_send_hook(h, on_hal_send);
            tcore_hal_remove_recv_callback(h, on_hal_recv);
        }

        /* Deinitialize the modules */
        s_modem_exit(p);
        s_network_exit(p);
        s_sim_exit(p);
        s_ps_exit(p);
        s_call_exit(p);
        s_ss_exit(p);
        s_sms_exit(p);
    }

    /* ATMODEM plug-in descriptor */
    struct tcore_plugin_define_desc plugin_define_desc = {
        .name = "ATMODEM",
        .priority = TCORE_PLUGIN_PRIORITY_MID,
        .version = 1,
        .load = on_load,
        .init = on_init,
        .unload = on_unload
    };

#### Workflow

1.  Initialization sequence
    1.  The server loads the modem interface plugin.
    2.  The modem interface plugin registers to the server.
    3.  The server enumerates the modem interface plugin.
    4.  Create the physical HAL.
    5.  The modem interface plugin queries the modem state.
    6.  If the modem is online, the CMUX (internal) channels are
        established.
    7.  The logical HAL is created for each CMUX channel and assigned
        for a core object type. These are updated to the mapping table.
    8.  Change the physical HAL mode to `TRANSPARENT` (disables the
        queue).
    9.  The modem interface plugin requests server to load the modem
        plugin (corresponding to its architecture).
    10. The server loads modem plugin.
    11. The modem plugin initializes the sub-modules and creates the
        core objects (based on the core object types defined in the
        mapping table by the modem interface plugin).
    12. The modem plugin notifies the server of the `PLUGIN_ADDED`
        event.
    13. The modem notifies the communicator of the `PLUGIN_ADDED` event.
    14. The communicator creates interfaces for the sub-modules present
        (based on the core objects created).

    :   The following figure shows the telephony loading sequence.
    :   ![](telephony10.png "fig:telephony10.png"){width="700"}

2.  Request processing sequence
    1.  The application request is sent to the communicator through
        TAPI.
    2.  The communicator creates a user request based on the incoming
        request.
    3.  The user request is dispatch to communicator.
    4.  The communicator dispatches user request to server.
    5.  The server finds the plugin based on the modem name.
    6.  The server extracts the core object type based on the request
        command from plugin's core objects list.
    7.  The server dispatches the user request to the core object.
    8.  The core object dispatches the user request to dispatch a
        function based on the request command.
    9.  Pending request is formed, added to the queue, and sent to the
        logical HAL assigned for the core object.
    10. The logical HAL dispatches the request data to a CMUX channel
        dedicated to it.
    11. CMUX encodes the request data and dispatches it to the physical
        HAL.
    12. The physical HAL sends the request data to the modem.

    :   The following figure shows the telephony request processing
        sequence.
    :   ![](telephony11.png "fig:telephony11.png"){width="700"}

3.  Response processing sequence
    1.  Response data sent by the modem is received by the physical HAL.
    2.  The physical HAL dispatches the response data to CMUX.
    3.  CMUX decodes the received response data and dispatches the
        corresponding logical HAL based on the CMUX channel.
    4.  The logical HAL dispatches the decoded response data to the
        corresponding core object.
    5.  The core object processes the received response data and
        extracts the user request from the pending queue and sends the
        response data corresponding to the user request.
    6.  The user request extracts the communicator.
    7.  The received response data is sent to the corresponding
        communicator.
    8.  The communicator sends the response data to TAPI which
        communicates the response to application.

    :   The following figure shows the telephony response processing
        sequence.
    :   ![](telephony12.png "fig:telephony12.png"){width="700"}

4.  Indication processing sequence
    1.  Notification data sent by the modem is received by the physical
        HAL.
    2.  The physical HAL dispatches the notification data to CMUX.
    3.  CMUX decodes the received notification data and dispatches the
        corresponding logical HAL based on the CMUX channel registered
        for the notification.
    4.  The logical HAL dispatches the decoded notification data to the
        corresponding core object that registered for the notification.
    5.  The core object processes the received notification data and
        dispatches to the server.
    6.  The server dispatches the notification data to corresponding
        communicator.
    7.  The communicator sends the notification data to TAPI, which
        communicates the same to the application.

    :   The following figure shows the telephony indication processing
        sequence.
    :   ![](telephony13.png "fig:telephony13.png"){width="700"}

Application
===========

Appendix
========
