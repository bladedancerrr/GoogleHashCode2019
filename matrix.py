from slide import union, intersection
from init import getPhotoList
from slide import Slide
from scipy.cluster.hierarchy import linkage
import numpy as np

def dist(slide1, slide2):
	return len(slide1.tagList) + len(slide2.tagList) - 2 *len(intersection(slide1, slide2))

def getMatrix(slideshow):
	matrix = np.zeros((len(slideshow), len(slideshow)), dtype=int)
	i = 1
	while i < len(slideshow):
		j = 0
		while j < i:
			matrix[i][j] = dist(slideshow[i], slideshow[j])
			j += 1
		i += 1
	return matrix



if __name__ == '__main__':
	photoList = getPhotoList('a')
	slide1 = Slide(photoList[1], secondPhoto=photoList[2])
	slide2 = Slide(photoList[0])
	print(getMatrix([slide1, slide2]))