from init import getPhotoList

def intersection(firstPhoto, secondPhoto): 
	temp = set(secondPhoto.tagList) 
	result = [value for value in firstPhoto.tagList if value in temp] 
	return result

def union(list1, list2):
	return set(list1).union(set(list2))

class Slide:
	def __init__(self, firstPhoto, secondPhoto=None):
		self.isUsed = False
		if secondPhoto == None:
			self.isHorizontal = True
			self.tagNumber = firstPhoto.tagNumber
			self.tagList = firstPhoto.tagList
			self.firstPhoto = firstPhoto
			self.secondPhoto = secondPhoto
		else:
			self.isHorizontal = False
			self.tagList = union(firstPhoto.tagList, secondPhoto.tagList)
			self.tagNumber = len(self.tagList)
			self.firstPhoto = firstPhoto
			self.secondPhoto = secondPhoto

if __name__ == '__main__':
	photoList = getPhotoList('a')
	slide = Slide(photoList[1], secondPhoto=photoList[2])
	print(slide.isHorizontal)