# Get Started with Performance Profiling

## Running Core Profiler
   - If no Tizen device is connected and no Tizen emulators are running then launch Emulator Manager and launch the type of emulator you want to use for running and profiling your application.

     ![Launch Emulator](media/start_emulator.png)


   - Open the **Command Palette** and select **Tizen.NET: Run Tizen core profiler**.

     ![Run Memory Profiler](media/run_profiler.png)


   - If everything is ok then the application starts as if you are running it normally.

     ![Tizen application running](media/profiling_app_started.png)


   - Profiling progress window will be displayed with a "Stop" button in a new tab showing the application's live performance profiling.

     ![Close Application](media/profiling_progress.png)

   - Profiling can be stopped by clicking the "Stop" button.

     ![Close Application](media/profiling_stop.png)

## Running Memory Profiler
   - If no Tizen device is connected and no Tizen emulators are running then launch Emulator Manager and launch the type of emulator you want to use for running and profiling your application.

     ![Launch Emulator](media/start_emulator.png)


   - Open the **Command Palette** and select **Tizen.NET: Run Tizen memory profiler**.

     ![Run Memory Profiler](media/run_memory_profiler.png)


   - If everything is ok then the application starts as if you are running it normally.

     ![Tizen application running](media/memory_profiling_app_started.png)


   - The memory profiling data will be displayed with the Memory Profiler GUI after closing the application. The application can be closed by pressing the "Back" button.

     ![Close Application](media/close_application.png)

## Analyze the results
   - The GUI application provides several views of the memory profiling data. The views include the following:

       - Summary page with information on which process was profiled, its total runtime, some memory related statistics, and so on.
       - Bottom-up table tree view of the code locations that allocated memory with their aggregated cost and stack traces.
       - Caller/Callee table.
       - Top-down table tree view of the code locations.
       - Managed heap table tree view.
       - Flame graph visualization (explanation: [http://www.brendangregg.com/FlameGraphs/memoryflamegraphs.html](http://www.brendangregg.com/FlameGraphs/memoryflamegraphs.html){:target="_blank"}).
       - Consumed memory size over time graph.
       - Number of instances over time graph.
       - Number of memory allocations over time graph.
       - Size of memory allocated over time graph.
       - Allocation histogram displaying the number of allocations (the total number and the several topmost code locations) belonging to one of the groups divided by allocation size (0 - 8 bytes, 9 - 16 bytes, ... , 512 bytes - 1 KB, more than 1 KB).

### Flame graph view sample

   ![Flame graph view](media/memory_profiler_gui_flame_graph.png)

### Memory allocations graph view sample

   ![Memory allocations graph view](media/memory_profiler_gui_allocations_graph.png)

### Allocation histogram view sample

   ![Allocation histogram view](media/memory_profiler_gui_allocation_histogram.png)