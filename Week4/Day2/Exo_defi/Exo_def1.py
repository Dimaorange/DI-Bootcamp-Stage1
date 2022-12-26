#Def1
#1.
"""
number=int(input("Enter a number:\n"))
length=int(input("Enter number length:\n"))
#2.
i=1
while i <=length:
	print(f"{i*number}")
	i+=1
"""
#Defi 2
chain1=input("Enter a chaine:\n")
result=chain1
for i in chain1:
	result=result.replace(i+i,i)
print(result)