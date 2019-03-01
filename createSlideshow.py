from photo import Photo
from slide import Slide
from init import getPhotoList

def getSlideshow(photoList):
	"""
	:param photoList: a list of Photos
	:rtype slideShow: a list of Slides
	"""
	slideShow = []
	verticalPhotos = []
	for photo in photoList:
		if photo.isHorizontal:
			slideShow.append(Slide(photo))
		else:
			if len(verticalPhotos) == 2:
				slideShow.append(Slide(verticalPhotos[0], secondPhoto=verticalPhotos[1]))
				verticalPhotos = []
			else:
				verticalPhotos.append(photo)
	return slideShow


if __name__ == "__main__":
	photoList = getPhotoList('a')
	print(getSlideshow(photoList))