def binomialCoefficient(n,k):
	print n,k
	if k==0 or k==n:
		return 1
	included = binomialCoefficient(n-1,k-1)
	excluded = binomialCoefficient(n-1,k)
	print included,excluded
	return included+excluded
n=5
k=2
print binomialCoefficient(5,2)