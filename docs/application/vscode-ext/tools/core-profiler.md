# Core Profiler

- The profiler allows you to analyze the performance of your tizen application. The tools allows to profile CPU and memory usage of app while its running. Currently, profiling is supported only for .NET applications.

## Profiling Progress
After profiling starts, you can see profiling progress in visual studio code view.

## Running Core Profiler
   - If no Tizen device is connected and no Tizen emulators are running then launch Emulator Manager and launch the type of emulator you want to use for running and profiling your application.

     ![Launch Emulator](../getting-started/test-profile-app/media/start_emulator.png)


   - Open the **Command Palette** and select **Tizen.NET: Run Tizen core profiler**.

     ![Run Memory Profiler](../getting-started/test-profile-app/media/run_profiler.png)


   - If everything is ok then the application starts as if you are running it normally.

     ![Tizen application running](../getting-started/test-profile-app/media/profiling_app_started.png)


   - Profiling progress window will be displayed with a "Stop" button in a new tab showing the application's live performance profiling.

     ![Close Application](../getting-started/test-profile-app/media/profiling_progress.png)

   - Profiling can be stopped by clicking the "Stop" button.

     ![Close Application](../getting-started/test-profile-app/media/profiling_stop.png)

     