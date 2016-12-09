import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
import numpy as np
import wave
import sys

def Plot_Output(timeDomain, segmentTimeDomain, frequencyDomain, backup_1, backup_2):
    #Entire Music
    plt.subplot(5, 1, 1)
    plt.title('Music Analysis', fontsize=40)
    plt.plot(timeDomain)

    #Signal
    plt.subplot(5, 1, 2)
    plt.plot(segmentTimeDomain)

    #Channel 1
    plt.subplot(5, 1, 3)
    plt.plot(frequencyDomain)

    #specgram
    plt.subplot(5, 1, 4)
    if(backup_1 is None):
        plt.plot()
    else:
        plt.plot(backup_1)

    #Pxx, freqs, bins, im = plt.specgram(
    #    timeDomain, 
    #    NFFT=timeDomain, 
    #    Fs=timeDomain, 
    #    noverlap=900,
    #    cmap=plt.cm.gist_heat
    #)

    #Backup
    plt.subplot(5, 1, 5)
    if(backup_2 is None):
        plt.plot()
    else:
        plt.plot(backup_2)
    
    ##Text
    #plt.text(2, 4,"A test string", fontsize=50)

    plt.show()