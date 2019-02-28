import Photo

def createSlideshow(photoList):

	slideShow = []

	totalPhotos = len(photoList)

	firstVertPhoto = None
	secondVertPhoto = None
	numVertPhotos = 0

	for photoNum in totalPhotos:

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


			slideShow.append(currPhoto)

	return slideShow

