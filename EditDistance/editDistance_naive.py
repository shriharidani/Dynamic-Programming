def editDistance(str1,str2,str1Length,str2Length):

	if str1Length == 0:
		return str2Length
	if str2Length == 0:
		return str1Length
	if str1[str1Length-1] == str2[str2Length-1]:
		return editDistance(str1,str2,str1Length-1,str2Length-1)
	
	return 1 + min(editDistance(str1,str2,str1Length,str2Length-1),
					editDistance(str1,str2,str1Length-1,str2Length),
					editDistance(str1,str2,str1Length-1,str2Length-1))

str1 = "sunday"
str2 = "saturday"

print editDistance(str1,str2,len(str1),len(str2))