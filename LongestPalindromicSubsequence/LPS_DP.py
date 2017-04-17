def LPS(seq):
	n=len(seq)
	arrayDP = [[0]*n for x in range(n)]

	for i in range(n):
		arrayDP[i][i] = 1
	for l in range(2,n+1):
		for i in range(n-l+1): # 0 to 11 
			j=i+l-1 #1 to 12
			if seq[i] ==seq[j] and l==2:
				arrayDP[i][j] = 2
			elif seq[i] == seq[j]:
				arrayDP[i][j] =2+arrayDP[i+1][j-1]
			else:
				arrayDP[i][j] = max(arrayDP[i][j-1],arrayDP[i+1][j])
	return arrayDP[0][n-1]

seq = "geeksforgeeks"
print 'length of longest palindromic subsequence is ',LPS(seq)