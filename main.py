from init import getPhotoList
from createSlideshow import createSlideshow
from createOutput import createOutput
from convertToSlides import convertToSlides


def main():

    # read input
    # Create photos
    photoList = getPhotoList('c')

    # create slides
    slides = convertToSlides(photoList)
    print(slides)

    # # sorted the slides according to their tag numbers create size classes
    # sizeClasses = makeSizeClass(slides)
    #
    #
    # slideShow = []
    # for sizeClass in sizeClasses:
    # # for each size class
    #     # build dis matrix
    #     disMatrix = buildMatrix(sizeClass)
    #     # iterate through size classes, to find their average /3 * 2, and find row and col, append to slide show, # delete row and column, # update matrix and repeat until we can't anymore
    #     miniSlideShow = createSlideshow(disMatrix)
    #     slideShow.append(miniSlideShow)
    # # create output
    # createOutput(slideShow)

if __name__ == '__main__':
	main()
