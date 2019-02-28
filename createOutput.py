def createOutput(slideList):
    outputFile = open("Output.txt", "w")
    outputFile.write("{}\n".format(len(slideList)))
    for slide in slideList:
        photo1 = slide[0]
        photo2 = slide[1]
        outputFile.write("{}".format(photo1))
        if photo2:
            outputFile.write("{}".format(photo1))
        outputFile.write("\n")
    outputFile.close()


# if __name__ == "__main__":
