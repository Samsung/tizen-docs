# Downloading TAU

Tizen provides 2 versions of the TAU library: an uncompressed version for development and a minified version for production. The development version includes extra warnings about common mistakes, whereas the production version includes extra performance optimizations and strips all error messages.

This feature is supported in mobile and wearable applications only.

To download and build TAU from Git:

> **Note**  
> To build a TAU library, ensure that you have both Git and `Node.js` installed.

1. Download the Git repository:

   a. Clone a copy of the master branch in the TAU Git repository:

      ```
      git clone git://git.tizen.org/platform/framework/web/tau
      ```

   b. Change to the `tau` directory:

      ```
      cd tau
      ```

   c. Check out the latest version of TAU:

      ```
      git checkout master
      ```
      Or check out a specific version of TAU
      ```
      git checkout tau_x.xx.xx
      ```

2. Build TAU:

   a. Install the build module by npm:

      ```
      npm install
      ```

   b. Test that you have grunt installed:

      ```
      grunt -V
      ```
      If grunt is not installed, then run:
      ```
      (sudo) npm install -g grunt-cli
      ```

   c. Build TAU by running the following command in the `tau` directory:

      ```
      grunt build
      ```

## Related Information
* Dependencies      
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
