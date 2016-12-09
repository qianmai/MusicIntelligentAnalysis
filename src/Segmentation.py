# Created by Kun Li.
# 12/2016

def make_segment(rawdata, fr, to):
    segment = []
    i = 0
    for data in rawdata:
        if i >= fr and i <= to:
            segment.append(data)
        i += 1
        
    return segment