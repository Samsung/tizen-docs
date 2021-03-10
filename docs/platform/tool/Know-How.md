How to use iSCSI

`# Discover iSCSI targets`\
`> sudo iscsiadm -m discovery -t st -p 10.89.62.166`\
`(-m, --mode op)`\
`(-t, --type=type --> st == sendtargets)`\
`(-p, --portal=ip[:port])`

`# List discovery records`\
`> sudo iscsiadm -m discovery`

`# Display all data for every discovery`\
`> sudo iscsiadm -m discovery -o show`

`# List node records`\
`> sudo iscsiadm -m node`

`# Display all data for every node`\
`> sudo iscsiadm -m node -o show`

`# Display data for a given target`\
`> sudo iscsiadm -m node -T iqn.2016-01.com.sec.vd:island.target-01 -p 10.89.62.166:3260`\
`(-T, --targetname=targetname)`

`# Display all data for a given target`\
`> sudo iscsiadm -m node -T iqn.2016-01.com.sec.vd:island.target-01 -p 10.89.62.166:3260 -o show`

`# Login`\
`> sudo iscsiadm -m node -T iqn.2016-01.com.sec.vd:island.target-01 -p 10.89.62.166:3260 --login`\
`  (-l, --login)`

`# List session records`\
`> sudo iscsiadm -m session`

`# Display all data for every session`\
`> sudo iscsiadm -m session -o show`

`# logout a session`\
`> sudo iscsiadm -m node -T iqn.2016-01.com.sec.vd:island.target-01 -p 10.89.62.166:3260 --logout`

`# Logout all sessions`\
`> sudo iscsiadm -m session -u`\
`> sudo iscsiadm -m node -u`\
`  (-u, --logout)`

`# Delete node records`\
`> sudo iscsiadm -m node -p 10.89.62.166 --op delete`\
`> sudo iscsiadm -m node -p 192.168.0.2 --op delete`

`# Delete discovery records`\
`> sudo iscsiadm -m discovery -p 10.89.62.166 --op delete`

------------------------------------------------------------------------

1.  1.  Extend LV and expand ext4 filesystem

<!-- -->

1.  Unmount the filesystem if possible

umount /home

1.  Extend the LV to use all free space

lvextend -l +100%FREE /dev/vg\_home/home

1.  Check the LV if the filesystem has already been unmounted

e2fsck -f /dev/vg\_home/home

1.  Resize the partition to fill the LV

resize2fs -p /dev/vg\_home/home

1.  Check the LV if the filesystem has already been unmounted

e2fsck -f /dev/vg\_home/home

1.  Mount the LV if the filesystem has already been unmounted

mount /home

------------------------------------------------------------------------

1.  1.  For shrinking a LV, it is better to unmount the file system
        first to avoid data loss.

<!-- -->

1.  Unmount the filesystem and check its\' LV

umount /home e2fsck -f /dev/vg\_home/home

1.  Shrink ext4 and then the LV to the desired size

resize2fs -p /dev/vg\_home/home 40G lvreduce -L 40G /dev/vg\_home/home

1.  Before continuing, run e2fsck. If it bails because the partition
2.  is too small, don\'t panic! The LV can still be extended with
3.  lvextend until e2fsck succeeds, e.g.:
4.  lvextend -L +1G /dev/vg\_home/home

e2fsck -f /dev/vg\_home/home

1.  Resize the filesystem to match the LVs size, check and mount it

resize2fs -p /dev/vg\_home/home e2fsck -f /dev/vg\_home/home

mount /home

------------------------------------------------------------------------

1.  vgdisplay vg\_srv

If you want to create an LV that uses the entire VG

1.  lvcreate -l 100%VG -n srv vg\_srv

<!-- -->

1.  lvcreate -L 128GB -n obs vg\_srv

` Logical volume "obs" created`

If you want to create an LV that uses all free PEs in the VG

1.  lvcreate -l 100%FREE -n obs vg\_srv

<!-- -->

1.  mkfs -t ext4 /dev/vg\_srv/obs

[Category:Tool](Category:Tool "wikilink")
