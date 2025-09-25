# Get Started with Core and Memory Profiler

## Get Started with Core Profiler
This tutorial will guide you on how to use profiler in Visual Studio for tizen projects

### Recording Profiling Sessions

To record a profiling session:
1. In the Visual Studio menu, select **Tools &gt; Tizen &gt; Profiler &gt; Run Profiler**.  
  The profiler configuration dialog opens.

2. Define the profiling options.  
    ![Profiler configuration](media/profiler-config.png)
    - **Path to application** is automatically filled with the information for the current solution.
    - **Profiling Preset**  
    You can select from the following predefined profiling configurations:
      - **CPU Sampling**  
        Trace CPU and source lines, but not memory allocation.
      - **Memory Allocation**  
        Trace memory allocation and source lines, but not CPU.
      - **Complex Profiling**  
        Trace CPU, source lines, and memory allocation.
    - **Sampling Options**  
    You can set the following sampling options:
      - **Sampling Interval**  
        You can set the sampling time interval, in milliseconds. The default is 10 ms.
      - **High Granularity**  
        You can switch on high-granularity sampling. It enables better precision and sample regularity, at the cost of efficiency.
    - **Trace Options**  
    You can set the following trace options:
      - **Trace Execution**  
        You can trace CPU utilization.
      - **Trace Memory**  
        You can trace memory allocation for methods.
      - **Trace Garbage Collection**  
        You can trace garbage collection.
      - **Trace Source Lines**  
        You can switch on line source mapping.
      - **Stack Track**  
        You can enable a hybrid trace, which registers stack changes on memory allocation.
    - **CPU Tracing Options**  
    You can set the following CPU tracing options:
      - **Enable CPU Tracing**  
        You can switch on the CPU tracing features.
      - **Trace Process**  
        You can trace the application's CPU utilization.
      - **Trace Threads**  
        You can trace each processing thread's CPU utilization.
      - **Trace Interval (ms)**  
        You can set the sampling time interval, in milliseconds.
    - **Misc Options**  
    You can set the following additional option:
      - **Delayed start**  
        You can delay the application startup.

3. To start the profiling session, click **OK**.  
    The application is installed and launches on the emulator.  
    The **Output** panel displays the installation log, including any errors.  
    ![Output panel](media/profiler-output-window.png)

    The **Profiling Progress** panel shows live CPU and memory usage information.  
    ![Profiling progress](media/profiler-progress.png)

4. To pause and resume profiling, in the **Profiling Progress** panel, click **Pause** and **Resume**.  
    The chart in the **Profiling Progress** panel uses a light-blue background to distinguish the time period when profiling is paused.  

5. To stop profiling, click **Stop**.  
The application is terminated and the profiling data is retrieved from the emulator.

   ![Stop profiling](media/profiler-execute-stop.png)

### Managing Profiling Sessions

To manage the recorded profiling sessions:
1. In the Visual Studio menu, select **Tools &gt; Tizen &gt; Profiler &gt; Session Explorer**.  

   The **Session Explorer** panel opens. It lists the profiling sessions collected from the current solution.  
   ![Session Explorer](media/profiler-session-explorer.png)  


2. You can add a user-defined annotation to a session to, for example, identify what was tested during that session.  
   To add an annotation:
   1. In the **Session Explorer**, right-click the session and select **Edit Annotation**.  
      ![Edit annotation](media/profiler-session-explorer-context-menu.png)
   2. Enter the annotation text, and click **Ok**.  
      ![Edit annotation text](media/profiler-edit-annotation.png)

3. To view the session properties, click the session in the **Session Explorer**.  
   The **Properties** panel (below the **Session Explorer** panel by default) displays additional information about the session, such as the profiling options used for the session.  
   ![Session properties](media/profiler-session-properties.png)

4. To delete a session, in the **Session Explorer**, right-click the session and select **Delete**.

### Viewing Profiling Sessions

To view a profiling session, in the **Session Explorer**, double-click on the session you want to view.  
A session view opens, consisting of 3 panels:

- Filters panel on the left
- Timeline panel in the center
- Methods panel on the right
  
**Figure: Session view**  

![Session view](media/profiler-session-analysis.png)

### Filters Panel

You can filter the profiling data by selecting from the following options:
  - **Call Tree and Methods** filters define which information is displayed in the methods panel:  
    - **Time** shows how much time each method has occupied.
    - **Allocated Memory** shows how much memory was allocated for each method.
    - **Samples** shows the number of samples for each method.
  - **Thread Timeline** filters define which information is displayed in the timeline panel.  
  You can display **GC** (garbage collection), **JIT** (just-in-time compilation), or **Cpu Utilization**.

### Timeline Panel

The timeline panel consists of 2 parts:
- The upper part of the panel shows the overall CPU utilization chart.

  ![CPU utilization](media/profiler-cpu-utilization.png)

- The lower part of the panel shows GC, JIT or CPU utilization charts for each thread, depending on the selected filter.

  ![GC CPU utilization](media/profiler-gc-cpu-utilization.png)

You can select a specific time interval on the timeline, to view the detailed method data for it.  
To select a time interval:
  1. Highlight the interval you want to view in the upper part of the timeline panel.  
  ![Select interval](media/profiler-select-interval.png)  
  The methods panel shows data for the selected interval.
  2. To clear the selected interval, click anywhere in the timeline chart.

### Methods Panel

The criteria for the data shown in the methods panel depends on the selected filter. The following figure shows examples of the data displayed in the methods panel.  

**Figure: Method filters**  

![Method filters](media/profiler-categories.png)

The methods panel consists of 3 tabs:

  - The **Call Tree** tab displays the **Top Methods** and **Call Tree** for the selected thread and time interval.  
  ![Call Tree tab](media/profiler-call-tree-tab.png)

  - The **Hot Path** tab displays the hottest paths for the selected thread and time interval.  
  ![Hotpath tab](media/profiler-hotpath-tab.png)  
  The list displays the hottest methods. To view the call path from the method to its root, expand the list item.

  - The **Hot Lines** tab displays the top source lines for the selected thread and time interval.  The source line numbers are shown in brackets (**[ ]**).  
  ![Hot Lines tab](media/profiler-hotline-tab.png)
  
    To show a "hot line" entry in its source code context, double-click the method in the **Hot Lines** tab. The code line is highlighted with a color intensity corresponding to its hotness.  
    **Figure: "Hot line" in context**  
    !["Hot line" in context](media/profiler-jump-to-line.png)


## Get Started with Memory Profiling

### Step 1. Running Memory Profiler
   - In the menu, choose **Tools > Tizen > Profiler > Run Memory Profiler**.

     ![Run Memory Profiler](media/run_memory_profiler.png)

   - If no Tizen device is connected and no Tizen emulators are running then Emulator Manager will be started. Please launch the type of emulator you want to use for running and profiling your application.

     ![Launch Emulator](media/start_emulator.png)


   - If everything is OK then the application starts as if you run it normally (using Start Debugging in Visual Studio).

     ![Tizen application running](media/memory_profiling_app_started.png)


   - Output Window will display any information messages (debug, warnings, and so on).

     ![Memory Profiler Output Window](media/memory_profiling_msvs_output.png)


   - The memory profiling data will be displayed with the Memory Profiler GUI after finishing the application or after closing it. The application can be closed by pressing "Home" or "Back" buttons.

     ![Close Application](media/close_application.png)


   - Also you can display any previous debug session with Session Explorer (In the menu, **Tools > Tizen > Profiler > Session Explorer**).

     ![Open Session Explorer](media/open_session_explorer.png)

     ![Open Session Explorer](media/session_explorer_memory_profiler.png)

### Step 2. Analyzing the results
   - The GUI application provides several views to the memory profiling data. The views include:

       - summary page with information on which process was profiled, its total runtime, some memory related statistics, and so on.
       - bottom-up table tree view of the code locations that allocated memory with their aggregated cost and stack traces
       - caller/callee table
       - top-down table tree view of the code locations
       - managed heap table tree view
       - flame graph visualization (explanation: <http://www.brendangregg.com/FlameGraphs/memoryflamegraphs.html>)
       - consumed memory size over time graph
       - number of instances over time graph
       - number of memory allocations over time graph
       - size of memory allocated over time graph
       - allocation histogram displaying the number of allocations (the total number and the several topmost code locations) belonging to one of the groups divided by allocation size (0 - 8 bytes, 9 - 16 bytes, ... , 512 bytes - 1 KB, more than 1 KB)

### Managed heap view sample

   ![Managed heap view](media/memory_profiler_gui_managed_heap.png)

### Flame graph view sample

   ![Flame graph view](media/memory_profiler_gui_flame_graph.png)

### Memory allocations graph view sample

   ![Memory allocations graph view](media/memory_profiler_gui_allocations_graph.png)

### Allocation histogram view sample

   ![Allocation histogram view](media/memory_profiler_gui_allocation_histogram.png)
