<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
	<meta http-equiv="X-UA-Compatible" content="IE=9" />
	<link rel="stylesheet" type="text/css" href="../../css/styles.css" />
	<link rel="stylesheet" type="text/css" href="../../css/snippet.css" />
	<script type="text/javascript" src="../../scripts/snippet.js"></script>
	<script type="text/javascript" src="../../scripts/jquery.util.js" charset="utf-8"></script>
	<script type="text/javascript" src="../../scripts/common.js" charset="utf-8"></script>
	<script type="text/javascript" src="../../scripts/core.js" charset="utf-8"></script>
	<script type="text/javascript" src="../../scripts/search.js" charset="utf-8"></script>
  <title>Data Control</title>
 </head>
 <body onload="prettyPrint()" style="overflow: auto;">

 <div id="toc-navigation">
	<div id="profile">
		<p><img alt="Mobile native" src="../../images/mobile_s_n.png"/> <img alt="Wearable native" src="../../images/wearable_s_n.png"/></p>
	</div>

	<div id="toc_border"><div id="toc">
		<p class="toc-title">Dependencies</p>
		<ul class="toc">
			<li>Tizen 2.4 and Higher for Mobile</li>
			<li>Tizen 2.3.1 and Higher for Wearable</li>
		</ul>
		<p class="toc-title">Content</p>
		<ul class="toc">
			<li><a href="#prerequisites">Prerequisites</a></li>
			<li><a href="#map1">Working with Map-type Data Controls</a></li>
			<li><a href="#map2">Working with SQL-type Data Controls</a></li>
			<li><a href="#map3">Monitoring Data Changes</a></li>
			<li><a href="#export">Data Control Export</a></li>
		</ul>
		<p class="toc-title">Related Info</p>
		<ul class="toc">
			<li><a href="../../../../org.tizen.native.mobile.apireference/group__CAPI__DATA__CONTROL__MODULE.html">Data Control API for Mobile Native</a></li>
			<li><a href="../../../../org.tizen.native.wearable.apireference/group__CAPI__DATA__CONTROL__MODULE.html">Data Control API for Wearable Native</a></li>
		</ul>
	</div></div>
</div>

<div id="container"><div id="contents"><div class="content">

<h1 id="data_controls" name="data_controls">Data Control</h1>
<p>The data control is a standard mechanism for exchanging specific data between applications.</p>

<p>A provider application shares its data, and a consumer application can request the shared data. All applications can function as consumers and request data shared by other applications using a data control. However, only service applications can function as providers and share their own data.</p>

<p>The main features of the Data Control API include:</p>
<ul>
<li>Working with map-type data controls
<p>You can <a href="#map1">use a key-value-type data control</a> to access data exported by service applications. You can also define a key-value-type data control provider to export specific data from your service application.</p>
<p>The consumer sends a request to the provider to get, set, add, or remove map-type data. The provider processes the request and sends a response back to the consumer.</p>
</li>
<li>Working with SQL-type data controls
<p>You can <a href="#map2">use a SQL-type data control</a> to access specific data exported by service applications. You can also define a SQL-type data control provider to export specific data from your service application.</p>
<p>The consumer sends a request to the provider to insert, update, select, or delete SQL-type data. The provider processes the request and sends a response back to the consumer.</p>
</li>
<li>Monitoring data changes
<p>You can <a href="#map3">monitor data changes and provide notifications about them</a>. The available notification types are listed in the <code>data_control_data_change_type_e</code> enumerator (in <a href="../../../../org.tizen.native.mobile.apireference/group__CAPI__DATA__CONTROL__MODULE.html#ga09ee00edc0c08676b2fa241f30fab378">mobile</a> and <a href="../../../../org.tizen.native.wearable.apireference/group__CAPI__DATA__CONTROL__MODULE.html#ga09ee00edc0c08676b2fa241f30fab378">wearable</a> applications).</p></li>
</ul>
<p>To create a provider, you must <a href="#export">export its provider functionalities</a> in the application project settings in the IDE. For the consumer to access shared data, it must know the provider ID and data ID.</p>

  <p align="center"><strong>Figure: Data control mechanism</strong></p>
  <p align="center"><img alt="Data control mechanism" src="../../images/datacontrol.png" /></p>

<h2 id="prerequisites">Prerequisites</h2>

<p>The data control use cases run 2 applications. Each application plays a different role: one as the consumer, the other as the provider.</p>

<p>To enable your application to use the data control functionality:</p>
<ol>
<li>
<p>To use the Data Control API (in <a href="../../../../org.tizen.native.mobile.apireference/group__CAPI__DATA__CONTROL__MODULE.html">mobile</a> and <a href="../../../../org.tizen.native.wearable.apireference/group__CAPI__DATA__CONTROL__MODULE.html">wearable</a> applications), the consumer has to request permission by adding the following privileges to the <code>tizen-manifest.xml</code> file:</p>
<pre class="prettyprint">
&lt;privileges&gt;
   &lt;privilege&gt;http://tizen.org/privilege/datasharing&lt;/privilege&gt;
   &lt;privilege&gt;http://tizen.org/privilege/appmanager.launch&lt;/privilege&gt;
&lt;/privileges&gt;
</pre>
</li>
<li>
<p>For the provider, in the Tizen Studio, double-click <strong>tizen-manifest.xml</strong>, and in the manifest editor, go to <strong>Advanced &gt; Data Control</strong>, and click <strong>+</strong> to add the provider details. Add the <strong>Read</strong> and <strong>Write</strong> access rights to both <strong>SQL</strong> and <strong>Map</strong> types.</p>
<p>You can set the data access to be trusted, allowing other applications signed with the same certificate to access the data. You can also define privileges to restrict access to applications having the specific privileges.</p>
<p>The following code example shows how the <code>&lt;datacontrol&gt;</code> element is consequently added to the <code>tizen-manifest.xml</code> file:</p>
<pre class="prettyprint">
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;manifest xmlns="http://tizen.org/ns/packages" api-version="4.0"
          package="@PACKAGE_NAME@" version="@VERSION@" install-location="internal-only"&gt;
   &lt;label&gt;datacontrolprovider&lt;/label&gt;
   &lt;author email="PUT YOUR EMAIL" href="www.tizen.org"&gt;PUT YOUR NAME&lt;/author&gt;
   &lt;description&gt;datacontrolprovider&lt;/description&gt;
   &lt;service-application appid="org.tizen.datacontrolprovider"
                   exec="datacontrolprovider"
                   nodisplay="true" multiple="false" type="capp" taskmanage="true"
                   auto-restart="false" on-boot="false"&gt;
      <span class="highlight">&lt;datacontrol providerid = "Your Provider ID" access="ReadWrite" type="Sql" trusted="True"&gt;</span>
         <span class="highlight">&lt;privilege&gt;http://tizen.org/privilege/contact.read&lt;/privilege&gt;</span>
         <span class="highlight">&lt;privilege&gt;http://tizen.org/privilege/email&lt;/privilege&gt;</span>
      <span class="highlight">&lt;/datacontrol&gt;</span>
      <span class="highlight">&lt;datacontrol providerid = "Your Provider ID" access="ReadWrite" type="Map" trusted="False"/&gt;</span>
   &lt;/service-application&gt;
   &lt;privileges&gt;
      &lt;privilege&gt;http://tizen.org/privilege/datasharing&lt;/privilege&gt;
   &lt;/privileges&gt;
&lt;/manifest&gt;
</pre>

</li>
<li>
<p>To use the functions and data types of the Data Control API, include the <code>&lt;data_control.h&gt;</code> header file in your application:</p>
<pre class="prettyprint">
#include &lt;data_control.h&gt;

#include &lt;sqlite3.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;glib.h&gt;
#include &lt;string.h&gt;
</pre>
<p>To execute the applications in the following use cases, the <code>&lt;sqlite3.h&gt;</code>, <code>&lt;stdlib.h&gt;</code>, <code>&lt;glib.h&gt;</code>, and <code>&lt;string.h&gt;</code> header files have to be included too.</p>
</li>
</ol>

 <h2 id="map1" name="map1">Working with Map-type Data Controls</h2>
<p>In the consumer, you must first get the unique map-type <code>datacontrol_h</code> instance using the <code>data_control_map_create()</code>, <code>data_control_map_set_provider_id()</code>, or <code>data_control_map_set_data_id()</code> function. Afterwards, you can send requests to the provider using the <code>data_control_map_get()</code>, <code>data_control_map_set()</code>, <code>data_control_map_add()</code>, and <code>data_control_map_remove()</code> functions.</p>

<p>The provider returns a response to the consumer. The consumer can handle the response in a callback of the <code>data_control_map_response_cb</code> struct (in <a href="../../../../org.tizen.native.mobile.apireference/structdata__control__map__response__cb.html">mobile</a> and <a href="../../../../org.tizen.native.wearable.apireference/structdata__control__map__response__cb.html">wearable</a> applications), which is triggered when the provider finishes the requested operation.</p>
<div class="note">
        <strong>Note</strong>
		Since Tizen 4.0, you can use the <code>data_control_map_bind_response_cb()</code> function, which binds a callback to a provider handle. This allows you to register multiple callbacks for a given provider ID.
</div>
<p>To get, set, add, and remove map-type data:</p>

<ol>
<li id="provider">Implement the provider application:
<ol type="a"><li>The provider stores and provides data to the consumer. The provider has 4 operations that the consumer can request: get, set, add, and remove.

<p>Implement the callbacks to react to the requests from the consumer:</p>

<pre class="prettyprint">
struct map_data {
    char **str_arr;
    int arr_size;
};
typedef struct map_data map_data_s;

static GHashTable *map_repository_test;

/* Callback for handling the get operation request */
void
get_value_request_cb(int request_id, data_control_h provider, const char *key,
                     void *user_data)
{
    map_data_s* map_data = (map_data_s*)g_hash_table_lookup(map_repository_test, key);

    int ret_value_count = 0;
    char **val_arr = NULL;
    if (map_data != NULL) {
        val_arr = map_data-&gt;str_arr;
        ret_value_count = map_data-&gt;arr_size;
    }

    int ret = data_control_provider_send_map_get_value_result(request_id, val_arr,
                                                              ret_value_count);
    if (ret != DATA_CONTROL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "send_map_get_result failed with error: %d", ret);
    else
        dlog_print(DLOG_INFO, LOG_TAG, "Get value success request_id: %d", request_id);
}

/* Callback for handling the set operation request */
void
set_value_request_cb(int request_id, data_control_h provider, const char *key,
                     const char *old_value, const char *new_value, void *user_data)
{
    map_data_s* map_data = (map_data_s*)g_hash_table_lookup(map_repository_test, key);
    if (map_data != NULL) {
        for (int i = 0; i &lt; map_data-&gt;arr_size; i++) {
            if (strcmp(map_data-&gt;str_arr[i], old_value) == 0)
                map_data-&gt;str_arr[i] = g_strdup(new_value);
        }
    }

    int ret = data_control_provider_send_map_result(request_id);
    if (ret != DATA_CONTROL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "send_map_result failed with error: %d", ret);
    else
        dlog_print(DLOG_INFO, LOG_TAG, "Set value success request_id: %d", request_id);
}

/* Callback for handling the add operation request */
void
add_value_request_cb(int request_id, data_control_h provider, const char *key,
                     const char *value, void *user_data)
{
    map_data_s* map_data = (map_data_s*)g_hash_table_lookup(map_repository_test, key);

    if (map_data == NULL) {
        map_data = (map_data_s*)(g_malloc(sizeof(*map_data)));
        map_data-&gt;arr_size = 0;
        map_data-&gt;str_arr = (char**)calloc(1, sizeof(char*));
        map_data-&gt;str_arr[0] = g_strdup(value);
        g_hash_table_insert(map_repository_test, g_strdup(key), map_data);
    } else {
        char **new_arr = (char**)calloc(map_data-&gt;arr_size + 2, sizeof(char*));
        for (int i = 0; i &lt; map_data-&gt;arr_size; i++)
            new_arr[i] = g_strdup(map_data-&gt;str_arr[i]);
        free(map_data-&gt;str_arr);
        new_arr[map_data-&gt;arr_size] = g_strdup(value);
        map_data-&gt;str_arr = g_strdupv(new_arr);
        free(new_arr);
    }
    map_data-&gt;arr_size += 1;

    int ret = data_control_provider_send_map_result(request_id);
    if (ret != DATA_CONTROL_ERROR_NONE) {
        dlog_print(DLOG_ERROR, LOG_TAG, "send_map_result failed with error: %d", ret);
    } else {
        dlog_print(DLOG_INFO, LOG_TAG, "Add value success request_id: %d %d %s",
                   request_id, map_data-&gt;arr_size, map_data-&gt;str_arr[0]);
    }
}

/* Callback for handling the remove operation request */
void
remove_value_request_cb(int request_id, data_control_h provider, const char *key,
                        const char *value, void *user_data)
{
    map_data_s* map_data = (map_data_s*)g_hash_table_lookup(map_repository_test, key);

    if (map_data != NULL) {
        int size = map_data-&gt;arr_size;
        for (int i = 0; i &lt; size; i++) {
            if (strcmp(map_data-&gt;str_arr[i], value) == 0) {
                free(map_data-&gt;str_arr[i]);
                map_data-&gt;arr_size--;
            }
        }
        if (map_data-&gt;arr_size == 0) {
            if (!g_hash_table_remove(map_repository_test, key)) {
                dlog_print(DLOG_ERROR, LOG_TAG, "remove value failed -%s", key);

                return;
            }
        }
    }

    int ret = data_control_provider_send_map_result(request_id);
    if (ret != DATA_CONTROL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "send_map_result failed with error: %d", ret);
    else
        dlog_print(DLOG_INFO, LOG_TAG, "Remove value Success");
}
</pre>
</li>
<li>
<p>Register the operation callbacks within the <code>app_create()</code> function (generated by the Tizen Studio) using the <code>data_control_provider_map_register_cb()</code> function:</p>
<pre class="prettyprint">
void
__free_key(gpointer data)
{
    if (data) {
        g_free(data);
        data = NULL;
        dlog_print(DLOG_INFO, LOG_TAG, "Remove key");
    }
}

void
__free_data(gpointer data)
{
    if (data) {
        g_free(data);
        data = NULL;
        dlog_print(DLOG_INFO, LOG_TAG, "Remove value");
    }
}

data_control_provider_map_cb map_callback;
void
initialize_datacontrol_provider()
{
    map_repository_test = g_hash_table_new_full(g_str_hash, g_str_equal,
                                                __free_key, __free_data);

    map_callback.get_cb = get_value_request_cb;
    map_callback.add_cb = add_value_request_cb;
    map_callback.remove_cb = remove_value_request_cb;
    map_callback.set_cb = set_value_request_cb;

    int result = data_control_provider_map_register_cb(&amp;map_callback);
    if (result != DATA_CONTROL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "data_control_provider_map_register_cb failed with error: %d",
                   result);
    else
        dlog_print(DLOG_INFO, LOG_TAG, "Provider map register success");
}

static bool
app_create(void *data)
{
    initialize_datacontrol_provider()

    return true;
}
</pre>
</li>
</ol>
</li>
<li id="consumer">Implement the consumer application:
<ol type="a"><li>The consumer sends requests for the get, set, add, and remove operations to the provider, and receives the results as a response from the provider.

<p>Implement the response callbacks, which receive the request result and data from the provider:</p>
<pre class="prettyprint">
/* Callback for the get operation response */
void
map_get_response_cb(int request_id, data_control_h provider,
                    char **ret_value_list, int ret_value_count, bool provider_ret,
                    const char *error, void *user_data)
{
    if (provider_ret) {
        dlog_print(DLOG_INFO, LOG_TAG,
                   "The get operation is successful. Value count: %d ", ret_value_count);
        for (int i = 0; i &lt; ret_value_count; i++)
            dlog_print(DLOG_INFO, LOG_TAG, "(%d) Return value: %s ",
                       i, ret_value_list[i]);
    } else {
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "The get operation for the request %d failed. error message: %s",
                   request_id, error);
    }
}

/* Callback for the set operation response */
void
map_set_response_cb(int request_id, data_control_h provider, bool provider_ret,
                    const char *error, void *user_data)
{
    if (provider_ret) {
        dlog_print(DLOG_INFO, LOG_TAG, "The set operation is successful");
    } else {
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "The set operation for the request %d failed. error message: %s",
                   request_id, error);
    }
}

/* Callback for the add operation response */
void
map_add_response_cb(int request_id, data_control_h provider, bool provider_ret,
                    const char *error, void *user_data)
{
    if (provider_ret) {
        dlog_print(DLOG_INFO, LOG_TAG, "The add operation is successful");
    } else {
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "The add operation for the request %d failed. error message: %s",
                   request_id, error);
    }
}

/* Callback for the remove operation response */
void
map_remove_response_cb(int request_id, data_control_h provider, bool provider_ret,
                       const char *error, void *user_data)
{
    if (provider_ret) {
        dlog_print(DLOG_INFO, LOG_TAG, "The remove operation is successful");
    } else {
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "The remove operation for the request %d failed. error message: %s",
                   request_id, error);
    }
}
</pre>
</li>
<li>
<p>To identify the provider and data, initialize a data control handler within the <code>app_create()</code> function generated by the Tizen Studio:</p>
<pre class="prettyprint">
data_control_map_response_cb map_callback;
void
initialize_datacontrol_consumer(appdata_s *ad)
{
    const char *provider_id = Your Provider ID;
    const char *data_id = "table";
    int ret;

    /* Create data control handler */
    ret = data_control_map_create(&amp;(ad-&gt;provider_h));
    if (ret != DATA_CONTROL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "creating data control provider failed with error: %d", ret);
    ret = data_control_map_set_provider_id(ad-&gt;provider_h, provider_id);
    if (ret != DATA_CONTROL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "setting provider id failed with error: %d", ret);
    ret = data_control_map_set_data_id(ad-&gt;provider_h, data_id);
    if (ret != DATA_CONTROL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "setting data id failed with error: %d", ret);

    /* Set response callbacks */
    map_callback.get_cb = map_get_response_cb;
    map_callback.set_cb = map_set_response_cb;
    map_callback.add_cb = map_add_response_cb;
    map_callback.remove_cb = map_remove_response_cb;

    /* Register response callbacks */
    ret = data_control_map_register_response_cb(ad-&gt;provider_h, &amp;map_callback, NULL);
    if (ret != DATA_CONTROL_ERROR_NONE) {
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "Registering the callback function failed with error: %d", ret);

        if (ret == DATA_CONTROL_ERROR_IO_ERROR)
            dlog_print(DLOG_ERROR, LOG_TAG, "I/O error");
        else
            dlog_print(DLOG_ERROR, LOG_TAG, "Out of memory");
    }

    int req_id = 0;

    /* Send a request to add a value */
    const char *key = "key";
    const char *value = "value";
    data_control_map_add(ad-&gt;provider_h, key, value, &amp;req_id);

    /* Send a request to get a value */
    data_control_map_get(ad-&gt;provider_h, key, &amp;req_id);

    /* Send a request to set a value */
    const char *old_value = "old value";
    const char *new_value = "new value";
    data_control_map_set(ad-&gt;provider_h, key, old_value, new_value, &amp;req_id);

    /* Send a request to remove a value */
    data_control_map_remove(ad-&gt;provider_h, key, value, &amp;req_id);
}

static bool
app_create(void *data)
{
    initialize_datacontrol_consumer(ad);

    return true;
}
</pre>
</li>
</ol></li>
</ol>


<h2 id="map2" name="map2">Working with SQL-type Data Controls</h2>
<p>In the consumer, you must first get the unique SQL-type <code>datacontrol_h</code> instance using the <code>data_control_sql_create()</code>, <code>data_control_sql_set_provider_id()</code>, or <code>data_control_sql_set_data_id()</code> function. Afterwards, you can send requests to the provider using the <code>datacontrol_sql_select()</code>, <code>data_control_sql_insert()</code>, <code>data_control_sql_update()</code>, and <code>data_control_sql_delete()</code> functions.</p>
<p>The provider returns a response to the consumer. The consumer can handle the response in a callback of the <code>data_control_sql_response_cb</code> struct (in <a href="../../../../org.tizen.native.mobile.apireference/structdata__control__sql__response__cb.html">mobile</a> and <a href="../../../../org.tizen.native.wearable.apireference/structdata__control__sql__response__cb.html">wearable</a> applications), which is triggered when the provider finishes the requested operation.</p>
<div class="note">
        <strong>Note</strong>
		Since Tizen 4.0, you can use the <code>data_control_sql_bind_response_cb()</code> function, which binds a callback to a provider handle. This allows you to register multiple callbacks for a given provider ID.
</div>
<p>To insert, select, update, and delete SQL-type data:</p>

<ol>
<li id="provider2">Implement the provider application:
<ol type="a"><li>The provider stores and provides data to the consumer. The provider has 4 operations that the consumer can request: insert, select, update, and delete.

<p>Implement the callbacks to react to the requests from the consumer:</p>

<pre class="prettyprint">
data_control_provider_sql_cb *sql_callback;
static sqlite3* db;

/* Callback for handling the insert operation request */
void
insert_request_cb(int request_id, data_control_h provider, bundle *insert_data,
                  void *user_data)
{
    char* command = data_control_provider_create_insert_statement(provider,
                                                                  insert_data);
    int ret = sqlite3_exec(db, command, NULL, NULL, NULL);

    if (ret != SQLITE_OK) {
        data_control_provider_send_error(request_id, sqlite3_errmsg(db));
        free(command);

        return;
    }
    dlog_print(DLOG_INFO, LOG_TAG, "[insert_request_cb] insert success");

    long long inserted_row_id = sqlite3_last_insert_rowid(db);
    ret = data_control_provider_send_insert_result(request_id, inserted_row_id);
    if (ret != DATA_CONTROL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "insert_send_result failed with error: %d", ret);
    dlog_print(DLOG_INFO, LOG_TAG, "[insert_request_cb] send result success");

    free(command);
}

/* Callback for handling the select operation request */
void
select_request_cb(int request_id, data_control_h provider, const char **column_list,
                  int column_count, const char *where, const char *order,
                  void *user_data)
{
    sqlite3_stmt* sql_stmt = NULL;

    char* command = data_control_provider_create_select_statement(provider,
                                                                  column_list,
                                                                  column_count, where,
                                                                  order);
    int ret = sqlite3_prepare_v2(db, command, strlen(command), &amp;sql_stmt, NULL);
    if (ret != SQLITE_OK) {
        data_control_provider_send_error(request_id, sqlite3_errmsg(db));
        free(command);

        return;
    }

    ret = data_control_provider_send_select_result(request_id, (void *)sql_stmt);
    if (ret != DATA_CONTROL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "select_send_result failed with error: %d", ret);
    dlog_print(DLOG_INFO, LOG_TAG, "[select_request_cb] send result success");

    sqlite3_finalize(sql_stmt);
    free(command);
}

/* Callback for handling the update operation request */
void
update_request_cb(int request_id, data_control_h provider, bundle *update_data,
                  const char *where, void *user_data)
{
    char* command = data_control_provider_create_update_statement(provider,
                                                                  update_data, where);
    int ret = sqlite3_exec(db, command, NULL, NULL, NULL);
    if (ret != SQLITE_OK) {
        data_control_provider_send_error(request_id, sqlite3_errmsg(db));
        free(command);

        return;
    }

    ret = data_control_provider_send_update_result(request_id);
    if (ret != DATA_CONTROL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "update_send_result failed with error: %d", ret);
    dlog_print(DLOG_INFO, LOG_TAG, "[update_request_cb] send result success");

    free(command);
}

/* Callback for handling the delete operation request */
void
delete_request_cb(int request_id, data_control_h provider, const char *where,
                  void *user_data)
{
    dlog_print(DLOG_INFO, LOG_TAG, "[delete_request_cb] request_id(%d)", request_id);
    char* command = data_control_provider_create_delete_statement(provider, where);
    int ret = sqlite3_exec(db, command, NULL, NULL, NULL);
    if (ret != SQLITE_OK) {
        data_control_provider_send_error(request_id, sqlite3_errmsg(db));
        free(command);

        return;
    }

    ret = data_control_provider_send_delete_result(request_id);
    if (ret != DATA_CONTROL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "delete_send_result failed with error: %d", ret);
    dlog_print(DLOG_INFO, LOG_TAG, "[delete_request_cb] delete success");

    free(command);
}
</pre>
</li>
<li>
<p>Register the operation callbacks using the <code>data_control_provider_sql_register_cb()</code> function and create the database:</p>
<pre class="prettyprint">
int
create_database()
{
    dlog_print(DLOG_INFO, LOG_TAG, "%s%s", app_get_data_path(), "test.db");

    int open_flags = (SQLITE_OPEN_READWRITE | SQLITE_OPEN_CREATE);

    int ret = sqlite3_open_v2(Your DB Path, &amp;db, open_flags, NULL);
    if (ret != SQLITE_OK) {
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "database creation failed with error: %d", ret);

        return ret;
    }

    char* sql_command = "CREATE TABLE IF NOT EXISTS Dictionary (WORD VARCHAR(30),
                         WORD_DESC TEXT, WORD_NUM INT, Point INT)";
    ret = sqlite3_exec(db, sql_command, NULL, NULL, NULL);
    if (ret != SQLITE_OK)
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "database table creation failed with error: %d", ret);

    sql_command = "CREATE TABLE IF NOT EXISTS Note (TITLE VARCHAR(30), CONTENTS TEXT)";
    ret = sqlite3_exec(db, sql_command, NULL, NULL, NULL);
    if (ret != SQLITE_OK)
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "database table creation failed with error: %d", ret);

    dlog_print(DLOG_INFO, LOG_TAG, "DB init Success.");

    return ret;
}

void
initialize_datacontrol_provider()
{
    dlog_print(DLOG_INFO, LOG_TAG, "initialize_datacontrol_provider");

    int result = create_database();
    if (result != SQLITE_OK)
        return;

    sql_callback = (data_control_provider_sql_cb *)malloc(sizeof(data_control_provider_sql_cb));
    sql_callback-&gt;select_cb = select_request_cb;
    sql_callback-&gt;insert_cb = insert_request_cb;
    sql_callback-&gt;delete_cb = delete_request_cb;
    sql_callback-&gt;update_cb = update_request_cb;
    result = data_control_provider_sql_register_cb(sql_callback, NULL);
    if (result != DATA_CONTROL_ERROR_NONE)
        dlog_print(DLOG_ERROR,
                   "data_control_sql_response_c failed with error: %d", result);
    else
        dlog_print(DLOG_INFO, LOG_TAG, "Provider SQL register success");
}
</pre>
</li>
</ol></li>
<li id="consumer2">Implement the consumer application:
<ol type="a"><li>The consumer sends requests for the insert, select, update, and delete operations to the provider, and receives the results as a response from the provider.

<p>Implement the response callbacks, which receive the request result and data from the provider:</p>

<pre class="prettyprint">
/* Callback for the insert operation response */
void
sql_insert_response_cb(int request_id, data_control_h provider,
                       long long inserted_row_id, bool provider_result,
                       const char *error, void *user_data)
{
    if (provider_result) {
        dlog_print(DLOG_INFO, LOG_TAG, "The insert operation is successful");
    } else {
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "The insert operation for the request %d failed. error message: %s",
                   request_id, error);
    }
}

/* Callback for the select operation response */
void
sql_select_response_cb(int request_id, data_control_h provider,
                       result_set_cursor cursor, bool provider_result,
                       const char *error, void *user_data)
{
    if (provider_result) {
        dlog_print(DLOG_INFO, LOG_TAG, "The select operation is successful");
    } else {
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "The select operation for the request %d failed. error message: %s",
                   request_id, error);
    }

    while (data_control_sql_step_next(cursor) == DATA_CONTROL_ERROR_NONE) {
        char word[32] = {0,};
        char word_desc[32] = {0,};
        long long word_number = -1;

        data_control_sql_get_text_data(cursor, 0, word);
        data_control_sql_get_text_data(cursor, 1, word_desc);
        data_control_sql_get_int64_data(cursor, 2, &amp;word_number);

        dlog_print(DLOG_INFO, LOG_TAG, "Word: %s, Word DESC: %s, Word NUM: %ld ",
                   word, word_desc, word_number);
    }
}

/* Callback for the update operation response */
void
sql_update_response_cb(int request_id, data_control_h provider, bool provider_result,
                       const char *error, void *user_data)
{
    if (provider_result) {
        dlog_print(DLOG_INFO, LOG_TAG, "The update operation is successful");
    } else {
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "The update operation for the request %d failed. error message: %s",
                   request_id, error);
    }
}

/* Callback for the delete operation response */
void
sql_delete_response_cb(int request_id, data_control_h provider, bool provider_result,
                       const char *error, void *user_data)
{
    if (provider_result) {
        dlog_print(DLOG_INFO, LOG_TAG, "The delete operation is successful");
    } else {
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "The delete operation for the request %d failed. error message: %s",
                   request_id, error);
    }
}
</pre>
<p>Once you get the <code>result_set_cursor</code> object in the select operation response callback, you can use the following functions to get information:</p>
<ul><li><code>data_control_sql_step_first()</code></li>
<li><code>data_control_sql_step_last()</code></li>
<li><code>data_control_sql_step_next()</code></li>
<li><code>data_control_sql_set_previous()</code></li>
<li><code>data_control_sql_get_column_count()</code></li>
<li><code>data_control_sql_get_column_name()</code></li>
<li><code>data_control_sql_get_column_item_size()</code></li>
<li><code>data_control_sql_get_column_item_type()</code></li>
<li><code>data_control_sql_get_blob_data()</code></li>
<li><code>data_control_sql_get_int_data()</code></li>
<li><code>data_control_sql_get_int64_data()</code></li>
<li><code>data_control_sql_get_double_data()</code></li>
<li><code>data_control_sql_get_text_data()</code></li></ul>
</li>
<li>To identify the provider and data, initialize a data control handler within the <code>app_create()</code> function generated by the Tizen Studio:
<pre class="prettyprint">
data_control_sql_response_cb sql_callback;
void
initialize_datacontrol_consumer(appdata_s *ad)
{
    int ret;

    const char *provider_id = Your Provider ID;
    const char *data_id = "Dictionary";

    /* Create data control handler */
    ret = data_control_sql_create(&amp;(ad-&gt;provider_h));
    if (ret != DATA_CONTROL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "creating data control provider failed with error: %d", ret);

    ret = data_control_sql_set_provider_id(ad-&gt;provider_h, provider_id);
    if (ret != DATA_CONTROL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "setting provider id failed with error: %d", ret);

    ret = data_control_sql_set_data_id(ad-&gt;provider_h, data_id);
    if (ret != DATA_CONTROL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "setting data id failed with error: %d", ret);

    /* Set response callbacks */
    sql_callback.delete_cb = sql_delete_response_cb;
    sql_callback.insert_cb = sql_insert_response_cb;
    sql_callback.select_cb = sql_select_response_cb;
    sql_callback.update_cb = sql_update_response_cb;

    /* Register response callbacks */
    ret = data_control_sql_register_response_cb(ad-&gt;provider_h, &amp;sql_callback, NULL);
    if (ret != DATA_CONTROL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "Registering the callback function failed with error: %d", ret);

    dlog_print(DLOG_INFO, LOG_TAG, "Init data control success");

    int req_id = 0;

    /* Send a request to insert a row */
    bundle *b = bundle_create();
    bundle_add_str(b, "WORD", "'test'");
    bundle_add_str(b, "WORD_DESC", "'test desc'");

    data_control_sql_insert(ad-&gt;provider_h, b, &amp;req_id);

    /* Send a request to select a row */
    char *column_list[2];
    column_list[0] = "WORD";
    column_list[1] = "WORD_DESC";

    const char *where = "WORD = 'test'";
    const char *order = "WORD ASC";

    data_control_sql_select(ad-&gt;provider_h, column_list, 2, where, order, &amp;req_id);

    /* Send a request to add a row */
    bundle_add_str(b, "WORD", "'test_new'");
    data_control_sql_update(ad-&gt;provider_h, b, where, &amp;req_id);

    /* Send a request to delete a row */
    const char *where_delete = "WORD = 'test'";
    result = data_control_sql_delete(ad-&gt;provider_h, where_delete, &amp;req_id);

    /* Free memory */
    bundle_free(b);
}

static bool
app_create(void *data)
{
    /*
       Take necessary actions before main event loop starts
       Initialize UI resources and application data
       If this function returns true, the main loop of application starts
       If this function returns false, the application is terminated
    */
    appdata_s *ad = data;

    create_base_gui(ad);
    initialize_datacontrol_consumer(ad);

    return true;
}
</pre>
</li>
<li>
<p>To send requests to a specific table, use the <code>data_control_sql_set_data_id()</code> function:</p>
<pre class="prettyprint">
{
    bundle *b;
    int ret;

    /* Insert data to the Note table */
    ret = data_control_sql_set_data_id(ad-&gt;provider_h, "Note");
    if (ret != DATA_CONTROL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "setting data id failed with error: %d", ret);

    b = bundle_create();
    bundle_add_str(b, "TITLE", "'test'");
    bundle_add_str(b, "CONTENTS", "'test contents'");
    data_control_sql_insert(ad-&gt;provider_h, b, &amp;req_id);
    bundle_free(b);

    /* Insert data to the Dictionary table */
    ret = data_control_sql_set_data_id(ad-&gt;provider_h, "Dictionary");
    if (ret != DATA_CONTROL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "setting data id failed with error: %d", ret);

    b = bundle_create();
    bundle_add_str(b, "WORD", "'test'");
    bundle_add_str(b, "WORD_DESC", "'test desc'");
    data_control_sql_insert(ad-&gt;provider_h, b, &amp;req_id);
    bundle_free(b);
}
</pre>
</li>
</ol>
</li></ol>

<h2 id="map3" name="map3">Monitoring Data Changes</h2>
<p>If the consumer wants to receive data change notifications from the provider, it can request notifications with a data change callback:</p>
<ul>
<li>The consumer can add a data change callback using the <code>data_control_add_data_change_cb()</code> function. When no longer needed, the callback can be removed using the <code>data_control_remove_data_change_cb()</code> function.</li>
<li>To accept the callback addition and notification request from the consumer, the provider uses the <code>data_control_provider_add_data_change_consumer_filter_cb()</code> function to add a notification filter. When no longer needed, the filter can be removed using the <code>data_control_provider_remove_data_change_consumer_filter_cb()</code> function.</li>
<li>In the provider, you can use the <code>data_control_provider_foreach_data_change_consumer()</code> function to list all the consumers whose request for the data change notifications has been successful, and who can receive data change notifications from the provider.</li>
</ul>

<p>To monitor data changes, and send and receive notifications:</p>

<ol>
<li id="provider3">Implement monitoring in the provider application.
<p>When the provider's data changes, the provider can send information about the changed data to the consumers who have registered a data change notification callback.</p>
<p>When a consumer attempts to register a data change notification callback, the provider can decide whether to allow it.</p>

<pre class="prettyprint">
bool
change_noti_consumer_list_cb(data_control_h provider, char *consumer_appid,
                             void *user_data)
{
    dlog_print(DLOG_INFO, LOG_TAG,
               "Added change noti consumer appid: %s", consumer_appid);

    return true;
}

bool
consumer_filter_cb_1(data_control_h provider, char *consumer_appid, void *user_data)
{
    dlog_print(DLOG_INFO, LOG_TAG,
               "consumer appid %s try to add data change callback", consumer_appid);
    if (strcmp(consumer_appid, "org.tizen.helloworld_consumer2") == 0) {
        dlog_print(DLOG_INFO, LOG_TAG, "Invalid appid: %s", consumer_appid);

        return false;
    }
    data_control_provider_foreach_data_change_consumer(provider,
                                                       &amp;change_noti_consumer_list_cb,
                                                       NULL);

    return true;
}

bool
consumer_filter_cb_2(data_control_h provider, char *consumer_appid, void *user_data)
{
    dlog_print(DLOG_INFO, LOG_TAG,
               "consumer appid %s try to add data change callback", consumer_appid);
    if (strcmp(consumer_appid, "org.tizen.helloworld_consumer3") == 0) {
        dlog_print(DLOG_INFO, LOG_TAG, "Invalid appid: %s", consumer_appid);

        return false;
    }

    return true;
}

/* Add the filter for the accepted callback registration */
int filter_callback_id_1;
int filter_callback_id_2;
void
add_consumer_filter_cb_func(void *data, Evas_Object *obj EINA_UNUSED,
                            void *event_info EINA_UNUSED)
{
    data_control_provider_add_data_change_consumer_filter_cb(consumer_filter_cb_1,
                                                             NULL,
                                                             &amp;filter_callback_id_1);
    dlog_print(DLOG_INFO, LOG_TAG,
               "filter_callback_id_1 id: %d", filter_callback_id_1);

    data_control_provider_add_data_change_consumer_filter_cb(consumer_filter_cb_2,
                                                             NULL,
                                                             &amp;filter_callback_id_2);
    dlog_print(DLOG_INFO, LOG_TAG,
               "filter_callback_id_2 id: %d", filter_callback_id_2);
}

/* Remove the filter */
void
remove_consumer_filter_cb_func(void *data, Evas_Object *obj EINA_UNUSED,
                               void *event_info EINA_UNUSED)
{
    data_control_provider_remove_data_change_consumer_filter_cb(filter_callback_id_1);
    dlog_print(DLOG_INFO, LOG_TAG, "remove callback %d", filter_callback_id_1);

    data_control_provider_remove_data_change_consumer_filter_cb(filter_callback_id_2);
    dlog_print(DLOG_INFO, LOG_TAG, "remove callback %d", filter_callback_id_2);
}

/* Send a data change notification */
void
update_request_cb(int request_id, data_control_h provider, bundle *update_data,
                  const char *where, void *user_data)
{
    char* command = data_control_provider_create_update_statement(provider,
                                                                  update_data, where);
    int ret = sqlite3_exec(db, command, NULL, NULL, NULL);
    if (ret != SQLITE_OK) {
        data_control_provider_send_error(request_id, sqlite3_errmsg(db));
        free(command);

        return;
    }

    ret = data_control_provider_send_update_result(request_id);
    if (ret != DATA_CONTROL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "update_send_result failed with error: %d", ret);
    dlog_print(DLOG_INFO, LOG_TAG, "[update_request_cb] send result success");

    data_control_provider_send_data_change_noti(provider,
                                                DATA_CONTROL_DATA_CHANGE_SQL_UPDATE,
                                                update_data);
    dlog_print(DLOG_INFO, LOG_TAG,
               "[send data change notification] Notify data change");

    free(command);
}
</pre>
</li>

<li id="consumer3">Implement the consumer application.
<p>The consumer requests the provider to add or remove the data change callback, and receives the request result from the provider. If the provider allows the data change notifications, the consumer receives them when the data changes.</p>

<pre class="prettyprint">
/* Triggered when the data change notification arrives */
void
data_change_cb(data_control_h provider, data_control_data_change_type_e type,
               bundle *data, void *user_data)
{
    char *word;
    char *word_desc;
    char *word_num;

    bundle_get_str(data, "WORD", &amp;word);
    bundle_get_str(data, "WORD_DESC", &amp;word_desc);
    bundle_get_str(data, "WORD_NUM", &amp;word_num);
    dlog_print(DLOG_INFO, LOG_TAG, "%d type noti, changed data: %s, %s, %s",
               type, word, word_desc, word_num);
}

/* Triggered when the provider has accepted the callback registration */
void
result_cb(data_control_h provider, data_control_error_e result, int callback_id,
          void *user_data)
{
    dlog_print(DLOG_INFO, LOG_TAG, "Add data change callback RESULT: %d", result);
}

/* Register the callback */
int cb_id;
void
add_data_change_cb_func(void *data, Evas_Object *obj, void *event_info)
{
    appdata_s *ad = (appdata_s *)data;
    int ret = data_control_add_data_change_cb(ad-&gt;provider_h, data_change_cb, NULL,
                                              result_cb, NULL, &amp;cb_id);
    if (ret != DATA_CONTROL_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG,
                   "add data change callback failed with error: %d", ret);
    dlog_print(DLOG_INFO, LOG_TAG, "add data change callback done: %d", cb_id);
}

/* Remove the callback */
void
remove_data_change_cb_func(void *data, Evas_Object *obj, void *event_info)
{
    appdata_s *ad = (appdata_s *)data;
    data_control_remove_data_change_cb(ad-&gt;provider_h, cb_id);
    dlog_print(DLOG_INFO, LOG_TAG, "remove data change callback done: %d", cb_id);
}
</pre>
</li>
</ol>

<h2 id="export" name="export">Data Control Export</h2>

<p>You can export the provider functionalities of your Tizen native service application in the <a href="../../../../org.tizen.training/html/native/process/setting_properties_n.htm#manifest">application project settings</a> in the Tizen Studio. The provider ID, type, and accessibility must be specified for the available data control.</p>
  <p align="center"><strong>Figure: Exporting data control</strong></p>
  <p align="center"><img alt="Exporting data control" src="../../images/exporting_datacontrol.png"/></p>
  <p id="data">The data model must be opened to the public to help other applications to use the exported data controls. The data model consists of the following data:</p>
  <ul>
<li>Provider ID
    <ul>
	 <li>It is used for identifying the data control provider.</li>
     <li>It must be unique and use a fully-qualified domain name.</li>
	 <li>It must consist of alpha-numeric letters separated with the period (".") character, and it must start with a letter.</li>
     <li>Platform-defined data control provider is defined in the <code>http://tizen.org/datacontrol/provider/&lt;application name&gt;</code> format.</li>
     <li>User-defined data control provider is defined in the <code>http://&lt;vendor.com&gt;/datacontrol/provider/&lt;application name&gt;</code> format.</li>
    </ul>
</li>
   <li>Data ID
    <ul>
	 <li>It is used for identifying data (usually a database table name or a registry section name) exported by the data control provider.</li>
     <li>It must be unique in the data control provider and it is given as a string of 1 or more components, separated by a slash ("/") character.</li>
    </ul>
</li>
   <li>Type
    <ul>
	 <li>You can use Tizen native applications that provide their own data structure table and implement the SQL-type data control provider using the database file.</li>
     <li>You can use Tizen native applications that provide their own key-value pairs data structure map and implement the map-type data control provider using registry file or collection map classes.</li>
    </ul>
</li>
   <li>Data schema
    <ul>
	 <li>SQL-type data control exports column names and types of the data structure table.</li>
     <li>Map-type data control exports key names and types of the data structure map.</li>
    </ul>
</li>
	<li>Data accessibility
		<ul>
			<li>Tizen native applications can control read and write access from other applications by defining data control accessibility.</li>
		</ul>
	</li>
	<li>Trusted
		<ul>
			<li>You can allow access from other applications signed with the same certificate by setting the trusted status for the data control.</li>
		</ul>
	</li>
	<li>Privileges
		<ul>
			<li>Your provider application can restrict access to applications that have specific privileges defined.</li>
		</ul>
	</li>
</ul>

<p>The following table contains an example data model of a data control provider.</p>
  <p align="center" class="Table"><strong>Table: Data model example of a data control provider</strong></p>
<table border="1" style="width: 100%">
   <tbody>
<tr>
<th style="text-align:center;margin-left:auto;margin-right:auto;">Data control type</th>
     <th style="text-align:center;margin-left:auto;margin-right:auto;">Data control provider ID</th>
     <th style="text-align:center;margin-left:auto;margin-right:auto;">Data control data ID</th>
     <th colspan="2" style="text-align:center;margin-left:auto;margin-right:auto;">Data schema</th>
     <th style="text-align:center;margin-left:auto;margin-right:auto;">Data accessibility</th>
     <th style="text-align:center;margin-left:auto;margin-right:auto;">Trusted</th>
     <th style="text-align:center;margin-left:auto;margin-right:auto;">Privileges</th>
    </tr>
<tr>
<td>SQL</td>
     <td><code>http://&lt;vendor.com&gt;/datacontrol/provider/sample</code></td>
     <td><code>data1</code></td>
     <td><code>column1</code>
	<p>(Type: Integer)</p> </td>
     <td><code>column2</code>
	 <p>(Type: String)</p> </td>
     <td>Read-Only</td>
	<td>True</td>
	<td><code>http://tizen.org/privilege/application.admin</code></td>
    </tr>
<tr>
<td>Map</td>
     <td><code>http://&lt;vendor.com&gt;/datacontrol/provider/sample2</code></td>
     <td><code>data2</code></td>
     <td><code>key1</code>
	 <p>(Type: String)</p> </td>
     <td><code>key2</code>
	 <p>(Type: String)</p> </td>
     <td>Read-Write</td>
	<td>False</td>
	<td><code>http://tizen.org/privilege/appmanager.launch</code></td>
    </tr>
</tbody>
</table>



<script type="text/javascript" src="../../scripts/jquery.zclip.min.js"></script>
<script type="text/javascript" src="../../scripts/showhide.js"></script>

</div></div></div>

<a class="top sms" href="#"><img src="../../images/btn_top.gif" alt="Go to top" /></a>

<div id="footer">
<p class="footer">Except as noted, this content - excluding the Code Examples - is licensed under <a href="http://creativecommons.org/licenses/by/3.0/legalcode" target="_blank">Creative Commons Attribution 3.0</a> and all of the Code Examples contained herein are licensed under <a href="https://www.tizen.org/bsd-3-clause-license" target="_blank">BSD-3-Clause</a>.<br/>For details, see the <a href="https://www.tizen.org/content-license" target="_blank">Content License</a>.</p>
</div>

<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-25976949-1']);
_gaq.push(['_trackPageview']);
(function() {
var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();
</script>

</body>
</html>
