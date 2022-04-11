#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:26:54 2020

"""

from qcmenu import QCMenu
from fbxapitool import Freebox

# Simply translate of list and dictionnaries, recursively
def printList(myList, startline=''):
    txtOut = []
    if myList == None: txtOut.append('Empty report')
    elif isinstance(myList, list):
        if myList == []: txtOut.append('Empty list')
        else:
            for item in myList:
                if isinstance(item, list) or isinstance(item, dict):
                    txtOut = txtOut + printList(item,startline=startline + '  ')
                else:
                    txtOut = txtOut + '{0}{1}'.format(startline, item).split('\n')
                txtOut = txtOut + '{0}  ##'.format(startline).split('\n')
    elif not isinstance(myList, dict): txtOut.append('Invalid list or dict')
    elif myList == {}: txtOut.append('Empty report')
    else:
        for item in myList:
            if isinstance(myList[item], list) or isinstance(myList[item], dict):
                txtOut = txtOut + '{0}{1} ='.format(startline, item).split('\n')
                txtOut = txtOut + printList(myList[item],startline=startline + '  ')
            else: txtOut = txtOut + '{0}{1} = {2}'.format(startline, item, myList[item]).split('\n')
    return txtOut

def doIt(cFunc, *args):
    try: data = cFunc(*args)
    except: return { 'Operation': 'failed' }
    else: return data

def myMain(qcmObj, fbx, vmSelect, vmSelIds, wifiSelect, wifiIds, freeplug, downSelect, downIds, partSelect, partSelIds, partSelTypes):
    mainMenu = [ 'VM', 'Wifi', 'CPL', 'Downloads', 'Storage' ]
    cplMenu = [ 'Show', 'Reset' ]
    wifiMenu = [ 'Config', 'Scan', 'Radar' ]
    vmMenu = [ 'Status', 'Start', 'Stop' ]
    dwnMenu = [ 'Status', 'Retry', 'Seed', 'Stop', 'Start tracker', 'Stop tracker' ]
    partMenu = [ 'Status', 'Umount', 'Mount', 'Check', 'Repair' ]
    menuLevel = 'Main'

    while True:
        if menuLevel == 'Main': curMenu = mainMenu
        elif menuLevel == 'Main>CPL': curMenu = cplMenu
        elif menuLevel == 'Main>Wifi': curMenu = wifiMenu
        elif menuLevel == 'Main>Downloads': curMenu = dwnMenu
        elif menuLevel == 'Main>Storage': curMenu = partMenu
        else: curMenu = vmMenu
        userSelect = qcmObj.QCMmenu(curMenu, menuLevel)
        if menuLevel == 'Main':
            if userSelect == 'Quit': break
            else: menuLevel = menuLevel + '>' + userSelect
        elif menuLevel == 'Main>VM':
            if userSelect == 'Quit': menuLevel = 'Main'
            else:
                menuLevel = menuLevel + '>' + userSelect
                selVM = qcmObj.QCMmenu(vmSelect, menuLevel)
                if selVM == 'Quit': menuLevel = 'Main'
                else:
                    if userSelect == 'Status': exTxt = printList(doIt(fbx.vm.get_config_vm,vmSelIds[vmSelect.index(selVM)]))
                    elif userSelect == 'Start': exTxt = printList(doIt(fbx.vm.start,vmSelIds[vmSelect.index(selVM)]))
                    else: exTxt = printList(doIt(fbx.vm.stop,vmSelIds[vmSelect.index(selVM)]))
                    qcmObj.QCMdisplay(exTxt,menuLevel + '>' + selVM)
                    menuLevel = 'Main>VM'
        elif menuLevel == 'Main>Storage':
            if userSelect == 'Quit': menuLevel = 'Main'
            else:
                menuLevel = menuLevel + '>' + userSelect
                selPart = qcmObj.QCMmenu(partSelect, menuLevel)
                if selPart == 'Quit': menuLevel = 'Main'
                else:
                    if userSelect == 'Status': exTxt = printList(doIt(fbx.storage.get_partition,partSelIds[partSelect.index(selPart)]))
                    elif userSelect == 'Check': 
                        if partSelTypes[partSelect.index(selPart)] in set(['ext4', 'xfs', 'hfsplus' ]): exTxt = printList(doIt(fbx.storage.check_partition,partSelIds[partSelect.index(selPart)]))
                    elif userSelect == 'Repair': 
                        if partSelTypes[partSelect.index(selPart)] in set(['ext4', 'xfs', 'hfsplus' ]): exTxt = printList(doIt(fbx.storage.check_partition,partSelIds[partSelect.index(selPart)], True))
                    elif userSelect == 'Mount': exTxt = printList(doIt(fbx.storage.mount_partition,partSelIds[partSelect.index(selPart)]))
                    else: exTxt = printList(doIt(fbx.storage.umount_partition,partSelIds[partSelect.index(selPart)]))
                    qcmObj.QCMdisplay(exTxt,menuLevel + '>' + selPart)
                    menuLevel = 'Main>Storage'
        elif menuLevel == 'Main>Wifi':
            if userSelect == 'Quit': menuLevel = 'Main'
            else:
                menuLevel = menuLevel + '>' + userSelect
                selWF = qcmObj.QCMmenu(wifiSelect, menuLevel)
                if selWF == 'Quit': menuLevel = 'Main'
                else:
                    accPt = wifiIds[wifiSelect.index(selWF)]
                    if userSelect == 'Config': exTxt = printList(doIt(fbx.wifi.get_ap,accPt))
                    elif userSelect == 'Scan': exTxt = printList(doIt(fbx.wifi.start_wifi_access_point_neighbors_scan,accPt))
                    else: exTxt = printList(doIt(fbx.wifi.get_ap_neighbors,0))
                    qcmObj.QCMdisplay(exTxt,menuLevel + '>' + selWF)
                    menuLevel = 'Main>Wifi'
        elif menuLevel == 'Main>Downloads':
            if userSelect == 'Quit': menuLevel = 'Main'
            else:
                menuLevel = menuLevel + '>' + userSelect
                selDwn = qcmObj.QCMmenu(downSelect, menuLevel)
                if selDwn == 'Quit': menuLevel = 'Main'
                else:
                    tskId = downIds[downSelect.index(selDwn)]
                    selTrk = ''
                    if userSelect == 'Status': exTxt = printList(doIt(fbx.downloads.get_task,tskId)) + printList(doIt(fbx.downloads.get_task_trackers,tskId))
                    elif userSelect == 'Retry': exTxt = printList(doIt(fbx.downloads.set_task,tskId, { 'status': 'retry' }))
                    elif userSelect == 'Seed': exTxt = printList(doIt(fbx.downloads.set_task,tskId, { 'status': 'seeding' }))
                    elif userSelect == 'Stop': exTxt = printList(doIt(fbx.downloads.set_task,tskId, { 'status': 'stopped' }))
                    elif userSelect == 'Start tracker':
                        trackers = fbx.downloads.get_task_trackers(tskId)
                        trkList = []
                        for curTrk in trackers: trkList.append(curTrk['announce'])
                        selTrk = qcmObj.QCMmenu(trkList,menuLevel + '>' + selDwn)
                        if selTrk != 'Quit':
                            exTxt = printList(doIt(fbx.downloads.start_task_tracker,tskId,selTrk))
                            selTrk = '>' + selTrk
                    else:
                        trackers = fbx.downloads.get_task_trackers(tskId)
                        trkList = []
                        for curTrk in trackers: trkList.append(curTrk['announce'])
                        selTrk = qcmObj.QCMmenu(trkList,menuLevel + '>' + selDwn)
                        if selTrk != 'Quit':
                            exTxt = printList(doIt(fbx.downloads.stop_task_tracker,tskId,selTrk))
                            selTrk = '>' + selTrk
                    if selTrk != 'Quit': qcmObj.QCMdisplay(exTxt,menuLevel + '>' + selDwn + selTrk)
                    menuLevel = 'Main>Downloads'
        else:
            if userSelect == 'Quit': menuLevel = 'Main'
            else:
                if menuLevel == 'Main>CPL' and userSelect == 'Show': exTxt = printList(doIt(fbx.freeplugs.get_freeplugs_list))
                elif menuLevel == 'Main>CPL' and userSelect == 'Reset':
                    if freeplug == None: exTxt = [ 'Freeplugs offline' ]
                    else: exTxt = printList(doIt(fbx.freeplugs.reset_freeplug,freeplug))
                qcmObj.QCMdisplay(exTxt,menuLevel + '>' + userSelect)

# Main
fMenu = QCMenu()
fBox = Freebox()
fBox.open('corwin31.freeboxos.fr', 32769)

vmList = []
vmIds = []
allVM = fBox.vm.get_config_all()
for curVM in allVM:
    vmList.append(curVM['name'])
    vmIds.append(curVM['id'])
wfList = []
wfIds = []
allWF = fBox.wifi.get_ap_list()
for curWF in allWF:
    wfList.append(curWF['name'])
    wfIds.append(curWF['id'])

mainPlug = None
plugs = fBox.freeplugs.get_freeplugs_list()
if plugs != None and plugs != [] and 'members' in plugs[0]:
    if plugs[0]['members'] != None:
        for plug in plugs[0]['members']:
            if plug['net_role'] == 'cco': mainPlug = plug['id']

dwnTsks = []
dwnIds = []
dwnlds = fBox.downloads.get_tasks()
for curDwn in dwnlds:
    dwnTsks.append(curDwn['name'])
    dwnIds.append(curDwn['id'])
    
partList = []
partIds = []
partTypes = []
partitions = fBox.storage.get_partitions()
for curPart in partitions:
    partList.append(curPart['label'])
    partIds.append(curPart['id'])
    partTypes.append(curPart['fstype'])

fMenu.QCMstart(myMain, fBox, vmList, vmIds, wfList, wfIds, mainPlug, dwnTsks, dwnIds, partList, partIds, partTypes)

fBox.close()
