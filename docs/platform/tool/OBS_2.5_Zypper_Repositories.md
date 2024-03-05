###  <big>***Add zypper repositories***</big>

:   \# zypper ar -f
    <http://download.opensuse.org/repositories/OBS:/Server:/2.5/openSUSE_13.1/OBS:Server:2.5.repo>
:   \# zypper ar -Gf -t rpm-md -n \"Tizen Services (openSUSE\_13.1)\"
    <http://download.tizen.org/services/archive/0.15.13/openSUSE_13.1>
    tizen-services
:   \# zypper ar -Gf -t rpm-md -n \"Tizen Tools (openSUSE\_13.1)\"
    <http://download.tizen.org/tools/latest-release/openSUSE_13.1>
    tizen-tools
:   \# zypper refresh

[Category:Tool](Category:Tool "wikilink")
