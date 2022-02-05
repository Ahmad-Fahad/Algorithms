def Insertion_Sort(lst):
	l = len(lst)
	for i in range(1,l):
		temp = lst[i]
		j = i-1
		while j>=0:
			if temp[0]<lst[j][0]:
				lst[j+1] = lst[j]
				lst[j]   = temp
			j = j-1
	return lst

lst = []
lst   = ['Tininha', 'Dudinha','Carlinhos','Marquinhos','Joaozinho','Bruninha','Fernandinha','Rafinha','Pedrinho','Aninha','Tamirinha','Gaguinho','Zezinho','Luquinhas','Julhinha']
print(Insertion_Sort(lst))
lst_1 = ['Tininha', 'Dudinha','Carlinhos','Marquinhos','Joaozinho','Bruninha','Fernandinha','Rafinha','Pedrinho','Aninha','Tamirinha','Gaguinho','Zezinho','Luquinhas','Julhinha']
lst_1.sort() # sort() will sort it in alphabetic order
print(lst_1)
lst_1.sort(reverse = True) # sort() will sort it in alphabetic DSC order
print(lst_1)
lst_1.sort(key = len) # sort() will sort it according to length
print(lst_1)
