def count(array,arrayLength,change):
 	if change ==0:
 		return 1
 	if change <0:
 		return 0
 	if arrayLength<=0 and change >= 1:
 		return 0
 	return count(array,arrayLength-1,change) + count(array,arrayLength,change-array[arrayLength-1])
arr =[1,2,3]
print 'count = ', count(arr,len(arr),4)