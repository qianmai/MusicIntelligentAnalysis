import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
import numpy as np
import wave
import sys

def Plot_Output(timeDomain, frequencyDomain):
    #Signal
    plt.subplot(4, 1, 1)
    plt.title('Music Analysis', fontsize=40)
    plt.plot(timeDomain)

    #Channel 1
    plt.subplot(4, 1, 2)
    plt.plot(frequencyDomain)

    #specgram
    plt.subplot(4, 1, 3)
    plt.plot()
    #Pxx, freqs, bins, im = plt.specgram(
    #    timeDomain, 
    #    NFFT=timeDomain, 
    #    Fs=timeDomain, 
    #    noverlap=900,
    #    cmap=plt.cm.gist_heat
    #)

    #Fourier
    plt.subplot(4, 1, 4)
    plt.plot()
    
    ##Text
    #plt.text(2, 4,"A test string", fontsize=50)

    plt.show()


#Change1 KunLi
