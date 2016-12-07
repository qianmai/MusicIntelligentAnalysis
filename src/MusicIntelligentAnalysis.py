import wave
import numpy as np
import Output
import FourierTransform as ft

fileName1 = 'music/scout_1000.wav'
fileName2 = 'music/music_test.wav'
fileName3 = 'music/happy_piano.wav'

def main():
    #Time Domain
    wavFile = wave.open(fileName3, 'r')
    signal = wavFile.readframes(-1)
    timeDomain = np.fromstring(signal, 'Int16')
    
    #Frequency Domain
    #frequencyDomain = ft.Transform(timeDomain)
    frequencyDomain = timeDomain

    #Output
    Output.Plot_Output(timeDomain, frequencyDomain)

main()

##Fourier
#fs, data = wavfile.read(fileName1) # load the data

#channel_1 = data.T[0] # this is a two channel soundtrack

#b=[]
#for ele in range(channel_1):
#    b.append((ele/2**8.)*2-1) # this is 8-bit track, b is now normalized on [-1,1)
#c = fft(b) # calculate fourier transform (complex numbers list)
#d = len(c)/2  # you only need half of the fft list (real signal symmetry)
