def knapSack(W,wt,val,n):
	arrayDP = [[0]*(W+1) for x in range(n+1)]
	for i in range(n+1):
		for w in range(W+1):
			if i==0 or W==0:
				arrayDP[i][w] = 0
			elif wt[i-1] <= w:
				arrayDP[i][w] = max(val[i-1]+arrayDP[i-1][w-wt[i-1]],
								arrayDP[i-1][w])
			else:
				arrayDP[i][w] = arrayDP[i-1][w]
	return arrayDP[n][W]
val =[60,100,120]
wt = [10,20,30]
W = 50
n=len(val)
print knapSack(W,wt,val,n)