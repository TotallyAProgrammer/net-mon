'''
Zane Reick 2021
This is centered around PfSense, and as such some OIDs might not work on some systems
'''

hostname_oid = '1.3.6.1.2.1.1.5.0'
bytes_in_oid = '1.3.6.1.2.1.2.2.1.10.1'
bytes_out_oid = '1.3.6.1.2.1.2.2.1.16.1'
interface_oid = '1.3.6.1.2.1.2.2.1.2'
interface_oid_2 = '1.3.6.1.2.1.31.1.1.1.18.1'
min1_load_oid = '1.3.6.1.4.1.2021.10.1.3.1'
min5_load_oid = '1.3.6.1.4.1.2021.10.1.3.2'
min15_load_oid = '1.3.6.1.4.1.2021.10.1.3.3'
total_swap_oid = '1.3.6.1.4.1.2021.4.3.0'
free_swap_oid = '1.3.6.1.4.1.2021.4.4.0'
total_mem_oid = '1.3.6.1.4.1.2021.4.5.0'
used_mem_oid = '1.3.6.1.4.1.2021.4.6.0'
free_mem_oid = '1.3.6.1.4.1.2021.4.11.0'
uptime_oid = '1.3.6.1.2.1.1.3.0'
uptime2_oid = '1.3.6.1.2.1.25.1.1.0'
known_ips_oid = '1.3.6.1.2.1.4.22.1.3.2'
sys_ips_oid = '1.3.6.1.2.1.4.20.1.1'
all_ip_info = '1.3.6.1.2.1.4' # Caution, on some systems this can produce and absurd amount of output
