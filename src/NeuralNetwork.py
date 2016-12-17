import numpy as np
import neurolab as nl

def neuralNetworkTest(imgMSE, histMSE):
	# Create train samples
	input1 = imgMSE
	input2 = histMSE
	#input = np.random.uniform(-0.5, 0.5, (30, 2))
	#target = (input[:, 0] + input[:, 1]).reshape(30, 1)
	target = similarityAlgorithm(imgMSE, histMSE)
	# Create network with 2 inputs, 5 neurons in input layer and 1 in output layer
	net = nl.net.newff([[0, 2000.0], [0, 100.0]], [5, 1])
	# Train process
	err = net.train(input1, input2, target, show=10)
	# Test
	print net.sim([[1040.8, 78.5]]) # 0.2 + 0.1

def similarityAlgorithm(imgMSE, histMSE):
	imgPer = 1 - imgMSE / 2000;
	histPer = 1 - histMSE / 100;
	finalPer = (imgPer + hisPer) / 2
	return finalPer
'''
def main():
	neuralNetworkTest()

main()
'''
