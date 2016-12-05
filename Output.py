import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
import numpy as np
import wave
import sys

def Plot_Output(timeDomain):
    #Signal
    plt.subplot(4, 1, 1)
    plt.title('Music Analysis', fontsize=40)
    plt.plot(timeDomain)

    #Channel 1
    plt.subplot(4, 1, 2)
    plt.plot()

    #Channel 2
    plt.subplot(4, 1, 3)
    plt.plot()

    #Fourier
    plt.subplot(4, 1, 4)
    plt.plot()

    plt.show()


#Change1 KunLi
