from slide import union, intersection
from init import getPhotoList
from slide import Slide
from scipy.cluster.hierarchy import linkage
import numpy as np

def dist(slide1, slide2):
	return len(slide1.tagList) + len(slide2.tagList) - 2 *len(intersection(slide1, slide2))

def getMatrix(slideshow):
	matrix = np.array([0, len(slideshow)-1, 0, len(slideshow)-1])
	i = 0
	for slide1 in slideshow:
		j = 0
		for slide2 in slideshow:
			matrix[i][j] = dist(slide1, slide2)
			j += 1
		i += 1
	return matrix



if __name__ == '__main__':
	photoList = getPhotoList('a')
	slide1 = Slide(photoList[1], secondPhoto=photoList[2])
	slide2 = Slide(photoList[0])
	print(getMatrix([slide1, slide2]))
	print(dist(slide1, slide2))
