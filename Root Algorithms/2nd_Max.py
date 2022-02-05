lst = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,10,10,10,10,10,11,11,11,11,11,13,13,13,13,13, 12]
#lst = [40,32,39,36]
max_1 = lst[0]
max_2 = None
lst.sort()
for i in range(len(lst)):
	if max_1<lst[i]:
		max_2 = max_1
		max_1 = lst[i]
	elif max_2 == None or max_2 < lst[i]:
		if max_1 != lst[i]:
		   max_2 = lst[i]
print(max_1, max_2)





