def Insertion_Sort(lst):
	l = len(lst)
	for i in range(1,l):
		temp = lst[i]
		j = i-1
		while j>=0:
			if temp<lst[j]:
				lst[j+1] = lst[j]
				lst[j]   = temp
			j = j-1
	return lst

lst = [3,2,1]
print(Insertion_Sort(lst))

"""
lst = [6,5,4,3,2,1]
l   = len(lst) 
for i in range(1, l):
	temp = lst[i]
	for j in range(i-1, -1, -1):
		if temp<lst[j]:
			lst[j+1] = lst[j]
			lst[j]   = temp


print(lst)

"""