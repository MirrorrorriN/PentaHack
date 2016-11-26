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
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
        print "Initialized"
        global data
        data = []

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        controller.config.set("Gesture.Swipe.MinLength", 100);  
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
            handEach["palm_position"] = str(hand.palm_position)
            handEach["palm_normal"] = str(hand.palm_normal)
            handEach["direction"] = str(hand.direction)

            arm = hand.arm
            armData = {}
            armData["direction"] = str(arm.direction)
            armData["wrist_position"] = str(arm.wrist_position)
            armData["elbow_position"] = str(arm.elbow_position)
            handEach['arm'] = armData

            fingerData = []
            for finger in hand.fingers:
                fingerEach = {}
                fingerEach['finger_names'] = self.finger_names[finger.type]
                fingerEach['finger_length'] = finger.length
                fingerEach['finger_width'] = finger.width
                fingerData.append(fingerEach)
            handEach['finger'] = fingerData

            handData.append(handEach)
        frameEach["hand"] = handData


        gestureData = []
        for gesture in frame.gestures():
            gestureEach = {}
            gestureEach["type"] = gesture.type
            #Gesture 1
            if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                circle = CircleGesture(gesture)

                # Determine clock direction using the angle between the pointable and the circle normal
                if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
                    gestureEach["clockwiseness"] = "clockwise"
                else:
                    gestureEach["clockwiseness"] = "counterclockwise"

                swept_angle = 0
                if circle.state != Leap.Gesture.STATE_START && pre != No:
                    previous_update = CircleGesture(pre.gesture(circle.id))
                    swept_angle =  (circle.progress - previous_update.progress) * 2 * Leap.PI
                gestureEach["progress"], gestureEach["radius"], gestureEach["angle"], gestureEach["degrees"] = circle.progress, circle.radius, swept_angle * Leap.RAD_TO_DEG, clockwiseness


            #Gesture 2
            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                swipe = SwipeGesture(gesture)
                gestureEach["state"], gestureEach["position"], gestureEach["direction"], gestureEach["speed"] = self.state_names[gesture.state], swipe.position, swipe.direction, swipe.speed


            #Gesture 3
            if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                keytap = KeyTapGesture(gesture)
                gestureEach["state"], gestureEach["position"], gestureEach["direction"] = self.state_names[gesture.state], keytap.position, keytap.direction 


            #Gesture 4
            if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
                screentap = ScreenTapGesture(gesture)
                gestureEach["state"], gestureEach["position"], gestureEach["direction"] = self.state_names[gesture.state], screentap.position, screentap.direction 

            gestureData.append(gestureEach)
        frameEach["gesture"] = gestureData
        return frameEach


    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        global data
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
            if len(data) >= 30: 
                break
    except KeyboardInterrupt:
        pass
    finally:
       # Remove the sample listener when done
        controller.remove_listener(listener)
        return data
