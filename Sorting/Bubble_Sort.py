def Bubble_Sort(lst):
	l = len(lst)
	for i in range(l):
		for j in range(l-1):
			if lst[j] > lst[j+1]:
				lst[j+1], lst[j] = lst[j], lst[j+1]
	return lst

lst = [6,5,4,3,2,1]
print(Bubble_Sort(lst))



'''
lst = [6,5,4,3,2,1]
l   = len(lst)
for i in range(l):
	for j in range(l-1):
		if lst[j] > lst[j+1]:
			lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst)

'''