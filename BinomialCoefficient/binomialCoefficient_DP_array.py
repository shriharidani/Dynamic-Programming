def binomialCoefficient(n,k):
	arrayDP = [0 for x in range(k+1)]
	arrayDP[0] = 1
	for i in range(1,n+1):
		j = min(i,k)
		while j>0:
			arrayDP[j] = arrayDP[j]+arrayDP[j-1]
			j-=1
	return arrayDP[k]
n=5
k=2
print binomialCoefficient(n,k)