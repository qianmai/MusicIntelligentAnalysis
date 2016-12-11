# Created by Kun Li.
# 12/2016

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