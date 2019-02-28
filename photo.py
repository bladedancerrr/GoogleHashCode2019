class Photo:
	def __init__(self, data):
		self.ID = data[0]
		self.isHorizontal = data[1]
		self.tagNumber = data[2]
		self.tagList = data[3]
		self.isUsed = False