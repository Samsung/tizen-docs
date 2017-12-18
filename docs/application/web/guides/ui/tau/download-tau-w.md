# Downloading TAU

## Dependencies

- Tizen 2.4 and Higher for Mobile
- Tizen 2.3.1 and Higher for Wearable

Tizen provides 2 versions of the TAU library: an uncompressed version for development and a minified version for production. The development version includes extra warnings about common mistakes, whereas the production version includes extra performance optimizations and strips all error messages.

This feature is supported in mobile and wearable applications only.

To download and build TAU from Git:

> **Note**
> To build the TAU library, make sure that you have both Git and `Node.js` installed.

1. Download the Git repository:

   1. Clone a copy of the master TAU Git repository:

      ```
      git clone git://review.tizen.org/platform/framework/web/tau.git
      ```

   2. Change to the TAU directory:

      ```
      cd tau
      ```

   3. Check out and build a specific version of TAU:

      ```
      git checkout 0.x-stable
      ```

2. Build TAU:

   1. Install the build module by npm:

      ```
      npm install
      ```

   2. Test that you have grunt installed:

      ```
      grunt -V
      ```

   3. Build TAU by running the following command in the `tau` directory:

      ```
      grunt build
      ```