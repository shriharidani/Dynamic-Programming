# length of lis in nlog(n) time
def ceil(array,left,right,key):
	while right-left > 1:
		mid = left+(right-left)/2
		if array[mid] >= key :
			right=mid
		else:
			left = mid
	return right


def lis(arr):
	n=len(arr)
	temp= [-1]*n
	temp[0] = arr[0]
	length = 1
	for i in range(n):
		if arr[i]<temp[0]:
			temp[0]=arr[i]
		elif arr[i] > temp[length-1]:
			temp[length] = arr[i]
			length +=1
		else:
			temp[ceil(temp,-1,length-1,arr[i])] = arr[i]
	return length

arr = [10, 22, 9, 33, 21, 50, 41, 60]
print 'Length of lis is ',lis(arr)