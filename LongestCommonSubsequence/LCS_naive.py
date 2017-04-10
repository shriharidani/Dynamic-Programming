#LCS naive approach take exponential time
def lcs(X,Y,n,m):
	#there will be no common subsequences
	if n==0 or m==0:
		return 0
	if X[n-1] == Y[m-1]:
		return 1+ lcs(X,Y,n-1,m-1)
	return max(lcs(X,Y,n-1,m),lcs(X,Y,n,m-1))
X="AGGTAB"
Y="GXTXAYB"
print 'Length of LCS is ',lcs(X,Y,len(X),len(Y))