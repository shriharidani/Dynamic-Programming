def lcs(X,Y):
	n = len(X)
	m = len(Y)
	arrayDP = [[None]*(n+1)for i in range(m+1)]
	for i in range(m+1):
		for j in range(n+1):
			if i==0 or j==0:
				arrayDP[i][j] = 0
			elif Y[i-1] == X[j-1]:
				arrayDP[i][j] = arrayDP[i-1][j-1] + 1
			else:
				arrayDP[i][j] = max(arrayDP[i-1][j],arrayDP[i][j-1])
	return arrayDP[m][n]

X = "AGGTAB"
Y = "GXTXAYB"
print "Length of LCS is ", lcs(X, Y)