def binomialCoefficient(n,k):
	t = [[0]*(k+1) for x in range(n+1)]
	for i in range(n+1):
		for j in range(min(i,k)+1):
			if j==0 or j==i:
				t[i][j] = 1
			else:
				t[i][j] = t[i-1][j-1]+t[i-1][j]
	return t[n][k]
n=5
k=2
print binomialCoefficient(n,k)