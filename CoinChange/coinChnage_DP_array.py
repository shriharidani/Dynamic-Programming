def count(arr,change):
	x,y=0,0
	n = len(arr)
	t = [0]*(change+1)
	t[0]=1
	for i in range(n):
		for j in range(arr[i],change+1):
			t[j] += t[j-arr[i]]
	return t[change]
arr = [1,3,2]
print 'Coin change is ',count(arr,4)