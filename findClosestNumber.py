def findClosestNumber(matrix, n):
	rows = matrix.shape[0]
	cols = matrix.shape[1]
	closest = 10000000000000000000
	row = 0
	col = 0
	for i in range(rows):
		for j in range(cols):
			if abs(n-matrix[i][j]) < closest:
				row = i
				col = j
				closest = abs(n-matrix[i][j])
	coordinates = (row, col)

	return coordinates


	


