import configparser, sys, time, datetime, math
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

def secondsToWords(seconds):
    print(float(seconds/1000))
    seconds /= 1000
    ret = ""
    seconds_r = math.modf(float(seconds) / 60)
    if (seconds_r[1] > 0):
        ret = "{seconds} seconds ".format(seconds=int(seconds_r[1]))
        print(ret)
        minutes_r = math.modf((float(seconds_r[1]) / 60) / 60)
        if (minutes_r[1] > 0):
            hours_r = math.modf((float(seconds_r[1]) / 3600) / 24)
            ret = "{minutes} minutes ".format(minutes=int(minutes_r[1]))
            print(ret)
            if (hours_r[1] > 0):
                days_r = math.modf(float(float(seconds_r[1]) / (3600*24)))
                ret = "{hours} hours ".format(hours=int(hours_r[1]))
                print(ret)
                if (days_r[1] > 0):
                    ret = "{days} days ".format(days=int(days_r[1]))
                    print(ret)

    return ret

def getn(oid):
    global host
    return get(host, [oid], hlapi.CommunityData(community)).get(oid)

print(secondsToWords(getn(uptime2_oid)))

oidsToLookup = [hostname_oid, min1_load_oid, total_mem_oid, total_swap_oid, uptime_oid]
try:
    while True:
        t = getn(uptime2_oid)
        time_dict = {
            'seconds': '%.2f' % ((t/1000)%60),
            'minutes': '%.2f' % ((t/(1000*60))%60),
            'hours': '%.2f' % ((t/(1000*60*60))%24),
            'days': '%.2f' % (t/(1000*60*60*24)*10)
        }
        #seconds, minutes, hours, days = (t/1000)%60, (t/(1000*60))%60, (t/(1000*60*60))%24, (t/(1000*60*60*24))
        text_dict = {
            'hostname': str(getn(hostname_oid)),
            'min1_load': str(getn(min1_load_oid)),
            'total_mem': str(getn(total_mem_oid)),
            'total_swap': str(getn(total_swap_oid)),
            #'uptime': str('%.2f' % (int(getn(uptime2_oid))/8640000))
            'uptime': 'Days: {days}, Hours: {hours} Minutes: {minutes} Seconds: {seconds}'.format(**time_dict)
        }
        text = 'Hostname: {hostname}, 1 min load avg: {min1_load} ,Total memory: {total_mem}, Total swap: {total_swap}, Uptime: {uptime}'.format(**text_dict)
        print(text, end='\r')
        time.sleep(0.5)
except Exception as exp:
    print(str(exp) + '\n')
    sys.exit()