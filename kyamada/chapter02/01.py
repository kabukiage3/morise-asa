import numpy as np
import matplotlib.pyplot as plt

fs = 44100
t = np.arange(fs/2)/fs
x = np.sin(2*np.pi*t)

S = np.sum(x)/fs
print(S)

plt.plot(t,x)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()