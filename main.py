from init import getPhotoList, getSlideShow
from writeOutput import writeOutput
from makeSizeClasses import makeSizeClasses
from matrix import Matrix
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import sys
import timeit


def main():

    # read input
    # Create photos
    letterList = ['c']
    for letter in letterList:
        print(f"\nProcessing file {letter}")
        start = timeit.default_timer()
        photoList = getPhotoList(letter)
        slideShow = getSlideShow(photoList)
        matrix = Matrix(slideShow)
        while not matrix.allPairsUsed():
            pair = matrix.nextMostSimilarPair()
            matrix.appendToOrderedSlideShow(pair)
            matrix.consolidate(pair)
            sys.stdout.write(f'\r{matrix.percentage()} % completed')
            sys.stdout.flush()
        stop = timeit.default_timer()
        print(f"\nElapsed time (in seconds): ", stop-start)
        writeOutput(matrix.orderedSlideShow, letter)

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
