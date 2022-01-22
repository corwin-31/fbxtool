#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Freebox command line tool
Args : <command args>...
Help provided with incomplete command

Package fbxapitool required
'''

import sys
from fbxapitool import Freebox

# Simply display of list and dictionnaries, recursively
def printList(myList, startline=''):
    if myList == None: print('Empty report')
    elif isinstance(myList, list):
        if myList == []: print('Empty list')
        else:
            for item in myList:
                if isinstance(item, list) or isinstance(item, dict):
                    printList(item,startline=startline + '  ')
                else:
                    print('{0}{1}'.format(startline, item))
                print('{0}  ##'.format(startline))
    elif not isinstance(myList, dict): print('Invalid list or dict')
    elif myList == {}: print('Empty report')
    else:
        for item in myList:
            if isinstance(myList[item], list) or isinstance(myList[item], dict):
                print('{0}{1} ='.format(startline, item))
                printList(myList[item],startline=startline + '  ')
            else: print('{0}{1} = {2}'.format(startline, item, myList[item]))
            
# Print contextual parameters
def printParms(parmList):
    print('Valid parmeters are: ',end='')
    sep = ''
    for name, typ in parmList.items():
        print(sep + name + ' (' + typ + ')',end='')
        sep = ', '
    print('')

# Simply load a file, used to get OpenVPN Client config from a file
def get_config_from_file(cfile):
    fd = open(cfile, 'r')
    return fd.read()

# All read accesses
def fbx_read_system():
    global fbx
    fbx_data = fbx.system.get_config()
    print('#System config')
    printList(fbx_data)

def fbx_read_airmedia_config():
    global fbx
    fbx_data = fbx.airmedia.get_config()
    print('#Airmedia config')
    printList(fbx_data)

def fbx_read_airmedia_receivers():
    global fbx
    fbx_data = fbx.airmedia.get_receivers()
    print('#Airmedia receivers')
    printList(fbx_data)

def fbx_read_airmedia():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read airmedia <command args...>'.format(prg))
        print('Available command args: config, receivers')
    elif cmdline[0] == 'config': fbx_read_airmedia_config()
    elif cmdline[0] == 'receivers': fbx_read_airmedia_receivers()
    else:
        print('Freebox command line tool: {0} read airmedia <command args...>'.format(prg))
        print('Available command args: config, receivers')

def fbx_read_call_list():
    global fbx
    fbx_data = fbx.call.get_call_list()
    print('#Call list')
    printList(fbx_data)

def fbx_read_call_id(call_id):
    global fbx
    try: fbx_data = fbx.call.get_call(call_id)
    except: print('Invalid id')
    else:
        print(f"#Call {call_id}")
        printList(fbx_data)

def fbx_read_call():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read call <command args...>'.format(prg))
        print('Available command args: list, <id>')
    elif cmdline[0] == 'list': fbx_read_call_list()
    else: fbx_read_call_id(cmdline[0])

def fbx_read_lcd():
    global fbx
    fbx_data = fbx.lcd.get_configuration()
    print('#LCD config')
    printList(fbx_data)

def fbx_read_ftp():
    global fbx
    fbx_data = fbx.ftp.get_ftp_configuration()
    print('#ftp config')
    printList(fbx_data)

def fbx_read_contact_list():
    global fbx
    fbx_data = fbx.contact.get_contact_list()
    print('#Contact list')
    printList(fbx_data)

def fbx_read_contact_id(contact_id):
    global fbx
    try: fbx_data = fbx.contact.get_contact(contact_id)
    except: print('Invalid id')
    else:
        print(f"#Contact {contact_id}")
        printList(fbx_data)

def fbx_read_contact():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read contact <command args...>'.format(prg))
        print('Available command args: list, <id>')
    elif cmdline[0] == 'list': fbx_read_contact_list()
    else: fbx_read_contact_id(cmdline[0])

def fbx_read_phone_list():
    global fbx
    fbx_data = fbx.phone.get_list()
    print('#Phone list')
    printList(fbx_data)

def fbx_read_phone_config():
    global fbx
    fbx_data = fbx.phone.get_config()
    print(f"#Phone config")
    printList(fbx_data)

def fbx_read_phone_dect():
    global fbx
    fbx_data = fbx.phone.get_dect_vendors()
    print(f"#Phone dect vendors")
    printList(fbx_data)

def fbx_read_phone():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read phone <command args...>'.format(prg))
        print('Available command args: config, dect, list')
    elif cmdline[0] == 'list': fbx_read_phone_list()
    elif cmdline[0] == 'config': fbx_read_phone_config()
    elif cmdline[0] == 'dect': fbx_read_phone_dect()
    else:
        print('Freebox command line tool: {0} read phone <command args...>'.format(prg))
        print('Available command args: config, dect, list')

def fbx_read_freeplug_list():
    global fbx
    fbx_data = fbx.freeplugs.get_freeplugs_list()
    print('#Freeplug list')
    printList(fbx_data)

def fbx_read_freeplug_id(freeplug_id):
    global fbx
    try: fbx_data = fbx.freeplugs.get_freeplug(freeplug_id)
    except: print('Invalid id')
    else:
        print(f"#Freeplug {freeplug_id}")
        printList(fbx_data)

def fbx_read_freeplug():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read freeplug <command args...>'.format(prg))
        print('Available command args: list, <id>')
    elif cmdline[0] == 'list': fbx_read_freeplug_list()
    else: fbx_read_freeplug_id(cmdline[0])

def fbx_read_storage_config():
    global fbx
    fbx_data = fbx.storage.get_config()
    print('#Storage config')
    printList(fbx_data)

def fbx_read_storage_media():
    global fbx
    fbx_data = fbx.storage.get_media_list()
    print('#Media list')
    printList(fbx_data)

def fbx_read_storage():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read storage <command args...>'.format(prg))
        print('Available command args: config, media')
    elif cmdline[0] == 'config': fbx_read_storage_config()
    elif cmdline[0] == 'media': fbx_read_storage_media()
    else:
        print('Freebox command line tool: {0} read airmedia <command args...>'.format(prg))
        print('Available command args: config, media')

def fbx_read_disk_list():
    global fbx
    fbx_data = fbx.storage.get_disks()
    print('#Disk list')
    printList(fbx_data)

def fbx_read_disk_id(disk_id):
    global fbx
    try: fbx_data = fbx.storage.get_disk(disk_id)
    except: print('Invalid id')
    else:
        print(f"#Disk {disk_id}")
        printList(fbx_data)

def fbx_read_disk():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read disk <command args...>'.format(prg))
        print('Available command args: list, <id>')
    elif cmdline[0] == 'list': fbx_read_disk_list()
    else: fbx_read_disk_id(cmdline[0])

def fbx_read_partition_list():
    global fbx
    fbx_data = fbx.storage.get_partitions()
    print('#Partition list')
    printList(fbx_data)

def fbx_read_partition_id(partition_id):
    global fbx
    try: fbx_data = fbx.storage.get_partition(partition_id)
    except: print('Invalid id')
    else:
        print(f"#Partition {partition_id}")
        printList(fbx_data)

def fbx_read_partition():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read partition <command args...>'.format(prg))
        print('Available command args: list, <id>')
    elif cmdline[0] == 'list': fbx_read_partition_list()
    else: fbx_read_partition_id(cmdline[0])

def fbx_read_raid_list():
    global fbx
    fbx_data = fbx.storage.get_raids()
    print('#RAID list')
    printList(fbx_data)

def fbx_read_raid_id(raid_id):
    global fbx
    try: fbx_data = fbx.storage.get_raid(raid_id)
    except: print('Invalid id')
    else:
        print(f"#RAID {raid_id}")
        printList(fbx_data)

def fbx_read_raid():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read raid <command args...>'.format(prg))
        print('Available command args: list, <id>')
    elif cmdline[0] == 'list': fbx_read_raid_list()
    else: fbx_read_raid_id(cmdline[0])

def fbx_read_netshare_afp():
    global fbx
    fbx_data = fbx.netshare.get_afp_configuration()
    print('#AFP netshare')
    printList(fbx_data)

def fbx_read_netshare_samba():
    global fbx
    fbx_data = fbx.netshare.get_samba_configuration()
    print('#SAMBA/CiFS netshare')
    printList(fbx_data)

def fbx_read_netshare():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read netshare <command args...>'.format(prg))
        print('Available command args: afp, samba')
    elif cmdline[0] == 'afp': fbx_read_netshare_afp()
    elif cmdline[0] == 'samba': fbx_read_netshare_samba()
    else:
        print('Freebox command line tool: {0} read netshare <command args...>'.format(prg))
        print('Available command args: afp, samba')

def fbx_read_connection_status():
    global fbx
    fbx_data = fbx.connection.get_status()
    print('#Connection status')
    printList(fbx_data)

def fbx_read_connection_details():
    global fbx
    fbx_data = fbx.connection.get_status_details()
    print('#Connection status details')
    printList(fbx_data)

def fbx_read_connection_config():
    global fbx
    fbx_data = fbx.connection.get_config()
    print('#Connection config')
    printList(fbx_data)

def fbx_read_connection_logs():
    global fbx
    fbx_data = fbx.connection.get_logs()
    print('#Connection logs')
    printList(fbx_data)

def fbx_read_connection_ipv6():
    global fbx
    fbx_data = fbx.connection.get_ipv6_config()
    print('#IPv6 config')
    printList(fbx_data)

def fbx_read_connection_xdsl():
    global fbx
    try: fbx_data = fbx.connection.get_xdsl_stats()
    except: print('#xDSL stats\nNo xDSL')
    else:
        print('#xDSL stats')
        printList(fbx_data)

def fbx_read_connection_ftth():
    global fbx
    try: fbx_data = fbx.connection.get_ftth_stats()
    except: print('#FTTH stats\nNo xDSL')
    else:
        print('#FTTH stats')
        printList(fbx_data)

def fbx_read_connection_lte():
    global fbx
    try: fbx_data = fbx.connection.get_lte_config()
    except: print('#LTE config\nNo LTE')
    else:
        print('#LTE config')
        printList(fbx_data)

def fbx_read_connection():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read connection <command args...>'.format(prg))
        print('Available command args: config, details, ftth, ipv6, logs, lte, status, xdsl')
    elif cmdline[0] == 'status': fbx_read_connection_status()
    elif cmdline[0] == 'config': fbx_read_connection_config()
    elif cmdline[0] == 'details': fbx_read_connection_details()
    elif cmdline[0] == 'logs': fbx_read_connection_logs()
    elif cmdline[0] == 'ipv6': fbx_read_connection_ipv6()
    elif cmdline[0] == 'xdsl': fbx_read_connection_xdsl()
    elif cmdline[0] == 'ftth': fbx_read_connection_ftth()
    elif cmdline[0] == 'lte': fbx_read_connection_lte()
    else:
        print('Freebox command line tool: {0} read connection <command args...>'.format(prg))
        print('Available command args: config, details, ftth, ipv6, logs, lte, status, xdsl')

def fbx_read_dyndns_status(dyndns_service):
    global fbx
    try: fbx_data = fbx.connection.get_dyndns_status(dyndns_service)
    except: print(f"#DynDNS status for service {dyndns_service}\nService not used")
    else:
        print(f"#DynDNS status for service {dyndns_service}")
        printList(fbx_data)

def fbx_read_dyndnsstatus():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read dyndns.status <command args...>'.format(prg))
        print('Available command args: <dyndns service (dyndns, ovh, noip)>')
    else: fbx_read_dyndns_status(cmdline[0])

def fbx_read_dyndns_config(dyndns_service):
    global fbx
    try: fbx_data = fbx.connection.get_dyndns_config(dyndns_service)
    except: print(f"#DynDNS config for service {dyndns_service}\nService not used")
    else:
        print(f"#DynDNS config for service {dyndns_service}")
        printList(fbx_data)

def fbx_read_dyndnsconfig():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read dyndns.config <command args...>'.format(prg))
        print('Available command args: <dyndns service (dyndns, ovh, noip)>')
    else: fbx_read_dyndns_config(cmdline[0])

def fbx_read_dhcp_config():
    global fbx
    fbx_data = fbx.dhcp.get_config()
    print('#DHCP config')
    printList(fbx_data)

def fbx_read_dhcp_dynamic():
    global fbx
    fbx_data = fbx.dhcp.get_dynamic_dhcp_lease()
    print('#DHCP dynamic leases')
    printList(fbx_data)

def fbx_read_dhcp_static():
    global fbx
    fbx_data = fbx.dhcp.get_static_dhcp_lease()
    print('#DHCP static leases')
    printList(fbx_data)

def fbx_read_dhcp_v6():
    global fbx
    fbx_data = fbx.dhcp.get_v6_config()
    print('#DHCP v6 config')
    printList(fbx_data)

def fbx_read_dhcp():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read dhcp <command args...>'.format(prg))
        print('Available command args: config, dynamic, static, v6')
    elif cmdline[0] == 'config': fbx_read_dhcp_config()
    elif cmdline[0] == 'dynamic': fbx_read_dhcp_dynamic()
    elif cmdline[0] == 'static': fbx_read_dhcp_static()
    elif cmdline[0] == 'v6': fbx_read_dhcp_v6()
    else:
        print('Freebox command line tool: {0} read dhcp <command args...>'.format(prg))
        print('Available command args: config, dynamic, static, v6')

def fbx_read_download_config():
    global fbx
    fbx_data = fbx.downloads.get_config()
    print('#Download config')
    printList(fbx_data)

def fbx_read_download_stats():
    global fbx
    fbx_data = fbx.downloads.get_stats()
    print('#Download stats')
    printList(fbx_data)

def fbx_read_download_tasks():
    global fbx
    fbx_data = fbx.downloads.get_tasks()
    print('#Download task list')
    printList(fbx_data)

def fbx_read_download():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read download <command args...>'.format(prg))
        print('Available command args: config, stats, tasks')
    elif cmdline[0] == 'config': fbx_read_download_config()
    elif cmdline[0] == 'stats': fbx_read_download_stats()
    elif cmdline[0] == 'tasks': fbx_read_download_tasks()
    else:
        print('Freebox command line tool: {0} read download <command args...>'.format(prg))
        print('Available command args: config, stats, tasks')

def fbx_read_dwntask_details(task_id):
    global fbx
    try: fbx_data = fbx.downloads.get_task(task_id)
    except: print(f"#Download task {task_id}\nInvalid task id")
    else:
        print(f"#Download task {task_id}")
        printList(fbx_data)

def fbx_read_dwntask_log(task_id):
    global fbx
    try: fbx_data = fbx.downloads.get_task_log(task_id)
    except: print(f"#Log of download task {task_id}\nInvalid task id")
    else:
        print(f"#Log of download task {task_id}")
        print(fbx_data)

def fbx_read_dwntask_files(task_id):
    global fbx
    try: fbx_data = fbx.downloads.get_task_files(task_id)
    except: print(f"#Files of download task {task_id}\nInvalid task id")
    else:
        print(f"#Files of download task {task_id}")
        printList(fbx_data)

def fbx_read_dwntask_trackers(task_id):
    global fbx
    try: fbx_data = fbx.downloads.get_task_trackers(task_id)
    except: print(f"#Trackers of download task {task_id}\nInvalid task id")
    else:
        print(f"#Trackers of download task {task_id}")
        printList(fbx_data)

def fbx_read_dwntask_peers(task_id):
    global fbx
    try: fbx_data = fbx.downloads.get_task_peers(task_id)
    except: print(f"#Peers of download task {task_id}\nInvalid task id")
    else:
        print(f"#Peers of download task {task_id}")
        printList(fbx_data)

def fbx_read_dwntask_pieces(task_id):
    global fbx
    try: fbx_data = fbx.downloads.get_task_pieces(task_id)
    except: print(f"#Pieces of download task {task_id}\nInvalid task id")
    else:
        print(f"#Pieces of download task {task_id}")
        print(fbx_data)

def fbx_read_dwntask_blacklist(task_id):
    global fbx
    try: fbx_data = fbx.downloads.get_task_blacklist(task_id)
    except: print(f"#Blacklist of download task {task_id}\nInvalid task id")
    else:
        print(f"#Blacklist of download task {task_id}")
        printList(fbx_data)

def fbx_read_dwntask():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read download.task <command args...>'.format(prg))
        print('Available command args: blacklist <id>, details <id>, files <id>, log <id>, peers <id> pieces <id>, trackers <id>')
    else:
        cmd = cmdline[0]
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} read download.task <command args...>'.format(prg))
            print('Available command args: blacklist <id>, details <id>, files <id>, log <id>, peers <id> pieces <id>, trackers <id>')
        else:
            if cmd == 'details': fbx_read_dwntask_details(cmdline[0])
            elif cmd == 'log': fbx_read_dwntask_log(cmdline[0])
            elif cmd == 'files': fbx_read_dwntask_files(cmdline[0])
            elif cmd == 'trackers': fbx_read_dwntask_trackers(cmdline[0])
            elif cmd == 'peers': fbx_read_dwntask_peers(cmdline[0])
            elif cmd == 'pieces': fbx_read_dwntask_pieces(cmdline[0])
            elif cmd == 'blacklist': fbx_read_dwntask_blacklist(cmdline[0])
            else:
                print('Freebox command line tool: {0} read download.task <command args...>'.format(prg))
                print('Available command args: blacklist <id>, details <id>, files <id>, log <id>, peers <id> pieces <id>, trackers <id>')

def fbx_read_dwnrss_id(rss_id):
    global fbx
    try: fbx_data = fbx.storage.get_rssfeed(rss_id)
    except: print('Invalid id')
    else:
        print(f"#Download RSS feed {rss_id}")
        printList(fbx_data)

def fbx_read_dwnrss_list():
    global fbx
    fbx_data = fbx.downloads.get_rssfeeds()
    print('#Download RSS feed list')
    printList(fbx_data)

def fbx_read_dwnrss():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read download.rss <command args...>'.format(prg))
        print('Available command args: list, <id>')
    elif cmdline[0] == 'list': fbx_read_dwnrss_list()
    else: fbx_read_dwnrss_id(cmdline[0])

def fbx_read_files_tasks():
    global fbx
    fbx_data = fbx.fs.get_tasks_list()
    print('#Tasks on files')
    printList(fbx_data)

def fbx_read_files():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read files <command args...>'.format(prg))
        print('Available command args: tasks')
    elif cmdline[0] == 'tasks': fbx_read_files_tasks()
    else:
        print('Freebox command line tool: {0} read files <command args...>'.format(prg))
        print('Available command args: tasks')

def fbx_read_fw_dmz():
    global fbx
    fbx_data = fbx.fw.get_dmz_config()
    print('#DMZ config')
    printList(fbx_data)

def fbx_read_fw_fwd():
    global fbx
    fbx_data = fbx.fw.get_forward()
    print('#Port forwarding')
    printList(fbx_data)

def fbx_read_fw_in():
    global fbx
    fbx_data = fbx.fw.get_incoming_ports_configuration()
    print('#Incoming port frowarding')
    printList(fbx_data)

def fbx_read_fw():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read fw <command args...>'.format(prg))
        print('Available command args: dmz, forward, incoming')
    elif cmdline[0] == 'dmz': fbx_read_fw_dmz()
    elif cmdline[0] == 'forward': fbx_read_fw_fwd()
    elif cmdline[0] == 'incoming': fbx_read_fw_in()
    else:
        print('Freebox command line tool: {0} read fw <command args...>'.format(prg))
        print('Available command args: dmz, forward, incoming')

def fbx_read_lan_config():
    global fbx
    fbx_data = fbx.lan.get_config()
    print('#LAN config')
    printList(fbx_data)

def fbx_read_lan_interfaces():
    global fbx
    fbx_data = fbx.lan.get_interfaces()
    print('#LAN config')
    printList(fbx_data)

def fbx_read_lan():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read lan <command args...>'.format(prg))
        print('Available command args: config, interfaces')
    elif cmdline[0] == 'config': fbx_read_lan_config()
    elif cmdline[0] == 'interfaces': fbx_read_lan_interfaces()
    else:
        print('Freebox command line tool: {0} read lan <command args...>'.format(prg))
        print('Available command args: config, interfaces')

def fbx_read_lanhost_list(inter):
    global fbx
    try: fbx_data = fbx.lan.get_hosts_list(inter)
    except: print(f"#Host list on interface {inter}\nInvalid interface")
    else:
        print(f"#Host list on interface {inter}")
        printList(fbx_data)

def fbx_read_lanhost_details(inter, host_id):
    global fbx
    try: fbx_data = fbx.lan.get_host_information(host_id, inter)
    except: print(f"#Host details for {host_id} on interface {inter}\nInvalid interface or host id")
    else:
        print(f"#Host details for {host_id} on interface {inter}")
        printList(fbx_data)

def fbx_read_lanhost():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read lan.host <command args...>'.format(prg))
        print('Available command args: list <interface>, details <interface> <host id>')
    else:
        cmd = cmdline[0]
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} read lan.host <command args...>'.format(prg))
            print('Available command args: list <interface>, details <interface> <host id>')
        else:
            if cmd == 'details':
                inter = cmdline[0]
                del cmdline[0]
                if cmdline == []:
                    print('Freebox command line tool: {0} read lan.host <command args...>'.format(prg))
                    print('Available command args: list <interface>, details <interface> <host id>')
                else: fbx_read_lanhost_details(inter, cmdline[0])
            elif cmd == 'list': fbx_read_lanhost_list(cmdline[0])
            else:
                print('Freebox command line tool: {0} read lan.host <command args...>'.format(prg))
                print('Available command args: list <interface>, details <interface> <host id>')

def fbx_read_switch_status():
    global fbx
    fbx_data = fbx.switch.get_status()
    print('#Switch status')
    printList(fbx_data)

def fbx_read_switch():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read switch <command args...>'.format(prg))
        print('Available command args: status')
    elif cmdline[0] == 'status': fbx_read_switch_status()
    else:
        print('Freebox command line tool: {0} read switch <command args...>'.format(prg))
        print('Available command args: status')

def fbx_read_switchport_config(port_id):
    global fbx
    try: fbx_data = fbx.switch.get_port_conf(port_id)
    except: print(f"#Switch port {port_id} config\nInvalid port")
    else:
        print(f"#Switch port {port_id} config")
        printList(fbx_data)

def fbx_read_switchport_stats(port_id):
    global fbx
    try: fbx_data = fbx.switch.get_port_stats(port_id)
    except: print(f"#Switch port {port_id} stats\nInvalid port")
    else:
        print(f"#Switch port {port_id} stats")
        printList(fbx_data)

def fbx_read_switchport():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read switch.port <command args...>'.format(prg))
        print('Available command args: config <port id>, stats <port id>')
    else:
        cmd = cmdline[0]
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} read switch.port <command args...>'.format(prg))
            print('Available command args: config <port id>, stats <port id>')
        else:
            if cmd == 'config': fbx_read_switchport_config(cmdline[0])
            elif cmd == 'stats': fbx_read_switchport_stats(cmdline[0])
            else:
                print('Freebox command line tool: {0} read switch.port <command args...>'.format(prg))
                print('Available command args: config <port id>, stats <port id>')

def fbx_read_upnpav_config():
    global fbx
    fbx_data = fbx.upnpav.get_configuration()
    print('#UPnP AV config')
    printList(fbx_data)

def fbx_read_upnpav():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read upnpav <command args...>'.format(prg))
        print('Available command args: config')
    elif cmdline[0] == 'config': fbx_read_upnpav_config()
    else:
        print('Freebox command line tool: {0} read upnpav <command args...>'.format(prg))
        print('Available command args: config')

def fbx_read_upnpigd_config():
    global fbx
    fbx_data = fbx.upnpigd.get_configuration()
    print('#UPnP IGD config')
    printList(fbx_data)

def fbx_read_upnpigd_redir():
    global fbx
    fbx_data = fbx.upnpigd.get_redirs()
    print('#UPnP IGD redirections')
    printList(fbx_data)

def fbx_read_upnpigd():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read upnpigd <command args...>'.format(prg))
        print('Available command args: config, redir')
    elif cmdline[0] == 'config': fbx_read_upnpigd_config()
    elif cmdline[0] == 'redir': fbx_read_upnpigd_redir()
    else:
        print('Freebox command line tool: {0} read upnpigd <command args...>'.format(prg))
        print('Available command args: config, redir')

def fbx_read_vm_id(vm_id):
    global fbx
    try: fbx_data = fbx.vm.get_config_vm(vm_id)
    except: print('Invalid id')
    else:
        print(f"#VM {vm_id} config")
        printList(fbx_data)

def fbx_read_vm_tsk(tsk_id):
    global fbx
    try: fbx_data = fbx.vm.get_task(tsk_id)
    except: print('Invalid id')
    else:
        print(f"#VM disk resize task {tsk_id} status")
        printList(fbx_data)

def fbx_read_vm_list():
    global fbx
    fbx_data = fbx.vm.get_config_all()
    print('#VM list')
    printList(fbx_data)

def fbx_read_vm_distr():
    global fbx
    fbx_data = fbx.vm.get_distrib()
    print('#VM available distributions')
    printList(fbx_data)

def fbx_read_vm():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read vm <command args...>'.format(prg))
        print('Available command args: <id>, distribs, list, task <task id>')
    elif cmdline[0] == 'list': fbx_read_vm_list()
    elif cmdline[0] == 'distribs': fbx_read_vm_distr()
    elif cmdline[0] == 'task':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} read vm <command args...>'.format(prg))
            print('Available command args: <id>, distribs, list, task <task id>')
        else: fbx_read_vm_tsk(cmdline[0])
    else: fbx_read_vm_id(cmdline[0])

def fbx_read_vpnsrv_ippool():
    global fbx
    fbx_data = fbx.vpn.get_server_ippool()
    print('#VPN Server IP pool')
    printList(fbx_data)

def fbx_read_vpnsrv_connections():
    global fbx
    fbx_data = fbx.vpn.get_server_connections()
    print('#VPN Server connections')
    printList(fbx_data)

def fbx_read_vpnsrv_list():
    global fbx
    fbx_data = fbx.vpn.get_server_list()
    print('#VPN Server list')
    printList(fbx_data)

def fbx_read_vpnsrv_users():
    global fbx
    fbx_data = fbx.vpn.get_server_users()
    print('#VPN Server users')
    printList(fbx_data)

def fbx_read_vpnsrv_config(srv_id):
    global fbx
    try: fbx_data = fbx.vpn.get_server_config(srv_id)
    except: print('Invalid id')
    else:
        print(f"#VPN Server {srv_id} config")
        printList(fbx_data)

def fbx_read_vpnsrv_user(login):
    global fbx
    try: fbx_data = fbx.vpn.get_server_user(login)
    except: print('Invalid login')
    else:
        print(f"#VPN Server user {login} config")
        printList(fbx_data)

def fbx_read_vpnsrv_open(srv, login):
    global fbx
    try: fbx_data = fbx.vpn.get_server_user_config(srv, login)
    except: print('Invalid server name or login')
    else:
        print(f"#OpenVPN Server {srv} user {login} config")
        printList(fbx_data)

def fbx_read_vpnsrv():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read vpn.server <command args...>'.format(prg))
        print('Available command args: config <server id>, connections, ippool, list, openvpn <server name> <user login>, user <login>, users')
    elif cmdline[0] == 'config':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} read vpn.server <command args...>'.format(prg))
            print('Available command args: config <server id>, connections, ippool, list, openvpn <server name> <user login>, user <login>, users')
        else: fbx_read_vpnsrv_config(cmdline[0])
    elif cmdline[0] == 'connections': fbx_read_vpnsrv_connections()
    elif cmdline[0] == 'ippool': fbx_read_vpnsrv_ippool()
    elif cmdline[0] == 'list': fbx_read_vpnsrv_list()
    elif cmdline[0] == 'users': fbx_read_vpnsrv_users()
    elif cmdline[0] == 'user':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} read vpn.server <command args...>'.format(prg))
            print('Available command args: config <server id>, connections, ippool, list, openvpn <server name> <user login>, user <login>, users')
        else: fbx_read_vpnsrv_user(cmdline[0])
    elif cmdline[0] == 'openvpn':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} read vpn.server <command args...>'.format(prg))
            print('Available command args: config <server id>, connections, ippool, list, openvpn <server name> <user login>, user <login>, users')
        else:
            srv = cmdline[0]
            del cmdline[0]
            if cmdline == []:
                print('Freebox command line tool: {0} read vpn.server <command args...>'.format(prg))
                print('Available command args: config <server id>, connections, ippool, list, openvpn <server name> <user login>, user <login>, users')
            else: fbx_read_vpnsrv_open(srv, cmdline[0])
    else:
        print('Freebox command line tool: {0} read vpn.server <command args...>'.format(prg))
        print('Available command args: config <server id>, connections, ippool, list, openvpn <server name> <user login>, user <login>, users')

def fbx_read_vpnclt_config(clt_id):
    global fbx
    try: fbx_data = fbx.vpn.get_client_config(clt_id)
    except: print('Invalid id')
    else:
        print(f"#VPN Client {clt_id} config")
        printList(fbx_data)

def fbx_read_vpnclt_list():
    global fbx
    fbx_data = fbx.vpn.get_client_list()
    print('#VPN Client list')
    printList(fbx_data)

def fbx_read_vpnclt_status():
    global fbx
    fbx_data = fbx.vpn.get_client_status()
    print('#VPN Client status')
    printList(fbx_data)

def fbx_read_vpnclt_logs():
    global fbx
    fbx_data = fbx.vpn.get_client_logs()
    print('#VPN Client logs')
    print(fbx_data)

def fbx_read_vpnclt_slv():
    global fbx
    fbx_data = fbx.vpn.get_slavery()
    print('#VPN Client slavery')
    print(fbx_data)

def fbx_read_vpnclt():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read vpn.client <command args...>'.format(prg))
        print('Available command args: config <client id>, list, logs, slavery, status')
    elif cmdline[0] == 'config':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} read vpn.client <command args...>'.format(prg))
            print('Available command args: config <client id>, list, logs, slavery, status')
        else: fbx_read_vpnclt_config(cmdline[0])
    elif cmdline[0] == 'list': fbx_read_vpnclt_list()
    elif cmdline[0] == 'status': fbx_read_vpnclt_status()
    elif cmdline[0] == 'logs': fbx_read_vpnclt_logs()
    elif cmdline[0] == 'slavery': fbx_read_vpnclt_slv()
    else:
        print('Freebox command line tool: {0} read vpn.client <command args...>'.format(prg))
        print('Available command args: config <client id>, list, logs, slavery, status')

def fbx_read_wifi_config():
    global fbx
    fbx_data = fbx.wifi.get_global_config()
    print('#Wifi config')
    printList(fbx_data)

def fbx_read_wifi_allaccess():
    global fbx
    fbx_data = fbx.wifi.get_ap_list()
    print('#Wifi access point list')
    printList(fbx_data)

def fbx_read_wifi_allbss():
    global fbx
    fbx_data = fbx.wifi.get_bss_list()
    print('#Wifi BSS list')
    printList(fbx_data)

def fbx_read_wifi_candidates():
    global fbx
    fbx_data = fbx.wifi.get_wps_candidates()
    print('#Wifi WPS candidates')
    printList(fbx_data)

def fbx_read_wifi_filters():
    global fbx
    fbx_data = fbx.wifi.get_wifi_mac_filters()
    print('#Wifi MAC filters')
    printList(fbx_data)

def fbx_read_wifi_keys():
    global fbx
    fbx_data = fbx.wifi.get_wifi_custom_keys()
    print('#Wifi custom keys')
    printList(fbx_data)

def fbx_read_wifi_planning():
    global fbx
    fbx_data = fbx.wifi.get_wifi_planning()
    print('#Wifi planning')
    printList(fbx_data)

def fbx_read_wifi_sessions():
    global fbx
    fbx_data = fbx.wifi.get_wps_sessions()
    print('#Wifi WPS sessions')
    print(fbx_data)

def fbx_read_wifi_wps():
    global fbx
    fbx_data = fbx.wifi.get_wps_status()
    print('#Wifi WPS global status')
    print(fbx_data)

def fbx_read_wifi_access(ap_id):
    global fbx
    try: fbx_data = fbx.wifi.get_ap(ap_id)
    except: print('Invalid id')
    else:
        print(f"#Wifi access point {ap_id}")
        printList(fbx_data)

def fbx_read_wifi_bss(ap_id):
    global fbx
    try: fbx_data = fbx.wifi.get_bss(ap_id)
    except: print('Invalid id')
    else:
        print(f"#Wifi BSS for access point {ap_id}")
        printList(fbx_data)

def fbx_read_wifi_channels(ap_id):
    global fbx
    try: fbx_data = fbx.wifi.get_ap_allowed_channel(ap_id)
    except: print('Invalid id')
    else:
        print(f"#Wifi allowed channels for access point {ap_id}")
        printList(fbx_data)

def fbx_read_wifi_neighbors(ap_id):
    global fbx
    try: fbx_data = fbx.wifi.get_ap_neighbors(ap_id)
    except: print('Invalid id')
    else:
        print(f"#Wifi neighbors for access point {ap_id}")
        printList(fbx_data)

def fbx_read_wifi_session(sess_id):
    global fbx
    try: fbx_data = fbx.wifi.get_wps_session(sess_id)
    except: print('Invalid id')
    else:
        print(f"#Wifi WPS session {sess_id}")
        printList(fbx_data)

def fbx_read_wifi_stations(ap_id):
    global fbx
    try: fbx_data = fbx.wifi.get_station_list(ap_id)
    except: print('Invalid id')
    else:
        print(f"#Wifi station list for access point {ap_id}")
        printList(fbx_data)

def fbx_read_wifi_station(ap_id, mac):
    global fbx
    try: fbx_data = fbx.wifi.get_wifi_access_point_station(ap_id, mac)
    except: print('Invalid id or mac')
    else:
        print(f"#Wifi station {mac} for access point {ap_id}")
        printList(fbx_data)

def fbx_read_wifi_usage(ap_id):
    global fbx
    try: fbx_data = fbx.wifi.get_wifi_access_point_channel_usage(ap_id)
    except: print('Invalid id')
    else:
        print(f"#Wifi channel usage for access point {ap_id}")
        printList(fbx_data)

def fbx_read_wifi_filter(filter_id):
    global fbx
    try: fbx_data = fbx.wifi.get_wifi_mac_filter(filter_id)
    except: print('Invalid id')
    else:
        print(f"#MAC filter {filter_id}")
        printList(fbx_data)

def fbx_read_wifi_key(key_id):
    global fbx
    try: fbx_data = fbx.wifi.get_wifi_custom_key(key_id)
    except: print('Invalid id')
    else:
        print(f"#Wifi custom key {key_id}")
        printList(fbx_data)

def fbx_read_wifi():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read wifi <command args...>'.format(prg))
        print('Available command args: allaccess, access <access point id>, allbss, bss <access point id>, candidates, channels <access point id>, config, filters, filter <filter id>, keys, key <key id>, neighbors <access point id>, planning, session <id>, sessions, station <access point id> <mac>, stations <access point id>, usage <access point id>, wps')
    elif cmdline[0] == 'access':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} read wifi <command args...>'.format(prg))
            print('Available command args: allaccess, access <access point id>, allbss, bss <access point id>, candidates, channels <access point id>, config, filters, filter <filter id>, keys, key <key id>, neighbors <access point id>, planning, session <id>, sessions, station <access point id> <mac>, stations <access point id>, usage <access point id>, wps')
        else: fbx_read_wifi_access(cmdline[0])
    elif cmdline[0] == 'bss':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} read wifi <command args...>'.format(prg))
            print('Available command args: allaccess, access <access point id>, allbss, bss <access point id>, candidates, channels <access point id>, config, filters, filter <filter id>, keys, key <key id>, neighbors <access point id>, planning, session <id>, sessions, station <access point id> <mac>, stations <access point id>, usage <access point id>, wps')
        else: fbx_read_wifi_bss(cmdline[0])
    elif cmdline[0] == 'channels':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} read wifi <command args...>'.format(prg))
            print('Available command args: allaccess, access <access point id>, allbss, bss <access point id>, candidates, channels <access point id>, config, filters, filter <filter id>, keys, key <key id>, neighbors <access point id>, planning, session <id>, sessions, station <access point id> <mac>, stations <access point id>, usage <access point id>, wps')
        else: fbx_read_wifi_channels(cmdline[0])
    elif cmdline[0] == 'neighbors':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} read wifi <command args...>'.format(prg))
            print('Available command args: allaccess, access <access point id>, allbss, bss <access point id>, candidates, channels <access point id>, config, filters, filter <filter id>, keys, key <key id>, neighbors <access point id>, planning, session <id>, sessions, station <access point id> <mac>, stations <access point id>, usage <access point id>, wps')
        else: fbx_read_wifi_neighbors(cmdline[0])
    elif cmdline[0] == 'session':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} read wifi <command args...>'.format(prg))
            print('Available command args: allaccess, access <access point id>, allbss, bss <access point id>, candidates, channels <access point id>, config, filters, filter <filter id>, keys, key <key id>, neighbors <access point id>, planning, session <id>, sessions, station <access point id> <mac>, stations <access point id>, usage <access point id>, wps')
        else: fbx_read_wifi_session(cmdline[0])
    elif cmdline[0] == 'stations':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} read wifi <command args...>'.format(prg))
            print('Available command args: allaccess, access <access point id>, allbss, bss <access point id>, candidates, channels <access point id>, config, filters, filter <filter id>, keys, key <key id>, neighbors <access point id>, planning, session <id>, sessions, station <access point id> <mac>, stations <access point id>, usage <access point id>, wps')
        else: fbx_read_wifi_stations(cmdline[0])
    elif cmdline[0] == 'station':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} read wifi <command args...>'.format(prg))
            print('Available command args: allaccess, access <access point id>, allbss, bss <access point id>, candidates, channels <access point id>, config, filters, filter <filter id>, keys, key <key id>, neighbors <access point id>, planning, session <id>, sessions, station <access point id> <mac>, stations <access point id>, usage <access point id>, wps')
        else:
            ap = cmdline[0]
            del cmdline[0]
            if cmdline == []:
                print('Freebox command line tool: {0} read wifi <command args...>'.format(prg))
                print('Available command args: allaccess, access <access point id>, allbss, bss <access point id>, candidates, channels <access point id>, config, filters, filter <filter id>, keys, key <key id>, neighbors <access point id>, planning, session <id>, sessions, station <access point id> <mac>, stations <access point id>, usage <access point id>, wps')
            else: fbx_read_wifi_station(ap, cmdline[0])
    elif cmdline[0] == 'usage':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} read wifi <command args...>'.format(prg))
            print('Available command args: allaccess, access <access point id>, allbss, bss <access point id>, candidates, channels <access point id>, config, filters, filter <filter id>, keys, key <key id>, neighbors <access point id>, planning, session <id>, sessions, station <access point id> <mac>, stations <access point id>, usage <access point id>, wps')
        else: fbx_read_wifi_usage(cmdline[0])
    elif cmdline[0] == 'filter':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} read wifi <command args...>'.format(prg))
            print('Available command args: allaccess, access <access point id>, allbss, bss <access point id>, candidates, channels <access point id>, config, filters, filter <filter id>, keys, key <key id>, neighbors <access point id>, planning, session <id>, sessions, station <access point id> <mac>, stations <access point id>, usage <access point id>, wps')
        else: fbx_read_wifi_filter(cmdline[0])
    elif cmdline[0] == 'key':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} read wifi <command args...>'.format(prg))
            print('Available command args: allaccess, access <access point id>, allbss, bss <access point id>, candidates, channels <access point id>, config, filters, filter <filter id>, keys, key <key id>, neighbors <access point id>, planning, session <id>, sessions, station <access point id> <mac>, stations <access point id>, usage <access point id>, wps')
        else: fbx_read_wifi_key(cmdline[0])
    elif cmdline[0] == 'allaccess': fbx_read_wifi_allaccess()
    elif cmdline[0] == 'allbss': fbx_read_wifi_allbss()
    elif cmdline[0] == 'candidates': fbx_read_wifi_candidates()
    elif cmdline[0] == 'config': fbx_read_wifi_config()
    elif cmdline[0] == 'filters': fbx_read_wifi_filters()
    elif cmdline[0] == 'keys': fbx_read_wifi_keys()
    elif cmdline[0] == 'planning': fbx_read_wifi_planning()
    elif cmdline[0] == 'sessions': fbx_read_wifi_sessions()
    elif cmdline[0] == 'wps': fbx_read_wifi_wps()
    else:
        print('Freebox command line tool: {0} read wifi <command args...>'.format(prg))
        print('Available command args: allaccess, access <access point id>, allbss, bss <access point id>, candidates, channels <access point id>, config, filters, filter <filter id>, keys, key <key id>, neighbors <access point id>, planning, session <id>, sessions, station <access point id> <mac>, stations <access point id>, usage <access point id>, wps')

def fbx_read_notifications_list():
    global fbx
    fbx_data = fbx.notifications.get_notification_targets()
    print('#Notification targets')
    printList(fbx_data)

def fbx_read_notifications_id(target_id):
    global fbx
    try: fbx_data = fbx.notifications.get_notification_target(target_id)
    except: print('Invalid id')
    else:
        print(f"#Wifi channel usage for access point {target_id}")
        printList(fbx_data)

def fbx_read_notifications():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} read notifications <command args...>'.format(prg))
        print('Available command args: list, <target id>')
    elif cmdline[0] == 'list': fbx_read_notifications_list()
    else: fbx_read_notifications_id(cmdline[0])

def fbx_read_prof_rule(prof_id, rul_id):
    global fbx
    try: fbx_data = fbx.profile.get_netcontrol_rule(prof_id, rul_id)
    except: print('Invalid profile or rule id')
    else:
        print(f"#Rule {rul_id} for profile {prof_id}")
        printList(fbx_data)

def fbx_read_prof_rules(prof_id):
    global fbx
    try: fbx_data = fbx.profile.get_netcontrol_rules(prof_id)
    except: print('Invalid id')
    else:
        print(f"#Rule for profile {prof_id}")
        printList(fbx_data)

def fbx_read_prof_controls():
    global fbx
    fbx_data = fbx.profile.get_netcontrols()
    print('#All net controls')
    printList(fbx_data)

def fbx_read_prof_control(prof_id):
    global fbx
    try: fbx_data = fbx.profile.get_netcontrol(prof_id)
    except: print('Invalid id')
    else:
        print(f"#Net controls for profile {prof_id}")
        printList(fbx_data)

def fbx_read_prof_list():
    global fbx
    fbx_data = fbx.profile.get_profiles()
    print('#Profile list')
    printList(fbx_data)

def fbx_read_prof_id(prof_id):
    global fbx
    try: fbx_data = fbx.profile.get_profile(prof_id)
    except: print('Invalid id')
    else:
        print(f"#Profile {prof_id}")
        printList(fbx_data)

def fbx_read_profile():
    global fbx
    global cmdline
    del cmdline[0]
    fbx_data = fbx.profile.get_migration_status()
    if cmdline == [] or not fbx_data['default_mode_migrated']:
        print('Freebox command line tool: {0} read profile <command args...>'.format(prg))
        print('Available command args: <id>, control <id>, controls, list, rule <profile id> <rule id>, rules <id>')
        if not fbx_data['default_mode_migrated']: print('Warning : you must migrate to new profiles first')
        else: print('Info : migration to new profiles ok')
    elif cmdline[0] == 'control':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} read profile <command args...>'.format(prg))
            print('Available command args: <id>, control <id>, controls, list, rule <profile id> <rule id>, rules <id>')
        else: fbx_read_prof_control(cmdline[0])
    elif cmdline[0] == 'rules':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} read profile <command args...>'.format(prg))
            print('Available command args: <id>, control <id>, controls, list, rule <profile id> <rule id>, rules <id>')
        else: fbx_read_prof_rules(cmdline[0])
    elif cmdline[0] == 'rule':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} read profile <command args...>'.format(prg))
            print('Available command args: <id>, control <id>, controls, list, rule <profile id> <rule id>, rules <id>')
        else:
            prf = cmdline[0]
            del cmdline[0]
            if cmdline == []:
                print('Freebox command line tool: {0} read profile <command args...>'.format(prg))
                print('Available command args: <id>, control <id>, controls, list, rule <profile id> <rule id>, rules <id>')
            else: fbx_read_prof_rule(prf, cmdline[0])
    elif cmdline[0] == 'list': fbx_read_prof_list()
    elif cmdline[0] == 'controls': fbx_read_prof_controls()
    else: fbx_read_prof_id(cmdline[0])

def fbx_read():
    global fbx
    global cmdline
    if cmdline == []:
        print('Freebox command line tool: {0} read <command args...>'.format(prg))
        print('Available command args: airmedia, call, connection, contact, dhcp, disk, download, download.rss, download.task, dyndns.config, dynsdns.status, files, freeplug, ftp, fw, lan, lan.host, lcd, netshare, notifications, partition, phone, profile, raid, storage, switch, switch.port, system, upnpav, upnpigd, vm, vpn.client, vpn.server, wifi')
    elif cmdline[0] == 'system': fbx_read_system()
    elif cmdline[0] == 'airmedia': fbx_read_airmedia()
    elif cmdline[0] == 'call': fbx_read_call()
    elif cmdline[0] == 'lcd': fbx_read_lcd()
    elif cmdline[0] == 'ftp': fbx_read_ftp()
    elif cmdline[0] == 'contact': fbx_read_contact()
    elif cmdline[0] == 'phone': fbx_read_phone()
    elif cmdline[0] == 'freeplug': fbx_read_freeplug()
    elif cmdline[0] == 'storage': fbx_read_storage()
    elif cmdline[0] == 'disk': fbx_read_disk()
    elif cmdline[0] == 'partition': fbx_read_partition()
    elif cmdline[0] == 'notifications': fbx_read_notifications()
    elif cmdline[0] == 'raid': fbx_read_raid()
    elif cmdline[0] == 'netshare': fbx_read_netshare()
    elif cmdline[0] == 'connection': fbx_read_connection()
    elif cmdline[0] == 'dyndns.status': fbx_read_dyndnsstatus()
    elif cmdline[0] == 'dyndns.config': fbx_read_dyndnsconfig()
    elif cmdline[0] == 'dhcp': fbx_read_dhcp()
    elif cmdline[0] == 'download': fbx_read_download()
    elif cmdline[0] == 'download.task': fbx_read_dwntask()
    elif cmdline[0] == 'download.rss': fbx_read_dwnrss()
    elif cmdline[0] == 'files': fbx_read_files()
    elif cmdline[0] == 'fw': fbx_read_fw()
    elif cmdline[0] == 'lan': fbx_read_lan()
    elif cmdline[0] == 'lan.host': fbx_read_lanhost()
    elif cmdline[0] == 'switch': fbx_read_switch()
    elif cmdline[0] == 'switch.port': fbx_read_switchport()
    elif cmdline[0] == 'upnpav': fbx_read_upnpav()
    elif cmdline[0] == 'upnpigd': fbx_read_upnpigd()
    elif cmdline[0] == 'vm': fbx_read_vm()
    elif cmdline[0] == 'vpn.server': fbx_read_vpnsrv()
    elif cmdline[0] == 'vpn.client': fbx_read_vpnclt()
    elif cmdline[0] == 'wifi': fbx_read_wifi()
    elif cmdline[0] == 'profile': fbx_read_profile()
    else:
        print('Freebox command line tool: {0} read <command args...>'.format(prg))
        print('Available command args: airmedia, call, connection, contact, dhcp, disk, download, download.rss, download.task, dyndns.config, dyndns.status, files, freeplug, ftp, fw, lan, lan.host, lcd, netshare, notifications, partition, phone, profile, raid, storage, switch, switch.port, system, upnpav, upnpigd, vm, vpn.client, vpn.server, wifi')

def fbx_change_system():
    global fbx
    fbx.system.reboot()
    print('#System reboot requested')

def fbx_change_dwntask_start():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change download.task start <command args...>'.format(prg))
        print('Available command args: <task id> <tracker url>')
    else:
        tsk = cmdline[0]
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change download.task start <command args...>'.format(prg))
            print('Available command args: <task id> <tracker url>')
        else:
            try: fbx_data = fbx.downloads.start_task_tracker(tsk, cmdline[0])
            except: print('Invalid id or url')
            else:
                print(f"#Tracker {cmdline[0]} started for download task {tsk}")
                printList(fbx_data)

def fbx_change_dwntask_stop():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change download.task stop <command args...>'.format(prg))
        print('Available command args: <task id> <tracker url>')
    else:
        tsk = cmdline[0]
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change download.task stop <command args...>'.format(prg))
            print('Available command args: <task id> <tracker url>')
        else:
            try: fbx_data = fbx.downloads.stop_task_tracker(tsk, cmdline[0])
            except: print('Invalid id or url')
            else:
                print(f"#Tracker {cmdline[0]} stopped for download task {tsk}")
                printList(fbx_data)

def fbx_change_dwnprio():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change download.task priority <command args...>'.format(prg))
        print('Available command args: <task id> <file id> <priority>')
    else:
        tsk = cmdline[0]
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change download.task priority <command args...>'.format(prg))
            print('Available command args: <task id> <file id> <priority>')
        else:
            file = cmdline[0]
            del cmdline[0]
            if cmdline == []:
                print('Freebox command line tool: {0} change download.task priority <command args...>'.format(prg))
                print('Available command args: <task id> <file id> <priority>')
            else:
                try: fbx_data = fbx.downloads.set_file_priority(tsk, file, cmdline[0])
                except: print('Invalid parms')
                else:
                    print(f"#File {file} priority for download task {tsk} set to {cmdline[0]}")
                    printList(fbx_data)

def fbx_change_dwntask_throt():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change download.task throttling <command args...>'.format(prg))
        print('Available command args: <mode>')
    else:
        try: fbx_data = fbx.downloads.set_throttling(cmdline[0])
        except: print('Invalid parms')
        else:
            print(f"#Download throttling set to {cmdline[0]}")
            printList(fbx_data)

def fbx_change_dwntask_tsk():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change download.task task <command args...>'.format(prg))
        print('Available command args: <task id> [<parmameter>=<value> ...]')
        printParms(fbx.downloads.task_write_parms)
    else:
        tsk = cmdline[0]
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change download.task task <command args...>'.format(prg))
            print('Available command args: <task id> [<parmameter>=<value> ...]')
            printParms(fbx.downloads.task_write_parms)
        else:
            conf = fbx.encodeJSON(fbx.downloads.task_write_parms, cmdline)
            if conf == None:
                print('Freebox command line tool: {0} change download.task task <command args...>'.format(prg))
                print('Available command args: <task id> [<parmameter>=<value> ...]')
                printParms(fbx.downloads.task_write_parms)
            else:
                try: fbx_data = fbx.downloads.set_task(tsk, conf)
                except: print('Invalid parms')
                else:
                    print(f"#Task {tsk} changed")
                    printList(fbx_data)

def fbx_change_dwnblock():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change download config.blocklist <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.downloads.blocklist_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.downloads.blocklist_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change download config.blocklist <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.downloads.blocklist_write_parms)
        else:
            try: fbx_data = fbx.downloads.set_config({ 'blocklist': conf})
            except: print('Invalid parms')
            else:
                print(f"#Blocklist config changed")
                printList(fbx_data)

def fbx_change_dwnbt():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change download config.bt <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.downloads.bt_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.downloads.bt_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change download config.bt <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.downloads.bt_write_parms)
        else:
            try: fbx_data = fbx.downloads.set_config({ 'bt': conf})
            except: print('Invalid parms')
            else:
                print(f"#BitTorrent config changed")
                printList(fbx_data)

def fbx_change_dwnnews():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change download config.news <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.downloads.news_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.downloads.news_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change download config.news <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.downloads.news_write_parms)
        else:
            try: fbx_data = fbx.downloads.set_config({ 'news': conf})
            except: print('Invalid parms')
            else:
                print(f"#News config changed")
                printList(fbx_data)

def fbx_change_dwnthrot():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change download config.throttling <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.downloads.throttling_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.downloads.throttling_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change download config.throttling <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.downloads.throttling_write_parms)
        else:
            try: fbx_data = fbx.downloads.set_config({ 'throttling': conf})
            except: print('Invalid parms')
            else:
                print(f"#Throttling config changed")
                printList(fbx_data)

def fbx_change_dwnglob():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change download config.global <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.downloads.global_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.downloads.global_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change download config.global <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.downloads.global_write_parms)
        else:
            try: fbx_data = fbx.downloads.set_config(conf)
            except: print('Invalid parms')
            else:
                print(f"#Download global config changed")
                printList(fbx_data)

def fbx_change_dwnfeed():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change download config.feed <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.downloads.feed_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.downloads.feed_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change download config.feed <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.downloads.feed_write_parms)
        else:
            try: fbx_data = fbx.downloads.set_config({ 'feed': conf })
            except: print('Invalid parms')
            else:
                print(f"#RSS feed config changed")
                printList(fbx_data)

def fbx_change_dwntask():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change download.task <command args...>'.format(prg))
        print('Available command args: priority, start, stop, task, throttling')
    elif cmdline[0] == 'start': fbx_change_dwntask_start()
    elif cmdline[0] == 'stop': fbx_change_dwntask_stop()
    elif cmdline[0] == 'priority': fbx_change_dwnprio()
    elif cmdline[0] == 'task': fbx_change_dwntask_tsk()
    elif cmdline[0] == 'throttling': fbx_change_dwntask_throt()
    else:
        print('Freebox command line tool: {0} change download.task <command args...>'.format(prg))
        print('Available command args: priority, start, stop, task, throttling')

def fbx_change_downloads():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change downloads <command args...>'.format(prg))
        print('Available command args: config.blocklist, config.bt, config.feed, config.global, config.news, config.throttling')
    elif cmdline[0] == 'config.blocklist': fbx_change_dwnblock()
    elif cmdline[0] == 'config.bt': fbx_change_dwnbt()
    elif cmdline[0] == 'config.feed': fbx_change_dwnfeed()
    elif cmdline[0] == 'config.global': fbx_change_dwnglob()
    elif cmdline[0] == 'config.news': fbx_change_dwnnews()
    elif cmdline[0] == 'config.throttling': fbx_change_dwnthrot()
    else:
        print('Freebox command line tool: {0} change downloads <command args...>'.format(prg))
        print('Available command args: config.blocklist, config.bt, config.feed, config.global, config.news, config.throttling')

def fbx_change_airmedia():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change airmedia <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.airmedia.airmedia_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.airmedia.airmedia_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change airmedia <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.airmedia.airmedia_write_parms)
        else:
            try: fbx_data = fbx.airmedia.set_config(conf)
            except: print('Invalid parms')
            else:
                print(f"#Airmedia changed")
                printList(fbx_data)

def fbx_change_call_readall():
    global fbx
    try: fbx_data = fbx.call.mark_call_list_as_read()
    except: print('An error occured')
    else:
        print('#Mark all calls as read')
        printList(fbx_data)

def fbx_change_call_read(call_id):
    global fbx
    try: fbx_data = fbx.call.mark_call_as_read(call_id)
    except: print('Invalid id')
    else:
        print(f"#Mark call {call_id} as read")
        printList(fbx_data)

def fbx_change_call():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change call <command args...>'.format(prg))
        print('Available command args: read <id>, read.all')
    elif cmdline[0] == 'read.all': fbx_change_call_readall()
    elif cmdline[0] == 'read':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change call <command args...>'.format(prg))
            print('Available command args: read <id>, read.all')
        else: fbx_change_call_read(cmdline[0])
    else:
        print('Freebox command line tool: {0} change call <command args...>'.format(prg))
        print('Available command args: read <id>, read.all')

def fbx_change_contactnum():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change contact.number <command args...>'.format(prg))
        print('Available command args: <id> [<parmameter>=<value> ...]')
        printParms(fbx.contact.contact_write_numbers)
    else:
        num_id = cmdline[0]
        del cmdline[0]
        conf = fbx.encodeJSON(fbx.contact.contact_write_numbers, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change contact.number <command args...>'.format(prg))
            print('Available command args: <id> [<parmameter>=<value> ...]')
            printParms(fbx.contact.contact_write_numbers)
        else:
            try: fbx_data = fbx.contact.update_number(num_id, conf)
            except: print('Invalid parms')
            else:
                print(f"#Contact number {num_id} changed")
                printList(fbx_data)

def fbx_change_contact():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change contact <command args...>'.format(prg))
        print('Available command args: <id> [<parmameter>=<value> ...]')
        printParms(fbx.contact.contact_write_parms)
    else:
        contact_id = cmdline[0]
        del cmdline[0]
        conf = fbx.encodeJSON(fbx.contact.contact_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change contact <command args...>'.format(prg))
            print('Available command args: <id> [<parmameter>=<value> ...]')
            printParms(fbx.contact.contact_write_parms)
        else:
            try: fbx_data = fbx.contact.update_contact(contact_id, conf)
            except: print('Invalid parms')
            else:
                print(f"#Contact {contact_id} changed")
                printList(fbx_data)

def fbx_change_lcd():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change lcd <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.lcd.lcd_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.lcd.lcd_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change lcd <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.lcd.lcd_write_parms)
        else:
            try: fbx_data = fbx.lcd.set_configuration(conf)
            except: print('Invalid parms')
            else:
                print(f"#LCD config changed")
                printList(fbx_data)

def fbx_change_ftp():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change ftp <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.ftp.ftp_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.ftp.ftp_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change ftp <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.ftp.ftp_write_parms)
        else:
            try: fbx_data = fbx.ftp.set_ftp_configuration(conf)
            except: print('Invalid parms')
            else:
                print(f"#FTP config changed")
                printList(fbx_data)

def fbx_change_afp():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change netshare afp <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.netshare.afp_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.netshare.afp_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change netshare afp <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.netshare.afp_write_parms)
        else:
            try: fbx_data = fbx.netshare.set_afp_configuration(conf)
            except: print('Invalid parms')
            else:
                print(f"#AFP config changed")
                printList(fbx_data)

def fbx_change_samba():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change netshare samba <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.netshare.samba_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.netshare.samba_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change netshare samba <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.netshare.samba_write_parms)
        else:
            try: fbx_data = fbx.netshare.set_samba_configuration(conf)
            except: print('Invalid parms')
            else:
                print(f"#SAMBA/CiFS config changed")
                printList(fbx_data)

def fbx_change_netshare():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change netshare <command args...>'.format(prg))
        print('Available command args: afp, samba')
    elif cmdline[0] == 'afp': fbx_change_afp()
    elif cmdline[0] == 'samba': fbx_change_samba()
    else:
        print('Freebox command line tool: {0} change netshare <command args...>'.format(prg))
        print('Available command args: afp, samba')

def fbx_reset_freeplug(free_id):
    global fbx
    try: fbx_data = fbx.freeplugs.reset_freeplug(free_id)
    except: print('An error occured')
    else:
        print(f"#Resetting freeplu {free_id}")
        printList(fbx_data)

def fbx_change_freeplug():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change freeplug <command args...>'.format(prg))
        print('Available command args: reset <id>')
    elif cmdline[0] == 'reset':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change freeplug <command args...>'.format(prg))
            print('Available command args: reset <id>')
        else: fbx_reset_freeplug(cmdline[0])
    else:
        print('Freebox command line tool: {0} change freeplug <command args...>'.format(prg))
        print('Available command args: reset <id>')

def fbx_change_upnpav():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change upnpav <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.upnpav.upnpav_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.upnpav.upnpav_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change upnpav <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.upnpav.upnpav_write_parms)
        else:
            try: fbx_data = fbx.upnpav.set_configuration(conf)
            except: print('Invalid parms')
            else:
                print(f"#UPnP AV config changed")
                printList(fbx_data)

def fbx_change_upnpigd():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change upnpigd <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.upnpigd.upnpigd_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.upnpigd.upnpigd_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change upnpigd <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.upnpigd.upnpigd_write_parms)
        else:
            try: fbx_data = fbx.upnpigd.update_configuration(conf)
            except: print('Invalid parms')
            else:
                print(f"#UPnP IGD config changed")
                printList(fbx_data)

def fbx_change_dect():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change phone dect <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.phone.dect_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.phone.dect_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change phone dect <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.phone.dect_write_parms)
        else:
            try: fbx_data = fbx.phone.start_dect_configuration(conf)
            except: print('Invalid parms')
            else:
                print(f"#DECT config changed")
                printList(fbx_data)

def fbx_change_phone_ring():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change phone ring<command args...>'.format(prg))
        print('Available command args: start, stop')
    elif cmdline[0] == 'start':
        fbx.phone.start_fxs_ring()
    elif cmdline[0] == 'stop':
        fbx.phone.start_fxs_ring()
    else:
        print('Freebox command line tool: {0} change phone ring <command args...>'.format(prg))
        print('Available command args: start, stop')

def fbx_change_phone():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change phone <command args...>'.format(prg))
        print('Available command args: dect, ring')
    elif cmdline[0] == 'dect': fbx_change_dect()
    elif cmdline[0] == 'ring': fbx_change_phone_ring()
    else:
        print('Freebox command line tool: {0} change phone <command args...>'.format(prg))
        print('Available command args: dect, ring')

def fbx_change_dhcp_config():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change dhcp config <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.dhcp.dhcp_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.dhcp.dhcp_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change dhcp config <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.dhcp.dhcp_write_parms)
        else:
            try: fbx_data = fbx.dhcp.set_config(conf)
            except: print('Invalid parms')
            else:
                print(f"#DHCP config changed")
                printList(fbx_data)

def fbx_change_dhcp_v6():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change dhcp v6 <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.dhcp.dhcpv6_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.dhcp.dhcpv6_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change dhcp v6 <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.dhcp.dhcpv6_write_parms)
        else:
            try: fbx_data = fbx.dhcp.set_v6_config(conf)
            except: print('Invalid parms')
            else:
                print(f"#DHCP v6 config changed")
                printList(fbx_data)

def fbx_change_dhcp_static(lease_id):
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change dhcp static <id> <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.dhcp.lease_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.dhcp.lease_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change dhcp static <id> <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.dhcp.lease_write_parms)
        else:
            try: fbx_data = fbx.dhcp.update_static_dhcp_lease(lease_id, conf)
            except: print('Invalid parms')
            else:
                print(f"#DHCP static lease {lease_id} changed")
                printList(fbx_data)

def fbx_change_dhcp():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change dhcp <command args...>'.format(prg))
        print('Available command args: config, static <id>, v6')
    elif cmdline[0] == 'config': fbx_change_dhcp_config()
    elif cmdline[0] == 'v6': fbx_change_dhcp_v6()
    elif cmdline[0] == 'static':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change dhcp <command args...>'.format(prg))
            print('Available command args: config, static <id>, v6')
        else: fbx_change_dhcp_static(cmdline[0])
    else:
        print('Freebox command line tool: {0} change dhcp <command args...>'.format(prg))
        print('Available command args: config, static <id>, v6')

def fbx_change_lan_config():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change lan config <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.lan.lanconf_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.lan.lanconf_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change lan config <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.lan.lanconf_write_parms)
        else:
            try: fbx_data = fbx.lan.set_config(conf)
            except: print('Invalid parms')
            else:
                print(f"#LAN config changed")
                printList(fbx_data)

def fbx_change_lan():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change lan <command args...>'.format(prg))
        print('Available command args: config')
    elif cmdline[0] == 'config': fbx_change_lan_config()
    else:
        print('Freebox command line tool: {0} change lan <command args...>'.format(prg))
        print('Available command args: config')

def fbx_change_lanhost_config():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change lan.host config <interface> <host id> <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.lan.lanhost_write_parms)
    else:
        interf = cmdline[0]
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change lan.host config <interface> <host id> <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.lan.lanhost_write_parms)
        else:
            host_id = cmdline[0]
            del cmdline[0]
            if cmdline == []:
                print('Freebox command line tool: {0} change lan.host config <interface> <host id> <command args...>'.format(prg))
                print('Available command args: [<parmameter>=<value> ...]')
                printParms(fbx.lan.lanhost_write_parms)
            else:
                conf = fbx.encodeJSON(fbx.lan.lanhost_write_parms, cmdline)
                if conf == None:
                    print('Freebox command line tool: {0} change lan.host config <interface> <host id> <command args...>'.format(prg))
                    print('Available command args: [<parmameter>=<value> ...]')
                    printParms(fbx.lan.lanhost_write_parms)
                else:
                    try: fbx_data = fbx.lan.set_host_information(host_id, conf, interf)
                    except: print('Invalid parms')
                    else:
                        print(f"#Host config changed")
                        printList(fbx_data)

def fbx_change_lanhost_wol():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change lan.host wol <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.lan.wol_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.lan.wol_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change lan.host wol <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.lan.wol_write_parms)
        else:
            try: fbx_data = fbx.lan.wol(conf)
            except: print('Invalid parms')
            else:
                print(f"#Wake on LAN send")
                printList(fbx_data)

def fbx_change_lanhost():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change lan.host <command args...>'.format(prg))
        print('Available command args: config, wol')
    elif cmdline[0] == 'config': fbx_change_lanhost_config()
    elif cmdline[0] == 'wol': fbx_change_lanhost_wol()
    else:
        print('Freebox command line tool: {0} change lan.host <command args...>'.format(prg))
        print('Available command args: config, wol')

def fbx_change_connection_config():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change connection config <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.connection.configuration_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.connection.configuration_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change connection config <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.connection.configuration_write_parms)
        else:
            try: fbx_data = fbx.connection.set_config(conf)
            except: print('Invalid parms')
            else:
                print(f"#Connection config changed")
                printList(fbx_data)

def fbx_change_connection_ipv6():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change connection ipv6 <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.connection.ipv6_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.connection.ipv6_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change connection ipv6 <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.connection.ipv6_write_parms)
        else:
            try: fbx_data = fbx.connection.set_ipv6_config(conf)
            except: print('Invalid parms')
            else:
                print(f"#IPv6 config changed")
                printList(fbx_data)

def fbx_change_connection():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change connection <command args...>'.format(prg))
        print('Available command args: config, ipv6')
    elif cmdline[0] == 'config': fbx_change_connection_config()
    elif cmdline[0] == 'ipv6': fbx_change_connection_ipv6()
    else:
        print('Freebox command line tool: {0} change connection <command args...>'.format(prg))
        print('Available command args: config, ipv6')

def fbx_change_dyndns_config(dyndns_service, parms):
    global fbx
    conf = fbx.encodeJSON(fbx.connection.ddns_write_parms, cmdline)
    if conf == None:
        print('Freebox command line tool: {0} change dyndns.config <command args...> '.format(prg))
        print('Available command args: <dyndns service (dyndns, ovh, noip)> [<parmameter>=<value> ...]')
        printParms(fbx.connection.ddns_write_parms)
    else:
        try: fbx_data = fbx.connection.set_dyndns_config(parms, dyndns_service)
        except: print(f"#DynDNS config for service {dyndns_service}\nService not used or bad parameters")
        else:
            print(f"#DynDNS config for service {dyndns_service} changed")
            printList(fbx_data)

def fbx_change_dyndns():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change dyndns.config <command args...> '.format(prg))
        print('Available command args: <dyndns service (dyndns, ovh, noip)> [<parmameter>=<value> ...]')
    else:
        provider = cmdline[0]
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change dyndns.config <command args...> '.format(prg))
            print('Available command args: <dyndns service (dyndns, ovh, noip)> [<parmameter>=<value> ...]')
        else: fbx_change_dyndns_config(provider, cmdline[0])

def fbx_change_fw_forward():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change fw forward <command args...>'.format(prg))
        print('Available command args: <id> [<parmameter>=<value> ...]')
        printParms(fbx.fw.forwarding_write_parms)
    else:
        portid = cmdline[0]
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change fw forward <command args...>'.format(prg))
            print('Available command args: <id> [<parmameter>=<value> ...]')
            printParms(fbx.fw.forwarding_write_parms)
        else:
            conf = fbx.encodeJSON(fbx.fw.forwarding_write_parms, cmdline)
            if conf == None:
                print('Freebox command line tool: {0} change fw forward <command args...>'.format(prg))
                print('Available command args: <id> [<parmameter>=<value> ...]')
                printParms(fbx.fw.forwarding_write_parms)
            else:
                try: fbx_data = fbx.fw.update_forward(portid, conf)
                except: print('Invalid parms')
                else:
                    print(f"#Port forwarding {portid} config changed")
                    printList(fbx_data)

def fbx_change_fw_incoming():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change fw incoming <command args...>'.format(prg))
        print('Available command args: <id> [<parmameter>=<value> ...]')
        printParms(fbx.fw.incoming_write_parms)
    else:
        portid = cmdline[0]
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change fw incoming <command args...>'.format(prg))
            print('Available command args: <id> [<parmameter>=<value> ...]')
            printParms(fbx.fw.incoming_write_parms)
        else:
            conf = fbx.encodeJSON(fbx.fw.incoming_write_parms, cmdline)
            if conf == None:
                print('Freebox command line tool: {0} change fw incoming <command args...>'.format(prg))
                print('Available command args: <id> [<parmameter>=<value> ...]')
                printParms(fbx.fw.incoming_write_parms)
            else:
                try: fbx_data = fbx.fw.set_incoming_port(portid, conf)
                except: print('Invalid parms')
                else:
                    print(f"#Incoming port {portid} config changed")
                    printList(fbx_data)

def fbx_change_fw_dmz():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change fw dmz <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.fw.dmz_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.fw.dmz_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change fw dmz <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.fw.dmz_write_parms)
        else:
            try: fbx_data = fbx.fw.set_dmz_config(conf)
            except: print('Invalid parms')
            else:
                print(f"#DMZ config changed")
                printList(fbx_data)

def fbx_change_fw():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change fw <command args...> '.format(prg))
        print('Available command args: dmz, forward, incoming')
    elif cmdline[0] == 'dmz': fbx_change_fw_dmz()
    elif cmdline[0] == 'forward': fbx_change_fw_forward()
    elif cmdline[0] == 'incoming': fbx_change_fw_incoming()
    else:
        print('Freebox command line tool: {0} change fw <command args...> '.format(prg))
        print('Available command args: dmz, forward, incoming')

def fbx_change_disk():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change disk <command args...> '.format(prg))
        print('Available command args: eject <id>, format <id> <label> <file system> <table>, mount <id>')
    elif cmdline[0] == 'eject':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change disk <command args...> '.format(prg))
            print('Available command args: eject <id>, format <id> <label> <file system> <table>, mount <id>')
        else:
            try: fbx_data = fbx.storage.eject_disk(cmdline[0])
            except: print('Invalid parms')
            else:
                print(f"#Disk {cmdline[0]} ejected")
                printList(fbx_data)
    elif cmdline[0] == 'mount':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change disk <command args...> '.format(prg))
            print('Available command args: eject <id>, format <label> <id> <file system> <table>, mount <id>')
        else:
            try: fbx_data = fbx.storage.mount_disk(cmdline[0])
            except: print('Invalid parms')
            else:
                print(f"#Disk {cmdline[0]} mounted")
                printList(fbx_data)
    elif cmdline[0] == 'format':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change disk <command args...> '.format(prg))
            print('Available command args: eject <id>, format <id> <label> <file system> <table>, mount <id>')
        else:
            dsk = cmdline[0]
            del cmdline[0]
            if cmdline == []:
                print('Freebox command line tool: {0} change disk <command args...> '.format(prg))
                print('Available command args: eject <id>, format <id> <label> <file system> <table>, mount <id>')
            else:
                lbl = cmdline[0]
                del cmdline[0]
                if cmdline == []:
                    print('Freebox command line tool: {0} change disk <command args...> '.format(prg))
                    print('Available command args: eject <id>, format <id> <label> <file system> <table>, mount <id>')
                else:
                    fs = cmdline[0]
                    del cmdline[0]
                    if cmdline == []:
                        print('Freebox command line tool: {0} change disk <command args...> '.format(prg))
                        print('Available command args: eject <id>, format <id> <label> <file system> <table>, mount <id>')
                    else:
                        try: fbx_data = fbx.storage.format_disk(dsk, lbl, fs, cmdline[0])
                        except: print('Invalid parms')
                        else:
                            print(f"#Disk {dsk} formated")
                            printList(fbx_data)
    else:
            print('Freebox command line tool: {0} change disk <command args...> '.format(prg))
            print('Available command args: eject <id>, format <id> <file system> <table>, mount <id>')

def fbx_change_partition():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change partition <command args...> '.format(prg))
        print('Available command args: check <id>, mount <id>, repair <id>, umount <id>')
    elif cmdline[0] == 'check':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change partition <command args...> '.format(prg))
            print('Available command args: check <id>, mount <id>, repair <id>, umount <id>')
        else:
            try: fbx_data = fbx.storage.check_partition(cmdline[0], False)
            except: print('Invalid parms')
            else:
                print(f"#Partition {cmdline[0]} checked")
                printList(fbx_data)
    elif cmdline[0] == 'mount':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change partition <command args...> '.format(prg))
            print('Available command args: check <id>, mount <id>, repair <id>, umount <id>')
        else:
            try: fbx_data = fbx.storage.mount_partition(cmdline[0])
            except: print('Invalid parms')
            else:
                print(f"#Partition {cmdline[0]} mounted")
                printList(fbx_data)
    elif cmdline[0] == 'repair':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change partition <command args...> '.format(prg))
            print('Available command args: check <id>, mount <id>, repair <id>, umount <id>')
        else:
            try: fbx_data = fbx.storage.check_partition(cmdline[0], True)
            except: print('Invalid parms')
            else:
                print(f"#Partition {cmdline[0]} checked & may be repaired")
                printList(fbx_data)
    elif cmdline[0] == 'umount':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change partition <command args...> '.format(prg))
            print('Available command args: check <id>, mount <id>, repair <id>, umount <id>')
        else:
            try: fbx_data = fbx.storage.umount_partition(cmdline[0])
            except: print('Invalid parms')
            else:
                print(f"#Partition {cmdline[0]} unmounted")
                printList(fbx_data)
    else:
        print('Freebox command line tool: {0} change partition <command args...> '.format(prg))
        print('Available command args: check <id>, mount <id>, repair <id>, umount <id>')

def fbx_change_switch():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change switch.port <command args...>'.format(prg))
        print('Available command args: <id> [<parmameter>=<value> ...]')
        printParms(fbx.switch.switch_port_write_parms)
    else:
        port_id = cmdline[0]
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change switch.port <command args...>'.format(prg))
            print('Available command args: <id> [<parmameter>=<value> ...]')
            printParms(fbx.switch.switch_port_write_parms)
        else:
            conf = fbx.encodeJSON(fbx.switch.switch_port_write_parms, cmdline)
            if conf == None:
                print('Freebox command line tool: {0} change connection config <command args...>'.format(prg))
                print('Available command args: <id> [<parmameter>=<value> ...]')
                printParms(fbx.switch.switch_port_write_parms)
            else:
                try: fbx_data = fbx.switch.set_port_conf(port_id, conf)
                except: print('Invalid parms')
                else:
                    print(f"#Switch port {port_id} config changed")
                    printList(fbx_data)

def fbx_change_rss_mode(feed, mode):
    global fbx
    info = 'disabled'
    if mode: info = 'enabled'
    try: fbx_data = fbx.downloads.set_rssfeed_mode(feed, mode)
    except: print('Invalid parms')
    else:
        print(f"#Auto download for RSS feed {feed} {info}")
        printList(fbx_data)

def fbx_change_rss_start(feed, item):
    global fbx
    try: fbx_data = fbx.downloads.set_rssfeed_download_item(feed, item)
    except: print('Invalid parms')
    else:
        print(f"#Item {item} for RSS feed {feed} enqueued")
        printList(fbx_data)

def fbx_change_rss_read(feed, item, mode):
    global fbx
    info = 'marked as unread'
    if mode: info = 'marked as read'
    try: fbx_data = fbx.downloads.mark_rssfeed_item(feed, item, mode)
    except: print('Invalid parms')
    else:
        print(f"#Item {item} for RSS feed {feed} {info}")
        printList(fbx_data)

def fbx_change_rss_reada(feed):
    global fbx
    try: fbx_data = fbx.downloads.set_rssfeed_mark_all_items_as_read(feed)
    except: print('Invalid parms')
    else:
        print(f"#All items for RSS feed {feed} marked as read")
        printList(fbx_data)

def fbx_change_rss_rfresh(feed):
    global fbx
    try: fbx_data = fbx.downloads.refresh_rssfeed(feed)
    except: print('Invalid parms')
    else:
        print(f"#RSS feed {feed} refreshed")
        printList(fbx_data)

def fbx_change_rss_rfresha():
    global fbx
    try: fbx_data = fbx.downloads.refresh_rssfeeds()
    except: print('Unable to refresh')
    else:
        print(f"#All RSS feeds refreshed")
        printList(fbx_data)

def fbx_change_rss():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change download.rss <command args...>'.format(prg))
        print('Available command args: auto <id>, enqueue <id> <item>, noauto <id>, read <id> <item>, read.all <id>, refresh <id>, refresh.all, unread <id> <item>')
    elif cmdline[0] == 'auto':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change download.rss <command args...>'.format(prg))
            print('Available command args: auto <id>, enqueue <id> <item>, noauto <id>, read <id> <item>, read.all <id>, refresh <id>, refresh.all, unread <id> <item>')
        else: fbx_change_rss_mode(cmdline[0], True)
    elif cmdline[0] == 'enqueue':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change download.rss <command args...>'.format(prg))
            print('Available command args: auto <id>, enqueue <id> <item>, noauto <id>, read <id> <item>, read.all <id>, refresh <id>, refresh.all, unread <id> <item>')
        else:
            feed_id = cmdline[0]
            del cmdline[0]
            if cmdline == []:
                print('Freebox command line tool: {0} change download.rss <command args...>'.format(prg))
                print('Available command args: auto <id>, enqueue <id> <item>, noauto <id>, read <id> <item>, read.all <id>, refresh <id>, refresh.all, unread <id> <item>')
            else: fbx_change_rss_start(feed_id, cmdline[0])           
    elif cmdline[0] == 'noauto':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change download.rss <command args...>'.format(prg))
            print('Available command args: auto <id>, enqueue <id> <item>, noauto <id>, read <id> <item>, read.all <id>, refresh <id>, refresh.all, unread <id> <item>')
        else: fbx_change_rss_mode(cmdline[0], False)
    elif cmdline[0] == 'read':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change download.rss <command args...>'.format(prg))
            print('Available command args: auto <id>, enqueue <id> <item>, noauto <id>, read <id> <item>, read.all <id>, refresh <id>, refresh.all, unread <id> <item>')
        else:
            feed_id = cmdline[0]
            del cmdline[0]
            if cmdline == []:
                print('Freebox command line tool: {0} change download.rss <command args...>'.format(prg))
                print('Available command args: auto <id>, enqueue <id> <item>, noauto <id>, read <id> <item>, read.all <id>, refresh <id>, refresh.all, unread <id> <item>')
            else: fbx_change_rss_read(feed_id, cmdline[0], True)           
    elif cmdline[0] == 'unread':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change download.rss <command args...>'.format(prg))
            print('Available command args: auto <id>, enqueue <id> <item>, noauto <id>, read <id> <item>, read.all <id>, refresh <id>, refresh.all, unread <id> <item>')
        else:
            feed_id = cmdline[0]
            del cmdline[0]
            if cmdline == []:
                print('Freebox command line tool: {0} change download.rss <command args...>'.format(prg))
                print('Available command args: auto <id>, enqueue <id> <item>, noauto <id>, read <id> <item>, read.all <id>, refresh <id>, refresh.all, unread <id> <item>')
            else: fbx_change_rss_read(feed_id, cmdline[0], False)           
    elif cmdline[0] == 'read.all':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change download.rss <command args...>'.format(prg))
            print('Available command args: auto <id>, enqueue <id> <item>, noauto <id>, read <id> <item>, read.all <id>, refresh <id>, refresh.all, unread <id> <item>')
        else: fbx_change_rss_reada(cmdline[0])
    elif cmdline[0] == 'refresh':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change download.rss <command args...>'.format(prg))
            print('Available command args: auto <id>, enqueue <id> <item>, noauto <id>, read <id> <item>, read.all <id>, refresh <id>, refresh.all, unread <id> <item>')
        else: fbx_change_rss_rfresh(cmdline[0])
    elif cmdline[0] == 'refresh.all': fbx_change_rss_rfresha()
    else:
        print('Freebox command line tool: {0} change download.rss <command args...>'.format(prg))
        print('Available command args: auto <id>, enqueue <id> <item>, noauto <id>, read <id> <item>, read.all <id>, refresh <id>, refresh.all, unread <id> <item>')

def fbx_change_wifi_ap():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change wifi access <command args...>'.format(prg))
        print('Available command args: config <id> [<parmameter>=<value> ...], ht <id> [<parmameter>=<value> ...]')
    elif cmdline[0] == 'config':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change wifi access <command args...>'.format(prg))
            print('Available command args: config <id> [<parmameter>=<value> ...], ht <id> [<parmameter>=<value> ...]')
            printParms(fbx.wifi.ap_config_write_parms)
        else:
            ap_id = cmdline[0]
            del cmdline[0]
            conf = fbx.encodeJSON(fbx.wifi.ap_config_write_parms, cmdline)
            if conf == None:
                print('Freebox command line tool: {0} change wifi access <command args...>'.format(prg))
                print('Available command args: config <id> [<parmameter>=<value> ...], ht <id> [<parmameter>=<value> ...]')
                printParms(fbx.wifi.ap_config_write_parms)
            else:
                try: fbx_data = fbx.wifi.set_ap(ap_id, conf)
                except: print('Invalid parms')
                else:
                    print(f"#Access point {ap_id} config changed")
                    printList(fbx_data)
    elif cmdline[0] == 'ht':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change wifi access <command args...>'.format(prg))
            print('Available command args: config <id> [<parmameter>=<value> ...], ht <id> [<parmameter>=<value> ...]')
            printParms(fbx.wifi.apht_config_write_parms)
        else:
            ap_id = cmdline[0]
            del cmdline[0]
            conf = fbx.encodeJSON(fbx.wifi.apht_config_write_parms, cmdline)
            if conf == None:
                print('Freebox command line tool: {0} change wifi access <command args...>'.format(prg))
                print('Available command args: config <id> [<parmameter>=<value> ...], ht <id> [<parmameter>=<value> ...]')
                printParms(fbx.wifi.apht_config_write_parms)
            else:
                try: fbx_data = fbx.wifi.set_ap(ap_id, { 'ht': conf })
                except: print('Invalid parms')
                else:
                    print(f"#Access point {ap_id} config changed")
                    printList(fbx_data)
    else:
        print('Freebox command line tool: {0} change wifi access <command args...>'.format(prg))
        print('Available command args: config <id> [<parmameter>=<value> ...], ht <id> [<parmameter>=<value> ...]')

def fbx_change_wifi_bss():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change wifi bss <command args...>'.format(prg))
        print('Available command args: shared <id> [<parmameter>=<value> ...], specific <id> [<parmameter>=<value> ...]')
        printParms(fbx.wifi.bss_config_write_parms)
    elif cmdline[0] == 'shared':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change wifi bss <command args...>'.format(prg))
            print('Available command args: shared <id> [<parmameter>=<value> ...], specific <id> [<parmameter>=<value> ...]')
            printParms(fbx.wifi.bss_config_write_parms)
        else:
            bss_id = cmdline[0]
            del cmdline[0]
            conf = fbx.encodeJSON(fbx.wifi.bss_config_write_parms, cmdline)
            if conf == None:
                print('Freebox command line tool: {0} change wifi bss <command args...>'.format(prg))
                print('Available command args: shared <id> [<parmameter>=<value> ...], specific <id> [<parmameter>=<value> ...]')
                printParms(fbx.wifi.bss_config_write_parms)
            else:
                try: fbx_data = fbx.wifi.set_bss(bss_id, conf, True)
                except: print('Invalid parms')
                else:
                    print(f"#BSS {bss_id} config changed")
                    printList(fbx_data)
    elif cmdline[0] == 'specific':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change wifi bss <command args...>'.format(prg))
            print('Available command args: shared <id> [<parmameter>=<value> ...], specific <id> [<parmameter>=<value> ...]')
            printParms(fbx.wifi.bss_config_write_parms)
        else:
            bss_id = cmdline[0]
            del cmdline[0]
            conf = fbx.encodeJSON(fbx.wifi.bss_config_write_parms, cmdline)
            if conf == None:
                print('Freebox command line tool: {0} change wifi bss <command args...>'.format(prg))
                print('Available command args: shared <id> [<parmameter>=<value> ...], specific <id> [<parmameter>=<value> ...]')
                printParms(fbx.wifi.bss_config_write_parms)
            else:
                try: fbx_data = fbx.wifi.set_bss(bss_id, conf, False)
                except: print('Invalid parms')
                else:
                    print(f"#BSS {bss_id} config changed")
                    printList(fbx_data)
    else:
        print('Freebox command line tool: {0} change wifi bss <command args...>'.format(prg))
        print('Available command args: shared <id> [<parmameter>=<value> ...], specific <id> [<parmameter>=<value> ...]')
        printParms(fbx.wifi.bss_config_write_parms)

def fbx_change_wifi_config():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change wifi config <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.wifi.wifi_config_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.wifi.wifi_config_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change wifi config <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.wifi.wifi_config_write_parms)
        else:
            try: fbx_data = fbx.wifi.set_global_config(conf)
            except: print('Invalid parms')
            else:
                print(f"#Wifi global config changed")
                printList(fbx_data)

def fbx_change_wifi_filter():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change wifi filter <command args...>'.format(prg))
        print('Available command args: <id> [<parmameter>=<value> ...]')
        printParms(fbx.wifi.mac_filter_write_parms)
    else:
        filter_id = cmdline[0]
        del cmdline[0]
        conf = fbx.encodeJSON(fbx.wifi.mac_filter_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change wifi filter <command args...>'.format(prg))
            print('Available command args: <id> [<parmameter>=<value> ...]')
            printParms(fbx.wifi.mac_filter_write_parms)
        else:
            try: fbx_data = fbx.wifi.set_wifi_mac_filter(filter_id, conf)
            except: print('Invalid parms')
            else:
                print(f"#MAC filter {filter_id} changed")
                printList(fbx_data)

def fbx_change_wifi_plan():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change wifi planning <command args...>'.format(prg))
        print('Available command args: disable, enable [<parmameter>=<value> ...]')
        printParms(fbx.wifi.planning_write_parms)
    elif cmdline[0] == 'enable':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change wifi planning <command args...>'.format(prg))
            print('Available command args: disable, enable [<parmameter>=<value> ...]')
            printParms(fbx.wifi.planning_write_parms)
        else:
            del cmdline[0]
            conf = fbx.encodeJSON(fbx.wifi.planning_write_parms, cmdline)
            if conf == None:
                print('Freebox command line tool: {0} change wifi planning <command args...>'.format(prg))
                print('Available command args: disable, enable [<parmameter>=<value> ...]')
                printParms(fbx.wifi.planning_write_parms)
            else:
                try: fbx_data = fbx.wifi.set_wifi_planning(True, conf)
                except: print('Invalid parms')
                else:
                    print(f"#Wifi planning changed changed")
                    printList(fbx_data)
    elif cmdline[0] == 'disable':
        try: fbx_data = fbx.wifi.set_wifi_planning(False)
        except: print('Invalid parms')
        else:
            print(f"#Wifi planning disabled")
            printList(fbx_data)
    else:
        print('Freebox command line tool: {0} change wifi planning <command args...>'.format(prg))
        print('Available command args: disable, enable [<parmameter>=<value> ...]')
        printParms(fbx.wifi.planning_write_parms)

def fbx_change_wifi_scan():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change wifi scan <command args...>'.format(prg))
        print('Available command args: <access point id>')
    else:
        try: fbx_data = fbx.wifi.start_wifi_access_point_neighbors_scan(cmdline[0])
        except: print('Invalid parms')
        else:
            print(f"#Wifi scan on access point {cmdline[0]} started")
            printList(fbx_data)

def fbx_change_wifi_wps():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change wifi wps <command args...>'.format(prg))
        print('Available command args: disable, enable, start <bss id>, stop <session id>')
    elif cmdline[0] == 'start':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change wifi wps <command args...>'.format(prg))
            print('Available command args: disable, enable, start <bss id>, stop <session id>')
        else:
            try: fbx_data = fbx.wifi.start_wps_session(cmdline[0])
            except: print('Invalid parms')
            else:
                print(f"#WPS started on BSS {cmdline[0]}")
                printList(fbx_data)
    elif cmdline[0] == 'stop':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change wifi wps <command args...>'.format(prg))
            print('Available command args: disable, enable, start <bss id>, stop <session id>')
        else:
            try: fbx_data = fbx.wifi.stop_wps_session(cmdline[0])
            except: print('Invalid parms')
            else:
                print(f"#WPS session {cmdline[0]} stopped")
                printList(fbx_data)
    elif cmdline[0] == 'disable':
        try: fbx_data = fbx.wifi.set_wps_status(False)
        except: print('Invalid parms')
        else:
            print(f"#WPS disabled")
            printList(fbx_data)
    elif cmdline[0] == 'enable':
        try: fbx_data = fbx.wifi.set_wps_status(True)
        except: print('Invalid parms')
        else:
            print(f"#WPS enabled")
            printList(fbx_data)
    else:
        print('Freebox command line tool: {0} change wifi wps <command args...>'.format(prg))
        print('Available command args: disable, enable, start <bss id>, stop <session id>')

def fbx_change_wifi():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change wifi <command args...> '.format(prg))
        print('Available command args: access, bss, config, filter, planning, reset, scan, wps')
    elif cmdline[0] == 'access': fbx_change_wifi_ap()
    elif cmdline[0] == 'bss': fbx_change_wifi_bss()
    elif cmdline[0] == 'config': fbx_change_wifi_config()
    elif cmdline[0] == 'filter': fbx_change_wifi_filter()
    elif cmdline[0] == 'planning': fbx_change_wifi_plan()
    elif cmdline[0] == 'reset': fbx_change_wifi_reset()
    elif cmdline[0] == 'scan': fbx_change_wifi_scan()
    elif cmdline[0] == 'wps': fbx_change_wifi_wps()
    else:
        print('Freebox command line tool: {0} change wifi <command args...> '.format(prg))
        print('Available command args: access, bss, config, filter, planning, reset, scan, wps')

def fbx_change_vpnsrv_close():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change vpn.server close <command args...>'.format(prg))
        print('Available command args: <connection id>')
    else:
        try: fbx_data = fbx.vpn.close_server_connection(cmdline[0])
        except: print('Invalid parms')
        else:
            print(f"#VPN Server connection {cmdline[0]} closed")
            printList(fbx_data)

def fbx_change_vpnsrv_glob():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change vpn.server config.global <command args...>'.format(prg))
        print('Available command args: <vpn server id> [<parmameter>=<value> ...]')
        printParms(fbx.vpn.vpnserver_global_write_parms)
    else:
        vpn_id = cmdline[0]
        del cmdline[0]
        conf = fbx.encodeJSON(fbx.vpn.vpnserver_global_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change vpn.server config.global <command args...>'.format(prg))
            print('Available command args: <vpn server id> [<parmameter>=<value> ...]')
            printParms(fbx.vpn.vpnserver_global_write_parms)
        else:
            try: fbx_data = fbx.vpn.set_server_config(vpn_id, conf)
            except: print('Invalid parms')
            else:
                print(f"#VPN Server {vpn_id} config changed")
                printList(fbx_data)

def fbx_change_vpnsrv_spec():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change vpn.server config.spec <command args...>'.format(prg))
        print('Available command args: <vpn server id> [<parmameter>=<value> ...]')
    else:
        vpn_id = cmdline[0]
        del cmdline[0]
        try: vpnconf = fbx.vpn.get_server_config(vpn_id)
        except: parms = None
        else:
            if vpnconf['type'] == 'pptp': parms = fbx.vpn.vpnserver_pptp_write_parms
            elif vpnconf['type'] == 'ipsec': parms = fbx.vpn.vpnserver_ipsec_write_parms
            elif vpnconf['type'] == 'openvpn': parms = fbx.vpn.vpnserver_open_write_parms
            elif vpnconf['type'] == 'wireguard': parms = fbx.vpn.vpnserver_wireguard_write_parms
            else: parms = None
        if parms == None:
            print('Freebox command line tool: {0} change vpn.server config.spec <command args...>'.format(prg))
            print('Available command args: <vpn server id> [<parmameter>=<value> ...]')
        else:
            conf = fbx.encodeJSON(parms, cmdline)
            if conf == None:
                print('Freebox command line tool: {0} change vpn.server config.spec <command args...>'.format(prg))
                print('Available command args: <vpn server id> [<parmameter>=<value> ...]')
                printParms(parms)
            else:
                try: fbx_data = fbx.vpn.set_server_config(vpn_id, spec_conf = conf)
                except: print('Invalid parms')
                else:
                    print(f"#VPN Server {vpn_id} config changed")
                    printList(fbx_data)

def fbx_change_vpnsrv_auth():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change vpn.server config.auth <command args...>'.format(prg))
        print('Available command args: <vpn server id> [<parmameter>=<value> ...]')
        printParms(fbx.vpn.pptp_auths_write_parms)
    else:
        vpn_id = cmdline[0]
        del cmdline[0]
        conf = fbx.encodeJSON(fbx.vpn.pptp_auths_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change vpn.server config.auth <command args...>'.format(prg))
            print('Available command args: <vpn server id> [<parmameter>=<value> ...]')
            printParms(fbx.vpn.pptp_auths_write_parms)
        else:
            try: fbx_data = fbx.vpn.set_server_pptp_auth(vpn_id, conf)
            except: print('Invalid parms')
            else:
                print(f"#VPN Server {vpn_id} config changed")
                printList(fbx_data)

def fbx_change_vpnsrv():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change vpn.server <command args...> '.format(prg))
        print('Available command args: close, config.auth, config.global, config.spec')
    elif cmdline[0] == 'close': fbx_change_vpnsrv_close()
    elif cmdline[0] == 'config.global': fbx_change_vpnsrv_glob()
    elif cmdline[0] == 'config.spec': fbx_change_vpnsrv_spec()
    elif cmdline[0] == 'config.auth': fbx_change_vpnsrv_auth()
    else:
        print('Freebox command line tool: {0} change vpn.server <command args...> '.format(prg))
        print('Available command args: close, config.auth, config.global, config.spec')

def fbx_change_vpnclt_sw():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change vpn.client switch <command args...>'.format(prg))
        print('Available command args: <vpn client id>')
    else:
        try: fbx_data = fbx.vpn.set_client_active(cmdline[0])
        except: print('Invalid parms')
        else:
            print(f"#VPN Client {cmdline[0]} is now active")
            printList(fbx_data)

def fbx_change_vpnclt_conf():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change vpn.client config <command args...>'.format(prg))
        print('Available command args: <vpn client id> <description> [<parmameter>=<value> ...]')
    else:
        vpn_id = cmdline[0]
        del cmdline[0]
        try: vpnconf = fbx.vpn.get_client_config(vpn_id)
        except: parms = None
        else:
            if vpnconf['type'] == 'pptp': parms = fbx.vpn.vpnclient_pptp_write_parms
            elif vpnconf['type'] == 'openvpn': parms = fbx.vpn.vpnclient_open_write_parms
            else: parms = None
        if parms == None:
            print('Freebox command line tool: {0} change vpn.client config <command args...>'.format(prg))
            print('Available command args: <vpn client id> <description> [<parmameter>=<value> ...]')
        else:
            if cmdline == []:
                print('Freebox command line tool: {0} change vpn.client config <command args...>'.format(prg))
                print('Available command args: <vpn client id> <description> [<parmameter>=<value> ...]')
                printParms(parms)
            else:   
                desc = cmdline[0]
                del cmdline[0]
                conf = fbx.encodeJSON(parms, cmdline)
                if conf == None:
                    print('Freebox command line tool: {0} change vpn.client config <command args...>'.format(prg))
                    print('Available command args: <vpn client id> <description> [<parmameter>=<value> ...]')
                    printParms(parms)
                else:
                    if vpnconf['type'] == 'openvpn' and 'config_file' in conf: conf['config_file'] = get_config_from_file(conf['config_file'])
                    try: fbx_data = fbx.vpn.set_client(vpn_id, conf, desc)
                    except: print('Invalid parms')
                    else:
                        print(f"#VPN Client {vpn_id} config changed")
                        printList(fbx_data)

def fbx_change_vpnclt_auth():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change vpn.client config.auth <command args...>'.format(prg))
        print('Available command args: <vpn client id> [<parmameter>=<value> ...]')
        printParms(fbx.vpn.pptp_all_auths_write_parms)
    else:
        vpn_id = cmdline[0]
        del cmdline[0]
        conf = fbx.encodeJSON(fbx.vpn.pptp_all_auths_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change vpn.client config.auth <command args...>'.format(prg))
            print('Available command args: <vpn client id> [<parmameter>=<value> ...]')
            printParms(fbx.vpn.pptp_all_auths_write_parms)
        else:
            try: fbx_data = fbx.vpn.set_client_pptp_auth(vpn_id, conf)
            except: print('Invalid parms')
            else:
                print(f"#VPN Client {vpn_id} config changed")
                printList(fbx_data)

def fbx_change_vpnclt_slv(slave):
    global fbx
    try: fbx_data = fbx.vpn.set_slavery(slave)
    except: print('Invalid parms')
    else:
        print(f"#VPN Client slavery is now {slave}")
        printList(fbx_data)

def fbx_change_vpnclt():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change vpn.client <command args...> '.format(prg))
        print('Available command args: config, config.auth, enslave, free, switch')
    elif cmdline[0] == 'switch': fbx_change_vpnclt_sw()
    elif cmdline[0] == 'config': fbx_change_vpnclt_conf()
    elif cmdline[0] == 'config.auth': fbx_change_vpnclt_auth()
    elif cmdline[0] == 'enslave': fbx_change_vpnclt_slv(True)
    elif cmdline[0] == 'free': fbx_change_vpnclt_slv(False)
    else:
        print('Freebox command line tool: {0} change vpn.client <command args...> '.format(prg))
        print('Available command args: config.auth, config, enslave, free, switch')

def fbx_change_profile_rule():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change profile rule <command args...>'.format(prg))
        print('Available command args: <profile id> <rule id> [<parmameter>=<value> ...]')
        printParms(fbx.profile.rule_write_parms)
    else:
        prof_id = cmdline[0]
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change profile rule <command args...>'.format(prg))
            print('Available command args: <profile id> <rule id> [<parmameter>=<value> ...]')
            printParms(fbx.profile.rule_write_parms)
        else:
            rul_id = cmdline[0]
            del cmdline[0]
            conf = fbx.encodeJSON(fbx.profile.rule_write_parms, cmdline)
            if conf == None:
                print('Freebox command line tool: {0} change profile rule <command args...>'.format(prg))
                print('Available command args: <profile id> <rule id> [<parmameter>=<value> ...]')
                printParms(fbx.profile.rule_write_parms)
            else:
                try: fbx_data = fbx.profile.set_netcontrol_rule(prof_id, rul_id, conf)
                except: print('Invalid parms')
                else:
                    print(f"#Rule {rul_id} for profile {prof_id} changed")
                    printList(fbx_data)

def fbx_change_profile_ctrl():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change profile control <command args...>'.format(prg))
        print('Available command args: <profile id> [<parmameter>=<value> ...]')
        printParms(fbx.profile.netcontrol_write_parms)
    else:
        prof_id = cmdline[0]
        del cmdline[0]
        conf = fbx.encodeJSON(fbx.profile.netcontrol_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} change control <command args...>'.format(prg))
            print('Available command args: <profile id> [<parmameter>=<value> ...]')
            printParms(fbx.profile.netcontrol_write_parms)
        else:
            try: fbx_data = fbx.profile.set_netcontrol(prof_id, conf)
            except: print('Invalid parms')
            else:
                print(f"#Network control for profile {prof_id} changed")
                printList(fbx_data)

def fbx_change_profile_prof():
    global fbx
    global cmdline
    prof_id = cmdline[0]
    del cmdline[0]
    conf = fbx.encodeJSON(fbx.profile.profile_write_parms, cmdline)
    if conf == None:
        print('Freebox command line tool: {0} change profile <profile id> <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.profile.profile_write_parms)
    else:
        try: fbx_data = fbx.profile.set_profile(prof_id, conf)
        except: print('Invalid parms')
        else:
            print(f"#Profile {prof_id} changed")
            printList(fbx_data)

def fbx_change_profile_over():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change profile override <command args...>'.format(prg))
        print('Available command args: <profile id> [time]')
    else:
        prof_id = cmdline[0]
        del cmdline[0]
        if cmdline == []: time=0
        else: time=int(cmdline[0])
        try: fbx_data = fbx.profile.override(prof_id, time)
        except: print('Invalid parms')
        else:
            print(f"#Profile {prof_id} overrided")
            printList(fbx_data)

def fbx_change_profile_bck():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change profile back <command args...>'.format(prg))
        print('Available command args: <profile id>')
    else:
        try: fbx_data = fbx.profile.back(cmdline[0])
        except: print('Invalid parms')
        else:
            print(f"#Profile {cmdline[0]} back to normal mode")
            printList(fbx_data)

def fbx_change_profile_mig():
    global fbx
    try: fbx_data = fbx.profile.migrate()
    except: print('#Profile migration refused')
    else:
        print(f"#Profile migration requested")
        printList(fbx_data)

def fbx_change_profile():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change profile <command args...> '.format(prg))
        print('Available command args: <id>, back, control, migrate, override, rule')
    elif cmdline[0] == 'back': fbx_change_profile_bck()
    elif cmdline[0] == 'override': fbx_change_profile_over()
    elif cmdline[0] == 'migrate': fbx_change_profile_mig()
    elif cmdline[0] == 'rule': fbx_change_profile_rule()
    elif cmdline[0] == 'control': fbx_change_profile_ctrl()
    else: fbx_change_profile_prof()

def fbx_change_vm_state(cmd):
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change vm {1} <command args...> '.format(prg, cmd))
        print('Available command args: <id>')
    if cmd == 'start':
        try: fbx_data = fbx.vm.start(cmdline[0])
        except: print('#Invalid id')
        else:
            print(f"#{cmd} VM {cmdline[0]} initiated")
            printList(fbx_data)
    elif cmd == 'restart':
        try: fbx_data = fbx.vm.restart(cmdline[0])
        except: print('#Invalid id')
        else:
            print(f"#{cmd} VM {cmdline[0]} initiated")
            printList(fbx_data)
    elif cmd == 'stop':
        try: fbx_data = fbx.vm.stop(cmdline[0])
        except: print('#Invalid id')
        else:
            print(f"#{cmd} VM {cmdline[0]} initiated")
            printList(fbx_data)
    elif cmd == 'halt':
        try: fbx_data = fbx.vm.halt(cmdline[0])
        except: print('#Invalid id')
        else:
            print(f"#{cmd} VM {cmdline[0]} initiated")
            printList(fbx_data)

def fbx_change_vm_rsz():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change vm resize <command args...>'.format(prg))
        print('Available command args: <VM disk file> <size> [shrink]')
    else:
        vfile = cmdline[0]
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} change vm resize <command args...>'.format(prg))
            print('Available command args: <VM disk file> <size> [shrink]')
        else:
            size = int(cmdline[0])
            del cmdline[0]
            if cmdline == []: shrk = False
            else: shrk = (cmdline[0] == 'shrink')
            try: fbx_data = fbx.vm.resize(vfile, size, shrk)
            except: print('Invalid parms')
            else:
                print(f"#VM disk file {vfile} resized to {size} bytes, shrink allowed : {shrk}")
                printList(fbx_data)

def fbx_change_vm_conf():
    global fbx
    global cmdline
    vm_id = cmdline[0]
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change vm <id> <command args...>'.format(prg))
        print('Available command args: [raw] [<parmameter>=<value> ...]')
        printParms(fbx.vm.vm_write_parms)
    else:
        if cmdline[0] == 'raw':
            ddir = False
            del cmdline[0]
        else: ddir = True
        conf = fbx.encodeJSON(fbx.vm.vm_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} add vm <id> <command args...>'.format(prg))
            print('Available command args: [raw] [<parmameter>=<value> ...]')
            printParms(fbx.vm.vm_write_parms)
        else:
            if 'cloudinit_userdata' in conf: conf['cloudinit_userdata'] = fbx.vm.decode_cloudinit_data(conf['cloudinit_userdata'])
            print(conf)
            fbx.vm.set_config(vm_id, conf)
            try: fbx_data = fbx.vm.set_config(vm_id, conf, ddir)
            except: print('Invalid parms')
            else:
                print(f"#VM {vm_id} config changed")
                printList(fbx_data)            

def fbx_change_vm_dhcp():
    global fbx
    leasings = fbx.dhcp.get_static_dhcp_lease()
    for vm in fbx.vm.get_config_all():
        for lease in leasings:
            if lease['hostname'] == vm['name'] and vm['mac'].upper() != lease['mac']:
                try: fbx.dhcp.del_static_dhcp_lease(lease['id'])
                except: print(f"Fail to remove DHCP lease for id {lease['id']}")
                else:
                    try: fbx_data = fbx.dhcp.add_static_dhcp_lease({ 'ip': lease['ip'], 'mac': vm['mac'].upper(), 'comment': lease['comment'] })
                    except: print(f"Fail to add DHCP lease for VM {vm['name']}={vm['mac']}/{lease['ip']}")
                    else:
                        print(f"#DHCP lease changed for VM {vm['name']}={vm['mac']}/{lease['ip']}")
                        printList(fbx_data)

def fbx_change_vm():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} change vm <command args...> '.format(prg))
        print('Available command args: <id>, dhcp.fixlease, halt, resize, restart, start, stop')
    elif cmdline[0] == 'start': fbx_change_vm_state(cmdline[0])
    elif cmdline[0] == 'restart': fbx_change_vm_state(cmdline[0])
    elif cmdline[0] == 'stop': fbx_change_vm_state(cmdline[0])
    elif cmdline[0] == 'halt': fbx_change_vm_state(cmdline[0])
    elif cmdline[0] == 'dhcp.fixlease': fbx_change_vm_dhcp()
    elif cmdline[0] == 'resize': fbx_change_vm_rsz()
    else: fbx_change_vm_conf()

def fbx_change():
    global fbx
    global cmdline
    if cmdline == []:
        print('Freebox command line tool: {0} change <command args...>'.format(prg))
        print('Available command args: airmedia, call, connection, contact, contact.number, dhcp, disk, download, download.rss, download.task, dyndns.config, freeplug, ftp, fw, lan, lan.host, lcd, netshare, partition, phone, profile, switch.port, system, upnpav, upnpigd, vm, vpn.client, vpn.server, wifi')
    elif cmdline[0] == 'system': fbx_change_system()
    elif cmdline[0] == 'download.task': fbx_change_dwntask()
    elif cmdline[0] == 'airmedia': fbx_change_airmedia()
    elif cmdline[0] == 'call': fbx_change_call()
    elif cmdline[0] == 'contact.number': fbx_change_contactnum()
    elif cmdline[0] == 'contact': fbx_change_contact()
    elif cmdline[0] == 'lcd': fbx_change_lcd()
    elif cmdline[0] == 'ftp': fbx_change_ftp()
    elif cmdline[0] == 'netshare': fbx_change_netshare()
    elif cmdline[0] == 'freeplug': fbx_change_freeplug()
    elif cmdline[0] == 'upnpav': fbx_change_upnpav()
    elif cmdline[0] == 'upnpigd': fbx_change_upnpigd()
    elif cmdline[0] == 'phone': fbx_change_phone()
    elif cmdline[0] == 'dhcp': fbx_change_dhcp()
    elif cmdline[0] == 'lan': fbx_change_lan()
    elif cmdline[0] == 'lan.host': fbx_change_lanhost()
    elif cmdline[0] == 'connection': fbx_change_connection()
    elif cmdline[0] == 'dyndns.config': fbx_change_dyndns()
    elif cmdline[0] == 'fw': fbx_change_fw()
    elif cmdline[0] == 'disk': fbx_change_disk()
    elif cmdline[0] == 'partition': fbx_change_partition()
    elif cmdline[0] == 'switch.port': fbx_change_switch()
    elif cmdline[0] == 'download.rss': fbx_change_rss()
    elif cmdline[0] == 'download': fbx_change_downloads()
    elif cmdline[0] == 'wifi': fbx_change_wifi()
    elif cmdline[0] == 'vpn.server': fbx_change_vpnsrv()
    elif cmdline[0] == 'vpn.client': fbx_change_vpnclt()
    elif cmdline[0] == 'profile': fbx_change_profile()
    elif cmdline[0] == 'vm': fbx_change_vm()
    else:
        print('Freebox command line tool: {0} change <command args...>'.format(prg))
        print('Available command args: airmedia, call, connection, contact, contact.number, dhcp, disk, download, download.rss, download.task, dyndns.config, freeplug, ftp, fw, lan, lan.host, lcd, netshare, partition, phone, profile, switch.port, system, upnpav, upnpigd, vm, vpn.client, vpn.server, wifi')

def fbx_del_dwntask_tsk(tsk_id, full):
    global fbx
    try: fbx_data = fbx.downloads.del_task(tsk_id, full)
    except: print('Invalid id')
    else:
        print(f"#Download task {tsk_id} deleted")
        printList(fbx_data)

def fbx_del_dwntask_blck(tsk_id, host):
    global fbx
    try: fbx_data = fbx.downloads.del_task_blackentry(tsk_id, host)
    except: print('Invalid id')
    else:
        print(f"#Host {host} removed from task {tsk_id} blacklist")
        printList(fbx_data)

def fbx_del_dwntask_blcklst(tsk_id):
    global fbx
    try: fbx_data = fbx.downloads.del_task_blacklist(tsk_id)
    except: print('Invalid id')
    else:
        print(f"#Blacklist for task {tsk_id} wiped pout")
        printList(fbx_data)

def fbx_del_dwntask_trck(tsk_id, tracker):
    global fbx
    try: fbx_data = fbx.downloads.del_task_tracker(tsk_id, tracker)
    except: print('Invalid id')
    else:
        print(f"#Tracker {tracker} removed from task {tsk_id}")
        printList(fbx_data)

def fbx_del_dwntask():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} del download.task <command args...>'.format(prg))
        print('Available command args: <task id>, blackentry <task id> <host>, blacklist <task id>, full <task id>, tracker <task id> <url>')
    elif cmdline[0] == 'full':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} del download.task <command args...>'.format(prg))
            print('Available command args: <task id>, blackentry <task id> <host>, blacklist <task id>, full <task id>, tracker <task id> <url>')
        else: fbx_del_dwntask_tsk(cmdline[0], True)
    elif cmdline[0] == 'blackentry':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} del download.task <command args...>'.format(prg))
            print('Available command args: <task id>, blackentry <task id> <host>, blacklist <task id>, full <task id>, tracker <task id> <url>')
        else:
            task_id = cmdline[0]
            del cmdline[0]
            if cmdline == []:
                print('Freebox command line tool: {0} del download.task <command args...>'.format(prg))
                print('Available command args: <task id>, blackentry <task id> <host>, blacklist <task id>, full <task id>, tracker <task id> <url>')
            else: fbx_del_dwntask_blck(task_id, cmdline[0])
    elif cmdline[0] == 'tracker':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} del download.task <command args...>'.format(prg))
            print('Available command args: <task id>, blackentry <task id> <host>, blacklist <task id>, full <task id>, tracker <task id> <url>')
        else:
            task_id = cmdline[0]
            del cmdline[0]
            if cmdline == []:
                print('Freebox command line tool: {0} del download.task <command args...>'.format(prg))
                print('Available command args: <task id>, blackentry <task id> <host>, blacklist <task id>, full <task id>, tracker <task id> <url>')
            else: fbx_del_dwntask_trck(task_id, cmdline[0])
    elif cmdline[0] == 'blacklist':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} del download.task <command args...>'.format(prg))
            print('Available command args: <task id>, blackentry <task id> <host>, blacklist <task id>, full <task id>, tracker <task id> <url>')
        else: fbx_del_dwntask_blcklst(cmdline[0])
    else: fbx_del_dwntask_tsk(cmdline[0], False)

def fbx_del_call_all():
    global fbx
    try: fbx_data = fbx.call.delete_call_list()
    except: print('An error occured')
    else:
        print('#Delete all calls')
        printList(fbx_data)

def fbx_del_call_id(call_id):
    global fbx
    try: fbx_data = fbx.call.delete_call(call_id)
    except: print('Invalid id')
    else:
        print(f"#Delete call {call_id}")
        printList(fbx_data)

def fbx_del_call():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} del call <command args...>'.format(prg))
        print('Available command args: <id>, all')
    elif cmdline[0] == 'all': fbx_del_call_all()
    else: fbx_del_call_id(cmdline[0])

def fbx_del_contactnum():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} del contact.number <command args...>'.format(prg))
        print('Available command args: <id>')
    else:
        try: fbx_data = fbx.contact.del_number(cmdline[0])
        except: print('Invalid id')
        else:
            print(f"#Contact number {cmdline[0]} deleted")
            printList(fbx_data)

def fbx_del_contact():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} del contact <command args...>'.format(prg))
        print('Available command args: <id>')
    else:
        try: fbx_data = fbx.contact.del_contact(cmdline[0])
        except: print('Invalid id')
        else:
            print(f"#Contact {cmdline[0]} deleted")
            printList(fbx_data)

def fbx_del_redir(redir_id):
    global fbx
    try: fbx_data = fbx.upnpigd.delete_redir(redir_id)
    except: print('Invalid id')
    else:
        print(f"#UPnP IGD redirection {redir_id} deleted")
        printList(fbx_data)

def fbx_del_upnpigd():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} del upnpigd <command args...>'.format(prg))
        print('Available command args: redir <id>')
    elif cmdline[0] == 'redir':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} del upnpigd <command args...>'.format(prg))
            print('Available command args: redir <id>')
        else: fbx_del_redir(cmdline[0])
    else:
        print('Freebox command line tool: {0} del upnpigd <command args...>'.format(prg))
        print('Available command args: redir <id>')        

def fbx_del_static(lease_id):
    global fbx
    try: fbx_data = fbx.dhcp.del_static_dhcp_lease(lease_id)
    except: print('Invalid id')
    else:
        print(f"#DHCP static lease {lease_id} deleted")
        printList(fbx_data)

def fbx_del_dhcp():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} del dhcp <command args...>'.format(prg))
        print('Available command args: static <id>')
    elif cmdline[0] == 'static':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} del dhcp <command args...>'.format(prg))
            print('Available command args: static <id>')
        else: fbx_del_static(cmdline[0])
    else:
        print('Freebox command line tool: {0} del dhcp <command args...>'.format(prg))
        print('Available command args: static <id>')        

def fbx_del_lanhost():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} del lan.host <command args...>'.format(prg))
        print('Available command args: <interface> <host id>')
    else:
        interf = cmdline[0]
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} del lan.host <command args...>'.format(prg))
            print('Available command args: <interface> <host id>')
        else:
            try: fbx_data = fbx.lan.delete_lan_host(cmdline[0], interf)
            except: print('Invalid host id or interface')
            else:
                print(f"#Host {cmdline[0]} deleted")
                printList(fbx_data)

def fbx_del_fw():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} del fw <command args...>'.format(prg))
        print('Available command args: forward <id>')
    elif cmdline[0] == 'forward':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} del fw <command args...>'.format(prg))
            print('Available command args: forward <id>')
        else:
            try: fbx_data = fbx.fw.delete_forward(cmdline[0])
            except: print('Invalid id')
            else:
                print(f"#Port forwarding {cmdline[0]} deleted")
                printList(fbx_data)
    else:
        print('Freebox command line tool: {0} del fw <command args...>'.format(prg))
        print('Available command args: forward <id>')

def fbx_del_rss():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} del download.rss <command args...>'.format(prg))
        print('Available command args: <id>')
    else:
        try: fbx_data = fbx.downloads.del_rssfeed(cmdline[0])
        except: print('Invalid parms')
        else:
            print(f"#RSS feed {cmdline[0]} removed")
            printList(fbx_data)

def fbx_del_wifi():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} del wifi <command args...>'.format(prg))
        print('Available command args: filter <filter id>, key <key id>, wps')
    elif cmdline[0] == 'filter':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} del wifi <command args...>'.format(prg))
            print('Available command args: filter <filter id>, key <key id>, wps')
        else:
            try: fbx_data = fbx.wifi.delete_wifi_mac_filter(cmdline[0])
            except: print('Invalid parms')
            else:
                print(f"#MAC filter {cmdline[0]} removed")
                printList(fbx_data)
    elif cmdline[0] == 'key':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} del wifi <command args...>'.format(prg))
            print('Available command args: filter <filter id>, key <key id>, wps')
        else:
            try: fbx_data = fbx.wifi.delete_wifi_custom_key(cmdline[0])
            except: print('Invalid parms')
            else:
                print(f"#Wifi custom key {cmdline[0]} removed")
                printList(fbx_data)
    elif cmdline[0] == 'wps':
        try: fbx_data = fbx.wifi.delete_wps_sessions()
        except: print('Invalid call')
        else:
            print(f"#WPS sessions wiped out")
            printList(fbx_data)
    else:
        print('Freebox command line tool: {0} del wifi <command args...>'.format(prg))
        print('Available command args: filter <filter id>, key <key id>, wps')        

def fbx_del_vpnsrv():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} del vpn.server <command args...>'.format(prg))
        print('Available command args: user <login>')
    elif cmdline[0] == 'user':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} del vpn.server <command args...>'.format(prg))
            print('Available command args: user <login>')
        else:
            try: fbx_data = fbx.vpn.del_server_user(cmdline[0])
            except: print('Invalid parms')
            else:
                print(f"#VPN Server user {cmdline[0]} removed")
                printList(fbx_data)
    else:
        print('Freebox command line tool: {0} del vpn.server <command args...>'.format(prg))
        print('Available command args: user <login>')

def fbx_del_vpnclt():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} del vpn.client <command args...>'.format(prg))
        print('Available command args: <client id>')
    else:
        try: fbx_data = fbx.vpn.del_client(cmdline[0])
        except: print('Invalid parms')
        else:
            print(f"#VPN Client {cmdline[0]} removed")
            printList(fbx_data)

def fbx_del_profile():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} del profile <command args...>'.format(prg))
        print('Available command args: <profile id>, rule <profile id> <rule id>')
    elif cmdline[0] == 'rule':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} del profile <command args...>'.format(prg))
            print('Available command args: <profile id>, rule <profile id> <rule id>')
        else:
            prof_id = cmdline[0]
            del cmdline[0]
            if cmdline == []:
                print('Freebox command line tool: {0} del profile <command args...>'.format(prg))
                print('Available command args: <profile id>, rule <profile id> <rule id>')
            else:
                try: fbx_data = fbx.profile.del_netcontrol_rule(prof_id, cmdline[0])
                except: print('Invalid parms')
                else:
                    print(f"#Rule {cmdline[0]} for profile {prof_id} removed")
                    printList(fbx_data)
    else:
        try: fbx_data = fbx.profile.del_profile(cmdline[0])
        except: print('Invalid parms')
        else:
            print(f"#Profile {cmdline[0]} removed")
            printList(fbx_data)

def fbx_del_vm():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} del vm <command args...>'.format(prg))
        print('Available command args: <id>, task <task id>')
    elif cmdline[0] == 'task':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} del vm <command args...>'.format(prg))
            print('Available command args: <id>, task <task id>')
        else:
            try: fbx_data = fbx.vm.del_task(cmdline[0])
            except: print('Invalid parms')
            else:
                print(f"#VM disk resize task {cmdline[0]} removed")
                printList(fbx_data)
    else:
        try: fbx_data = fbx.vm.delete(cmdline[0])
        except: print('Invalid parms')
        else:
            print(f"#VM {cmdline[0]} removed")
            printList(fbx_data)

def fbx_del():
    global fbx
    global cmdline
    if cmdline == []:
        print('Freebox command line tool: {0} del <command args...>'.format(prg))
        print('Available command args: call, contact, contact.number, dhcp, download.rss, download.task, fw, lan.host, profile, upnpigd, vm, vpn.client, vpn.server, wifi')
    elif cmdline[0] == 'download.task': fbx_del_dwntask()
    elif cmdline[0] == 'call': fbx_del_call()
    elif cmdline[0] == 'contact.number': fbx_del_contactnum()
    elif cmdline[0] == 'contact': fbx_del_contact()
    elif cmdline[0] == 'upnpigd': fbx_del_upnpigd()
    elif cmdline[0] == 'dhcp': fbx_del_dhcp()
    elif cmdline[0] == 'lan.host': fbx_del_lanhost()
    elif cmdline[0] == 'fw': fbx_del_fw()
    elif cmdline[0] == 'download.rss': fbx_del_rss()
    elif cmdline[0] == 'wifi': fbx_del_wifi()
    elif cmdline[0] == 'vpn.server': fbx_del_vpnsrv()
    elif cmdline[0] == 'vpn.client': fbx_del_vpnclt()
    elif cmdline[0] == 'profile': fbx_del_profile()
    elif cmdline[0] == 'vm': fbx_del_vm()
    else:
        print('Freebox command line tool: {0} del <command args...>'.format(prg))
        print('Available command args: call, contact, contact.number, dhcp, download.rss, download.task, fw, lan.host, profile, upnpigd, vm, vpn.client, vpn.server, wifi')

def fbx_add_contact():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} add contact <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.contact.contact_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.contact.contact_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} add contact <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.contact.contact_write_parms)
        else:
            try: fbx_data = fbx.contact.add_contact(conf)
            except: print('Invalid parms')
            else:
                print(f"#Contact added")
                printList(fbx_data)

def fbx_add_contactnum():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} add contact.number <command args...>'.format(prg))
        print('Available command args: <contact id> [<parmameter>=<value> ...]')
        printParms(fbx.contact.contact_write_numbers)
    else:
        contact_id = cmdline[0]
        del cmdline[0]
        conf = fbx.encodeJSON(fbx.contact.contact_write_numbers, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} add contact.number <command args...>'.format(prg))
            print('Available command args: <contact id> [<parmameter>=<value> ...]')
            printParms(fbx.contact.contact_write_numbers)
        else:
            try: fbx_data = fbx.contact.add_number(contact_id,conf)
            except: print('Invalid parms')
            else:
                print(f"#Contact number added")
                printList(fbx_data)

def fbx_add_dhcp():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} add dhcp <command args...>'.format(prg))
        print('Available command args: static [<parmameter>=<value> ...]')
        printParms(fbx.dhcp.lease_write_parms)
    elif cmdline[0] == 'static':
        del cmdline[0]
        conf = fbx.encodeJSON(fbx.dhcp.lease_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} add dhcp <command args...>'.format(prg))
            print('Available command args: static [<parmameter>=<value> ...]')
            printParms(fbx.dhcp.lease_write_parms)
        else:
            try: fbx_data = fbx.dhcp.add_static_dhcp_lease(conf)
            except: print('Invalid parms')
            else:
                print(f"#DHCP static lease added")
                printList(fbx_data)
    else:
        print('Freebox command line tool: {0} add dhcp <command args...>'.format(prg))
        print('Available command args: static [<parmameter>=<value> ...]')
        printParms(fbx.dhcp.lease_write_parms)

def fbx_add_fw():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} add fw <command args...>'.format(prg))
        print('Available command args: forward [<parmameter>=<value> ...]')
        printParms(fbx.fw.forwarding_write_parms)
    elif cmdline[0] == 'forward':
        del cmdline[0]
        conf = fbx.encodeJSON(fbx.fw.forwarding_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} add fw <command args...>'.format(prg))
            print('Available command args: forward [<parmameter>=<value> ...]')
            printParms(fbx.fw.forwarding_write_parms)
        else:
            try: fbx_data = fbx.fw.add_forward(conf)
            except: print('Invalid parms')
            else:
                print(f"#Port forwarding added")
                printList(fbx_data)
    else:
        print('Freebox command line tool: {0} add fw <command args...>'.format(prg))
        print('Available command args: forward [<parmameter>=<value> ...]')
        printParms(fbx.fw.forwarding_write_parms)

def fbx_add_rss():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} add download.rss <command args...>'.format(prg))
        print('Available command args: <url>')
    else:
        try: fbx_data = fbx.downloads.add_rssfeed(cmdline[0])
        except: print('Invalid parms')
        else:
            print(f"#RSS feed {cmdline[0]} added")
            printList(fbx_data)

def fbx_add_dwnltsk_black():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} add download.task blackentry <command args...>'.format(prg))
        print('Available command args: <task id> <host>')
    else:
        tsk_id = cmdline[0]
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} add download.task blackentry <command args...>'.format(prg))
            print('Available command args: <task id> <host>')
        else:
            try: fbx_data = fbx.downloads.add_task_blackentry(tsk_id, cmdline[0])
            except: print('Invalid parms')
            else:
                print(f"#Host {cmdline[0]} added into task {tsk_id} blacklist")
                printList(fbx_data)

def fbx_add_dwnltsk_track():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} add download.task tracker <command args...>'.format(prg))
        print('Available command args: <task id> <url>')
    else:
        tsk_id = cmdline[0]
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} add download.task tracker <command args...>'.format(prg))
            print('Available command args: <task id> <url>')
        else:
            try: fbx_data = fbx.downloads.add_task_blackentry(tsk_id, cmdline[0])
            except: print('Invalid parms')
            else:
                print(f"#Tracker {cmdline[0]} added for task {tsk_id}")
                printList(fbx_data)

def fbx_add_dwnltsk_url():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} add download.task url <command args...>'.format(prg))
        print('Available command args: <url>')
    else:
        try: fbx_data = fbx.downloads.add_task(cmdline[0])
        except: print('Invalid parms')
        else:
            print(f"#{cmdline[0]} added for download")
            printList(fbx_data)

def fbx_add_dwnltsk():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} add download.task <command args...>'.format(prg))
        print('Available command args: blackentry, tracker, url')
    elif cmdline[0] == 'blackentry': fbx_add_dwnltsk_black()
    elif cmdline[0] == 'tracker': fbx_add_dwnltsk_track()
    elif cmdline[0] == 'url': fbx_add_dwnltsk_url()
    else:
        print('Freebox command line tool: {0} add download.task <command args...>'.format(prg))
        print('Available command args: blackentry, tracker, url')

def fbx_add_wifi_key():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} add wifi key <command args...>'.format(prg))
        print('Available command args: [<parmameter>=<value> ...]')
        printParms(fbx.wifi.custom_key_write_parms)
    else:
        conf = fbx.encodeJSON(fbx.wifi.custom_key_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} add wifi key <command args...>'.format(prg))
            print('Available command args: [<parmameter>=<value> ...]')
            printParms(fbx.wifi.custom_key_write_parms)
        else:
            try: fbx_data = fbx.wifi.create_wifi_custom_key(conf)
            except: print('Invalid parms')
            else:
                print(f"#Wifi custom key added")
                printList(fbx_data)

def fbx_add_wifi_filter():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} add wifi filter <command args...>'.format(prg))
        print('Available command args: <mac address> [<parmameter>=<value> ...]')
        printParms(fbx.wifi.mac_filter_write_parms)
    else:
        mac = cmdline[0]
        del cmdline[0]
        conf = fbx.encodeJSON(fbx.wifi.mac_filter_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} add wifi filter <command args...>'.format(prg))
            print('Available command args: <mac address>  [<parmameter>=<value> ...]')
            printParms(fbx.wifi.mac_filter_write_parms)
        else:
            try: fbx_data = fbx.wifi.create_wifi_mac_filter(mac, conf)
            except: print('Invalid parms')
            else:
                print(f"#MAC filter added")
                printList(fbx_data)

def fbx_add_wifi():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} add wifi <command args...>'.format(prg))
        print('Available command args: filter, key')
    elif cmdline[0] == 'filter': fbx_add_wifi_filter()
    elif cmdline[0] == 'key': fbx_add_wifi_key()
    else:
        print('Freebox command line tool: {0} add wifi <command args...>'.format(prg))
        print('Available command args: filter, key')

def fbx_add_vpnsrv():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} add vpn.server <command args...>'.format(prg))
        print('Available command args: user [<parmameter>=<value> ...]')
        printParms(fbx.vpn.vpnserver_user_write_parms)
    elif cmdline[0] == 'user':
        del cmdline[0]
        conf = fbx.encodeJSON(fbx.vpn.vpnserver_user_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} add vpn.server <command args...>'.format(prg))
            print('Available command args: user [<parmameter>=<value> ...]')
            printParms(fbx.vpn.vpnserver_user_write_parms)
        else:
            try: fbx_data = fbx.vpn.add_server_user(conf)
            except: print('Invalid parms')
            else:
                print(f"#VPN Server user added")
                printList(fbx_data)
    else:
        print('Freebox command line tool: {0} add vpn.server <command args...>'.format(prg))
        print('Available command args: user [<parmameter>=<value> ...]')
        printParms(fbx.vpn.vpnserver_user_write_parms)

def fbx_add_vpnclt():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} add vpn.client <command args...>'.format(prg))
        print('Available command args: <type> <description> [<parmameter>=<value> ...]')
    else:
        typ = cmdline[0]
        del cmdline[0]
        if typ == 'pptp': parms = fbx.vpn.vpnclient_pptp_write_parms
        elif typ == 'openvpn': parms = fbx.vpn.vpnclient_open_write_parms
        else: parms = None
        if parms == None:
            print('Freebox command line tool: {0} add vpn.client <command args...>'.format(prg))
            print('Available command args: <type> <description> [<parmameter>=<value> ...]')
            print('<type> must be pptp or openvpn')
        elif cmdline == []:
            print('Freebox command line tool: {0} add vpn.client <command args...>'.format(prg))
            print('Available command args: <type> <description> [<parmameter>=<value> ...]')
            printParms(parms)
        else:
            desc = cmdline[0]
            del cmdline[0]
            conf = fbx.encodeJSON(parms, cmdline)
            if conf == None:
                print('Freebox command line tool: {0} add vpn.client <command args...>'.format(prg))
                print('Available command args: <type> <description> [<parmameter>=<value> ...]')
                printParms(parms)
            else:
                if typ == 'openvpn' and 'config_file' in conf: conf['config_file'] = get_config_from_file(conf['config_file'])
                try: fbx_data = fbx.vpn.add_client(conf, typ, desc)
                except: print('Invalid parms')
                else:
                    print(f"#VPN Client added")
                    printList(fbx_data)

def fbx_add_profile():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} add profile <command args...>'.format(prg))
        print('Available command args: new [<parmameter>=<value> ...], rule <profile id> [<parmameter>=<value> ...]')
    elif cmdline[0] == 'new':
        del cmdline[0]
        conf = fbx.encodeJSON(fbx.profile.profile_write_parms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} add profile <command args...>'.format(prg))
            print('Available command args: new [<parmameter>=<value> ...], rule <profile id> [<parmameter>=<value> ...]')
            printParms(fbx.profile.profile_write_parms)
        else:
            try: fbx_data = fbx.profile.add_profile(conf)
            except: print('Invalid parms')
            else:
                print(f"#New profile added")
                printList(fbx_data)            
    elif cmdline[0] == 'rule':
        del cmdline[0]
        if cmdline == []:
            print('Freebox command line tool: {0} add profile <command args...>'.format(prg))
            print('Available command args: new [<parmameter>=<value> ...], rule <profile id> [<parmameter>=<value> ...]')
            printParms(fbx.profile.rule_write_parms)
        else:
            prof_id = cmdline[0]
            del cmdline[0]
            conf = fbx.encodeJSON(fbx.profile.rule_write_parms, cmdline)
            if conf == None:
                print('Freebox command line tool: {0} add profile <command args...>'.format(prg))
                print('Available command args: new [<parmameter>=<value> ...], rule <profile id> [<parmameter>=<value> ...]')
                printParms(fbx.profile.rule_write_parms)
            else:
                print(conf)
                try: fbx_data = fbx.profile.add_netcontrol_rule(prof_id, conf)
                except: print('Invalid parms')
                else:
                    print(f"#New rule for profile {prof_id} added")
                    printList(fbx_data)            
    else:
        print('Freebox command line tool: {0} add profile <command args...>'.format(prg))
        print('Available command args: new [<parmameter>=<value> ...], rule <profile id> [<parmameter>=<value> ...]')

def fbx_add_vm():
    global fbx
    global cmdline
    del cmdline[0]
    if cmdline == []:
        print('Freebox command line tool: {0} add vm <command args...>'.format(prg))
        print('Available command args: [raw] [<parmameter>=<value> ...]')
        printParms(fbx.vm.vm_write_parms)
    else:
        lparms = fbx.vm.vm_write_parms
        if cmdline[0] == 'raw':
            ddir = False
            del cmdline[0]
            lparms['cloudinit_userdata'] = 'text'
        else: ddir = True
        conf = fbx.encodeJSON(lparms, cmdline)
        if conf == None:
            print('Freebox command line tool: {0} add vm <command args...>'.format(prg))
            print('Available command args: [raw] [<parmameter>=<value> ...]')
            printParms(fbx.vm.vm_write_parms)
        else:
            if ddir:
                if 'cloudinit_userdata' in conf: conf['cloudinit_userdata'] = fbx.vm.decode_cloudinit_data(conf['cloudinit_userdata'])
            else:
                if 'cloudinit_userdata' in conf: conf['cloudinit_userdata'] = conf['cloudinit_userdata'].replace('\\n','\n')
            try: fbx_data = fbx.vm.create(conf, ddir)
            except: print('Invalid parms')
            else:
                print(f"#New VM added")
                printList(fbx_data)            

def fbx_add():
    global fbx
    global cmdline
    if cmdline == []:
        print('Freebox command line tool: {0} add <command args...>'.format(prg))
        print('Available command args: contact, contact.number, dhcp, download.rss, download.task, fw, profile, vm, vpn.client, vpn.server, wifi')
    elif cmdline[0] == 'contact': fbx_add_contact()
    elif cmdline[0] == 'contact.number': fbx_add_contactnum()
    elif cmdline[0] == 'dhcp': fbx_add_dhcp()
    elif cmdline[0] == 'fw': fbx_add_fw()
    elif cmdline[0] == 'download.task': fbx_add_dwnltsk()
    elif cmdline[0] == 'download.rss': fbx_add_rss()
    elif cmdline[0] == 'wifi': fbx_add_wifi()
    elif cmdline[0] == 'vpn.server': fbx_add_vpnsrv()
    elif cmdline[0] == 'vpn.client': fbx_add_vpnclt()
    elif cmdline[0] == 'profile': fbx_add_profile()
    elif cmdline[0] == 'vm': fbx_add_vm()
    else:
        print('Freebox command line tool: {0} add <command args...>'.format(prg))
        print('Available command args: contact, contact.number, dhcp, download.rss, download.task, fw, profile, vm, vpn.client, vpn.server, wifi')

#__main__
# Set here your freebox API parms
fbx_dns = 'mafreebox.free.fr'
fbx_port = 443
# Basic checks of command line
cmdline = sys.argv
prg = sys.argv[0]
del cmdline[0]
if cmdline == []:
    print('Freebox command line tool: {0} <command args...>'.format(prg))
    print('Available command args: add, change, del, read')
elif cmdline[0] == 'read':
    del cmdline[0]
    fbx = Freebox()
    fbx.open(fbx_dns, fbx_port)
    fbx_read()
    fbx.close()
elif cmdline[0] == 'change':
    del cmdline[0]
    fbx = Freebox()
    fbx.open(fbx_dns, fbx_port)
    fbx_change()
    fbx.close()
elif cmdline[0] == 'del':
    del cmdline[0]
    fbx = Freebox()
    fbx.open(fbx_dns, fbx_port)
    fbx_del()
    fbx.close()
elif cmdline[0] == 'add':
    del cmdline[0]
    fbx = Freebox()
    fbx.open(fbx_dns, fbx_port)
    fbx_add()
    fbx.close()
else:
    print('Freebox command line tool: {0} <command args...>'.format(prg))
    print('Available command args: add, change, del, read')
