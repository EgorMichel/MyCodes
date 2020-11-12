import math
import RPi.GPIO as GPIO
import time 
import sys
import numpy as np
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)
GPIO.setup (17, GPIO.OUT)
GPIO.setup (4, GPIO.IN)
leds = [26, 19, 13, 6, 5, 11, 9, 10]

for k in leds:
    GPIO.setup(k,GPIO.OUT)


def decToBinList (decNumber):
    return [int(i) for i in bin(decNumber)[2:].zfill(8)]


def lightNumber (decNumber):
    a = decToBinList(decNumber)
    for i in range(8):
        GPIO.output(leds[i], a[i])

def BinarySearch ():
    l = 0
    r = 255
    while r - l >= 2:
        m = (l + r)//2
        lightNumber(m)
        time.sleep(0.001)
        if GPIO.input(4):
            l = m
        else:
            r = m
    return m

try:
    T = int(input())
    Tstart = time.time()
    amplitude = [0]
    Time = [0]
    GPIO.output(17, 1)
    while time.time() < Tstart + T:
        f = BinarySearch()
        amplitude.append(f / 256 * 3.3)
        Time.append(time.time() - Tstart)
        print("Digital value: " + str(f) + ", Analog value: " + str(round((f / 256 * 3.3), 3)) + " V")
        for i in range(8):
            GPIO.output(leds[i], 0)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()
    plt.plot(Time, amplitude)
    plt.title("Plot of charging")
    plt.xlabel("Time, seconds")
    plt.ylabel("Voltage, V")
    np.savetxt("data1.txt", amplitude, fmt = "%1.3f", header = "Values of voltage: ")
    plt.savefig("Plot of charging")
    plt.show()