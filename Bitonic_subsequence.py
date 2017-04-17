def lbs(arr):
	n=len(arr)
	lis = [1 for i in range(n+1)]
	lds = [1 for j in range(n+1)]
	for i in range(1,n):
		for j in range(0,i):
			if (arr[i] > arr[j]) and (lis[i] < lis[j]+1):
				lis[i] = lis[j] +1
	for k in range(1,n):
		for l in range(0,i):
			if (arr[k] < arr[l]) and (lds[k] < lds[l+1]+1):
				lds[k] = lds[l]+1
	maximum = lis[0]+lds[0] -1
	for i in range(1,n):
		maximum = max(lis[i]+lds[i]-1,maximum)
	return maximum
arr =  [0 , 8 , 4, 12, 2, 10 , 6 , 14 , 1 , 9 , 5 , 13, 3, 11 , 7 , 15]
print "Length of LBS is",lbs(arr)