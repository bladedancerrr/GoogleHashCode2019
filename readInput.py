def readInput(file): 

	lines = open(file).readlines()
	photos = []
	N = int(lines[0])

	for i in range(1, len(lines)):
		line = lines[i].split()
		isHorizontal = lambda a: a == 'H'
		photos.append((i-1,isHorizontal(line[0]), int(line[1]), []))
		for j in range(int(line[1])):
			photos[i-1][3].append(line[j+2])

	returnList = []
	returnList.append(N)
	returnList.append(photos)
	print(returnList)
	return returnList
	




