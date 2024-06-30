AutoFDO uses sampling based profile to drive feedback directed
optimizations.

AutoFDO uses *perf* to collect sample profiles. A standalone tool is
used to convert the perf.data file into *gcov* format. GCC reads in the
gcov file and interprets the profile into a set of hashmaps. A
standalone pass is added to use the processed profile data to annotate
the basic block counts and estimate branch
probabilities.[1](https://gcc.gnu.org/wiki/AutoFDO)

The major difference between AutoFDO and FDO (aka PGO) is that AutoFDO
profiles on optimized binary instead of instrumented binary. This makes
it very different in handling cloned functions.

Applicability
-------------

Currently data collection is targeted to Intel CPUs with Last Branch
Record hardware registers.
[2](https://gcc.gnu.org/ml/gcc/2015-04/msg00250.html)

Profile created on x86 can be applied during cross ARM-build though
[3](https://gcc.gnu.org/ml/gcc/2015-04/msg00113.html) There is a
theoretical possibility to use *-use\_lbr=false* flag to record profile
on ARM device and a report that it works for linpack benchmark
[4](https://gcc.gnu.org/ml/gcc/2015-04/msg00267.html)

Also the simplest way to grab a profile is *ocperf*
[pmu-tools](https://github.com/andikleen/pmu-tools)

Usage
-----

Say we have a *test-app* benchmark, so the AutoFDO build will be the
following:

`gcc -O2 -g test-app.c -o test-app`\
`ocperf.py record -e br_inst_retired.near_taken:pp -b -o profile.data ./test-app`\
`create_gcov --binary=test-app --profile=profile.data --gcov=test-app.gcov --gcov_version=0x1`\
`gcc -O2 -g test-app.c -o test-app -fauto-profile=test-app.gcov`

[Category:Tool](Category:Tool "wikilink")
