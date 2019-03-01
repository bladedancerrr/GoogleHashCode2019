from init import getPhotoList, getSlideShow
from writeOutput import writeOutput
from makeSizeClasses import makeSizeClasses
from matrix import getMatrix


def main():

    # read input
    # Create photos
    photoList = getPhotoList('d')
    print("Created list of photos")
    slideShow = getSlideShow(photoList)
    print("Created list of slides")
    matrix = getMatrix(slideShow)
    print(matrix)
    # # sorted the slides according to their tag numbers create size classes
    # sizeClasses = makeSizeClasses(slides, 5)
    # print(sizeClasses)
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
