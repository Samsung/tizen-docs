Introduction
------------

This document reveals the interface between Tizen tools backend service
and gbp.

Function Calling Procedure
--------------------------

1\. command.py calls gbp\_export().

`      def main(argv=None):`\
`              """Main function"""`\
`      ...`\
`      # Run GBP`\
`              ret = gbp_export(repo, args, config)`\
`      "obs-service-git-buildpackage1/obs_service_gbp/command.py"`

-   Note: In comparison, in GBS\'s procedure, cmd\_export.py calls
    export\_sources().

`      277     with utils.Workdir(workdir):`\
`      278         export_sources(repo, commit, export_dir, main_spec, args)`\
`      "gbs/gitbuildsys/cmd_export.py"`

2\. gbp\_export() calls fork\_call() after confirming the export target
as RPM package.

`      128         if args.rpm == 'yes' or (args.rpm == 'auto' and specs_found):`\
`      129             LOGGER.info('Exporting RPM packaging files with GBP')`\
`      130             LOGGER.debug('git-buildpackage-rpm args: %s', ' '.join(rpm_args))`\
`      131             import ipdb;ipdb.set_trace()`\
`      132             ret = fork_call(uid, gid, gbp_rpm)(rpm_args)`\
`      133             if ret:`\
`      134                 LOGGER.error('Git-buildpackage-rpm failed, unable to export '`\
`      135                              'RPM packaging files')`\
`      136                 return 2`\
`      "gbs/gitbuildsys/cmd_export.py"`

-   Note: In comparison, in GBS\'s procedure, export\_sources() directly
    calls buildpackage\_rpm.py.

`      198 def export_sources(repo, commit, export_dir, spec, args, create_tarball=True):`\
`              ...`\
`      205     gbp_args = create_gbp_export_args(repo, commit, export_dir, tmp.path,`\
`      206                                       spec, args, create_tarball=create_tarball)`\
`      207     try:`\
`      208         ret = gbp_build(gbp_args)`\
`      "gbs/gitbuildsys/cmd_export.py"`

3\. fork\_call() calls partial(), then partial() calls \_fork\_call.

`      118 def fork_call(user, group, func):`\
`      119     """Fork and call a function. The function should return an integer.`\
`      120        Returns a callable that runs the function."""`\
`      121     return partial(_fork_call, user, group, func)`\
`      "obs-service-git-buildpackage1/obs_service_gbp_utils/__init__.py"`

4\. \_fork\_call calls process().

`       99 def _fork_call(user, group, func, *args, **kwargs):`\
`               ...`\
`       104     # Run function in a child process`\
`       105     data_q = Queue()`\
`       106     import ipdb;ipdb.set_trace()`\
`       107     child = Process(target=_demoted_child_call,`\
`       108                     args=(uid, gid, data_q, partial(func, *args, **kwargs)))`\
`       ""obs-service-git-buildpackage1/obs_service_gbp_utils/__init__.py`

5\. process() calls buildpackage\_rpm().

[Category:Tool](Category:Tool "wikilink")
