#Exercise 1
#1.
my_fav_numbers={"+22663944821","+22666939120"}
#2.
my_fav_numbers.add("+22678388911")
my_fav_numbers.add("+22678488372")
#3.
my_fav_numbers.discard("+22678488372")
#4.
friend_fav_numbers={"+22670700334","+22670461173","+22670176714"}
#5.
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)

#Exercise 2
#1. It is not possible to add item because tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

#Exercise 3
basket=["Banana","Apples","Oranges","Blueberries"]
#1.
basket.remove("Banana")
#2.
basket.remove("Blueberries")
#3.
basket.append("Kiwi")
#4.
basket.insert(0,"Apples")
#5.
nb=basket.count("Apples")
#6.
basket.clear()
#7.
for i in basket:
	print(i)

#Exercise 4
#1.Un float represente l'ensemble des nombres à virgule et sans virgule. Un entier n'a pas de virgule tandisque qu'un nombre flottant peut avoir une virgule.

#2.Nous pouvons obtenir aussi une séquence de flottants à partir de la convertion d'une liste de type int en type float.

#3.
liste_seq=[]
i=1
while i<5:
	i+=0.5
	liste_seq.append(f"{i}")
print(liste_seq)

#Exercise 5
#1.
for i in list(range(1,21)):
	print(i)
#2.
liste=list(range(1,21))
for i in range(1,21):
	if i%2==0:
		print(liste[i])

#Exercise 6
#1.
name=input("What is your name:\n")
while name!="DIMA":
	name=input("What is your name:\n")

#Exercise 7
#1.
fruit=input("Enter their favorite fruit(s), one or several fruits. separate the fruits with a single space, eg: apple mango cherry:\n")
#2.
liste=fruit.split(" ")
#3.
name_fruit=input("Enter a fruit:\n")
if name_fruit in liste:
	print("You chose one of your favorite fruits! Enjoy!")
else:
	print("You chose a new fruit. I hope you enjoy.")

#Exercise 8
liste_pizza=[]
prix=10
liste_piz=input("Enter a series of pizza toppings or quit for stopped:\n")
while liste_piz !="quit":
	prix=prix+2.5
	print(f"you’ll add that {liste_piz} to their pizza.")
	liste_piz=liste_piz.split(" ")
	liste_pizza=liste_pizza+liste_piz
	liste_piz=input("Enter a series of pizza toppings or quit for stopped:\n")
print(f"{liste_pizza} \n {prix}")

#Exercise 9
#1.
nb=int(input("Enter the number of person would need ticket in family:\n"))
#2.
i=0
somme=0
while i<nb:
	age=int(input("Enter old of person concerned:\n"))
	if age<3:
		ticket=0
	elif 3<=age<12:
		ticket=10
	else:
		ticket=15
	somme=somme+ticket
	i=i+1
#3.
print(f"The total cost of all the family’s tickets is :{somme}$")
#4.
liste_name=["John","Nestor","Daoud","Malgue1deba","Constantin"]
i=0
while i<len(liste_name):
	age_per=int(input(f"{liste_name[i]} how old are you:\n"))
	if age_per<16:
		liste_name.remove(f"{liste_name[i]}")
		i=i
	else:
		i=i+1
print(liste_name)

#Exercise 10
#1.
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
#2.
finished_sandwiches=[]
#3.
i=0
while len(sandwich_orders)!=0:
	for san in sandwich_orders:
		rep=input(f"Input yes or 1 if {san} is:\n")
		if rep=="yes" or rep=="1":
			finished_sandwiches.append(f"{sandwich_orders.pop(sandwich_orders.index(san))}")
#4.
for san in finished_sandwiches:
	print(f"I made your {san}.")

#Exercise 11
#1.
while sandwich_orders.count("Pastrami sandwich")<3:
	sandwich_orders.append("Pastrami sandwich")
#2.
print("The deli has run out of pastrami.")
i=0
while i<len(sandwich_orders):
	if sandwich_orders[i]=="Pastrami sandwich":
		sandwich_orders.remove(f"{sandwich_orders[i]}")
		i=i
	else:
		i=i+1
#3.
print(sandwich_orders)