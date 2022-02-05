def Selection_Sort(lst):
	l = len(lst)
	for i in range(l-1):
		min = lst[i]
		for j in range(i+1, l):
			if min>lst[j]:
				min   = lst[j]
				index = j
		lst[i], lst[index] = lst[index], lst[i]
	return lst
lst = [3,2,1] #problem generating
print(Selection_Sort(lst))

"""

lst = [6,5,4,3,2,1]

l   = len(lst)
for i in range(l-1):
	min = lst[i]
	for j in range(i+1, l):
		if min>lst[j]:
			min   = lst[j]
			index = j 
	lst[i],lst[index] = lst[index], lst[i]

print(lst)



"""

