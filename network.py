import os, pdb, struct, random, sys
import numpy as np
import matplotlib

# why is matplotlib brokennnn on python3
matplotlib.use('TkAgg')

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
n_training = 100
n_testing = 10000
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
		plt.title('this is a {}'.format(self.label))
		plt.show()

# numbers <Number []> : list of number objects
# size <int> : length of {self.numbers}
class NumberList:

	# label_file: path to the file containing the number labels
	# image_file: path to the file containing the handwritten number images
	# n_numbers: the number of numbers to read in.
	#   defaults to the number of numbers in label_file and image_file; throws exception if they disagree
	def __init__(self, label_file, image_file, n_numbers=None):
		self.numbers = []
		self.label_file = label_file
		self.image_file = image_file
		with open(train_label_file, 'rb') as lab_file:
			with open(train_image_file, 'rb') as im_file:
				# pass by the magic numbers
				lab_file.read(4)
				im_file.read(4)
				# get the number of numbers 
				n_labs = struct.unpack('i', lab_file.read(4))[0]
				n_ims = struct.unpack('i', im_file.read(4))[0]
				# make sure they agree
				if n_ims != n_labs:
					raise Exception('Number of images and labels should agree')
				# use this number as n_numbers, unless one was provided
				if not n_numbers:
					n_numbers = n_ims
				self.size = n_numbers

				# read in the actual data
				for i in range(n_numbers):
					cur_label = struct.unpack('B', label_file.read(1))[0]
					cur_im_array = []
					for s in range(IM_RES*IM_RES):
						cur_im_array.append(struct.unpack('B', im_file.read(1))[0]/IM_SCALE)
					self.numbers.append(Number(cur_label, cur_im_array))


with open(train_label_file, 'rb') as lab_file:
	with open(train_image_file, 'rb') as im_file:
		# read through the beginning of the label file
		lab_file.read(8)
		# read through the beginning of the image file
		im_file.read(16)
		# read in the next label and the next image
		for i in range(n_training):
			n_testing = 10000
			numbers.append(readNumber(lab_file, im_file))

for i in range
