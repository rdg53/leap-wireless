##Ruben Guzman
##A server connection that sends wrist position data from a leap motion controller to a client 
import socket
import os, sys, inspect, thread, time,  select, msvcrt, struct
import re
import subprocess
import csv
import cPickle as pickle

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# Windows and Linux library locations, replace if your locations are different 
arch_dir = 'C:/LeapSDK/lib/x64' if sys.maxsize > 2**32 else '../lib/x86'

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap

class SampleListener(Leap.Listener):
	finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
	bone_names = ['Metacarpol', 'Proximal', 'Intermediate', 'Distal']


	def on_connect(self, controller):
		print "Connected to Leap Motion"
		
	def on_frame(self, controller):
		frame = controller.frame()
		print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d" % (frame.id, frame.timestamp, len(frame.hands), len(frame.fingers))
		
		#Create array variables for each finger on both(left and right) hands 
		#Left Hand Finger Data
		IndexLeftData = []
		ThumbLeftData = []
		MiddleLeftData = []
		RingLeftData = []
		PinkyLeftData = []
		
		#Right Hand Finger Data
		IndexRightData = []
		ThumbRightData = []
		MiddleRightData = []
		RingRightData = []
		PinkyRightData = []
		
		#create left hand
		leftHand = frame.hands.leftmost
		#create right hand
		rightHand = frame.hands.rightmost
		
		#Gather all the hand, finger, and bone data 
		#check if left hand is valid and continue
		if (leftHand.is_valid and leftHand.is_left) or (rightHand.is_valid and rightHand.is_right):
			
			#set wrist arrays for return
			leftWristPosition = [0,0,0]
			leftWristRotation = [0,0,0]
			rightWristPosition = [0,0,0]
			rightWristRotation = [0,0,0]
			
			#check for left hand data
			if (leftHand.is_valid and leftHand.is_left):
				#get wrist position
				leftWristPosition = frame.hands.leftmost.arm.wrist_position
				
				#get wrist rotation based on palm
				leftPalmPosition = leftHand.palm_position.normalized
				leftPalmNormal = leftHand.palm_normal
				leftPalmDirection = leftHand.direction
				leftPalmRotation = [(leftPalmDirection.pitch*Leap.RAD_TO_DEG),(leftPalmNormal.roll*Leap.RAD_TO_DEG),(leftPalmDirection.yaw*Leap.RAD_TO_DEG)]
				leftWristRotation = [((leftPalmRotation[0]+360)%360),((leftPalmRotation[1]+360)%360),((leftPalmRotation[2]+360)%360)]
				
				#Gather all the finger data 
				for finger in leftHand.fingers:
					#print "Type: " + self.finger_names[finger.type]
					
					#Check if finer is index finger
					if self.finger_names[finger.type] == "Index":
						#print self.finger_names[finger.type]
						
						#loop for all the bones in finger
						for b in range(0,4):
							
							#if the bone exists gather data
							if finger.bone(b).is_valid:
								bone = finger.bone(b)
								#print self.bone_names[bone.type]
								rotations = []
								
								#rotation data for the bone and append it to the rotation array
								rot = [(bone.direction.pitch*Leap.RAD_TO_DEG),(bone.center.roll*Leap.RAD_TO_DEG),(bone.direction.yaw*Leap.RAD_TO_DEG)]
								#print rot[0]
								
								#normalize -180-180 to 0-360 and append roations
								rotations.append((rot[0]))
								rotations.append((rot[1]))
								rotations.append((rot[2]))
								IndexLeftData.append(list((self.bone_names[bone.type],rotations)))
					
					#check if finger is thumb
					if self.finger_names[finger.type] == "Thumb":
						#print self.finger_names[finger.type]
						
						#loop for all the bones in the finger
						for b in range(0,4):
							
							#if the bone exists gather data
							if finger.bone(b).is_valid:
								bone = finger.bone(b)
								rotations = []
								rot = [(bone.direction.pitch*Leap.RAD_TO_DEG),(bone.center.roll*Leap.RAD_TO_DEG),(bone.direction.yaw*Leap.RAD_TO_DEG)]
								
								#normalize -180-180 to 0-360 and append roations
								rotations.append((rot[0]))
								rotations.append((rot[1]))
								rotations.append((rot[2]))
								ThumbLeftData.append(list((self.bone_names[bone.type],rotations)))
					
					#check if finger is middle
					if self.finger_names[finger.type] == "Middle":
						#print self.finger_names[finger.type]
						
						#loop for all the bones in the finger
						for b in range(0,4):
							
							#if the bone exists gather data
							if finger.bone(b).is_valid:
								bone = finger.bone(b)
								#print self.bone_names[bone.type]
								rotations = []
								rot = [(bone.direction.pitch*Leap.RAD_TO_DEG),(bone.center.roll*Leap.RAD_TO_DEG),(bone.direction.yaw*Leap.RAD_TO_DEG)]
								
								#normalize -180-180 to 0-360 and append roations
								rotations.append((rot[0]))
								rotations.append((rot[1]))
								rotations.append((rot[2]))
								MiddleLeftData.append(list((self.bone_names[bone.type],rotations)))
					
					#check if finger is ring finger
					if self.finger_names[finger.type] == "Ring":
						#print self.finger_names[finger.type]
						
						#loop for all the bones in the finger
						for b in range(0,4):
							
							#if the bone exists gather data
							if finger.bone(b).is_valid:
								bone = finger.bone(b)
								rotations = []
								rot = [(bone.direction.pitch*Leap.RAD_TO_DEG),(bone.center.roll*Leap.RAD_TO_DEG),(bone.direction.yaw*Leap.RAD_TO_DEG)]
								
								#normalize -180-180 to 0-360 and append roations
								rotations.append((rot[0]))
								rotations.append((rot[1]))
								rotations.append((rot[2]))
								RingLeftData.append(list((self.bone_names[bone.type],rotations)))
					
					#check if the finger is pinky finger
					if self.finger_names[finger.type] == "Pinky":
						#print self.finger_names[finger.type]
						
						#loop for all the bones in the finger
						for b in range(0,4):
						
							#if bone exists gather data
							if finger.bone(b).is_valid:
								bone = finger.bone(b)
								rotations = []
								rot = [(bone.direction.pitch*Leap.RAD_TO_DEG),(bone.center.roll*Leap.RAD_TO_DEG),(bone.direction.yaw*Leap.RAD_TO_DEG)]
								
								#normalize -180-180 to 0-360 and append roations
								rotations.append((rot[0]))
								rotations.append((rot[1]))
								rotations.append((rot[2]))
								PinkyLeftData.append(list((self.bone_names[bone.type],rotations)))
			
			if (rightHand.is_valid and rightHand.is_right):
				#get wrist position
				rightWristPosition = frame.hands.rightmost.arm.wrist_position
				
				#get wrist rotation based on palm
				rightPalmPosition = rightHand.palm_position.normalized
				rightPalmNormal = rightHand.palm_normal
				rightPalmDirection = rightHand.direction
				rightPalmRotation = [(rightPalmDirection.pitch*Leap.RAD_TO_DEG),(rightPalmNormal.roll*Leap.RAD_TO_DEG),(rightPalmDirection.yaw*Leap.RAD_TO_DEG)]
				rightWristRotation = [((rightPalmRotation[0]+360)%360),((rightPalmRotation[1]+360)%360),((rightPalmRotation[2]+360)%360)]
			
				#Gather all the finger data 
				for finger in rightHand.fingers:
					#print "Type: " + self.finger_names[finger.type]
					
					#Check if finer is index finger
					if self.finger_names[finger.type] == "Index":
						#print self.finger_names[finger.type]
						
						#loop for all the bones in finger
						for b in range(0,4):
							
							#if the bone exists gather data
							if finger.bone(b).is_valid:
								bone = finger.bone(b)
								#print self.bone_names[bone.type]
								rotations = []
								
								#rotation data for the bone and append it to the rotation array
								rot = [(bone.direction.pitch*Leap.RAD_TO_DEG),(bone.center.roll*Leap.RAD_TO_DEG),(bone.direction.yaw*Leap.RAD_TO_DEG)]
								#print rot[0]
								
								#normalize -180-180 to 0-360 and append roations
								rotations.append((rot[0]))
								rotations.append((rot[1]))
								rotations.append((rot[2]))
								IndexRightData.append(list((self.bone_names[bone.type],rotations)))
					
					#check if finger is thumb
					if self.finger_names[finger.type] == "Thumb":
						#print self.finger_names[finger.type]
						
						#loop for all the bones in the finger
						for b in range(0,4):
							
							#if the bone exists gather data
							if finger.bone(b).is_valid:
								bone = finger.bone(b)
								rotations = []
								rot = [(bone.direction.pitch*Leap.RAD_TO_DEG),(bone.center.roll*Leap.RAD_TO_DEG),(bone.direction.yaw*Leap.RAD_TO_DEG)]
								
								#normalize -180-180 to 0-360 and append roations
								rotations.append((rot[0]))
								rotations.append((rot[1]))
								rotations.append((rot[2]))
								ThumbRightData.append(list((self.bone_names[bone.type],rotations)))
					
					#check if finger is middle
					if self.finger_names[finger.type] == "Middle":
						#print self.finger_names[finger.type]
						
						#loop for all the bones in the finger
						for b in range(0,4):
							
							#if the bone exists gather data
							if finger.bone(b).is_valid:
								bone = finger.bone(b)
								#print self.bone_names[bone.type]
								rotations = []
								rot = [(bone.direction.pitch*Leap.RAD_TO_DEG),(bone.center.roll*Leap.RAD_TO_DEG),(bone.direction.yaw*Leap.RAD_TO_DEG)]
								
								#normalize -180-180 to 0-360 and append roations
								rotations.append((rot[0]))
								rotations.append((rot[1]))
								rotations.append((rot[2]))
								MiddleRightData.append(list((self.bone_names[bone.type],rotations)))
					
					#check if finger is ring finger
					if self.finger_names[finger.type] == "Ring":
						#print self.finger_names[finger.type]
						
						#loop for all the bones in the finger
						for b in range(0,4):
							
							#if the bone exists gather data
							if finger.bone(b).is_valid:
								bone = finger.bone(b)
								rotations = []
								rot = [(bone.direction.pitch*Leap.RAD_TO_DEG),(bone.center.roll*Leap.RAD_TO_DEG),(bone.direction.yaw*Leap.RAD_TO_DEG)]
								
								#normalize -180-180 to 0-360 and append roations
								rotations.append((rot[0]))
								rotations.append((rot[1]))
								rotations.append((rot[2]))
								RingRightData.append(list((self.bone_names[bone.type],rotations)))
					
					#check if the finger is pinky finger
					if self.finger_names[finger.type] == "Pinky":
						#print self.finger_names[finger.type]
						
						#loop for all the bones in the finger
						for b in range(0,4):
						
							#if bone exists gather data
							if finger.bone(b).is_valid:
								bone = finger.bone(b)
								rotations = []
								rot = [(bone.direction.pitch*Leap.RAD_TO_DEG),(bone.center.roll*Leap.RAD_TO_DEG),(bone.direction.yaw*Leap.RAD_TO_DEG)]
								
								#normalize -180-180 to 0-360 and append roations
								rotations.append((rot[0]))
								rotations.append((rot[1]))
								rotations.append((rot[2]))
								PinkyRightData.append(list((self.bone_names[bone.type],rotations)))
			
			#print leftWristPosition, leftWristRotation, rightWristPosition, rightWristRotation
			return frame.id, leftWristPosition, leftWristRotation, rightWristPosition, rightWristRotation, IndexLeftData, ThumbLeftData, MiddleLeftData, RingLeftData, PinkyLeftData, IndexRightData, ThumbRightData, MiddleRightData, RingRightData, PinkyRightData
		else:
			return frame.id , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	
	
	def on_disconnect(self, controller):
		controller.remove_listener(self)
		return "Disconnected Leap Motion"


def main():

	#create socket
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#get local machine name
	host = socket.gethostname()

	port = 9999

	#bind the port
	serversocket.bind((host, port))

	#queue up requests
	serversocket.listen(5)

	
	#create leap controller and listener
	listener = SampleListener()
	controller = Leap.Controller()
	
	
	controller.add_listener(listener)
	
	#true if leap is connected
	connected = listener.on_connect(controller)
	
	#set last frame
	oldFrame, leftWristPosition, leftWristRotation, rightWristPosition, rightWristRotation, IndexLeftData, ThumbLeftData, MiddleLeftData, RingLeftData, PinkyLeftData, IndexRightData, ThumbRightData, MiddleRightData, RingRightData, PinkyRightData = listener.on_frame(controller)
	
	#establish connection
	clientsocket,addr = serversocket.accept()
	
	#create csv
	dir = os.path.dirname(os.path.realpath(__file__))
	csv = open(str(dir.replace("\\","/")) + "/animDataServer.csv", 'w+b')
	
	#set some variables for counting and checking
	frameCount = 0
	
	#parse frame data to frame number and wrist position and send to the client pc
	while True:
		if not msvcrt.kbhit():
			#print listener.on_frame(controller)
			if oldFrame != listener.on_frame(controller)[0]:
				if str(leftWristPosition) != '0':
				#if we have legit values continue
					if (leftWristPosition[0]==0) and (leftWristPosition[1]==0) and (leftWristPosition[2]==0):
						#write 0's if we cant find wrist
						csv.write(('"leftWrist"')+","+str(frameCount)+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+"\n")
						#clientsocket.send(('leftWrist')+","+str(frameCount)+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0")
						#clientsocket.sendall('leftWrist'+","+str(frameCount)+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"\n")
					else:
						leftWristPosition = re.sub('[()]', '', str(leftWristPosition))
						leftWristPosition = re.sub(r'\s+', '', str(leftWristPosition))
						
						csv.write(('"leftWrist"')+","+str(frameCount)+","+str(leftWristPosition)+","+str(360-leftWristRotation[1])+","+str(leftWristRotation[0])+","+str(leftWristRotation[2])+","+"\n")
						#clientsocket.sendall('leftWrist'+","+str(frameCount)+","+str(leftWristPosition)+","+str(round(360-leftWristRotation[1],2))+","+str(round(leftWristRotation[0],2))+","+str(round(leftWristRotation[2],2))+","+"\n")
						
						for i in range(0,4):
							csv.write(('"Left Thumb "')+str(ThumbLeftData[i][0])+":"+","+str(frameCount)+","+str(ThumbLeftData[i][1][0])+","+str(ThumbLeftData[i][1][1])+","+str(ThumbLeftData[i][1][2])+"\n")
							#clientsocket.sendall('Left Thumb '+str(ThumbLeftData[i][0])+":"+","+str(frameCount)+","+str(round(ThumbLeftData[i][1][0],2))+","+str(round(ThumbLeftData[i][1][1],2))+","+str(round(ThumbLeftData[i][1][2],2))+","+"\n")							
						for i in range(0,4):
							csv.write(('"Left Index "')+str(IndexLeftData[i][0])+":"+","+str(frameCount)+","+str(IndexLeftData[i][1][0])+","+str(IndexLeftData[i][1][1])+","+str(IndexLeftData[i][1][2])+"\n")
							#clientsocket.sendall('Left Index '+str(IndexLeftData[i][0])+":"+","+str(frameCount)+","+str(round(IndexLeftData[i][1][0],2))+","+str(round(IndexLeftData[i][1][1],2))+","+str(round(IndexLeftData[i][1][2],2))+","+"\n")
						for i in range(0,4):
							csv.write(('"Left Middle "')+str(MiddleLeftData[i][0])+":"+","+str(frameCount)+","+str(MiddleLeftData[i][1][0])+","+str(MiddleLeftData[i][1][1])+","+str(MiddleLeftData[i][1][2])+"\n")
							#clientsocket.sendall('Left Middle '+str(MiddleLeftData[i][0])+":"+","+str(frameCount)+","+str(round(MiddleLeftData[i][1][0],2))+","+str(round(MiddleLeftData[i][1][1],2))+","+str(round(MiddleLeftData[i][1][2],2))+","+"\n")
						for i in range(0,4):
							csv.write(('"Left Ring "')+str(RingLeftData[i][0])+":"+","+str(frameCount)+","+str(RingLeftData[i][1][0])+","+str(RingLeftData[i][1][1])+","+str(RingLeftData[i][1][2])+"\n")
							#clientsocket.sendall('Left Ring '+str(RingLeftData[i][0])+":"+","+str(frameCount)+","+str(round(RingLeftData[i][1][0],2))+","+str(round(RingLeftData[i][1][1],2))+","+str(round(RingLeftData[i][1][2],2))+","+"\n")
						for i in range(0,4):	
							csv.write(('"Left Pinky "')+str(PinkyLeftData[i][0])+":"+","+str(frameCount)+","+str(PinkyLeftData[i][1][0])+","+str(PinkyLeftData[i][1][1])+","+str(PinkyLeftData[i][1][2])+"\n")
							#clientsocket.sendall('Left Pinky '+str(PinkyLeftData[i][0])+":"+","+str(frameCount)+","+str(round(PinkyLeftData[i][1][0],2))+","+str(round(PinkyLeftData[i][1][1],2))+","+str(round(PinkyLeftData[i][1][2],2))+","+"\n")

				if (str(rightWristPosition) != '0'):
					#if we have legit values continue
					if (rightWristPosition[0]==0) and (rightWristPosition[1]==0) and (rightWristPosition[2]==0):
						csv.write(('"rightWrist"')+","+str(frameCount)+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+"\n")
						#clientsocket.send(('rightWrist')+","+str(frameCount)+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0")
					else:
						#write wrist location and rotations and bone rotations
						rightWristPosition = re.sub('[()]', '', str(rightWristPosition))
						rightWristPosition = re.sub(r'\s+', '', str(rightWristPosition))
						
						csv.write(('"rightWrist"')+","+str(frameCount)+","+str(rightWristPosition)+","+str(360-rightWristRotation[1])+","+str(rightWristRotation[0])+","+str(rightWristRotation[2])+","+"\n")		
						#clientsocket.send(('rightWrist')+","+str(frameCount)+","+str(rightWristPosition)+","+str(360-rightWristRotation[1])+","+str(rightWristRotation[0])+","+str(rightWristRotation[2]))		
						
						for i in range(0,4):
							csv.write(('"Right Thumb "')+str(ThumbRightData[i][0])+":"+","+str(frameCount)+","+str(ThumbRightData[i][1][0])+","+str(ThumbRightData[i][1][1])+","+str(ThumbRightData[i][1][2])+"\n")
						for i in range(0,4):
							csv.write(('"Right Index "')+str(IndexRightData[i][0])+":"+","+str(frameCount)+","+str(IndexRightData[i][1][0])+","+str(IndexRightData[i][1][1])+","+str(IndexRightData[i][1][2])+"\n")
						for i in range(0,4):
							csv.write(('"Right Middle "')+str(MiddleRightData[i][0])+":"+","+str(frameCount)+","+str(MiddleRightData[i][1][0])+","+str(MiddleRightData[i][1][1])+","+str(MiddleRightData[i][1][2])+"\n")
						for i in range(0,4):
							csv.write(('"Right Ring "')+str(RingRightData[i][0])+":"+","+str(frameCount)+","+str(RingRightData[i][1][0])+","+str(RingRightData[i][1][1])+","+str(RingRightData[i][1][2])+"\n")
						for i in range(0,4):	
							csv.write(('"Right Pinky "')+str(PinkyRightData[i][0])+":"+","+str(frameCount)+","+str(PinkyRightData[i][1][0])+","+str(PinkyRightData[i][1][1])+","+str(PinkyRightData[i][1][2])+"\n")
				oldFrame, leftWristPosition, leftWristRotation, rightWristPosition, rightWristRotation, IndexLeftData, ThumbLeftData, MiddleLeftData, RingLeftData, PinkyLeftData, IndexRightData, ThumbRightData, MiddleRightData, RingRightData, PinkyRightData = listener.on_frame(controller)
				frameCount += 1
		else:
			print listener.on_disconnect(controller)
			break

	#handle data transfer
	csv.seek(0)
	data = csv.read(1024)
	while (data):
		print 'Sending Leap Motion data...'
		clientsocket.send(data)
		data = csv.read(1024)
	csv.close()
	print "Sent Data and Closing"
	clientsocket.shutdown(socket.SHUT_WR)
		

if __name__=="__main__":
	main()