import math
from operator import itemgetter
from slide import Slide

def makeSizeClasses(slideSizeList, nClasses):

	sortedSlideList = slideSizeList.sort(key = itemgetter(1))

	return splitToClasses(sortedSlideList, nClasses)


def makeSlideSizeList(slideList):

	output = []

	for slide in slideList:

		output.append((slide, slide.tagNumber))

	return output



def splitToClasses(sortedSlideList, nClasses):

	output = []

	maxTags = sortedSlideList[-1].tagNumber
	classSize = math.ceiling(maxTags/nClasses)

	assert(maxTags >= nClasses)
	assert(classSize >= 1)

	currentClassMax = classSize

	sizeClass = []

	for slide in sortedSlideList:
		
		if slide.tagNumber < currentClassMax:
			sizeClass.append(slide)
		else:
			output.append(sizeClass)
			sizeClass = []
			currentClassMax += classSize

	return output

