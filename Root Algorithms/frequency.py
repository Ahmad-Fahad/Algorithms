freq = {}
lst = [6,6,5,5,5,5,9,4,3,2,2,2,2,7,7,1,1,1,3,1,1]
for i in lst:
	if i in freq:
		freq[i] = freq[i]+1
	else:
		freq[i] = 1
for key, value in freq.items():
	print("{} : {}".format(key, value))		
print(freq)

frequency = {}
for i in lst:
	frequency[i] = lst.count(i)
	
for key, value in freq.items():
	print("{} : {}".format(key, value))



	