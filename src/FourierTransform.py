from scipy.io import wavfile
import numpy
from socket import socket

fileName3 = 'music/happy_piano.wav'

def Transform(signal):
    fs, data = wavfile.read(fileName3) # load the data

    channel_1 = data.T[0] # this is a two channel soundtrack

    b=[]
    for ele in range(channel_1):
        b.append((ele/2**8.)*2-1) # this is 8-bit track, b is now normalized on [-1,1)
    c = numpy.fft(b) # calculate fourier transform (complex numbers list)
    d = len(c)/2  # you only need half of the fft list (real signal symmetry)
    return abs(c[:(d-1)])