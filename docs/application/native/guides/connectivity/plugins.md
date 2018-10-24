# Service Access through Plugins


You can manage [various adaptors](#adaptors), which function as agents between the Service Adaptor Client and the related plugins, to take advantage of various services. You must use the adapters to [initialize a plugin](#start_plugin) to use its services. For example, the Auth and Storage adaptors allow you to access the Auth and Service Plugins to use services, such as Amazon, Box, Dropbox, Google Drive, OneDrive, and Sugarsync.

This feature is supported in mobile applications only.

The main feature of the Service Adaptor API is to connect adaptors to and disconnect them from the Service Adaptor Client though D-Bus. The Service Adaptor uses 2 path types:

- **Logical path**

  The path of the root file system. It starts from the root path ("/"), and you can use the path like in Linux (for example, "/folder1/image1.jpg").

- **Physical path**

  A specific URI used for the cloud server. Some clouds use a logical path, but others use a specific key or URL (for example, "/" is "ZmNhMWY2MTZlY2M1NDg4OGJmZDY4O" and "/folder1" is "2JI32UNJDWQEQWQWEADSSAD").

**Figure: Service Adaptor structure**

![Service Adaptor structure](./media/service_adaptor_structure.png)

<a name="adaptors"></a>
## Available Adaptors

The following adaptors are provided:

- Auth adaptor

  This adaptor manages authentication plugins. It allows you to:

  - Get the Auth Plugin list.
  - Set the Plugin.
  - Request the Channel Auth, such as the service name ("com.serviceadaptor.message"), app ID, service ID (0: contact, 1: free message), and mobile station identification number (IMSI).

- Storage adaptor

  This adaptor handles files transfers to and from a cloud. It allows you to:

  - [Download a server or thumbnail file](#File_download) and write it to a local file.
  - [Upload a local file](#File_upload) to a server path.
  - [Request the file status](#Files_listing).
  - Cancel, pause, and resume a file transfer.
  - [Remove a file from the storage](#File_remove).

- Contact adaptor

  This adaptor manages contact information in the Contact server, including the contact profiles and service registration information. It allows you to:

  - Reset contact information in the Contact server and upload native contact information from the device to the server.
  - Synchronize native contact information between the device and the Contact server according to the `[type]` field of each contact.
  - Get contact profiles and service registration information.
  - Set and update the device profile in the server.
  - Upload and delete profile image meta in the File server and set the my profile image to the Profile server.
  - Set and get the my profile privacy level
  - Set my presence ON/OFF information to the Presence server.

- Discovery adaptor

  This adaptor is a future development. Not in use yet.

- Message adaptor

  This adaptor manages chatting and messaging. It allows you to:

  - Create a chatroom, and invite people to (or end) a chat.
  - Get all unread messages.
  - Read or unseal a message.
  - Forward online or unread messages.
  - Save the call log.
  - Get the chat ID based on the phone number.

- Push adaptor

  This adaptor receives push notifications from a push service.

- Shop adaptor

  This adaptor allows you to:

  - Get a list of items.
  - Get item information for download.
  - Download an item.
  - Get the item panel URL.

<a name="start_plugin"></a>
## Plugin Initialization

To start a plugin, use the following process:

1. [Create a Service Adaptor](#prerequisites) with the `service_adaptor_create()` function.
2. With a valid Service Adaptor handler, [iterate through all installed plugins](#Starting_up) with the `service_adaptor_foreach_plugin()` function.
3. Inside the callback (invoked for each plugin), get the `plugin_uri` value, which is passed to the `service_adaptor_create_plugin()` function.
4. Request a start initialization for the service plugin with the `service_plugin_start()` function.

The following example starts all installed Auth and Storage plugins appending each `plugin_uri` to the `list` object:

```
bool
_plugin_iterator_cb(char *plugin_uri, int service_mask, void *user_data);

service_adaptor_h service_adaptor = NULL;
ret = service_adaptor_create(&service_adaptor);

Evas_Object *list;
ret = service_adaptor_foreach_plugin(service_adaptor, _plugin_iterator_cb, (void *)list);

bool
_plugin_iterator_cb(char *plugin_uri, int service_mask, void *user_data)
{
    Evas_Object *list = (Evas_Object *)user_data;

    if (!plugin_uri || !list)
        return false;

    if ((service_mask & SERVICE_PLUGIN_SERVICE_AUTH) && (service_mask & SERVICE_PLUGIN_SERVICE_STORAGE)) {
        elm_list_item_append(list, plugin_uri, NULL, NULL, _show_plugin_view, plugin_uri);

        service_plugin_h plugin = NULL;
        service_adaptor_create_plugin(service_adaptor, plugin_uri, &plugin);

        /* Hide this using config file or user input, because it is security information */
        service_plugin_add_property(plugin, SERVICE_PLUGIN_PROPERTY_APP_KEY, "enasvv4l8hdbmhn");
        service_plugin_add_property(plugin, SERVICE_PLUGIN_PROPERTY_APP_SECRET, "uqhl4pp8mo7hmgn");

        service_plugin_start(plugin, (SERVICE_PLUGIN_SERVICE_AUTH | SERVICE_PLUGIN_SERVICE_STORAGE));
    }

    return true;
}
```
<a name="prerequisites"></a>
## Prerequisites

To enable your application to use the Service Adaptor functionality:

1. To use the functions and data types of the [Service Adaptor](../../api/mobile/latest/group__SERVICE__ADAPTOR__MODULE.html) API, include the `<service_adaptor_client.h>` header file in your application:

   ```
   #include <service_adaptor_client.h>
   ```

2. Create a Service Adaptor handle using the `service_adaptor_create()` function:

   ```
   static service_adaptor_h service_adaptor;

   void
   service_adaptor_init()
   {
       int ret = service_adaptor_create(&service_adaptor);

       if (ret != SERVICE_ADAPTOR_ERROR_NONE)
           /* Error handling */
   }
   ```

3. When no longer needed, destroy the Service Adaptor handle and release all its resources with the `service_adaptor_destroy()` function:

   ```
   static void
   service_adaptor_deinit(int result, void *user_data)
   {
       int ret = service_adaptor_destroy(service_adaptor);

       if (ret != SERVICE_ADAPTOR_ERROR_NONE)
           /* Error handling */
   }
   ```

<a name="Starting_up"></a>
## Retrieving Available Service Plugins

To retrieve available service plugins:

1. Create a data structure for storing the service plugin handles:

   ```
   struct plugin_list_item_s {
       service_plugin_h plugin;
       struct plugin_list_item_s *next;
   };

   typedef struct plugin_list_item_s plugin_list_item_t;
   typedef plugin_list_item_t plugin_list_t;
   typedef plugin_list_item_t* plugin_list_item_h;
   typedef plugin_list_t* plugin_list_h;
   ```

2. Retrieve a list of available service plugins:

   ```
   static plugin_list_t plugins;

   /* Handle a plugin from the plugin list */
   static bool
   _plugin_iterator_cb(char *plugin_uri, int service_mask, void *user_data)
   {
       plugin_list_item_h plugin_item = (plugin_list_item_h)calloc(1, sizeof(plugin_list_item_t));

       /* Create the plugin handle */
       service_adaptor_create_plugin(service_adaptor, plugin_uri, &plugin_item->plugin);

       /* Set the plugin properties */
       service_plugin_add_property(plugin_item->plugin, SERVICE_PLUGIN_PROPERTY_APP_KEY, "app_key");
       service_plugin_add_property(plugin_item->plugin, SERVICE_PLUGIN_PROPERTY_APP_SECRET, "app_secret");

       /* Initialize the plugin */
       service_plugin_start(plugin_item->plugin, service_mask);

       return true;
   }

   /* Retrieve the plugin list */
   void
   plugin_lookup()
   {
       /* Iterate through the plugin list */
       /* Use the callback to separately handle each plugin in the list */
       int ret = service_adaptor_foreach_plugin(service_adaptor, _plugin_iterator_cb, &plugins);

       if (ret == SERVICE_ADAPTOR_ERROR_NO_DATA)
           /* Handle no plugins */
       else if (ret != SERVICE_ADAPTOR_ERROR_NONE)
           /* Error handling */
   }
   ```

<a name="Files_listing"></a>
## Retrieving Files

To retrieve information about all the files in the storage:

1. Retrieve the list of files using the `service_storage_get_file_list()` function with the storage service plugin handle as the first parameter and the file list callback as the third parameter:

   ```
   void
   plugin_get_file_list(service_plugin_h plugin)
   {
       service_storage_get_file_list(plugin, "/", _service_storage_result_cb, NULL);
   }
   ```

2. Define the file list callback. In the callback, iterate through the list using the `service_storage_file_list_foreach_file()` function with the file callback as the second parameter. The file callback is called separately for each file in the list.

   ```
   /* Handle the returned file list */
   static void
   _service_storage_result_cb(int result, service_storage_file_list_h list, void *user_data)
   {
       /* Iterate through the list */
       /* Use the callback to separately handle each file in the list */
       service_storage_file_list_foreach_file(list, _file_iterator_cb, NULL);
   }
   ```

3. Define the file callback. In the callback, use the `service_storage_file_XXX()` functions to retrieve information about the current file.

   ```
   /* Handle a file from the file list */
   static bool
   _file_iterator_cb(service_storage_file_h file, void *user_data)
   {
       char *name = NULL;
       unsigned long long size = 0;
       bool is_dir = false;

       /* Get basic file information */
       service_storage_file_is_dir(file, &is_dir);
       service_storage_file_get_size(file, &size);
       service_storage_file_get_logical_path(file, &name);

       return true;
   }
   ```

<a name="File_upload"></a>
## Uploading Files

To upload a file to the storage:

1. Define the callbacks for monitoring the upload task progress and state during the upload:

   ```
   static void
   task_progress_cb(unsigned long long progress, unsigned long long total, void *user_data)
   {
       /* Handle the task progress */
   }

   static void
   task_state_cb(service_storage_task_state_e state, void *user_data)
   {
       /* Handle task states */
       switch (state) {
       case SERVICE_STORAGE_TASK_IN_PROGRESS:
           break;
       case SERVICE_STORAGE_TASK_COMPLETED:
           break;
       case SERVICE_STORAGE_TASK_CANCELED:
           break;
       case SERVICE_STORAGE_TASK_FAILED:
           break;
       }
   }
   ```

2. Create an upload task:

   ```
   void
   plugin_upload_file(service_plugin_h plugin, const char *local_path, const char *storage_path)
   {
       service_storage_task_h task;

       /* Upload a local file to the storage */
       if (service_storage_create_upload_task(plugin, local_path, storage_path, &task) != SERVICE_ADAPTOR_ERROR_NONE) {
           /* Error handling */

           return;
       }
   ```

3. Register the defined callbacks:

   ```
       /* Register the task progress change callback */
       if (service_storage_set_task_progress_cb(task, task_progress_cb, NULL) != SERVICE_ADAPTOR_ERROR_NONE) {
           /* Error handling */

           return;
       }

       /* Register the task state change callback */
       if (service_storage_set_task_state_changed_cb(task, task_state_cb, NULL) != SERVICE_ADAPTOR_ERROR_NONE) {
           /* Error handling */

           return;
       }
   ```

4. Start the upload task:

   ```
       if (service_storage_start_task(task) != SERVICE_ADAPTOR_ERROR_NONE) {
           /* Error handling */

           return;
       }
   }
   ```

<a name="File_download"></a>
## Downloading Files

To download a file from the storage:

1. Create a download task:

   ```
   void
   plugin_download_file(service_plugin_h plugin, const char *storage_path, const char *local_path)
   {
       service_storage_task_h task;

       /* Download a file from the storage to a local directory */
       if (service_storage_create_download_task(plugin, storage_path, local_path, &task) != SERVICE_ADAPTOR_ERROR_NONE) {
           /* Error handling */

           return;
       }
   ```

2. Register callbacks for monitoring the download task progress and state:

   ```
       /* Register the task progress change callback */
       if (service_storage_set_task_progress_cb(task, task_progress_cb, NULL) != SERVICE_ADAPTOR_ERROR_NONE) {
           /* Error handling */

           return;
       }

       /* Register the task state change callback */
       if (service_storage_set_task_state_changed_cb(task, task_state_cb, NULL) != SERVICE_ADAPTOR_ERROR_NONE) {
           /* Error handling */

           return;
       }
   ```

   The file upload and download processes use the same callback types. You can use the callbacks defined for the file upload, or define separate callbacks, as needed.

3. Start the download task:

   ```
       if (service_storage_start_task(task) != SERVICE_ADAPTOR_ERROR_NONE) {
           /* Error handling */

           return;
       }
   }
   ```

<a name="File_remove"></a>
## Removing Files

To remove a file from the storage, use the `service_storage_remove()` function:

```
/* Handle the results of removing the file */
static void
file_remove_cb(int result, void *user_data)
{
    if (result != SERVICE_ADAPTOR_ERROR_NONE)
        /* Error handling */
}

/* Remove the file */
void
plugin_remove_file(service_plugin_h plugin, const char *file)
{
    int ret = service_storage_remove(plugin, file, file_remove_cb, NULL);

    if (ret != SERVICE_ADAPTOR_ERROR_NONE)
        /* Error handling */
}
```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
