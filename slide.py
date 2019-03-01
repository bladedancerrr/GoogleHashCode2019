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
			self.secondPhoto = None
		else:
			self.isHorizontal = False
			self.tagList = union(firstPhoto.tagList, secondPhoto.tagList)
			self.tagNumber = len(self.tagList)
			self.firstPhoto = firstPhoto
			self.secondPhoto = secondPhoto