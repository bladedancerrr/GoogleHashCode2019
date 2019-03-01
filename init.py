"""
Initialization of file, photoList and slideShow
"""
from readInput import readInput
from photo import Photo
from slide import Slide

def getFile(letter='a'):
	fileDict = {'a':'a_example.txt', 'b':'b_lovely_landscapes.txt', 'c':'c_memorable_moments.txt', 'd':'d_pet_pictures.txt', 'e':'e_shiny_selfies.txt'}
	return f"inputFiles/{fileDict[letter]}"

def getPhotoList(letter):
	"""
	:param letter: char
	:rtype: list of Photos'
	"""
	dataList = readInput(getFile(letter))
	photoList = [Photo(dataItem) for dataItem in dataList]
	return photoList

def getSlideShow(photoList):
	"""
	:param photoList: a list of Photos
	:rtype slideShow: a list of Slides
	"""
	slideShow = []
	verticalPhoto = None
	for photo in photoList:
		if photo.isHorizontal:
			slideShow.append(Slide(photo))
		else:
			if verticalPhoto:
				slideShow.append(Slide(verticalPhoto, secondPhoto=photo))
				verticalPhoto = None
			else:
				verticalPhoto = photo
	return slideShow

if __name__ == '__main__':
	photoList = getPhotoList('a')
	slideShow = getSlideShow(photoList)
