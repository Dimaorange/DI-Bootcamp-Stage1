#Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
for item in zip(keys,values):
	print(item)

#Exercise 2
#2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
3.La somme que chaque membre de la famille doit payer:
rick=15$
beth=15$
morty=10$
summer=10$
#4.
som=0
for name ,age in family.items():
	if 3<age<12:
		som+=10
	elif age>=12:
		som+=15
print(f"Le coût total de la famille pour les films est:{som}")

#4.
family={}
name=input("Entre une clé du dictionnaire ou quit pour quitter:\n")
if name !="quit":
	age=int(input(f"Entre l'age de {name}:\n"))
	family.update({name:age})
	while name !="quit":
		name=input("Entre une clé du dictionnaire ou quit pour quitter:\n")
		if name == "quit":
			break
		age=int(input(f"Entre l'age de {name}:\n"))
		family.update({name:age})
print(family)

#Exercise 3
#2.
brand={
	"name":"Zara",
	"creation_date":1975,
	"creator_name":"Amancio Ortega Gaona",
	"type_of_clothes":["men","women","children","home"],
	"international_competitors":["Gap","H&M","Benetton"],
	"number_stores":7000,
	"major_color":{"France":"blue","Spain":"red","US":["pink","green"]}
}
#3.
brand["number_stores"]="2"
#4.
print("Les clients de Zara sont:",brand["type_of_clothes"][:])
#5.
brand.update({"country_creation":"Spain"})
#6.
for cle in brand:
	if cle=="international_competitors":
		brand["international_competitors"].append("Desigual")
print(brand)
#7.
del brand["creation_date"]
#8.
print(brand["international_competitors"][-1])
#9.
print(brand["major_color"]["US"][:])
#10.
print(len(brand))
#11.
print(brand.keys())
#12.
more_on_zara={"creation_date":1975,"number_stores":10000}
#13.
brand.update({"creation_date":1975,"number_stores":10000})
#14.
print(brand["number_stores"])
#La valeur de la clé number_stores est changé de 7000 à 10000

#Exercise 4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
#1.
disney_users_A={}
for index_count,name in enumerate(users):
	disney_users_A.update({name:index_count})
print(disney_users_A)
#2.
disney_users_B={}
for index_count,name in enumerate(users):
	disney_users_B.update({index_count:name})
print(disney_users_B)
#3.
disney_users_C={}
list(users)
users=sorted(users)
for index_count,name in enumerate(users):
	disney_users_C.update({name:index_count})
print(disney_users_C)
#4.1.
nouv={}
for index_count,name in enumerate(users):
	if "i" in name:
		nouv.update({name:index_count})
print(nouv)
#4.2.
nv={}
for index_count,name in enumerate(users):
	#list(users)
	i=0
	while i<len(users):
		if name[0]=="M" or name[0]=="P":
			nv.update({name:index_count})
		i+=1
print(nv)