# Tizen Action 2.0

Tizen Action 2.0 allows your application to expose its capabilities to an Agent as structured, discoverable tools. The platform defines Actions, Entities, and View Entities; your application implements and registers the capabilities it provides through a TIDL-based service.

The main Tizen Action 2.0 features are:

- Providing platform-defined Actions

  You can implement Actions and Entities defined by the platform specification by generating a service stub with the `actionc` tool and implementing the generated methods.

- Defining application-owned Actions

  You can author your own `.action` and `.entity` schema files, generate the service code, and register the definitions and your application as a provider through manifest metadata.

- Exposing screen context with View Annotation

  You can attach an annotation to a DALi UI element so that an Agent can read the current screen as `Tizen.Entity.View` Entities and chain follow-up Actions.

## Core concepts

| Component | Role |
|---|---|
| Action | A capability an Agent can discover and run. An `.action` file is a JSON schema; a 2.0 TIDL Action has `"type": "tidl"`. |
| Entity | A typed data model passed between Actions. An `.entity` file defines its type name, inheritance, and data schema. |
| View Entity | An Entity describing current UI view information, based on `Tizen.Entity.View`. |
| `actionc` | Generates TIDL and a service stub from Actions and Entities. |
| Agent | Discovers Actions and Entities and executes an Action through the Action API or the `action-tool` CLI. |

Within one Agent request, the result Entity of one Action can become the input Entity of the following Action. Because Action names and input and output types are specified, this composition is structural and does not require an LLM to reinterpret the intermediate data.

## Action and Entity schemas

A TIDL Action schema declares its name, category, contracts, and provider:

```json
{
  "version": "v2",
  "name": "App_Example.Action.Bookmark_Save",
  "type": "tidl",
  "category": "Example.Action.Bookmark",
  "description": "Save or update a bookmark so it can be used by later actions",
  "allowedBackground": true,
  "autoDispose": false,
  "inputSchema": { "type": "Example.Entity.Bookmark" },
  "outputSchema": { "type": "Tizen.Entity.Status" },
  "details": { "appid": "org.example.tidlcustomactionsample" }
}
```

| Field | Description |
|---|---|
| `version` | The 2.0 schema version. Platform examples use `v2`. |
| `name` | The unique Action name. Action names are device-wide identifiers. |
| `type` | Use `tidl` for a TIDL Action. |
| `category` | One category generates one TIDL interface. |
| `inputSchema`, `outputSchema` | JSON-Schema-shaped contracts. Reference an Entity directly in `type`, or from an object property. In `outputSchema`, the property named `return` becomes the generated method return value; other properties become out parameters. |
| `details.appid` | The provider application ID. It must match the provider's manifest `appid`. |
| `allowedBackground`, `autoDispose` | Optional background and lifecycle flags passed to the RPC-port connection. Both default to `false`. |

An Entity keeps data meaning by using a `Tizen.Entity.*`-style type instead of only JSON primitives, and can inherit from the platform root Entity:

```json
{
  "typeName": "Example.Entity.Bookmark",
  "description": "A bookmark exposed by the example application",
  "base": "Tizen.Entity",
  "dataSchema": {
    "type": "object",
    "properties": {
      "Url": { "type": "string", "description": "Bookmark URL" },
      "Title": { "type": "string", "description": "Human-readable bookmark title" }
    }
  }
}
```

Every Entity reference needs a corresponding `.entity` file. Property names directly affect the generated getter and setter names, so treat published names as part of the contract.

## Generate a service stub with actionc

To implement a platform-defined Action category, generate from the schemas supplied by the platform:

```bash
actionc -a Tizen.Action.Browser -l C++ -o ImplBrowser
```

For application-owned Action files, repeat `-i` for every Action in the category and add Entity paths with `-e`:

```bash
actionc \
  -i actions/App_Example.Action.Bookmark_Get.action \
  -i actions/App_Example.Action.Bookmark_List.action \
  -i actions/App_Example.Action.Bookmark_Save.action \
  -e entities \
  -l C++ \
  -o gen/ImplBookmark
```

`actionc` converts `.action` and `.entity` files into `.tidl` and runs `tidlc -s`. Use `--keep-temp` to retain the intermediate `.tidl` files. The `-a` and `-i` options are mutually exclusive.

> [!NOTE]
> TIDL method order is an RPC ABI contract. For an application-owned category, `actionc -i` preserves the command-line input order, so pass every `-i` in lexicographical order by full Action name. Adding a new Action whose name sorts before an existing method renumbers the wire IDs; treat such an extension as ABI-incompatible and use a new category or version instead.

## Implement the generated ServiceBase

Inherit the generated category interface and implement every pure virtual method. Do not hand-edit the `.tidl` files or the generated stubs; regenerate after a schema change:

```cpp
class BookmarkService
    : public bookmark::stub::ExampleActionBookmark::ServiceBase {
 public:
  BookmarkService(std::string sender, std::string instance)
      : ServiceBase(std::move(sender), std::move(instance)) {}

  bookmark::TizenEntityStatus Save(
      bookmark::ExampleEntityBookmark value) override {
    if (!g_store.Save(FromEntity(value)))
      return bookmark::TizenEntityStatus(false, "bookmark Id must not be empty");
    return bookmark::TizenEntityStatus(true, "");
  }
};
```

`Factory::CreateService()` creates a `ServiceBase` object for each connected client. In the service application's create callback, construct the generated stub and start listening:

```cpp
g_stub = std::make_unique<bookmark::stub::ExampleActionBookmark>();
g_stub->Listen(std::make_shared<BookmarkFactory>());
```

Shared state can be accessed concurrently, so protect it. Do not block generated methods indefinitely, and return failures through the declared status contract.

## Register the provider in the manifest

An application-defined TIDL Action requires Action-definition and provider metadata. Add Entity metadata only when the package also owns and installs a new Entity:

```xml
<service-application appid="org.example.tidlcustomactionsample"
                     exec="tidl-custom-action-sample" type="capp"
                     multiple="false" auto-restart="false" on-boot="false">
    <metadata key="http://tizen.org/metadata/action"
              value="App_Example.Action.Bookmark_Save.action"/>
    <metadata key="http://tizen.org/metadata/action/entity"
              value="Example.Entity.Bookmark.entity"/>
    <metadata key="http://tizen.org/metadata/action/provider"
              value="App_Example.Action.Bookmark_Save"/>
</service-application>
```

| Key | Value | Purpose |
|---|---|---|
| `http://tizen.org/metadata/action` | `.action` filename under the package `res/` directory | Installs the Action definition |
| `http://tizen.org/metadata/action/entity` | `.entity` filename under the package `res/` directory | Installs the Entity definition |
| `http://tizen.org/metadata/action/provider` | The exact `.action` `name` | Registers the current `appid` as a provider |

Add one definition and one provider entry per Action, and one Entity entry per application-owned Entity file. Provider metadata must list each Action name; a category value is silently ignored. If an application declares an Action or Entity name already owned by the platform, the package installation is rejected.

The Action and Entity resource files must be installed under the package `res/` directory. The manifest also needs the privileges that allow the TIDL proxy to connect to the service stub:

```xml
<privileges>
  <privilege>http://tizen.org/privilege/datasharing</privilege>
  <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
</privileges>
```

Declare only the minimum privileges required by the platform security policy for your application.

## View Annotation for DALi applications

A DALi application can expose meaningful UI elements to an Agent by attaching an annotation to an `Actor`. The built-in provider in `dali-adaptor` answers the platform `Tizen.Action.View` Actions (`View_FindById`, `View_GetAnnotatedViews`, `View_GetFocusedView`, and `View_ToPresentation`), so the application does not register View provider metadata or generated View stubs.

DALi version 2.5.36 or later is required. Attach an annotation as follows:

```cpp
auto card = Dali::Toolkit::TextLabel::New("Now Playing");
card.SetAnnotation("music:now-playing", "Tizen.Entity.Music",
                   R"({"Title":"Morning Jazz"})");
window.Add(card);
```

- The first argument is the application-defined logical entity ID, the second is the entity type, and the third is a JSON string containing Entity fields (use an empty string if there is no data).
- Both the entity ID and entity type must be non-empty for the annotation to be valid.
- One Actor has one annotation; `SetAnnotation()` replaces the existing one. Use `GetAnnotation()` and `ClearAnnotation()` to inspect or remove it.
- If your application is built on `dali-ui-foundation`, the same three-argument API is available on `Dali::Ui::View`.

Do not store the runtime View ID (from `actor.GetId()`) as the application's entity ID: recreating a View can change its View ID, but the logical entity ID must remain the same. Expose screen state only, and do not place sensitive data or an unnecessary complete UI hierarchy in a View Entity.

## Verify on the target device

After building and installing the package, check registration and execution with `action-tool`:

```bash
sdb shell action-tool get-action App_Example.Action.Bookmark_Save
sdb shell action-tool get-entity Example.Entity.Bookmark
sdb shell 'action-tool search bookmark --json'

sdb shell action-tool execute '{
  "id": 1,
  "params": {
    "name": "App_Example.Action.Bookmark_Save",
    "appid": "org.example.tidlcustomactionsample",
    "arguments": {
      "Id": "bookmark-1",
      "Url": "https://docs.tizen.org",
      "Title": "Tizen Documentation"
    }
  }
}'
```

If discovery fails, check the following:

1. `/usr/share/packages/<pkgid>.xml` exists.
2. Metadata values match the files under `/usr/apps/<pkgid>/res`.
3. The Action JSON validates and `details.appid` matches the provider manifest `appid`.
4. The package-manager and Action metadata parser logs.
5. Provider metadata contains exact Action names, not a category.

For View Annotation, enumerate providers and Views first, and use a returned `View.Id` (not the annotation's entity ID) with the remaining Actions:

```bash
sdb shell action-tool find-appids Tizen.Action.View --json
sdb shell action-tool execute \
  '{"id":201,"params":{"name":"Common_Tizen.Action.View_GetAnnotatedViews","appid":"<APP_ID>","arguments":{}}}'
```

In the response, `isError` indicates whether the request reached the provider, while `return.Success` indicates whether the provider's application logic succeeded. Evaluate both values separately.

## Related information
* Dependencies
  - Tizen 10.1 and Higher
