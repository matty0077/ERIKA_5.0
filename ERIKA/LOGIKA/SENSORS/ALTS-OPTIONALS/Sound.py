#!/usr/bin/env python
#SOUND SENSOR-POTENTIALLY MEASURE USEFUL/HARMFUL ACCOUSTIC VIBRATIONS FOR AGRICULTURE
import time
import grovepi

# Connect the Grove Sound Sensor to analog port A0
# SIG,NC,VCC,GND
sound_sensor = 2
grovepi.pinMode(sound_sensor,"INPUT")

def ACCOUSTICS():
    try:
        # Read the sound level(0-1023) NO direct decibal measurement yet
        sensor_value = grovepi.analogRead(sound_sensor)

        # If loud, illuminate LED, otherwise dim
        '''if sensor_value > threshold_value:
            grovepi.digitalWrite(led,1)
        else:
            grovepi.digitalWrite(led,0)'''

        print("sensor_value = %d" %sensor_value)
        time.sleep(.5)

    except IOError:
        print ("Error")

#while True:
    #ACCOUSTICS()
