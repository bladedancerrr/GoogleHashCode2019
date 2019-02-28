from photo import Photo



def createSlideshow(photoList):

	slideShow = []

	totalPhotos = len(photoList)

	firstVertPhoto = None
	secondVertPhoto = None
	numVertPhotos = 0

	for photoNum in range(totalPhotos):

		currPhoto = photoList[photoNum]

		if currPhoto.isHorizontal:

			slideShow.append((currPhoto, None))
			currPhoto.isUsed = True

		else:

			numVertPhotos += 1

			if numVertPhotos % 2:

				firstVertPhoto = currPhoto

			else: 

				secondVertPhoto = currPhoto

				slideShow.append((firstVertPhoto, secondVertPhoto))
				firstVertPhoto.isUsed = True
				secondVertPhoto.isUsed = True

	return slideShow

if __name__ == "__main__":
	photo1 = Photo()