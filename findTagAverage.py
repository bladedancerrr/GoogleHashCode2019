def findTagAverage(slides):
	numSlides = len(slides)
	sumTagNumbers = 0
	for slide in slides: 
		sumTagNumbers += slide.tagNumber
	average = sumTagNumbers/numSlides
	return int((average/3)*2)



		





