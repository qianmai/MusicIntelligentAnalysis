from scipy.io import wavfile
import wave
import numpy as np
import Output
import Segmentation
import FourierTransform as ft

fileName1 = '../music/scout_1000.wav'
fileName2 = '../music/music_test.wav'
fileName3 = '../music/happy_piano.wav'
guitar = '../dataset/guitar/6.wav'
piano ='../dataset/piano/c3.wav'

def main():
    #Signal
    wavFile = wave.open(piano, 'r')
    signal = wavFile.readframes(-1)
    timeDomain = np.fromstring(signal, 'Int16')
    
    #Get Key Time List
    timePointList = Segmentation.get_segment_pairs(timeDomain, 1500, 800)
    head, tail = Segmentation.split_pair_from_list_by_index(timePointList, 0)

    # Added by Kun Li.
    segmentTimeDomain = Segmentation.make_segment(timeDomain, head, tail)
    
    #Frequency Domain
    xf, segmentFrequencyDomain = ft.Transform(segmentTimeDomain, 600)

    #Output
    Output.Plot_Output(segmentTimeDomain, xf, segmentFrequencyDomain)
    #Output.Plot_Output(timeDomain, segmentTimeDomain, frequencyDomain, None, None)
    

main()
