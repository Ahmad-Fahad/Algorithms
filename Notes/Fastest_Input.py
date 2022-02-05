from sys import stdin, stdout  
"""
n = stdin.readline()

print(type(n)) # input also str
stdout.write(str(n))  # must be str
"""
arr = [int(x) for x in stdin.readline().split()]
print(arr)
for i in range(len(arr)):
	stdout.write(str(arr[i])+" ") 
