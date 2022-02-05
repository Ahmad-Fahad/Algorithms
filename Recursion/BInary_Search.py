def Binary_Search(lst, x, l, r):
	if l >= r:
		return -1
	mid = (l+r)//2
	mid = int(mid)
	print("__",mid)
	if lst[mid] == x:
		print(mid)
		return mid
	if lst[mid] > x:
		Binary_Search(lst, x, l, mid-1)
	if lst[mid] < x:
		Binary_Search(lst, x, mid+1, r)

lst = [1,2,3,4,5,6,7,8,9,10]
for i in range(11): 
	x = i
	l = 0
	r = len(lst)-1
	print(i)
	flag = Binary_Search(lst, x, l, r)
	print(flag)
	print("......")
