lst = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,10,10,10,10,10,11,11,11,11,11,13,13,13,13,13, 12]
#lst = [40,32,39,36]
min_1 = lst[0]
min_2 = None
#lst.sort()
for i in range(len(lst)):
	if min_1>lst[i]:
		min_2 = min_1
		min_1 = lst[i]
	elif min_2 == None or min_2 > lst[i]:
		if min_1 != lst[i]:
			min_2 = lst[i]
print(min_1, min_2)


