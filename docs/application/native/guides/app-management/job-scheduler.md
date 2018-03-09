# Job Scheduler

The Job Scheduler API is specific to service applications. Using the Job Scheduler API, service applications can register a background task with trigger conditions. The service application is launched when the trigger condition occurs and can perform the background task.

The main features of the Job Scheduler API include:

-   Registering a job service handler

    To register the job service handler, use the `job_scheduler_service_add()` function to register the job service handler. When the job is triggered, the `job_service_start_cb()` and `job_service_stop_cb()` callbacks are invoked and you can handle the background task in the callbacks.

-   Creating and scheduling a job

    To add the job to the scheduling list, use the `job_scheduler_schedule()` function. You can create the job and set job-execution conditions as trigger events or schedule it for a specific time.

-   Retrieving all scheduled jobs

    To retrieve all scheduled jobs, use the `job_scheduler_foreach_job()` function. As a result, the `job_scheduler_foreach_job_cb` callback is invoked and you can get the scheduled job.

## Prerequisites

To enable your application to use the job scheduler functionality:

1.  To use the Job Scheduler API (in [mobile](../../api/mobile/latest/group__CAPI__JOB__SCHEDULER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__JOB__SCHEDULER__MODULE.html) applications), the application has to request permission. Add the following privilege to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
    </privileges>
    ```

2.  To use the functions and trigger events of the Job Scheduler API, include the `<job_scheduler.h>` header file in your application:

    ```
    #include <job_scheduler.h>
    ```

<a name="register"></a>
## Registering a Job Service Handler

To handle the scheduled job, register a job service handler:

1.  To use the Job Scheduler API, initialize the job scheduler:

    ```
    ret = job_scheduler_init();
    if (ret != JOB_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "Failed to initialize job scheduler. err = %d", ret);
    ```

2.  Create the callbacks for handling the job:

    ```
    static void job_service_start(job_info_h job_info, void *user_data)
    {
        int ret;
        char *job_id = NULL;

        ret = job_info_get_job_id(job_info, &job_id);
        if (ret != JOB_ERROR_NONE) {
            dlog_print(DLOG_ERROR, LOG_TAG, "Failed to get job id. err = %d", ret);
            return;
        }

        dlog_print(DLOG_INFO, LOG_TAG, "[START] job ID: %s", job_id);
        free(job_id);
    }

    static void job_service_stop(job_info_h job_info, void *user_data)
    {
        int ret;
        char *job_id = NULL;

        ret = job_info_get_job_id(job_info, &job_id);
        if (ret != JOB_ERROR_NONE) {
            dlog_print(DLOG_ERROR, LOG_TAG, "Failed to get job id. err = %d", ret);
            return;
        }

        dlog_print(DLOG_INFO, LOG_TAG, "[STOP] job ID: %s", job_id);
        free(job_id);
    }
    ```

    When the trigger condition occurs, the `job_service_start()` function is invoked. And then, the `job_service_stop()` function is invoked. The service application can then perform the background task.

3.  Register the job service handler to handle the job when the job is triggered.

    ```
    job_service_callbacks callbacks = {
        job_service_start,
        job_service_stop
    };
    job_service_h job_service = NULL;

    ret = job_scheduler_service_add("TestJob", &callbacks, NULL, &job_service);
    if (ret != JOB_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "Failed to add job service handler. err = %d", ret);
    ```

<a name="create"></a>
## Creating and Scheduling a Job

To schedule a job, create and schedule the job:

1.  To use the Job Scheduler API, initialize the job scheduler:

    ```
    ret = job_scheduler_init();
    if (ret != JOB_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "Failed to initialize job scheduler. err = %d", ret);
    ```

2.  Create a job

    The following example shows how to create a job with a trigger condition when the battery level is critical:

    ```
    job_info_h job_info = NULL;

    ret = job_info_create(&job_info);
    if (ret != JOB_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "Failed to create job info. err = %d", ret);

    ret = job_info_add_trigger_event(job_info, JOB_TRIGGER_EVENT_BATTERY_LEVEL_CRITICAL);
    if (ret != JOB_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "Failed to add trigger event. err = %d", ret);
    ```

    When the battery status is at critical level, the job is triggered.

    The following example shows how to create a periodic job with a specific requirement. Example, the interval is set to 20 minutes and the requirement is that the battery status must not be low:

    ```
    job_info_h job_info = NULL;

    ret = job_info_create(&job_info);
    if (ret != JOB_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "Failed to create job info. err = %d", ret);

    ret = job_info_set_periodic(job_info, 20);
    if (ret != JOB_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "Failed to set periodic interval. err = %d", ret);

    ret = job_info_set_requires_battery_now_low(job_info, true);
    if (ret != JOB_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "Failed to set the requirement. err = %d", ret);
    ```

    > **Note**  
    > The platform does not guarantee the accuracy of the given interval for minimizing the wakeup of the device. Hence, you must not rely on the platform for timing.

3.  Schedule the job:

    ```
    ret = job_scheduler_schedule(job_info, "TestJob");
    if (ret != JOB_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "Failed to schedule the job. err = %d", ret);
    ```

4.  When no longer needed, release the job info:

    ```
    ret = job_info_destroy(job_info);
    if (ret != JOB_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "Failed to destroy job info. err = %d", ret);
    ```

<a name="retrieve"></a>
## Retrieving all Scheduled Jobs

To retrieve all scheduled jobs:

1.  To use the Job Scheduler API, initialize the job scheduler:

    ```
    ret = job_scheduler_init();
    if (ret != JOB_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "Failed to initialize job scheduler. err = %d", ret);
    ```

2.  Create a callback for retrieving the scheduled job:

    ```
    static bool foreach_job(job_info_h job_info, void *user_data)
    {
        int ret;
        char *job_id = NULL;

        ret = job_info_get_job_id(job_info, &job_id);
        if (ret != JOB_ERROR_NONE) {
            dlog_print(DLOG_ERROR, LOG_TAG, "Failed to get job ID, err = %d", ret);
            return false;
        }

        dlog_print(DLOG_INFO, LOG_TAG, "Job ID: %s", job_id);
        free(job_id);

        return true;
    }
    ```

3.  Retrieve all the scheduled jobs:

    ```
    ret = job_scheduler_foreach_job(foreach_job, NULL);
    if (ret != JOB_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "Failed to retrieve jobs. err = %d", ret);
    ```

## Related Information
- Dependencies
  -  Tizen 4.0 and Higher
