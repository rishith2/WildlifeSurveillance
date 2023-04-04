# Python file to record GPS data cal culate distances and send mails and website posts accordingly


import serial
import pynmea2
from geopy.distance import geodesic
import time
import os 
import requests 
import time

current_milli_time = lambda: int(round(time.time() * 1000))
oldtime1=0 #int(round(time.time() * 1000))
oldtime2=0 #int(round(time.time() * 1000))
URL='http://poth.000webhostapp.com/animaltrack'
DeviceID='1'
Timedif1=5000 #ms

Timedif2=900000 #ms
radius=.5 #inKM
#ser = serial.Serial('/dev/ttyACM0')

#port = "/dev/serial"
port= '/dev/ttyS0'
location1=[]
location2=[]
def SendMail(data):
	global oldtime2
	if current_milli_time()-oldtime2>Timedif2:
		oldtime2=current_milli_time()
		with open('emaillist.txt') as f:
			mails = f.readlines()
			for id in mails:
				print( "echo '"+data+"' | mailx -s '"+data+"' "+id)
                                os.system( "echo '"+data+"' | mailx -s '"+data+"' "+id)
def SendLoc(lat,lon):
	global oldtime1
	if current_milli_time()-oldtime1>Timedif1:
                oldtime1=current_milli_time()
		to = URL+"/recLoc.php"
 		data = {'DeviceID':DeviceID,'lat':lat,'lon':lon} 
		r = requests.post(url = to, data = data)
		print 'datasent'+r 
  
def setlocation():
	global locid,location1,location2
	location1=[]
	location2=[]
	locid=[]
	try:
		filex = open('addloc.csv', 'r') 
		strsloc=filex.readlines()
		for j in range(0,len(strsloc)):
			strloc=strsloc[j]
			print strloc
			locn=strloc.split(",")
			if len(locn)==3:
				locid=locid+[locn[0]]
				location1=location1+[float(locn[1])]
				location2=location2+[float(locn[2])]
		
		#		print "location data read error"
		filex.close() 
	except:
		location1=location1+[]
		location2=location2+[]
		print "location file read error"


def comploc(loc):
	print loc
	loc1 = (loc[0],loc[1])
	dmin=radius
	point=-1
        for i in range(0,len(location1)):
		loc2=(location1[i],location2[i])
		dist=geodesic(loc1,loc2).km
        	print "Distance from point "+str(i)+" ="
		print dist
		if dist<dmin:
			dmin=dist
			point=i
	if(dmin<radius):
		return point
	else:
		return -1
 
def parseGPS(strx,file1):
    if strx.find('GGA') > 0:
	try:
	
        	msg = pynmea2.parse(strx)
		Lat=msg.lat
		Latdd = float(Lat[:2])
		Latmmmmm = float(Lat[2:])
		Latddmmmm = Latdd+(Latmmmmm/60.0)
		Lon =msg.lon 
		Londd = float(Lon[:3])
		Lonmmmmm = float(Lon[3:])
		Londdmmmm = Londd+(Lonmmmmm/60.0)
        #	print "Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude: %s %s -- Satellites: %s" % (msg.timestamp,Latddmmmm,msg.lat_dir, Londdmmmm,msg.lon_dir,msg.altitude,msg.altitude_units,msg.num_sats)
 		file1.write("%s,%s,%s,%s,%s,%s,%s,%s\n" % (msg.timestamp, Latddmmmm,msg.lat_dir, Londdmmmm,msg.lon_dir,msg.altitude,msg.altitude_units,msg.num_sats))
		SendLoc(Latddmmmm,Londdmmmm)
		print  [Latddmmmm,Londdmmmm]
		return [Latddmmmm,Londdmmmm]
	except:
		return 0
    else:
        return 0


try:
	serialPort = serial.Serial(port, baudrate = 9600, timeout = 0.5)
	print "serial port connected"
except:
	print "serial port unavailable"
cnt=0
while True:
    if cnt==0:
	setlocation()
	#print "printing locations"
	#print location1
	#print location2
    cnt=cnt+1
    file1 = open("testfile.txt", 'a')
    loc=0
    while loc==0:
	try:
		strx = serialPort.readline()
        except:
		print "error in reading gps readline"
		serialPort.close() 
		time.sleep(.05)
		try:
			serialPort = serial.Serial(port, baudrate = 9600, timeout = 0.5)
			print "Serial port reconnected"
		except:
			time.sleep(.005)
        		print "serial port unavailable"
		strx=" "
	loc=parseGPS(strx,file1)
    file1.close()
    print "Location=="
    print loc
    if cnt>=10:
        cnt=0
    if loc!=0:
	pnt=comploc(loc)
	if pnt>=0: 
	    SendData="Animal with DeviceID:"+DeviceID+" is near location: "+str(locid[pnt])
	    SendMail(SendData)
	    print "within radius"
    else:
	print "GPS read error" 
    #time.sleep(2) 

