def Binary_Search(lst, x):
	length = len(lst)
	left   = 0
	right  = length-1
	while left<=right:
		mid = (left+right)/2
		mid = int(mid)
		if lst[mid] == x:
			return mid
		elif lst[mid] < x:
			left = mid+1
		elif lst[mid] > x:
			right = mid-1
	return -1

lst    = [1,2,3,4,5,6,7,8,9,10]
while True:
	x      = int(input())
	index  = Binary_Search(lst, x)
	if index == -1:
		print("Not Found")
	else:
		print("Position  ", index)


'''

while True:
	lst    = [1,2,3,4,5,6,7,8,9,10]
	x      = int(input())
	length = len(lst)
	left   = 0
	right  = length-1
	flag   = 0
	while left<=right:
		mid    = (left+right)/2
		mid    = int(mid)
		if lst[mid] == x:
			flag = 1
			break
		if lst[mid] > x:
			right = mid-1
		if lst[mid] < x:
			left  = mid+1
	if flag == 1:
		print("Position  ", mid)
	else:
		print("Not Found")

'''