import os, pdb, struct, random
import numpy as np
import matplotlib
# why is this brokennnn
matplotlib.use('PS')
import matplotlib.pyplot as plt

from pandas import DataFrame

# documentation on the data files can be found at http://yann.lecun.com/exdb/mnist/index.html

# set the paths to the training & testing files
data_path = 'data/'
train_label_file = os.path.join(data_path, 'train-labels-idx1-ubyte')
train_image_file = os.path.join(data_path, 'train-images-idx3-ubyte')
test_label_file = os.path.join(data_path, 't10k-labels-idx1-ubyte')
test_image_file = os.path.join(data_path, 't10k-images-idx3-ubyte')

# set the number of examples in the files
n_examples = 1
# images are 28x28 pixels
IM_RES = 28
# images are scaled from 0 to 255 for each pixel value
IM_SCALE = 255

# stores a handwritten number and its label
# label <int> : the correct numerical value of the number
# image <arr[int]> : array of length IM_RES**2,
#   listing all pixel values on a 0-1 scale, top left to bottom right, read like words on a page
class Number:

	def __init__(self, label=None, image=None):
		self.label = label
		self.image = image

	def getAsDataFrame(self):
		to_arr = []
		for i in range(IM_RES):
			to_arr.append(self.image[i*IM_RES:(i+1)*IM_RES])
		return DataFrame(to_arr)

	def showImage(self):
		df = self.getAsDataFrame()
		plt.imshow(df)


# read the next number in from the label file and the image file
# inputs: label file, image file
#   NOTE that both files must already be read up to the next number
# output: Number class object
def readNumber(label_file, image_file):
	label = struct.unpack('B', label_file.read(1))[0]
	# flat (unpacked) array, reading from top to bottom, left to right, like words on a page
	im_array = []
	for s in range(IM_RES*IM_RES):
		im_array.append(struct.unpack('B', label_file.read(1))[0]/IM_SCALE)
	return Number(label, im_array)

print('reading in data')
numbers = []
with open(train_label_file, 'rb') as lab_file:
	with open(train_image_file, 'rb') as im_file:
		# read through the beginning of the label file
		lab_file.read(8)
		# read through the beginning of the image file
		im_file.read(16)
		# read in the next label and the next 
		for i in range(n_examples):
			numbers.append(readNumber(lab_file, im_file))

numbers[0].getAsDataFrame()
