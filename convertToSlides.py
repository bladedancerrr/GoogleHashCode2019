import slide 

def convertToSlides(photoList):
	"""takes a list of photos and converts it into a list of slides"""

	slideShow = []
	vertical = []
	horizontal = []

	for photo in photoList:
		if photo.isHorizontal: 
			horizontal.append(photo)
		else:
			vertical.append(photo)

	for hPhoto in horizontal:
		s = Slide(horizontal)
		s.isUsed = True
		slideShow.append(s)

	if len(vertical)%2 == 0:
		for i in range(0, len(vertical), 2):
			s = Slide(vertical[i], vertical[i+1])
			s.isUsed = True
			slideShow.append(s)

	return slideShow
