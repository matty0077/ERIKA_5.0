#!/usr/bin/env python

'''ERIKA SYSTEM- Manages Environmental Data for the purpose of
planting and/or locating ideal environments in which life can thrive optimally.'''

#SUN SENSOR-measures visible, ultraviolet and infrared light,skin cancer warnings.
#SOIL MOISTURE SENSOR-Seed Suitability and Hydration Locator.
#BME280 BAROMETER/TEMPERATURE/HUMIDITY-Calculate temp/humid, Fire danger, dew point, fog and frost,rain-storms.
#RGBLCD BACKLIGHT- Color Coated Display
#TOUCH SENSOR- for switching modes
##########################IMPROVEMENTS
#ALTITUDE CALCULATIONS==PREDICT PLANT SIZES?

import sys, time
sys.path.append("/home/pi/Desktop/ERIKA_5.0/ERIKA/LOGIKA/")
sys.path.append('/home/pi/Desktop/ERIKA_5.0/ERIKA/LOGIKA/SENSORS/')

import threading
import subprocess
import math
import logging
from datetime import datetime

from META import *
from rgb_lcd import *
from Light import *
from Sun import *
from Soil import *
from Baro import *

# Connect the Grove Touch Sensor to digital port D8
touch_sensor = 8
grovepi.pinMode(touch_sensor,"INPUT")

######ERIKA CLASS
class ERIKA:
        MODE=0
        TIME= "%a %-d %b %-I:%M"
########################DATE TIME
        def Date_Time(self):
                msg = "%s" % (datetime.now().strftime(self.TIME))
                setText(msg)
                Set_Yellow()
                time.sleep(1)
                Set_Clear()

################################button. cycles through programs
        def Button(self):
                press=grovepi.digitalRead(touch_sensor)
                #print(press)
                if press==1:
                        self.MODE+=1
                        if self.MODE>14:
                                self.MODE=0

#############abbreviate class                
E=ERIKA()

###########MAIN PROGRAM(FOR SWITCHING MODES)
while True:
    try:
        if  E.MODE==0:#date/time
                E.Date_Time()
        elif  E.MODE==1:#temperature
                Temperature()
        elif  E.MODE==2:#humidity
                Humidity()
        elif  E.MODE==3:#air pressure
                Pressure()
        elif  E.MODE==4:#Altitude
                computeHeight()
        elif  E.MODE==5:#Flammability
                CBI()
        elif  E.MODE==6:#dew point
                Dew_Point()
        elif  E.MODE==7:#pesticide effectiveness
                PESTICIDE()
        elif  E.MODE==8:#water vapor for fog n frost
                VAPOR()
        elif  E.MODE==9:#vapor pressure
                Evap_Rate()
        elif  E.MODE==10:#visible light
                LVIS()
        elif  E.MODE==11:#UV light for people
                UV_PPL()
        elif  E.MODE==12:#UV light for plants
                UV_AGRI()
        elif  E.MODE==13:#IR light for plants
                IR()
        elif  E.MODE==14:#soil  moisture
                Soil()
                
        Threader(E.Button)

    except KeyboardInterrupt:
        Set_Clear()
        break
        sys.exit()
    except TypeError:
        setText("ERIKA TYPE Error")
        Set_Red()
        time.sleep(1)
        Set_Clear()
    except IOError:
        setText("ERIKA IO Error")
        Set_Red()
        time.sleep(1)
        Set_Clear()
        
