#recursive approach which takes exponential time 
global max_length_lis
max_length_lis =1
def lis(arr,n):
	global max_length_lis
	if n==1:
		return 1
	current_lis_length = 1
	for i in range(0,n-1):
		sub_lis_length = lis(arr,i)
		if current_lis_length < (1+sub_lis_length) and arr[i] <= arr[n-1]:
			current_lis_length = 1+sub_lis_length
	if max_length_lis < current_lis_length:
		max_length_lis = current_lis_length
	return current_lis_length


def main():
	arr=[10, 22, 9, 33, 21, 50, 41, 60]
	n = len(arr)
	print 'Length of LIS is ',lis(arr,n)

if __name__=="__main__":
	main()