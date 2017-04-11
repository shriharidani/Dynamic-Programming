def count(arr,change):
	x,y=0,0
	n = len(arr)
	t = [[0]*n for x in range(change+1)]
	for i in range(n):
		t[0][i] = 1
	for j in range(1,change+1):
		for k in range(n):
			x = t[j-arr[k]][k] if j-arr[k] >=0 else 0
			y =  t[j][k-1] if j>=1 else 0
			t[j][k] = x+y 
	return t[change][n-1]

arr = [1,3,2]
print 'Coin change is ',count(arr,4)