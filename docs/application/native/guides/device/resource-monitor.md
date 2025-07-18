# Resource Monitor

You can monitor various resources in a unified API with [resource type](#resource_types), [attributes](#resource_attributes), and some [controls](#resource_controls).

The basic procedures for getting monitoring data are simple and unified as below:

-   At first, set up the environment for resources and attributes that are monitored:

    1.  Create a resource instance with the corresponding [resource type](#resource_types).

    2.  If required, set [resource control](#resource_controls) to specify the target among multi-instantiable resources.

    3.  Set interesting [attributes](#resource_attributes) for created resource instance.

-   Now, it is ready to get monitoring data. Repeat the next two steps when the application wants to get resource attributes:

    1.  Request to update the individual resource or all resources at once.

    2.  Get the attribute value along with the type of attributes using APIs listed in the table below.

**Table: Resource Monitor APIs for getting attribute values**

 | Functions                                                                     | Description                                                |
 |-------------------------------------------------------------------------------|------------------------------------------------------------|
 | `resource_monitor_get_value_[int|int64|uint32|uint64|double|string]`          | Get the attribute data                                     |
 | `resource_monitor_get_array_[int|int64|uint32|uint64|double|string]`          | Get array-type attribute data with the corresponding type  |


## Prerequisites

To enable your application to use the Resource Monitor functionalities, follow these steps:

1. To use the [Resource Monitor](../../api/common/latest/group__CAPI__SYSTEM__RESOURCE__MONITOR__MODULE.html) API, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```xml
    <privileges>
       <privilege>http://tizen.org/privilege/systemmonitor</privilege>
    </privileges>
    ```

2. To use the functions and data types of the Resource Monitor API, include the `<system/resource-monitor.h>` header file in your application:

    ```
    #include <system/resource-monitor.h>
    ```

3. To establish and keep connection with internal monitoring daemon, please get monitor id by `resource_monitor_init()` during using resource monitor:
    ```
    int monitor_id = resource_monitor_init();
    ```

<a name="appusage_get_single"></a>
## Get interested attributes from resources

To get the information of various resource attributes in a unified method, follow these steps:

- Get the attributes of singly existing resources without setting controls.
  For example, **the number of possible CPUs** of **SYSTEM** resource:

    ```
    void
    func(int monitor_id, int *num_possible_cpu)
    {
        int error = RESOURCE_MONITOR_ERROR_NONE;
        int res_id = resource_monitor_create_resource(monitor_id, RESOURCE_MONITOR_TYPE_SYSTEM);

        if (res_id < 0) {
            printf("failed to create resource: %d\n", RESOURCE_MONITOR_TYPE_SYSTEM);
            return res_id;
        }

        error = resource_monitor_set_resource_attr(monitor_id, res_id, RESOURCE_MONITOR_SYSTEM_ATTR_POSSIBLE_CPU);
        if (error < 0) {
            printf("failed to set resource atrribute [%d]\n", RESOURCE_MONITOR_SYSTEM_ATTR_POSSIBLE_CPU);
            return error;
        }

        error = resource_monitor_update_resource(monitor_id, res_id);
        if (error < 0) {
            printf("failed to update monitoring data\n");
            return error;
        }

        error = resource_monitor_get_value_int(monitor_id, res_id, RESOURCE_MONITOR_SYSTEM_ATTR_POSSIBLE_CPU, num_possible_cpu);
        if (error < 0) {
            printf("failed to get attribute data\n");
            return error;
        }

        return RESOURCE_MONITOR_ERROR_NONE;
    }
    ```

<a name="appusage_get_multi"></a>
- Get the attributes of multi-instantiable resources along with counting and setting controls.
  For example, **the current frequency** for **all CPUs** resource instance:

    ```
    void
    func(int monitor_id, int *num_cpu, int *results)
    {
        int error = RESOURCE_MONITOR_ERROR_NONE;
        int *cpu_ids
        int res_count;
        int i;

        /* Get the number of available instance */
        error = resource_monitor_get_resource_count(monitor_id, RESOURCE_MONITOR_TYPE_CPU, &res_count);
        if (error < 0) {
            printf("failed to get resource count for res: [%d]\n", RESOURCE_MONITOR_TYPE_CPU);
            return error;
        }

        cpu_ids = calloc(res_count, sizeof(int));
        if (!cpu_ids)
            return RESOURCE_MONITOR_ERROR_OUT_OF_MEMORY;

        /* Create resources and set attributes and controls */
        for (i = 0; i < res_count; i++) {
            cpu_ids[i] = resource_monitor_create_resource(monitor_id, RESOURCE_MONITOR_TYPE_CPU);
            if (cpu_ids[i] < 0) {
                printf("failed to create resource: %d", RESOURCE_MONITOR_TYPE_CPU);
                goto error_cleanup;
            }

            error = resource_monitor_set_resource_attr(monitor_id, cpu_ids[i], RESOURCE_MONITOR_CPU_CUR_FREQ);
            if (error < 0) {
                printf("failed to set resource atrribute [%d]\n", RESOURCE_MONITOR_SYSTEM_ATTR_POSSIBLE_CPU);
                goto error_cleanup;
            }

            error = resource_monitor_set_resource_ctrl(monitor_id, cpu_ids[i], RESOURCE_MONITOR_CTRL_CLUSTER_ID, i);
            if (error < 0) {
                printf("failed to set resource control [%d]\n", RESOURCE_MONITOR_SYSTEM_ATTR_POSSIBLE_CPU);
                goto error_cleanup;
            }
        }

        /* Update attributes */
        error = resource_monitor_update(monitor_id);
        if (error < 0) {
            printf("failed to update monitoring data\n");
            i--;
            goto error_cleanup;
        }

        for (i = 0; i < res_count; i++) {
            error = resource_monitor_get_value_int(monitor_id, res_id, RESOURCE_MONITOR_CPU_CUR_FREQ, &results[i]);
            if (error < 0) {
                printf("failed to get attribute data\n");
                goto error_cleanup;
            }
        }

        *num_cpu = res_count;

        error = RESOURCE_MONITOR_ERROR_NONE;

    error_cleanup:
        for (;i >= 0; i--)
            resource_monitor_delete_resource(monitor_id, cpu_ids[i]);

        free(cpu_ids);

        return error;
    }

    ```

## Resource monitor keys

<a name="resource_types"></a>

The following table lists the available resource types, which are part of the `resource_monitor_type_e` enumeration:

**Table: Resource type keys**

 | Key                                            | Description                               |
 |------------------------------------------------|-------------------------------------------|
 | `RESOURCE_MONITOR_TYPE_CPU`                    | Resource type for CPU clusters            |
 | `RESOURCE_MONITOR_TYPE_BUS`                    | Resource type for BUS devices             |
 | `RESOURCE_MONITOR_TYPE_GPU`                    | Resource type for GPU devices             |
 | `RESOURCE_MONITOR_TYPE_MEMORY`                 | Resource type for main memory             |
 | `RESOURCE_MONITOR_TYPE_BATTERY`                | Resource type for battery                 |
 | `RESOURCE_MONITOR_TYPE_DISPLAY`                | Resource type for display devices         |
 | `RESOURCE_MONITOR_TYPE_SYSTEM'`                | Resource type for system overall status   |
 | `RESOURCE_MONITOR_TYPE_DISK`                   | Resource type for disk devices            |

 <a name="resource_attributes"></a>

The following table lists the available attributes for each resource, which are part of the `resource_monitor_attr_id_e` enumeration:

**Table: Resource attribute keys for CPU**

 | Attribute                                          | Data type | Description                                             |
 |----------------------------------------------------|-----------|---------------------------------------------------------|
 | `RESOURCE_MONITOR_CPU_ATTR_CUR_FREQ`               | int       | Resource attribute for current CPU frequency            |
 | `RESOURCE_MONITOR_CPU_ATTR_MIN_FREQ`               | int       | Resource attribute for minimum CPU frequency            |
 | `RESOURCE_MONITOR_CPU_ATTR_MAX_FREQ`               | int       | Resource attribute for maximum CPU frequency            |
 | `RESOURCE_MONITOR_CPU_ATTR_AVAILABLE_MIN_FREQ`     | int       | Resource attribute for available minimum CPU frequency  |
 | `RESOURCE_MONITOR_CPU_ATTR_AVAILABLE_MAX_FREQ`     | int       | Resource attribute for available maximum CPU frequency  |
 | `RESOURCE_MONITOR_CPU_ATTR_CUR_GOVERNOR`           | string    | Resource attribute for current governor of CPU          |
 | `RESOURCE_MONITOR_CPU_ATTR_NAME`                   | string    | Resource attribute for CPU cluster name                 |

**Table: Resource attribute keys for BUS**

 | Attribute                                          | Data type | Description                                             |
 |----------------------------------------------------|-----------|---------------------------------------------------------|
 | `RESOURCE_MONITOR_BUS_ATTR_CUR_FREQ`               | int       | Resource attribute for current BUS frequency            |
 | `RESOURCE_MONITOR_BUS_ATTR_MIN_FREQ`               | int       | Resource attribute for minimum BUS frequency            |
 | `RESOURCE_MONITOR_BUS_ATTR_MAX_FREQ`               | int       | Resource attribute for maximum BUS frequency            |
 | `RESOURCE_MONITOR_BUS_ATTR_AVAILABLE_MIN_FREQ`     | int       | Resource attribute for available minimum BUS frequency  |
 | `RESOURCE_MONITOR_BUS_ATTR_AVAILABLE_MAX_FREQ`     | int       | Resource attribute for available maximum BUS frequency  |
 | `RESOURCE_MONITOR_BUS_ATTR_CUR_GOVERNOR`           | string    | Resource attribute for current governor of BUS          |
 | `RESOURCE_MONITOR_BUS_ATTR_NAME`                   | string    | Resource attribute for BUS device name                  |

**Table: Resource attribute keys for GPU**

 | Attribute                                          | Data type | Description                                             |
 |----------------------------------------------------|-----------|---------------------------------------------------------|
 | `RESOURCE_MONITOR_GPU_ATTR_CUR_FREQ`               | int       | Resource attribute for current GPU frequency            |
 | `RESOURCE_MONITOR_GPU_ATTR_MIN_FREQ`               | int       | Resource attribute for minimum GPU frequency            |
 | `RESOURCE_MONITOR_GPU_ATTR_MAX_FREQ`               | int       | Resource attribute for maximum GPU frequency            |
 | `RESOURCE_MONITOR_GPU_ATTR_AVAILABLE_MIN_FREQ`     | int       | Resource attribute for available minimum GPU frequency  |
 | `RESOURCE_MONITOR_GPU_ATTR_AVAILABLE_MAX_FREQ`     | int       | Resource attribute for available maximum GPU frequency  |
 | `RESOURCE_MONITOR_GPU_ATTR_CUR_GOVERNOR`           | string    | Resource attribute for current governor of GPU          |
 | `RESOURCE_MONITOR_GPU_ATTR_NAME`                   | string    | Resource attribute for GPU device name                  |

**Table: Resource attribute keys for Memory**

 | Attribute                                          | Data type | Description                                             |
 |----------------------------------------------------|-----------|---------------------------------------------------------|
 | `RESOURCE_MONITOR_MEMORY_ATTR_TOTAL`               | uint64    | Resource attribute for total memory in system           |
 | `RESOURCE_MONITOR_MEMORY_ATTR_AVAILABLE`           | uint64    | Resource attribute for available memory in system       |
 | `RESOURCE_MONITOR_MEMORY_ATTR_FREE`                | uint64    | Resource attribute for free memory in system            |
 | `RESOURCE_MONITOR_MEMORY_ATTR_BUFFER`              | uint64    | Resource attribute for size of buffered page in system  |
 | `RESOURCE_MONITOR_MEMORY_ATTR_CACHED`              | uint64    | Resource attribute for size of cached page in system    |
 | `RESOURCE_MONITOR_MEMORY_ATTR_CMA_TOTAL`           | uint64    | Resource attribute for total memory in CMA zone         |
 | `RESOURCE_MONITOR_MEMORY_ATTR_CMA_FREE`            | uint64    | Resource attribute for free memory in CMA zone          |
 | `RESOURCE_MONITOR_MEMORY_ATTR_SWAP_TOTAL`          | uint64    | Resource attribute for total memory in swap space       |
 | `RESOURCE_MONITOR_MEMORY_ATTR_SWAP_FREE`           | uint64    | Resource attribute for free memory in swap space        |

**Table: Resource attribute keys for Battery**

 | Attribute                                          | Data type | Description                                             |
 |----------------------------------------------------|-----------|---------------------------------------------------------|
 | `RESOURCE_MONITOR_BATTERY_ATTR_CAPACITY`           | int       | Resource attribute for total battery capacity           |
 | `RESOURCE_MONITOR_BATTERY_ATTR_STATUS`             | string    | Resource attribute for status of battery                |
 | `RESOURCE_MONITOR_BATTERY_ATTR_TEMPERATURE`        | int       | Resource attribute for temperature of battery           |
 | `RESOURCE_MONITOR_BATTERY_ATTR_VOLTAGE_NOW`        | int       | Resource attribute for battery voltage                  |
 | `RESOURCE_MONITOR_BATTERY_ATTR_CURRENT_NOW`        | int       | Resource attribute for battery current                  |
 | `RESOURCE_MONITOR_BATTERY_ATTR_PRESENT`            | int       | Resource attribute for presence of battery              |
 | `RESOURCE_MONITOR_BATTERY_ATTR_ONLINE`             | int       | Resource attribute for status of charger connection     |

**Table: Resource attribute keys for Display**

 | Attribute                                          | Data type | Description                                             |
 |----------------------------------------------------|-----------|---------------------------------------------------------|
 | `RESOURCE_MONITOR_DISPLAY_ATTR_FPS`                | double    | Resource attribute for frame per sec for display        |
 | `RESOURCE_MONITOR_DISPLAY_ATTR_NAME`               | string    | Resource attribute for display name                     |

**Table: Resource attribute keys for System**

 | Attribute                                          | Data type      | Description                                             |
 |----------------------------------------------------|----------------|---------------------------------------------------------|
 | `RESOURCE_MONITOR_SYSTEM_ATTR_CPU_UTIL`            | double         | Resource attribute for total CPU utilization            |
 | `RESOURCE_MONITOR_SYSTEM_ATTR_CPU_USER_UTIL`       | double         | Resource attribute for user CPU utilization             |
 | `RESOURCE_MONITOR_SYSTEM_ATTR_CPU_SYS_UTIL`        | double         | Resource attribute for kernel CPU utilization           |
 | `RESOURCE_MONITOR_SYSTEM_ATTR_PER_CPU_UTIL`        | array (double) | Resource attribute for per CPU utilization              |
 | `RESOURCE_MONITOR_SYSTEM_ATTR_PER_CPU_USER_UTIL`   | array (double) | Resource attribute for per CPU user utilization         |
 | `RESOURCE_MONITOR_SYSTEM_ATTR_PER_CPU_SYS_UTIL`    | array (double) | Resource attribute for per CPU kernel utilization       |
 | `RESOURCE_MONITOR_SYSTEM_ATTR_POSSIBLE_CPU`        | int            | Resource attribute for the number of possible CPUs      |
 | `RESOURCE_MONITOR_SYSTEM_ATTR_ONLINE_CPU`          | int            | Resource attribute for the number of online CPUs        |

**Table: Resource attribute keys for Disk**

 | Attribute                                          | Data type | Description                                             |
 |----------------------------------------------------|-----------|---------------------------------------------------------|
 | `RESOURCE_MONITOR_DISK_ATTR_NAME`                  | string    | Resource attribute for disk name                        |
 | `RESOURCE_MONITOR_DISK_ATTR_READ_PER_SEC`          | double    | Resource attribute for read throughput per sec          |
 | `RESOURCE_MONITOR_DISK_ATTR_WRITE_PER_SEC`         | double    | Resource attribute for write throughput per sec         |
 | `RESOURCE_MONITOR_DISK_ATTR_READ_TOTAL`            | uint64    | Resource attribute for total read amount                |
 | `RESOURCE_MONITOR_DISK_ATTR_WRITE_TOTAL`           | uint64    | Resource attribute for total write amount               |


 <a name="resource_controls"></a>

The following table lists the required controls for some resources, which are part of the `resource_monitor_ctrl_id_e` enumeration:

**Table: Resource control keys**

 | Control                                            | Resource type | Description                                             |
 |----------------------------------------------------|---------------|---------------------------------------------------------|
 | `RESOURCE_MONITOR_CPU_CTRL_CLUSTER_ID`             | CPU           | Resource controls for setting CPU cluster id            |
 | `RESOURCE_MONITOR_BUS_CTRL_DEVICE_ID`              | BUS           | Resource controls for setting BUS device id             |
 | `RESOURCE_MONITOR_GPU_CTRL_DEVICE_ID`              | GPU           | Resource controls for setting GPU device id             |
 | `RESOURCE_MONITOR_DISPLAY_CTRL_DEVICE_ID`          | Display       | Resource controls for setting display device id         |
 | `RESOURCE_MONITOR_DISK_CTRL_DEVICE_ID`             | Disk          | Resource controls for setting disk device id            |

## Related information
- Dependencies
  - Since Tizen 7.0
- API References
  - [Resource Monitor API](../../api/common/latest/group__CAPI__SYSTEM__RESOURCE__MONITOR__MODULE.html)
