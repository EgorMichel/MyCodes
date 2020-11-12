from MikhelPlakhotniuk2 import *
import numpy as np
import matplotlib.pyplot as plt
import time


# ndarray = [0]*256
T = float(input("Enter time: "))
F = float(input("Enter Frequency: "))


Time = np.arange(0, T, 0.01)
amplitude = ((np.sin(Time * 2 * 3.1415 * F) + 1) * 127.5) // 1
plt.plot(Time, amplitude)
plt.title("Sinys")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()
try:
    for i in amplitude:
        lightNumber(int(i))
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()