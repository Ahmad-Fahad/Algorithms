def Sort_in_range(lst, start, end):
	temp = []
	for i in range(start,end+1): 
		temp.append(lst[i])
	temp.sort()
	k = 0
	for i in range(start, end+1):
		lst[i] = temp[k]
		k += 1
	return lst

lst_0 = [5, 21, 2, 67, 12, 7, 66, 3, 5]
lst_0 = Sort_in_range(lst_0, 1,6)
print(lst_0)
	