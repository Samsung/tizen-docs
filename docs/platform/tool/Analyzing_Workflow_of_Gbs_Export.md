Introduction
------------

This document will introduce the basic workflow of \`gbs export\`. First
the whole structure will be shown as follow, the following sections will
analyze each section in details.

.. image:: ../../../data/images/gbs\_packaging.png

Upstream Branch Existing
------------------------

Upstream branch is the first condition to enable non-native packaging
development model, the default upstream branch is \`upstream\`, which
can be customized with the following ways:

1.Configure in gbs conf:

` [general]`\
` upstream_branch=upstream_tizen`\
` upstream_tag=upstream/${upstreamversion}`

2.Command line option: \--upstream-branch

` $ gbs export --upstream-branch=123`

### Code Analysis

` 151     if is_native_pkg(repo, args) or args.no_patch_export:`\
` 152         argv.extend(["--git-no-patch-export",`\
` 153                      "--git-upstream-tree=%s" % commit])`\
` 154     else:`\
` 155         # Check if the revision seems to be of an orphan development branch`\
` 156         is_orphan = False`\
` 157         export_commitish = 'HEAD' if commit == 'WC.UNTRACKED' else commit`\
` "gitbuildsys/cmd_export.py" 320 lines --38%--                                  `\
` --------`\
` 52     def is_native_pkg(repo, args):`\
` 53         """`\
` 54         Determine if the package is "native"`\
` 55         """`\
` 56         upstream_branch = configmgr.get_arg_conf(args, 'upstream_branch')`\
` 57         return not repo.has_branch(upstream_branch)`\
` 58 `\
` "gitbuildsys/cmd_export.py" 320 lines --18%--`

Generate Tarball from \'HEAD\'(No patch generated)
--------------------------------------------------

Not having a upstream branch in specific project git tree indicates that
the corresponding package is in a native packaging deevelopment model.
For native packages, gbs simply creates tarball from the HEAD of the
current branch, no patch generated.

### Code Analysis

1\. buildpackage\_rpm.py calls is\_native() and git\_archive().

` 619   # Get/build the orig tarball`\
` 620   if is_native(repo, options):`\
`               ...`\
` 626           if not git_archive(repo, spec, source_dir, options.tmp_dir,`\
` 627                              tree, options.orig_prefix,`\
` 628                              options.comp_level,`\
` 629                              options.with_submodules):`\
` 630               raise GbpError, "Cannot create source tarball at '%s'" % export_dir`\
` "git-buildpackage/gbp/scripts/buildpackage_rpm.py"`

2\. git\_archive() calls git\_archive\_single().

` 54 def git_archive(repo, spec, output_dir, tmpdir_b, treeish, prefix,`\
` 55                 comp_level, with_submodules):`\
`            ...`\
` 73         else:`\
` 74             git_archive_single(repo, treeish, output, prefix,`\
` 75                                spec.orig_src['compression'], comp_level, comp_opts,`\
` 76                                spec.orig_src['archive_fmt'])`\
` "git-buildpackage/gbp/scripts/buildpackage_rpm.py"`

3\. git\_archive\_single() calls archive().

` 101 def git_archive_single(repo, treeish, output, prefix, comp_type, comp_level,`\
` 102                        comp_opts, format='tar'):`\
`             ...`\
` 115         popen = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=archive_fd)`\
` 116         for chunk in repo.archive(format, prefix, None, treeish):`\
` 117             popen.stdin.write(chunk)`\
` 118         popen.stdin.close()`\
` "git-buildpackage/gbp/scripts/common/buildpackage.py"`

4\. archive() calls \_git\_inout2().

` 1837   def archive(self, format, prefix, output, treeish, paths=None):`\
`            ...`\
` 1862       if output:`\
` 1863           out, err, ret = self._git_inout('archive', args.args)`\
` 1864           if ret:`\
` 1865               raise GitRepositoryError("Unable to archive %s: %s" % (treeish,`\
` 1866                                                                      err))`\
` 1867       else:`\
` 1868           return self._git_inout2('archive', args.args)`\
` "git-buildpackage/gbp/git/repository.py"`

5\. \_git\_inout2() calls \_git\_inout().

` 194   def _git_inout2(self, command, args, stdin=None, extra_env=None, cwd=None,`\
` 195                   capture_stderr=False):`\
`           ...`\
` 207       try:`\
` 208           for outdata in self.__git_inout(command, args, stdin, extra_env,`\
` 209                                           cwd, capture_stderr, True):`\
` 210               stderr += outdata[1]`\
` 211               yield outdata[0]`\
` "git-buildpackage/gbp/git/repository.py"`

6\. \_git\_inout() executes git command:\*\*git archive \--format=tar
\--prefix=<Package_Dir>/ HEAD \--\*\*

` 217   def __git_inout(cls, command, args, stdin, extra_env, cwd, capture_stderr,`\
` 218                   capture_stdout):`\
`           ...`\
` 232       cmd = ['git', command] + args`\
` 233       env = cls.__build_env(extra_env)`\
` "git-buildpackage/gbp/git/repository.py"`

7\. Compress command (gzip, bzip2) takes the output of \`git archive\` as
input to generate compressed files by using pipe technology.

` 101 def git_archive_single(repo, treeish, output, prefix, comp_type, comp_level,`\
` 102                        comp_opts, format='tar'):`\
`                ...`\
` 108     prefix = sanitize_prefix(prefix)`\
` 109     with open(output, 'w') as archive_fd:`\
` 110         if comp_type:`\
` 111             cmd = [comp_type, '--stdout', '-%s' % comp_level] + comp_opts`\
` 112         else:`\
` 113             cmd = ['cat']`\
` 114`\
` 115    popen = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=archive_fd)`

` This is equivalent to the following command when the comp_type is tar.bz2: `\
` git archive --format=tar --prefix=`<Package_Dir>`/ HEAD -- | bzip2 --stdout -6 > fake-0.1.tar.bz2`

HEAD and Upstream Branch has Common Ancestor
--------------------------------------------

If current HEAD and upstream branch have common ancestor, this is the
joint-packaging development model, the next step is to check tag exists
or not. Else if current HEAD and upstream branch don\'t have common
ancestor, gbs will regards current branch as orphan-packaging branch,
this means your are in orphan-packaging development model, the next step
is to copy packaging files from packaging branch during gbs generates
tarball.

Upstream Tag Exists
-------------------

In joint-packageing model,If there is upstream branch, gbs will generate
patches first, during this period, the upstream tag is the most
importand role, individual patches (one per commit) are generated from
the upstream tag to the exported revision. So if no related upstream
tag, gbs will displays the error message and exit.

Whether the tag exist or not will result two consequences:

-   If yes, gbs will check whether tag is the ancester of current HEAD.
-   If no, gbs will exist abnormally with error message:\*\*Invalid
    upstream treeish <Tag>\*\*.

### Code Analysis

1\. buildpackage\_rpm.py calls export\_patches().

` 580  if options.patch_export and not is_native(repo, options):`\
` 581      if options.patch_export_rev:`\
` 582          patch_tree = get_tree(repo, options.patch_export_rev)`\
` 583      else:`\
` 584          patch_tree = tree`\
` 585      export_patches(repo, spec, patch_tree, options)`\
` "git-buildpackage/gbp/scripts/buildpackage_rpm.py"`

2\. export\_patches calls get\_upstream\_tree().

` 296 def export_patches(repo, spec, export_treeish, options):`\
`      ...`\
` 300     try:`\
` 301         upstream_tree = get_upstream_tree(repo, spec, options)`\
` 302         update_patch_series(repo, spec, upstream_tree, export_treeish, options)`\
` "git-buildpackage/gbp/scripts/buildpackage_rpm.py"`

3\. get\_upstream\_tree() calls has\_treeish().

` 157 def get get_upstream_tree():`\
`         ...`\
` 169     if not repo.has_treeish(upstream_tree):`\
` 170         raise GbpError('Invalid upstream treeish %s' % upstream_tree)`\
` 171     return upstream_tree`\
` "git-buildpackage/gbp/scripts/buildpackage_rpm.py"`

4\. has\_treeish() calls \_git\_inout().

` 1019   def has_treeish(self, treeish):`\
`            ...`\
` 1028       _out, _err, ret =  self._git_inout('ls-tree', [treeish],`\
` 1029                                          capture_stderr=True)`\
` 1030       return [ True, False ][ret != 0]`\
` "git-buildpackage/gbp/git/repository"`

5\. \_git\_inout() calls its \_git\_inout() class method.

` 161   def _git_inout(self, command, args, input=None, extra_env=None, cwd=None,`\
` 162                  capture_stderr=False, capture_stdout=True):`\
`           ...`\
` 184       try:`\
` 185           for outdata in self.__git_inout(command, args, input, extra_env,`\
` 186                                           cwd, capture_stderr,`\
` 187                                           capture_stdout):`\
` 188               stdout += outdata[0]`\
` 189               stderr += outdata[1]`\
` "git-buildpackage/gbp/git/repository"`

6\. \_git\_inout() class method executes the git command: \*\*git ls-tree
<Tag>\*\*.

` 216   @classmethod`\
` 217   def __git_inout(cls, command, args, stdin, extra_env, cwd, capture_stderr,`\
` 218                   capture_stdout):`\
`           ...`\
` 232       cmd = ['git', command] + args`\
` 233       env = cls.__build_env(extra_env)`\
` 234       stdout_arg = subprocess.PIPE if capture_stdout else None`\
` 235       stdin_arg = subprocess.PIPE if stdin else None`\
` 236       stderr_arg = subprocess.PIPE if capture_stderr else None`\
` "git-buildpackage/gbp/git/repository"`

Upstream Tag is Ancestor of Current HEAD
----------------------------------------

GBS uses tag as the boundary of tarball creation and patch generation,
that is, tag and all its ancestors will be included in tarball, whereas
every child of tag will be generated as a patch, hence, upstream tag
must be reachable for the current HEAD and tag must be ancestor of HEAD.

And there are two consequences about this topic:

-   If ancestor of HEAD, gbs will generate patches from upstream tag to
    current \`HEAD\`.
-   If not, gbs will exist abnormally with error message: \*\*Start
    commit \'<tag>\' not an ancestor of end commit \'HEAD\'\*\*

### Three Incorrect Cases

Here we graphical three incorrect cases, what we need pay attentions are
the relations among upstream branch, current HEAD and position of the
tag.

:   

    :   images:

-   For case one, tag is on upstream branch, but tag isn\'t the ancestor
    of the current HEAD, the HEAD to the tag is unreachable. For
    details, see \"merge\_base = repo.get\_merge\_base(parent\_sha1,
    child\_sha1)\" in step-05.

<!-- -->

-   For case two, upstream branch and current branch don\'t have any
    intersection, in this case, current HEAD and tag are unreachable.
    For details, see \"merge\_base = repo.get\_merge\_base(parent\_sha1,
    child\_sha1)\" in step-05.

<!-- -->

-   For case three, current HEAD and tag is reachable, but tag is not
    the ancestor of current HEAD. For details, see \"return merge\_base
    == parent\_sha1\" in step-05.

### Code Analysis

1\. buildpackage\_rpm.py calls export\_patches().

` 579  # Generate patches, if requested`\
` 580  if options.patch_export and not is_native(repo, options):`\
` 581      if options.patch_export_rev:`\
` 582          patch_tree = get_tree(repo, options.patch_export_rev)`\
` 583      else:`\
` 584          patch_tree = tree`\
` 585      export_patches(repo, spec, patch_tree, options)`\
` "/home/rui/projects/git-buildpackage/gbp/scripts/buildpackage_rpm.py"`

2\. export\_patches() calls update\_patch\_series().

` 258 def export_patches(repo, options):`\
`         ...`\
` 274     update_patch_series(repo, spec, upstream_commit, export_treeish, options)`\
` "git-buildpackage/gbp/scripts/buildpackage_rpm.py"`

3\. update\_patch\_series() calls generate\_patches().

` 198 def update_patch_series(repo, spec, start, end, options):`\
`         ...`\
` 211     patches, commands = generate_patches(repo, start, squash, end,`\
` 212                                          spec.specdir, options)`\
` "git-buildpackage/gbp/scripts/pq_rpm.py"`

4\. generate\_patches() calls is\_ancestor().

` 91 def generate_patches(repo, start, squash, end, outdir, options):`\
`         ...`\
` 115     if not is_ancestor(repo, start_sha1, end_commit_sha1):`\
` 116         raise GbpError("Start commit '%s' not an ancestor of end commit "`\
` 117                        "'%s'" % (start, end_commit))`\
` "git-buildpackage/gbp/scripts/pq_rpm.py"`

5\. is\_ancestor() calls repo.get\_merge\_base(): \*\*git merge-base HEAD
upstream\*\*

` 81 def is_ancestor(repo, parent, child):`\
` 82     """Check if commit is ancestor of another"""`\
` 83     parent_sha1 = repo.rev_parse("%s^0" % parent)`\
` 84     child_sha1 = repo.rev_parse("%s^0" % child)`\
` 85     try:`\
` 86         merge_base = repo.get_merge_base(parent_sha1, child_sha1)`\
` 87     except GitRepositoryError:`\
` 88         merge_base = None`\
` 89     return merge_base == parent_sha1`\
` 90`\
` "git-buildpackage/gbp/scripts/pq_rpm.py"`

Generate Patches from Upstream Tag to HEAD
------------------------------------------

In joint-packaging development model, after checking the upstream tag,
next is generate patches from upstream tag to the HEAD.

### Code Analysis

1.With the gbp parameters about patches are transfered to gbp code, the
function \`export\_patches(repo, spec, export\_treeish, options)\` is
called for patches generation.

` 294 def export_patches(repo, spec, export_treeish, options):`\
` 295     """`\
` 296     Generate patches and update spec file`\
` 297     """`\
` 298     try:`\
` 299         upstream_tree = get_upstream_tree(repo, spec, options)`\
` 300         update_patch_series(repo, spec, upstream_tree, export_treeish, options)`\
` 301     except (GitRepositoryError, GbpError) as err:`\
` 302         raise GbpAutoGenerateError(str(err))`

2.In function \`update\_patch\_series\`, it calles
\`generate\_patches\`. And the function \`format\_patch\` is key for
patches\' generation.

` 91 def generate_patches(repo, start, squash, end, outdir, options):`\
`         ...`\
` 153     for commit in reversed(repo.get_commits(start, end_commit)):`\
` 154         info = repo.get_commit_info(commit)`\
` 155         cmds = parse_gbp_commands(info, 'gbp-rpm', ('ignore'),`\
` 156                                   ('if', 'ifarch'))[0]`\
` 157         if not 'ignore' in cmds:`\
` 158             patch_fn = format_patch(outdir, repo, info, patches,`\
` 159                                     options.patch_numbers,`\
` 160                                     options.patch_export_ignore_path)`\
` 161             if patch_fn:`\
` 162                 commands[os.path.basename(patch_fn)] = cmds`\
` "git-buildpackage/gbp/scripts/pq_rpm.py"`

3.We can see that patches\' generation including two steps, first is get
code diff in git tree by git command, second is write code diff to a
file which endwith .patch, this file is the patch we want.

` Git command to get code diff, we take project platform/upstream/js as an example:`\
` git diff -p --no-ext-diff --stat=80 --summary --text --ignore-submodules`\
` db4843164340e965dc0e6168dbb59b3e795e511c^! -- js/src/  configure js/src/configure.in`

` 237 def format_patch(outdir, repo, commit_info, series, numbered=True,`\
` 238                  path_exclude_regex=None, topic=''):`\
` 260     ...`\
` 261     # Finally, create the patch`\
` 262     patch = None`\
` 263     if paths:`\
` 264         diff = repo.diff('%s^!' % commit_info['id'], paths=paths, stat=80,`\
` 265                          summary=True, text=True)`\
` 266         patch = write_patch_file(filepath, commit_info, diff)`\
` "git-buildpackage/gbp/scripts/common/pq.py"`

4.This function achieves execute git command with subprocess.Popen.

` 217    def __git_inout(cls, command, args, stdin, extra_env, cwd, capture_stderr,`\
` 218                    capture_stdout):`\
` 231`\
` 232        cmd = ['git', command] + args`\
` 239        popen = subprocess.Popen(cmd,`\
` 240                                 stdin=stdin_arg,`\
` 241                                 stdout=stdout_arg,`\
` 242                                 stderr=stderr_arg,`\
` 243                                 env=env,`\
` 244                                 close_fds=True,`\
` 245                                 cwd=cwd)`\
` "git-buildpackage/gbp/git/repository.py"  `

5.After patches are generated, macro defines about patches will be added
in specfile.

` 197 def update_patch_series(repo, spec, start, end, options):`\
`         ...`\
` 212     spec.update_patches(patches, commands)`\
` 213     spec.write_spec_file()`\
` "git-buildpackage/gbp/scripts/pq_rpm.py"`

6.Addition

-   With the subcommand :\*\*\--squash-patches-until\*\*. Gbs will
    squash commits(from upstream) up to certain tree-ish into one
    monolithic diff. Diff file also including two steps, first is get
    code diff with git command, second is wirte code diff into a file
    which endwith .diff, this diff file is the final file generated with
    subcommand \`\--squash-patches-until\`.

`  91 def generate_patches(repo, start, squash, end, outdir, options):  `\
`          ...`\
`  117     # Squash commits, if requested`\
`  126             # Shorten SHA1s`\
`  127             squash_sha1 = repo.rev_parse(squash_sha1, short=7)`\
`  128             start_sha1 = repo.rev_parse(start_sha1, short=7)`\
`  129             gbp.log.info("Squashing commits %s..%s into one monolithic diff" %`\
`  130                          (start_sha1, squash_sha1))`\
`  131             patch_fn = format_diff(outdir, squash[1], repo,`\
`  132                                    start_sha1, squash_sha1,`\
`  133                                    options.patch_export_ignore_path)`\
`  "git-buildpackage/gbp/scripts/pq_rpm.py"`\
`  -----------------`\
`  272 def format_diff(outdir, filename, repo, start, end, path_exclude_regex=None):`\
`  288     if paths:`\
`  289         diff = repo.diff(start, end, paths=paths, stat=80, summary=True,`\
`  290                          text=True)`\
`  291         return write_patch_file(filename, info, diff)`\
`  "git-buildpackage/gbp/scripts/common/pq.py"`

-   The last merge commit are squashed into one diff if \"Merge\"
    commits are found in the revision list, from which patches are to be
    generated. Diff file generation is the same as \`With the subcommand
    : \--squash-patches-until\` part.

`  91 def generate_patches(repo, start, squash, end, outdir, options):`\
`          ...`\
`  137     # Check for merge commits, yet another squash if merges found`\
`  138     merges = repo.get_commits(start, end_commit, options=['--merges'])`\
`  139     if merges:`\
`  140         # Shorten SHA1s`\
`  141         start_sha1 = repo.rev_parse(start, short=7)`\
`  142         merge_sha1 = repo.rev_parse(merges[0], short=7)`\
`  143         patch_fn = format_diff(outdir, None, repo, start_sha1, merge_sha1,`\
`  144                                options.patch_export_ignore_path)`\
`  145         if patch_fn:`\
`  146             gbp.log.info("Merge commits found! Diff between %s..%s written "`\
`  147                          "into one monolithic diff" % (start_sha1, merge_sha1))`\
`  "git-buildpackage/gbp/scripts/pq_rpm.py"`\
`  -----------------`\
`  272 def format_diff(outdir, filename, repo, start, end, path_exclude_regex=None):`\
`  288     if paths:`\
`  289         diff = repo.diff(start, end, paths=paths, stat=80, summary=True,`\
`  290                          text=True)`\
`  291         return write_patch_file(filename, info, diff)`\
`  "git-buildpackage/gbp/scripts/common/pq.py"`

Copy Packaging Files from HEAD
------------------------------

In joint-packaging model, gbs will copy packaging files from current
HEAD to the target export directory. After copying packaging files, the
next step is generate tarball from pristine-tar branch.

### Code Analysis

1.Specdir is packaging dir, code bellow achieves copy all pkgfiles under
packaging dir to export\_dir, export\_dir\'s creation is under /var/tmp/
dir temporary.

` 591     # Move packaging files`\
` 592     gbp.log.debug("Exporting packaging files in '%s' to '%s'" % (spec.specdir, export_dir))`\
` 593     pkgfiles = os.listdir(spec.specdir)`\
` 594     for f in pkgfiles:`\
` 595         src = os.path.join(spec.specdir, f)`\
` 596         if f == spec.specfile:`\
` 597             dst = os.path.join(spec_dir, f)`\
` 598         else:`\
` 599             dst = os.path.join(source_dir, f)`\
` 600         try:`\
` 601             if os.path.isdir(src):`\
` 602                 # dir is not packaging files, skip it`\
` 603                 continue`\
` 604             else:`\
` 605                 shutil.copy2(src, dst)`\
` 606         except IOError, err:`\
` 607             raise GbpError, "Error exporting files: %s" % err`\
` "git-buildpackage/gbp/scripts/buildpackage_rpm.py"`

2.After gbs finish copying packaging files and generating tarball(see
the next two parts), gbs will move files under export\_dir to dest
source git tree.

` 314     shutil.move(export_dir, outdir)`\
` "gbs/gitbuildsys/cmd_export.py"`

Pristine-tar Branch Exists and Checkout Tarball
-----------------------------------------------

For tarball\'s generation, gbs will check pristine-tar branch exists or
not, if pristine-tar branch exists and also contain the tarball with
correct version, gbs will generation from pristine-tar directly.But even
with correct version, tarball generation from pristine-tar would failed
sometimes,not to mention no corrent tarball in that branch, in this
case, gbs will generate tarball using upstream tag.

### Code Analysis

1.Code analysis bellow, if current git tree is non-native development
model, the function \`prepare\_upstream\_tarball(repo, spec, options,
source\_dir)\` will be called for generating tarball.

` 631    elif spec.orig_src:`\
` 632         prepare_upstream_tarball(repo, spec, options, source_dir)`\
` "git-buildpackage/gbp/scripts/buildpackage_rpm.py"`

2.The function bellow shows gbs will check pristine-tar branch first, if
there is pristine-tar branch in git tree, gbs will checkout tarball from
there by calling the function \`pristine\_tar\_build\_orig(repo,
orig\_file, output\_dir, options)\`.

` 91 def prepare_upstream_tarball(repo, spec, options, output_dir):`\
` 103`\
` 104     # build an orig unless the user forbids it, always build (and overwrite pre-existing) if user forces it`\
` 105     if options.force_create or (not options.no_create_orig and not RpmPkgPolicy.has_orig(orig_file, output_dir)):`\
` 106         if not pristine_tar_build_orig(repo, orig_file, output_dir, options):`\
` 107             upstream_tree = git_archive_build_orig(repo, spec, output_dir, options)`\
` "git-buildpackage/gbp/scripts/buildpackage_rpm.py"`\

3.Check pristine-tar branch exists or not:

` Check branch command : **git show-ref refs/heads/pristine-tar**`

` 137 def pristine_tar_build_orig(repo, orig_file, output_dir, options):`\
`         ...`\
` 142     if options.pristine_tar:`\
` 143         if not repo.has_branch(repo.pristine_tar_branch):`\
` 144             gbp.log.warn('Pristine-tar branch "%s" not found' %`\
` 145                          repo.pristine_tar.branch)`\
` "git-buildpackage/gbp/scripts/buildpackage_rpm.py"`\
` -----------------`\
` 448     def has_branch(self, branch, remote=False):`\
` 458         if remote:`\
` 459             ref = 'refs/remotes/%s' % branch`\
` 460         else:`\
` 461             ref = 'refs/heads/%s' % branch`\
` 462         try:`\
` 463             self._git_command('show-ref', [ ref ])`\
` "git-buildpackage/gbp/git/repository.py"`

4.For example, we take generate tarball js185-1.0.0.tar.bz2 from
pristine-tar branchas an example, the final function to execute cmd by
subprocess.Popen is \`\_\_call(self, args)\`, let\'s see the code
segment bellow:

` Checkout tarball command : **/usr/bin/pristine-tar checkout /var/tmp/.gbs_export_pTzq29/js185-1.0.0.tar.bz2**`

` 137 def pristine_tar_build_orig(repo, orig_file, output_dir, options):`\
`             ...`\
` 146         try:`\
` 147             repo.pristine_tar.checkout(os.path.join(output_dir, orig_file))`\
` 148             return True`\
` 149         except CommandExecFailed:`\
`                     ...`\
` 155                 raise`\
` 156     return False`\
` "git-buildpackage/gbp/scripts/buildpackage_rpm.py"`\
` -----------------`\
` 55    def __call(self, args):`\
` 66`\
` 67        cmd = [ self.cmd ] + self.args + args`\
` 68        if self.shell:`\
` 70            cmd = " ".join(cmd)`\
` 71        popen = subprocess.Popen(cmd,`\
` 72                                 cwd=self.cwd,`\
` 73                                 shell=self.shell,`\
` 74                                 env=self.env,`\
` 75                                 preexec_fn=default_sigpipe,`\
` 76                                 stderr=stderr_arg)`\
` "git-buildpackage/gbp/command_wrappers.py"`

Generate Tarall Using Upstream Tag
----------------------------------

If no pristine-tar branch or no correct tarball in pristine-tar branch
or generate tarball failed, gbs will generate tarball using upstream
tag.

### Code Analysis

1.Tarball\'s generation is by calling the function
\`git\_archive\_build\_orig(repo, spec, output\_dir, options)\`

` 91 def prepare_upstream_tarball(repo, spec, options, output_dir):`\
` 103`\
` 107             upstream_tree = git_archive_build_orig(repo, spec, output_dir, options)`\
` ""`

2.Let us suppose tarball js185-1.0.0.tar.bz2 checkout from pristine-tar
failed, we will generate it with the upstream tag, take this as an
example:

``  The final function to execute cmd by subprocess.Popen is `__git_inout`: ``\
` Archive tarball command: **git archive --format=tar --prefix=js-1.0.0/ upstream/1.0.0 -- | bzip2 --stdout -6 > js185-1.0.0.tar.bz2**`

` 262 def git_archive_build_orig(repo, spec, output_dir, options):`\
` 285         if not git_archive(repo, spec, output_dir, options.tmp_dir,`\
` 286                            upstream_tree, options.orig_prefix,`\
` 287                            options.comp_level, options.with_submodules):`\
` "git-buildpackage/gbp/scripts/buildpackage_rpm.py"`\
` -----------------`\
` 217def __git_inout(cls, command, args, stdin, extra_env, cwd, capture_stderr,`\
` 218                capture_stdout):`\
` 231    ...`\
` 232    cmd = ['git', command] + args`\
` 239    popen = subprocess.Popen(cmd,`\
` 240                             stdin=stdin_arg,`\
` 241                             stdout=stdout_arg,`\
` 242                             stderr=stderr_arg,`\
` 243                             env=env,`\
` 244                             close_fds=True,`\
` 245                             cwd=cwd)`\
` "git-buildpackage/gbp/git/repository.py"`

Update Spec Files (Adding VCS tag)
----------------------------------

After gbs generates tarball successfuly, the final step is update spec
file with adding VCS tag.

### Code Analysis

` 673                 Command(options.posttag, shell=True,`\
` 674                         extra_env={'GBP_TAG': tag,`\
` 675                                    'GBP_BRANCH': branch,`\
` 676                                    'GBP_SHA1': sha})()`\
` 677         else:`\
` 678             vcs_info = get_vcs_info(repo, tree)`\
` 679         # Put 'VCS:' tag to .spec`\
` 680         spec.set_tag('VCS', None, options.spec_vcs_tag % vcs_info)`\
` 681         spec.write_spec_file()`\
` 682 `\
` 683     except CommandExecFailed:`\
` "gbp/scripts/buildpackage_rpm.py"`

Orphan\_packaging Branch Exist
------------------------------

If you get the result that current HEAD and upstream branch don\'t have
common ancestor, this means you\'ve been on orphan packaging branch
already. Gbs export wouldn\'t generate patches on orphan packaging
branch, because gbp parameters about generate patches won\'t be
transfered to gbp code.

The parameters such as:\"\--git-patch-export\",
\"\--git-patch-export-compress=100k\",
\"\--git-patch-export-squash-until=%s\",
\"\--git-patch-export-ignore-path=\^(%s/.\*\|.gbs.conf)\".

Check whether you are on orphan packaging branch in orphan-packaging
model, follow the code segment bellow:

### Code Analysis

1.The result of final command \*\*git merge-base HEAD upstream\*\*
called by function \`repo.get\_merge\_base(export\_commitish,
upstream\_branch)\` will affect the bool value of is\_orhpan, if
\`is\_orphan = True\` means you are on orphan-packaging branch, let\'s
see the gbp parameters about patches handled for this branch by the
second code segment.

` 156    is_orphan = False`\
` 157    export_commitish = 'HEAD' if commit == 'WC.UNTRACKED' else commit`\
` 158    try:`\
` 159        repo.get_merge_base(export_commitish, upstream_branch)`\
` 160    except GitRepositoryError:`\
` 161        is_orphan = True`\
` 162`\
` "gbs/gitbuildsys/cmd_export.py"`

2.This code segment shows if the current branch you are on isn\'t the
orphan-packaging branch, the gbp parameters about patches will be
transfered to gbp code by adding them in argv. On the opposite,if on the
orphan-packaging branch, these parameters won\'t be added in argv, also
won\'t be transfered to gbp code.So no patches would be generated
finally.

` 165    if not is_orphan:`\
` 166        argv.extend(["--git-patch-export",`\
` 167                     "--git-patch-export-compress=100k",`\
` 168                     "--git-patch-export-squash-until=%s" %`\
` 169                        squash_patches_until,`\
` 170                     "--git-patch-export-ignore-path=^(%s/.*|.gbs.conf)" %`\
` 171                        packaging_dir,`\
` 172                    ])`\
` "gbs/gitbuildsys/cmd_export.py"`

Copy Packaging Files from Packaging Branch
------------------------------------------

In orphan-packaging develoment model, during gbs export period on
orphan-packaging branch, without patch generate action, the first step
is copy packaging files from the packaging branch to the target export
directory.

Code segment is the same as \`Copy Packaging files from HEAD\` part.

Generate Tarball in Orphan Packaging Model
------------------------------------------

In orphan-packaging model,on orphan-packaging branch,when developers
export the package gbs will verify the pristine-tar branch first, if
pristine-tar branch is available, tarball will be generated from there;
else gbs will generate tarball from upstream branch.

The tarball generation procedure is the same as joint-packaging
development model,

Verify pristine-tar and checkout tarball from there please refer to
\`Pristine-tar Branch Exists and Checkout Tarball\` part.

Generate tarball with upstream tag please refer to \`Generate Tarall
Using Upstream Tag\` part.

[Category:Tool](Category:Tool "wikilink")
