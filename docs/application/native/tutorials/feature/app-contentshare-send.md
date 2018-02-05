
# Sending Content to Other Applications

You can send various types of content to other applications, including
text, binaries, and files. The following sections provide you with the
fundamental building blocks for sharing your application data with other
applications.


## Sending Text

The most common content sharing use case is sending text to another
application. For example, a Web browser can share the URL of the
currently visited site with other applications, such as a messenger or
email application, to allow the user to send the URL to their friends.

Use the `APP_CONTROL_OPERATION_SHARE` operation and the `text/plain`
MIME type to create an application control request, and define the text
content to be shared in the `APP_CONTROL_DATA_TEXT` extra data:

```c++
#include <app_control.h>

app_control_h app_control;

app_control_create(&app_control);

app_control_set_operation(app_control, APP_CONTROL_OPERATION_SHARE);
app_control_set_mime(app_control, "text/plain");
app_control_add_extra_data(app_control, APP_CONTROL_DATA_TEXT, "Hello, World!");

app_control_send_launch_request(app_control, NULL, NULL);
```

The above example has no explicit designation of the application to be
called. When you request an implicit launch, the application launcher
framework determines which application to launch by comparing the
conditions: operation, URI (or scheme), and MIME type. If only one
application is found to match the given conditions, that application is
launched. If multiple matching applications are found, the application
selector is shown and the user can select the application they want.

> **Note**  
> When using application controls, pay attention to the following:  
> - Since Tizen 2.4, application controls that launch [service applications](../../guides/app-management/service-app.md) outside the current package are not supported. Because of this, a     service application can only be launched explicitly by an    application in the same package.
> - The operation is mandatory information for sending a launch request.    If the operation is not specified, the `APP_CONTROL_OPERATION_DEFAULT` operation is used. In that case, the application ID is mandatory to explicitly launch an application.


## Sending Binaries

Depending on the number of binary content items to be shared, you can
use the `APP_CONTROL_OPERATION_SHARE` (for a single item) or
`APP_CONTROL_OPERATION_MULTI_SHARE` (for multiple items) operation. The
location of the content to be shared is defined in the
`APP_CONTROL_DATA_PATH` extra data or extra data array.

The following example demonstrates how to share a single binary content
item and multiple items:

```c++
/* Single item */
#define PATH_MAX 128

char *shared_res_path = app_get_shared_resource_path();
char img_path[PATH_MAX] = {0,};
snprintf(img_path, PATH_MAX, "%s/image.jpg", shared_res_path);
free(shared_res_path);

app_control_h service;
app_control_create(&service);

app_control_set_operation(service, APP_CONTROL_OPERATION_SHARE);
app_control_set_mime(service, "image/*");
app_control_add_extra_data(service, APP_CONTROL_DATA_PATH, img_path);
app_control_set_launch_mode(service, APP_CONTROL_LAUNCH_MODE_GROUP);

app_control_send_launch_request(service, NULL, NULL);
app_control_destroy(service);

/* Multiple items */
#define PATH_MAX 128

char *shared_res_path = app_get_shared_resource_path();
char img1_path[PATH_MAX] = {0,};
char img2_path[PATH_MAX] = {0,};
const char *path_array[2] = {img1_path, img2_path};
snprintf(img1_path, PATH_MAX, "%s/image.jpg", shared_res_path);
snprintf(img2_path, PATH_MAX, "%s/image2.jpg", shared_res_path);
free(shared_res_path);

app_control_h service;
app_control_create(&service);

app_control_set_operation(service, APP_CONTROL_OPERATION_MULTI_SHARE);
app_control_set_mime(service, "image/*");
app_control_add_extra_data_array(service, APP_CONTROL_DATA_PATH, path_array, 2);
app_control_set_launch_mode(service, APP_CONTROL_LAUNCH_MODE_GROUP);

app_control_send_launch_request(service, NULL, NULL);
app_control_destroy(service);
```

If you try to share a set of files with different MIME types, use
`<type>/*` or `*/*`. For example, if you send `video/mp4` and
`audio/ogg`, the MIME type must be `*/*`.


## Sending Files

When sharing files, you can use the `app_control_set_uri()` function to
set the file URI with the `file://` scheme.

Since Tizen 2.4, if the second parameter of the `app_control_set_uri()`
function starts with `file://`, and it is a regular file in your
application's data path which can be obtained by calling the
`app_get_data_path()` function, the file is shared with the called
application. The framework grants a temporary permission to the called
application for this file, and revokes it when the called application is
terminated. The called application can just read the file.

The following example launches a viewer application with the operation,
URI, and MIME type:

```c++
#include <app.h>
#include <dlog.h>

#define TAG "MY_TAG"
#define PATH_MAX 128

app_control_h app_control;
char* data_path = app_get_data_path();

char file_path[PATH_MAX] = {0,};
snprintf(file_path, PATH_MAX, "%s/image.jpg", data_path);
free(data_path);

app_control_create(&app_control);
app_control_set_operation(app_control, APP_CONTROL_OPERATION_VIEW);
app_control_set_uri(app_control, file_path);
app_control_set_mime(app_control, "image/*");

if (app_control_send_launch_request(app_control, NULL, NULL) == APP_CONTROL_ERROR_NONE)
    dlog_print(DLOG_INFO, TAG, "Succeeded to launch a viewer app.");
else
    dlog_print(DLOG_ERROR, TAG, "Failed to launch a viewer app.");

app_control_destroy(app_control);
```
