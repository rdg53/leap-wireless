##Ruben Guzman
##Gets leap motion data from a CSV file and keys it to the selected hand bones of the given skeleton "leapmotionskeleton.fbx"
##The skeleton can be replaced if the bones are named the same
import os, sys, inspect
from pyfbsdk import *
import csv
import re


#get a list of the selected models
selectedModels = FBModelList()
FBGetSelectedModels(selectedModels, None, True, True)

#create an array to hold left hand bones
LeftHandMiddle = [0,0,0,0]
LeftHandThumb = [0,0,0,0]
LeftHandIndex = [0,0,0,0]
LeftHandRing = [0,0,0,0]
LeftHandPinky = [0,0,0,0]

#create an array to hold right hand bones
RightHandMiddle = [0,0,0,0]
RightHandThumb = [0,0,0,0]
RightHandIndex = [0,0,0,0]
RightHandRing = [0,0,0,0]
RightHandPinky = [0,0,0,0]

rightHand = 0
leftHand = 0

#parse through selected models and append them to the appropriate array or model
for model in selectedModels:
    if "LeftHandThumb" in model.LongName:
        if "1" in model.LongName:
            LeftHandThumb[0] = model
        elif "2" in model.LongName:
            LeftHandThumb[1] = model
        elif "3" in model.LongName:
            LeftHandThumb[2] = model
        #set hand bones to be animatable
        model.Translation.SetAnimated(True)
        model.Rotation.SetAnimated(True)
    elif "LeftHandIndex" in model.LongName:
        if "1" in model.LongName:
            LeftHandIndex[0] = model
        elif "2" in model.LongName:
            LeftHandIndex[1] = model
        elif "3" in model.LongName:
            LeftHandIndex[2] = model
        elif "4" in model.LongName:
            LeftHandIndex[3] = model
        #set hand bones to be animatable
        model.Translation.SetAnimated(True)
        model.Rotation.SetAnimated(True)
    elif "LeftHandMiddle" in model.LongName:
        if "1" in model.LongName:
            LeftHandMiddle[0] = model
        elif "2" in model.LongName:
            LeftHandMiddle[1] = model
        elif "3" in model.LongName:
            LeftHandMiddle[2] = model
        elif "4" in model.LongName:
            LeftHandMiddle[3] = model
        #set hand bones to be animatable
        model.Translation.SetAnimated(True)
        model.Rotation.SetAnimated(True)
    elif "LeftHandRing" in model.LongName:
        if "1" in model.LongName:
            LeftHandRing[0] = model
        elif "2" in model.LongName:
            LeftHandRing[1] = model
        elif "3" in model.LongName:
            LeftHandRing[2] = model
        elif "4" in model.LongName:
            LeftHandRing[3] = model
        #set hand bones to be animatable
        model.Translation.SetAnimated(True)
        model.Rotation.SetAnimated(True)
    elif "LeftHandPinky" in model.LongName:
        if "1" in model.LongName:
            LeftHandPinky[0] = model
        elif "2" in model.LongName:
            LeftHandPinky[1] = model
        elif "3" in model.LongName:
            LeftHandPinky[2] = model
        elif "4" in model.LongName:
            LeftHandPinky[3] = model
        #set hand bones to be animatable
        model.Translation.SetAnimated(True)
        model.Rotation.SetAnimated(True)
    elif model.LongName == "LeftHand":
        leftHand = model
        #set left hand translation and rotation to be animatable 
        leftHand.Translation.SetAnimated(True)    
        leftHand.Rotation.SetAnimated(True)
        #create offsets for left x,y,z (starting locations)
        xLHOffset = leftHand.Translation.GetAnimationNode().Nodes[0].FCurve.Evaluate(FBTime(0,0,0,0))
        yLHffset = leftHand.Translation.GetAnimationNode().Nodes[1].FCurve.Evaluate(FBTime(0,0,0,0))
        zLHffset = leftHand.Translation.GetAnimationNode().Nodes[2].FCurve.Evaluate(FBTime(0,0,0,0))
    elif "RightHandThumb" in model.LongName:
        if "1" in model.LongName:
            RightHandThumb[0] = model
        elif "2" in model.LongName:
            RightHandThumb[1] = model
        elif "3" in model.LongName:
            RightHandThumb[2] = model
        #set hand bones to be animatable
        model.Translation.SetAnimated(True)
        model.Rotation.SetAnimated(True)
    elif "RightHandIndex" in model.LongName:
        if "1" in model.LongName:
            RightHandIndex[0] = model
        elif "2" in model.LongName:
            RightHandIndex[1] = model
        elif "3" in model.LongName:
            RightHandIndex[2] = model
        elif "4" in model.LongName:
            RightHandIndex[3] = model      
        #set hand bones to be animatable
        model.Translation.SetAnimated(True)
        model.Rotation.SetAnimated(True)
    elif "RightHandMiddle" in model.LongName:
        if "1" in model.LongName:
            RightHandMiddle[0] = model
        elif "2" in model.LongName:
            RightHandMiddle[1] = model
        elif "3" in model.LongName:
            RightHandMiddle[2] = model
        elif "4" in model.LongName:
            RightHandMiddle[3] = model
        #set hand bones to be animatable
        model.Translation.SetAnimated(True)
        model.Rotation.SetAnimated(True)
    elif "RightHandRing" in model.LongName:
        if "1" in model.LongName:
            RightHandRing[0] = model
        elif "2" in model.LongName:
            RightHandRing[1] = model
        elif "3" in model.LongName:
            RightHandRing[2] = model
        elif "4" in model.LongName:
            RightHandRing[3] = model
        #set hand bones to be animatable      
        model.Translation.SetAnimated(True)
        model.Rotation.SetAnimated(True)
    elif "RightHandPinky" in model.LongName:
        if "1" in model.LongName:
            RightHandPinky[0] = model
        elif "2" in model.LongName:
            RightHandPinky[1] = model
        elif "3" in model.LongName:
            RightHandPinky[2] = model
        elif "4" in model.LongName:
            RightHandPinky[3] = model
        #set hand bones to be animatable
        model.Translation.SetAnimated(True)
        model.Rotation.SetAnimated(True)
    elif model.LongName == "RightHand":
        rightHand = model
        #set right hand translation and rotation to be animatable 
        rightHand.Translation.SetAnimated(True)
        rightHand.Rotation.SetAnimated(True)
        #create offsets for right x,y,z (starting locations)
        xRHOffset = rightHand.Translation.GetAnimationNode().Nodes[0].FCurve.Evaluate(FBTime(0,0,0,0))
        yRHffset = rightHand.Translation.GetAnimationNode().Nodes[1].FCurve.Evaluate(FBTime(0,0,0,0))
        zRHffset = rightHand.Translation.GetAnimationNode().Nodes[2].FCurve.Evaluate(FBTime(0,0,0,0))
    else:
        print 'no hand selected'

pitchOffset = 0
rollOffset = 0
yawOffset = 0

TranslateArrayAll = []
        
#keep track of frames  
frameCount = 0
startFrame = 0
currentFrame = 0
prevFrame = 0

#read through csv
#get wrist position and rotation for both hands
#0='leftWrist''rightWrist',1=frame,2=x position,left 3=y position,4=z position,5=pitch,6=yaw,7=roll
with open("C:/Users/Ruben/Onedrive/Desktop/animData3.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        #print row[0] , row[1] , row[2], row[3], row[4], row[5], row[6], row[7]
        currentFrame = int(row[1])        
        print frameCount
        if currentFrame == prevFrame:
            if 'leftWrist' in row[0]:
                if leftHand != 0:
                    #print leftHand.Translation.GetAnimationNode().Nodes[0].FCurve.Evaluate(FBTime(0,0,0,frameCount))
                    #Add keys to wrist location and rotation, divide by 1000 for millimeters
                    leftHand.Translation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount), ((row[2]/1000)+xLHOffset))
                    leftHand.Translation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount), ((row[3]/1000)+yLHffset))
                    leftHand.Translation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount), ((row[4]/1000)+zLHffset))
                    leftHand.Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount), (row[5]))
                    leftHand.Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount), (row[6]))
                    leftHand.Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount), (row[7]))
            elif "Left Thumb Prox" in row[0]:
                if LeftHandThumb[0] != 0:
					#thumb rotations with offsets
                    LeftHandThumb[0].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(-row[2]+45))
                    LeftHandThumb[0].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandThumb[0].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(-row[4])+45)
            elif "Left Thumb Inter" in row[0]:
                if LeftHandThumb[1] != 0:
					#thumb rotations with offsets
                    LeftHandThumb[1].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandThumb[1].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandThumb[1].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(-row[4]+45))
            elif "Left Index Met" in row[0]:
                if LeftHandIndex[0] != 0:
					#thumb rotations with offsets
                    LeftHandIndex[0].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]+90))
                    LeftHandIndex[0].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]-10))
                    LeftHandIndex[0].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Index Prox" in row[0]:
                if LeftHandIndex[1] != 0:
					#index rotations with offsets
                    LeftHandIndex[1].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandIndex[1].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandIndex[1].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Index Inter" in row[0]:
                if LeftHandIndex[2] != 0:
					#index rotations with offsets
                    LeftHandIndex[2].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandIndex[2].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandIndex[2].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Index Dist" in row[0]:
                if LeftHandIndex[3] != 0:
					#index rotations with offsets
                    LeftHandIndex[3].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandIndex[3].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandIndex[3].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Middle Met" in row[0]:
                if LeftHandMiddle[0] != 0:
					#index rotations with offsets
                    LeftHandMiddle[0].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]+90))
                    LeftHandMiddle[0].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]-20))
                    LeftHandMiddle[0].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Middle Prox" in row[0]:
                if LeftHandMiddle[1] != 0:
					#middle rotations with offsets
                    LeftHandMiddle[1].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandMiddle[1].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandMiddle[1].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Middle Inter" in row[0]:
                if LeftHandMiddle[2] != 0:
					#middle rotations with offsets
                    LeftHandMiddle[2].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandMiddle[2].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandMiddle[2].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Middle Dist" in row[0]:
                if LeftHandMiddle[3] != 0:
					#middle rotations with offsets
                    LeftHandMiddle[3].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandMiddle[3].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandMiddle[3].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Ring Met" in row[0]:
                if LeftHandRing[0] != 0:
					#ring rotations with offsets
                    LeftHandRing[0].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]+90))
                    LeftHandRing[0].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]-30))
                    LeftHandRing[0].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Ring Prox" in row[0]:
                if LeftHandRing[1] != 0:
					#ring rotations with offsets
                    LeftHandRing[1].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandRing[1].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandRing[1].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Ring Inter" in row[0]:
                if LeftHandRing[2] != 0:
					#ring rotations with offsets
                    LeftHandRing[2].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandRing[2].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandRing[2].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Ring Dist" in row[0]:
                if LeftHandRing[3] != 0:
					#ring rotations with offsets
                    LeftHandRing[3].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandRing[3].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandRing[3].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Pinky Met" in row[0]:
                if LeftHandPinky[0] != 0:
					#pinky rotations with offsets
                    LeftHandPinky[0].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]+90))
                    LeftHandPinky[0].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]-40))
                    LeftHandPinky[0].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Pinky Prox" in row[0]:
                if LeftHandPinky[1] != 0:
					#pinky rotations with offsets
                    LeftHandPinky[1].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandPinky[1].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandPinky[1].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Pinky Inter" in row[0]:
                if LeftHandPinky[2] != 0:
					#pinky rotations with offsets
                    LeftHandPinky[2].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandPinky[2].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandPinky[2].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Pinky Dist" in row[0]:
                if LeftHandPinky[3] != 0:
					#pinky rotations with offsets
                    LeftHandPinky[3].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandPinky[3].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandPinky[3].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif 'rightWrist' in row[0]:
                if rightHand != 0:
                    #print rightHand.Translation.GetAnimationNode().Nodes[0].FCurve.Evaluate(FBTime(0,0,0,frameCount))
                    #Add keys to wrist location and rotation, divide by 1000 for millimeters
                    rightHand.Translation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount), ((row[2]/1000)+xRHOffset))
                    rightHand.Translation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount), ((row[3]/1000)+yRHffset))
                    rightHand.Translation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount), ((row[4]/1000)+zRHffset))
                    rightHand.Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount), (row[5]))
                    rightHand.Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount), (row[6]))
                    rightHand.Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount), (row[7])) 
            elif "Right Thumb Prox" in row[0]:
                if RightHandThumb[0] != 0:
					#thumb rotations with offsets
                    RightHandThumb[0].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]-180))
                    RightHandThumb[0].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]+45))
                    RightHandThumb[0].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4])+90)
            elif "Right Thumb Inter" in row[0]:
                if RightHandThumb[1] != 0:
					#thumb rotations with offsets
                    RightHandThumb[1].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandThumb[1].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandThumb[1].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Index Met" in row[0]:
                if RightHandIndex[0] != 0:
					#index rotations with offsets
                    RightHandIndex[0].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]+180))
                    RightHandIndex[0].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]+40))
                    RightHandIndex[0].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]+45))
            elif "Right Index Prox" in row[0]:
                if RightHandIndex[1] != 0:
					#index rotations with offsets
                    RightHandIndex[1].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandIndex[1].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandIndex[1].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Index Inter" in row[0]:
                if RightHandIndex[2] != 0:
					#index rotations with offsets
                    RightHandIndex[2].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandIndex[2].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandIndex[2].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Index Dist" in row[0]:
                if RightHandIndex[3] != 0:
					#index rotations with offsets
                    RightHandIndex[3].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandIndex[3].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandIndex[3].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Middle Met" in row[0]:
                if RightHandMiddle[0] != 0:
					#middle rotations with offsets
                    RightHandMiddle[0].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]+180))
                    RightHandMiddle[0].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]+30))
                    RightHandMiddle[0].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]+45))
            elif "Right Middle Prox" in row[0]:
                if RightHandMiddle[1] != 0:
					#middle rotations with offsets
                    RightHandMiddle[1].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandMiddle[1].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandMiddle[1].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Middle Inter" in row[0]:
                if RightHandMiddle[2] != 0:
					#middle rotations with offsets
                    RightHandMiddle[2].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandMiddle[2].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandMiddle[2].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Middle Dist" in row[0]:
                if RightHandMiddle[3] != 0:
					#middle rotations with offsets
                    RightHandMiddle[3].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandMiddle[3].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandMiddle[3].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Ring Met" in row[0]:
                if RightHandRing[0] != 0:
					#ring rotations with offsets
                    RightHandRing[0].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]+180))
                    RightHandRing[0].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]+20))
                    RightHandRing[0].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]+45))
            elif "Right Ring Prox" in row[0]:
                if RightHandRing[1] != 0:
					#ring rotations with offsets
                    RightHandRing[1].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandRing[1].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandRing[1].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Ring Inter" in row[0]:
                if RightHandRing[2] != 0:
					#ring rotations with offsets
                    RightHandRing[2].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandRing[2].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandRing[2].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Ring Dist" in row[0]:
                if RightHandRing[3] != 0:
					#ring rotations with offsets
                    RightHandRing[3].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandRing[3].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandRing[3].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Pinky Met" in row[0]:
                if RightHandPinky[0] != 0:
					#pinky rotations with offsets
                    RightHandPinky[0].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]+180))
                    RightHandPinky[0].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]+10))
                    RightHandPinky[0].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]+45))
            elif "Right Pinky Prox" in row[0]:
                if RightHandPinky[1] != 0:
					#pinky rotations with offsets
                    RightHandPinky[1].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandPinky[1].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandPinky[1].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Pinky Inter" in row[0]:
                if RightHandPinky[2] != 0:
					#pinky rotations with offsets
                    RightHandPinky[2].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandPinky[2].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandPinky[2].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Pinky Dist" in row[0]:
                if RightHandPinky[3] != 0:
					#pinky rotations with offsets
                    RightHandPinky[3].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandPinky[3].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandPinky[3].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))   
        elif currentFrame != prevFrame:
            frameCount += 1
            if 'leftWrist' in row[0]:
                if leftHand != 0:
                    #print leftHand.Translation.GetAnimationNode().Nodes[0].FCurve.Evaluate(FBTime(0,0,0,frameCount))
                    #Add keys to wrist location and rotation, divide by 1000 for millimeters
                    leftHand.Translation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount), ((row[2]/1000)+xLHOffset))
                    leftHand.Translation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount), ((row[3]/1000)+yLHffset))
                    leftHand.Translation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount), ((row[4]/1000)+zLHffset))
                    leftHand.Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount), (row[5]))
                    leftHand.Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount), (row[6]))
                    leftHand.Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount), (row[7]))
            elif "Left Thumb Prox" in row[0]:
                if LeftHandThumb[0] != 0:
                    LeftHandThumb[0].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(-row[2]+45))
                    LeftHandThumb[0].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandThumb[0].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(-row[4])+45)
            elif "Left Thumb Inter" in row[0]:
                if LeftHandThumb[1] != 0:
                    LeftHandThumb[1].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandThumb[1].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandThumb[1].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(-row[4]+45))
            elif "Left Index Met" in row[0]:
                if LeftHandIndex[0] != 0:
                    LeftHandIndex[0].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]+90))
                    LeftHandIndex[0].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]-10))
                    LeftHandIndex[0].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Index Prox" in row[0]:
                if LeftHandIndex[1] != 0:
                    LeftHandIndex[1].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandIndex[1].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandIndex[1].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Index Inter" in row[0]:
                if LeftHandIndex[2] != 0:
                    LeftHandIndex[2].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandIndex[2].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandIndex[2].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Index Dist" in row[0]:
                if LeftHandIndex[3] != 0:
                    LeftHandIndex[3].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandIndex[3].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandIndex[3].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Middle Met" in row[0]:
                if LeftHandMiddle[0] != 0:
                    LeftHandMiddle[0].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]+90))
                    LeftHandMiddle[0].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]-20))
                    LeftHandMiddle[0].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Middle Prox" in row[0]:
                if LeftHandMiddle[1] != 0:
                    LeftHandMiddle[1].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandMiddle[1].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandMiddle[1].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Middle Inter" in row[0]:
                if LeftHandMiddle[2] != 0:
                    LeftHandMiddle[2].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandMiddle[2].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandMiddle[2].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Middle Dist" in row[0]:
                if LeftHandMiddle[3] != 0:
                    LeftHandMiddle[3].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandMiddle[3].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandMiddle[3].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Ring Met" in row[0]:
                if LeftHandRing[0] != 0:
                    LeftHandRing[0].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]+90))
                    LeftHandRing[0].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]-30))
                    LeftHandRing[0].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Ring Prox" in row[0]:
                if LeftHandRing[1] != 0:
                    LeftHandRing[1].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandRing[1].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandRing[1].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Ring Inter" in row[0]:
                if LeftHandRing[2] != 0:
                    LeftHandRing[2].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandRing[2].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandRing[2].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Ring Dist" in row[0]:
                if LeftHandRing[3] != 0:
                    LeftHandRing[3].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandRing[3].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandRing[3].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Pinky Met" in row[0]:
                if LeftHandPinky[0] != 0:
                    LeftHandPinky[0].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]+90))
                    LeftHandPinky[0].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]-40))
                    LeftHandPinky[0].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Pinky Prox" in row[0]:
                if LeftHandPinky[1] != 0:
                    LeftHandPinky[1].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandPinky[1].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandPinky[1].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Pinky Inter" in row[0]:
                if LeftHandPinky[2] != 0:
                    LeftHandPinky[2].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandPinky[2].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandPinky[2].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Left Pinky Dist" in row[0]:
                if LeftHandPinky[3] != 0:
                    LeftHandPinky[3].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    LeftHandPinky[3].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    LeftHandPinky[3].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif 'rightWrist' in row[0]:
                if rightHand != 0:
                    #print rightHand.Translation.GetAnimationNode().Nodes[0].FCurve.Evaluate(FBTime(0,0,0,frameCount))
                    #Add keys to wrist location and rotation, divide by 1000 for millimeters
                    rightHand.Translation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount), ((row[2]/1000)+xRHOffset))
                    rightHand.Translation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount), ((row[3]/1000)+yRHffset))
                    rightHand.Translation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount), ((row[4]/1000)+zRHffset))
                    rightHand.Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount), (row[5]))
                    rightHand.Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount), (row[6]))
                    rightHand.Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount), (row[7])) 
            elif "Right Thumb Prox" in row[0]:
                if RightHandThumb[0] != 0:
                    RightHandThumb[0].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),((row[2])-180))
                    RightHandThumb[0].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]+45))
                    RightHandThumb[0].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4])+90)
            elif "Right Thumb Inter" in row[0]:
                if RightHandThumb[1] != 0:
                    RightHandThumb[1].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandThumb[1].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandThumb[1].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Index Met" in row[0]:
                if RightHandIndex[0] != 0:
                    RightHandIndex[0].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]+180))
                    RightHandIndex[0].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]+40))
                    RightHandIndex[0].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]+45))
            elif "Right Index Prox" in row[0]:
                if RightHandIndex[1] != 0:
                    RightHandIndex[1].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandIndex[1].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandIndex[1].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Index Inter" in row[0]:
                if RightHandIndex[2] != 0:
                    RightHandIndex[2].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandIndex[2].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandIndex[2].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Index Dist" in row[0]:
                if RightHandIndex[3] != 0:
                    RightHandIndex[3].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandIndex[3].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandIndex[3].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Middle Met" in row[0]:
                if RightHandMiddle[0] != 0:
                    RightHandMiddle[0].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]+180))
                    RightHandMiddle[0].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]+30))
                    RightHandMiddle[0].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]+45))
            elif "Right Middle Prox" in row[0]:
                if RightHandMiddle[1] != 0:
                    RightHandMiddle[1].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandMiddle[1].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandMiddle[1].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Middle Inter" in row[0]:
                if RightHandMiddle[2] != 0:
                    RightHandMiddle[2].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandMiddle[2].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandMiddle[2].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Middle Dist" in row[0]:
                if RightHandMiddle[3] != 0:
                    RightHandMiddle[3].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandMiddle[3].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandMiddle[3].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Ring Met" in row[0]:
                if RightHandRing[0] != 0:
                    RightHandRing[0].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]+180))
                    RightHandRing[0].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]+20))
                    RightHandRing[0].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]+45))
            elif "Right Ring Prox" in row[0]:
                if RightHandRing[1] != 0:
                    RightHandRing[1].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandRing[1].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandRing[1].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Ring Inter" in row[0]:
                if RightHandRing[2] != 0:
                    RightHandRing[2].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandRing[2].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandRing[2].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Ring Dist" in row[0]:
                if RightHandRing[3] != 0:
                    RightHandRing[3].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandRing[3].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandRing[3].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Pinky Met" in row[0]:
                if RightHandPinky[0] != 0:
                    RightHandPinky[0].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]+180))
                    RightHandPinky[0].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]+10))
                    RightHandPinky[0].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]+45))
            elif "Right Pinky Prox" in row[0]:
                if RightHandPinky[1] != 0:
                    RightHandPinky[1].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandPinky[1].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandPinky[1].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Pinky Inter" in row[0]:
                if RightHandPinky[2] != 0:
                    RightHandPinky[2].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandPinky[2].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandPinky[2].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))
            elif "Right Pinky Dist" in row[0]:
                if RightHandPinky[3] != 0:
                    RightHandPinky[3].Rotation.GetAnimationNode().Nodes[0].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[2]))
                    RightHandPinky[3].Rotation.GetAnimationNode().Nodes[1].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[3]))
                    RightHandPinky[3].Rotation.GetAnimationNode().Nodes[2].FCurve.KeyAdd(FBTime(0,0,0,frameCount),(row[4]))   
        
        prevFrame = int(row[1])
