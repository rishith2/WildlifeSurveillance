# This code captures video analyse and detects specific objects 
# if found send the frame to severver with info and send mails with detected object name to all emailids


from imutils.video import VideoStream
from imutils.video import FPS
from multiprocessing import Process
from multiprocessing import Queue
import numpy as np
import argparse
import imutils
import time
import cv2
import requests
import os
DeviceID='1'
oldtime1=0
Timedif1=5000 #ms 
current_milli_time = lambda: int(round(time.time() * 1000))
def sendImage(image_path,obj):
	global oldtime1

	url = 'http://poth.000webhostapp.com/animaltrack/detObjUl.php'
	image_filename = os.path.basename(image_path) 
	multipart_form_data = {
        	'image': (image_filename, open(image_path, 'rb')),
        	'obj': ('', obj),
        	'DeviceID': ('', DeviceID)
	} 
	response = requests.post(url,files=multipart_form_data)
	print("image uploaded")
	if ((current_milli_time()-oldtime1)>Timedif1):
		oldtime1=current_milli_time()
		print(response.status_code)
		data=obj+" is detected near device "+DeviceID
		with open('emaillist.txt') as f:
				mails = f.readlines()
				for id in mails:
					#"echo '"+data+"' | mailx -s 'Object detected in camera' "+id +" &"	
					print( "echo '"+data+"' | mailx -s 'Object detected in camera' "+id)
					os.system( "echo '"+data+"' | mailx -s 'Object detected in camera' "+id)
					

def classify_frame(net, inputQueue, outputQueue):
	while True:
		if not inputQueue.empty():
			frame = inputQueue.get()
			frame = cv2.resize(frame, (300, 300),interpolation=cv2.INTER_LINEAR)
			blob = cv2.dnn.blobFromImage(frame, 0.007843,(300, 300), 127.5)
			net.setInput(blob)
			detections = net.forward()
			outputQueue.put(detections)

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True,
	help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,
	help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.2,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

inputQueue = Queue(maxsize=1)
outputQueue = Queue(maxsize=1)
detections = None

print("[INFO] starting process...")
p = Process(target=classify_frame, args=(net, inputQueue,outputQueue,))
p.daemon = True
p.start()
print("[INFO] starting video stream...")
#vs = VideoStream(src=0).start()
vs = VideoStream(usePiCamera=True).start()

time.sleep(2.0)
cnt=0
while True:
	frame= vs.read()
	cnt=cnt+1
	#print(cnt)
	if cnt>3:
		cnt=0	
		(fH, fW) = frame.shape[:2]
		if inputQueue.empty():
			inputQueue.put(frame)
		if not outputQueue.empty():
			detections = outputQueue.get()
		if detections is not None:
			opS=''
			for i in np.arange(0, detections.shape[2]):
				confidence = detections[0, 0, i, 2]
				if confidence <args["confidence"]:
					continue
				idx = int(detections[0, 0, i, 1])
				label = "{}: {:.2f}%".format(CLASSES[idx],confidence * 100)
				opS=opS+","+label
			if opS!='':
				na="det%d.jpg" % current_milli_time()
				cv2.imwrite(na, frame)
				print(opS)
				sendImage(na,opS)
		else:
				na="det%d.jpg" % current_milli_time()
				cv2.imwrite(na, frame)

vs.stop()
