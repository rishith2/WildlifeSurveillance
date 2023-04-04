# This code captures video analyse and detects specific objects 
# if found send the frame to server with info and send mails with detected object name to all emailids


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
print("its workingggggg===========")
DeviceID='0'
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
# Pretrained classes in the model
classNames = {0: 'background', 1: 'person', 2: 'bicycle', 3: 'car', 4: 'motorcycle', 5: 'airplane', 6: 'bus',7: 'train', 8: 'truck', 9: 'boat', 10: 'traffic light', 11: 'fire hydrant',
              13: 'stop sign', 14: 'parking meter', 15: 'bench', 16: 'bird', 17: 'cat',18: 'dog', 19: 'horse', 20: 'sheep', 21: 'cow', 22: 'elephant', 23: 'bear',
              24: 'zebra', 25: 'giraffe', 27: 'backpack', 28: 'umbrella', 31: 'handbag',
              32: 'tie', 33: 'suitcase', 34: 'frisbee', 35: 'skis', 36: 'snowboard',
              37: 'sports ball', 38: 'kite', 39: 'baseball bat', 40: 'baseball glove',
              41: 'skateboard', 42: 'surfboard', 43: 'tennis racket', 44: 'bottle',
              46: 'wine glass', 47: 'cup', 48: 'fork', 49: 'knife', 50: 'spoon',
              51: 'bowl', 52: 'banana', 53: 'apple', 54: 'sandwich', 55: 'orange',
              56: 'broccoli', 57: 'carrot', 58: 'hot dog', 59: 'pizza', 60: 'donut',
              61: 'cake', 62: 'chair', 63: 'couch', 64: 'potted plant', 65: 'bed',
              67: 'dining table', 70: 'toilet', 72: 'tv', 73: 'laptop', 74: 'mouse',
              75: 'remote', 76: 'keyboard', 77: 'cell phone', 78: 'microwave', 79: 'oven',
              80: 'toaster', 81: 'sink', 82: 'refrigerator', 84: 'book', 85: 'clock',
              86: 'vase', 87: 'scissors', 88: 'teddy bear', 89: 'hair drier', 90: 'toothbrush'}


def id_class_name(class_id, classes):
	for key, value in classes.items():
		if class_id == key:
			return value


# Loading model
model = cv2.dnn.readNetFromTensorflow('frozen_inference_graph.pb','ssd_mobilenet_v2_coco_2018_03_29.pbtxt')
# print(output[0,0,:,:].shape)


print("[INFO] starting video stream...")
#vs = VideoStream(src=0).start()
vs = VideoStream(usePiCamera=True).start()

time.sleep(2.0)
cnt=0
while True:
	frame= vs.read()
	cnt=cnt+1
	print(cnt)
	if cnt>2:
		cnt=0
		model.setInput(cv2.dnn.blobFromImage(frame, size=(300, 300), swapRB=True))
		output = model.forward()
		opS=''
		for detection in output[0, 0, :, :]:
			confidence = detection[2]
			if confidence > .5:
				class_id = detection[1]
				class_name=id_class_name(class_id,classNames)
				label = "{}: {:.2f}%".format(class_name,confidence * 100)
				opS=opS+label+","
		if opS!='':
			na="det%d.jpg" % current_milli_time()
			cv2.imwrite(na, frame)
			print(opS)
			#sendImage(na,opS)

vs.stop()
