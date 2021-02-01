import configparser, sys
from pysnmp import hlapi
from quicksnmp import get, get_bulk_auto
from snmp_oids import *

# Read config
try:
    config = configparser.ConfigParser()
    config.read_file(open(r'C:\Users\foo\Documents\GitHub\net-mon\config.ini'))
except Exception as exp:
    print(str(exp))
    sys.exit()

community = config.get('General', 'community')
host = config.get('General', 'router_ip')
'''
#megabytes=bytes/1048576
its = get_bulk_auto(host, ['1.3.6.1.2.1.2.2.1.2 ', '1.3.6.1.2.1.31.1.1.1.18', '1.3.6.1.2.1.2.2.1.10', '1.3.6.1.2.1.2.2.1.16'], hlapi.CommunityData(community), '1.3.6.1.2.1.2.1.0')
for it in its:
    for k, v in it.items():
        if '1.3.6.1.2.1.2.2.1.10' in k or '1.3.6.1.2.1.2.2.1.16' in k:
            v = v/1073741824
        if '1.3.6.1.2.1.31.1.1.1.18' in k:
            pass
        else:
            print("{0}={1}".format(k, v))
    print('')
'''
#                  Bytes in                      Bytes out              Get interface 1 info     Get interface 1 info
oidsToLookup = [hostname_oid, min1_load_oid, total_mem_oid, total_swap_oid, uptime_oid]

for oidStr in oidsToLookup:
    oid = [oidStr]
#    oid[1] = oidStr
    print(get(host, oid, hlapi.CommunityData(community)))
