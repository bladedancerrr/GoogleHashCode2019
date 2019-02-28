def findTagAverage(slides):
	numSlides = len(slides)
	sumTagNumbers = 0
	for slide in slides: 
		sumTagNumbers += slide.tagNumber
	average = int(sumTagNumbers/numSlides)
	return (average/3)*2



		





