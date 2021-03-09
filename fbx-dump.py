#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Dumps freebox config: out format is calls to Freebox command line tool (fbx-cmd.py)
Passwords can't be dumped, so they must be manually changed before restoring
OpenVPN Client config files as well
'''

from fbxapitool import Freebox

# Print basic JSON
def dumpConf(mode='change', topic='', keys=[], conf={}, finish=True):
    if topic !='': print(f'fbx-cmd.py {mode} {topic}', end='')
    for key in keys:
        line = f' "{key}={conf[key]}"'
        line = line.replace('\n','\\n')
        print(line, end='')
    if finish: print('', end='\n', flush=True)

# Print multiple JSON
def dumpConf_Listmulti(mode='change', topic='', keys=[], conf={}, finish=True):
    if topic !='': print(f'fbx-cmd.py {mode} {topic}', end='')
    for key in keys:
        print(f' "{key}=', end='')
        coma = False
        for item in conf[key]:
            if coma: print(',', end='')
            coma = True
            semi = False
            for entry in item.keys():
                if semi: print(';', end='')
                semi = True
                print(f'{entry}#{item[entry]}', end='')
        print('"', end='')
    if finish: print('', end='\n', flush=True)

# Print JSON containing sublists
def dumpConf_Sublist(mode='change', topic='', keys=[], conf={}, finish=True):
    if topic !='': print(f'fbx-cmd.py {mode} {topic}', end='')
    for key in keys:
        print(f' "{key}=', end='')
        semi = False
        for entry in conf[key].keys():
            if semi: print(';', end='')
            semi = True
            print(f'{entry}#{conf[key][entry]}', end='')
        print('"', end='')
    if finish: print('', end='\n', flush=True)

# Print JSON with lists
def dumpConf_List(mode='change', topic='', keys=[], conf={}, finish=True):
    if topic !='': print(f'fbx-cmd.py {mode} {topic}', end='')
    for key in keys:
        print(f' "{key}=', end='')
        coma = False
        for item in conf[key]:
            if coma: print(',', end='')
            coma = True
            print(f'{item}', end='')
        print('"', end='')
    if finish: print('', end='\n', flush=True)

#__main__
fbx = Freebox()
# Set here your Freebox parms
fbx.open('mafreebox.freebox.fr',443)
print('#Begin')

print('#LCD')
fbx_config = fbx.lcd.get_configuration()
parmKeys = ['brightness']
dumpConf('change', 'lcd', parmKeys, fbx_config)

print('#Airmedia')
fbx_config = fbx.airmedia.get_config()
parmKeys = ['enabled', 'password' ]
fbx_config['password'] = '1Pwd_here'
dumpConf('change', 'airmedia', parmKeys, fbx_config)

print('#FTP')
fbx_config = fbx.ftp.get_ftp_configuration()
parmKeys = [ 'enabled', 'password', 'allow_anonymous', 'allow_anonymous_write', 'allow_remote_access', 'remote_domain', 'port_ctrl', 'port_data' ]
fbx_config['password'] = '1Pwd_here'
dumpConf('change', 'ftp', parmKeys, fbx_config)

print('#Phone')
fbx_config = fbx.phone.get_config()
parmKeys = [ 'dect_enabled', 'dect_registration', 'dect_eco_mode', 'dect_pin', 'dect_ring_pattern', 'dect_nemo_mode', 'dect_ring_on_off' ]
dumpConf('change', 'phone dect', parmKeys, fbx_config)

print('#Connection')
fbx_config = fbx.connection.get_config()
parmKeys = [ 'ping', 'remote_access', 'remote_access_port', 'allow_token_request', 'adblock', 'wol', 'https_port', 'https_available', 'disable_guest' ]
dumpConf('change', 'connection config', parmKeys, fbx_config)
fbx_config = fbx.connection.get_ipv6_config()
parmKeys = [ 'ipv6_enabled', 'ipv6_firewall' ]
dumpConf('change', 'connection ipv6', parmKeys, fbx_config, False)
parmKeys = ['delegations']
dumpConf_Listmulti('change', '', parmKeys, fbx_config, True)

print('#Dynamic DNS')
parmKeys = [ 'enabled', 'hostname', 'user' ]
for prov in [ 'dyndns','ovh','noip' ]:
    fbx_config = fbx.connection.get_dyndns_config(provider=prov)
    dumpConf('change', f'dyndns.config {prov}', parmKeys, fbx_config)

print('#Contacts')
fbx_config = fbx.contact.get_contact_list()
for contact in fbx_config:
    parmKeys = [ 'display_name', 'first_name', 'last_name', 'company' ]
    dumpConf('add', 'contact', parmKeys, contact)
    for num in contact['numbers']:
        parmKeys = [ 'number', 'type', 'is_default' ]
        dumpConf('add', 'contact.number', parmKeys, num)

print('#DHCP')
fbx_config = fbx.dhcp.get_config()
parmKeys = [ 'always_broadcast', 'enabled', 'ip_range_start', 'ip_range_end', 'sticky_assign' ]
dumpConf('change', 'dhcp config', parmKeys, fbx_config, False)
parmKeys = [ 'dns' ]
dumpConf_List('change', '', parmKeys, fbx_config, True)
fbx_config = fbx.dhcp.get_static_dhcp_lease()
parmKeys = [ 'ip', 'mac', 'comment' ]
for lease in fbx_config: dumpConf('add', 'dhcp static', parmKeys, lease)
fbx_config = fbx.dhcp.get_v6_config()
parmKeys = [ 'enabled', 'use_custom_dns' ]
dumpConf('change', 'dhcp v6', parmKeys, fbx_config, False)
parmKeys = [ 'dns' ]
dumpConf_List('change', '', parmKeys, fbx_config, True)

print('#Firewall')
fbx_config = fbx.fw.get_forward()
parmKeys = [ 'comment', 'enabled', 'ip_proto', 'lan_ip', 'lan_port', 'src_ip', 'wan_port_end', 'wan_port_start' ]
if fbx_config != None:
    for rule in fbx_config: dumpConf('add', 'fw forward', parmKeys, rule)
fbx_config = fbx.fw.get_incoming_ports_configuration()
parmKeys = [ 'enabled', 'in_port' ]
for pat in fbx_config: dumpConf('change', f"fw incoming {pat['id']}", parmKeys, pat)
fbx_config = fbx.fw.get_dmz_config()
parmKeys = [ 'enabled', 'ip' ]
dumpConf('change', 'fw dmz', parmKeys, fbx_config)

print('#Netshare')
fbx_config = fbx.netshare.get_afp_configuration()
parmKeys = [ 'enabled', 'guest_allow', 'login_name', 'login_password', 'server_type' ]
fbx_config['login_password'] = '1Pwd_here'
dumpConf('change', 'netshare afp', parmKeys, fbx_config)
fbx_config = fbx.netshare.get_samba_configuration()
parmKeys = [ 'file_share_enabled', 'logon_enabled', 'logon_user', 'logon_password', 'print_share_enabled', 'workgroup' ]
fbx_config['logon_password'] = '1Pwd_here'
dumpConf('change', 'netshare afp', parmKeys, fbx_config)

print('#UPnP AV')
fbx_config = fbx.upnpav.get_configuration()
parmKeys = [ 'enabled' ]
dumpConf('change', 'upnpav', parmKeys, fbx_config)

print('#UPnP IGD')
fbx_config = fbx.upnpigd.get_configuration()
parmKeys = [ 'enabled', 'version' ]
dumpConf('change', 'upnpigd', parmKeys, fbx_config)

print('#VPN Servers')
vpn_srv = fbx.vpn.get_server_list()
for srv in vpn_srv:
    fbx_config = fbx.vpn.get_server_config(srv['name'])
    if srv['type'] == 'ipsec':
        parmKeys = [ 'enabled', 'enable_ipv4', 'enable_ipv6', 'port_ike', 'port_nat']
        dumpConf('change', f"vpn.server config.global {srv['name']}", parmKeys, fbx_config)
        parmKeys = [ 'ike_version' ]
        dumpConf('change', f"vpn.server config.spec {srv['name']}", parmKeys, fbx_config['conf_ipsec'])
    elif srv['type'] == 'pptp':
        parmKeys = [ 'enabled', 'enable_ipv4', 'enable_ipv6', 'port']
        dumpConf('change', f"vpn.server config.global {srv['name']}", parmKeys, fbx_config)
        parmKeys = [ 'mppe' ]
        dumpConf('change', f"vpn.server config.spec {srv['name']}", parmKeys, fbx_config['conf_pptp'])
        parmKeys = [ 'pap', 'chap', 'mschapv2' ]
        dumpConf('change', f"vpn.server config.auth {srv['name']}", parmKeys, fbx_config['conf_pptp']['allowed_auth'])
    else:
        parmKeys = [ 'enabled', 'enable_ipv4', 'enable_ipv6', 'port']
        dumpConf('change', f"vpn.server config.global {srv['name']}", parmKeys, fbx_config)
        parmKeys = [ 'cipher', 'use_tcp', 'disable_fragment' ]
        dumpConf('change', f"vpn.server config.spec {srv['name']}", parmKeys, fbx_config['conf_openvpn'])
fbx_config = fbx.vpn.get_server_users()
parmKeys = [ 'login', 'password', 'ip_reservation' ]
for usr in fbx_config:
    usr['password'] = '1Pwd_here'
    dumpConf('add', 'vpn.server user', parmKeys, usr)

print('#VPN Clients')
vpn_clt = fbx.vpn.get_client_list()
for clt in vpn_clt:
    if clt['type'] == 'pptp':
        parmKeys = [ 'username', 'password', 'mppe', 'remote_host' ]
        clt['conf_pptp']['password'] = '1Pwd_here'
        dumpConf('add', f"vpn.client {clt['type']} {clt['description']}", parmKeys, clt['conf_pptp'])
    else:
        parmKeys = [ 'username', 'password', 'config_file' ]
        clt['conf_openvpn']['config_file'] = 'file here'
        clt['conf_openvpn']['password'] = '1Pwd_here'
        dumpConf('add', f"vpn.client {clt['type']} {clt['description']}", parmKeys, clt['conf_openvpn'])
fbx_config = fbx.vpn.get_slavery()
if fbx_config['fbxgrabberd']['use_vpn']: dumpConf('change', 'vpn.client enslave')
else: dumpConf('change', 'vpn.client free')

print('#Wifi')
fbx_config = fbx.wifi.get_global_config()
parmKeys = [ 'enabled', 'mac_filter_state' ]
dumpConf('change', 'wifi config', parmKeys, fbx_config)
fbx_config = fbx.wifi.get_wifi_custom_keys()
parmKeys = [ 'access_type', 'description', 'duration', 'key', 'max_use_count' ]
for key in fbx_config: dumpConf('add', 'wifi key', parmKeys, key['params'])
fbx_config = fbx.wifi.get_wifi_mac_filters()
parmKeys = [ 'comment', 'type' ]
for filter in fbx_config: dumpConf('add', f"wifi filter {filter['mac']}", parmKeys, filter)
fbx_config = fbx.wifi.get_wifi_planning()
parmKeys = [ 'mapping' ]
dumpConf_List('change', 'wifi planning enable', parmKeys, fbx_config)
if not fbx_config['use_planning']: dumpConf('change', 'wifi planning disable', finish=True)
fbx_config = fbx.wifi.get_ap_list()
for ap in fbx_config:
    parmKeys = [ 'band', 'channel_width', 'primary_channel', 'secondary_channel', 'dfs_enabled' ]
    dumpConf('change', f"wifi access config {ap['id']}", parmKeys, ap['config'])
    parmKeys = [ 'ac_enabled', 'ht_enabled', 'greenfield', 'shortgi20',
      'vht_rx_ldpc', 'ldpc', 'vht_rx_stbc', 'vht_shortgi80', 'rx_stbc',
      'dsss_cck_40', 'tx_stbc', 'smps', 'vht_shortgi160', 'vht_mu_beamformer',
      'vht_tx_stbc', 'vht_su_beamformee', 'vht_su_beamformer', 'delayed_ba',
      'vht_tx_antenna_consistency', 'max_amsdu_7935', 'vht_max_ampdu_len_exp',
      'vht_max_mpdu_len', 'psmp', 'shortgi40', 'vht_rx_antenna_consistency',
      'lsig_txop_prot' ]
    dumpConf('change', f"wifi access ht {ap['id']}", parmKeys, ap['config']['ht'])
fbx_config = fbx.wifi.get_bss_list()
parmKeys = [ 'enabled', 'wps_enabled', 'encryption', 'hide_ssid', 'eapol_version', 'key', 'ssid' ]
for bss in fbx_config:
    arg = 'specific'
    if bss['use_shared_params']: arg='shared'
    dumpConf('change', f"wifi bss {arg} {bss['id']}", parmKeys, bss['config'])

print('#LAN')
fbx_config = fbx.lan.get_config()
parmKeys = [ 'ip', 'name', 'name_dns', 'name_mdns', 'mode', 'name_netbios' ]
dumpConf('change', 'lan config', parmKeys, fbx_config)
parmKeys = [ 'primary_name', 'host_type', 'persistent' ]
fbx_interf = fbx.lan.get_interfaces()
for interf in fbx_interf:
    fbx_config = fbx.lan.get_hosts_list(interf['name'])
    for host in fbx_config: dumpConf('change', f"lan.host config {interf['name']} {host['id']}", parmKeys, host)

print('#Downloads')
fbx_config = fbx.downloads.get_config()
parmKeys = [ 'use_watch_dir', 'dns2', 'dns1', 'max_downloading_tasks', 'download_dir', 'watch_dir' ]
dumpConf('change', 'download config.global', parmKeys, fbx_config)
parmKeys = [ 'enable_pex', 'dht_port', 'announce_timeout', 'max_peers', 'main_port', 'enable_dht', 'crypto_support', 'stop_ratio' ]
dumpConf('change', 'download config.bt', parmKeys, fbx_config['bt'])
parmKeys = [ 'user', 'erase_tmp', 'port', 'nthreads', 'auto_repair', 'ssl', 'auto_extract', 'lazy_par2', 'server' ]
dumpConf('change', 'download config.news', parmKeys, fbx_config['news'])
parmKeys = [ 'max_items', 'fetch_interval' ]
dumpConf('change', 'download config.feed', parmKeys, fbx_config['feed'])
parmKeys = [ 'schedule' ]
dumpConf_List('change', 'download config.throttling', parmKeys, fbx_config['throttling'], False)
parmKeys = [ 'normal', 'slow' ]
dumpConf_Sublist('change', '', parmKeys, fbx_config['throttling'], False)
parmKeys = [ 'mode' ]
dumpConf('change', '', parmKeys, fbx_config['throttling'], True)
parmKeys = [ 'sources' ]
dumpConf_List('change', 'download config.blocklist', parmKeys, fbx_config['blocklist'])

print('#Profiles')
fbx_prof = fbx.profile.get_profiles()
for prof in fbx_prof:
    parmKeys = [ 'name', 'icon' ]
    dumpConf('add', 'profile new', parmKeys, prof)
    for rule in fbx.profile.get_netcontrol_rules(prof['id']):
        parmKeys = [ 'name', 'mode', 'start_time', 'end_time', 'enabled' ]
        dumpConf('add', f"profile rule {rule['profile_id']}", parmKeys, rule, False)
        parmKeys = [ 'weekdays' ]
        dumpConf_List('add', '', parmKeys, rule, True)
for ctrl in fbx.profile.get_netcontrols():
    parmKeys = [ 'macs', 'cdayranges' ]
    dumpConf_List('change', f"profile control {ctrl['profile_id']}", parmKeys, ctrl, False)
    parmKeys = [ 'override_mode' ]
    dumpConf('change', '', parmKeys, ctrl, True)

print('#VM')
fbx_vm = fbx.vm.get_config_all()
for vm in fbx_vm:
    parmKeys = [ 'bind_usb_ports' ]
    dumpConf_List('add', 'vm raw', parmKeys, vm, False)
    parmKeys = [ 'cd_path', 'cloudinit_hostname', 'cloudinit_userdata', 'disk_type', 'enable_cloudinit', 'disk_path', 'enable_screen', 'memory', 'name', 'os', 'vcpus' ]
    dumpConf('add', '', parmKeys, vm, True)
dumpConf('change', 'vm dhcp.fixlease')

print('#End')
fbx.close()
