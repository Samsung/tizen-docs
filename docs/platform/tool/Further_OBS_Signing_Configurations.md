You need additional configurations after
<https://en.opensuse.org/openSUSE:Build_Service_Signer>\

### Installing obssignd

#### Prepare gnupg

-   The mainline gnupg cannot use obs-signd.
-   You may use other standard signd (you won\'t be able to do
    per-project sign)
-   However, the author did never test with other signd.

\
\
\* You need to apply the patch from obs-sign to gnupg.

-   -   The patch is available at
        <https://github.com/openSUSE/obs-sign.git> (
        gnupg-1.4.7-files\_are\_digests.patch )
    -   Or download at
        <https://raw.githubusercontent.com/openSUSE/obs-sign/master/gnupg-1.4.7-files_are_digests.patch>

-   The patch is intended for 1.4.7, but the author used 1.4.16 (Ubuntu
    14.04) with some additional modifications.
-   Apply the patch to your gnupg source
    -   In recent gnupg, g10/sign.c requires additional changes:
        -   add \#include \"../include/host2net.h\"
        -   modify buffer\_to\_u32 to buf32\_to\_u32
-   Recompile gnupg
-   Install the modified & recompiled gnupg to your system.

\
==== Prepare obssignd ====

-   Download <https://github.com/openSUSE/obs-sign.git>
-   Do what dist/obs-signd.spec says (if your system does not use RPM).
    It\'s pretty short and straightforward.
-   Modify dist/obssignd to configure /etc/init.d/obssignd for your
    system.
    -   For example, in Ubuntu 14.04, modify the main daemon-start part
        to:
        -   start-stop-daemon \--start \--background \--no-close \--exec
            \${SN\_BIN} -p \${PID} \-- \${SN\_OPTS} \>
            \"\$logdir\"/signd.log
-   Run the \"obssignd\" daemon along with obssigner

\
=== Apply Tizen-Wide Public Key, Not Public Key per Project ===

-   Edit /usr/lib/obs/server/BSConfig.pm (The official openSUSE guide
    configures a public key per project)

:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> ······\

    our $sign = "/usr/bin/sign";
    our $sign_project = 0;
    our $keyfile = "/etc/ourkeyfile.asc";
    our $forceprojectkeys = 0;

······\
</font> \|}

-   Delete per-project public keys if they are already created

:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> ······\

    $ for X in `osc ls`; do osc signkey --delete $X; done

······\
</font> \|}

-   -   Projects published after this will use the public key configured
        as in the openSUSE official guide (/etc/ourkeyfile.asc)

\

### Verifying the Key

-   Note that MIC automatically checks the corresponding public key.
    -   It rejects creating images if the public key is not recognized.
    -   You need to import the public key in your system (\$ gpg
        \--import keyfile)

<!-- -->

-   Verifying repmod.xml (both repmod.xml and repmod.xml.asc should
    exist in the current path)
    -   \$ gpg \--verify repmod.xml.asc

<!-- -->

-   Importing the key
    -   \$ gpg \--import repmod.xml.key

[Category:Tool](Category:Tool "wikilink")
