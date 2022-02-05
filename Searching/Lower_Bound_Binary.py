from bisect import bisect_left
def Search(lst, x):
	index = bisect_left(lst,x)
	if index != len(lst) and lst[index] == x:
		return index
	else:
		return -1

lst = [9,9,8,8,3,3,2,2,1,1]
x = 8

lst.sort()
print(lst)
index = Search(lst, x)
print(index)
