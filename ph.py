#!/usr/bin/env python
#
# GrovePi Example for using the Grove PH Sensor (http://www.seeedstudio.com/wiki/Grove_-_PH_Sensor)
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Just used the grove analog sensor lib and used the calculations from ther audrino example.
#
import time
import grovepi

# Connect the Grove PH Sensor to analog port A2
# SIG,NC,VCC,GND
sensor = 2

grovepi.pinMode(sensor,"INPUT")
time.sleep(1)

# Reference voltage of ADC is 5v
adc_ref = 5

while True:
    try:
        # Read sensor value
        sensor_value = grovepi.analogRead(sensor)

        # Calculate PH
        ph = -19.18518519 * (float)(sensor_value) * adc_ref / 1024 + 41.02740741

        print("sensor_value =", sensor_value, " ph =", ph)

    except IOError:
        print ("Error")
