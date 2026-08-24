# Tizen Action 2.0

Tizen Action 2.0 allows your application to expose its capabilities to an Agent as structured, discoverable tools. The platform defines Actions, Entities, and View Entities; your application implements and registers the capabilities it provides through a TIDL-based service.

The main Tizen Action 2.0 features are:

- Providing platform-defined Actions

  You can implement Actions and Entities defined by the platform specification by generating a service interface from the supplied schemas and implementing its methods.

- Defining application-owned Actions

  You can author your own `.action` and `.entity` schema files, generate the service code, and register the definitions and your application as a provider through manifest metadata.

## Core concepts

| Component | Role |
|---|---|
| Action | A capability an Agent can discover and run. An `.action` file is a JSON schema; a 2.0 TIDL Action has `"type": "tidl"`. |
| Entity | A typed data model passed between Actions. An `.entity` file defines its type name, inheritance, and data schema. |
| View Entity | An Entity describing current UI view information, based on `Tizen.Entity.View`. |
| `actionc` | Converts Actions and Entities into a TIDL interface and generates a service stub. |
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

## Generate the service code

`actionc` converts `.action` and `.entity` files into a `.tidl` interface and runs the TIDL compiler on it to generate a service stub. For a .NET service application, retain the intermediate `.tidl` file with the `--keep-temp` option and generate the C# stub with `tidlc`:

```bash
# Platform-defined category
actionc -a Tizen.Action.Browser --keep-temp -o gen/ImplBrowser

# Application-owned Actions: repeat -i for every Action in the category,
# and add application Entity paths with -e
actionc \
  -i actions/App_Example.Action.Bookmark_Get.action \
  -i actions/App_Example.Action.Bookmark_List.action \
  -i actions/App_Example.Action.Bookmark_Save.action \
  -e entities --keep-temp -o gen/ImplBookmark

# Generate the C# service stub from the intermediate TIDL file
tidlc -s -l C# -i Example.Action.Bookmark.tidl -o ImplBookmark
```

Inherit the generated `ServiceBase` class, implement every abstract Action method, and start listening in your service application, in the same way as any TIDL-based .NET service (see [TIDL](../../../native/guides/app-management/tidl.md)). Do not hand-edit the `.tidl` files or the generated stubs; regenerate them after a schema change. Return failures through the declared `Tizen.Entity.Status` contract, and protect shared state because service methods can be called for multiple connected clients.

> [!NOTE]
> TIDL method order is an RPC ABI contract. For an application-owned category, `actionc -i` preserves the command-line input order, so pass every `-i` in lexicographical order by full Action name. Adding a new Action whose name sorts before an existing method renumbers the wire IDs; treat such an extension as ABI-incompatible and use a new category or version instead.

## Register the provider in the manifest

An application-defined TIDL Action requires Action-definition and provider metadata in `tizen-manifest.xml`. Add Entity metadata only when the package also owns and installs a new Entity; an Action that uses primitives or already-installed platform Entities does not need a new Entity entry:

```xml
<service-application appid="org.example.tidlcustomactionsample"
                     exec="TidlCustomActionSample.dll" type="dotnet"
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

Add one definition and one provider entry per Action, and one Entity entry per application-owned Entity file. Provider metadata must list each Action name; a category value is silently ignored. If an application declares an Action or Entity name already owned by the platform, the package installation is rejected. `details.appid` in the Action schema must match the provider manifest `appid`.

The Action and Entity resource files must be installed under the package `res/` directory. Installing the package makes the metadata parser register the schemas and the provider into the Action catalog, after which Agent discovery is available.

The manifest also needs the privileges that allow the TIDL proxy to connect to the service stub:

```xml
<privileges>
  <privilege>http://tizen.org/privilege/datasharing</privilege>
  <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
</privileges>
```

Declare only the minimum privileges required by the platform security policy for your application.

## Verify on the target device

After building and installing the package, check registration and execution with the `action-tool` CLI:

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
2. Metadata values match the files under the installed package `res/` directory.
3. The Action JSON validates and `details.appid` matches the provider manifest `appid`.
4. The package-manager and Action metadata parser logs.
5. Provider metadata contains exact Action names, not a category.

## Design recommendations

- Reuse the same Entity type for the same semantics so that Actions can be chained.
- Return stable identifiers and actionable failure reasons.
- Keep the actual returned values aligned with the `outputSchema` contract.
- Persist required state so that provider restart and connection auto-dispose are safe; the connection can be recreated at any time.
- Verify success and failure paths, and background, disconnect, and provider-restart behavior under your `allowedBackground` and `autoDispose` settings.

## Related information
* Dependencies
  - Tizen 10.1 and Higher
