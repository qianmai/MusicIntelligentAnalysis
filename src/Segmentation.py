import numpy as np

#Find all segment key time from a music
def get_segment_pairs(rawdata, downLimit, continueLength):
    head = tail = 0
    highNumberCount = 0
    lowNummberCount = 0
    previousTail = 0
    isBegin = False
    list = []

    i = 0
    for element in rawdata:
        
        if(isBegin == False):
            if(element > downLimit):
                highNumberCount += 1
                #Start Recording
                if(highNumberCount > 40):
                    head = max(i-continueLength, previousTail)
                    isBegin = True
                    lowNummberCount = 0
            else:
                highNumberCount = 0


        if(isBegin):
            if(element < downLimit):
                lowNummberCount += 1
                #Finish Recording
                if(lowNummberCount > continueLength):
                    tail = i
                    previousTail = tail
                    isBegin = False
                    pair = (head, tail)
                    list.append(pair)
            else:
                lowNummberCount = 0
        i += 1

    if(len(list) == 0):
        pair = (head, i - 1)
        list.append(pair)

    return list

#Get the head and tail of a segment
def split_pair_from_list_by_index(pairlist, index):
    pair = pairlist[index]
    return pair[0], pair[1]

#Get a segment of a music by start and end time
def make_segment(rawdata, fr, to):
    segment = []
    i = 0
    for data in rawdata:
        if i >= fr and i <= to:
            segment.append(data)
        i += 1
        
    return segment

#Get a segment of a frequency in frequency range
def make_frequency_segment(rawdata, fr, to):
    segment = []
    i = 0
    for data in rawdata:
        if i <= to:
            if i >= fr:
                segment.append(data)
            else:
                segment.append(0)
        i += 1
        
    return segment

#Get Peak Pattern
def get_peak_pattern(frequencyDomain, limitPercentage ):
    peakValue = max(frequencyDomain)
    limit = peakValue * limitPercentage
    lowNummberCount = 0
    peakIndex = np.argmax(frequencyDomain)
    head = 0
    tail = len(frequencyDomain) - 1
    lowNummberCount = 0
    foundHead = False
    foundTail = False

    #Get head by searching leftward
    i = peakIndex
    while((not foundHead) and (i > 0)):
        if(frequencyDomain[i] < limit):
            lowNummberCount += 1
            if(lowNummberCount > 10):
                head = i
                foundHead = True
                lowNummberCount = 0
        else:
            lowNummberCount = 0
        i -= 1
    
    #Get tail by searching rightward
    i = peakIndex
    lowNummberCount = 0
    while((not foundTail) and (i < len(frequencyDomain) - 1)):
        if(frequencyDomain[i] < limit):
            lowNummberCount += 1
            if(lowNummberCount > 10):
                tail = i
                foundTail = True
        else:
            lowNummberCount = 0
        i += 1
    
    return make_segment(frequencyDomain, head, tail), head, tail
    #return make_frequency_segment(frequencyDomain, head, tail), head, tail
    
