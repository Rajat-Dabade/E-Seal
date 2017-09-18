#!/usr/bin/env python

import commands as cmd
import sys
import os
import urllib2 

def getPath():
	return os.path.dirname(os.path.realpath(__file__))+'\\'

def getURL(path):
	with open('{0}url'.format(path),'r') as f:
		return f.readline()
def check():
	Devices=[]
	path1=getPath()
	# path=os.path.realpath(__file__)
    # path1=""
    # for i in range(len(path)-14):
    #     path1=path1+path[i]
	cmdDeviceToFile="""wmic diskdrive get serialnumber > {0}devices.txt""".format(path1)
	print cmdDeviceToFile
	cmdDeviceFileState=os.system(cmdDeviceToFile)
	print cmdDeviceFileState
	if(cmdDeviceFileState != 0):
		sys.stderr.write('Could not execute command lsusb. Press Enter to exit')
		sys.exit(0)
	else:
		cmdToAscii="TYPE {0}devices.txt > {0}devicesAscii.txt".format(path1)
		if(os.system(cmdToAscii)!=0):
			sys.stderr.write('Could not execute command TYPE. Press Enter to exit')
			sys.exit(0)
		else:
			with open('{0}devicesAscii.txt'.format(path1),'r') as f:
				f.readline()
				while(True):
					tmp = f.readline()
					if(tmp==""):
						break
					tmp=tmp.replace(" ","")
					tmp=tmp.strip("\n")
					Devices.append(tmp)
                print Devices
		os.system('del /f {0}devices.txt'.format(path1))
		os.system('del /f {0}devicesAscii.txt'.format(path1))
		url=getURL(path1)
		try:
			u=urllib2.urlopen('{0}/serialKey'.format(url))
			localFile = open('{0}serialKey'.format(path1), 'w')
			localFile.write(u.read())
			localFile.close()
		except:
			print "Please Check your Internet Connection"

		with open('{0}serialKey'.format(path1),'r') as keys:
			for key in keys.readlines():
				key=key.split(':')
				if (key[0] in Devices):
					os.system('del /f {0}serialKey'.format(path1))
					print "Device is connected"
					return 1
				else:
					os.system('del /f {0}serialKey'.format(path1))
					print "Device is not connected"
        
"""
def main():
	cmd_listBus = 
	busDeviceList=cmd.getstatusoutput(cmd_listBus)
	Devices=[]
    if(busDeviceList[0] != 0):
		sys.stderr.write('Could not execute command lsusb. Press Enter to exit')
		sys.exit(0)
	else:
		busDeviceList=busDeviceList[1].split('\n')
		for i in range(len(busDeviceList)):
			busDeviceList[i]=busDeviceList[i].strip(':').split()
		print busDeviceList
		for i in busDeviceList:
			cmd_getSerialID=
			serialID=cmd.getstatusoutput(cmd_getSerialID)
			if(serialID[0] != 0):
				sys.stderr.write('Could not execute command lsusb. Press Enter to exit')
				sys.exit(0)
			else:
				if(serialID[1] != ""):
					Devices.append(serialID[1])
					print serialID[1]
		print Devices
		dload_keys_state=cmd.getstatusoutput('wget -r 172.17.0.2/serialKey')
		if(dload_keys_state[0] != 0):
			sys.stderr.write('Could not execute command wget.\nPlease Check ur Internet and try Again.\nPress Enter to exit')
			sys.exit(0)
		else:
			pass
		with open('172.17.0.2/serialKey','r') as keys:
			key=keys.readline().strip('\n ')
			if (key in Devices):
				print "Device is connected"
			else:
				print "Device is not connected"
		cmd.getoutput('rm -r -f 172.17.0.2')
"""
# if __name__=="__main__":
# 	main()
