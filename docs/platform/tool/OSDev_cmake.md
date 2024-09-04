CMake has been updated in Tizen 5 to
[3.9](https://cmake.org/cmake/help/v3.9/) (previous: 2.8.x), and some
policies were updated.

If your CMake-based application build fails for Tizen 5.5 please check
build log for CMake warning messages. It\'s better to rewrite script for
new version of CMake, but as a temporary solution you might try to use

`CMAKE_POLICY(SET CMPXXXX OLD)`

Where XXXX is policy number and restore old behavior. This is not very
reliable, but might work.

Most interesting policies with behavior changes
-----------------------------------------------

-   [CMP0046](https://cmake.org/cmake/help/v3.0/policy/CMP0046.html):
    Error on non-existent dependency in add\_dependencies. This may
    break code with non-existent dependencies.
-   [CMP0053](https://cmake.org/cmake/help/v3.1/policy/CMP0053.html):
    Simplify variable reference and escape sequence evaluation. This may
    break existing code with variables (e.g. some dependency-tracking
    scripts)
-   [CMP0054](https://cmake.org/cmake/help/v3.1/policy/CMP0053.html):
    Only interpret if() arguments as variables or keywords when
    unquoted. This may break some old-style if() blocks

[Category:Tool](Category:Tool "wikilink")
