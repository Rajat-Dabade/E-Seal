#import easygui as eg
import commands as cmd
import sys

def makeKey():
	Devices=[]
	rawData=cmd.getstatusoutput('lsusb')
	if(rawData[0]==0):
		SpecList=rawData[1].split('\n')
		for i in SpecList:
			i=i.split(' ')
			i[5]=i[5].split(':')
			if(int("0x"+i[5][1],16)> 50):
				Devices.append([i[1],i[3].strip(':'),i[6:]])
	print """
---------------------------------------------------------

Please provide the number for usbstick.
		"""
	cnt=1
	for i in Devices:
		print "{0} {1}".format(cnt,''.join(i[2]))
		cnt+=1
	opt=input("(Ctrl-C to terminate) Option:")
	if(opt <= len(Devices) and opt >0):
		print len(Devices)
	else:
		sys.stderr.write('No mathing Option Found. Exiting...')
		sys.exit(0)
	opt=opt-1
	print "Checking initial keys ....."
	serialKey=cmd.getstatusoutput("""lsusb -v -s {0}:{1}""".format(Devices[opt][0],Devices[opt][1])+""" | awk -F " " '($1 == "iSerial") {print $3}'""")
	flg = 0
	try:
		f = open('serialKey','r+')
		for line in f:
			tmp=line.split(':')
			if(tmp[0].strip('\n') == serialKey[1]):
				flg=1
				print "Device is already Configured. Please Update file on Server"
	except:
		f = open('serialKey','w')
		f.close()
		f = open('serialKey','r+')
	if(flg == 1):
		sys.exit(0)
	else:
		f.write(serialKey[1]+":"+''.join(Devices[opt][2]))
		f.write("\n")
		f.close()
		
	print(''.join(Devices[opt][2]))
	print('File Updates Kindly  update over server')

if __name__=="__main__":
	makeKey()
