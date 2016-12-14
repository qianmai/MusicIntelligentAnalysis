import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
import numpy as np
import wave
import sys
import Segmentation
import FourierTransform as ft

def single_Output(dataSource, xmin, xmax):
    plt.figure(2)
    plt.plot(dataSource)
    axes = plt.gca()
    #axes.set_xlim([xmin,xmax])
    axes.set_xlim([0,xmax - xmin])
    axes.set_axis_off()
    SaveImage(plt)
    plt.show()
    
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
        frequencyDomain = ft.Transform(segmentTimeDomain, 1000)
        fd.append(frequencyDomain)
        
        i += 1

    #output
    #Plot_Output(timeDomain, td[0], td[1], td[2], td[3])
    #Plot_Output(timeDomain, fd[0], fd[1], fd[2], fd[3])

    dataSource, xmin, xmax = Segmentation.get_peak_pattern(fd[1], 0.1)
    #single_Output(dataSource, xmin, xmax)
    single_Output(fd[1], xmin, xmax)
    Plot_Output(timeDomain, fd[0], fd[1], fd[2], fd[3])

def Plot_Output(timeDomain, segmentTimeDomain, frequencyDomain, backup_1, backup_2):
    plt.figure(1)
    #Entire Music
    plt.subplot(5, 1, 1)
    plt.title('Music Analysis', fontsize=40)
    plt.subplot(2, 1, 1)
    plt.ylabel('Time Domain')
    plt.grid(True)
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

    #Backup
    plt.subplot(5, 1, 5)
    if(backup_2 is None):
        plt.plot()
    else:
        plt.plot(backup_2)

    plt.show()

def DrawGraphs(timeDomain, xf, frequencyDomain):
    
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
    
    #plt.show()

def SaveImage(plot):
    fig = plot.gcf()
    fig.savefig('waveform.png', dpi = 100)
