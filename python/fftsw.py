# FFTSW fastest fourier transform of the south west
import numpy as np


def fftsw(x:np.array):
    
    n = len(x)
    if n == 1:
        return x
    else:
        # calcualte fft
        xk_e = fftsw(x[::2]) # even 
        xk_o = fftsw(x[1::2]) # odd
        for K in range((n//2) - 1):
            w = np.exp(-2j*np.pi*K/n)
            return np.concatenate([xk_e + (w*xk_o), xk_e - (w*xk_o)])
    

