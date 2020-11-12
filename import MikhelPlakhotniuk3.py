import MikhelPlakhotniuk2
from MikhelPlakhotniuk2 import lightNumber as x

repetitionNumber = int(input("Enter repetition number: "))

try:
    for i in range(repetitionNumber):
        x(i)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()