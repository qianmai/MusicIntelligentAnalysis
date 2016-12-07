from scipy.io import wavfile
import wave
import numpy as np
import Output
import Segmentation
import FourierTransform as ft

fileName1 = '../music/scout_1000.wav'
fileName2 = '../music/music_test.wav'
fileName3 = '../music/happy_piano.wav'
fileName4 = '../music/guitar.wav'

def main():
    #Signal
    wavFile = wave.open(fileName4, 'r')
    signal = wavFile.readframes(-1)
    timeDomain = np.fromstring(signal, 'Int16')
    
    # Added by Kun Li.
    timeDomain = Segmentation.make_segment(timeDomain, 57000, 63000)
    
    #Frequency Domain
    frequencyDomain = ft.Transform(timeDomain, 600)

    #Output
    Output.Plot_Output(timeDomain, frequencyDomain)
    
    

main()
