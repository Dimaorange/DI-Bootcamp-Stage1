chaine=input("Put a string to 10 characters long: \n")
if len(chaine)<10:
	print("string not long enough")
elif len(chaine)>10:
	print("string too long")

print(chaine[0]+" "+chaine[-1])

a=""
for i in chaine:
	a=a+i
	print(a)
	
import random as r
chaine1=list(chaine)
r.shuffle(chaine1)
tata="".join(chaine1)
print(tata)