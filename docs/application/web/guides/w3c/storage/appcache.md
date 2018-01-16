# HTML5 Application caches

HTML5 application caches can be used to store and utilize resources needed in Web applications, such as HTML, CSS, and JavaScript files, and images. You can cache certain files in the browser to use them in an offline state, or define them to be always updated from the server.

This feature is supported in mobile and TV applications only.

HTML5 application caches provide you with the following benefits:

- Offline support

  If a cache file is downloaded after connecting to a site, the application can be used in an offline state.

- Speed

  The cached files are saved in local storage, making cached resources load faster.

- Reduced server load

  The browser only downloads content from the server when the cached files need to be updated, reducing server load.

The main application cache features include:

- Cache activation

  You can use the cache manifest file to [activate the application cache](#setting-the-cache-manifest) and display cache information in the browser as simple text.

- Cache updating

  To update a cached item in the client, you need to [change the manifest file](#updating-the-cache).

- Cache management

  Application cache can control JavaScript based on [events](http://www.w3.org/TR/2014/REC-html5-20141028/browsers.html#appcacheevents). It can [check or update the current cache status](#managing-the-cache-events).

## Setting the Cache Manifest

To enable application caches, include the `manifest` attribute in the `<html>` tag on every page of your Web application that you want cached. The recommended file extension for the manifest file is `.appcache`. The file must be served using the `text/cache-manifest` MIME type.

The following example demonstrates cache enabling. For a complete source code, see [appcache_update.html](http://download.tizen.org/misc/examples/w3c_html5/storage/html5_application_caches).

```
<!DOCTYPE html>
<html manifest="tizen.appcache">
   <!--Page content-->
</html>
```

To set the cache manifest file content:

1. Begin the [manifest file](http://www.w3.org/TR/2014/REC-html5-20141028/browsers.html#writing-cache-manifests) with CACHE MANIFEST content:

   ```
   CACHE MANIFEST
   # 2013-03-18 v2.0.0
   images/sound-icon.png
   images/background.png
   /tizen_application_cache.html
   /main.js
   ```

 > **Note**  
 > The `# 2013-03-18 v2.0.0` line is used for searching. When the content in an image or file list is changed, it does not automatically update the cache. It is updated if the manifest file is changed. Even if the content in the description is changed, cache update is possible.

2. Define the files to be cached in the `CACHE` section:

   ```
   CACHE:
   style/default.css
   ```

   This is the default section for entries. Files listed under this header are explicitly cached after they are downloaded for the first time.

 > **Note**  
 > The `CACHE` section can be omitted, if automatic cache save is used.

3. Define the online white list in the `NETWORK` section:

   ```
   NETWORK:
   comm.cgi
   login.asp
   ```

   All requests to these resources bypass the cache, even if the user if offline.  Wild cards like '*' can be used.

4. Define the fallback pages in the `FALLBACK` section:

   ```
   FALLBACK:
   / tizen  /tizen_offline.html
   ```

   This section is optional and used to specify fallback pages in case a resource is inaccessible. In the example above, if the file in the `/tizen` folder cannot be loaded in an offline state, it is replaced with the `tizen_offline.html` file.

> **Note**  
> The cached version of the file is displayed to the user even when an updated file is uploaded to the server. If the file is updated, the manifest file must be changed accordingly. The cache size in a mobile or desktop Web browser is normally set as 5 MB per domain.

## Updating the Cache

The browser checks only the edited items in the manifest, and checks whether a cache update is needed. If the relevant page is updated from the server, the manifest is applied as the basis even after edited items have been applied. If the update content is an addition or deletion of the defined file within the manifest, the manifest file can be edited.

However, if the content in the defined file is changed, the cache is not updated. In that case, if the description or version is changed in the manifest, the browser can update the cache.

To update the cache:

1. Include the `manifest` property in  the `<html>` tag to enable loading the manifest file and caching content by the browser:

   ```
   <!DOCTYPE html>
   <html manifest="clock.appcache">
   ```

2. If the content of the `cache_test.js` file is changed and updating the cache is necessary, edit the manifest file accordingly:

   ```
   CACHE MANIFEST
   #VERSION 1.0.0
   CACHE:
   cache_test.js
   ```

3. Reconnect and check whether there are edited items in the manifest file using the `update()` method:

   ```
   <script>
       var update = function() {
           var appCache = window.applicationCache;
           appCache.addEventListener('updateready', handleCacheEvent, false);
           appCache.update();
   ```

4. If there are changes in the manifest file, use the `swapCache()` and `handleCacheEvent()` methods to update the cache:

   ```
           function handleCacheEvent(e) {
               if (appCache.status == appCache.UPDATEREADY) {
                   try {
                       window.applicationCache.swapCache();
                       document.getElementById('log').innerHTML = 'Update is successful';
                   }
               }
           }
       };
   </script>
   ```

> **Note**  
> The files used in this example are Web server source files. A change in the client cache occurs when the server file changes.

### Source Code

For the complete source code related to this use case, see the following file:

- [appcache_update.html](http://download.tizen.org/misc/examples/w3c_html5/storage/html5_application_caches)

## Managing the Cache Events

To check the current status of the cache:

1. Check the `window.applicationCache.status` value:

   ```
   <script>
       var appCache = window.applicationCache;

       switch (appCache.status) {
           case 0: /* ApplicationCache.status is UNCACHED */
               break;
           case 1: /* ApplicationCache.status is IDLE */
               break;
           case 2: /* ApplicationCache.status is CHECKING */
               break;
           case 3: /* ApplicationCache.status is DOWNLOADING */
               break;
           case 4: /* ApplicationCache.status is UPDATEREADY */
               break;
           case 5: /* ApplicationCache.status is OBSOLETE */
               break;
           default: break;
       }
   </script>
   ```

2. Different events can occur based on the cache status. Use the `addEventListener()` method to add listeners in order to detect events:

   ```
   <script>
       var appCache = window.applicationCache;
       appCache.addEventListener('cached', function() {
           /* Cached resource is downloaded */
       }, false);

       appCache.addEventListener('checking', function() {
           /*
              Manifest file is downloaded for the first time
              or if there is an update in the manifest
           */
       }, false);

       appCache.addEventListener('downloading', function() {
           /* Content is being updated */
       }, false);

       appCache.addEventListener('error', function() {
           /* Error occurred */
       }, false);

       appCache.addEventListener('noupdate', function() {
           /* No update is available */
       }, false);

       appCache.addEventListener('obsolete', function() {
           /* Manifest file cannot be found */
       }, false);

       appCache.addEventListener('progress', function() {
           /* Cache file is being downloaded */
       }, false);

       appCache.addEventListener('updateready', function() {
           /* All resources for update are downloaded */
       }, false);
   </script>
   ```

## Related Information
* Dependencies   
   - Tizen 2.4 and Higher for Mobile
   - Tizen 3.0 and Higher for TV
