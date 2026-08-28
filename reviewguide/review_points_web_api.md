# Review points in Web API

This page describes the review points that were often asked to be updated.
Unlike .NET or Native, Web contains the API file also in tizen-docs repository. If the files under /appliation/web/api are updated, refer this page.

Web API files are in HTML format. So don't be confused. These files must follow HTML format (as like \<strong> or \<li>), not markdown format (as like \*\* or \-).

As most updates are in `device_api` folder these days, this description is for the case of updates in `device_api` folder. If Web api in `ui_fw_api` or `w3c_api` is updated, check the folder structure and relation with other pages also to not to miss related pages update.


## Add new page

When a new page is created, check the `toc.xml`, `index.html`, and `index.xml` of the created page.

```
- /application/web/api/<VERSION>/device_api/<PROFILE>/inde.html
- /application/web/api/<VERSION>/device_api/<PROFILE>/index.xml
- /docs/application/web/api/toc.xml
```

**Example :**

- /application/web/api/*10.0*/device_api/*tv*/index.html
- /application/web/api/*10.0*/device_api/*tv*/index.xml
- /docs/application/web/api/toc.xml

### index

There are two kinds of index file, `index.html` and `index.xml`.
`index.html` is used as a cover page for each profile in Web API. This page is displayed on docs.tizen.org.

index.xml lists up the page structure.

**Example :**

If a new page is added under the `Base` section of the `tv` profile, both `index.html` and `index.xml` for the TV profile must be updated to include the page.

### toc.xml

toc.xml file is to manage the LNB of API pages. According to the structure listed in toc.xml, the LNB in API pages is created. In previous days it listed up all Native & Web API structure, but now only listing up Web API is enough. 

index.xml is used in toc.xml. 

Use the information in `index.xml` to populate the corresponding TV Web API section in `toc.xml` and generate its LNB structure.
