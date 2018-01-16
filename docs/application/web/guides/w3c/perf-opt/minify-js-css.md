# JavaScript and CSS Minification

File minification improves application performance as unnecessary data is being removed. For example, page loading time can be decreased by reducing the number of JavaScript and CSS files.

This feature is supported in mobile and wearable applications only.

Minifying tools, such as [Closure Compiler](https://developers.google.com/closure/compiler/) and [Grunt](http://gruntjs.com/), include features that can combine and reduce JavaScript file. The following table shows Closure Compiler and Grunt features in comparison.

**Table: Comparison of minifying tools**

| Item     | Closure Compiler                         | Grunt                                    |
| -------- | ---------------------------------------- | ---------------------------------------- |
| Summary  | JavaScript-optimized compiler created by Google | Task-based automatic JavaScript build tool |
| Features | File compilation, minimizing size					Can be integrated with Ant Builder for automatic features | File compilation plug-in					Minimizing JavaScript and CSS					Various plug-ins (JavaScript, CSS compilation, and compression)					Application performance improvement based on the decrease of request count, transferred data, and transfer time |
| Usage    | Java applicationsProvided as a `.jar` file, used as a command line.				[Web application](http://closure-compiler.appspot.com/home)				RESTful API | `Node.js` installation				`grunt-cli` installation				`package.json` must be inserted to the project root				Task definition in the `gruntfile.js` file |

Grunt has advantages in terms of expandability by providing various plug-ins. For more information on Grunt, see:

- [Installing and using Grunt](#installing-and-using-grunt)
- [Improvement through Grunt](#improvement-through-grunt)

## Installing and Using Grunt

The Grunt tool provides application performance improvement based on the decrease of request count, transferred data, and transfer time.

### Prerequisites

The commands used for installing and using Grunt work in the same manner, without any changes, across most of the major operating systems. To run the commands, you may need to use sudo (for Linux and BSD), or run your command shell as Administrator (for Windows®).

### Installing Grunt

1. Install the [Node.js](http://www.nodejs.org/) platform. The platform includes the Node.js package manager, npm, which is used to install Grunt CLI (command line interface).

2. Install Grunt CLI:

   ```
   npm install -g grunt-cli /* -g: global type */
   ```

### Using Grunt

1. Change to the root directory of the project:

   ```
   cd <Project root>
   ```

2. Install Grunt and create the `Gruntfile.js` file:`npm install grunt --save-dev`

3. Create the `package.json` file: When executing the following command, interactive prompt that receives information on the project is executed. Through the information entered, the `package.json` file is created.`npm init`

4. Install Grunt plug-in:

   ```
   /* Install grunt concat */
   npm install grunt-contrib-concat --save-dev

   /* Install grunt contrib uglify */
   npm install grunt-contrib-uglify --save-dev

   /* Install grunt contrib cssmin */
   npm install grunt-contrib-cssmin --save-dev
   ```

5. Run the Grunt plug-in:

   ```
   grunt
   ```

   Using the `Gruntfile.js` file, tasks, such as `concat`, `uglify`, and `cssmin`, are registered.

## Improvement through Grunt

After running the Grunt plug-in, the following comparison result is shown through the inspector in the Google Chrome™ browser. The expected results vary depending on the application, but since the improvement effects are certain, it is recommended to use Grunt.

> **Note**  
> For the sake of comparing improvement, in the following examples, 2 Web applications have been arbitrarily chosen and named App#1 and App#2.

**Table: Result for App #01**

| Item                                     | Item              | Request (count)    | Request (count)    | Transferred data (mb) | Transferred data (mb) | Onload time (s)    | Onload time (s)    |
| ---------------------------------------- | ----------------- | ------------------ | ------------------ | --------------------- | --------------------- | ------------------ | ------------------ |
| Item                                     | Item              | Result             | Improvement        | Result                | Improvement           | Result             | Improvement        |
| Original                                 | Original          | 254                | -                  | 6.66                  | -                     | 3.28               | -                  |
| Minification applied (accumulated result) | #01_grunt_concat  | 68                 | -186               | 6.62                  | -0.04                 | 2.43               | -0.85              |
| Minification  applied (accumulated result) | #02_grunt_uglify  | 68                 | -                  | 1.9                   | -4.72                 | 1.59               | -0.85              |
| Minification  applied (accumulated result) | #03_grunt_cssmin  | 68                 | -                  | 1.87                  | -0.03                 | 1.61               | 0.02               |
| Total  improvement                       | Total improvement | 73.23% improvement | 73.23% improvement | 71.92% improvement    | 71.92% improvement    | 51.07% improvement | 51.07% improvement |

**Table: Result for App #02**

| Item                                     | Item             | Request (count) | Request (count)     | Transferred data (mb) | Transferred data (mb) | Onload time (s) | Onload time (s)     |
| ---------------------------------------- | ---------------- | --------------- | ------------------- | --------------------- | --------------------- | --------------- | ------------------- |
| Item                                     | Item             | Result          | Improvement         | Result                | Improvement           | Result          | Improvement         |
| Original                                 | Original         | 235             | -                   | 7.89                  | -                     | 5.8             | -                   |
| Minification applied (accumulated result) | #01_grunt_concat | 106             | -129                | 7.87                  | -0.02                 | 5.15            | -0.65               |
| Minification  applied (accumulated result) | #02_grunt_uglify | 106             | -                   | 5.85                  | -2.02                 | 4.95            | -0.19               |
| Minification  applied (accumulated result) | #03_grunt_cssmin | 106             | -                   | 5.84                  | -0.01                 | 4.89            | -0.06               |
| Total  improvement                       | -                | -               | 54.89%  improvement | -                     | 25.98%  improvement   | -               | 15.63%  improvement |

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
