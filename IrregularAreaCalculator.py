def polygonArea(X, Y, n):

	area = 0.0

	j = n - 1
	for i in range(0,n):
		area += (X[j] + X[i]) * (Y[j] - Y[i])
		j = i
	
	return int(abs(area / 2.0))

