# Exercice 1
print("Hello world \n" "Hello world \n" "Hello world \n" "Hello world \n" )

#Exercice 2
print((99**3)*8)
"""
#Exercice 3
5<3
False
3==3
True
3=="3"
False
"3">3
False
"Hello"=="hello"
False
"""
#Exercice 4
computer_brand="hp"
print("I have a "+computer_brand+" computer")

#Exercice 5
name="DIMA"
age="23"
shoe_size="41"
info="Hello my name is "+name+", i have "+age+" years old and i wear size "+shoe_size
print(info)

#Exercise 6
a=float(input("Put number: \n"))
b=float(input("Put number: \n"))
if a>b:
	print("Hello World.")

#Exercise 7
nb=float(input("Put number: \n"))
if nb==0:
	print("This number is not odd not even \n")
elif nb%2==0:
	print("This number is odd \n")
else:
	print("This number is even \n")

#Exercise 8
name="DIMA"
user_name=input("What's your Name ? \n")
if user_name!=name:
	print("you forgot your name")
else:
	print("Well done, you have find")

#Exercise 9
height=float(input("Put your height in inches \n"))
if height*2.54 >145:
	print("You are tall enough to ride")
elif height*2.54 <145:
	print("You need to grow some to ride ")