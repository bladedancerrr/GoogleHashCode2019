from init import getPhotoList, getSlideShow
from scipy.cluster.hierarchy import linkage
import numpy as np

def intersection(list1, list2): 
	temp = set(list1) 
	result = [value for value in list2 if value in temp] 
	return result

def dist(slide1, slide2):
	return len(slide1.tagList) + len(slide2.tagList) - 2*len(intersection(slide1.tagList, slide2.tagList))

class Matrix:
	def __init__(self, slideShow):
		matrix = np.zeros((len(slideShow), len(slideShow)), dtype=int)
		i = 1
		while i < len(slideShow):
			j = 0
			while j < i:
				matrix[i][j] = dist(slideShow[i], slideShow[j])
				j += 1
			i += 1
		self.matrix = matrix

		self.orderedSlideShow = []

	def nextMostSimilarPair(self):
		minScore = self.matrix[1][0]
		minPair = (1, 0)
		i = 1
		while i < len(self.matrix[0]):
			j = 0
			while j < i:
				if self.matrix[i][j] < minScore:
					minScore = self.matrix[i][j]
					minPair = (i, j)
				j += 1
			i += 1
		print(minScore)
		return minPair

	def consolidate(self, pair):
		# row oriented consolidation
		print(self.matrix[pair[0]])



if __name__ == '__main__':
	photoList = getPhotoList('c')
	slideShow = getSlideShow(photoList)
	matrix = Matrix(slideShow)
	pair = matrix.nextMostSimilarPair()
	matrix.consolidate(pair )