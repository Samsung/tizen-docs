# Device Definition

The device definition is stored in a JSON configuration file that you need to provide. The following table describes the key components of a JSON file skeleton.

**Table: JSON file key components**
<table>
	<thead>
		<tr>
			<th>JSON configuration file skeleton</th>
			<th>Key component</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
              <pre><code>
{
   "device": [
      {
         "specification": {
            ...
            ...
         },
         "resources": {
            ...
            ...
         }
      }
   ],
   "resourceTypes": [
    ...
    ...
   ],
   "configuration": {
      "easySetup": {
         ...
         ...
      },
      "wifi": {
         ...
         ...
      },
      "filePath": {
         ...
         ...
      }
   }
}
</code></pre>
			</td>
			<td>
			<ul>
				<li><code>"device"</code> = Array of devices (each device specification and resources), only a device is supported currently.</li>
				<li><code>"specification"</code>: Contains device and platform information.</li>
				<li><code>"resources"</code>: Contains single and collection resources.</li>
				<li><code>"resourceTypes"</code>: Resource type database for all resources present in <code>"device" &gt; "resources"</code>.</li>
				<li><code>"configuration"</code>: Configuration info.</li>
				<li><code>"easySetup"</code>: Configuration info for Easy Setup.</li>
				<li><code>"wifi"</code>: Supported Wi-Fi related info.</li>
				<li><code>"filePath"</code>: File location where additional security and certificate files are stored.</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

## Device Specification Component

The `"device" > "specification"` component has 2 subsections: 
-   `"device"` contains device information. It has the following fields:
    -   `deviceType`: Device type based on the OCF specification
    -   `deviceName`: Name of the device that you want to create
    -   `specVersion`: OCF specification followed for the device
    -   `dataModelVersion`: OCF resource type followed for the device
-   `"platform"` contains the platform information. It has the following fields:
    -   `manufacturerName`: Name of the manufacturer. Manufacturer Identifier issued by DevWorkSpace
    -   `manufacturerUrl`: Manufacturer Web site
    -   `manufacturingDate`: Date of manufacturing
    -   `modelNumber`: Device model number
    -   `platformVersion`: Platform version
    -   `osVersion`: Operating system version
    -   `hardwareVersion`: Hardware revision information
    -   `firmwareVersion`: Firmware version
    -   `vendorId`: Vendor identification

The following example shows a sample entry for the `"device" > "specification"` component:

```
"specification": {
   "device": {
      "deviceType": "oic.d.networkaudio",
      "deviceName": "[av] Samsung",
      "specVersion": "core.1.1.0",
      "dataModelVersion": "res.1.1.0"
   },
   "platform": {
      "manufacturerName": "samsung",
      "manufacturerUrl": "http://www.samsung.com/sec/",
      "manufacturingDate": "2017-08-31",
      "modelNumber": "NWSP-01",
      "platformVersion": "1.0",
      "osVersion": "1.0",
      "hardwareVersion": "1.0",
      "firmwareVersion": "1.0",
      "vendorId": "VD-NetworkAudio-2017"
   }
}
```

## Device Resources Component

The device acts as an IoTivity server and can host a number of resources. These resources can be published to the cloud and can be controlled through the Samsung Connect (or IoTivity Client) Application using the resource URI. Each resource has a unique resource URI on the device.

The `"device" > "resources"` component can be of 2 types:

-   Single: Resources are standalone resources. These types of resources are mostly used by simple devices, such as temperature sensor and electric bulb.

    All single resources can be represented using array values with `"single"` as a key under `"resources"`:

    ```
    "resources": {
       "single": [
          {
             Resource Information #1
          },
          {
             Resource Information #2
          },
          ...
          {
             Resource Information #N
          }
       ]
    }
    ```

    A single resource has the following fields:

    -   `uri`: Uniform Resource Identifier to identify the resource
    -   `types`: OCF defined resource type applicable for the resource
    -   `interfaces`: OCF-defined interfaces where resources are registered
    -   `policy`: Possible policy values are: `b0001` (discoverable), `b0010` (observable), `b0100` (secure)

    The following example shows a sample entry for the `"device" > "resources" > "single"` component:

    ```
    {
       "uri": "/switch",
       "types": [
          "oic.r.switch.binary"
       ],
       "interfaces": [
          "oic.if.a",
          "oic.if.baseline"
       ],
       "policy": 7
    }
    ```

-   Collection: Multiple resources can be controlled using a collection resource. Collection resource can have 1 or more resources as links. For example, robot cleaner and refrigerator.

    All collection resources can be represented using array values with `"collection"` as a key under `"resources"`. A collection resource has a very similar structure as a single resource, as it has all the same fields. In addition, the collection resource has links, which are the array of resource information that are part of that collection.

    The collection resource `"types"` field is set to `"oic.wk.col"` to distinguish the single and collection resources.

    The following example shows a sample entry for the `"device" > "resources" > "collection"` component:

    ```
    "resources": {
       "collection": [
          {
             "uri": "/led",
             "types": [
                "oic.wk.col"
             ],
             "interfaces": [
                "oic.if.baseline",
                "oic.if.ll",
                "oic.if.b"
             ],
             "links": [
                {
                   Resource Information #1
                },
                {
                   Resource Information #2
                },
                ...
                {
                   Resource Information #N
                }
             ],
             "policy": 7
          }
       ]
    }
    ```

> **Note**
>
> Make sure that the resources are not duplicated in the `"single"` and `"collection"` components.

## Resource Type Component

The `"resourceTypes"` component is a database of all the resource types present in the current configuration.

The following fields are present for each resource type entry:

-   `type`: Resource type that is present in the current configuration
-   `properties`: Array of property information of a specified resource type

The following example shows a sample entry for the `"resourceTypes"` component:

```
"resourceTypes": [
   {
      "type": "oic.r.switch.binary",
      "properties": [
         {
            Property Information #1
         },
         {
            Property Information #2
         },
         ...
         {
            Property Information #N
         }
      ]
   },
   {
      "type": "oic.r.audio",
      "properties": [
         {
            Property Information #1
         },
         {
            Property Information #2
         },
         ...
         {
            Property Information #N
         }
      ]
   }
]
```

Each property has the following fields:

-   `key[string]`: Key of a property
-   `type[int]`: Data type of the property value:
    -   0: boolean
    -   1: integer
    -   2: double
    -   3: string
    -   4: object
    -   5: bytes
    -   6: integer array
    -   7: double array
    -   8: string array
    -   9: object array
-   `rw[int]`: Access authority of the property:
    -   read(b0001)
    -   write(b0010)
    -   both(b0011)
-   `mandatory[bool]`: Whether the property is mandatory according to the property access authority (rw)

The following example shows a sample entry for the `"resources"` and `"resourceTypes"` component. The resource types used in the resources must be defined in the resource types.

**Example: Defining resource types**

<table>
	<tbody>
		<tr>
			<td valign="top">
			<pre><code>
"resources": {
   "single": [
      {
         "uri": "/switch",
         "types": [
            <span class="highlight">"oic.r.switch.binary"</span>
         ],
         "interfaces": [
            "oic.if.a",
            "oic.if.baseline"
         ],
         "policy": 7
      },
      {
         "uri": "/audio",
         "types": [
            <span class="highlight">"oic.r.audio"</span>
         ],
         "interfaces": [
            "oic.if.a",
            "oic.if.baseline"
         ],
         "policy": 7
      }
   ]
}
</code></pre>
			</td>
			<td>
			<pre><code>
"resourceTypes": [
   {
      "type": <span class="highlight">"oic.r.switch.binary"</span>,
      "properties": [
         {
            "key": "value",
            "type": 0,
            "mandatory": true,
            "rw": 3
         }
      ]
   },
   {
      "type": <span class="highlight">"oic.r.audio"</span>,
      "properties": [
         {
            "key": "volume",
            "type": 1,
            "mandatory": true,
            "rw": 3
         },
         {
            "key": "mute",
            "type": 0,
            "mandatory": true,
            "rw": 3
         }
      ]
   }
]
</code></pre>
			</td>
		</tr>
	</tbody>
</table>

## Configuration Component

The `"configuration"` component has the following fields:

-   `easySetup[object]`: Defines easy-setup information.
    -   `connectivity[object]`: Defines connectivity information.
        -   `type[int]`: Connectivity type for easy-setup: 1 (SoftAP)
        -   `softAP[object]`: Defines softap information that is supported in the thing.
            -   `setupId[string]`: Setup identifier
            -   `artik[bool]`: Whether the ARTIK certificate is used
    -   `ownershipTransferMethod[int]`: Authentication method during easy-setup: b0001(Random PIN-based) or b0010(UserConfirm-based)
-   `wifi[object]`: Defines the supported Wi-Fi specification.
    -   `interfaces[int]`: Supported Wi-Fi interfaces: b000001(a), b000010(b), b000100(g), b001000(n), or b010000(ac)
    -   `frequency[int]`: Supported Wi-Fi frequency: b0001(2.4G) or b0010(5G)
-   `filePath[object]`: Defines the full file path of some read and write files.
    -   `svrdb[string]`: Full (or relative) path for the security database file
    -   `provisioning[string]`: Full (or relative) path for the provisioning data file
    -   `certificate[string]`: Full (or relative) path for the certificate file
    -   `privateKey[string]`: Full (or relative) path for the privateKey file


  > **Note**
  >
  > Optionally, if you want to configure the read-only and read-write paths in the `st_things_set_configuration_prefix_path()` function, you only need to define the file names or relative path in the `filePath` object.
  >
  > For example, if the optional function is invoked with `st_things_set_configuration_prefix_path("/mnt/ro", "/mnt/rw");`, the read-only configuration files are prefixed with `/mnt/ro` and the read-write configuration files are prefixed with `/mnt/rw`.

For more information on Easy Setup, see <https://wiki.iotivity.org/easy_setup>.

The following example shows a sample entry for the `"configuration"` component. To configure a device for easy setup, the following details must be included in the configuration file.

```
"configuration": {
   "easySetup": {
      "connectivity": {
         "type": 1,
         "softAP": {
            "setupId": "sid",
            "artik": true
         }
      },
      "ownershipTransferMethod": 2
   },
   "wifi": {
      "interfaces": 31,
      "frequency": 3
   },
   "filePath": {
      "svrdb": "/things/my/svrdb.dat",
      "provisioning": "/things/my/provisioning.json",
      "certificate": "/things/my/certificate.pem",
      "privateKey": "/things/my/privatekey.der"
   }
}
```

> **Note**
>
> Optionally, if you want to configure the read-only and read-write paths, you can define the file names only in the configuration file, and specify the paths in the `st_things_set_configuration_prefix_path()` function:
> ```
> "filePath": {
>   "svrdb": "svrdb.dat",
>   "provisioning": "provisioning.json",
>   "certificate": "certificate.pem",
>   "privateKey": "privatekey.der"
> }
>
> st_things_set_configuration_prefix_path("/ropath/XXX/res", "/rwpath/XXX/data");
> ```
