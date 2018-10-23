# Application

Tizen supports both core and reference applications. Core applications are developed with platform internal interfaces, such as the Enlightenment Foundation Libraries (EFL) and other third party libraries. Reference applications are developed with Tizen native APIs.

The following table shows whether the core and reference versions of the preloaded sample applications are supported by default on the emulator and target device.

**Table: Sample application support**

| Application name | Emulator              |                  | Target                |      |
| ---------------- | --------------------- | ---------------- | --------------------- | ---- |
|                  | **Core application**  | **Reference application** | **Core application** | **Reference application**|
| Calculator       | No                    | Yes              | Yes                   | No   |
| Calendar         | No                    | Yes              | Yes                   | No   |
| CalendarService  | No                    | Yes              | Yes                   | No   |
| Camera           | No                    | Yes              | Yes                   | No   |
| Clock            | No                    | Yes              | Yes                   | No   |
| Contacts         | No                    | Yes              | Yes                   | No   |
| Email            | No                    | Yes              | Yes                   | No   |
| Gallery          | No                    | Yes              | Yes                   | No   |
| Home             | Yes                   | No               | Yes                   | No   |
| ImageViewer      | No                    | Yes              | Yes                   | No   |
| Internet         | No                    | Yes              | No                    | Yes  |
| Lock             | Yes                   | No               | Yes                   | No   |
| Memo             | No                    | Yes              | Yes                   | No   |
| Messages         | No                    | Yes              | Yes                   | No   |
| MusicPlayer      | No                    | Yes              | Yes                   | No   |
| MyFiles          | No                    | Yes              | Yes                   | No   |
| Phone            | No                    | Yes              | Yes                   | No   |
| Settings         | No                    | Yes              | Yes                   | No   |
| VideoPlayer      | No                    | Yes              | Yes                   | No   |

## Configuration

You can switch a preloaded sample application between core and reference applications using the [MIC image creator](../reference/mic/mic-overview.md). To switch the application, remove the preloaded application package and add the new package image with the correct name. The following table shows the core and reference application image names of the preloaded sample applications.

**Table: Sample application image names**

| Application name | Core application            | Reference application  |
| ---------------- | --------------------------- | ---------------------- |
| Calculator       | `org.tizen.calculator`      | `apps.Calculator`      |
| Calendar         | `org.tizen.calendar`        | `apps.Calendar`        |
| CalendarService  | `org.tizencalendar-service` | `apps.CalendarService` |
| Camera           | `org.tizen.camera-app`      | `apps.Camera`          |
| Clock            | `org.tizen.clock`           | `apps.Clock`           |
| Contacts         | `org.tizen.contacts`        | `apps.Contacts`        |
| Email            | `org.tizen.email`           | `apps.Email`           |
| Gallery          | `org.tizen.gallery`         | `apps.Gallery`         |
| Home             | `org.tizen.menu-screen`     | `apps.Home`            |
| ImageViewer      | `org.tizen.image-viewer`    | `apps.ImageViewer`     |
| Internet         | `org.tizen.browser`         | `apps.Internet`        |
| Lock             | `org.tizen.lockscreen`      | `apps.Lock`            |
| Memo             | `org.tizen.memo`            | `apps.Memo`            |
| Messages         | `org.tizen.message`         | `apps.Messages`        |
| MusicPlayer      | `org.tizen.music-player`    | `apps.MusicPlayer`     |
| MyFiles          | `org.tizen.myfile`          | `apps.MyFiles`         |
| Phone            | `org.tizen.call`            | `apps.Phone`           |
| Settings         | `org.tizen.setting`         | `apps.Settings`        |
| VideoPlayer      | `org.tizen.video-player`    | `apps.VideoPlayer`     |

