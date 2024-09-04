###  <big>***Before starting OBS installation***</big>

#### Let\'s become a super user

:   \$ sudo su

\

#### Check \"name resolution\" of \'hostname\'

-   Each hostname (e.g. \"build.pilot.tizen.org\") must be saved in the
    **/etc/HOSTNAME** file like as follows.

:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> build.pilot.tizen.org\
</font> \|}

-   All hostnames must be saved in the **/etc/hosts** file like as
    follows.

:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> ······\

    # OBS Server(s)
    192.168.0.2 build.pilot.tizen.org build frontend front fe api webui
    192.168.0.3 backend.pilot.tizen.org backend be rep
    192.168.0.4 storage.pilot.tizen.org storage src db

······\
</font> \|}

-   **NO\_PROXY** should be configured with hostnames like as follows
    <font color=blue>if it should be used</font>.

:   \# vi /etc/sysconfig/proxy
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> NO\_PROXY=\"localhost,
127.0.0.1<font color=red>, pilot.tizen.org, build, frontend, front, fe,
api, webui, backend, be, rep, storage, src, db</font>\"\
</font> \|}

:   \# vi /root/.curlrc
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> \--proxy \"http://192.168.0.1:8080\"\
<font color=red> \--noproxy \"localhost, 127.0.0.1, pilot.tizen.org,
build, frontend, front, fe, api, webui, backend, be, rep, storage, src,
db\" </font> </font> \|}\

#### If FQDN is not available (i.e. if only short hostnames are available),

-   Comment out all \"**search**\" statements like as follows.

:   \# vi /etc/resolv.conf
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> ······\
<font color=red>\#</font>search xyz.com\
······\
</font> \|}

-   Change \"**NETCONFIG\_DNS\_POLICY**\" like as follows.

:   \# vi /etc/sysconfig/network/config
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> ······\
<font color=red>\#</font>NETCONFIG\_DNS\_POLICY=\"auto\"\
NETCONFIG\_DNS\_POLICY=\"\"\
······\
</font> \|}\

------------------------------------------------------------------------

### <big>**\'\'Install and Configure OBS**\'\'</big>

The Open Build Service (OBS) consists of servers and workers.\
All OBS servers can be installed either in one computer (**all-in-one
server**) or throughout several computers (**distributed servers**).\
It is recommended for OBS workers to be installed on different computers
from the computers in which OBS servers are installed.\
\

#### OBS 2.4 Installation on openSUSE 12.3

-   [Zypper Repositories](OBS_2.4_Zypper_Repositories "wikilink")
-   [All-in-One Server + Workers](OBS_2.4_All-in-One_Server "wikilink")
-   [Distributed Servers +
    Workers](OBS_2.4_Distributed_Servers "wikilink")

\

#### OBS 2.5 Installation on openSUSE 13.1

-   [Zypper Repositories](OBS_2.5_Zypper_Repositories "wikilink")
-   [All-in-One Server + Workers](OBS_2.5_All-in-One_Server "wikilink")
-   [Distributed Servers +
    Workers](OBS_2.5_Distributed_Servers "wikilink")

\

#### Public Key Signing with OBS

-   Start signing infra:
    <https://en.opensuse.org/openSUSE:Build_Service_Signer>
-   [Further OBS Signing
    Configurations](Further_OBS_Signing_Configurations "wikilink")

\

------------------------------------------------------------------------

=== <big>***Troubleshooting***</big> === <big>***(How to solve issues
during OBS installation)***</big>\
\

#### Firewall setting fails

  **CAUSE**: ***/etc/services*** file had been deleted.

:   \# SuSEfirewall2
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> SuSEfirewall2: Setting up rules from
/etc/sysconfig/SuSEfirewall2 \...\
SuSEfirewall2: using default zone \'ext\' for interface eno1\
SuSEfirewall2: using default zone \'ext\' for interface eno2\
SuSEfirewall2: using default zone \'ext\' for interface eno3\
SuSEfirewall2: using default zone \'ext\' for interface eno4\
<font color=red> iptables-batch v1.4.21: invalid port/service \`ssh\'
specified\
Try \`iptables-batch -h\' or \'iptables-batch \--help\' for more
information.\
SuSEfirewall2: Error: iptables-batch failed, re-running using iptables\
iptables v1.4.21: invalid port/service \`ssh\' specified\
Try \`iptables -h\' or \'iptables \--help\' for more information.\
iptables v1.4.21: invalid port/service \`ssh\' specified\
Try \`iptables -h\' or \'iptables \--help\' for more information.\
ip6tables-batch v1.4.21: Port \"dhcpv6-client\" does not resolve to
anything.\
\
Try \`ip6tables-batch -h\' or \'ip6tables-batch \--help\' for more
information.\
SuSEfirewall2: Error: ip6tables-batch failed, re-running using
ip6tables\
ip6tables v1.4.21: Port \"dhcpv6-client\" does not resolve to anything.\
\
Try \`ip6tables -h\' or \'ip6tables \--help\' for more information.\
ip6tables v1.4.21: invalid port/service \`ssh\' specified\
Try \`ip6tables -h\' or \'ip6tables \--help\' for more information.\
ip6tables v1.4.21: invalid port/service \`ssh\' specified\
Try \`ip6tables -h\' or \'ip6tables \--help\' for more information.\
</font> SuSEfirewall2: Firewall rules successfully set\
</font> \|}

:   \# ls -al /etc/services
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=red> ls: cannot access /etc/services: No such file or
directory </font> \|}

\
  **Solution**: reinstall ***netcfg*** package

:   \# zypper install \--force netcfg
:   \# SuSEfirewall2
:   {\| width=\"1000px\" border=\"0\" style=\"margin:0;
    background:\#f2f2f2; font-family:Consolas,Monaco,Monospace;\"

\|- \| <font color=green> SuSEfirewall2: Setting up rules from
/etc/sysconfig/SuSEfirewall2 \...\
SuSEfirewall2: using default zone \'ext\' for interface eno1\
SuSEfirewall2: using default zone \'ext\' for interface eno2\
SuSEfirewall2: using default zone \'ext\' for interface eno3\
SuSEfirewall2: using default zone \'ext\' for interface eno4\
SuSEfirewall2: Firewall rules successfully set\
</font> \|}

[Category:Tool](Category:Tool "wikilink")
