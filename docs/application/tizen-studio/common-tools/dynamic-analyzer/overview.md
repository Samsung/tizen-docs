# Monitoring Performance with Dynamic Analyzer

The Dynamic Analyzer is a performance monitoring and analysis tool for your native and Web applications on a Tizen device or the emulator. The main focus of the Dynamic Analyzer is to analyze your application for potential performance issues, such as high usage of CPU, memory, file, or network operations.

The Dynamic Analyzer is designed to analyze performance issues on your application after development, to help you optimize the application. The following figure shows the basic workflow for how the Dynamic Analyzer works with other Tizen tools:

1. Develop your application with the Tizen Studio.
2. Compile and install the application to an emulator or Tizen device target.
3. Verify the application on the target and fix any functional issues to fulfill the requirements.
4. Profile the application with the Dynamic Analyzer.
5. Study the tracing result and fix any performance issues.

**Figure: Basic workflow using Dynamic Analyzer**

![Basic workflow using Dynamic Analyzer](./media/dynamic_analyzer_basic_workflow.png)

Using the various profiling features of the Dynamic Analyzer, you can determine where your application can be optimized further.

## Profiling Features

When the Dynamic Analyzer is launched, a feature selection dialog opens. You can select the available features for your profiling based on the selected target profile.

**Figure: Feature selection dialog**

![Feature selection dialog](./media/dynamic_analyzer_feature_selection.png)

The following table lists the supported features on the Dynamic Analyzer. Every feature is placed onto a specific group (CPU, Memory, File System, Graphics, Network, UI, Synchronization, or Energy) to help you understand the profiling category.

**Table: Available features**

| Group           | Feature                                  | Description                              | Page tab where shown |
|-----------------|------------------------------------------|------------------------------------------|----------------------|
| CPU             | ![CPU Usage](./media/dynamic_analyzer_cpu_usage.png) <br>CPU Usage | Shows the total CPU usage made by target processes on a system and the CPU usage in percentages. | **Timeline** |
| CPU             | ![Core Usage](./media/dynamic_analyzer_core_usage.png) <br>Core Usage | Shows the usage of each core on a device (or an emulator) in percentages. The number of series on the chart depends on the number of cores--. | **Timeline** |
| CPU             | ![Core Frequency](./media/dynamic_analyzer_core_frequency.png) <br>Core Frequency | Shows the frequency of each core on a device in MHz. This feature is only available on devices, not on emulators. |                      |
| Memory          | ![System Memory](./media/dynamic_analyzer_system_memory.png) <br>System Memory | Monitors the maximum and used memory of the system, and the memory used by a process, in KB. | **Timeline** |
| Memory          | ![Process Memory](./media/dynamic_analyzer_process_memory.png) <br>Process Memory | Monitors a partition of the PSS, 3D, and GEM memory of a process in KB. | **Timeline** |
| Memory          | ![Heap Allocation](./media/dynamic_analyzer_heap_allocation.png) <br>Heap Allocation | Records all memory allocations and frees the requested allocations from the executable and shared libraries. This feature shows un-freed allocations (leak candidates). | **Memory** |
| File System     | ![Disk IO](./media/dynamic_analyzer_disk_io.png) <br>Disk IO | Shows the system I/O events, such as the occurrence of the read/write operations and the number of bytes in them. | **Timeline** |
| File System     | ![File Analysis](./media/dynamic_analyzer_file_analysis.png) <br>File Analysis | Analyzes file activities, such as open, close, and lock operations, in a separate analysis view. | **File** |
| Graphics        | ![OpenGL ES Analysis](./media/dynamic_analyzer_opengl.png) <br>OpenGL ES Analysis | Analyzes OpenGL&reg; (Open Graphics Library) 2.0 and EvasGL information used on a process. It shows detailed OpenGL&reg; API lists, and context, program, and texture information at a particular point in time. | **OpenGL ES** |
| Network         | ![Network IO](./media/dynamic_analyzer_network_io.png) <br>Network IO | Shows the number of bytes that the system sends and receives through the network. | **Timeline** |
| Network         | ![Network Analysis](./media/dynamic_analyzer_network_analysis.png) <br>Network Analysis | Analyzes network activities, such as recv, send, bind, and accept operations, in a separate analysis view. | **Network** |
| UI              | ![UI Event](./media/dynamic_analyzer_UI_event.png) <br>UI Event | Shows the touch (press, move, release), gesture (distance, movement, angle), and orientation change events. | **Timeline** |
| UI              | ![Screenshot](./media/dynamic_analyzer_screenshot.png) <br>Screenshot | Shows a series of screenshot events taken by a user. It can be set to capture a screenshot during each screen transition or at specific time intervals. | **Timeline** |
| UI                | ![UI Hierarchy Analysis](./media/dynamic_analyzer_UI_hierarchy.png) <br>UI Hierarchy Analysis | Analyzes the hierarchy and details of an EFL-based application using EFL UI objects (Evas, Elementary, and Edje). | **UI Hierarchy** |
| Synchronization | ![Thread Analysis](./media/dynamic_analyzer_thread_analysis.png) <br>Thread Analysis | Analyzes the internal threads of a process and its synchronization operation. | **Thread** |
| Energy          | ![Peripheral Status](./media/dynamic_analyzer_peripheral_status.png) <br>Peripheral Status | Shows the on/off state of the Wi-Fi, Bluetooth, GPS, data network, and camera peripherals. | **Timeline** |
| Energy          | ![Power Estimation](./media/dynamic_analyzer_power_estimation.png) <br>Power Estimation | Calculates the power consumption of the CPU, flash, LCD, Wi-Fi, and Bluetooth with an accurate estimation model. | **Timeline** |

## Related information
* Dependencies
  - Tizen Studio 1.0 and Higher
