from photo import Photo

def createOutput(slideList):
    outputFile = open("Output.txt", "w")
    outputFile.write("{}\n".format(len(slideList)))
    for slide in slideList:
        photo1 = slide[0]
        photo2 = slide[1]
        outputFile.write("{}".format(photo1.ID))
        if photo2:
            outputFile.write(" {}".format(photo2.ID))
        outputFile.write("\n")
    outputFile.close()

if __name__ == "__main__":
    photoList = []
    data = [(0, False, 3, ['cat', 'dog', 'peter']), (1, False, 2, ['lexon', 'smart']), (2, True, 2, ['lexon', 'genius']), (3, True, 2, ['Hello', 'world']), (4, False, 2, ['swag', 'smart'])]
    for dataItem in data:
        photoList.append(Photo(dataItem))
    slideList = [(photoList[0], photoList[1]), (photoList[2], None), (photoList[3], None)]
    createOutput(slideList)
