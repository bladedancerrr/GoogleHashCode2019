from slide import Slide
from init import getPhotoList
from slide import Slide
from scipy.cluster.hierarchy import linkage
import numpy as np

def intersection(list1, list2): 
	temp = set(list1) 
	result = [value for value in list2 if value in temp] 
	return result

def dist(slide1, slide2):
	return len(slide1.tagList) + len(slide2.tagList) - 2*len(intersection(slide1.tagList, slide2.tagList))

def getMatrix(slideShow):
	matrix = np.zeros((len(slideShow), len(slideShow)), dtype=int)
	i = 1
	while i < len(slideShow):
		j = 0
		while j < i:
			matrix[i][j] = dist(slideShow[i], slideShow[j])
			j += 1
		i += 1
	return matrix



if __name__ == '__main__':
	photoList = getPhotoList('a')
	slideShow = getSlideShow(photoList)
	print(getMatrix(slideShow))