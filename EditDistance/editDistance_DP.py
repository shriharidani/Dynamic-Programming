def editDistance(str1,str2,str1Length,str2Length):
	arrayDP = [[0]*(str2Length+1) for x in range(str1Length+1)]
	for i in range(str1Length+1):
		for j in range(str2Length+1):
			if i==0:
				arrayDP[i][j] = j
			elif j==0:
				arrayDP[i][j] = i
			elif str1[i-1] == str2[j-1]:
				arrayDP[i][j] = arrayDP[i-1][j-1]
			else:
				arrayDP[i][j] = 1+min(arrayDP[i-1][j],
								arrayDP[i-1][j-1],
								arrayDP[i][j-1])
	print 'Matrix formed is ',arrayDP
	return arrayDP[str1Length][str2Length]



str1 = "sunday"
str2 = "saturday"

print editDistance(str1,str2,len(str1),len(str2))