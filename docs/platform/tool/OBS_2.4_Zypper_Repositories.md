### <big>***Add zypper repositories***</big>

:   \# zypper ar -f
    <http://download.opensuse.org/repositories/OBS:/Server:/2.4/openSUSE_12.3/OBS:Server:2.4.repo>
:   \# zypper ar -Gf -t rpm-md -n \"Tizen Services (openSUSE\_12.3)\"
    <http://download.tizen.org/services/latest-release/openSUSE_12.3>
    tizen-services
:   \# zypper ar -Gf -t rpm-md -n \"Tizen Tools (openSUSE\_12.3)\"
    <http://download.tizen.org/tools/latest-release/openSUSE_12.3>
    tizen-tools
:   \# zypper refresh

[Category:Tool](Category:Tool "wikilink")
