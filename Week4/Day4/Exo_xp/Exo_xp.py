#Exercice 1
#1.
def display_message():
	print("Nous allons apprendre dans ce cours l'utilisation des fonctions dans les programmes.")
#2.
display_message()

#Exercice 2
def favorite_book(titre):
	print(f"Mon meilleur livre est {titre}.")

titre="Le soleil des indépendances"
favorite_book(titre)

#Exercice 3
def describe_city(city,country):
	print(f"{city} is in {country}")
city="Ouagadougou"
country="Burkina Faso"
describe_city(city,country)

#Exercice 4
import random as r
nb=int(input("Entre un nombre compris entre 0 et 100:\n"))
while nb<1 or nb>100:
	nb=int(input("Entre un nombre compris entre 0 et 100:\n"))
liste=list(range(1,101))
r.shuffle(liste)
nob=liste.pop()
if nb==nob:
	print("Succès")
else:
	print(f"Echec {nb} et {nob}")

#Exercice 5
#1.
def make_shirt(size,text):
	print(f"The size of the shirt is {size} and the text is {text}")

size="L"
text="I am a africa people"
make_shirt(size,text)

def make_shirt(size="XL",text="I like python"):
	print(f"The size of the shirt is {size} and the text is {text}")

size="XXL"
make_shirt(size)

size="M"
make_shirt(size)

size="S"
text="Yes we can !"
make_shirt(size,text)

args=["XXXL","Welcome"]
make_shirt(*args)

#Exercice 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magician_n):
	for name in magician_n:
		print(name)
show_magicians(magician_names)

def make_great(liste):
	n=0
	for i in liste:
		liste[n]=i+" the great"
		n+=1
	print(liste)

make_great(magician_names)

show_magicians(magician_names)

#Exercice 7
def get_random_temps(saison):
	import random as r 
	liste=list(range(-10,41))
	r.shuffle(liste)
	elem=liste.pop()
	if saison.lower()=="hiver":
		while elem not in list(range(-10,17)):
			r.shuffle(liste)
			elem=liste.pop()
	elif saison.lower() =="automne":
		while elem not in list(range(17,23)):
			r.shuffle(liste)
			elem=liste.pop()
	elif saison.lower()=="printemps":
		while elem not in list(range(23,30)):
			r.shuffle(liste)
			elem=liste.pop()
	elif saison.lower()=="été":
		while elem not in list(range(30,41)):
			r.shuffle(liste)
			elem=liste.pop()
	return elem

#print(get_random_temps())
def main():
	a=float(get_random_temps(saison))
	print(f"La température actuelle est de {a} degrés Celsius.")
	if a<=0:
		print("C'est glacial! Portez des couches supplémentaires aujourd'hui")
	elif 0<a<=16:
		print("Assez froid! N'oubliez pas votre manteau")
	elif 16<a<=23:
		print("C'est froid! N'oubliez pas votre manteau au cas où la temperature baisse")
	elif 24<=a<=32:
		print("Il fait beau temps!")
	else:
		print("Il fait chaud!")

enum={"1":"janvier","2":"février","3":"mars","4":"avril","5":"mai","6":"juin","7":"juillet","8":"août","9":"septembre","10":"octobre","11":"novembre","12":"décembre"}
saison_an={"hiver":["décembre","janvier","février"],"automne":["septembre","octobre","novembre"],"printemps":["juin","juillet","août"],"été":["mars","avril","mai"]}
def mois(enum,saison_an):
	num=input("Entrez le numéro du mois:\n")
	mot=enum[num]
	i=0
	while len(saison_an)>0:
		for sai in saison_an:
			if mot in saison_an[sai]:
				return sai
			else:
				i+=1

saison=mois(enum,saison_an)
main()