def count_substring(string, sub_string):
	c = 0
	s = 0
	p = 0
	while s<len(string):
		p = string.find(sub_string, s)
		if p != -1:
			c = c+1
			s = p+1
		else:
			break
	return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)