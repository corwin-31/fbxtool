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

def myMain(qcmObj, fbx, vmSelect, wifiSelect, wifiIds, freeplug, downSelect, downIds):
    mainMenu = [ 'VM', 'Wifi', 'CPL', 'Downloads' ]
    cplMenu = [ 'Show', 'Reset' ]
    wifiMenu = [ 'Config', 'Scan', 'Radar' ]
    vmMenu = [ 'Status', 'Start', 'Stop' ]
    dwnMenu = [ 'Status', 'Retry', 'Seed', 'Stop', 'Start tracker', 'Stop tracker' ]
    menuLevel = 'Main'

    while True:
        if menuLevel == 'Main': curMenu = mainMenu
        elif menuLevel == 'Main>CPL': curMenu = cplMenu
        elif menuLevel == 'Main>Wifi': curMenu = wifiMenu
        elif menuLevel == 'Main>Downloads': curMenu = dwnMenu
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
                    if userSelect == 'Status': exTxt = printList(doIt(fbx.vm.get_config_vm,vmList.index(selVM)))
                    elif userSelect == 'Start': exTxt = printList(doIt(fbx.vm.start,vmList.index(selVM)))
                    else: exTxt = printList(doIt(fbx.vm.stop,vmList.index(selVM)))
                    qcmObj.QCMdisplay(exTxt,menuLevel + '>' + selVM)
                    menuLevel = 'Main>VM'
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
fBox.open('mafreebox.freebox.fr', 443)

vmList = []
allVM = fBox.vm.get_config_all()
for curVM in allVM: vmList.append(curVM['name'])
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

fMenu.QCMstart(myMain, fBox, vmList, wfList, wfIds, mainPlug, dwnTsks, dwnIds)

fBox.close()
