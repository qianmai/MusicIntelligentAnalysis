import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
import numpy as np
import wave
import sys
import Segmentation
import FourierTransform as ft

def multi_Output(timeDomain, timePointList, indexList):
    td = []
    fd = []
    i = 0
    for index in indexList:
        #Head and Tail
        head, tail = Segmentation.split_pair_from_list_by_index(timePointList, indexList[i])
        #Segment Time Domain
        segmentTimeDomain = Segmentation.make_segment(timeDomain, head, tail)
        td.append(segmentTimeDomain)
        #Frequency Domain
        frequencyDomain = ft.Transform(segmentTimeDomain, 2000)
        fd.append(frequencyDomain)
        
        i += 1

    #output
    #Plot_Output(timeDomain, td[0], td[1], td[2], td[3])
    Plot_Output(timeDomain, fd[0], fd[1], fd[2], fd[3])

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