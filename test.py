def longestWithSumLessThanK(nums, k):
	max_length,sums=0,0
	for i in range(len(nums)):
		sums+=i
		tl=0
		j=i
		while (sums+nums[j]) <= k:
			tl+=1
			sums+=nums[j]
			j+=1
		if max_length < tl:
			max_length = tl


	return max_length

nums = [1,2,3,4]
print(longestWithSumLessThanK(nums, 4))