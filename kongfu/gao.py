################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import Leap, sys, thread, time, copy
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
data, pre = [], None

class SampleListener(Leap.Listener):
    finger_names = ["Thumb", "Index", "Middle", "Ring", "Pinky"]
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ["STATE_INVALID", "STATE_START", "STATE_UPDATE", "STATE_END"]

    def on_init(self, controller):
        print "Initialized"
        global data, pre
        data, pre = [], None

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        controller.config.set("Gesture.Swipe.MinLength", 20);  
        controller.config.save();

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def deal(self, frame, pre):
        frameEach = {}

        handData = []
        for hand in frame.hands:
            handEach = {"handType": "Left hand" if hand.is_left else "Right hand"}
            position = str(hand.palm_position)[1:-1].split(',')
            pos = [float(p) for p in position]
            direction = str(hand.direction)[1:-1].split(',')
            dirs = [float(p) for p in direction]

            handEach["palmPosition"] = pos
           # handEach["palm_normal"] = str(hand.palm_normal)
            handEach["direction"] = dirs
            handEach["handerId"] = hand.id

            fingerData = []
            for finger in hand.pointables:
                fingerEach = {}
                fingerEach['fingerId'] = finger.id
                fingerEach['fingerName'] = self.finger_names[finger.id % 10]
                position = str(finger.direction)[1:-1].split(',')
                pos = [float(p) for p in position]
                direction = str(finger.tip_position)[1:-1].split(',')
                dirs = [float(p) for p in direction]

                fingerEach['direction'] = pos
                fingerEach['tipPostion'] = dirs
                fingerData.append(fingerEach)
            handEach['finger'] = fingerData

            for finger in hand.pointables:
                position = float(str(finger.direction)[1:-1].split(',')[1])
                if position < -0.5:
                    gestureData = {}
                    gestureData["type"] = 'keytap'
                    gestureData["pointableId"] = finger.id
                    handData.append(handEach)
                    frameEach["hand"] = handData        
                    frameEach['gesture'] = [gestureData]
                    return frameEach        


            handData.append(handEach)
        frameEach["hand"] = handData


        gestureData = []
        for gesture in frame.gestures():
            gestureEach = {} 
            #Gesture 1
            if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                gestureEach["type"] = 'circle'
                
                


            #Gesture 2
            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                gestureEach["type"] = "swipe"


            #Gesture 3
            if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                gestureEach["type"] = "keytap"
                gestureEach["pointableId"] = int(str(gesture.pointables[0]).split(":")[-1])

                keytap = KeyTapGesture(gesture)
                position = str(keytap.position)[1:-1].split(',')
                pos = [float(p) for p in position]
                direction = str(keytap.direction)[1:-1].split(',')
                dirs = [float(p) for p in direction]
                gestureEach["state"], gestureEach["position"], gestureEach["direction"] = self.state_names[gesture.state], pos, dirs
            
                if len(gestureData):
                    gestureData[0] = gestureEach
                else:
                    gestureData.append(gestureEach)
                break


            #Gesture 4
            if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
                gestureEach["type"] = "screentap"
                gestureEach["pointableId"] = str(gesture.pointables[0]).split(":")[-1]
               # print gestureEach['pointableId']
                screentap = ScreenTapGesture(gesture)
                position = str(screentap.position)[1:-1].split(',')
                pos = [float(p) for p in position]
                direction = str(screentap.direction)[1:-1].split(',')
                dirs = [float(p) for p in direction]
                gestureEach["state"], gestureEach["position"], gestureEach["direction"] = self.state_names[gesture.state], pos, dirs
                
                if len(gestureData):
                    gestureData[0] = gestureEach
                else:
                    gestureData.append(gestureEach)
                break
        
            gestureData.append(gestureEach)

        frameEach["gesture"] = gestureData
        return frameEach


    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        global data, pre
        frame = self.deal(controller.frame(), pre)
        pre = frame
        data.append(frame)
        

    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"


def getLeapData():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)
    try:
        global data
        while True:
            if len(data) >= 20: #Interval
                break
    except KeyboardInterrupt:
        pass
    finally:
       # Remove the sample listener when done
        controller.remove_listener(listener)
        return data
