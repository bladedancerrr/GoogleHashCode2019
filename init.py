from readInput import readInput
from photo import Photo

def getFile(letter='a'):
	fileDict = {'a':'a_example.txt', 'b':'b_lovely_landscapes.txt', 'c':'c_memorable_moments.txt', 'd':'d_pet_pictures.txt', 'e':'e_shiny_selfies.txt'}
	return f"inputFiles/{fileDict[letter]}"

def getPhotoList(letter):
	dataList = readInput(getFile(letter))
	return [Photo(dataItem) for dataItem in dataList]

if __name__ == '__main__':
	photoList = getPhotoList('a')
	for photo in photoList:
		print(photo.tagList)
