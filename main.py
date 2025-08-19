import cv2
import time
import controller as cnt
from cvzone.HandTrackingModule import HandDetector
import winsound
import pyttsx3
import pygame
import voice as voi
import requests
import speech_recognition as sr

#/////////////////////////////////////////////////////////////////
engine = pyttsx3.init()

engine.setProperty('rate', 100)  
engine.setProperty('volume', 1)

#/////////////////////////////////////////////////////////////////
frequency = 1100 
duration = 200

#/////////////////////////////////////////////////////////////////
detector = HandDetector(detectionCon=0.1, maxHands=2)

video = cv2.VideoCapture(0)

switch = "OFF"

#/////////////////////////////////////////////////////////////////
from music_test_01 import MusicPlayer, execute_command  
from music_library import music_files  

# Create an instance of MusicPlayer
player = MusicPlayer(music_files)


#/////////////////////////////////////////////////////////////////
# List of appliances with their statuses
appliances = [
    {"name": "Light", "status": "OFF", "power":1},
    {"name": "Fan", "status": "OFF", "power":0},
    {"name": "AC", "status": "OFF", "power":21},
    {"name": "TV", "status": "OFF", "power":1},
    {"name": "Geyser", "status": "OFF", "power":1},
    {"name": "Speaker", "status": "OFF", "power":1}
]

#/////////////////////////////////////////////////////////////////
def change_status(appliance_name, new_status):
    for appliance in appliances:
        if appliance['name'] == appliance_name:
            appliance['status'] = new_status
            break  

def is_on(appliance_name):
    for appliance in appliances:
        if appliance['name'] == appliance_name:
            return appliance['status'] == 'ON'  
    return False
    
#///////////////////////////////////////////////////////////////


while True:
    powerDown = 50
    
    while True:
        cnt.led(appliances)
        cnt.switch(False)
        
        ret, frame = video.read()
        frame = cv2.flip(frame, 1)  # Flip the frame horizontally
        hands, img = detector.findHands(frame)  # Detect hands
        
        if len(hands) == 2:
            # Assign the left and right hands based on handType
            if hands[0]['type'] == 'Left':
                leftHand = hands[0]
                rightHand = hands[1]
            else:
                leftHand = hands[1]
                rightHand = hands[0]

            # Swap left and right labels for display purposes after flip
            displayLeftHand = rightHand
            displayRightHand = leftHand

            fingerUpLeft = detector.fingersUp(displayLeftHand)
            fingerUpRight = detector.fingersUp(displayRightHand)

            if fingerUpLeft == [0, 0, 0, 0, 1] and fingerUpRight == [0, 0, 0, 0, 1]:
                switch = "ON"
                #engine.say("ON")
                #engine.runAndWait()
                print("Power ON")
                cnt.switch(True)
                break
        
        cv2.imshow("frame", frame)
        k = cv2.waitKey(1)
        if k == ord("k"):
            break
        
    count = 0
    prev_fingerUpLeft = [0,0,0,0,0]
    prev_fingerUpRight = [0,0,0,0,0]

    while switch == "ON":
        cnt.led(appliances)
        
        ret, frame = video.read()
        frame = cv2.flip(frame, 1)  # Flip the frame horizontally
        hands, img = detector.findHands(frame)
        
        if len(hands) == 2:
            powerDown = 50
            
            # Assign the left and right hands based on handType
            if hands[0]['type'] == 'Left':
                leftHand = hands[0]
                rightHand = hands[1]
            else:
                leftHand = hands[1]
                rightHand = hands[0]

            # Swap left and right labels for display purposes after flip
            displayLeftHand = rightHand
            displayRightHand = leftHand
            
            fingerUpLeft = detector.fingersUp(displayLeftHand)
            fingerUpRight = detector.fingersUp(displayRightHand)
            print(f"{fingerUpLeft}, {fingerUpRight}")
            
            if(prev_fingerUpLeft == fingerUpLeft and prev_fingerUpRight == fingerUpRight):
                count += 1
            else:
                count = 0
                prev_fingerUpLeft = fingerUpLeft
                prev_fingerUpRight = fingerUpRight
               
               
                   
            if(count >= 5):

                #//   ON   //#
                if not is_on('Light') and fingerUpLeft == [0, 0, 0, 0, 0] and fingerUpRight == [1, 0, 0, 0, 0]:
                    change_status('Light', 'ON')
                elif not is_on('Fan') and fingerUpLeft == [0, 0, 0, 0, 0] and fingerUpRight == [0, 1, 0, 0, 0]:
                    change_status('Fan', 'ON')
                elif not is_on('AC') and fingerUpLeft == [0, 0, 0, 0, 0] and fingerUpRight == [1, 1, 1, 0, 0]:
                    change_status('AC', 'ON')
                elif not is_on('TV') and fingerUpLeft == [0, 0, 0, 0, 0] and fingerUpRight == [0, 0, 0, 1, 1]:
                    change_status('TV', 'ON')
                elif not is_on('Geyser') and fingerUpLeft == [0, 0, 0, 0, 0] and fingerUpRight == [0, 0, 0, 0, 1]:
                    change_status('Geyser', 'ON')
                    
                #//   OFF   //#
                if is_on('Light') and fingerUpLeft == [1, 0, 0, 0, 0] and fingerUpRight == [0, 0, 0, 0, 0]:
                    change_status('Light', 'OFF')
                elif is_on('Fan') and fingerUpLeft == [0, 1, 0, 0, 0] and fingerUpRight == [0, 0, 0, 0, 0]:
                    change_status('Fan', 'OFF')
                elif is_on('AC') and fingerUpLeft == [1, 1, 1, 0, 0] and fingerUpRight == [0, 0, 0, 0, 0]:
                    change_status('AC', 'OFF')
                elif is_on('TV') and fingerUpLeft == [0, 0, 0, 1, 1] and fingerUpRight == [0, 0, 0, 0, 0]:
                    change_status('TV', 'OFF')
                elif is_on('Geyser') and fingerUpLeft == [0, 0, 0, 0, 1] and fingerUpRight == [0, 0, 0, 0, 0]:
                    change_status('Geyser', 'OFF')
                    
                #// POWER CHANGE //#
                if is_on('AC') and fingerUpLeft == [1, 0, 0, 0, 0] and fingerUpRight == [1, 1, 1, 0, 0]:
                    for appliance in appliances:
                        if appliance['name'] == 'AC':
                            if(appliance['power'] < 30):
                                appliance['power'] = appliance['power'] + 1
                                winsound.Beep(frequency, duration)
                                time.sleep(0.5)
                            elif(appliance['power'] == 30):
                                engine.say("Max Power")
                                engine.runAndWait()
                elif is_on('AC') and fingerUpLeft == [0, 1, 0, 0, 0] and fingerUpRight == [1, 1, 1, 0, 0]:
                    for appliance in appliances:
                        if appliance['name'] == 'AC':
                            if(appliance['power'] > 16):
                                appliance['power'] = appliance['power'] - 1
                                winsound.Beep(frequency, duration)
                                time.sleep(0.5)
                            elif(appliance['power'] == 16):
                                engine.say("Min Power")
                                engine.runAndWait()
                elif is_on('Fan') and fingerUpLeft == [1, 0, 0, 0, 0] and fingerUpRight == [0, 1, 0, 0, 0]:
                    for appliance in appliances:
                        if appliance['name'] == 'Fan':
                            if(appliance['power'] < 5):
                                appliance['power'] = appliance['power'] + 1
                                winsound.Beep(frequency, duration)
                                time.sleep(0.5)
                            elif(appliance['power'] == 5):
                                engine.say("Max Power")
                                engine.runAndWait()
                elif is_on('Fan') and fingerUpLeft == [0, 1, 0, 0, 0] and fingerUpRight == [0, 1, 0, 0, 0]:
                    for appliance in appliances:
                        if appliance['name'] == 'Fan':
                            if(appliance['power'] > 0):
                                appliance['power'] = appliance['power'] - 1
                                winsound.Beep(frequency, duration)
                                time.sleep(0.5)
                            elif(appliance['power'] == 0):
                                engine.say("Min Power")
                                engine.runAndWait()
                elif is_on('TV') and fingerUpLeft == [0, 1, 0, 0, 0] and fingerUpRight == [0, 0, 0, 1, 1]:
                        for appliance in appliances:
                            if appliance['name'] == 'TV':
                                appliance['power']=voi.listen(appliance['power'])
                                
                #Sound Control
                if not is_on('Speaker') and fingerUpLeft == [0, 0, 0, 0, 0] and fingerUpRight == [0, 1, 1, 0, 0]:
                    execute_command(player, "play")
                    change_status('Speaker', 'ON')
                elif fingerUpLeft == [1, 1, 1, 1, 1] and fingerUpRight == [0, 1, 1, 0, 0]:
                    execute_command(player, "pause")
                    time.sleep(1)
                elif fingerUpLeft == [0, 1, 1, 1, 1] and fingerUpRight == [0, 1, 1, 0, 0]:
                    execute_command(player, "resume")
                    time.sleep(1)
                elif fingerUpLeft == [0, 1, 1, 0, 0] and fingerUpRight == [0, 1, 1, 0, 0]:
                    execute_command(player, "next")
                    time.sleep(2)
                elif fingerUpLeft == [0, 0, 1, 1, 0] and fingerUpRight == [0, 1, 1, 0, 0]:
                    execute_command(player, "previous")
                    time.sleep(2)
                elif fingerUpLeft == [1, 0, 0, 0, 0] and fingerUpRight == [0, 1, 1, 0, 0]:
                    execute_command(player, "volume_up")
                    time.sleep(2)
                elif fingerUpLeft == [0, 1, 0, 0, 0] and fingerUpRight == [0, 1, 1, 0, 0]:
                    execute_command(player, "volume_down")
                    time.sleep(2)
                elif is_on('Speaker') and fingerUpLeft == [0, 1, 1, 0, 0] and fingerUpRight == [0, 0, 0, 0, 0]:
                    change_status('Speaker', 'OFF')
                    execute_command(player, "stop")
            
            #SwitchOFF
            if fingerUpLeft == [1, 1, 1, 1, 1] and fingerUpRight == [1, 1, 1, 1, 1]:
                switch = "OFF"
                #engine.say("OFF")
                #engine.runAndWait()
                print("\nSwitch OFF")
                cnt.switch(False)
                break
            
            # Display the status of each appliance
            for i, appliance in enumerate(appliances):
                text = f"{appliance['name']}"
                cv2.putText(frame, text, (20, 400 + i * 15), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                color = (0, 255, 0) if appliance['status'] == 'ON' else (0, 0, 255)
                cv2.circle(frame, (150, 400 + i * 15 - 10), 7, color, -1) 
                Power = f"{appliance['power']}"
                cv2.putText(frame, Power, (200, 400 + i * 15), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                
                
            cnt.led(appliances)

        else:
            powerDown -= 1
            print(f'\rPowering Off: {powerDown}', end='')
            if powerDown == 0:
                switch = "OFF"
                #engine.say("OFF")
                #engine.runAndWait()
                print("\nSwitch OFF")
                cnt.switch(False)
                break
            cv2.waitKey(2)
            
        cv2.imshow("frame", frame)
        k = cv2.waitKey(5)
        if k == ord("k"):
            break
        
    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord("k"):
        break

video.release()
cv2.destroyAllWindows()
