from art import *

ob1=art()
ob2=art()

while(1):
	print("\n 0.exit \n 1.Add list")
	ch1=int(input("enter the choice"))
	if ch1==0:
		exit()
	if ch1==1:
		ob1.add()
		ob2.add()
		if len(ob1.l1) == len(ob2.l1):
			while(1):
				print("\n 0.exit \n 1.addition \n 2.subraction \n 3.Multiplication \n 4.Floor Division")
				ch2=int(input("enter the choice"))
				if ch2==0:
					break
				if ch2==1:
					ob1 + ob2
				if ch2==2:
					ob1 - ob2
				if ch2==3:
					ob1 * ob2
				if ch2==4:
					ob1 // ob2
		else:
			print("Number of elements in the both list have to be same")
			ob1=art()
			ob2=art()
