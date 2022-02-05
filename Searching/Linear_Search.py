def Linear_Search(lst, x):
	i = 0
	n = len(lst)
	while(i < n):
		if lst[i] == x:
			return i
		i += 1
	return -1
while True:
	lst   = [1,2,3,4,5,6,7,89,90,67,45,34]
	x     = int(input())
	index = Linear_Search(lst, x)
	print(index)
	if index == -1:
		print("Not Found")
	else:
		print("Found in ", index)




'''
......For and index.......

def linear_search(lst, x):
	i = 0
	n = len(lst)
	for i in range(n):
		if lst[i] == x:
			return i
	return -1

while True:
	lst   = [1,2,3,4,5,6,7,89,90,67,45,34]
	x     = int(input())
	index = linear_search(lst, x)
	print(index)
	if index == -1:
		print("Not Found")
	else:
		print("Found in ", index)




def linear_search(lst, x):
	flag = 0
	for i in lst:
		if i == x:
			flag = 1
			break
	return flag


lst = [1,2,3,4,5,6,7,89,90,67,45,34]
x   = int(input())
r   = linear_search(lst, x)
if r == 1:
	print("Found")
else:
	print("Not Found")





......In main Direct method.......
flag = 0
for i in lst:
	if i == x:
		flag = 1
		break
if flag == 1:
	print("Found")
else:
	print("Not Found")

'''