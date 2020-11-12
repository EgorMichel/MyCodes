from MikhelPlakhotniuk2 import *

repetitionNumber = int(input("Enter repetition number: "))

try:
    for i in range(repetitionNumber):
        for j in range(255):
            lightNumber(j) 
        for j in range(255):
            lightNumber(255 - j) 
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()