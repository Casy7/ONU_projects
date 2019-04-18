w=0
d=0
l=0
i=0
while i<5:
	p=input("rock (r), paper (p) or scissors (s)? ").lower()
	from random import randint
	computer=randint(1,3)
	c=0
	if(computer==1):
		c="r"
	elif(computer==2):
		c="p"
	else:
		c="s"
	if(p=="r" or p=="s" or p=="p"):
		if(c==p):
			d+=1
			print(c)
			print("Draw")		
		elif((c=="r" and p=="s") or (c=="s" and p=="p") or (c=="p" and p=="r")):
			l+=1
			print(c)
			print("You lose")	
		else:
			w+=1
			print(c)
			print("You win")
		i+=1
	else:
		print("Error by entering")
print("Победа".ljust(14)+"Победа".ljust(14)+"Ничья"+"\nИгрока".ljust(14)+"Компьютера")
print((str(w)).ljust(14)+((str(l)).ljust(14)+str(d)))