import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
import numpy as np
import wave
import sys

def Plot_Output(timeDomain, xf, frequencyDomain):
    
    plt.figure(figsize = (8, 4))
    
    #Signal
    plt.title('Music Analysis', fontsize=40)
    plt.subplot(2, 1, 1)
    plt.ylabel('Time Domain')
    plt.grid(True)
    plt.plot(timeDomain)

    #Channel 1
    plt.subplot(2, 1, 2)
    plt.ylabel('Frequency Domain')
    plt.grid(True)
    plt.plot(xf, frequencyDomain, 'r-')
    
    plt.show()