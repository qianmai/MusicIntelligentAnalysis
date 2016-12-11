from scipy.io import wavfile
import wave
import numpy as np
import Output
import Segmentation
import FourierTransform as ft
import heapq

#fileName1 = '../music/scout_1000.wav'
fileName1 = 'music/scout_1000.wav'
fileName2 = 'music/music_test.wav'
fileName3 = 'music/happy_piano.wav'
fileName4 = 'music/guitar.wav'

def main():
    #Signal
    wavFile = wave.open(fileName4, 'r')
    signal = wavFile.readframes(-1)
    timeDomain = np.fromstring(signal, 'Int16')
    
    #Get Key Time List
    timePointList = Segmentation.get_segment_pairs(timeDomain, 1000, 800)
    test = len(timePointList)
    Output.multi_Output(timeDomain, timePointList, [0, 1, 2, 3])

    # Added by Kun Li.
    #segmentTimeDomain = Segmentation.make_segment(timeDomain, head, tail)
    
    #Frequency Domain
    #frequencyDomain = ft.Transform(segmentTimeDomain, 2000)

    #Output
    #Output.Plot_Output(timeDomain, segmentTimeDomain, frequencyDomain, None, None)
    
    

main()
