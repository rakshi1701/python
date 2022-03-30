class art:
	def __init__(s):
		s.l1=[]
	def add(s):
		n=input('\n enter the number of elemants ')
		if (n.isalpha()):
			print("\n invalid entry enter integer value ")
			s.add()
		else:
			for i in range(0,int(n)):
				ele=input("\n enter the elements to be added ")
				if (ele.isdigit()):
					s.l1.append(int(ele))

				else:
					print("----------------")
					ele=int(input("\n enter the integer value "))
					s.l1.append(ele)

			print(s.l1)
	def __add__(s,ot):
		l2=[]
		for i in range(0,len(s.l1)):
			l2.append(s.l1[i] + ot.l1[i])
		print("addition of lists ",l2)

	def __sub__(s,ot):
		l2=[]
		for i in range(0,len(s.l1)):
			l2.append(s.l1[i] - ot.l1[i])
		print("Subraction of lists ",l2)

	def __mul__(s,ot):
		l2=[]
		for i in range(0,len(s.l1)):
			l2.append(s.l1[i] * ot.l1[i])
		print("Multiplication of lists ",l2)

	def __floordiv__(s,ot):
		l2=[]
		for i in range(0,len(s.l1)):
			l2.append(s.l1[i] // ot.l1[i])
		print("Floor Division of lists ",l2)

