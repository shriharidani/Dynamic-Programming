def LPS(seq,start,end):
	if start == end:
		return 1
	if seq[start] == seq[end] and start+1==end:
		return 2
	if seq[start] == seq[end]:
		return 2 + LPS(seq,start+1,end-1)
	return max(LPS(seq,start,end-1),LPS(seq,start+1,end))

seq = "geeksforgeeks"
n = len(seq)
print 'length of longest palindromic subsequence is ',LPS(seq,0,n-1)