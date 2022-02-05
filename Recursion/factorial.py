def factorial(n):
	if n < 0:
		return None
	if n in [0,1]:
		return 1
	else:
		return n*factorial(n-1)

for i in range(12):
	print("{} --> {}".format(i, factorial(i)))