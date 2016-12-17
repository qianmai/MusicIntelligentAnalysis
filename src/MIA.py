from scipy.io import wavfile
import wave
import numpy as np
import Output
import Segmentation
import FourierTransform as ft
import heapq
import ImageProcess as ip

fileName1 = '../music/scout_1000.wav'
fileName2 = '../music/music_test.wav'
fileName3 = '../music/happy_piano.wav'
music = '../music/guitar.wav'
guitar = '../music/elements/guitar/5.wav'
piano ='../music/elements/piano/c1m.wav'

def main():
    #Signal
    wavFile = wave.open(music, 'r')
    signal = wavFile.readframes(-1)
    timeDomain = np.fromstring(signal, 'Int16')
    
    #Get Key Time List
    timePointList = Segmentation.get_segment_pairs(timeDomain, 1000, 800)
    #test = len(timePointList)
    #Output.multi_Output(timeDomain, timePointList, [0, 1, 2, 3])

    # Added by Kun Li.
    head, tail = Segmentation.split_pair_from_list_by_index(timePointList, 0)
    segmentTimeDomain = Segmentation.make_segment(timeDomain, head, tail)
    xf, segmentFrequencyDomain = ft.Transform(segmentTimeDomain, 600)
    #Output.DrawGraphs(timeDomain, xf, segmentFrequencyDomain)

    dataSource, xmin, xmax = Segmentation.get_peak_pattern(segmentFrequencyDomain, 0.1)
    Output.single_Output(dataSource, xmin, xmax)

    #ip.writeDataToImage(dataSource)
    
main()
