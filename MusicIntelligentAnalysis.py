from scipy.io import wavfile
import wave
import numpy as np
import Output

fileName1 = 'music/scout_1000.wav'
fileName2 = 'music/music_test.wav'

def main():
    #Signal
    wavFile = wave.open(fileName2, 'r')
    signal = wavFile.readframes(-1)
    timeDomain = np.fromstring(signal, 'Int16')
    
    

    #Output
    Output.Plot_Output(timeDomain)

main()

##Fourier
#fs, data = wavfile.read(fileName1) # load the data

#channel_1 = data.T[0] # this is a two channel soundtrack

#b=[]
#for ele in range(channel_1):
#    b.append((ele/2**8.)*2-1) # this is 8-bit track, b is now normalized on [-1,1)
#c = fft(b) # calculate fourier transform (complex numbers list)
#d = len(c)/2  # you only need half of the fft list (real signal symmetry)

#another change
# whgahdgnafdkng

#haha