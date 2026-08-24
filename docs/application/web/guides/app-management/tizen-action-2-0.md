# Tizen Action 2.0

Tizen Action 2.0 allows your Web application to expose its capabilities and current screen context to an Agent as structured, discoverable tools. The platform defines Actions, Entities, and View Entities; your application implements the applicable capabilities on top of a generated JavaScript runtime.

The main Tizen Action 2.0 features for Web applications are:

- Exposing screen context with View Annotation

  You can implement the platform `Tizen.Action.View` Actions with four synchronous JavaScript callbacks, so that an Agent can read the current screen as `Tizen.Entity.View` Entities and chain follow-up Actions.

- Filling annotations with typed Entity data

  You can serialize an application Entity into the annotation's `EntityInfo` field, so that the Agent can consume the screen data directly without an extra resolver round trip.

## Core concepts

| Component | Role |
|---|---|
| Action | A capability an Agent can discover and run. An `.action` file is a JSON schema; a 2.0 TIDL Action has `"type": "tidl"`. |
| Entity | A typed data model passed between Actions. An `.entity` file defines its type name, inheritance, and data schema. |
| View Entity | An Entity describing current UI view information, based on `Tizen.Entity.View`. |
| `actionc` | Generates the JavaScript runtime and service stub from Actions and Entities. |
| Agent | Discovers Actions and Entities and executes an Action through the Action API or the `action-tool` CLI. |

An Agent queries the current screen through the `Tizen.Action.View` category:

| Action | Input | Result key | Purpose |
|---|---|---|---|
| `Common_Tizen.Action.View_GetAnnotatedViews` | none | `views` | Enumerates currently visible annotated Views |
| `Common_Tizen.Action.View_FindById` | `{"id":"<View.Id>"}` | `view` | Finds one View by View ID |
| `Common_Tizen.Action.View_GetFocusedView` | none | `view` | Gets the currently focused View |
| `Common_Tizen.Action.View_ToPresentation` | `Tizen.Entity.View` | `result` | Converts a View into a presentation |

The `Tizen.Entity.View` fields are `Id`, `Type`, `Description`, `ScreenBounds`, `WindowBounds`, `IsFocused`, `IsEnabled`, and `Annotation` (`EntityId`, `EntityType`, and `EntityInfo`). `ScreenBounds` is in absolute screen pixels and `WindowBounds` is relative to the owning window. Visibility is not a View field; it is an enumeration criterion, so views that are not sufficiently visible are excluded from the `GetAnnotatedViews` result.

> [!NOTE]
> Your application does not register the platform View Actions or View Entity schema files again. The schemas are owned by the platform default-actions package; if an application declares an Action or Entity name already owned by the platform, the package installation is rejected.

## Configure the application

Register each of the four View Actions individually as provider metadata in `config.xml`. Registering only the category is silently ignored:

```xml
<tizen:metadata key="http://tizen.org/metadata/action/provider"
                value="Common_Tizen.Action.View_FindById"/>
<tizen:metadata key="http://tizen.org/metadata/action/provider"
                value="Common_Tizen.Action.View_GetAnnotatedViews"/>
<tizen:metadata key="http://tizen.org/metadata/action/provider"
                value="Common_Tizen.Action.View_GetFocusedView"/>
<tizen:metadata key="http://tizen.org/metadata/action/provider"
                value="Common_Tizen.Action.View_ToPresentation"/>
<tizen:privilege name="http://tizen.org/privilege/datasharing"/>
```

## Generate and load the runtime

Generate the JavaScript runtime with `actionc`, specifying the toolchain schema data directory:

```bash
ACTIONC_DATA_DIR=<TOOLCHAIN>/data actionc -a Tizen.Action.View -l JS -o ImplView
```

The generated stub's port and class name are `TizenActionView` and `TizenActionViewServiceBase`. Load the generated runtime, the RPC adapter, and your application code in order:

```html
<script src="js/gen/ImplView.js"></script>
<script src="js/view-rpc.js"></script>
<script src="js/main.js"></script>
```

When `ImplView.js` runs, `tizen.rpcport` must be available. If the page must also open in a standard browser, check for the Tizen runtime before loading the scripts. It is safer to load the next script in the `onload` handler of each script rather than relying on timing assumptions.

## Implement the View callbacks

Connect four synchronous callbacks on top of the generated runtime. The following example builds the object format that the `view-rpc.js` adapter receives as input; `Focused` and `Enabled` are adapter input fields, which the adapter converts to `IsFocused` and `IsEnabled`:

```js
function viewFor(element) {
  var rect = element.getBoundingClientRect();
  var annotation = JSON.parse(element.dataset.annotation || '{}');

  return {
    Id: element.dataset.tizenViewId || element.id,
    Type: element.dataset.tizenViewType || element.tagName,
    Description: element.getAttribute('aria-label') ||
                 element.textContent.trim().slice(0, 240),
    ScreenBounds: {
      X: Math.round(rect.left + window.screenLeft),
      Y: Math.round(rect.top + window.screenTop),
      Width: Math.round(rect.width),
      Height: Math.round(rect.height)
    },
    WindowBounds: {
      X: Math.round(rect.left),
      Y: Math.round(rect.top),
      Width: Math.round(rect.width),
      Height: Math.round(rect.height)
    },
    Focused: element === document.activeElement,
    Enabled: !element.disabled,
    Annotation: {
      entityId: annotation.entityId || '',
      entityType: annotation.entityType || '',
      entityInfo: annotation.entityInfo || ''
    }
  };
}
```

Because visibility is not a View field, the `getAnnotatedViews` callback implements visibility by excluding invisible elements from the result:

```js
function isVisible(element) {
  var rect = element.getBoundingClientRect();
  return rect.width > 0 && rect.height > 0 &&
         rect.bottom > 0 && rect.right > 0 &&
         rect.top < window.innerHeight && rect.left < window.innerWidth;
}

function getAnnotatedViews() {
  return Array.from(document.querySelectorAll('[data-tizen-view-id]'))
    .filter(isVisible)
    .map(viewFor)
    .filter(function (view) {
      return view.Annotation.entityId && view.Annotation.entityType;
    });
}

TizenViewRpc.start({
  findById: findById,
  getAnnotatedViews: getAnnotatedViews,
  getFocusedView: getFocusedView,
  toPresentation: toPresentation
});
```

Follow these rules:

- All four callbacks must be synchronous functions.
- Call `start()` only once, after the runtime and adapter are loaded.
- Annotations must provide both an entity ID and an entity type; `entityInfo` is optional.
- If you write the final Entity field names such as `IsFocused` directly in the callback object, the RPC adapter must read the same field names. Mixing different names can cause the state to serialize as `false`.

## Fill EntityInfo with a typed Entity

If the application has its own Entity schema, `entityInfo` can be filled with the `toJson()` output of the entity class generated by `actionc`. The Agent then reads the screen data directly, without a resolver Action round trip:

```js
function contentEntityInfo(id, name, mediaType, extra) {
  var runtime = window.TizenDisneyPlusRuntime;
  if (!runtime) return "";
  var content = new runtime.TizenEntityDisneyPlusContent();
  content.Id = id;
  content.Name = name;
  content.MediaType = mediaType;
  content.Extra = JSON.stringify(extra);
  return content.toJson();
}

element.dataset.annotation = JSON.stringify({
  entityId: title.id,
  entityType: title.type,
  entityInfo: contentEntityInfo(title.id, title.title, title.type,
                                { kind: "recommendation" })
});
```

An annotation with an empty `entityInfo` string is still valid. Hand-built JSON also works, but using the generated entity class keeps field names consistent with the schema.

## Build and verify

Build, package, and install the application:

```bash
tizen build-web -- .
tizen package -t wgt -s <SECURITY_PROFILE> -- .buildResult
sdb install .buildResult/<PACKAGE>.wgt
```

If the package file is modified, re-sign and reinstall it.

Verify the provider on the device:

```bash
sdb shell action-tool find-appids Tizen.Action.View --json
sdb shell app_launcher -s <APP_ID>
sdb shell action-tool execute \
  '{"id":201,"params":{"name":"Common_Tizen.Action.View_GetAnnotatedViews","appid":"<APP_ID>","arguments":{}}}'
```

Check `return.Success` first and select actual `View.Id` values from the successful `views` result; do not assume the View ID is the entity ID from the annotation. Use a returned ID with `View_FindById`, `View_GetFocusedView`, and `View_ToPresentation`. Note that `View_FindById` uses lowercase `id` in its arguments, while the input View for `View_ToPresentation` uses uppercase `Id`.

Common problems to check:

| Symptom | What to check |
|---|---|
| `find-appids` returns `[]` | Category spelling, individual Action metadata entries, platform default-actions installation, and package metadata processing |
| `isError: true` with empty content | The request did not reach the provider; check the `appid` and whether the RPC listener started |
| `return.Success: false` | The request reached the provider but the application logic failed; check `return.Reason` |
| `tizen.rpcport` is not available | Verify that the device's webapi plugin has the rpcport extension |
| State fields are all `false` | Verify that the callback object and RPC adapter use the same field names (`Focused`/`Enabled` versus `IsFocused`/`IsEnabled`) |
| WGT installation fails | Re-package the WGT with the correct security profile and verify the signature |

## Related information
* Dependencies
  - Tizen 10.1 and Higher
