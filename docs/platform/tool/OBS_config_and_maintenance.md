OBS of otctools is used for packages building. For supported targets,
there are local sets of packages stored, to reduce dependency on remote
build systems in case of networking issues, and in case when remote
repositories or mirrors decide to delete files or stop carrying some
distributions. The local repositories are kept as projects named
Target:Distribution:Version.

Creating a local Target repository
----------------------------------

Common:

\- create a OBS project named Targets:DISTRO:VERSION

\- copy project config from build.opensuse.org corresponding project and
save

\- Fedora note: add variable in project config \"Macros:\" section (near
end), it has been in older releases

but for some reason has been removed later, but some otctools packages
(at least bmap-tools) depend on it for naming packages

` Macros:`\
` %opensuse_bs 1`

\- create targets in Meta:

` `<repository name="standard">\
`   `<arch>`x86_64`</arch>\
`   `<arch>`i586`</arch>\
` `</repository>

Copy binary packages corresponding to release set, without updates. This
is distro-specific.

` Create /srv/obs/build/Targets:DISTRO:VERSION/standard/ARCH/:full/`\
` Resulting set of packages for ARCH needs to be copied to :full/ directory,`

### Ubuntu, Debian style:

For Ubuntu, there is helper script import-repo.py which parses Packages
list file and copies .deb files from pool.

    #!/usr/bin/env python

    # import-repo.py oneiric
    import sys
    import os
    import urllib
    import urllib2
    import bz2

    mirror_url_base='http://linux-ftp.jf.intel.com/pub/mirrors/'
    mirror_prefix='/srv/mirror/pub/mirrors/ubuntu/'
    repos=['main/','universe/']

    def main(distro, ver, arch):
        mirror_url=mirror_url_base + str(distro)
        cur_path=os.getcwd()
        dest=cur_path+r'/cache/'+ver
    #    if os.path.exists(dest) == False: 
    #        os.makedirs(dest)

        #prepare the director to put the binary.
    #    tdest=dest+r'/'+arch
    #    if os.path.exists(tdest) == False: 
    #        os.mkdir(tdest)

        #get the package list of dist
        for repo in repos:
            tpath=r'/dists/'+str(ver)+r'/'+repo+arch+r'/Packages.bz2'
            pkgs_url=mirror_url+tpath
            dest=cur_path+tpath
            if os.path.exists(dest):
                continue
            tpath=os.path.split(dest)[0]
            if os.path.exists(tpath) == False: 
                os.makedirs(tpath)
            urllib.urlretrieve(pkgs_url,dest)
                
        dest_path=cur_path+r'/cache/'+str(ver)+r'/'+arch
        dest_name=''
        for repo in repos:
            list_file=cur_path+r'/dists/'+str(ver)+r'/'+repo+arch+r'/Packages.bz2'
    #        print 'list file is %s' % list_file
            f=bz2.BZ2File(list_file)
            for line in f:
                words = line.split()
                if len(words) == 2 and words[0] == 'Filename:':
                    dest_name = words[1]
                    file_name= r'./' + str(repo) + os.path.basename(dest_name)
                    file_url =  mirror_url + r'/' + dest_name
                    print 'cp %s%s %s' % (mirror_prefix, dest_name,file_name)
    #                print '%s' % (dest_name)
    #                print 'get %s' % (file_url)
    #                urllib.urlretrieve(file_url, file_name)
            f.close()

        return

    if __name__=='__main__':
        if len(sys.argv) != 4:
            print 'wrong calling'
    #for arch in ['binary-amd64', 'binary-i386']:
            print "example: import-repo.py ubuntu oneiric binary-i386"
        main(sys.argv[1], sys.argv[2], sys.argv[3])
      

` Most convenient place for running this is on linux-ftp server, or some other`\
` host which has copy of original repositories. It is of course possible to`\
` use version of this script which copies Package list and packages from network.`

### RPM-style distro: example based on openSUSE 12.3

\- Copy all i586.rpm files from release:
distribution/12.3/repo/oss/suse/i586 to i568/:full directory

\- Copy all x86\_64.rpm files from release:
distribution/12.3/repo/oss/suse/x86\_64 to x86\_64/:full directory

\- Copy all noarch.rpm files from release:
distribution/12.3/repo/oss/suse/noarch to x86\_64/:full directory

\- link (hard of sym link) all noarch.rpm files so that they are also
present in i586/:full/

### RPM-style distro: example based on Fedora 20

\- Copy all i586.rpm files from release repo: to i568/:full directory

` cd /srv/obs/build/Targets:Fedora:20/standard/i586/:full`\
` rsync -av linux-ftp:/srv/mirror/pub/mirrors/fedora/linux/releases/20/Fedora/i386/os/Packages/?/* .`\
` # may need few steps here because rsync complians "arg list too long, split using [0-9] [a-l] [m-p] [q-z]`\
` rsync -av linux-ftp:/srv/mirror/pub/mirrors/fedora/linux/releases/20/Everything/i386/os/Packages/?/* .`

\- Copy all x86\_64.rpm files from release repo:to x86\_64/:full
directory

` cd /srv/obs/build/Targets:Fedora:20/standard/x86_64/:full`\
` rsync -av linux-ftp:/srv/mirror/pub/mirrors/fedora/linux/releases/20/Fedora/x86_64/os/Packages/?/* .`\
` # may need few steps here because rsync complians "arg list too long, split using [0-9] [a-l] [m-p] [q-z]`\
` rsync -av linux-ftp:/srv/mirror/pub/mirrors/fedora/linux/releases/20/Everything/x86_64/os/Packages/?/* .`

Common:

\- Set all files in local target repos in :full/ owned by obsrun.obsrun

` cd /srv/obs/build/Targets:DISTRO:VER/standard/ARCH/`\
` chown -R obsrun.obsrun :full`

\- Trigger re-scan of Target dir (example for openSUSE 12.3):

` obs_admin --rescan-repository Targets:openSUSE:12.3 standard x86_64`\
` obs_admin --rescan-repository Targets:openSUSE:12.3 standard i586`

Similar re-trigger is needed when contents of :full gets changed

[Category:Tool](Category:Tool "wikilink")
