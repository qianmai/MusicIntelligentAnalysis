from scipy.io import wavfile
import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt

def Transform(s, N):
    
    signal = np.asarray(s)
    T = 1.0 / 1400.0
    L = 1.0/(2.0*T) * 10
    #x = np.linspace(0.0, N*T, N)
    
    y = np.fft.rfft(signal)
    l = len(y)
    #r = L / l
    
    #yf = []
    #for i in range(int(L)):
    #    yf.append(y[int(i / r)])
    
    xf = np.linspace(0.0, L, L)
    
    return xf, np.abs(y[0:L])
