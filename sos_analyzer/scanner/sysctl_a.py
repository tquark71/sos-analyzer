#
# Copyright (C) 2013 Red Hat, Inc.
# Author: Satoru SATOH <ssato redhat.com>
# License: GPLv3+
#
from sos_analyzer.globals import LOGGER as logging
import sos_analyzer.scanner.base as SSB


"""sysctl -a output formats:

sunrpc.nfsd_debug = 0
sunrpc.nfs_debug = 0
sunrpc.rpc_debug = 0
crypto.fips_enabled = 0
abi.vsyscall32 = 1
    ...
dev.cdrom.autoclose = 1
dev.cdrom.info = CD-ROM information, Id: cdrom.c 3.20 2003/12/17
dev.cdrom.info =
dev.cdrom.info = drive name:            hdc
    ...
vm.drop_caches = 0
vm.lowmem_reserve_ratio = 256   256     32
vm.hugetlb_shm_group = 0
vm.nr_hugepages = 0
vm.swappiness = 60
    ...
fs.file-nr = 15810      0       6815744
fs.inode-state = 25452  1873    0       0       0       0       0
fs.inode-nr = 25452     1873
fs.binfmt_misc.status = enabled
"""


class Scanner(SSB.SinglePatternScanner):

    name = input_name = "sos_commands/kernel/sysctl_-a"
    ignore_pattern = r"^(?:\#|;).*$"
    pattern = r"^(?P<parameter>[^\s=]+)\s*=\s*(?:(?P<value>\S+.*\S+))?\s*$"

# vim:sw=4:ts=4:et: