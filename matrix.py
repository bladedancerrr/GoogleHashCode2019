from init import getPhotoList, getSlideShow
from scipy.cluster.hierarchy import linkage
import numpy as np
import sys

def intersection(list1, list2): 
	temp = set(list1) 
	result = [value for value in list2 if value in temp] 
	return result

def dist(slide1, slide2):
	return len(slide1.tagList) + len(slide2.tagList) - 2*len(intersection(slide1.tagList, slide2.tagList))


def singleDissimArrayIndex(slideNumber, index):
	"""
	rtype: two item list for accessing the matrix
	"""
	if index < slideNumber:
		return [[slideNumber], [index]]
	else:
		return [[index], [slideNumber]]

class Matrix:
	def __init__(self, slideShow):
		size = len(slideShow)
		matrix = np.zeros((size, size), dtype=int)
		i = 1
		while i < len(slideShow):
			j = 0
			while j < i:
				matrix[i][j] = dist(slideShow[i], slideShow[j])
				j += 1
			i += 1
		self.matrix = matrix
		self.size = size
		self.orderedSlideShow = []
		self.usedPairs = []
		self.slideShow = slideShow

	def allPairsUsed(self):
		# print("length: ", len(self.usedPairs), "	max: ", self.size*self.size - self.size)
		if len(self.usedPairs) == (self.size*self.size - self.size)/2:  # lower triangular matrix
			return True
		return False

	# Highly inefficient

	# def nextUnusedPair(self):
	# 	"""
	# 	:rtype: Tuple
	# 	"""
	# 	assert self.allPairsUsed() == False, "What?? All pairs used!"

	# 	i = 0
	# 	while i < len(self.matrix[0]):
	# 		j = 0
	# 		while j < i:
	# 			pair = (i, j)
	# 			if pair not in self.usedPairs:
	# 				return pair
	# 			j += 1
	# 		i += 1
	

	def appendToOrderedSlideShow(self, pair):
		slide1 = self.slideShow[pair[0]]
		slide2 = self.slideShow[pair[1]]
		if slide1 not in self.orderedSlideShow:
			self.orderedSlideShow.append(slide1)

		if slide2 not in self.orderedSlideShow:
			self.orderedSlideShow.append(slide2)


	def nextMostSimilarPair(self):
		minScore = sys.maxsize
		i = 1
		while i < len(self.matrix[0]):
			j = 0
			while j < i:
				pair = (i, j)
				if self.matrix[i][j] < minScore and pair not in self.usedPairs:
					minScore = self.matrix[i][j]
					minPair = pair
				j += 1
			i += 1
		self.usedPairs.append(minPair)
		return minPair

	def consolidate(self, pair):
		slideNum1 = pair[0]
		slideNum2 = pair[1]
		for i in range(self.size):
			# skip pairs with same numbers or the pair (slideNum1, slideNum2)
			if i != slideNum1 and i != slideNum2:
				minVal = min(self.matrix[singleDissimArrayIndex(slideNum1, i)], self.matrix[singleDissimArrayIndex(slideNum2, i)])
				self.matrix[singleDissimArrayIndex(slideNum1, i)] = minVal
				self.matrix[singleDissimArrayIndex(slideNum2, i)] = minVal

	def percentage(self):
		return round(len(self.usedPairs)*100/((self.size*self.size - self.size)/2), 2)


if __name__ == '__main__':
	photoList = getPhotoList('c')
	slideShow = getSlideShow(photoList)
	matrix = Matrix(slideShow)
	while not matrix.allPairsUsed():
		pair = matrix.nextMostSimilarPair()
		matrix.appendToOrderedSlideShow(pair)
		matrix.consolidate(pair)
		sys.stdout.write(f'\r{matrix.percentage()} % completed')
		sys.stdout.flush()
	print(matrix.orderedSlideShow)