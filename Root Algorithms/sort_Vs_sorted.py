lst = [6,6,5,5,5,5,9,4,3,2,2,2,2,7,7,1,1,1,3,1,1]
lst.sort()
print(lst)

lst_1 = [6,6,5,5,5,5,9,4,3,2,2,2,2,7,7,1,1,1,3,1,1]

lst_t = sorted(lst_1) #return sorted list

print(lst_1) #does not modify main list
print(lst_t)

d      = {"aa": 3, "bb": 4, "cc": 2, "dd": 1}
d_sort = sorted(d, key=d.get, reverse=True)
for k in d_sort:
	print(k, d[k])


d_int = {8: 3, 5: 4, 6: 2, 7: 1}


for k in sorted(d_int, key=d_int.get):
	print(k, d_int[k])

print(d.get("bb")) 
print(d_int.get(5))