from scipy.io import wavfile
import numpy as np
from scipy.fftpack import fft

def Transform(signal, N):
    T = 1.0 / 800.0
    x = np.linspace(0.0, N*T, N)
    yf = fft(signal)
    xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
    return np.abs(yf[0:N/2])