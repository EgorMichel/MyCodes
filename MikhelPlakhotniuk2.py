import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)
leds = [26, 19, 13, 6, 5, 11, 9, 10]

for m in leds:
    GPIO.setup(m,GPIO.OUT)


# "

def decToBinList (decNumber):
    return [int(i) for i in bin(decNumber)[2:].zfill(8)]


def lightNumber (decNumber):
    a = decToBinList(decNumber)
    for i in range(8):
        GPIO.output(leds[i], a[i])
    time.sleep(0)


# try:
#     while True:
#         value = int(input("Enter number: "))
#         lightNumber (value)
#         if value == -1 or value > 256:
#             break
# except KeyboardInterrupt:
#     GPIO.cleanup()
# finally:
#     GPIO.output(leds, 0)
#     GPIO.cleanup()
