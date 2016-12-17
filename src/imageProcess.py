import cv2
import numpy as np
from matplotlib import pyplot as plt
import Output
#from skimage.measure import structural_similarity as ssim
 
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

def readImageAsGray(imageFile):
    img = cv2.imread(imageFile)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imwrite('save.png', img)
    #cv2.imshow("save", img);
    return img

def readImageAsColor(imageFile):
    img = cv2.imread(imageFile)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return img
    
def computeHistogram(img1, img2):
    hist1 = cv2.calcHist([img1], [0], None, [256], [0,256])
    hist2 = cv2.calcHist([img2], [0], None, [256], [0,256])
    #plt.hist(img1.ravel(), 256, [0,256]);
    #plt.hist(img2.ravel(), 256, [0,256]);
    #plt.plot(hist1)
    #plt.plot(hist2)
    #plt.xlim([0,512])
    #plt.show()
    return hist1, hist2

def computeColorHSVHistogram(img1, img2):
    hist1 = cv2.calcHist([img1], [0, 1], None, [180, 256], [0, 180, 0, 256])
    hist2 = cv2.calcHist([img2], [0, 1], None, [180, 256], [0, 180, 0, 256])
    #plt.imshow(hist1, interpolation = 'nearest')
    #plt.imshow(hist2, interpolation = 'nearest')
    #plt.show()
    return hist1, hist2
    

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	#s = ssim(imageA, imageB)
 
	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f:" % m)
 
	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")
 
	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")
 
	# show and save the images
	Output.SaveImage(plt)
	plt.show()

def compare_histograms(hist1, hist2, title):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(hist1, hist2)
	#s = ssim(hisA, hisB)
 
	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f:" % m)
 
	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(hist1, interpolation = 'nearest')
	plt.axis("off")
 
	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(hist2)
	plt.axis("off")
 
	# show and save the images
	Output.SaveImage(plt)
	plt.show()

#def main():
#    #img1 = readImageAsGray('pic1.png')
#    #img2 = readImageAsGray('pic2.png')
#    img1 = readImageAsColor('pic1.png')
#    img2 = readImageAsColor('pic2.png')

#    hist1, hist2 = computeHistogram(img1, img2)
#    #hist1, hist2 = computeColorHSVHistogram(img1, img2)
#    compare_images(img1, img2, 'Images Comparison')
#    #compare_histograms(hist1, hist2, 'Histogram Comparison')

#main()

    
