import cv2
import numpy as np
from matplotlib import pyplot as plt
 
#img = cv2.imread('test.png', 0)
#plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()

#img = np.zeros([512,512,3])
#img[:,:,0] = np.ones([512,512])*64/255.0
#img[:,:,1] = np.ones([512,512])*128/255.0
#img[:,:,2] = np.ones([512,512])*192/255.0

def writeDataToImage(data):
    img_data = convertListToTwoDimentional(data)
    img = np.asarray(img_data)
    cv2.imwrite('wave_shape.png', img)
    cv2.imshow("wave", img);
    cv2.waitKey();

def convertListToTwoDimentional(mylist):
    twoDArray = []
    length = len(mylist)
    maximum = 0.0
    
    for x in mylist:
        if x > maximum:
            maximum = x

    for y in mylist:
        column = []
        for c in range(1024):
            if (c == int(y / maximum * 255)):
                column.append(255.0)
            else:
                column.append(0.0)
        twoDArray.append(column)

    return twoDArray
    
