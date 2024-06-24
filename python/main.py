
# Create time sereis sin wave
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import fftsw
N = 2**10 # Points
t = np.linspace(0,10,N)
T = t[1]-t[0]
x_n = np.sin(4*t*np.pi)
fft = fftsw.fftsw(x_n)
freq_scale = np.linspace(0,1/T, N)
# Plot the results
f, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(t, x_n)
ax1.set_title('Signal')
ax2.plot(freq_scale, np.absolute(fft))
ax2.set_title('DFT')
plt.plot