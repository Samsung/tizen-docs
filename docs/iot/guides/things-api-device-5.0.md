# Device Definition

The device definition is stored in two JSON configuration files such as `master.json` and `resource.json` in the directory of shared/res.

## Master JSON File Descriptions
Master JSON file can represent device and configuration for thing agent.

- **devices**[objectArray] : Define device type, name and so on.
  - **deviceType**[string] : Device type of thing
  - **deviceName**[string] : Human friendly name defined by the vendor (n of oic.wk.d)
  - **mnid**[string] : Name of manufacturer (mnmn of oic.wk.p) (Manufacturer Identifier issued by DevWorkSpace)
  - **vid**[string] : Vendor defined string for the platform (vid of oic.wk.p)
  - **nick**[string] : (Optional) Nick name

- **configuration**[object] : Define OTM, certificate type, and easy-setup information.
  - **otm**[int] : Ownership Transfer Method: b0001 (Random PIN-based), b0010 (UserConfirm-based), b0100 (Preconfigured PIN)  
     The default value is 2.
  - **crtType**[int] : Certificate type
    - 1(Test Certificate), 2(Artik Certificate), 3(Custom)  
    To use test certificate as described in [**Get Started**](../get-started/overview.md), the value should be 1.
  - **easySetup**[object] : Easy-setup information
    - **mode**[string] : Easy-setup mode: 1(SoftAP), 2(Custom)  
      To use Soft AP as described in [**Get Started**](../get-started/overview.md), the value should be 1.
    - **setupId**[string] : Setup Identifier. Onboarding ID registered in DevWorkSpace

### Sample Master JSON File
```json
{
	"devices": [
		{
			"deviceType": "oic.d.xxxx",
			"deviceName": "myname",
			"mnid": "myid",
			"vid": "myvid"
		}
	],
	"configuration": {
		"otm": 2,
		"crtType" : 1,
		"easySetup": {
			"mode": 1,
			"setupId": "001"
		}
	}
}
```
## Resource JSON File Descriptions
Resource JSON file can represent resources which can be defined as resource URI, resource types and so on.

- **resources**[object] : Define resources.
  - **single**[objectArray] : Define single resources
    - **device_no**[int] : Device number for multi-device (It can be used only in case of multi-device.  
      The default value is 0)
    - **uri**[string] : URI of resource
    - **types**[stringArray] : Resource types of resource
    - **interfaces**[stringArray] : Interfaces of resource
    - **policy**[int] : Policy (The default value is 7) : b0001 (Discoverable), b0010 (Observable), b0100 (Secure)

  - **collection**[object] : Define collection resource
    - **device_no**[int] : Device number for multi-device (It can be used only in case of multi-device. The default value is 0)
    - **uri**[string] : URI of collection resource
    - **types**[stringArray] : Resource types of collection resource
    - **interfaces**[stringArray] : Interfaces of collection resource
    - **links**[objectArray] : Collection child resources (Array of resource object, refer to 'single' resource definition and below sample JSON)

- **resourceTypes**[objectArray] : Define types of resources.
  - **type**[string] : The name of a resource type

  - **properties**[objectArray] : Properties information of resource type
    - **key**[string] : Property key name
    - **type**[string] : Data type of a property key : boolean, integer, double, string, bytestring, object (In case of 'bytestring', it doesn't support array type)
    - **isArray**[bool] : Indicate whether data type is an array or not. (The default value is false.)
    - **readOnly**[bool] : Indicate access authority of property. (The default value is false.)
    - **mandatory**[bool] : Indicate whether the property is mandatory or not. (The default value is false.)
    - **description**[string] : The description of the property key
    - **enumDescription**[stringArray] : The possible strings for the property value

### Sample Resource JSON File
```json
{
	"resources": {
		"single": [
			{
				"uri": "/capability/switch/main/0",
				"types": [
					"x.com.st.powerswitch"
				],
				"interfaces": [
					"oic.if.a",
					"oic.if.baseline"
				]
			},
			{
				"uri": "/capability/audioVolume/main/0",
				"types": [
					"x.com.st.audiovolume"
				],
				"interfaces": [
					"oic.if.a",
					"oic.if.baseline"
				]
			}
		],
		"collection" :
		{
			"uri" : "/a/room",
			"types" : ["core.room"],
			"interfaces" : [
				"oic.if.b",
				"oic.if.baseline",
				"oic.if.ll"
			],
			"links" :
			[
				{
					"uri" : "/a/fan",
					"types" : [
						"core.fan"
					],
					"interfaces" : [
						"oic.if.baseline"
					]
				},
				{
					"uri" : "/a/light",
					"types" : [
						"core.light"
					],
					"interfaces" : [
						"oic.if.baseline"
					]
				}
			]
		}
	},
	"resourceTypes": [
		{
			"type": "x.com.st.powerswitch",
			"properties": [
				{
					"key": "power",
					"type": "string",
					"isArray": false,
					"readOnly": false,
					"mandatory": true,
					"description": "State of the power switch.",
					"enumDescription": ["on", "off"]
				}
			]
		},
		{
			"type": "x.com.st.audiovolume",
			"properties": [
				{
					"key": "volume",
					"type": "integer",
					"mandatory": true,
					"description": "Volume setting of an audio rendering device."
				},
				{
					"key": "mute",
					"type": "boolean",
					"mandatory": true,
					"description": "Mute setting of an audio rendering device"
				},
				{
					"key": "command",
					"type": "string",
					"description": "Comand for controlling",
					"enumDescription": ["increase", "decrease", "max", "min"]
				}
			]
		},
		{
			"type" : "core.room",
			"properties" : [
				{
					"key" : "name",
					"type" : "string",
					"mandatory" : true
				}
			]
		},
		{
			"type" : "core.fan",
			"properties" : [
				{
					"key" : "state",
					"type" : "boolean",
					"mandatory" : true
				},
				{
					"key" : "speed",
					"type" : "integer",
					"mandatory" : true
				}
			]
		},
		{
			"type" : "core.light",
			"properties" : [
				{
					"key" : "state",
					"type" : "boolean",
					"mandatory" : true
				},
				{
					"key" : "power",
					"type" : "integer",
					"mandatory" : true
				}
			]
		}
	]
}
```
