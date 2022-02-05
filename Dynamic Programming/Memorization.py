cache = {}
def memorized(n):
	if n in cache:
		return cache[n]
	else:
		cache[n] = n*10000
		print("Calc.")
		return cache[n]

print(memorized(5))
print(memorized(5))
print(memorized(5))
print(memorized(5))
print(memorized(6))
print(memorized(6))
print(memorized(6))
print(memorized(5))
print(memorized(5))

 
#Simplified: 
print("\n.................\n")
cache = {}
def memorized(n):
	if n not in cache:
		print("Calc.")
		cache[n] = n*10000
	return cache[n]

print(memorized(3))
print(memorized(3))
print(memorized(3))
print(memorized(3))
print(memorized(7))
print(memorized(7))
print(memorized(7))
print(memorized(3))
print(memorized(3))